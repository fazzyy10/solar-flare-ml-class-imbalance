# Real-data audit — DeepSun/FlareML reconstruction, 8 October 2026

> **Status: new post-MSc exploratory analysis.** This is not the original assessed 2024 implementation, not an independent replication of its 29,400 reported model tests, and not an estimate of operational forecasting performance. The results below are from a public upstream source with traceable input integrity and GitHub Actions execution.

## Data provenance and verification

| Property | Verified value |
|---|---|
| Source | [ccsc-tools/FlareML](https://github.com/ccsc-tools/FlareML), Yasser Abduallah, Jason T. L. Wang and Haimin Wang |
| Pinned commit | `44ffd7ad0a6945ee36f6e488a034b8266cb4fb4c` |
| CSV | `data/original_data/flaringar_original_data.csv` |
| Git blob SHA-1 | `d3c40b44220b4480e0a600314cae46175cd9d127` |
| SHA-256 of verified raw CSV | `69c36526144f5d1485b7f8cc55b254c857c885a840020fe3cb2b887f4c4f8cd3` |
| Events / active regions / SHARP predictors | 845 / 472 / 13 |
| B / C / M / X | 128 / 552 / 142 / 23 |
| Missing numeric fields / exactly duplicate CSV rows | 0 / 0 |
| Active regions with 2+ events | 206 |
| Active regions containing different flare classes | 0 |

The upstream public original CSV has **raw-scale measurements**, not solely 0–1-normalised features. Agreement of its row, region and class counts with the submitted thesis **does not establish** that this was the exact preprocessed local matrix used in 2024.

## Experimental protocol

- **New Python code**, not the upstream FlareML application or the missing 2024 code.
- Fixed 13 SHARP predictors, target mapped to B/C/M/X, no `AR`, date or original flare class string used as model features.
- Extra Trees and Random Forest, each with 150 trees and `n_jobs=1`.
- No resampling; RandomUnderSampler; or SMOTE with `k_neighbors=3`, fitted **inside each training fold** along with the scaler.
- Stratified five-fold CV; active-region-grouped five-fold CV; chronological 80/20 holdout.
- Initial random seed 42. Repeated sensitivity seeds 73 and 2024 for both cross-validation protocols.
- Metrics are calculated according to the **submitted dissertation's equations**: for each class vs all others, `BACC=(TPR+TNR)/2` and `TSS=TPR-FPR`, then mean across B/C/M/X.
- We separately retain scikit-learn multiclass `balanced_accuracy_score`, which is macro recall and **not** the thesis's four-class one-vs-rest metric.
- If a held-out fold contains no event for any target class, the four-class BACC/TSS is recorded as **undefined**, not averaged over fewer classes.

## Initial 18-configuration matrix: thesis-defined BACC (seed 42)

| Model | Training resampling | Stratified 5-fold | Grouped 5-fold |
|---|---|---:|---:|
| Extra Trees | None | 0.6810 | 0.6108 |
| Extra Trees | Random undersampling | 0.6902 | 0.6769 |
| Extra Trees | SMOTE | 0.7071 | 0.6413 |
| Random Forest | None | 0.6583 | 0.6150 |
| Random Forest | Random undersampling | 0.7021 | 0.6705 |
| Random Forest | SMOTE | 0.6996 | 0.6380 |

All 18 model × sampling × validation-mode configurations executed without runtime failures. The six original chronological 80/20 test configurations have **undefined four-class BACC/TSS** because the last 169 events (April 2015 to December 2016) contain **zero X-class events**.

**Split audit:** Ordinary stratified CV had 88–93 active-region IDs shared by training and test in each fold; grouped CV had zero in every fold. These overlaps identify a dependence issue; the observed score differences cannot be assigned exclusively to leakage because group splits also change class composition and difficulty.

## Three-seed sensitivity: mean BACC across seeds 42, 73 and 2024

| Model | Sampling | Stratified mean (range) | Grouped mean (range) |
|---|---|---|---|
| Extra Trees | None | 0.6878 (0.6810–0.7000) | 0.6177 (0.6108–0.6279) |
| Extra Trees | Under | 0.6778 (0.6701–0.6902) | 0.6749 (0.6549–0.6930) |
| Extra Trees | SMOTE | 0.7066 (0.7018–0.7108) | 0.6425 (0.6413–0.6449) |
| Random Forest | None | 0.6720 (0.6583–0.6825) | 0.6247 (0.6150–0.6352) |
| Random Forest | Under | 0.6871 (0.6724–0.7021) | 0.6708 (0.6608–0.6811) |
| Random Forest | SMOTE | 0.7094 (0.6996–0.7159) | 0.6391 (0.6364–0.6428) |

Grouping reduced BACC in **17 of 18** seed-matched comparisons. The exception was Extra Trees with undersampling, seed 73 (stratified 0.6730; grouped 0.6930). Three seeds are a limited descriptive sensitivity check, not a confidence interval or hypothesis test.

## Alternative chronological holdout with four classes

To evaluate all four flare types temporally, we additionally examined a 1 January 2014 cutoff (selected *after* seeing that the 80/20 split lacked X cases). We trained on **481** pre-2014 observations and tested on **363** post-2013 observations, excluding the one later observation of active region 11936 also represented in training. The test contains B, C, M and **nine X-class** events.

| Model | Sampling | Four-class BACC | Four-class TSS |
|---|---|---:|---:|
| Extra Trees | None | 0.6872 | 0.3744 |
| Extra Trees | Under | 0.7026 | 0.4053 |
| Extra Trees | SMOTE | 0.6995 | 0.3991 |
| Random Forest | None | 0.6826 | 0.3652 |
| Random Forest | Under | 0.7023 | 0.4046 |
| Random Forest | SMOTE | 0.7025 | 0.4050 |

This is an **exploratory, post-hoc sensitivity split**, not a locked independent final test. Its nine X-class cases make rare-event conclusions especially uncertain.

## Comparison with the submitted 2024 dissertation

The submitted MSc thesis reports **Extra Trees mean BACC 0.829979** and **TSS 0.659958** in its historical results. Those values satisfy `TSS = 2×BACC−1`. The 2026 code verified that same metric identity at floating-point tolerance across evaluable folds.

A claim that the thesis score was reproduced, invalidated, or reduced by exactly a given amount would **not** be supported. The new experiment differs in fold grouping, 5 rather than 10 folds, sampling placement, 150-tree hyperparameters, number of resampling repetitions (not 100), seeds, software versions and unknown aspects of the lost 2024 environment.

### What the new work establishes

1. The public dataset can be obtained repeatably from a pinned upstream commit, checked cryptographically and validated against the thesis's published class/region counts.
2. A new, independent, fold-safe comparative pipeline executes correctly on those records.
3. Repeated active-region dependencies materially affect validation outcomes, making AR-separated and temporal evaluations essential in future studies.
4. The 2015–2016 chronological holdout lacks X events and is unsuitable for a four-class summary.
5. This small, event-only data source and the limited X-class sample are insufficient grounds for claims about reliable real-time solar-flare forecasting.

### Remaining scientific limitations

- Exact submitted 2024 notebook, input transformation, model hyperparameters and environment were not recovered.
- Public source may not equal the precise 2024 transformed input matrix.
- No separate model-selection set, external dataset, or prospectively locked test set has been assessed.
- Potential temporal shift, sampling dependencies and AR composition mean validation results are not interchangeable.
- **No formal inferential statistics or operational reliability claims** are made.
- The only benchmarked classifiers here are Extra Trees and Random Forest, not all 14 original MSc classifiers.

## Machine-readable evidence

[GitHub Actions successful expanded audit run](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/runs/37823855291) contains downloadable artifacts with:
`data_profile.json`, `split_diagnostics.json`, `matrix_summary.csv`,
`fold_metrics.csv`, `seed_sensitivity_extra.csv`,
`2014_chronological_holdout.csv`, the per-configuration JSON records,
exact package versions and source-file SHA-256. Artifacts may expire according to GitHub retention settings. Full-precision values in the artifacts govern over rounded values in this report.

To reproduce: follow `corrected_classical_ml/reconstruction_2026/README.md`, install dependencies, run `fetch_upstream.py`, `pytest`, `sweep.py`, then `sweep_extensions.py`. Running the notebook adds figures. Do **not** commit the downloaded data or re-label these 2026 outcomes as submitted 2024 results.
