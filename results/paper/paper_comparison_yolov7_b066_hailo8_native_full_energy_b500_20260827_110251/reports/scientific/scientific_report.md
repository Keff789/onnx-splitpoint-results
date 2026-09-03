# Scientific Evaluation Report

Generated: `2026-08-27T11:59:12+02:00`
Profile: `paper_comparison_yolov7_b066_hailo8_native_full_energy_b500`

## Decision summary

- Technical execution status: **failed**
- Quality-evaluation technical status: **failed**
- Quality-evaluation status: **failed**
- Aggregate quality decision: **not_evaluated**
- Scientific status: **not_evaluated**
- Development-analysis status: **unavailable**
- Claim readiness: **blocked** (0 claim-eligible row(s))
- Central quality results: **5 / 5** across **1** setup(s)
- Rows: **11**
- Performance observation rows: **8**
- Native energy attempts: **3** (**0** successful, **3** failed)
- Ranking eligible: **0**
- Performance eligible: **0**
- Energy eligible: **0**
- Development/screening performance observations: **8**
- Native setup-specific performance observations: **3** (matrix: **complete**)
- Native completed comparison endpoints: **3**
- Native host postprocessing: required **3**, available **3**, legacy-alias conflicts **0**
- Native runtime evidence: **complete**
- Native semantic evidence: **complete_pass**
- Native claim evidence: **ready**
- Native energy evidence: **measurement_failed**
- Technical status: **incomplete**
- Claim decisions complete: **True**
- Native energy attempts: **3 started, 0 not started**
- Energy plan completion: **0/3**
- Energy matrix coverage: **0/3**
- Energy claim eligible: **0**
- Final all-split energy complete: **False**
- Scientific status: **not_ready**
- Scientific ready: **False**
- Development/screening energy observations: **0**
- Campaign claim scope: **evaluated_matrix**
- Ranking-method comparison: **disabled**
- Best method under a common comparison coverage: **not available** (insufficient common coverage)
- Development diagnostic leader (not claim eligible): **not available** (minimum/coverage/strata prerequisites not met)
- Generic-to-Native ranking transfer: **insufficient_candidates** (1 paired candidates)

## Claim exclusion breakdown

- Performance excluded rows: **8**
- Energy excluded rows: **3**
- Exclusion reason assignments: **36**

### Grouped by model / backend / setup / reason

| Claim kind | Model | Backend | Setup | Reason | Count |
|---|---|---|---|---|---|
| performance | yolov7_paper | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo8 | unknown_setup | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo8_to_tensorrt | unknown_setup | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | 2 |
| performance | yolov7_paper | tensorrt | unknown_setup | contract_fail_or_unavailable | 2 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | effective_command_window_not_verified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | final_energy_gate_not_passed | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | measurement_execution_failed | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_output_endpoint_not_verified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | postprocess_not_ok | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | raw_input_energy_not_primary | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | 1 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | effective_command_window_not_verified | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | exact_runtime_work_units_missing | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | final_energy_gate_not_passed | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | measurement_execution_failed | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_not_passed | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | postprocess_not_ok | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | raw_input_energy_not_primary | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | 1 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | effective_command_window_not_verified | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | final_energy_gate_not_passed | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | measurement_execution_failed | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | postprocess_not_ok | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | raw_input_energy_not_primary | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | 1 |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | 1 |

### Stable detail rows

