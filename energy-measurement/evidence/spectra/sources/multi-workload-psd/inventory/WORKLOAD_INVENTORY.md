# Multi-workload inventory

| Workload | Family | Precision | Status | 5-MS/s pairs | Scope summary | Zero-offset status | PSD | Common reference |
|---|---|---:|---:|---:|---:|---|---:|---:|
| GEMM-FP32 | GEMM | FP32 | ready | 10 | yes | disabled | yes | yes |
| GEMM-INT8 | GEMM | INT8 | ready | 10 | yes | no_material_offset_detected | yes | yes |
| YOLO-FP32 | YOLO | FP32 | ready | 10 | yes | stable_offset_detected_and_corrected | yes | yes |
| YOLO-INT8 | YOLO | INT8 | ready | 10 | yes | no_material_offset_detected | yes | yes |
| Gemma3-4B | Gemma3-4B | unspecified | ready | 10 | yes | no_material_offset_detected | yes | yes |
| ResNet-50 FP32 | ResNet-50 | FP32 | ready | 9 | yes | no_material_offset_detected | yes | yes |

Missing or incomplete workloads are documented and skipped; the measurement trees remain read-only.
