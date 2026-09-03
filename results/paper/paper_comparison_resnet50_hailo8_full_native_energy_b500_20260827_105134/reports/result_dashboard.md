# Scientific Evaluation Report

Generated: `2026-08-27T11:00:24+02:00`
Profile: `paper_comparison_resnet50_hailo8_full_native_energy_b500`

## Decision summary

- Technical execution status: **failed**
- Quality-evaluation technical status: **failed**
- Quality-evaluation status: **failed**
- Aggregate quality decision: **not_evaluated**
- Scientific status: **not_evaluated**
- Development-analysis status: **incomplete**
- Claim readiness: **blocked** (0 claim-eligible row(s))
- Central quality results: **4 / 4** across **1** setup(s)
- Rows: **6**
- Performance observation rows: **4**
- Native energy attempts: **2** (**2** successful, **0** failed)
- Ranking eligible: **0**
- Performance eligible: **0**
- Energy eligible: **0**
- Development/screening performance observations: **4**
- Native setup-specific performance observations: **2** (matrix: **complete**)
- Native completed comparison endpoints: **0**
- Native host postprocessing: required **0**, available **0**, legacy-alias conflicts **0**
- Native runtime evidence: **complete**
- Native semantic evidence: **complete_pass**
- Native claim evidence: **ready**
- Native energy evidence: **complete**
- Technical status: **complete**
- Claim decisions complete: **True**
- Native energy attempts: **2 started, 0 not started**
- Energy plan completion: **2/2**
- Energy matrix coverage: **2/2**
- Energy claim eligible: **0**
- Final all-split energy complete: **True**
- Scientific status: **ready**
- Scientific ready: **True**
- Development/screening energy observations: **2**
- Campaign claim scope: **evaluated_matrix**
- Ranking-method comparison: **development_only**
- Best method under a common comparison coverage: **not available** (insufficient common coverage)
- Development diagnostic leader (not claim eligible): **not available** (minimum/coverage/strata prerequisites not met)
- Generic-to-Native ranking transfer: **insufficient_candidates** (0 paired candidates)

## Claim exclusion breakdown

- Performance excluded rows: **4**
- Energy excluded rows: **2**
- Exclusion reason assignments: **8**

### Grouped by model / backend / setup / reason

| Claim kind | Model | Backend | Setup | Reason | Count |
|---|---|---|---|---|---|
| performance | resnet50 | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | resnet50 | hailo8 | unknown_setup | contract_fail_or_unavailable | 1 |
| performance | resnet50 | tensorrt | orin_nx_hailo8_01 | screening_only | 2 |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_inconclusive | 1 |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | 1 |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |

### Stable detail rows

| Claim kind | Model | Backend | Setup | Reason | Case |
|---|---|---|---|---|---|
| performance | resnet50 | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | full |
| performance | resnet50 | hailo8 | unknown_setup | contract_fail_or_unavailable | full |
| performance | resnet50 | tensorrt | orin_nx_hailo8_01 | screening_only | b119 |
| performance | resnet50 | tensorrt | orin_nx_hailo8_01 | screening_only | full |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_inconclusive | full |
| energy | resnet50 | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | full |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | full |
| energy | resnet50 | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | full |

## Final-campaign readiness

- Claim scope: **evaluated_matrix**
- Status: **development_ready**
- Required failures: **0**

