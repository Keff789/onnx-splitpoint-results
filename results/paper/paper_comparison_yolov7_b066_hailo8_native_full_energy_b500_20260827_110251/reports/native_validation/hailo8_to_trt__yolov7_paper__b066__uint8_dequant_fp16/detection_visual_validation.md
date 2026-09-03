# Native detection semantic validation

Manifest: `/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/native_producers/hailo8/yolov7_paper/benchmark_set/native_pipeline/b066/hailo_to_trt/uint8_dequant_fp16/native_fifo_outputs/native_fifo_output_manifest.json`

Reference: `/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/models/yolov7_paper/benchmark_results/remote_diagnostics/case_reports/results/b066/results_ort_tensorrt/validation_report.json`

Semantic source: `full_onnx_self_reference`

Decode mode: `completed_v2:decoded_nms:detection_completion_execution_same_hotloop_completed_artifact`

Decode warning: `no_contract_compatible_decode`

Boundary warning: ``

Semantic: `True`  match_ratio=0.889 matched=8/9 pred=9

Class-agnostic IoU: match_ratio=0.889 matched=8/9

Artifacts:

- Native box overlay: `detection_boxes_overlay.png`
- Reference overlay: `detection_reference_overlay.png`

## Decode sweep
| conf | mode | count | top classes | top scores |
|---:|---|---:|---|---|
| 0.05 | `no_contract_compatible_decode` | 0 | [] | [] |
| 0.1 | `no_contract_compatible_decode` | 0 | [] | [] |
| 0.2 | `no_contract_compatible_decode` | 0 | [] | [] |
| 0.25 | `no_contract_compatible_decode` | 0 | [] | [] |
| 0.4 | `no_contract_compatible_decode` | 0 | [] | [] |
| 0.6 | `no_contract_compatible_decode` | 0 | [] | [] |

## Tensor debug
| output | shape | dtype | min | max | mean | scoremap |
|---|---|---|---:|---:|---:|---|
| `output` | `[1, 3, 80, 80, 85]` | `float32` | -31.796875 | 9.078125 | -7.400270938873291 | `detection_scoremap_00_output.png` |
| `clone_1` | `[1, 3, 40, 40, 85]` | `float32` | -29.015625 | 9.609375 | -7.7173075675964355 | `detection_scoremap_01_clone_1.png` |
| `clone_2` | `[1, 3, 20, 20, 85]` | `float32` | -21.0 | 8.796875 | -8.407490730285645 | `detection_scoremap_02_clone_2.png` |
