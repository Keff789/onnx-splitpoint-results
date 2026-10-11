# Tabellen und Tabellendaten: protocol-controls--controlled-rate-2026-10-01

[Zurück](README.md)

**Einordnung:** Originale Evidence / Zusatzprüfung.

| Datei | Format | Einordnung | Verfügbare Spalten (Auszug) |
|---|---|---|---|
| [balanced effects](../sources/controlled-rate-2026-10-01/complementary/data/balanced_effects.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | metric, display, n_2kSps, n_5MSps, mean_2kSps, mean_5MSps, balanced_effect_5MSps_minus_2kSps, balanced_effect_percent_of_2kSps_mean … |
| [combined runs](../sources/controlled-rate-2026-10-01/complementary/data/combined_runs.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | index, rate_Sps, TRT_queries, TRT_time_s, actual_pause_s, raw_bytes, sample_count, pico_pre_mean_voltage_V … |
| [position balance](../sources/controlled-rate-2026-10-01/complementary/data/position_balance.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | position, v1.0.1_rate_Sps, v1.0.2_rate_Sps |
| [position contrasts](../sources/controlled-rate-2026-10-01/complementary/data/position_contrasts.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | metric, display, position, session_5MSps, value_5MSps, session_2kSps, value_2kSps, difference_5MSps_minus_2kSps |
| [sequence slopes](../sources/controlled-rate-2026-10-01/complementary/data/sequence_slopes.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | session, metric, slope_per_sequence_position, first_value, last_value, last_minus_first |
| [session rate summaries](../sources/controlled-rate-2026-10-01/complementary/data/session_rate_summaries.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | session, metric, statistic, value_2kSps, value_5MSps, difference_5MSps_minus_2kSps, relative_difference_percent |
| [controlled-group-stats](../sources/controlled-rate-2026-10-01/data/controlled-group-stats.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | metric, mean_2k, mean_5M, mean_difference_5M_minus_2k, mean_relative_difference_pct, median_2k, median_5M, median_difference_5M_minus_2k … |
| [historical-endpoint-decomposition](../sources/controlled-rate-2026-10-01/data/historical-endpoint-decomposition.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload, n_2k, n_5M, pre_2k_W, pre_5M_W, pre_difference_W, pre_relative_difference_pct, load_2k_W … |
| [main summary](../sources/controlled-rate-2026-10-01/fixed-window/data/main_summary.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload, n_per_rate, median_2k_W, median_250k_W, median_5M_W, median_250k_vs_2k_pct, median_5M_vs_2k_pct, std_2k_W … |
| [preload decomposition](../sources/controlled-rate-2026-10-01/fixed-window/data/preload_decomposition.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload, mean_load_2k_W, mean_load_5M_W, mean_pre_2k_W, mean_pre_5M_W, load_difference_W, pre_difference_W, difference_of_load_minus_pre_W … |
| [run0 observation](../sources/controlled-rate-2026-10-01/fixed-window/data/run0_observation.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload, run0_5M_load_W, min_other_5M_load_W, max_other_5M_load_W, run0_larger_than_all_other_5M, n_5M_below_2k_median, run0_mtime_is_earliest_in_5M, note |
| [subwindows](../sources/controlled-rate-2026-10-01/fixed-window/data/subwindows.csv) | CSV | Originale Evidence / Zusatzprüfung; siehe Quellenzuordnung | workload, fixed_20_80, fixed_20_40, fixed_40_60, fixed_60_80 |

CSV-Dateien können vollständige Run-/Paarwerte oder Plotinputs enthalten; sie sind nicht automatisch zusätzliche Tabellen im Manuskript.
