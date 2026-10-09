# Tabellen und Tabellendaten: paper-tim

[Zurück](README.md)

**Einordnung:** TIM v0.3.

[Vollständige Zuordnung zu den TIM-Abbildungs-/Tabellennummern](../../../papers/tim-v0.3/SOURCE_MAPPING.md).

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [scope fixed 2k excerpt](../../../papers/tim-v0.3/data/final_reconstruction/scope_fixed_2k_excerpt.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | nominal_duration_s, rate_sps, native_envelope_Q95_pct, via_1M_envelope_Q95_pct, source_csv_line |
| [fp16 energy selection](../../../papers/tim-v0.3/data/robustness_20261009/fp16_energy_selection.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | cohort, rate_sps, expected_ids, used_ids, complete_cohort, all_intervals_104s_within_2us, window_bases, min_duration_s … |
| [scope persistent minima](../../../papers/tim-v0.3/data/robustness_20261009/scope_persistent_minima.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | duration_s, tolerance_pct, native_min_rate_sps, native_first_pointwise_pass_sps, native_highest_failing_rate_sps, native_eligible_rate_count, via_1M_min_rate_sps, via_1M_first_pointwise_pass_sps … |
| [scope selected envelope](../../../papers/tim-v0.3/data/robustness_20261009/scope_selected_envelope.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | duration_s, rate_sps, native_envelope_Q95_pct, via_1M_envelope_Q95_pct |
| [f min by workload duration](../../../papers/tim-v0.3/data/validation/multi_workload/f_min_by_workload_duration.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload_id, workload_label, source, mode, duration_s, threshold_pct, f_min_sps, selection_rule |
| [highlighted rate thresholds](../../../papers/tim-v0.3/data/validation/multi_workload/highlighted_rate_thresholds.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload_id, workload_label, source, mode, highlighted_rate_sps, threshold_pct, minimum_passing_duration_s, selection_rule |
| [table cross workload fmin](../../../papers/tim-v0.3/data/validation/multi_workload/table_cross_workload_fmin.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | Workload, Setup, Duration [s], $f_{min,E}$ for 1\% |
| [table cross workload two k sufficiency](../../../papers/tim-v0.3/data/validation/multi_workload/table_cross_workload_two_k_sufficiency.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | Workload, Setup, Tolerance [\%], Minimum tested duration [s] |
| [fp16 energy](../../../papers/tim-v0.3/generated/fp16_energy.csv) | CSV | Vollständige Ergebnis- / Plotinputs | cohort, rate_sps, expected_ids, used_ids, complete_cohort, all_intervals_104s_within_2us, window_bases, min_duration_s … |
| [fp16 energy plot](../../../papers/tim-v0.3/generated/fp16_energy_plot.csv) | CSV | Vollständige Ergebnis- / Plotinputs | rate_sps, native_pooled_Q95_pct, native_max_pct, n_offset_cases |
| [jetson foundation energy](../../../papers/tim-v0.3/generated/jetson_foundation_energy.csv) | CSV | Vollständige Ergebnis- / Plotinputs | nominal_duration_s, rate_sps, native_envelope_Q95_pct, via_1M_envelope_Q95_pct, source_csv_line, persistent_1pct_sps, persistent_0p5pct_sps |
| [native reconstruction](../../../papers/tim-v0.3/generated/native_reconstruction.csv) | CSV | Vollständige Ergebnis- / Plotinputs | nominal_duration_s, rate_sps, native_envelope_Q95_pct, via_1M_envelope_Q95_pct, source_csv_line, persistent_1pct_sps, persistent_0p5pct_sps |
| [Tab. II — Jetson: neun Energieintervalle](../../../papers/tim-v0.3/tables/jetson_reference.tex) | TEX | Hauptabbildung / Haupttabelle |  |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