| Claim kind | Model | Backend | Setup | Reason | Case |
|---|---|---|---|---|---|
| performance | yolov7_paper | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | full |
| performance | yolov7_paper | hailo8 | unknown_setup | contract_fail_or_unavailable | full |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b066 |
| performance | yolov7_paper | hailo8_to_tensorrt | unknown_setup | contract_fail_or_unavailable | b066 |
| performance | yolov7_paper | tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b066 |
| performance | yolov7_paper | tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | full |
| performance | yolov7_paper | tensorrt | unknown_setup | contract_fail_or_unavailable | b066 |
| performance | yolov7_paper | tensorrt | unknown_setup | contract_fail_or_unavailable | full |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | effective_command_window_not_verified | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | final_energy_gate_not_passed | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | measurement_execution_failed | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_output_endpoint_not_verified | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | postprocess_not_ok | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | raw_input_energy_not_primary | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | b066 |
| energy | yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | b066 |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | effective_command_window_not_verified | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | exact_runtime_work_units_missing | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | final_energy_gate_not_passed | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | measurement_execution_failed | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | native_accuracy_gate_not_passed | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | postprocess_not_ok | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | raw_input_energy_not_primary | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | full |
| energy | yolov7_paper | native_full_hailo8 | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | effective_command_window_not_verified | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | exact_runtime_work_units_missing | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | final_energy_gate_not_passed | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | measurement_execution_failed | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | native_quality_claim_result_not_verified | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | postprocess_not_ok | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | raw_input_energy_not_primary | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | scientific_primary_unavailable_or_unverified | full |
| energy | yolov7_paper | native_full_tensorrt | orin_nx_hailo8_01 | screening_energy_policy_nonclaimable | full |

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
| model_role_explicit_yolov7_paper | pass | required_for_final | Model yolov7_paper explicitly declares evaluation_role=development or confirmatory_holdout. |
| model_family_id_explicit_yolov7_paper | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for yolov7_paper. |
| model_generalization_scope_explicit_yolov7_paper | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for yolov7_paper. |
| model_validation_tier_explicit_yolov7_paper | pass | required_for_final | Model yolov7_paper explicitly declares validation_tier. |
| model_validation_tier_final_yolov7_paper | deferred | required_for_final | Model yolov7_paper uses the final validation tier in a final campaign. |
| model_identity_yolov7_paper | pass | required_for_final | Model yolov7_paper resolves to an exact local model artefact with a content hash. |
| candidate_universe_yolov7_paper | pass | required_for_final | Model yolov7_paper explicitly declares its candidate-universe mode. |
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
| yolov7_paper | hailo8 | orin_nx_hailo8_01 | b066 | full | completed | screening | coco_ap_50_95 | -0.0372354 |  | not_computed:point_estimate_below_non_inferiority_margin | 0.01 | fail | primary:coco_ap_50_95:decision:fail;primary:coco_ap_50_95:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:ap50:decision:pass;guardrail:ap50:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:ap75:decision:fail;guardrail:ap75:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| yolov7_paper | hailo8_to_trt | orin_nx_hailo8_01 | b066 | composed | completed | screening | coco_ap_50_95 | 0.00584413 | 0.00139443 | computed_95_percent_lcb | 0.01 | pass | primary:coco_ap_50_95:decision:pass;guardrail:ap50:decision:pass;guardrail:ap75:decision:pass |
| yolov7_paper | tensorrt | orin_nx_hailo8_01 | full | full | completed | screening | coco_ap_50_95 | 0.00911436 | 0.00655194 | computed_95_percent_lcb | 0.01 | pass | primary:coco_ap_50_95:decision:pass;guardrail:ap50:decision:pass;guardrail:ap75:decision:pass |
| yolov7_paper | ort_tensorrt | orin_nx_hailo8_01 | b066 | composed | completed | screening | coco_ap_50_95 | 0.00915388 | 0.00663746 | computed_95_percent_lcb | 0.01 | pass | primary:coco_ap_50_95:decision:pass;guardrail:ap50:decision:pass;guardrail:ap75:decision:pass |
| yolov7_paper | ort_tensorrt | orin_nx_hailo8_01 | b066 | full | completed | screening | coco_ap_50_95 | 0.00911436 | 0.00655194 | computed_95_percent_lcb | 0.01 | pass | primary:coco_ap_50_95:decision:pass;guardrail:ap50:decision:pass;guardrail:ap75:decision:pass |

## Development/screening performance observations

These rows are retained for debugging and method development but are explicitly not claim eligible.

| Model | Backend | Boundary | Latency ms | FPS | Quality | Eligibility | Reason |
|---|---|---|---|---|---|---|---|
| yolov7_paper | hailo8 | full | 62.4917 | 16.0021 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolov7_paper | hailo8 | full | 62.4917 | 16.0021 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolov7_paper | hailo8_to_tensorrt | b066 | 19.08 | 55.8708 | unavailable | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolov7_paper | hailo8_to_tensorrt | b066 | 19.08 | 55.8708 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolov7_paper | tensorrt | b066 | 23.9723 | 80.9055 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolov7_paper | tensorrt | b066 | 23.9723 | 82.2487 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolov7_paper | tensorrt | full | 18.1076 | 55.2254 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolov7_paper | tensorrt | full | 18.1076 | 55.2254 | pending_central_evaluation | contract_fail_or_unavailable | contract_fail_or_unavailable |

