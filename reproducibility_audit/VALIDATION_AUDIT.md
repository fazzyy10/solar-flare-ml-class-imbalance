# Validation audit

This is a later methodological audit. It does not rewrite the submitted MSc dissertation.

## 1. Fold-safe preprocessing and resampling

The dissertation describes generating under-sampled and SMOTE-over-sampled datasets and applying stratified 10-fold cross-validation to those datasets.

For a new reconstruction, any operation that learns from the data should be fitted inside the training fold. In particular:

- scaling/normalization fitted from data should be trained on the training fold only;
- random undersampling should be applied to the training fold only;
- SMOTE should generate synthetic examples from the training fold only.

This prevents validation-fold information from influencing training-time transformations.

The audit point is not that the historical numbers are automatically invalid. The point is that a corrected rerun should make the fold boundary explicit and test the effect.

## 2. Active-region grouping

The dissertation reports 845 flare events from 472 active regions. Because more than one flare can come from the same active region, a new audit should test whether ordinary stratified folds place related events from the same active region on both sides of a train/test split.

If the required active-region identifier is available, grouped validation should be compared with ordinary stratified validation. This is a **new audit question**, not a claim about the historical implementation.

## 3. Temporal validation

The dissertation itself identifies time-series cross-validation as a future methodological direction. A forecasting problem can be sensitive to temporal leakage and distribution shift.

A new reconstruction should therefore compare, where the data permit:

- stratified random cross-validation;
- grouped validation by active region;
- chronological or blocked validation.

## 4. Model-selection separation

If hyperparameters are tuned, the tuning process should be separated from the final performance estimate, for example through nested cross-validation or a locked final test set.

The submitted dissertation compared many algorithms but did not preserve a complete machine-readable record of every tuning decision in the surviving archive.

## 5. Metrics

BACC and TSS remain appropriate focal metrics for imbalance-sensitive evaluation, but a new rerun should also retain the class-level confusion information from which they are calculated.

Useful supporting outputs include:

- per-class sensitivity/recall;
- specificity;
- confusion matrices;
- macro-averaged metrics;
- uncertainty across folds/repeats.

Any metric not reported in the MSc dissertation must be labelled as new post-MSc analysis.

## 6. Reproducibility claim gate

Do not label the repository or a rerun "reproduced" until a clean environment can execute the documented workflow from identified inputs to outputs without hidden manual steps.
