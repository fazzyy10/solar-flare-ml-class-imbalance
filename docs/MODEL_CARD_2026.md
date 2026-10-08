# Model card — 2026 classical-ML evaluation baselines

**Research status:** independent post-MSc exploratory baselines. **Not** a deployed predictor, a validated forecasting system, a peer-reviewed publication or the recovered 2024 experiment.

## Model details

Models: `sklearn.ensemble.ExtraTreesClassifier` and `RandomForestClassifier`, each with **150 estimators**, `n_jobs=1` and a documented random seed. No hyperparameter-search claim is made. Input: 13 SHARP measurements from the [public DeepSun source](../data/DATASET_CARD.md). Target: four solar-flare intensity classes, B/C/M/X. Active-region ID, timestamp and original intensity suffix are excluded from predictors.

Transformations: `StandardScaler` fitted within the model training fold; optional `RandomUnderSampler` or `SMOTE(k_neighbors=3)` executed only inside training folds using an `imblearn.Pipeline`. Trees themselves do not require scaling, but the common pipeline ensures consistent treatment for the SMOTE variant.

## Evaluation design

- Stratified **5-fold** event-level CV (conventional baseline, AR IDs can occur in both partitions).
- Stratified **5-fold active-region grouped** CV (no AR overlap per fold).
- Last-20%-by-time holdout. The test period **has no X-class events**, so four-class BACC/TSS **must not** be reported.
- Explicitly **post hoc** 2014-start temporal sensitivity analysis with a one-observation active-region embargo and **nine** X-class examples in its holdout.
- Initial seed 42, supplementary seeds 73 and 2024 for stratified/grouped settings.

The 2026 experimental setting differs fundamentally from the MSc study (14 algorithms, reported 10-fold CV, repeated datasets and unverified original transformations). Do not compare them as a reproduced head-to-head.

## Metrics and provenance

- Principal comparison: four one-vs-rest class BACC values averaged. A class contributes only if both positive and negative labels exist in its evaluation subset.
- TSS per class = true-positive rate − false-positive rate; class BACC = (TSS + 1)/2. For fully evaluable four-class partitions, the macro averages have the same relationship.
- `sklearn.metrics.balanced_accuracy_score` is a **different** multiclass macro-recall metric and is labelled separately.
- New pipeline stores fold-level four-by-four confusion matrices, class support, precision, recall, specificity and class-wise TSS/BACC, allowing independent scrutiny of rare-event behaviour.

## Verified example (not a model-selection winner)

For Extra Trees + train-fold SMOTE, 2026 mean four-class BACC was **0.7071 stratified vs 0.6413 grouped**. Across 18 seed-matched comparisons, 17 grouped scores were lower. This sensitivity **does not isolate a causal leakage effect**, because split composition also changes. See [full protocol, results and all caveats](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md).

## Risks and prohibited applications

The trained baselines must **not** be used for live space-weather warnings, safety-critical decisions, claims about reliability for X-class flares, or extrapolated performance on future solar cycles. The dataset covers selected flare events and very few X events, lacks evidence for quiet-period operational false-alarm rates, and the evaluation work uses small and partly retrospective holdouts. There is no calibration, interval/predictive uncertainty validation, external benchmark or operational deployment.

## Source and known limitations

Original source: <https://github.com/ccsc-tools/FlareML> (DeepSun team). The research process, training and evaluation scripts in `corrected_classical_ml/reconstruction_2026/` are separately labelled new 2026 work. Underlying FlareML software/data are not claimed as authored by Fawaz.

The original 2024 executable notebook, environment, data transformations and code artefacts have not been recovered; its reported metrics are preserved as historical evidence, not independently reproduced. All original 2024 application files remain unchanged.