| Check | Status | Severity | Detail |
|---|---|---|---|
| campaign_mode | development | informational | Campaign remains development/screening. |
| claim_scope_valid | pass | required_for_final | Campaign claim_scope is evaluated_matrix or ranking_generalization. |
| claim_scope | pass | informational | The final claim is limited to the explicitly evaluated workload/hardware matrix. |
| profile_frozen | deferred | required_for_final | Profile and task-quality policy are marked frozen before the final campaign. |
| protocol_freeze_integrity | not_applicable | informational | A prospective five-manifest protocol freeze is optional for evaluated_matrix unless explicitly requested. |
| campaign_freeze_artifact | not_applicable | informational | No separate post-run campaign archive is required by this profile. |
| dataset_classification_calibration | pass | required_for_final | classification calibration dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/imagenet_train_calibration_manifest.json |
| dataset_classification_calibration_schema | pass | required_for_final | Dataset manifest task/role/schema match. |
| dataset_classification_calibration_content_hash | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| dataset_classification_calibration_current_files | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| dataset_classification_validation | pass | required_for_final | classification validation dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/imagenet_val_manifest.json |
| dataset_classification_validation_schema | pass | required_for_final | Dataset manifest task/role/schema match. |
| dataset_classification_validation_content_hash | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| dataset_classification_validation_current_files | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| dataset_detection_calibration | pass | required_for_final | detection calibration dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/coco2017_train_calibration_manifest.json |
| dataset_detection_calibration_schema | pass | required_for_final | Dataset manifest task/role/schema match. |
| dataset_detection_calibration_content_hash | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| dataset_detection_calibration_current_files | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| dataset_detection_validation | pass | required_for_final | detection validation dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/coco2017_val_manifest.json |
| dataset_detection_validation_schema | pass | required_for_final | Dataset manifest task/role/schema match. |
| dataset_detection_validation_content_hash | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| dataset_detection_validation_current_files | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| calibration_validation_disjoint | pass | required_for_final | Calibration and validation sets are content- and ID-disjoint. |
| pipeline_contract_manifest | deferred | required_for_final | Preprocessing/decoder/NMS contract manifest missing:  |
| development_models_present | pass | required_for_final | At least one development model is declared. |
| holdout_models_present | not_applicable | informational | No model-level hold-out is required because the claim is restricted to the evaluated matrix. |
| holdout_adapter_sources_frozen | not_applicable | informational | Prospective hold-out adapter freezing belongs to ranking_generalization, not evaluated_matrix. |
| model_role_disjoint | pass | required | Development and hold-out model IDs are disjoint. |
| model_ids_unique | pass | required_for_final | Every campaign model has a unique model ID. |
| model_role_explicit_resnet50 | pass | required_for_final | Model resnet50 explicitly declares evaluation_role=development or confirmatory_holdout. |
| model_family_id_explicit_resnet50 | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for resnet50. |
| model_generalization_scope_explicit_resnet50 | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for resnet50. |
| model_validation_tier_explicit_resnet50 | pass | required_for_final | Model resnet50 explicitly declares validation_tier. |
| model_validation_tier_final_resnet50 | deferred | required_for_final | Model resnet50 uses the final validation tier in a final campaign. |
| model_identity_resnet50 | pass | required_for_final | Model resnet50 resolves to an exact local model artefact with a content hash. |
| candidate_universe_resnet50 | pass | required_for_final | Model resnet50 explicitly declares its candidate-universe mode. |
| holdout_registry | not_applicable | informational | A hold-out registry is outside the evaluated_matrix claim scope. |
| holdout_registry_integrity | not_applicable | informational | No hold-out registry is consumed for evaluated_matrix claims. |
| ranking_validation_enabled | not_applicable | informational | Ranking validation is optional diagnostic output for evaluated_matrix and cannot enlarge the final claim. |
| ranking_model_bundle_integrity | not_applicable | informational | A fitted ranking bundle is required only for ranking_generalization. |
| stage_time_model | not_applicable | informational | A development-fitted ranking cost model is not a blocker for measured evaluated_matrix results. |
| native_handover_model | not_applicable | informational | Measured Native FIFO performance remains required, but a fitted handover predictor is not needed for evaluated_matrix claims. |
| native_full_baselines | pass | required_for_final | Native full baselines are enabled and use the same runtime contract whenever Native FIFO claims are enabled. |
| effective_energy_configuration | pass | required_for_final | One effective energy request is configured without conflicting generic/native enablement. |
| energy_window_method_ab | pass | required_for_final | The command-marker window is frozen as the scientific primary. The Chapter-4 legacy window is a same-trace, non-blocking sensitivity shadow; it never auto-switches, cannot invalidate the primary claim and requires no PicoScope rerun. |
| full_system_power_scope | deferred | required_for_final | Final energy campaign uses raw full-system input energy as the primary metric. |
| energy_command_window | deferred | required_for_final | Final full-system energy is bound to the command window. |
| energy_repetitions | deferred | required_for_final | Full-system energy uses at least three independent repetitions. |
| energy_confidence_interval | deferred | required_for_final | Repeated energy windows use a pre-declared confidence level of at least 95%. |
| energy_run_order | deferred | required_for_final | Final energy target blocks use a recorded deterministic random order with an explicit integer seed. |
| idle_normalization_policy | pass | required_for_final | Idle normalization reports raw and normalized values and uses a scope-compatible paired method. |
| energy_calibration_manifest | deferred | required_for_final | Full-system input-channel calibration manifest missing:  |


