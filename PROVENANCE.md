# Provenance

## 1. Frozen assessed record

The authoritative historical record is the MSc dissertation submitted in August 2024 at Cardiff Metropolitan University:

**Application of Machine Learning Modeling in NOAA SHARP Data for Solar Flare Prediction**

The PDF in `submitted_msc_record/` is a clean binary copy of that submitted dissertation. Its visible content is not rewritten in this repository.

Any later methodological criticism, reconstruction, corrected experiment or neural-network continuation is separate from the assessed MSc work.

## 2. Preserved code/data evidence

The private MSc archive was inspected during a later provenance sweep. The preserved code/evidence area contained a file named `ccsc_FlareML.ipynb`, and the raw evidence ZIP contained:

- `ccsc_FlareML.ipynb`
- `flaringar_simple_random_40.htm`

Inspection showed that both were saved HTML snapshots of public GitHub pages, not the underlying executable notebook/data files. The first points to the public FlareML notebook; the second points to a public FlareML CSV page.

This matters because the current archive is not sufficient to claim an exact, byte-for-byte reconstruction of the MSc computational environment.

## 3. Upstream FlareML dependency

The public upstream project is:

**FlareML — Predicting Solar Flares with Machine Learning**  
Authors: Yasser Abduallah, Jason T. L. Wang, Haimin Wang  
Repository: https://github.com/ccsc-tools/FlareML  
Zenodo DOI: https://doi.org/10.5281/zenodo.5634114  
Licence: MIT

The upstream repository includes, among other files, `ccsc_FlareML.ipynb`, `YA_01_PredictingSolarFlareswithMachineLearning.ipynb`, Python utilities, and public data directories.

Fawaz is not the author of this upstream software. It is treated as prior public work and a provenance source.

## 4. What belongs to the MSc dissertation

The submitted dissertation contains Fawaz's research framing, literature synthesis, dataset selection rationale, exploratory analysis, comparative modelling design, sampling/evaluation choices, interpretation and written conclusions.

The submitted study reports:

- 845 flare events from 472 active regions;
- class counts B=128, C=552, M=142, X=23;
- 13 SHARP parameters;
- original data plus 100 random-under-sampled and 100 SMOTE-over-sampled variants;
- stratified 10-fold cross-validation;
- 14 classifiers;
- BACC and TSS evaluation;
- 29,400 reported model tests.

These are historical claims from the dissertation and remain labelled as such until independently reproduced.

## 5. Later methodological audit

The later audit does not alter the submitted record. It asks whether a new reconstruction should improve experimental controls, including:

- fitting any preprocessing only on training data;
- applying resampling inside training folds rather than before cross-validation;
- recording random seeds and software versions;
- checking whether repeated active regions require grouped validation;
- checking whether temporal ordering should be respected in a forecasting setting;
- separating model selection from final performance estimation where appropriate;
- reporting class-level behaviour and uncertainty, not only averaged metrics.

These are post-MSc research questions, not retroactive claims about what was submitted.

## 6. Post-MSc PyTorch continuation

A later self-directed PyTorch exploration exists in Fawaz's application evidence. It is unpublished and explicitly separate from the MSc dissertation. It must not be described as part of the 2024 assessed project.

The repository will not publish detailed PyTorch code or numerical results until the underlying source artefacts are verified against the private archive.

## 7. Reproducibility status

Current status:

- historical dissertation: **verified and preserved**;
- upstream FlareML source: **publicly identifiable and attributed**;
- exact original MSc executable notebook: **not recovered from the preserved archive**;
- exact original local dataset copy: **not recovered from the preserved archive**;
- exact original environment: **not recovered**;
- byte-for-byte rerun: **not claimed**;
- corrected post-MSc reconstruction: **planned and must be verified before being labelled reproducible**.
