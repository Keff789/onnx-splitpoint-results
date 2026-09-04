# Generic-to-Native ranking transfer

Status: `quality_screening_only`  
Candidate pairs: **24**; technical: **24**, quality: **9**, claim: **0**
Planned Native intersection: **24/24**; Generic rows outside this denominator: **172**
Legacy normalized endpoint defaults reconciled by exact central request projection: **24**
Qualified technical micro-concordance: **17/18** (0.9444444444444444); Hit@1: **6/6**; Regret@1 median: **0.0**

| Model | Direction | Contract | technical n | technical pairwise | technical Hit@1 | technical Regret@1 | quality n | quality pairwise | quality Hit@1 | quality Regret@1 | claim n | claim pairwise | claim Hit@1 | claim Regret@1 | Status |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| resnet50 | deepx_m1_to_tensorrt | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | 3 | 1.0 | True | 0.0 | 0 |  |  |  | 0 |  |  |  | technical_diagnostic_only |
| resnet50 | hailo10h_to_tensorrt | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | 3 | 1.0 | True | 0.0 | 0 |  |  |  | 0 |  |  |  | technical_diagnostic_only |
| resnet50 | hailo8_to_tensorrt | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | 3 | 0.6666666666666666 | True | 0.0 | 0 |  |  |  | 0 |  |  |  | technical_diagnostic_only |
| yolo26s | deepx_m1_to_tensorrt | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | 3 | 1.0 | True | 0.0 | 3 | 1.0 | True | 0.0 | 0 |  |  |  | quality_screening_only |
| yolo26s | hailo10h_to_tensorrt | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | 3 | 1.0 | True | 0.0 | 0 |  |  |  | 0 |  |  |  | technical_diagnostic_only |
| yolo26s | hailo8_to_tensorrt | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | 3 | 1.0 | True | 0.0 | 0 |  |  |  | 0 |  |  |  | technical_diagnostic_only |
| yolov7_paper | deepx_m1_to_tensorrt | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | 2 |  |  |  | 2 |  |  |  | 0 |  |  |  | insufficient_candidates |
| yolov7_paper | hailo10h_to_tensorrt | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | 2 |  |  |  | 2 |  |  |  | 0 |  |  |  | insufficient_candidates |
| yolov7_paper | hailo8_to_tensorrt | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | 2 |  |  |  | 2 |  |  |  | 0 |  |  |  | insufficient_candidates |

Technical, quality and claim cohorts are evaluated separately. A qualified group requires at least three exact pairs in the respective cohort; technical membership does not imply a quality pass. Absolute Native throughput and energy remain Native-runner evidence; this report tests whether the Generic ordering is a usable shortlist surrogate.
