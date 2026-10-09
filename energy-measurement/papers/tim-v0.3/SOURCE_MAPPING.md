# Manuscript output mapping — IEEE TIM v0.3

All paths are relative to this package. Generation reads the stored numerical
exports and selected spectra; it does not access a measurement device or read
raw waveform data. All source input files are unchanged from v0.2.

| Manuscript output | Generated inputs | Primary source / generator |
|---|---|---|
| Figure 1, electrical boundaries | `figures/measurement_boundaries.pdf` | Vector retained from supplied TIM v0.1; current caption defines scope |
| Figure 2, Jetson fixed 2-kS/s energy | `jetson_foundation_energy.csv` | `data/final_reconstruction/scope_fixed_2k_excerpt.csv`; `make_foundation_figures.py` |
| Figure 3a, FP16 energy | `fp16_energy_plot.csv` | `data/robustness_20261009/fp16_energy_selection.csv`, all IDs 0–14 |
| Figure 3b, FP16 fluctuation coverage | `fp16_coverage_plot.csv` | `fp16_psd_selection.json`, all-15 / matched_4s_4s |
| Figure 4, scope CDF difference | `native_spectral_comparison.csv` | `data/validation/multi_workload/setup_comparison.csv`, power/excess |
| Figure 5, Hailo spectral tails | `hailo_spectra.csv` | `data/git/platform_spectral_metrics.csv`, matched_prefix, active/excess |
| Figure 6, Jetson deployed meters | `jetson_paired_300s.csv` | Per-execution outcomes, primary Jetson duration series, 300 s |
| Figure 7, Hailo DC/telemetry and AC | `paired_300s.csv` | Per-execution outcomes, primary Hailo duration series, 300 s |
| Figure 8, HailoRT duration / E–P–span | `paired_summary.csv`, `hailo_variable_interval_comparison.csv` | Same duration-series executions, each path's retained interval |
| Figure 9a, Jetson duration | `jetson_duration.csv` | Seven primary Jetson duration series, reference is own 600-s median |
| Figure 9b, Hailo duration | `duration.csv` | Three primary Hailo duration series, same within-series reference rule |
| Figure 10, fixed-rate pause test | `pause_timing.csv` | `data/pause/pause_runs.csv`, conditioning run excluded by design |
| Table I, experimental roles | Inline in `sections/instrumentation.tex` | Input inventories and `metadata/NUMERICAL_QA.json` |
| Table II, all nine energy intervals | `tables/jetson_reference.tex` | Native fixed-rate excerpt plus `scope_persistent_minima.csv` native columns |
| Table III, both-platform direct sweeps | `tables/direct_repeatability.tex` | All finite primary rate outcomes; unweighted mean of group means |
| Table IV, fixed-work acquisition control | `tables/controlled.tex` | Twelve stored outcomes in `combined_runs.csv`, additive model refit |

`generate_results.py` performs the shared result aggregation; the foundation
script selects existing outputs for fuller journal presentation and expands two
tables. `make_figures.py` is unchanged from v0.2. `verify_results.py` independently
recomputes pair ratios, quantiles and duration/direct-rate summaries, checks the
foundation selections and enforces the final native/all-15 convention.

The high-rate coverage paragraph uses
`data/robustness_20261009/high_rate_coverage.md`: 250-MS/s Tek observations,
GEMM-FP32 active-only and the remaining five workloads active-minus-idle. It is
not an energy-error or transfer-function calibration.

Full-precision pair values and percentiles remain available in
`generated/paired_all_durations.csv` and `generated/paired_summary.csv` even
when a manuscript plot shows only medians. The original signal transformations,
window policy and their limits remain in `METHOD_DETAILS.md` and `provenance/`.
