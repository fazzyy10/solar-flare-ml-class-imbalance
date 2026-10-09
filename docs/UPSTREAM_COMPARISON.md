# Where this repository stands relative to DeepSun/FlareML

DeepSun/FlareML was an existing public research project when I carried out my MSc dissertation. I used its research and data as a source. This page sets out which work belongs to the upstream team, which results I reported in 2024, and what I investigated separately in 2026.

| Dimension | DeepSun / ccsc-tools FlareML | This MSc research repository |
|---|---|---|
| Scope | Research software for solar-flare prediction with a public notebook, pretrained/ensemble methods and related prediction service | Historical thesis plus a new reproducibility, leakage and rare-event evaluation study |
| Ownership | Upstream researchers Yasser Abduallah, Jason T. L. Wang and Haimin Wang | Mohamed Fawaz Hussain Fareed's dissertation and separately labelled subsequent analytical code |
| Dataset | Published SHARP-derived 845-event source and sample training/test files | Identifies the same public source by commit and hash without claiming original local 2024 bytes were recovered |
| Algorithms | Ensemble voting, Random Forest, MLP and Extreme Learning Machine described by FlareML | 2024 assessed study reports comparison of 14 models; new 2026 *executed* pipeline covers Extra Trees and Random Forest only |
| Run experience | Public Binder notebook; older explicit environment requirements | GitHub Actions tested notebook and new scripted benchmark; verified upstream fetch, model sweeps and archives |
| Evaluation focus | Prediction demonstration and original authors' reported methods | Fold-safe preprocessing, rare-event class support, region grouping, temporal holdout, metric definitions and limitations |
| Research outputs | External academic publications and archived software release (Zenodo v1.5) | Assessed MSc dissertation and explicitly **unpublished** 2026 methodological follow-up |
| Service deployment | Public forecasting tools and connected research services | **None.** No operational forecasting or service-level reliability claimed |
| Licence | FlareML software: MIT, copyright upstream owner | Dissertation and repository documentation have separate rights; no blanket open-source licence granted |

### What the separate 2026 study examined

The 2026 study asks what changes when active regions are kept apart during validation. That prevents events from the same region appearing on both sides of a split. In 17 of 18 seed-matched comparisons over three seeds, the grouped BACC was lower. That is a **descriptive sensitivity finding**, not a significance test or proof that the entire difference is leakage.

The 80/20 time holdout also lacks X-class test examples, which prevents a defensible four-class aggregate. That is a stronger methodological observation than a model-performance ranking on an unevaluable holdout.

### Scope of the upstream project

FlareML includes more methods, public research releases and forecasting demonstrations than my MSc repository. I have not rebuilt its prediction service or matched its published research programme. My later code addresses the narrower question of how different evaluation designs affect results on the public dataset.

### What has been independently checked

- The upstream CSV SHA-256, flare counts, feature schema and AR structure are recorded in the [2026 results report](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md).
- The numerical 2026 model findings were produced in a successful [GitHub Actions run](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/runs/37823855291) with machine-readable outputs.
- Historical 2024 scores remain attributed to the thesis, **not** presented as independently reproduced.
- This repo does not copy or claim authorship of DeepSun's code, publications or datasets.

Sources: [FlareML upstream](https://github.com/ccsc-tools/FlareML), [DeepSun/FlareML v1.5 archived release](https://doi.org/10.5281/zenodo.7506997), [2024 thesis full text](../submitted_msc_record/THESIS_FULL_TEXT.md).
