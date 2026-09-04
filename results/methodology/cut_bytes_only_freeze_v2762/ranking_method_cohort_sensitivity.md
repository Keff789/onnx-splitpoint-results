# Ranking method cohort sensitivity

Identical predictor methods are recomputed on technical, quality-pass, and pass-or-inconclusive cohorts. Subset correlations are diagnostic; global Hit@1 and Regret@1 remain unavailable unless the complete declared technical universe is paired.

| Model | Direction | Method | Cohort | n | Coverage | Spearman | Kendall | Global Hit@1 | Global Regret@1 | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | technical | 19 | 0.95 | 0.981495 | 0.934159 |  |  | diagnostic_available |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | technical | 19 | 0.95 | 0.280702 | 0.169591 |  |  | diagnostic_available |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | technical | 19 | 0.95 | -0.0649123 | -0.0409357 |  |  | diagnostic_available |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | technical | 19 | 0.95 | 0.398246 | 0.239766 |  |  | diagnostic_available |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 19 | 0.95 | -0.153576 | -0.105572 |  |  | diagnostic_available |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | technical | 19 | 0.95 | 0.968268 | 0.897998 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass | 2 | 0.1 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 16 | 0.8 | 0.949721 | 0.867344 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | weighted_score | technical | 19 | 0.95 | 0.298246 | 0.22807 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass | 2 | 0.1 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 16 | 0.8 | 0.0970588 | 0.133333 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | technical | 19 | 0.95 | -0.0210526 | 0.0175439 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass | 2 | 0.1 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 16 | 0.8 | -0.208824 | -0.0666667 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | technical | 19 | 0.95 | -0.0754386 | -0.0292398 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass | 2 | 0.1 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 16 | 0.8 | -0.247059 | -0.116667 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 19 | 0.95 | -0.370338 | -0.234605 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 2 | 0.1 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 16 | 0.8 | -0.420898 | -0.259416 |  |  | diagnostic_available |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo10h_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | technical | 19 | 0.95 | 0.550272 | 0.439959 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass | 3 | 0.15 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 17 | 0.85 | 0.552962 | 0.445438 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | weighted_score | technical | 19 | 0.95 | 0.563158 | 0.403509 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass | 3 | 0.15 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 17 | 0.85 | 0.593137 | 0.426471 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | technical | 19 | 0.95 | 0.473684 | 0.309942 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass | 3 | 0.15 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 17 | 0.85 | 0.492647 | 0.308824 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | technical | 19 | 0.95 | 0.417544 | 0.28655 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass | 3 | 0.15 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 17 | 0.85 | 0.42402 | 0.279412 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 19 | 0.95 | -0.272927 | -0.105572 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 3 | 0.15 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 17 | 0.85 | -0.280809 | -0.125462 |  |  | diagnostic_available |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | hailo8_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cut_bytes_only | technical | 19 | 0.95 | 0.255736 | 0.222993 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cut_bytes_only | quality_pass | 19 | 0.95 | 0.255736 | 0.222993 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 19 | 0.95 | 0.255736 | 0.222993 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | weighted_score | technical | 19 | 0.95 | 0.777193 | 0.590643 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | weighted_score | quality_pass | 19 | 0.95 | 0.777193 | 0.590643 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 19 | 0.95 | 0.777193 | 0.590643 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cycle_time_no_handover | technical | 19 | 0.95 | 0.810526 | 0.614035 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cycle_time_no_handover | quality_pass | 19 | 0.95 | 0.810526 | 0.614035 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 19 | 0.95 | 0.810526 | 0.614035 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cycle_time_with_handover | technical | 19 | 0.95 | 0.845614 | 0.660819 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cycle_time_with_handover | quality_pass | 19 | 0.95 | 0.845614 | 0.660819 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 19 | 0.95 | 0.845614 | 0.660819 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 19 | 0.95 | 0.588855 | 0.44575 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 19 | 0.95 | 0.588855 | 0.44575 |  |  | diagnostic_available |
| resnet50 | tensorrt_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 19 | 0.95 | 0.588855 | 0.44575 |  |  | diagnostic_available |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | technical | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass | 6 | 0.3 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | technical | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | quality_pass | 6 | 0.3 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | technical | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass | 6 | 0.3 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | technical | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass | 6 | 0.3 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 6 | 0.3 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 8 | 0.4 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | technical | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | technical | 1 | 0.05 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass | 0 | 0 |  |  |  |  | insufficient_candidates |
| yolo26s | deepx_m1_to_tensorrt | onnx_real_boundary_hardware_aware | quality_pass_or_inconclusive | 0 | 0 |  |  |  |  | insufficient_candidates |

_Only the first 240 of 540 rows are shown._

