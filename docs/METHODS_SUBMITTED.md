# Submitted methodology

This file summarises the methodology as reported in the 2024 dissertation. It is descriptive, not a claim of independent reproduction.

## Dataset

The dissertation selected a DeepSun/FlareML-derived solar-flare dataset with:

- May 2010 to December 2016 coverage;
- 845 flares from 472 active regions;
- 128 B, 552 C, 142 M and 23 X flares;
- 13 SHARP magnetic parameters per sample;
- one sample corresponding to a flare event;
- values described as normalized to 0-1;
- a 24-hour prediction setting.

## Class imbalance

The X class contained only 23 events, making severe imbalance a central methodological concern.

The dissertation compared:

- the original dataset;
- 100 random-under-sampled variants;
- 100 SMOTE-over-sampled variants.

## Cross-validation

The dissertation reports stratified 10-fold cross-validation. For each algorithm, the text states that the 10-fold procedure was applied across the original, under-sampled and over-sampled datasets, producing 2,100 tests per algorithm and 29,400 tests across 14 algorithms.

## Algorithms

### Conventional algorithms

1. Decision Tree Classifier
2. Extra Tree Classifier
3. Gaussian NB
4. K Neighbors Classifier
5. Linear SVC
6. Passive Aggressive Classifier
7. Ridge Classifier
8. SGD Classifier
9. SVC

### High-performance algorithms

10. Bagging Classifier
11. Extra Trees Classifier
12. Gradient Boosting Classifier
13. Linear Discriminant Analysis
14. Random Forest Classifier

## Metrics

The dissertation evaluated each B/C/M/X class using a one-versus-rest framing and calculated:

- Balanced Accuracy (BACC)
- True Skill Statistic (TSS)

The class-level values were then averaged to form a multi-class summary.

## Historical design versus later audit

This file records what the dissertation says. The later `reproducibility_audit/VALIDATION_AUDIT.md` asks how a new reconstruction should strengthen fold isolation, grouping/temporal checks, uncertainty reporting and environment capture. Those later controls must not be retroactively described as part of the submitted MSc work.
