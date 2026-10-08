from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiment import CLASSES, FEATURES, build_pipeline, evaluate, load_data, tss_ovr
from fetch_upstream import GIT_BLOB_SHA1, verify_git_blob


def synthetic_data() -> pd.DataFrame:
    rng = np.random.default_rng(123)
    n = 120
    return pd.DataFrame({
        **{col: rng.normal(loc=i, size=n) for i, col in enumerate(FEATURES)},
        "target": list(CLASSES) * 30,
        "AR": [str(i // 4) for i in range(n)],
        "timestamp": pd.date_range("2020-01-01", periods=n, freq="D"),
    })


def test_blob_verification_rejects_unrelated_data():
    assert len(GIT_BLOB_SHA1) == 40
    assert not verify_git_blob(b"not the original GitHub CSV")


def test_load_data_and_schema(tmp_path: Path):
    d = synthetic_data()
    raw = d.loc[:, FEATURES].copy()
    raw.insert(0, "AR", d["AR"])
    raw.insert(0, "Flare Date", d["timestamp"].dt.strftime("%-m/%-d/%Y %H:%M"))
    raw.insert(0, "Flare Class", d["target"] + "12")
    path = tmp_path / "test.csv"
    raw.to_csv(path, index=False)
    loaded = load_data(path, verify_upstream=False)
    assert len(loaded) == 120
    assert set(loaded.target) == set(CLASSES)
    with pytest.raises(ValueError, match="reference dataset"):
        load_data(path, verify_upstream=True)


def test_score_exact_prediction():
    y = np.array(list(CLASSES) * 3)
    per_class = tss_ovr(y, y)
    assert all(x == 1.0 for x in per_class.values())


@pytest.mark.parametrize("sampling", ["none", "under", "smote"])
def test_fold_safe_train_and_evaluate(sampling: str):
    df = synthetic_data()
    output = evaluate(df, sampling=sampling, folds=3)
    assert output["analysis"].startswith("NEW POST-MSC")
    assert len(output["folds"]) == 3
    assert all(0 <= z["balanced_accuracy"] <= 1 for z in output["folds"])
    estimator = build_pipeline("extra_trees", sampling, 10)
    if sampling != "none":
        assert "sampler" in estimator.named_steps


def test_chronological_holdout():
    result = evaluate(synthetic_data(), mode="chronological")
    assert len(result["folds"]) == 1
    assert result["folds"][0]["train_size"] == 96
    assert result["folds"][0]["test_size"] == 24