## Native setup-specific performance matrix

Eligible Native comparison rows use the median and 95-percent confidence interval of independently initialized repetitions, never as a best-of value. Rows without verified independence remain visible and explicitly ineligible. FPS remains independent from any theoretical stage-cycle rate. These observations still require final-protocol admission before thesis claims.

| Model | Setup | Backend | Case | Mode | Claim | Input claim | Claim structure | Claim structurally clamped | Physical evidence conflict | Physical conflict fields | Mean IoU | Mean IoU threshold | Source E2E scope | E2E scope | E2E eligible | E2E reason | Endpoint stratum | Concurrency | Physical stage | Output format | Physical contract | Contract source | Physical contract complete | Physical contract hash | Accelerator stage | Accelerator contract | Accelerator contract hash | Comparison endpoint | Physical endpoint | Physical endpoint match | Comparison endpoint match | Comparison stratum explicit | Host decode/NMS required | Postprocess included | Postprocess location | Host tail frozen | Host postprocess required | Host tail required | Host postprocess available | Host tail available | Host postprocess evidence | Host evidence source | Host alias conflict | Decoder contract | NMS | Decoder ID | Postprocess completed frames | Postprocess completion verified | Frozen host contract hash | Completed stage | Completed contract | Completed contract hash | Completed endpoint | Completed comparison contract hash | Completed comparison endpoint | Completion mode | Completed endpoint attested | Completed attestation status | FPS median | Latency median [ms] | Latency CI95 low [ms] | Latency CI95 high [ms] | valid n | Aggregation | Theoretical cycle rate | Structure | Numerical | Task quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| yolov7_paper | orin_nx_hailo8_01 | hailo8_to_trt | b066 | native_split | True | True | True | False | False | [] | 0.984648 | 0.85 | unavailable | full_task_pipeline | True | not_native_full |  |  | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | raw_head | raw_head |  | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | False | False | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True |  | decoded_nms | decoded_nms | 7932660305f4258664f0577a85f65b85f889f9ff1a6616d70687bbe1bba0c3b9 | detection:decoded_nms:7932660305f4258664f0577a85f65b85f889f9ff1a6616d70687bbe1bba0c3b9 | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection_completion_execution_v1 | True | passed | 15.8722 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 15.8826 | pass | passed | pass |
| yolov7_paper | orin_nx_hailo8_01 | native_full_hailo8 | full | native_full_baseline | True | True | True | False | False | [] | 0.875778 | 0.85 | full_task_pipeline | full_task_pipeline | True | raw_accelerator_endpoint_plus_attested_frozen_timed_host_decode_nms | decoded_nms | 1 | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | raw_head | raw_head | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True | True | True | serialized_host_tail_inside_measured_interval | True | True | True | True | True | passed | completed_task_host_postprocess_attestation_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True | b0e7914f935eb0475433b5167271dbd2b4e5975c8aed3d3511f429d9721cddd1 | decoded_nms | decoded_nms | be397a26bdc58ae57dadd2a310c0462230043153167cb627fd5335791cf06edb | detection:decoded_nms:be397a26bdc58ae57dadd2a310c0462230043153167cb627fd5335791cf06edb | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | frozen_host_tail | True | passed | 16.1525 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 16.1525 | pass | passed | fail |
| yolov7_paper | orin_nx_hailo8_01 | native_full_tensorrt | full | native_full_baseline | True | True | True | False | False | [] | 0.998919 | 0.85 | full_task_pipeline | full_task_pipeline | True | raw_accelerator_endpoint_plus_attested_frozen_timed_host_decode_nms | decoded_nms | 1 | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | raw_head | raw_head | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True | True | True |  | True | True | True | True | True | passed | completed_task_host_postprocess_attestation_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True | b0e7914f935eb0475433b5167271dbd2b4e5975c8aed3d3511f429d9721cddd1 | decoded_nms | decoded_nms | be397a26bdc58ae57dadd2a310c0462230043153167cb627fd5335791cf06edb | detection:decoded_nms:be397a26bdc58ae57dadd2a310c0462230043153167cb627fd5335791cf06edb | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | frozen_host_tail | True | passed | 18.8481 | 53.0526 | 52.9826 | 53.0607 | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 18.8481 | pass | passed | pass |

