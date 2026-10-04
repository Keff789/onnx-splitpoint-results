# Curated input schema

All input CSVs have UTF-8 headers, decimal numbers, `True`/`False` booleans and blank unavailable values. Blank does not mean zero or a passed gate. Fields containing lists use JSON text. Setup aliases H8/H10/DeepX denote the three measured accelerator systems. `cohort` is `base` or `augmentation`; the separate short predecessor file uses `augmentation_short`. Backend/direction and precision retain the normal project identities. The original absolute source locations are excluded; the private source index and original archive retain them.

| Input | Row unit and essential interpretation |
|---|---|
| `generic_raw.csv` | One original Generic observation. `throughput_fps` refers to its explicit `measurement_endpoint`; only the 28 Full endpoints complete the task. |
| `generic_short_predecessors.csv` | One of twelve short augmentation predecessor observations, inventory only. It is neither a replacement nor a replicate of Generic completed-task timing. |
| `native_cases.csv` | One Native case, including Full baselines once. `fps` is the median of three completed-task repetitions. `native_quality_gate_status` preserves the Native report's own label, not an invented accuracy class. |
| `generic_cases.csv` | One actual Generic completed-task case, three repetitions. |
| `performance_repeats.csv` | One measured repetition. `completed_count`, `makespan_s` and both reported/recomputed FPS retain the direct arithmetic evidence. `measurement` distinguishes Native and Generic. |
| `completion_pairs.csv` | One model/case/setup pair with exact direction, precision, comparison backend, output endpoint and boundary class. Eligibility is retained independently for technical, quality and claim transfer. |
| `quality.csv` | One unique cohort/model/case/setup/backend/variant quality result. Top1 and COCO AP50:95, their deltas and paired CI bounds use the original fractional scale, not percent. `relative_loss` is also a fraction; plots explicitly multiply by 100. N/B/seed are verified central-result policies. |
| `quality_transfer_exclusions.csv` | The three technically eligible pairs that fail the unchanged stricter quality-transfer gate. Accuracy decisions remain separately visible. |
| `energy_cases.csv` | One Native energy case, three valid repetitions. Primary J/task is the mean of the per-repeat ratios; `energy_j`, `power_w` and `actual_duration_s` preserve case aggregates. `performance_fps` is explicitly separate historical Native context; `energy_window_throughput_fps` uses the energy-side workcounts and windows. |
| `energy_repeats.csv` | One valid energy repetition, with actual `completed_count`, `active_duration_s`, joules, watts and J/task. No separate performance FPS is used as a workcount. |
| `energy_physical_attempts.csv` | One actual `collector_started` budget chain. The stable row attempt index is not a logical repetition index. `role` separates the independent setup diagnostic. Failed and unconfirmed chains remain rows. The evidence SHA refers to the exact original chain object in the private budget. |
| `coverage.csv` | One of 588 original required scope entries. Original build/runtime status, raw representation, quality completion and decision are separate. |
| `energy_split_full_pairs.csv` | One descriptive Split↔Full comparison. The derived semantic projection and original semantic flag are both preserved. Pair counts must not be added to measurement counts. |
| `arithmetic_checks.csv` | One explicit stored-versus-derived numeric check. Error units follow the named check; errors are never pooled into a physical metric. |
| `semantics/` | The separate original stored-output comparison audit and 45-entry terminal-reason projection, with their own reproducible script and limitations. |

Constructed `case_uid` values disambiguate measurement/cohort and original case identities; they are analysis join keys, not new measurement authority. The compact projections retain the existing endpoint/command hashes where needed for comparison provenance. `input_manifest.json` covers the public inputs; original artifact and source SHA checks remain in the normal private evidence.

A Native **individual-observation** `claim_eligible` field may be true under its original report contract. It must not be confused with `eligible_for_claim_transfer` on a cross-runner pair or the energy pair's `claim_comparable`: all comparison claims in this release remain false. The measured observations stay available for descriptive analysis.

Derived `native_cv`/`generic_cv` values use sample standard deviation divided by the three-repetition mean. Ratios named `native_generic_ratio` mean Native completed FPS / Generic completed FPS. Energy ratios mean Split J/task / Full J/task. Regret is the dimensionless Native throughput-selection cycle penalty, not a measured latency.
