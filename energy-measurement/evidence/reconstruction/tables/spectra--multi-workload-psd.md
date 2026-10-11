# Tabellen und Tabellendaten: spectra--multi-workload-psd

[Zurück](README.md)

**Einordnung:** Originale Evidence / Zusatzprüfung.

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [cache energy qc](../../spectra/sources/multi-workload-psd/common_reference/cache_energy_qc.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload_id, workload_label, source, run, input_rate_sps, output_rate_sps, input_energy_j, output_energy_j … |
| [common reference summary](../../spectra/sources/multi-workload-psd/common_reference/common_reference_summary.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload_id, workload_label, source, mode, target_rate_sps, duration_s, physical_run_count, hierarchical_abs_error_q95_pct … |
| [f min by workload duration](../../spectra/sources/multi-workload-psd/common_reference/f_min_by_workload_duration.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload_id, workload_label, source, mode, duration_s, threshold_pct, f_min_sps, selection_rule |
| [highlighted rate thresholds](../../spectra/sources/multi-workload-psd/common_reference/highlighted_rate_thresholds.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload_id, workload_label, source, mode, highlighted_rate_sps, threshold_pct, minimum_passing_duration_s, selection_rule |
| [worst case envelope](../../spectra/sources/multi-workload-psd/common_reference/worst_case_envelope.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | source, mode, duration_s, threshold_pct, worst_case_f_min_sps, contributing_workloads, expected_workloads, complete_across_available_workloads … |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
