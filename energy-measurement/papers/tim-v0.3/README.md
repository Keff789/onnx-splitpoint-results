# IEEE TIM v0.3 — Self-contained journal extension

**Beyond Sampling Rate: Reference-Based Energy Measurement Across Edge-AI Platforms**
Kevin Mika, Joris Wachsmuth, Florian Porrmann, Jens Hagemeyer.
Working manuscript, 9 October 2026; not submitted or published.

## Read and build

`main.pdf` is the manuscript. `main.tex` is the main LaTeX file.

```bash
bash build.sh
```

Uses a local LaTeX installation and the included IEEEtran class/style. No network,
measurement acquisition, external repository changes or automatic installation.
BibTeX is preferred; a checked bundled bibliography supports unchanged sources.

## Full result-export regeneration

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON=.venv/bin/python bash regenerate.sh
```

The pipeline regenerates pair differences, duration/rate summaries and a fixed
control from existing per-execution outcomes. It selects the final native/all-15
reconstruction/spectral summaries, makes all charts, verifies arithmetic with an
independent standard-library implementation, and compiles the paper.

`make_foundation_figures.py` adds the self-contained Jetson presentation. It does
not rerun waveform reconstruction. `make_figures.py` retains the v0.2 Hailo and
control chart designs unchanged. Together they make thirteen numerical chart
files; four pairs share manuscript figure numbers. The boundary illustration is
the original supplied vector drawing.

The checked PDF has **13 IEEE pages including references, ten numbered figures
and four tables**, with unchanged class, body font and page geometry. The final
GPU campaign is not fabricated to fill a section. Its later incorporation may
change the final length.

## Scientific organisation

1. Measurement design and a complete explanation of the analysis.
2. RQ1: native Jetson rate/duration results, all nine intervals, and long-window FP16.
3. RQ2: energy versus fluctuation coverage, acquisition response, and Hailo spectra.
4. RQ3: full Jetson deployed-meter recap, Hailo card/DC/telemetry/AC comparison,
   and Hailo energy/power/span dependence across requested durations.
5. RQ4: duration dependence, direct sweeps and controlled execution conditions.
6. Practical interpretation and limits.

This is an integrated journal extension, not a supplement that requires reading
PARMA first. The introduction attributes the reused Jetson basis; the additional
Hailo and protocol evidence is distinguished in `EXTENSIONS_VS_PARMA.md`.
The chronological development record remains outside the manuscript.

## Package map

- `sections/`, `tables/`, `figures/`, `generated/numbers.tex`: manuscript inputs.
- `data/`: original numerical inputs, unchanged from TIM v0.2.
- `generated/`: reproducible summaries, all pair quantiles and plot inputs.
- `scripts/`: result selection/aggregation, charts and independent arithmetic checks.
- `METHOD_DETAILS.md`, `SOURCE_MAPPING.md`: methods and output-to-input binding.
- `KNOWLEDGEBASE_TIM_v03.md`: current editorial and scientific decisions.
- `TIM_ARBEITSSTAND_UND_OFFENE_EVIDENZ.md`: pending measurements and submission items.
- `EXTENSIONS_VS_PARMA.md`: internal technical-extension register.
- `metadata/`: source identities, numerical/build/render checks and policy source.
- `provenance/`: prior source descriptions and clearly versioned earlier decisions.

## Reproduction limits

This is a result-export reproduction package, not a complete waveform archive.
A successful run verifies selection, arithmetic, figures and manuscript inputs.
It does not establish a new calibration, PSD estimation, synchronised dynamic
telemetry test, host-energy decomposition or final discrete-GPU result.
All 81 files under `data/` are unchanged from v0.2, including the 79 inherited
PARMA inputs and the two pause-source files.

The cited source repository commit remains
`85eb488587a51659239c45d966f930f7c7b72a6e`. It identifies the source evidence and
PARMA state, not this locally generated journal package. No TIM push, tag,
release, DOI or submission is performed by the generation/build scripts.
