# Final campaign readiness

- Campaign: `BiggerSet`
- Mode: `development`
- Enforcement: `warn`
- Claim scope: `evaluated_matrix`
- Status: **development_ready**
- Required failures: **0**
- Deferred final requirements: **15**
- Pending post-run requirements: **0**

| Check | Status | Severity | Detail |
|---|---|---|---|
| `campaign_mode` | development | informational | Campaign remains development/screening. |
| `claim_scope_valid` | pass | required_for_final | Campaign claim_scope is evaluated_matrix or ranking_generalization. |
| `claim_scope` | pass | informational | The final claim is limited to the explicitly evaluated workload/hardware matrix. |
| `profile_frozen` | deferred | required_for_final | Profile and task-quality policy are marked frozen before the final campaign. |
| `protocol_freeze_integrity` | not_applicable | informational | A prospective five-manifest protocol freeze is optional for evaluated_matrix unless explicitly requested. |
| `campaign_freeze_artifact` | not_applicable | informational | No separate post-run campaign archive is required by this profile. |
| `dataset_classification_calibration` | pass | required_for_final | classification calibration dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/imagenet_train_calibration_manifest.json |
| `dataset_classification_calibration_schema` | pass | required_for_final | Dataset manifest task/role/schema match. |
| `dataset_classification_calibration_content_hash` | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| `dataset_classification_calibration_current_files` | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| `dataset_classification_validation` | pass | required_for_final | classification validation dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/imagenet_val_manifest.json |
| `dataset_classification_validation_schema` | pass | required_for_final | Dataset manifest task/role/schema match. |
| `dataset_classification_validation_content_hash` | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| `dataset_classification_validation_current_files` | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| `dataset_detection_calibration` | pass | required_for_final | detection calibration dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/coco2017_train_calibration_manifest.json |
| `dataset_detection_calibration_schema` | pass | required_for_final | Dataset manifest task/role/schema match. |
| `dataset_detection_calibration_content_hash` | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| `dataset_detection_calibration_current_files` | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| `dataset_detection_validation` | pass | required_for_final | detection validation dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/manifests/coco2017_val_manifest.json |
| `dataset_detection_validation_schema` | pass | required_for_final | Dataset manifest task/role/schema match. |
| `dataset_detection_validation_content_hash` | pass | required_for_final | Final manifests use per-item content hashes and a non-empty identity hash. |
| `dataset_detection_validation_current_files` | pass | required_for_final | Dataset manifest verification passed in sampled mode. |
| `calibration_validation_disjoint` | pass | required_for_final | Calibration and validation sets are content- and ID-disjoint. |
| `pipeline_contract_manifest` | deferred | required_for_final | Preprocessing/decoder/NMS contract manifest missing:  |
| `development_models_present` | pass | required_for_final | At least one development model is declared. |
| `holdout_models_present` | not_applicable | informational | No model-level hold-out is required because the claim is restricted to the evaluated matrix. |
| `holdout_adapter_sources_frozen` | not_applicable | informational | Prospective hold-out adapter freezing belongs to ranking_generalization, not evaluated_matrix. |
| `model_role_disjoint` | pass | required | Development and hold-out model IDs are disjoint. |
| `model_ids_unique` | pass | required_for_final | Every campaign model has a unique model ID. |
| `model_role_explicit_mobilenet_v3_large` | pass | required_for_final | Model mobilenet_v3_large explicitly declares evaluation_role=development or confirmatory_holdout. |
| `model_family_id_explicit_mobilenet_v3_large` | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for mobilenet_v3_large. |
| `model_generalization_scope_explicit_mobilenet_v3_large` | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for mobilenet_v3_large. |
| `model_validation_tier_explicit_mobilenet_v3_large` | pass | required_for_final | Model mobilenet_v3_large explicitly declares validation_tier. |
| `model_validation_tier_final_mobilenet_v3_large` | deferred | required_for_final | Model mobilenet_v3_large uses the final validation tier in a final campaign. |
| `model_identity_mobilenet_v3_large` | pass | required_for_final | Model mobilenet_v3_large resolves to an exact local model artefact with a content hash. |
| `candidate_universe_mobilenet_v3_large` | pass | required_for_final | Model mobilenet_v3_large explicitly declares its candidate-universe mode. |
| `model_role_explicit_resnet50` | pass | required_for_final | Model resnet50 explicitly declares evaluation_role=development or confirmatory_holdout. |
| `model_family_id_explicit_resnet50` | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for resnet50. |
| `model_generalization_scope_explicit_resnet50` | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for resnet50. |
| `model_validation_tier_explicit_resnet50` | pass | required_for_final | Model resnet50 explicitly declares validation_tier. |
| `model_validation_tier_final_resnet50` | deferred | required_for_final | Model resnet50 uses the final validation tier in a final campaign. |
| `model_identity_resnet50` | pass | required_for_final | Model resnet50 resolves to an exact local model artefact with a content hash. |
| `candidate_universe_resnet50` | pass | required_for_final | Model resnet50 explicitly declares its candidate-universe mode. |
| `model_role_explicit_yolo11l` | pass | required_for_final | Model yolo11l explicitly declares evaluation_role=development or confirmatory_holdout. |
| `model_family_id_explicit_yolo11l` | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for yolo11l. |
| `model_generalization_scope_explicit_yolo11l` | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for yolo11l. |
| `model_validation_tier_explicit_yolo11l` | pass | required_for_final | Model yolo11l explicitly declares validation_tier. |
| `model_validation_tier_final_yolo11l` | deferred | required_for_final | Model yolo11l uses the final validation tier in a final campaign. |
| `model_identity_yolo11l` | pass | required_for_final | Model yolo11l resolves to an exact local model artefact with a content hash. |
| `candidate_universe_yolo11l` | pass | required_for_final | Model yolo11l explicitly declares its candidate-universe mode. |
| `model_role_explicit_yolov7_ultralytics` | pass | required_for_final | Model yolov7_ultralytics explicitly declares evaluation_role=development or confirmatory_holdout. |
| `model_family_id_explicit_yolov7_ultralytics` | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for yolov7_ultralytics. |
| `model_generalization_scope_explicit_yolov7_ultralytics` | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for yolov7_ultralytics. |
| `model_validation_tier_explicit_yolov7_ultralytics` | pass | required_for_final | Model yolov7_ultralytics explicitly declares validation_tier. |
| `model_validation_tier_final_yolov7_ultralytics` | deferred | required_for_final | Model yolov7_ultralytics uses the final validation tier in a final campaign. |
| `model_identity_yolov7_ultralytics` | pass | required_for_final | Model yolov7_ultralytics resolves to an exact local model artefact with a content hash. |
| `candidate_universe_yolov7_ultralytics` | pass | required_for_final | Model yolov7_ultralytics explicitly declares its candidate-universe mode. |
| `model_role_explicit_yolo26m` | pass | required_for_final | Model yolo26m explicitly declares evaluation_role=development or confirmatory_holdout. |
| `model_family_id_explicit_yolo26m` | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for yolo26m. |
| `model_generalization_scope_explicit_yolo26m` | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for yolo26m. |
| `model_validation_tier_explicit_yolo26m` | pass | required_for_final | Model yolo26m explicitly declares validation_tier. |
| `model_validation_tier_final_yolo26m` | deferred | required_for_final | Model yolo26m uses the final validation tier in a final campaign. |
| `model_identity_yolo26m` | pass | required_for_final | Model yolo26m resolves to an exact local model artefact with a content hash. |
| `candidate_universe_yolo26m` | pass | required_for_final | Model yolo26m explicitly declares its candidate-universe mode. |
| `model_role_explicit_yolo26x` | pass | required_for_final | Model yolo26x explicitly declares evaluation_role=development or confirmatory_holdout. |
| `model_family_id_explicit_yolo26x` | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for yolo26x. |
| `model_generalization_scope_explicit_yolo26x` | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for yolo26x. |
| `model_validation_tier_explicit_yolo26x` | pass | required_for_final | Model yolo26x explicitly declares validation_tier. |
| `model_validation_tier_final_yolo26x` | deferred | required_for_final | Model yolo26x uses the final validation tier in a final campaign. |
| `model_identity_yolo26x` | pass | required_for_final | Model yolo26x resolves to an exact local model artefact with a content hash. |
| `candidate_universe_yolo26x` | pass | required_for_final | Model yolo26x explicitly declares its candidate-universe mode. |
| `model_role_explicit_yolo26s` | pass | required_for_final | Model yolo26s explicitly declares evaluation_role=development or confirmatory_holdout. |
| `model_family_id_explicit_yolo26s` | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for yolo26s. |
| `model_generalization_scope_explicit_yolo26s` | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for yolo26s. |
| `model_validation_tier_explicit_yolo26s` | pass | required_for_final | Model yolo26s explicitly declares validation_tier. |
| `model_validation_tier_final_yolo26s` | deferred | required_for_final | Model yolo26s uses the final validation tier in a final campaign. |
| `model_identity_yolo26s` | pass | required_for_final | Model yolo26s resolves to an exact local model artefact with a content hash. |
| `candidate_universe_yolo26s` | pass | required_for_final | Model yolo26s explicitly declares its candidate-universe mode. |
| `holdout_registry` | not_applicable | informational | A hold-out registry is outside the evaluated_matrix claim scope. |
| `holdout_registry_integrity` | not_applicable | informational | No hold-out registry is consumed for evaluated_matrix claims. |
| `ranking_validation_enabled` | not_applicable | informational | Ranking validation is optional diagnostic output for evaluated_matrix and cannot enlarge the final claim. |
| `ranking_model_bundle_integrity` | not_applicable | informational | A fitted ranking bundle is required only for ranking_generalization. |
| `stage_time_model` | not_applicable | informational | A development-fitted ranking cost model is not a blocker for measured evaluated_matrix results. |
| `native_handover_model` | not_applicable | informational | Measured Native FIFO performance remains required, but a fitted handover predictor is not needed for evaluated_matrix claims. |
| `native_full_baselines` | pass | required_for_final | Native full baselines are enabled and use the same runtime contract whenever Native FIFO claims are enabled. |
| `effective_energy_configuration` | pass | required_for_final | One effective energy request is configured without conflicting generic/native enablement. |
| `energy_window_method_ab` | pass | required_for_final | The command-marker window is frozen as the scientific primary. The Chapter-4 legacy window is a same-trace, non-blocking sensitivity shadow; it never auto-switches, cannot invalidate the primary claim and requires no PicoScope rerun. |
| `full_system_power_scope` | deferred | required_for_final | Final energy campaign uses raw full-system input energy as the primary metric. |
| `energy_command_window` | deferred | required_for_final | Final full-system energy is bound to the command window. |
| `energy_repetitions` | deferred | required_for_final | Full-system energy uses at least three independent repetitions. |
| `energy_confidence_interval` | deferred | required_for_final | Repeated energy windows use a pre-declared confidence level of at least 95%. |
| `energy_run_order` | deferred | required_for_final | Final energy target blocks use a recorded deterministic random order with an explicit integer seed. |
| `idle_normalization_policy` | pass | required_for_final | Idle normalization reports raw and normalized values and uses a scope-compatible paired method. |
| `energy_calibration_manifest` | deferred | required_for_final | Full-system input-channel calibration manifest missing:  |

## Interpretation

`development_ready` means the development workflow can run while final-only requirements remain explicitly deferred. `final_ready` validates the frozen software-side protocol and referenced hashes. Neither status manufactures missing measurements, proves that a human hold-out attestation is truthful, or replaces the final hardware campaign.
