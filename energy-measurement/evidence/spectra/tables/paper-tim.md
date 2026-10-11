# Tabellen und Tabellendaten: paper-tim

[Zurück](README.md)

**Einordnung:** TIM v0.3.

[Vollständige Zuordnung zu den TIM-Abbildungs-/Tabellennummern](../../../papers/tim-v0.3/SOURCE_MAPPING.md).

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [hailo psd selected rows](../../../papers/tim-v0.3/data/git/hailo_psd_selected_rows.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | key, workload, basis, window, physical_runs, active_duration_s, f95_median_hz, f95_q05_hz … |
| [platform spectral metrics](../../../papers/tim-v0.3/data/git/platform_spectral_metrics.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | key, workload_id, label, platform, setup, signal, basis, window … |
| [all spectral metrics](../../../papers/tim-v0.3/data/validation/multi_workload/all_spectral_metrics.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | key, workload_id, label, platform, setup, signal, basis, window … |
| [fp16 coverage](../../../papers/tim-v0.3/generated/fp16_coverage.csv) | CSV | Vollständige Ergebnis- / Plotinputs | rate_sps, median_pct, q05_pct, q95_pct, n |
| [fp16 coverage plot](../../../papers/tim-v0.3/generated/fp16_coverage_plot.csv) | CSV | Vollständige Ergebnis- / Plotinputs | rate_sps, median_pct, q05_pct, q95_pct, n |
| [hailo spectra](../../../papers/tim-v0.3/generated/hailo_spectra.csv) | CSV | Vollständige Ergebnis- / Plotinputs | key, workload_id, label, platform, setup, signal, basis, window … |
| [native spectral comparison](../../../papers/tim-v0.3/generated/native_spectral_comparison.csv) | CSV | Vollständige Ergebnis- / Plotinputs | workload_id, label, signal, basis, max_abs_cdf_difference_pp, conditional_0_77khz_max_abs_cdf_difference_pp, pico_to_tek_variance_ratio_db, ratio_interpretation … |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