## Task-quality gates

| Model | Backend | Setup | Case | Variant | Technical | Tier | Metric | Delta | Lower bound | Bound evidence | Margin | Status | Gate reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | hailo8 | orin_nx_hailo8_01 | b119 | full | completed | screening | top1_accuracy | -0.002 | -0.014 | computed_95_percent_lcb | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | tensorrt | orin_nx_hailo8_01 | full | full | completed | screening | top1_accuracy | 0 |  | not_computed:candidate_reference_identical | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_hailo8_01 | b119 | composed | completed | screening | top1_accuracy | 0 |  | not_computed:candidate_reference_identical | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_hailo8_01 | b119 | full | completed | screening | top1_accuracy | 0 |  | not_computed:candidate_reference_identical | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |

## Development/screening performance observations

These rows are retained for debugging and method development but are explicitly not claim eligible.

| Model | Backend | Boundary | Latency ms | FPS | Quality | Eligibility | Reason |
|---|---|---|---|---|---|---|---|
| resnet50 | hailo8 | full | 8.18582 | 122.163 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8 | full | 8.18582 | 122.163 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | tensorrt | b119 | 2.19121 | 517.279 | pass | screening_only | screening_only |
| resnet50 | tensorrt | full | 1.98607 | 503.506 | pass | screening_only | screening_only |

## Native setup-specific performance matrix

Eligible Native comparison rows use the median and 95-percent confidence interval of independently initialized repetitions, never as a best-of value. Rows without verified independence remain visible and explicitly ineligible. FPS remains independent from any theoretical stage-cycle rate. These observations still require final-protocol admission before thesis claims.

| Model | Setup | Backend | Case | Mode | Claim | Input claim | Claim structure | Claim structurally clamped | Physical evidence conflict | Physical conflict fields | Mean IoU | Mean IoU threshold | Source E2E scope | E2E scope | E2E eligible | E2E reason | Endpoint stratum | Concurrency | Physical stage | Output format | Physical contract | Contract source | Physical contract complete | Physical contract hash | Accelerator stage | Accelerator contract | Accelerator contract hash | Comparison endpoint | Physical endpoint | Physical endpoint match | Comparison endpoint match | Comparison stratum explicit | Host decode/NMS required | Postprocess included | Postprocess location | Host tail frozen | Host postprocess required | Host tail required | Host postprocess available | Host tail available | Host postprocess evidence | Host evidence source | Host alias conflict | Decoder contract | NMS | Decoder ID | Postprocess completed frames | Postprocess completion verified | Frozen host contract hash | Completed stage | Completed contract | Completed contract hash | Completed endpoint | Completed comparison contract hash | Completed comparison endpoint | Completion mode | Completed endpoint attested | Completed attestation status | FPS median | Latency median [ms] | Latency CI95 low [ms] | Latency CI95 high [ms] | valid n | Aggregation | Theoretical cycle rate | Structure | Numerical | Task quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | orin_nx_hailo8_01 | native_full_hailo8 | full | native_full_baseline | True | True | True | False | False | [] |  |  | accelerator_output_endpoint | full_task_pipeline | True | native_full_non_detection_explicit_input_contract | classification_logits | 1 | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification_logits | classification_logits | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  | False | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  | 0 | True |  |  |  |  |  |  |  |  | True | passed | 121.986 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 121.986 | pass | passed | inconclusive |
| resnet50 | orin_nx_hailo8_01 | native_full_tensorrt | full | native_full_baseline | True | True | True | False | False | [] |  |  | unavailable | full_task_pipeline | True | native_full_non_detection_explicit_input_contract | classification_logits | 1 | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification_logits | classification_logits | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  | False | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  |  |  |  |  |  |  |  |  |  |  |  | not_required | 589.63 | 1.73305 | 1.73265 | 1.73745 | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 589.63 | pass | passed | pass |