## Development/screening energy observations

This table includes every Native energy attempt. Failed attempts remain visible, carry no invented numeric result and are always ineligible.

| Model | Backend | Boundary | Status | Power W | Energy/work J | Scope | Window | Failure | Reason |
|---|---|---|---|---|---|---|---|---|---|
| yolov7_paper | hailo8_to_trt | b066 | measurement_failed |  |  | MB | unknown | mika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/native_energy_measurements/measurements/hailo8_to_trt__yolov7_paper__b066__orin_nx_hailo8_01__b4a9dc5882cc/plan_30671fc2278e429f908b23c535f15665/attempt_371677f5b7c94cd699c8d8c041ce10cd/repeat_retry_attempts/repeat_002/attempt_01/run_000/preflight/preflight_stderr.log", "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "attestation_path": "/home/kmi... | measurement_execution_failed;native_output_endpoint_not_verified;final_energy_gate_not_passed;postprocess_not_ok;exact_runtime_work_units_missing;effective_command_window_not_verified;raw_input_energy_not_primary;scientific_primary_unavailable_or_unverified;screening_energy_policy_nonclaimable;native_quality_claim_result_not_verified |
| yolov7_paper | native_full_hailo8 | full | measurement_failed |  |  | MB | unknown | 60827_110251/reports/native_energy_measurements/measurements/native_full_hailo8__yolov7_paper__full__orin_nx_hailo8_01__9b0225ee3618/plan_30671fc2278e429f908b23c535f15665/attempt_d3eb0b283acf4688855ac59b14156b7e/repeat_retry_attempts/repeat_002/attempt_01/run_000/preflight/preflight_stderr.log", "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "attestation_path": "/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_... | measurement_execution_failed;final_energy_gate_not_passed;postprocess_not_ok;exact_runtime_work_units_missing;effective_command_window_not_verified;raw_input_energy_not_primary;scientific_primary_unavailable_or_unverified;screening_energy_policy_nonclaimable;native_accuracy_gate_not_passed |
| yolov7_paper | native_full_tensorrt | full | measurement_failed |  |  | MB | unknown | y_measurements/measurements/native_full_tensorrt__yolov7_paper__full__orin_nx_hailo8_01__5d969ecc44a9/plan_30671fc2278e429f908b23c535f15665/attempt_c8ed1363e5634d3c93bf87f47e10ada5/repeat_retry_attempts/repeat_002/attempt_01/run_000/preflight/preflight_stderr.log", "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "attestation_path": "/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/reports/native_... | measurement_execution_failed;final_energy_gate_not_passed;postprocess_not_ok;exact_runtime_work_units_missing;effective_command_window_not_verified;raw_input_energy_not_primary;scientific_primary_unavailable_or_unverified;screening_energy_policy_nonclaimable;native_quality_claim_result_not_verified |

## Ranking-method comparison (macro)

_No rows available._

## Ranking-method comparison (per model/direction/runner)

_No rows available._

## Generic-to-Native ranking transfer

The same semantically valid candidate boundaries are compared under Generic and Native execution. Absolute Native throughput and energy remain Native-runner evidence; this section tests whether Generic ordering is a useful shortlist surrogate.

| Model | Direction | Contract | Technical n | Quality n | Claim n | n | Technical Spearman | Technical Concordance | Technical Hit@1 | Technical Regret@1 | Quality Spearman | Quality Concordance | Quality Hit@1 | Quality Regret@1 | Spearman | Kendall | Concordance | Native Hit@1 | Native Regret@1 | Generic/Native ratio | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| yolov7_paper | hailo8_to_tensorrt | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | insufficient_candidates |

## Open items

- **informational — campaign_development_mode**: Campaign status is development_ready; 9 final-only requirements remain deferred.
- **required_for_final — quality_profile_not_frozen**: Set quality_gate.frozen_before_final_campaign=true before the final campaign and archive the profile hash.
- **required_for_final — screening_dataset_only**: The configured task-quality tier is screening; these rows are not final task-quality evidence.
- **informational — ranking_generalization_out_of_scope**: The scientific claim is limited to the evaluated workload/hardware matrix; unseen-model ranking generalisation is not claimed.
