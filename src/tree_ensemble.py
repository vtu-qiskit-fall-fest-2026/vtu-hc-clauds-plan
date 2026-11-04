"""Dependency-free inference for trained LightGBM / XGBoost binary classifiers.

LightGBM and XGBoost ship native libraries (LightGBM needs OpenMP's
``libgomp.so.1``; XGBoost wheels are 100+ MB with CUDA). Serverless hosts such
as Vercel can't load them, so after training we export the boosted trees into
flat NumPy arrays and score them here with the same decision rules, so
production inference needs only NumPy.

Decision rules reproduced exactly:
* LightGBM: go left when ``x <= threshold`` (float64).
* XGBoost:  go left ("yes") when ``float32(x) < float32(threshold)``;
  the raw margin starts at ``logit(base_score)``.
"""

import json
import math

import numpy as np


class TreeEnsembleClassifier:
    """Pure-NumPy replica of a LightGBM / XGBoost binary ``predict_proba``."""

    def __init__(self, trees: list[dict], n_features: int, base_margin: float = 0.0,
                 rule: str = "le", source: str = "lightgbm"):
        self.trees = trees
        self.n_features = n_features
        self.base_margin = base_margin
        self.rule = rule  # "le" (LightGBM, float64) or "lt32" (XGBoost, float32)
        self.source = source
        self.classes_ = np.array([0, 1])

    def __setstate__(self, state):
        # Models pickled before XGBoost support lack these attributes.
        state.setdefault("base_margin", 0.0)
        state.setdefault("rule", "le")
        state.setdefault("source", "lightgbm")
        self.__dict__.update(state)

    @classmethod
    def from_xgboost(cls, model) -> "TreeEnsembleClassifier":
        """Build from a fitted ``xgboost.XGBClassifier`` (binary:logistic)."""
        booster = model.get_booster() if hasattr(model, "get_booster") else model
        cfg = json.loads(booster.save_config())["learner"]
        objective = cfg["objective"]["name"]
        if objective != "binary:logistic":
            raise ValueError(f"Only binary:logistic is supported, got {objective!r}")
        base_score = float(str(cfg["learner_model_param"]["base_score"]).strip("[]"))
        base_margin = math.log(base_score / (1.0 - base_score))
        trees = [cls._flatten_xgb(json.loads(t)) for t in booster.get_dump(dump_format="json")]
        n_features = int(cfg["learner_model_param"]["num_feature"])
        return cls(trees, n_features, base_margin=base_margin, rule="lt32", source="xgboost")

    @staticmethod
    def _flatten_xgb(root: dict) -> dict:
        feature, threshold, left, right, value, default_left = [], [], [], [], [], []

        def visit(node: dict) -> int:
            idx = len(feature)
            feature.append(-1)
            threshold.append(0.0)
            left.append(-1)
            right.append(-1)
            value.append(0.0)
            default_left.append(True)
            if "leaf" in node:
                value[idx] = float(node["leaf"])
                return idx
            children = {c["nodeid"]: c for c in node["children"]}
            feature[idx] = int(str(node["split"]).lstrip("f"))
            threshold[idx] = float(node["split_condition"])
            default_left[idx] = node["missing"] == node["yes"]
            left[idx] = visit(children[node["yes"]])
            right[idx] = visit(children[node["no"]])
            return idx

        visit(root)
        return {
            "feature": np.array(feature, dtype=np.int32),
            "threshold": np.array(threshold, dtype=np.float32).astype(np.float64),
            "left": np.array(left, dtype=np.int32),
            "right": np.array(right, dtype=np.int32),
            "value": np.array(value, dtype=np.float64),
            "default_left": np.array(default_left, dtype=bool),
        }

    @classmethod
    def from_lightgbm(cls, model) -> "TreeEnsembleClassifier":
        """Build from a fitted ``lightgbm.LGBMClassifier`` (or ``Booster``)."""
        booster = model.booster_ if hasattr(model, "booster_") else model
        dump = booster.dump_model()
        objective = str(dump.get("objective", ""))
        if not objective.startswith("binary"):
            raise ValueError(f"Only binary objectives are supported, got {objective!r}")
        if "sigmoid:" in objective and not objective.endswith("sigmoid:1"):
            raise ValueError(f"Only sigmoid:1 is supported, got {objective!r}")
        trees = [cls._flatten(t["tree_structure"]) for t in dump["tree_info"]]
        return cls(trees, int(dump["max_feature_idx"]) + 1)

    @staticmethod
    def _flatten(root: dict) -> dict:
        feature, threshold, left, right, value, default_left = [], [], [], [], [], []

        def visit(node: dict) -> int:
            idx = len(feature)
            feature.append(-1)
            threshold.append(0.0)
            left.append(-1)
            right.append(-1)
            value.append(0.0)
            default_left.append(True)
            if "leaf_value" in node and "split_feature" not in node:
                value[idx] = float(node["leaf_value"])
                return idx
            if node.get("decision_type", "<=") != "<=":
                raise ValueError(f"Unsupported split type {node.get('decision_type')!r}")
            feature[idx] = int(node["split_feature"])
            threshold[idx] = float(node["threshold"])
            default_left[idx] = bool(node.get("default_left", True))
            left[idx] = visit(node["left_child"])
            right[idx] = visit(node["right_child"])
            return idx

        visit(root)
        return {
            "feature": np.array(feature, dtype=np.int32),
            "threshold": np.array(threshold, dtype=np.float64),
            "left": np.array(left, dtype=np.int32),
            "right": np.array(right, dtype=np.int32),
            "value": np.array(value, dtype=np.float64),
            "default_left": np.array(default_left, dtype=bool),
        }

    def decision_function(self, X) -> np.ndarray:
        X = np.asarray(X, dtype=np.float64)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        if self.rule == "lt32":
            # XGBoost compares float32 features against float32 thresholds.
            X = X.astype(np.float32).astype(np.float64)
        rows = np.arange(len(X))
        raw = np.full(len(X), self.base_margin)
        for t in self.trees:
            node = np.zeros(len(X), dtype=np.int32)
            while True:
                feat = t["feature"][node]
                internal = feat >= 0
                if not internal.any():
                    break
                x = X[rows, np.where(internal, feat, 0)]
                thr = t["threshold"][node]
                split = x < thr if self.rule == "lt32" else x <= thr
                go_left = np.where(np.isnan(x), t["default_left"][node], split)
                nxt = np.where(go_left, t["left"][node], t["right"][node])
                node = np.where(internal, nxt, node)
            raw += t["value"][node]
        return raw

    def predict_proba(self, X) -> np.ndarray:
        p = 1.0 / (1.0 + np.exp(-self.decision_function(X)))
        return np.column_stack([1.0 - p, p])

    def predict(self, X) -> np.ndarray:
        return (self.predict_proba(X)[:, 1] >= 0.5).astype(int)
