# Tabellen und Tabellendaten: reconstruction--offline-robustness-2026-10-09

[Zurück](README.md)

**Einordnung:** Originale Evidence / Zusatzprüfung.

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [fp16 energy selection](../sources/offline-robustness-2026-10-09/fp16/fp16_energy_selection.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | cohort, rate_sps, expected_ids, used_ids, complete_cohort, all_intervals_104s_within_2us, window_bases, min_duration_s … |
| [fp16 psd per run](../sources/offline-robustness-2026-10-09/fp16/fp16_psd_per_run.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | run_id, status, branch, positive_excess_variance_W2, signed_excess_variance_W2, negative_excess_variance_W2, f95_hz, f99_hz … |
| [scope envelope original comparison](../sources/offline-robustness-2026-10-09/review/scope_envelope_original_comparison.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | duration_s, rate_sps, native_Q95_pct, via_1M_Q95_pct, original_phase_only_Q95_pct, native_minus_via_pp, via_minus_original_pp, native_minus_original_pp … |
| [scope persistent minima](../sources/offline-robustness-2026-10-09/review/scope_persistent_minima.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | duration_s, tolerance_pct, native_min_rate_sps, native_first_pointwise_pass_sps, native_highest_failing_rate_sps, native_eligible_rate_count, via_1M_min_rate_sps, via_1M_first_pointwise_pass_sps … |
| [scope envelope](../sources/offline-robustness-2026-10-09/scopes/scope_envelope.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | nominal_duration_s, rate_sps, n_workload_source_groups, complete_requested_cohort, all_six_paper_workloads_and_ids, native_envelope_Q95_pct, via_1M_envelope_Q95_pct, native_minus_via_Q95_pp … |
| [scope groups](../sources/offline-robustness-2026-10-09/scopes/scope_groups.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload, source, nominal_duration_s, rate_sps, expected_ids, used_ids, complete_requested_cohort, n_physical_records … |
| [scope per run](../sources/offline-robustness-2026-10-09/scopes/scope_per_run.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload, source, run_id, nominal_duration_s, rate_sps, n_windows, n_offsets_cases, ineligible_offset_cases … |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
