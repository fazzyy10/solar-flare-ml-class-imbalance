# Data provenance

No dataset is redistributed in this repository at present.

## Dataset described in the dissertation

The dissertation describes a DeepSun/FlareML-derived dataset with 845 flare events from 472 active regions, using 13 SHARP parameters and B/C/M/X labels.

Class distribution reported in the dissertation:

| Class | Count |
|---|---:|
| B | 128 |
| C | 552 |
| M | 142 |
| X | 23 |
| **Total** | **845** |

The dissertation cites the public solar-flare prediction resources associated with DeepSun/FlareML and gives this historical access point:

https://nature.njit.edu/spacesoft/Flare-Predict/

## Public upstream FlareML data

The upstream FlareML repository currently exposes public data directories, including:

- `data/original_data/flaringar_original_data.csv`
- `data/train_data/flaringar_training_sample.csv`
- `data/test_data/flaringar_simple_random_40.csv`

Upstream repository:

https://github.com/ccsc-tools/FlareML

## Why the data are not copied here yet

The private MSc archive does not currently contain a verified local copy that can be proven to be the exact dataset instance used in the submitted experiments. A public upstream file may be useful for a new reconstruction, but it must not automatically be labelled as the byte-identical original MSc input.

A corrected rerun should therefore record:

1. exact source URL and commit/release where possible;
2. file hash;
3. schema and class counts;
4. any cleaning or feature-selection steps;
5. whether the input is historically identical, reconstructed, or a new public substitute.
