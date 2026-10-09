# Jetson window and pause study — evidence freeze, 29 September 2026

**Completed diagnostic measurements and export review, not an absolute calibration.**
No claim of a universal sampling-rate correction or a specific throttling mechanism.

## Contents

- [Findings and limitations](FINDINGS.md)
- [Per-run tables](data/) and [original log excerpts](evidence/log_excerpts.md)
- [Analyzer source excerpts](evidence/code_excerpts.md)
- [Source identities](sources.json), [publication boundary](EXCLUSIONS.md)
- [Next stage on Twix](TWIX_REANALYSIS.md)

| Evidence | Scope | Public file / source |
|---|---|---|
| Timeout sweep | 405 YAMLs, 27 rates, 15 repeats, 102-s legacy windows | timeout_rates.csv, S01/S06 |
| Iterations sweep | 45 runs, 3 rates; 46 logs including dry-run | iteration_runs.csv, S02/S03/S06 |
| Unforced reintegration | Same 45 stored traces, original detector bounds restored | window_runs.csv, S04 |
| Pause experiment | Constant 2 kS/s; conditioner + six scored runs | pause_*.csv, pause_quality.json, S05/S07 |

Tables are exact field selections from identified exports, not ADC samples.
Iteration mapping and timeout medians come from derived S06; unforced records from
remote reintegration S04; pause tables from audit S07. The separate original S01–S05
archives preserve the review inputs. None of the derived reviews is another experiment.
No percentile trimming of physical repetitions is applied. Conditioner 0 remains
in the table and is excluded from group statistics.

Powers retain the recorded NvGpu scaling at the Jetson, not newly validated absolute
metrology. Signal envelopes are not hardware-synchronized kernel markers. Queries
are not automatically individual images. See FINDINGS.md for negative evidence.

## Verify and reproduce

From this directory, Python 3.9+ standard library:

```bash
python3 verify.py
python3 verify.py --sources /path/to/private_bundle/originals
python3 reproduce_tables.py --sources /path/to/private_bundle/originals --out /new/output
```

`verify.py` checks file integrity and table arithmetic. `--sources` also checks all
16 original source fingerprints. Reproduction creates six byte-identical CSVs from
the corresponding source exports. Neither operation re-integrates raw traces,
accesses hardware, or independently validates calibration. SHA256SUMS covers this
directory except itself; it is a checksum manifest, not a signature.

The complete project knowledgebase and original review/software archives are in the
private companion package. The Git freeze is deliberately not a full raw-data backup.
