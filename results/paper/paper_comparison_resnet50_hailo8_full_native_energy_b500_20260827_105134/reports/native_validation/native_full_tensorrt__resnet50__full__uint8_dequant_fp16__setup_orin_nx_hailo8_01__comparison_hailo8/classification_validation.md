# Native classification semantic validation

Manifest: `/home/kmika/Models/EvaluationRuns/paper_comparison_resnet50_hailo8_full_native_energy_b500_20260827_105134/native_producers/hailo8/resnet50/benchmark_set/native_full_outputs/model=resnet50/backend=native_full_tensorrt/setup=orin_nx_hailo8_01/comparison=hailo8/native_full_outputs_manifest.json`

Reference source: `full_onnx_self_reference`

Self-reference diagnosis: `native_classification_matches_full_self_reference`

Semantic: `True`  Top1 match: `True`  Top5 overlap: `5`

## Native TopK
| rank | class index | score |
|---:|---:|---:|
| 1 | 1 | 6.07812 |
| 2 | 794 | 1.31152 |
| 3 | 443 | 1.27734 |
| 4 | 411 | 1.2627 |
| 5 | 4 | 0.836426 |

## Full-ONNX Self-Reference TopK
| rank | class index | score |
|---:|---:|---:|
| 1 | 1 | 6.06688 |
| 2 | 794 | 1.3119 |
| 3 | 443 | 1.27741 |
| 4 | 411 | 1.26752 |
| 5 | 4 | 0.838185 |
