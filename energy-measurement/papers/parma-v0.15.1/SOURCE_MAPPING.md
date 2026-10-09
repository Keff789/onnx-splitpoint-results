# Manuscript output map — v0.15.1 (PARMA, Jetson only)

Original numerical inputs are unchanged. The main reconstruction and FP16
selections remain those of v0.13; only the publication scope and presentation
of existing direct results change. Rounding is applied only for display.

| Main output | Source and selection | Generator / supplied output |
|---|---|---|
| Figure 1 — electrical boundaries | Author-supplied SVG, adapted to the Jetson-only configuration; original preserved in `revision_history/v013/figures/` | Static `figures/measurement_boundaries.svg` and vector PDF; only platform branch/layout labels edited. |
| Table 1 — experimental roles | Original cohort inventories/settings; Jetson only | `paper.tex`; details in `EXPERIMENT_CONFIGURATIONS.md`. |
| Figure 2 — fixed-2-kS/s reconstruction | `data/final_reconstruction/scope_fixed_2k_excerpt.csv`, native column | `scripts/build_final_manuscript.py` → `figures/scope_native_energy.pdf`. |
| Table 2 — errors and persistent minima | Same native excerpt plus `data/robustness_20261009/scope_persistent_minima.csv` | Same generator → `generated/table_reconstruction_native.tex`; 9 rows. |
| Table 3 — direct rate groups | `data/final_direct/`, all 8 Jetson series and finite candidates | `scripts/build_tables.py`; explicit selection also in `generated/parma_direct_rates.csv`; 215 groups, 3,225 executions. |
| Table 4 — controlled rate effect | `data/validation/controlled/complementary/data/combined_runs.csv` | `scripts/extend_controlled.py` and `build_final_manuscript.py`; same three displayed outcomes. |
| Figure 3 — FP16 spectral coverage | `fp16_psd_selection.json`, all 15 IDs / `matched_4s_4s` | `build_final_manuscript.py` → `figures/fp16_variance_coverage.pdf`; three evaluated rates, no spectral-minimum inference. |
| Figure 4 — Jetson duration dependence | Original candidates, 7 Jetson duration series including variable YOLO | `extend_tables.py` → `generated/parma_duration_curve_data.csv`; `make_paper_figures.py` → one-chart `duration_dependence.pdf`. Own-span power, fixed within-series 600-s median denominator, all Q05–Q95 bands visible. |
| Figure 5 — deployed meter comparison | 7 Jetson workloads × 3 comparators, common 300-s request; 15 paired executions per workload | `extend_tables.py` → `parma_device_pair_values.csv`, `parma_device_pair_spread.csv`, `scripts/make_device_comparison.py` → `generated/device_pair_medians.csv` and `figures/device_pair_medians.pdf`. Median of individual signed power differences; complete Q05/Q95 and pairs retained outside the main figure. |
| Abstract / results narrative values | Same native FP16 inputs plus named Jetson rate/meter groups | `generated/final_numbers.tex` and `generated/parma_numbers.tex`. |
| Calibration and acquisition-path spectral context | Unchanged calibration and native paired-scope summaries | Existing calibration/native-spectrum scripts; qualifications in `METHOD_DETAILS.md`. |

## Exact source identity

The scope/FP16 robustness material remains pinned to result commit
`9b4208c97420b1621a14b7dc91f051985e65e6f5`. The fixed-2-kS/s input is explicitly an
excerpt, not a complete envelope or raw waveform. Provenance is in
`data/final_reconstruction/SOURCE.json`, `metadata/ROBUSTNESS_SOURCE.json` and the
original input manifests. No new Git release, branch or DOI is implied.

## Material retained for TIM, not PARMA results

Multi-platform source exports and unprefixed all-platform derived tables remain
in the package. `data/git/platform_spectral_metrics.csv`, Hailo-selected spectrum
summaries and Hailo supplementary figures are not cited as main experimental
results. The original boundary artwork and changed v0.13 source files remain
under `revision_history/v013/`. See `PARMA_TIM_SCOPE_v014.md`.

## Reproduction limits

`bash regenerate.sh` regenerates manuscript outputs from the supplied summaries,
with an independent check against the original pair candidates. It performs no
raw-waveform integration, new acquisition, calibration fit or new telemetry
characterisation. The SVG/PDF boundary artwork is a static supplied asset, as in
the predecessor package; it needs no rendering dependency to build the paper.
