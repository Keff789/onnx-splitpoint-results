# YOLOv7 Fast NumPy Decode Canary v1

- Status: **PASS_FAST_NUMPY_TARGET_MET**
- Python: `/home/nx/hailo_py/bin/python`
- NumPy: `1.26.4`
- Raw heads: **8.568 MB/frame**
- Target: **≤ 10.00 ms**

## Main A/B

| Mode | Median ms | P95 ms | Saved vs oracle | Speedup | Parity |
|---|---:|---:|---:|---:|---|
| `oracle_prebound_current_processor` | 38.3440 | 38.4602 | 0.0000 | 1.00× | exact |
| `fast_dense_precomputed_geometry` | 34.5385 | 34.6397 | 3.8056 | 1.11× | exact |
| `fast_sparse_exact_decode` | 1.5613 | 1.5840 | 36.7827 | 24.56× | exact |

## Sparse candidate counts

| Stride | Total | Objectness survivors | Final score survivors |
|---:|---:|---:|---:|
| 8 | 19200 | 18 | 18 |
| 16 | 4800 | 22 | 22 |
| 32 | 1200 | 16 | 16 |

## Sparse stage medians

| Stage | Median ms | P95 ms |
|---|---:|---:|
| `class_argmax_on_raw_logits` | 0.0282 | 0.0292 |
| `head_concatenation` | 0.0091 | 0.0095 |
| `nms_inverse_letterbox_materialization` | 0.6434 | 0.6675 |
| `objectness_exact_prune` | 0.0440 | 0.0465 |
| `objectness_sigmoid_all_candidates` | 0.3712 | 0.3898 |
| `selected_box_decode` | 0.2824 | 0.3016 |
| `total` | 1.5895 | 1.6197 |
| `winner_class_sigmoid_and_score_filter` | 0.1100 | 0.1134 |

## Decision

`build_small_multi_image_raw_head_parity_corpus_before_product_integration`

This is a read-only single-payload optimization canary. A passing speed result must still be followed by a small diverse raw-head parity corpus before any v2.79 integration.
