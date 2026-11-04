"""Dependency-free inference for trained LightGBM binary classifiers.

LightGBM's Python package loads a native library that needs OpenMP
(``libgomp.so.1``). Serverless hosts such as Vercel don't ship it, so
unpickling an ``LGBMClassifier`` fails there. After training we export the
booster's trees into flat NumPy arrays and score them here with the same
decision rules, so production inference needs only NumPy.
"""

import numpy as np


class TreeEnsembleClassifier:
    """Pure-NumPy replica of a LightGBM binary ``predict_proba``."""

    def __init__(self, trees: list[dict], n_features: int):
        self.trees = trees
        self.n_features = n_features
        self.classes_ = np.array([0, 1])

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
        rows = np.arange(len(X))
        raw = np.zeros(len(X))
        for t in self.trees:
            node = np.zeros(len(X), dtype=np.int32)
            while True:
                feat = t["feature"][node]
                internal = feat >= 0
                if not internal.any():
                    break
                x = X[rows, np.where(internal, feat, 0)]
                go_left = np.where(np.isnan(x), t["default_left"][node], x <= t["threshold"][node])
                nxt = np.where(go_left, t["left"][node], t["right"][node])
                node = np.where(internal, nxt, node)
            raw += t["value"][node]
        return raw

    def predict_proba(self, X) -> np.ndarray:
        p = 1.0 / (1.0 + np.exp(-self.decision_function(X)))
        return np.column_stack([1.0 - p, p])

    def predict(self, X) -> np.ndarray:
        return (self.predict_proba(X)[:, 1] >= 0.5).astype(int)
