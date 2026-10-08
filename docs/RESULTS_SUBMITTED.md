# Results reported in the submitted dissertation

These are historical results reported by the 2024 dissertation. They have **not** yet been independently reproduced in this repository.

## Original dataset

The dissertation reports Gaussian Naive Bayes as a strong performer on the original dataset and describes Ridge Classifier as among the weakest in that setting.

## Random-under-sampled datasets

For the 100 under-sampled datasets, the dissertation identifies Gradient Boosting Classifier and Linear Discriminant Analysis as strong performers. It reports for Gradient Boosting:

- average BACC: **0.734617**
- average TSS: **0.469233**

## SMOTE-over-sampled datasets

For the 100 over-sampled datasets, the dissertation reports Extra Trees Classifier as the top performer, with Random Forest Classifier also performing strongly.

## Overall reported comparison

Across the dissertation's reported aggregation of the original, under-sampled and over-sampled evaluations:

- **Extra Trees Classifier:** average BACC **0.829979**, average TSS **0.659958**
- **Passive Aggressive Classifier:** average BACC **0.691841**, average TSS **0.311008**

The dissertation therefore selects Extra Trees Classifier as the most suitable algorithm among the 14 evaluated approaches.

## Rare-event behaviour

The dissertation states that performance fell when forecasting X-class flares, linking this to the very small number of X-class examples.

## Interpretation boundary

These values are recorded here because they appear in the submitted thesis. They are not presented as fresh benchmark results. A later corrected rerun must be reported separately and must not overwrite these historical numbers.
