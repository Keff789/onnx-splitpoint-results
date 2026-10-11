# Tabellen und Tabellendaten: paper-tim

[Zurück](README.md)

**Einordnung:** TIM v0.3.

[Vollständige Zuordnung zu den TIM-Abbildungs-/Tabellennummern](../../../papers/tim-v0.3/SOURCE_MAPPING.md).

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [groups all candidates](../../../papers/tim-v0.3/data/final_direct/groups_all_candidates.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | series, window, sensor, axis_value, n, n_reported, run_ids, n_flagged … |
| [paper window policy](../../../papers/tim-v0.3/data/final_direct/paper_window_policy.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | series, label, paper_window, reason |
| [plotted candidates](../../../papers/tim-v0.3/data/final_direct/plotted_candidates.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | id, record_id, series, window, sensor, run_id, axis_value, energy_J … |
| [pause runs](../../../papers/tim-v0.3/data/pause/pause_runs.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | index, conditioning, pause_s, actual_pause_s, trt_s, process_s, envelope_span_s, energy_J … |
| [jetson calibration](../../../papers/tim-v0.3/data/validation/calibration/jetson_calibration.ods) | ODS | Zusatzdatei; nicht automatisch im Haupttext |  |
| [jetson calibration verification rows](../../../papers/tim-v0.3/data/validation/calibration/jetson_calibration_verification_rows.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | sheet, row, zero_target, actual_A, adjusted_A, signed_relative_error_pct, adjusted_formula |
| [balanced effects](../../../papers/tim-v0.3/data/validation/controlled/complementary/data/balanced_effects.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | metric, display, n_2kSps, n_5MSps, mean_2kSps, mean_5MSps, balanced_effect_5MSps_minus_2kSps, balanced_effect_percent_of_2kSps_mean … |
| [combined runs](../../../papers/tim-v0.3/data/validation/controlled/complementary/data/combined_runs.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | index, rate_Sps, TRT_queries, TRT_time_s, actual_pause_s, raw_bytes, sample_count, pico_pre_mean_voltage_V … |
| [position balance](../../../papers/tim-v0.3/data/validation/controlled/complementary/data/position_balance.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | position, v1.0.1_rate_Sps, v1.0.2_rate_Sps |
| [position contrasts](../../../papers/tim-v0.3/data/validation/controlled/complementary/data/position_contrasts.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | metric, display, position, session_5MSps, value_5MSps, session_2kSps, value_2kSps, difference_5MSps_minus_2kSps |
| [sequence slopes](../../../papers/tim-v0.3/data/validation/controlled/complementary/data/sequence_slopes.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | session, metric, slope_per_sequence_position, first_value, last_value, last_minus_first |
| [session rate summaries](../../../papers/tim-v0.3/data/validation/controlled/complementary/data/session_rate_summaries.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | session, metric, statistic, value_2kSps, value_5MSps, difference_5MSps_minus_2kSps, relative_difference_percent |
| [main summary](../../../papers/tim-v0.3/data/validation/controlled/fixed-window/data/main_summary.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload, n_per_rate, median_2k_W, median_250k_W, median_5M_W, median_250k_vs_2k_pct, median_5M_vs_2k_pct, std_2k_W … |
| [preload decomposition](../../../papers/tim-v0.3/data/validation/controlled/fixed-window/data/preload_decomposition.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload, mean_load_2k_W, mean_load_5M_W, mean_pre_2k_W, mean_pre_5M_W, load_difference_W, pre_difference_W, difference_of_load_minus_pre_W … |
| [run0 observation](../../../papers/tim-v0.3/data/validation/controlled/fixed-window/data/run0_observation.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload, run0_5M_load_W, min_other_5M_load_W, max_other_5M_load_W, run0_larger_than_all_other_5M, n_5M_below_2k_median, run0_mtime_is_earliest_in_5M, note |
| [subwindows](../../../papers/tim-v0.3/data/validation/controlled/fixed-window/data/subwindows.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload, fixed_20_80, fixed_20_40, fixed_40_60, fixed_60_80 |
| [cache energy qc](../../../papers/tim-v0.3/data/validation/multi_workload/cache_energy_qc.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload_id, workload_label, source, run, input_rate_sps, output_rate_sps, input_energy_j, output_energy_j … |
| [common reference summary](../../../papers/tim-v0.3/data/validation/multi_workload/common_reference_summary.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload_id, workload_label, source, mode, target_rate_sps, duration_s, physical_run_count, hierarchical_abs_error_q95_pct … |
| [setup comparison](../../../papers/tim-v0.3/data/validation/multi_workload/setup_comparison.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload_id, label, signal, basis, max_abs_cdf_difference_pp, conditional_0_77khz_max_abs_cdf_difference_pp, pico_to_tek_variance_ratio_db, ratio_interpretation … |
| [table cross workload idle load summary](../../../papers/tim-v0.3/data/validation/multi_workload/table_cross_workload_idle_load_summary.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | Workload, Idle runs, Idle duration [s], Active/idle [dB], Idle-overlap [\%], Additional under load [\%], Idle aggregation |
| [workload inventory](../../../papers/tim-v0.3/data/validation/multi_workload/workload_inventory.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | workload_id, workload_label, workload_family, workload_precision, configured_enabled, enabled, include_in_paper, scope_config … |
| [worst case envelope](../../../papers/tim-v0.3/data/validation/multi_workload/worst_case_envelope.csv) | CSV | Zusatzdatei; nicht automatisch im Haupttext | source, mode, duration_s, threshold_pct, worst_case_f_min_sps, contributing_workloads, expected_workloads, complete_across_available_workloads … |
| [controlled effects](../../../papers/tim-v0.3/generated/controlled_effects.csv) | CSV | Vollständige Ergebnis- / Plotinputs | metric, label, mean_2k, mean_5M, effect_pct, ci95_low_pct, ci95_high_pct, df |
| [direct rates](../../../papers/tim-v0.3/generated/direct_rates.csv) | CSV | Vollständige Ergebnis- / Plotinputs | platform, slug, series, window, rates, finite_runs, max_cv_pct, max_group_displacement_pct … |
| [duration](../../../papers/tim-v0.3/generated/duration.csv) | CSV | Vollständige Ergebnis- / Plotinputs | platform, slug, series, window, requested_s, n, power_median_W, power_q05_W … |
| [Abb. 9a — Jetson: Benchmarkdauer](../../../papers/tim-v0.3/generated/jetson_duration.csv) | CSV | Vollständige Ergebnis- / Plotinputs | platform, slug, series, window, requested_s, n, power_median_W, power_q05_W … |
| [pause summary](../../../papers/tim-v0.3/generated/pause_summary.csv) | CSV | Vollständige Ergebnis- / Plotinputs | pause_s, n, runtime_median_s, start_gpu_median_C |
| [pause timing](../../../papers/tim-v0.3/generated/pause_timing.csv) | CSV | Vollständige Ergebnis- / Plotinputs | index, pause_s, actual_pause_s, trt_s, gpu_before_5s_median_C |
| [Tab. IV — Kontrollierter Festarbeitsvergleich](../../../papers/tim-v0.3/tables/controlled.tex) | TEX | Hauptabbildung / Haupttabelle |  |
| [Tab. III — Direkte Ratensweeps beider Plattformen](../../../papers/tim-v0.3/tables/direct_repeatability.tex) | TEX | Hauptabbildung / Haupttabelle |  |
| [hailo repeatability](../../../papers/tim-v0.3/tables/hailo_repeatability.tex) | TEX | Zusatzdatei; nicht automatisch im Haupttext |  |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
