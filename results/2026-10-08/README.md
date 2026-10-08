# Verified new 2026 research results: permanent small-format extract

This folder fixes the **essential reported values** in Git history so application reviewers are not dependent on GitHub Actions artifact-retention periods.

- [Seed-42 baseline summary](seed42_baselines.csv): 18 configurations (2 models × 3 training-fold sampling variants × 3 validations), values from the verified real-dataset run.
- [2014-start chronological sensitivity](temporal_2014_sensitivity.csv): six **post-hoc** model/sampling comparisons; the test uses only nine X-class observations and removes one overlapping-AR event.
- Full-precision per-fold metrics, diagnostics, alternative seed checks and Python environment capture: [successful GitHub Actions run](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/runs/37823855291) and the scripts [sweep.py](../../corrected_classical_ml/reconstruction_2026/sweep.py), [sweep_extensions.py](../../corrected_classical_ml/reconstruction_2026/sweep_extensions.py).
- Method-level interpretation: [complete audit](../../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md).

**Input (not redistributed):** upstream `ccsc-tools/FlareML` original CSV at commit `44ffd7ad0a6945ee36f6e488a034b8266cb4fb4c`; Git blob `d3c40b44220b4480e0a600314cae46175cd9d127`; input SHA-256 `69c36526144f5d1485b7f8cc55b254c857c885a840020fe3cb2b887f4c4f8cd3`.

### Interpretation is part of the result

- `sklearn_macro_recall` is **not** the thesis metric. `thesis_four_class_ovr_BACC` is the average of four per-class one-vs-rest BACC scores, not scikit-learn's balanced_accuracy_score.
- A blank four-class value in the 80/20 chronological rows means **undefined** because there are no X-class events in the test partition. It is not a zero and must not be imputed.
- These are new 2026 **exploratory**, cross-validation or post-hoc findings, not the exact 2024 thesis experiments and not deployed or externally validated predictions.
- Artifact run logs and full-precision CSVs take precedence over any rounded explanatory text here. No significance tests were performed.

**To reproduce:** in `corrected_classical_ml/reconstruction_2026/`, install `requirements.txt`; run `python fetch_upstream.py`, `python -m pytest -q`, `python sweep.py` and `python sweep_extensions.py`.
