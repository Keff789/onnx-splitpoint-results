# Ranking method cohort sensitivity

Identical predictor methods are recomputed on technical, quality-pass, and pass-or-inconclusive cohorts. Subset correlations are diagnostic; global Hit@1 and Regret@1 remain unavailable unless the complete declared technical universe is paired.

| Model | Direction | Method | Cohort | n | Coverage | Spearman | Kendall | Global Hit@1 | Global Regret@1 | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | tensorrt_to_tensorrt | cut_bytes_only | technical | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cut_bytes_only | quality_pass | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cut_bytes_only | quality_pass_or_inconclusive | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | weighted_score | technical | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | weighted_score | quality_pass | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | weighted_score | quality_pass_or_inconclusive | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cycle_time_no_handover | technical | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cycle_time_no_handover | quality_pass | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cycle_time_no_handover | quality_pass_or_inconclusive | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cycle_time_with_handover | technical | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cycle_time_with_handover | quality_pass | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |
| resnet50 | tensorrt_to_tensorrt | cycle_time_with_handover | quality_pass_or_inconclusive | 1 | 0.00833333 |  |  |  |  | insufficient_candidates |

