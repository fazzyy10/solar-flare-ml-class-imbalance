# Reproducibility audit

This directory records the post-MSc audit of what can and cannot be reproduced from the surviving evidence.

## Current conclusion

The submitted dissertation is intact, but the preserved private archive does not contain enough executable code and exact local data to justify an exact-reproduction claim.

The preserved file called `ccsc_FlareML.ipynb` is an HTML snapshot of the public upstream GitHub page, not executable notebook JSON. The raw evidence ZIP also contains an HTML snapshot of the upstream test-data page rather than the underlying CSV.

Therefore the responsible next step is a **provenance reconstruction and corrected rerun**, not an invented restoration of missing code.

## Minimum standard before calling a new rerun reproducible

A new rerun should record:

- exact data source and file hash;
- exact code commit;
- Python and package versions;
- random seeds;
- preprocessing order;
- resampling order;
- cross-validation splitter and grouping logic;
- model hyperparameters;
- class-level and aggregate metrics;
- outputs saved from a clean run;
- a clear statement of whether the run is historically identical or methodologically revised.
