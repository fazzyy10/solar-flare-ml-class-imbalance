# Corrected classical-ML reconstruction

This directory is reserved for a new post-MSc reconstruction of the classical machine-learning study.

It is intentionally **not** populated with invented or reconstructed code presented as if it were the original 2024 notebook.

## Planned reconstruction standard

A future implementation should:

1. identify and hash the exact public/reconstructed input data;
2. keep preprocessing and resampling inside each training fold;
3. define reproducible random seeds;
4. implement transparent baseline models before large model sweeps;
5. evaluate BACC and TSS consistently with the historical study;
6. preserve per-class results;
7. compare ordinary stratified validation with grouped/temporal alternatives where feasible;
8. store configuration and outputs for every run;
9. distinguish historical thesis results from new results in filenames and tables.

## Historical comparison table

Any future report should separate:

| Layer | Meaning |
|---|---|
| Submitted method | What the 2024 dissertation actually reports |
| Audit finding | What later methodological review identifies as worth testing |
| Corrected rerun | New post-MSc implementation and results |

No new number belongs in the "submitted" column unless it is directly supported by the thesis.
