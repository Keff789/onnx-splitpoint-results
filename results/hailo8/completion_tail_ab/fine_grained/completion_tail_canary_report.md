# Detection Completion-Tail Canary

- Status: **PASS**
- Completion mode: `raw_head_frozen_decode_nms`
- Iterations: 200 after 20 warm-up calls
- Runtime median: **48.008 ms**
- Reference integrated tail: **47.663 ms**
- Parity: **exact** (max coordinate delta 0 px)

## Inclusive stage timings

Parent stages are inclusive and are not additive with their children.

| Stage | Median ms | P95 ms | Calls/iteration | Inclusive share |
|---|---:|---:|---:|---:|
| `frozen_processor_total` | 37.9642 | 38.0836 | 1.0 | 79.1% |
| `yolo_harness_total` | 35.9861 | 36.0818 | 1.0 | 74.9% |
| `multiscale_decode` | 34.9544 | 35.0563 | 1.0 | 72.8% |
| `raw_output_content_hashing` | 8.4911 | 8.5785 | 1.0 | 17.7% |
| `frozen_contract_verification` | 1.5878 | 1.6301 | 1.0 | 3.3% |
| `yolov7_head_mapping` | 1.0868 | 1.1207 | 1.0 | 2.3% |
| `canonical_json_hashing` | 0.7922 | 0.8239 | 10.0 | 1.7% |
| `class_aware_nms` | 0.4424 | 0.4488 | 6.0 | 0.9% |
| `multiscale_head_normalization` | 0.1869 | 0.2074 | 2.0 | 0.4% |
| `source_tensor_signature` | 0.1469 | 0.1508 | 2.0 | 0.3% |
| `canonical_detection_records` | 0.1373 | 0.1585 | 2.0 | 0.3% |
| `yolo_format_detection` | 0.0431 | 0.0455 | 1.0 | 0.1% |
| `completion_artifact_materialization` | 0.0246 | 0.0259 | 1.0 | 0.1% |
| `postprocess_result_conversion` | 0.0087 | 0.0096 | 1.0 | 0.0% |
| `output_shape_description` | 0.0076 | 0.0081 | 1.0 | 0.0% |

## Additive leaf approximation

- Leaf-stage median sum: 47.9389 ms
- Unattributed residual median: 0.0684 ms

The residual contains Python control flow, NumPy indexing/materialisation, coordinate projection and operations not exposed as separate functions.
