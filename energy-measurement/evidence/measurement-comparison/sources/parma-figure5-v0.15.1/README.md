# PARMA v0.15.1 — deployed-meter comparison artifact

This is the **compact, executable Figure-5 companion artifact**, not the complete raw-data archive or full manuscript source package. It records the Jetson-only comparison used by the PARMA author draft *How Fast Is Fast Enough? Reference-Calibrated Energy Measurement for Edge-AI Inference*.

## Contents

- `pairs.json`: 105 physical executions, each with PicoScope, u.RECS, INA3221 and scaled-Shelly mean powers; original recording IDs retained. These yield 315 comparisons, not 315 independent experiments.
- `summary.csv`: all 21 medians and empirical 5th/95th percentiles at full stored precision.
- `reproduce.py` and `figure.py`: recompute the paired statistics, verify them and render Figure 5 as vector PDF and PNG.
- `PROVENANCE.json`: source archive and source-member identities, export definition and limits.
- [Knowledgebase update](../../knowledgebase/2026-10-09-parma-v0151.md): current manuscript decisions and PARMA/TIM scope.
- `CITATION.cff`: the four manuscript authors in manuscript order.

## Reproduce

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python reproduce.py
```

Outputs are `figures/device_pair_medians.pdf`, its PNG preview, full derived pair CSVs and `generated/device_figure_qa.json`. The seven workload groups and three comparators must be complete. The script checks all medians and percentiles to 1e-10 percentage points. It reads only stored mean powers, not waveforms.

The displayed metric is `median_i(100*(P_sensor,i/P_pico,i - 1))`. Percentiles remain downloadable rather than crowding the main figure. They are empirical run spread, not confidence intervals. Every meter keeps its recorded scaling and own integration interval. In particular, scaled AC readings are not raw wall-socket measurements and do not share the selected DC boundary. Do not interpret the differences as intrinsic meter error or a universal 0.5% specification.

## Release and complete paper package

The release workflow builds this compact artifact and publishes its PDF, CSVs, ZIP and checksum file under the tag `parma-figure5-v0.15.1`. A commit identifies the exact source state. A successful workflow/release is required before claiming that tag exists.

The separately delivered full v0.15.1 manuscript package contains `paper.tex`, all five main figures, the updated full regeneration pipeline and the unchanged broader evidence inputs, including TIM material. The clean LaTeX ZIP builds the complete eleven-page author draft. These full packages are separate from this compact public Figure-5 release; their names and checksums are recorded in `DELIVERABLES.json` when available. Do not infer that this directory alone reproduces the entire paper.

No acceptance, artifact-evaluation badge, DOI, new calibration or new measurement is claimed. Zenodo metadata is not a deposit. See RIGHTS_AND_AVAILABILITY.md before redistribution or DOI registration.
