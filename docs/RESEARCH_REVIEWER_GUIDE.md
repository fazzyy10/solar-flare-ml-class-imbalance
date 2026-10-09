# A closer look at my solar-flare research

**Mohamed Fawaz Hussain Fareed** · MSc Data Science, Cardiff Metropolitan University  
**2024 assessed dissertation; separate, executable 2026 methodology study**

If you only have a few minutes, I would draw your attention to one feature of this research: **the result changes when the question used to evaluate it changes.**

## Where the work started

For my MSc dissertation I studied classification of **B, C, M and X solar-flare events** using NOAA SHARP-derived magnetic measurements. The reference dataset contains **845 events**, of which only **23** are X class.

An overall score can conceal weak evidence for the rarest class, which is why the original study compared models and sampling approaches using Balanced Accuracy and True Skill Statistic rather than treating ordinary accuracy as sufficient. It reports **14 classifiers**, with Extra Trees leading the thesis's reported evaluation. The published thesis figures are **BACC 0.829979** and **TSS 0.659958**. These are the original dissertation's figures, **not an independently reproduced result**.

[Original dissertation](../submitted_msc_record/THESIS_FULL_TEXT.md) · [Methods and historical provenance](../PROVENANCE.md).

## A question that surfaced later

I returned to the source and noticed that 845 observations did not represent 845 unrelated solar regions. There are **472 active-region identifiers**, and **206 regions appear more than once**.

This leads to a specific question: if events from a region can appear in both the training and test fold, are we really evaluating performance on a *new region*?

The independent **2026 follow-up** compares traditional stratification with active-region-grouped validation. Preprocessing and optional SMOTE/undersampling occur within training folds, not on the complete dataset.

![The different questions asked by three evaluation designs](figures/validation_comparison.svg)

For **Extra Trees + train-fold SMOTE**, the mean four-class one-versus-rest BACC was:

- **0.7071** using stratified five-fold validation.
- **0.6413** using grouped five-fold validation.

Across **18** seed-matched comparisons, the grouped result was lower in **17**. This does not establish the exact size of leakage bias. Grouped partitions also alter class composition and sample difficulty. I treat it as evidence that the validation decision affects the estimate, not as proof of a particular causal mechanism.

## One result that should not be scored

I also tested a straightforward final-20%-by-time holdout. Its test set contained **no X events**. That makes a full four-class BACC/TSS **undefined**.

Reporting a neat number anyway would answer a different question than the one in the dissertation. A separately reported, retrospectively selected 2014-start temporal sensitivity check includes nine X examples, but it is post hoc and too limited to claim operational forecasting validity.

## Reproduction is a different claim

The original 2024 executable workflow and the exact transformation of its local dataset have not been fully recovered. A preserved `ccsc_FlareML.ipynb` archive entry was in fact an HTML page snapshot, not notebook JSON.

I therefore do not compare the original thesis's scores to the new 2026 scores as if the latter reproduced the former. The new script uses other folds, preprocessing, model settings and selection decisions. What it demonstrates is a **testable methodological investigation** using a pinned and checksum-verified public source, not restoration of an irrecoverable execution.

[Full 2026 method and figures](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) · [Executable code](../corrected_classical_ml/reconstruction_2026/experiment.py) · [Validation checks](../corrected_classical_ml/reconstruction_2026/test_reconstruction.py) · [Successful GitHub Actions run](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/runs/37831563054).

## What I would want to investigate next

The work makes me interested in a general research problem: **how can we tell whether the test data answer the generalisation question we care about?**

I would extend this with predeclared temporal splits, external evaluation across regions and solar cycles, uncertainty estimates for rare classes and a more explicit examination of calibration. The present work does not establish those results. It creates reasons to test them.

For someone reviewing this as evidence of research potential, the point I would emphasise is the progression from *comparing classifiers* to *challenging what makes a comparison credible*. The fact that some results became harder to report after a more careful audit is not something I want to hide.

## Sources and credit

DeepSun/FlareML was developed by **Yasser Abduallah, Jason T. L. Wang and Haimin Wang**. [Upstream code and attribution](https://github.com/ccsc-tools/FlareML) · [Source comparison](UPSTREAM_COMPARISON.md) · [Data card](../data/DATASET_CARD.md).

The assessed MSc project, this later independent follow-up and the original upstream software are three distinct contributions. None is being presented here as a peer-reviewed paper by me.

**Suggested reading:** [original 2024 method](../submitted_msc_record/THESIS_FULL_TEXT.md) → [2026 validation results](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) → [source code](../corrected_classical_ml/reconstruction_2026/).
