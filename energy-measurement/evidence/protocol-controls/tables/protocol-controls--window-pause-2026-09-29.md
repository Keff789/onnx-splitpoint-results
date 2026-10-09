# Tabellen und Tabellendaten: protocol-controls--window-pause-2026-09-29

[Zurück](README.md)

**Einordnung:** Originale Evidence / Zusatzprüfung.

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [iteration runs](../sources/window-pause-2026-09-29/data/iteration_runs.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | order, rate_Sps, run_id, reported_sample_rate_Sps, energy_J, yaml_duration_s, detected_duration_s, analysis_duration_s … |
| [pause latency groups](../sources/window-pause-2026-09-29/data/pause_latency_groups.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | run_id, conditioning, pause_s, group_of_ten, gpu_latency_mean_ms |
| [pause runs](../sources/window-pause-2026-09-29/data/pause_runs.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | index, conditioning, pause_s, actual_pause_s, trt_s, process_s, envelope_span_s, energy_J … |
| [pause window sensitivity](../sources/window-pause-2026-09-29/data/pause_window_sensitivity.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | fraction, median_20_J, median_120_J, relative_120_to_20_pct |
| [timeout rates](../sources/window-pause-2026-09-29/data/timeout_rates.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | protocol, rate_Sps, n, median_energy_J, median_duration_s, median_power_W, relative_energy_to_2000_pct, population_relative_sd_energy_pct |
| [window runs](../sources/window-pause-2026-09-29/data/window_runs.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | rate_Sps, run_id, order, yaml_sha256, status, recomputed_minus_yaml_J, legacy_start_index_inclusive, legacy_stop_index_inclusive … |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
