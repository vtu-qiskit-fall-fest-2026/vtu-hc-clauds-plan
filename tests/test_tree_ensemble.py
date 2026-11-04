"""Tests for domain-only model input and the pure-NumPy LightGBM export."""

import pickle

import numpy as np
import pytest

from src.features import extract_features, model_input_url
from src.tree_ensemble import TreeEnsembleClassifier


@pytest.mark.parametrize(
    "url, expected",
    [
        ("https://en.wikipedia.org/wiki/Phishing", "https://en.wikipedia.org"),
        ("http://paypa1-verify.com/signin?id=1&token=x", "http://paypa1-verify.com"),
        ("http://user@evil.com:8081/a#frag", "http://user@evil.com:8081"),
        ("example.com/path", "http://example.com"),
        ("", ""),
    ],
)
def test_model_input_url_keeps_scheme_and_authority_only(url, expected):
    assert model_input_url(url) == expected


def test_pages_on_same_site_get_identical_model_features():
    a = extract_features(model_input_url("https://en.wikipedia.org"))
    b = extract_features(model_input_url("https://en.wikipedia.org/wiki/Quantum_computing"))
    assert a == b


def test_tree_ensemble_matches_lightgbm_exactly():
    lgb = pytest.importorskip("lightgbm")
    rng = np.random.default_rng(0)
    X = rng.normal(size=(400, 6))
    y = (X[:, 0] + 0.5 * X[:, 1] ** 2 - X[:, 2] > 0.3).astype(int)
    clf = lgb.LGBMClassifier(n_estimators=40, num_leaves=15, verbose=-1, random_state=0).fit(X, y)

    exported = TreeEnsembleClassifier.from_lightgbm(clf)
    X_new = rng.normal(size=(200, 6))
    np.testing.assert_allclose(
        exported.predict_proba(X_new), clf.predict_proba(X_new), rtol=0, atol=1e-9
    )


def test_tree_ensemble_pickles_without_lightgbm_classes():
    lgb = pytest.importorskip("lightgbm")
    rng = np.random.default_rng(1)
    X = rng.normal(size=(200, 3))
    y = (X[:, 0] > 0).astype(int)
    clf = lgb.LGBMClassifier(n_estimators=10, verbose=-1).fit(X, y)
    blob = pickle.dumps(TreeEnsembleClassifier.from_lightgbm(clf))
    assert b"lightgbm" not in blob
    restored = pickle.loads(blob)
    assert restored.predict_proba(X).shape == (200, 2)


def test_saved_production_model_loads_and_predicts_without_lightgbm():
    """Simulate a host where lightgbm can't be imported (e.g. Vercel, no libgomp)."""
    import subprocess
    import sys
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    code = (
        "import sys; sys.modules['lightgbm'] = None\n"
        "from src.model import load_model, predict_url\n"
        "b = load_model()\n"
        "r = predict_url('https://en.wikipedia.org/wiki/Phishing', clf=b.clf, scaler=b.scaler, threshold=b.threshold)\n"
        "assert r['label'] == 0, r\n"
        "r = predict_url('http://paypa1-verify.com/signin', clf=b.clf, scaler=b.scaler, threshold=b.threshold)\n"
        "assert r['label'] == 1, r\n"
        "print('ok')\n"
    )
    out = subprocess.run([sys.executable, "-c", code], cwd=root, capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    assert out.stdout.strip() == "ok"
