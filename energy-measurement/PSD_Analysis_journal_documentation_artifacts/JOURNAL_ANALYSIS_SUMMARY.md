# Journal PSD analysis

- Tool: `0.9.0`
- Status: **completed**
- Jetson workloads with native Tek/Pico spectra: 6
- Additional platform series: 12
- Figures: 63
- Input records unavailable/skipped: 0

## Start with these figures

`pico_vs_tek_psd/figures/pico_cross_workload_current_cumulative.pdf`
`pico_vs_tek_psd/figures/tek_vs_pico_current_cumulative_overlay.pdf`
`pico_vs_tek_psd/figures/tek_vs_pico_current_conditional_cumulative_0_77khz.pdf`
`pico_vs_tek_psd/figures/tek_vs_pico_current_cumulative_difference.pdf`

Individual workload overlays and absolute PSDs are under `pico_vs_tek_psd/figures/per_workload/`.
Platform results and their comparison limits are under `cross_platform_psd/`.

## Data and interpretation

Existing native Jetson spectra were read, not remeasured or regenerated. No PARMA result or Common-Reference cache was modified.
Additional legacy power NPYs use their declared rate and exact inclusive YAML sample window, an energy consistency check, and memory-bounded native Welch.
Full windows and duration-matched prefixes remain separate. Independent physical runs are not concatenated. Missing idle is not replaced with zero or Jetson idle.
All frequency percentiles are explicitly labelled as per-run medians or derived from the pointwise-median curve. They need not be equal.
The 77-kHz marker is not a hard cutoff. Conditional low-band CDFs distinguish shape changes from full-band denominator changes.
Cross-platform plots are exploratory unless measurement boundary, setup, precision, model and operating state are independently matched.

## Review bundle

The compact ZIP includes PDF/PNG, exact numeric tables, LaTeX snippets, source metadata and thinned review curves. No raw waveform or NPZ cache is copied.
Native aggregate files remain local and are identified by their source metadata. This is a review bundle, not a raw-data archive.