## Development/screening energy observations

This table includes every Native energy attempt. Failed attempts remain visible, carry no invented numeric result and are always ineligible.

| Model | Backend | Boundary | Status | Power W | Energy/work J | Scope | Window | Failure | Reason |
|---|---|---|---|---|---|---|---|---|---|
| resnet50 | native_full_hailo8 | full | available | 17.1748 | 0.358874 | MB | command_window |  | screening_energy_policy_nonclaimable;native_accuracy_gate_inconclusive |
| resnet50 | native_full_tensorrt | full | available | 23.1533 | 0.102631 | MB | command_window |  | screening_energy_policy_nonclaimable;native_quality_claim_result_not_verified |

## Ranking-method comparison (macro)

| Method | Groups | Validated hold-outs | MAE ms | MAPE % | Spearman | Kendall | Diagnostic groups | Diagnostic Spearman | Diagnostic Kendall | Hit@5 | Elite R@5 | Regret@5 | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cut bytes only | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  | development_only |
| Weighted score | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  | development_only |
| Cycle time without handover | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  | development_only |
| Cycle time with runner/direction handover | 1 | 0 |  |  |  |  | 0 |  |  |  |  |  | development_only |

## Ranking-method comparison (per model/direction/runner)

| Model | Role | Direction | Runner | Method | n | Universe | Declared | Coverage | Frozen | MAE ms | MAPE % | Spearman | Kendall | Diagnostic n | Diagnostic Spearman | Diagnostic Kendall | Hit@5 | Elite R@5 | Regret@5 | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | development | tensorrt_to_tensorrt | generic | Cut bytes only | 0 | False | False | 0.00833333 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_candidates_for_correlation |
| resnet50 | development | tensorrt_to_tensorrt | generic | Weighted score | 0 | False | False | 0.00833333 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_candidates_for_correlation |
| resnet50 | development | tensorrt_to_tensorrt | generic | Cycle time without handover | 0 | False | False | 0.00833333 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_candidates_for_correlation |
| resnet50 | development | tensorrt_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | False | 0.00833333 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_candidates_for_correlation |

## Generic-to-Native ranking transfer

The same semantically valid candidate boundaries are compared under Generic and Native execution. Absolute Native throughput and energy remain Native-runner evidence; this section tests whether Generic ordering is a useful shortlist surrogate.

_No rows available._

## Open items

- **informational — campaign_development_mode**: Campaign status is development_ready; 9 final-only requirements remain deferred.
- **required_for_final — quality_profile_not_frozen**: Set quality_gate.frozen_before_final_campaign=true before the final campaign and archive the profile hash.
- **required_for_final — screening_dataset_only**: The configured task-quality tier is screening; these rows are not final task-quality evidence.
- **informational — ranking_generalization_out_of_scope**: The scientific claim is limited to the evaluated workload/hardware matrix; unseen-model ranking generalisation is not claimed.
