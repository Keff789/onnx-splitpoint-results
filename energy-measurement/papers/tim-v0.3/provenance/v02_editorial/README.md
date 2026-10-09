# IEEE TIM v0.2 — Beyond Sampling Rate

**Beyond Sampling Rate: Reference-Based Energy Measurement Across Edge-AI Platforms**  
Kevin Mika, Joris Wachsmuth, Florian Porrmann, Jens Hagemeyer  
Working manuscript, 9 October 2026. Not submitted; not a published journal article.

## Read and build

`main.pdf` is the manuscript. `main.tex` is the main LaTeX file.

```bash
bash build.sh
```

The build uses the supplied IEEEtran class and bibliography style with a local
LaTeX installation. It does not install software, contact GitHub, acquire data,
or modify any external repository. BibTeX is used when available; the checked
bundled bibliography is a fallback for unchanged references.

## Regenerate from included numerical exports

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON=.venv/bin/python bash regenerate.sh
```

`generate_results.py` recomputes paired energy/power/span differences, duration
summaries and direct-rate group statistics from stored per-execution outcomes.
It also refits the 12-run additive control and selects the final native/all-15
reference summaries. `make_figures.py` produces eight numerical chart files;
two pairs of those files form two side-by-side manuscript figures.
`verify_results.py` independently checks the exported calculations with Python's
standard library and explicit type-7 quantiles. `build.sh` compiles the paper.

The checked manuscript has **10 pages in total, seven numbered figures and four
tables** in the unchanged IEEE two-column layout. Page count depends on the
LaTeX environment; the shipped PDF is the checked rendering.

## Scientific organisation

The central contribution is the deployed measurement: Hailo card-input sensing,
HailoRT and AC observations, followed across duration and interpreted together
with recorded energy and interval span. Jetson's native-reconstruction and
all-15 FP16 results are a concise reference, not a second long presentation of
PARMA. Hailo's spectral results and the separate fixed-rate pause diagnostic
complete the practical argument.

The main text reports actual evidence and its limits, not a chronology of
previous analyses or a list of experiments promised as if already completed.
`TIM_ARBEITSSTAND_UND_OFFENE_EVIDENZ.md` keeps the remaining work explicit.

## Package map

- `sections/`, `tables/`, `figures/`, `generated/numbers.tex`: manuscript inputs.
- `data/`: unchanged PARMA-source data exports plus the bound pause export.
- `generated/`: this version's reproducible summaries, including all pair quantiles.
- `scripts/`: numerical generation, plotting, and an independent arithmetic audit.
- `METHOD_DETAILS.md`: current definitions, estimator order and disclosure limits.
- `SOURCE_MAPPING.md`: figure/table-to-input mapping.
- `EXPERIMENT_CONFIGURATIONS.md`: supported configuration and missing bindings.
- `EXTENSIONS_VS_PARMA.md`: baseline versus additional journal evidence.
- `REVISION_NOTES_DE.md`: changes from the supplied TIM v0.1.
- `metadata/`: input identities, numerical checks, and build/render checks.
- `provenance/`: explicitly labelled prior method/configuration documents and excerpts.

## What reproduction does not establish

This is a **result-export reproduction package**, not the complete raw-signal
archive. It performs no new waveform integration, calibration or PSD estimation.
The 79 files in the original PARMA `data/` directory are preserved byte-for-byte;
source metadata are retained separately. Some preserved files cover broader
work, including GPU or alternate protocols; they are not selected as final TIM
results merely because they are in the package. The final discrete-GPU extension,
Hailo same-trace energy-rate validation, quantitative host decomposition and
synchronised dynamic telemetry are not silently filled in.

The reference repository commit is
`85eb488587a51659239c45d966f930f7c7b72a6e`. It contains the PARMA/evidence source
state, **not this newly generated TIM package**. No TIM Git push, tag, release,
DOI or journal submission was performed in this editing step.
