# Offline robustness evidence — 9 October 2026

Additional checks for *How Fast Is Fast Enough? Reference-Calibrated Energy Measurement
for Edge-AI Inference*. The original paper exports remain unchanged. Interpretation and
remaining questions are documented in the [knowledgebase update](../knowledgebase/2026-10-09-offline-robustness.md).

## Contents and evidence status

| Location | Contents | Status at this review |
|---|---|---|
| `scopes/` | Three original CSVs, `summary.json`, original `REPORT.txt` | Supplied by the author and reviewed; 118 source records / 59 pairs complete |
| `fp16/` | Original FP16 summaries, metadata and all 15 small record JSONs | Reviewed; IDs 0–14 complete |
| `review/` | Independent aggregate audit, all persistent minima and original-export comparison | Recomputed from the supplied CSVs; executable standard-library audit included |
| `energy_paper_checks.py` | Delivered v1.0.1 analysis script | Native/via-1M sensitivity method; original FP16 return used v1.0.0 with the same numerical kernels |
| `archive_energy_checks.py` | Local result-only archiver | Adds the companion files and compact details listed below; no raw-data analysis |

The supplied Scope `REPORT(2).txt` is stored as `scopes/REPORT.txt` without changing its
contents. The five Scope files are about 3.38 MB in total. The large Scope archive
reported as exceeding 500 MB was not transferred or independently reviewed in full.

The FP16 files are retained from the earlier standard return. The earlier full-grid
return has identical FP16 energy tables, PSD tables and per-record numerical payloads;
its different settings are retained as `fp16/repeat_full_grid_run_settings.json`.
Both returns describe the same 15 physical recordings. Their failed Scope-discovery
status is historical and is superseded by the separate successful `scopes/` return.

## Findings that matter for interpretation

- The outer Q95 hierarchy and envelope reproduce from the per-run table. The audit
  does not independently recalculate the inner per-window/per-phase Q95 without its
  original vectors, the calibrated raw signals or filtering.
- Eight pointwise envelope decisions change at 0.5% or 1% between native and via-1M;
  four persistent minima change at those tolerances. Two further minima change at 5%.
- At 2 s, 2 kS/s passes the individual 1% criterion, but 9.4 kS/s fails in both new
  branches. The new persistent 1% minimum is 16 kS/s, versus 2 kS/s in the original
  export. The difference is already present in the via-1M branch and is not explained
  solely by removing the intermediate processing.
- Original and additional reconstruction grids must not be mixed. These outputs are
  a sensitivity check, not an exact Table-2 reproduction or an absolute calibration.
- The Scope summary flags extrapolation of the 0–3.5-A voltage model in 51 records.
  Its extent requires the stored audit counts and current extrema, exported below.
- FP16 50/85-S/s energy decisions and 125/160-kS/s spectral decisions survive the
  tested cohort and PSD sensitivities. The earlier exact 1.071% maximum at 50 S/s is
  not reproduced by the additional grid.

## Add the local companion evidence on Twix

From the repository root, run:

```bash
python3 energy-measurement/2026-10-09-offline-robustness/archive_energy_checks.py
```

Python 3.10 or later is sufficient; no third-party packages are required. The source
defaults to `~/Reports/energy-paper-check-scopes`. A different result folder can be
selected with `--source /absolute/path`. The optional actually available analysis
script is taken from `~/Downloads/energy_paper_checks.py` or `--analysis-script`.

The helper first compares all five original Scope files with the registered contents.
A different run or report is not silently substituted. It then reads only existing
result JSONs, one record at a time, and adds:

- `scopes/run_settings.json`, `environment.json`, `input_inventory.json` and
  `metadata_evidence.json`, plus their listed small metadata copies;
- `scopes/record_audit.jsonl`: all 118 original record headers and every window header,
  with only the large `comparisons` lists removed;
- `scopes/critical_comparisons.jsonl.gz`: unchanged original comparison vectors for
  the native/via envelope-determining groups at the eight threshold-change cells and
  at 2 s / 9.4 kS/s (12 distinct workload/source/duration/rate keys for this return);
- `scopes/energy_paper_checks.py`, if the local supplied script is available as v1.0.1;
- `scopes/archive_index.json`: source paths, byte sizes, input timestamps, selected
  critical cells and the location/size of the unchanged full ZIP, if present.

The full result ZIP, full Scope record JSONs and raw NPY/Parquet traces stay at their
existing laboratory locations. The helper does not read the raw traces, hash the large
archive, resample data, modify the source outputs, or run Git commands. The compact
details are expected to be much smaller; their actual byte count is printed on completion.
Existing different destination files cause a visible stop instead of being overwritten.

These companion files are only present after the local helper and subsequent Git commit
have succeeded. Their existence is not claimed by the initial summary-only publication.

## Reproduce the aggregate review

```bash
python3 energy-measurement/2026-10-09-offline-robustness/review/audit_scope_results.py
```

This uses only Python's standard library and the existing original
[`common_reference_summary.csv`](../PSD_Analysis_multi_workload_documentation_artifacts/common_reference/common_reference_summary.csv),
restricted to `mode=phase_only`. It regenerates the three review result files next to
the audit script. Quantiles use explicit linear/type-7 interpolation; persistent minima
require every higher eligible tested rate to pass. The 20-ms/150-S/s cell has only one
valid numerical case per record and changes none of the reported minima.

## Scope of preservation

This compact Git evidence preserves the reviewed aggregates, software, metadata and
selected detailed checks. It is not a replacement for the complete raw-data and result
archive. Code and results remain tied to their declared inputs and settings; physical
recordings, numerical cases, empirical quantiles and confidence limits are distinct.
