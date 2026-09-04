# Scientific Evaluation Report

Generated: `2026-08-24T06:26:35+02:00`
Profile: `resnet_yolo26s_yolov7_v27549_phase2_ranking_audit_b500`

## Decision summary

- Technical execution status: **ok**
- Quality-evaluation technical status: **ok**
- Quality-evaluation status: **evaluated**
- Aggregate quality decision: **pass**
- Scientific status: **not_claim_ready**
- Development-analysis status: **development_diagnostic_available**
- Claim readiness: **blocked** (0 claim-eligible row(s))
- Central quality results: **217 / 217** across **3** setup(s)
- Rows: **208**
- Performance observation rows: **206**
- Native energy attempts: **0** (**0** successful, **0** failed)
- Ranking eligible: **0**
- Performance eligible: **0**
- Energy eligible: **0**
- Development/screening performance observations: **206**
- Native setup-specific performance observations: **24** (matrix: **complete**)
- Native completed comparison endpoints: **15**
- Native host postprocessing: required **15**, available **15**, legacy-alias conflicts **0**
- Native runtime evidence: **unavailable**
- Native semantic evidence: **unavailable**
- Native claim evidence: **unavailable**
- Native energy evidence: **unavailable**
- Technical status: **unavailable**
- Claim decisions complete: **unavailable**
- Native energy attempts: **unavailable started, unavailable not started**
- Energy plan completion: **unavailable/unavailable**
- Energy matrix coverage: **unavailable/unavailable**
- Energy claim eligible: **unavailable**
- Final all-split energy complete: **unavailable**
- Scientific status: **unavailable**
- Scientific ready: **unavailable**
- Development/screening energy observations: **0**
- Campaign claim scope: **evaluated_matrix**
- Ranking-method comparison: **development_only**
- Best method under a common comparison coverage: **not available** (insufficient common coverage)
- Development diagnostic leader (not claim eligible): **Cut bytes only** (frozen_minimum_80pct_identical_actual_strata)
- Generic-to-Native ranking transfer: **insufficient_candidates** (0 paired candidates)

## Claim exclusion breakdown

- Performance excluded rows: **208**
- Energy excluded rows: **0**
- Exclusion reason assignments: **208**

### Grouped by model / backend / setup / reason

| Claim kind | Model | Backend | Setup | Reason | Count |
|---|---|---|---|---|---|
| performance | resnet50 | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 1 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 20 |
| performance | resnet50 | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | 1 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | 20 |
| performance | resnet50 | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | 20 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | 21 |
| performance | yolo26s | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 1 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 9 |
| performance | yolo26s | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | 1 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | 9 |
| performance | yolo26s | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | 9 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 10 |
| performance | yolov7_paper | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 20 |
| performance | yolov7_paper | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | 20 |
| performance | yolov7_paper | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | 1 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | 18 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | terminal_process_failure | 2 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | 21 |

### Stable detail rows

| Claim kind | Model | Backend | Setup | Reason | Case |
|---|---|---|---|---|---|
| performance | resnet50 | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | full |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b001 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b003 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b008 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b009 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b020 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b022 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b027 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b042 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b052 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b054 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b056 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b068 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b074 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b078 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b091 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b095 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b107 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b112 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b118 |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b119 |
| performance | resnet50 | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | full |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b001 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b003 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b008 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b009 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b020 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b022 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b027 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b042 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b052 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b054 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b056 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b068 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b074 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b078 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b091 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b095 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b107 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b112 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b118 |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b119 |
| performance | resnet50 | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | full |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b001 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b003 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b008 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b009 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b020 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b022 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b027 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b042 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b052 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b054 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b056 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b068 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b074 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b078 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b091 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b095 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b107 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b112 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b118 |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b119 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b001 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b003 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b008 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b009 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b020 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b022 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b027 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b042 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b052 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b054 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b056 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b068 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b074 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b078 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b091 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b095 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b107 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b112 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b118 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | b119 |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | full |
| performance | yolo26s | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | full |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b001 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b002 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b005 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b038 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b042 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b118 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b148 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b181 |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b221 |
| performance | yolo26s | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | full |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b001 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b002 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b005 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b038 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b042 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b118 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b148 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b181 |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b221 |
| performance | yolo26s | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | full |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b001 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b002 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b005 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b038 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b042 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b118 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b148 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b181 |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b221 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b001 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b002 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b005 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b038 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b042 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b118 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b148 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b181 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b221 |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | full |
| performance | yolov7_paper | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | full |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b001 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b002 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b013 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b044 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b049 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b065 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b088 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b092 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b114 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b134 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b155 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b165 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b186 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b189 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b222 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b228 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b262 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b270 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b306 |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b307 |
| performance | yolov7_paper | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | full |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b001 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b002 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b013 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b044 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b049 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b065 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b088 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b092 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b114 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b134 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b155 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b165 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b186 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b189 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b222 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b228 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b262 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b270 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b306 |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | b307 |
| performance | yolov7_paper | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | full |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b001 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b002 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b044 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b049 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b065 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b088 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b092 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b114 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b134 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b155 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b165 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b186 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b189 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b222 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b228 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b262 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b270 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | b307 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | terminal_process_failure | b013 |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | terminal_process_failure | b306 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b001 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b002 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b013 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b044 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b049 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b065 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b088 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b092 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b114 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b134 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b155 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b165 |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | b186 |

_Only the first 200 of 208 rows are shown._

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
| dataset_classification_calibration | pass | required_for_final | classification calibration dataset manifest found: /home/kmika/.onnx_splitpoint_tool/final_datasets/v27541_imagenet_n500_s20260710/manifests/imagenet_train_calibration_manifest.json |
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
| model_role_explicit_resnet50 | pass | required_for_final | Model resnet50 explicitly declares evaluation_role=development or confirmatory_holdout. |
| model_family_id_explicit_resnet50 | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for resnet50. |
| model_generalization_scope_explicit_resnet50 | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for resnet50. |
| model_validation_tier_explicit_resnet50 | pass | required_for_final | Model resnet50 explicitly declares validation_tier. |
| model_validation_tier_final_resnet50 | deferred | required_for_final | Model resnet50 uses the final validation tier in a final campaign. |
| model_identity_resnet50 | pass | required_for_final | Model resnet50 resolves to an exact local model artefact with a content hash. |
| candidate_universe_resnet50 | pass | required_for_final | Model resnet50 explicitly declares its candidate-universe mode. |
| model_role_explicit_yolo26s | pass | required_for_final | Model yolo26s explicitly declares evaluation_role=development or confirmatory_holdout. |
| model_family_id_explicit_yolo26s | not_applicable | informational | Model-family transfer is outside the evaluated_matrix claim for yolo26s. |
| model_generalization_scope_explicit_yolo26s | not_applicable | informational | A generalisation scope is not consumed by the evaluated_matrix claim for yolo26s. |
| model_validation_tier_explicit_yolo26s | pass | required_for_final | Model yolo26s explicitly declares validation_tier. |
| model_validation_tier_final_yolo26s | deferred | required_for_final | Model yolo26s uses the final validation tier in a final campaign. |
| model_identity_yolo26s | pass | required_for_final | Model yolo26s resolves to an exact local model artefact with a content hash. |
| candidate_universe_yolo26s | pass | required_for_final | Model yolo26s explicitly declares its candidate-universe mode. |
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
| effective_energy_configuration | deferred | required_for_final | One effective energy request is configured without conflicting generic/native enablement. |
| energy_window_method_ab | deferred | required_for_final | The command-marker window is frozen as the scientific primary. The Chapter-4 legacy window is a same-trace, non-blocking sensitivity shadow; it never auto-switches, cannot invalidate the primary claim and requires no PicoScope rerun. |
| full_system_power_scope | deferred | required_for_final | Final energy campaign uses raw full-system input energy as the primary metric. |
| energy_command_window | deferred | required_for_final | Final full-system energy is bound to the command window. |
| energy_repetitions | deferred | required_for_final | Full-system energy uses at least three independent repetitions. |
| energy_confidence_interval | deferred | required_for_final | Repeated energy windows use a pre-declared confidence level of at least 95%. |
| energy_run_order | deferred | required_for_final | Final energy target blocks use a recorded deterministic random order with an explicit integer seed. |
| idle_normalization_policy | pass | required_for_final | Idle normalization reports raw and normalized values and uses a scope-compatible paired method. |
| energy_calibration_manifest | deferred | required_for_final | Full-system input-channel calibration manifest missing:  |


## Task-quality gates

| Model | Backend | Setup | Case | Variant | Technical | Tier | Metric | Delta | CI low | Margin | Status | Gate reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | deepx_m1 | orin_nx_deepx_m1_01 | full | full | completed | screening | top1_accuracy | -0.01 | -0.02 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b001 | composed | completed | screening | top1_accuracy | -0.046 | -0.046 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b003 | composed | completed | screening | top1_accuracy | -0.048 | -0.048 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b008 | composed | completed | screening | top1_accuracy | -0.044 | -0.044 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b009 | composed | completed | screening | top1_accuracy | -0.052 | -0.052 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b020 | composed | completed | screening | top1_accuracy | -0.048 | -0.048 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b022 | composed | completed | screening | top1_accuracy | -0.048 | -0.048 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b027 | composed | completed | screening | top1_accuracy | -0.044 | -0.044 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b042 | composed | completed | screening | top1_accuracy | -0.042 | -0.042 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b052 | composed | completed | screening | top1_accuracy | -0.044 | -0.044 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b054 | composed | completed | screening | top1_accuracy | -0.046 | -0.046 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b056 | composed | completed | screening | top1_accuracy | -0.044 | -0.044 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b068 | composed | completed | screening | top1_accuracy | -0.044 | -0.044 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b074 | composed | completed | screening | top1_accuracy | -0.044 | -0.044 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b078 | composed | completed | screening | top1_accuracy | -0.044 | -0.044 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b091 | composed | completed | screening | top1_accuracy | -0.046 | -0.046 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b095 | composed | completed | screening | top1_accuracy | -0.048 | -0.048 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b107 | composed | completed | screening | top1_accuracy | -0.048 | -0.048 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b112 | composed | completed | screening | top1_accuracy | -0.052 | -0.052 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b118 | composed | completed | screening | top1_accuracy | -0.05 | -0.05 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | deepx_to_trt | orin_nx_deepx_m1_01 | b119 | composed | completed | screening | top1_accuracy | -0.052 | -0.052 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:fail;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo10 | orin_nx_hailo10_01 | b119 | full | completed | screening | top1_accuracy | 0 | -0.012 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b001 | composed | completed | screening | top1_accuracy | -0.012 | -0.012 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b003 | composed | completed | screening | top1_accuracy | -0.012 | -0.012 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b008 | composed | completed | screening | top1_accuracy | 0.002 | -0.01 | 0.01 | inconclusive | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b009 | composed | completed | screening | top1_accuracy | 0 | -0.012 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b020 | composed | completed | screening | top1_accuracy | -0.002 | -0.014 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b022 | composed | completed | screening | top1_accuracy | 0.008 | -0.004 | 0.01 | inconclusive | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b027 | composed | completed | screening | top1_accuracy | -0.008 | -0.02 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b042 | composed | completed | screening | top1_accuracy | -0.012 | -0.012 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b052 | composed | completed | screening | top1_accuracy | -0.012 | -0.012 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b054 | composed | completed | screening | top1_accuracy | -0.008 | -0.022 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b056 | composed | completed | screening | top1_accuracy | -0.006 | -0.016 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b068 | composed | completed | screening | top1_accuracy | -0.008 | -0.022 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b074 | composed | completed | screening | top1_accuracy | 0 | -0.0141 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b078 | composed | completed | screening | top1_accuracy | -0.006 | -0.02 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b091 | composed | completed | screening | top1_accuracy | -0.008 | -0.022 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b095 | composed | completed | screening | top1_accuracy | -0.002 | -0.016 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b107 | composed | completed | screening | top1_accuracy | 0.002 | -0.01 | 0.01 | pass | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b112 | composed | completed | screening | top1_accuracy | 0.002 | -0.012 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b118 | composed | completed | screening | top1_accuracy | 0 | -0.014 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo10h_to_trt | orin_nx_hailo10_01 | b119 | composed | completed | screening | top1_accuracy | 0.004 | -0.01 | 0.01 | pass | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8 | orin_nx_hailo8_01 | b119 | full | completed | screening | top1_accuracy | -0.002 | -0.014 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b001 | composed | completed | screening | top1_accuracy | -0.012 | -0.012 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b003 | composed | completed | screening | top1_accuracy | -0.01 | -0.024 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b008 | composed | completed | screening | top1_accuracy | 0 | -0.012 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b009 | composed | completed | screening | top1_accuracy | 0 | -0.012 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b020 | composed | completed | screening | top1_accuracy | -0.002 | -0.014 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b022 | composed | completed | screening | top1_accuracy | 0.006 | -0.008 | 0.01 | inconclusive | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b027 | composed | completed | screening | top1_accuracy | -0.004 | -0.014 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b042 | composed | completed | screening | top1_accuracy | -0.006 | -0.0181 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b052 | composed | completed | screening | top1_accuracy | -0.014 | -0.014 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b054 | composed | completed | screening | top1_accuracy | -0.01 | -0.024 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b056 | composed | completed | screening | top1_accuracy | -0.004 | -0.016 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b068 | composed | completed | screening | top1_accuracy | -0.002 | -0.014 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b074 | composed | completed | screening | top1_accuracy | -0.01 | -0.022 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b078 | composed | completed | screening | top1_accuracy | -0.006 | -0.02 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b091 | composed | completed | screening | top1_accuracy | -0.012 | -0.012 | 0.01 | fail | primary:top1_accuracy:decision:fail;primary:top1_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:point_estimate_below_non_inferiority_margin |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b095 | composed | completed | screening | top1_accuracy | -0.006 | -0.02 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:inconclusive |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b107 | composed | completed | screening | top1_accuracy | 0.008 | -0.006 | 0.01 | pass | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b112 | composed | completed | screening | top1_accuracy | 0.006 | -0.006 | 0.01 | pass | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b118 | composed | completed | screening | top1_accuracy | 0.002 | -0.012 | 0.01 | inconclusive | primary:top1_accuracy:decision:inconclusive;guardrail:top5_accuracy:decision:pass |
| resnet50 | hailo8_to_trt | orin_nx_hailo8_01 | b119 | composed | completed | screening | top1_accuracy | 0.004 | -0.008 | 0.01 | pass | primary:top1_accuracy:decision:pass;guardrail:top5_accuracy:decision:pass |
| resnet50 | tensorrt | orin_nx_deepx_m1_01 | full | full | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | tensorrt | orin_nx_hailo10_01 | full | full | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | tensorrt | orin_nx_hailo8_01 | full | full | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b001 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b003 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b008 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b009 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b020 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b022 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b027 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b042 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b052 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b054 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b056 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b068 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b074 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |
| resnet50 | ort_tensorrt | orin_nx_deepx_m1_01 | b078 | composed | completed | screening | top1_accuracy | 0 | 0 | 0.01 | pass | primary:top1_accuracy:decision:pass;primary:top1_accuracy:bootstrap_skipped_reason:candidate_reference_identical;guardrail:top5_accuracy:decision:pass;guardrail:top5_accuracy:bootstrap_skipped_reason:candidate_reference_identical |

_Only the first 80 of 217 rows are shown._

## Development/screening performance observations

These rows are retained for debugging and method development but are explicitly not claim eligible.

| Model | Backend | Boundary | Latency ms | FPS | Quality | Eligibility | Reason |
|---|---|---|---|---|---|---|---|
| resnet50 | deepx_m1 | full | 3.16632 | 315.824 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b001 | 23.3131 | 58.4354 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b003 | 28.4174 | 49.1818 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b008 | 36.6928 | 35.8799 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b009 | 25.2341 | 55.2686 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b020 | 27.5968 | 48.0583 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b022 | 35.5735 | 34.8587 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b027 | 23.5023 | 57.7153 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b042 | 19.5885 | 67.8272 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b052 | 15.5983 | 77.3697 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b054 | 20.2826 | 64.3456 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b056 | 17.2257 | 83.6917 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b068 | 12.247 | 95.0822 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b074 | 12.9648 | 91.856 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b078 | 13.7489 | 86.3702 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b091 | 12.7118 | 83.9503 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b095 | 12.3041 | 88.8509 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b107 | 10.05 | 94.3047 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b112 | 10.1941 | 91.44 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b118 | 9.34119 | 97.2855 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | deepx_m1_to_tensorrt | b119 | 7.63016 | 118.624 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10 | full | 10.1498 | 98.5244 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b001 | 27.9563 | 39.6433 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b003 | 33.6678 | 38.6588 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b008 | 40.2333 | 34.9087 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b009 | 26.87 | 40.975 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b020 | 33.5922 | 38.4546 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b022 | 40.291 | 34.2326 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b027 | 24.343 | 53.7741 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b042 | 20.3917 | 59.3422 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b052 | 18.024 | 60.7282 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b054 | 21.2163 | 57.2161 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b056 | 16.307 | 75.1905 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b068 | 13.6795 | 80.2737 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b074 | 13.9449 | 78.2675 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b078 | 14.8874 | 75.4667 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b091 | 15.3032 | 73.0743 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b095 | 14.4908 | 74.1539 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b107 | 12.9557 | 83.5621 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b112 | 12.8765 | 82.3399 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b118 | 12.9694 | 80.069 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo10_to_tensorrt | b119 | 10.5894 | 98.3045 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8 | full | 8.19273 | 122.059 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b001 | 5.34649 | 208.366 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b003 | 9.98974 | 121.484 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b008 | 13.9494 | 85.8219 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b009 | 5.14379 | 211.899 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b020 | 10.0943 | 105.155 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b022 | 14.091 | 85.6473 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b027 | 7.14793 | 163.513 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b042 | 5.37701 | 189.06 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b052 | 3.47896 | 314.783 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b054 | 5.99203 | 183.884 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b056 | 4.38461 | 252.123 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b068 | 3.63126 | 296.32 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b074 | 3.7272 | 292.212 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b078 | 4.47459 | 231.049 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b091 | 4.42581 | 244.157 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b095 | 4.1872 | 260.429 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b107 | 4.54793 | 236.196 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b112 | 4.44841 | 226.759 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b118 | 6.92062 | 157.886 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | hailo8_to_tensorrt | b119 | 6.95224 | 156.682 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| resnet50 | tensorrt | b001 | 6.37193 | 140.696 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b003 | 6.53949 | 250.308 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b008 | 7.56464 | 245.787 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b009 | 5.09486 | 315.257 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b020 | 6.4208 | 280.143 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b022 | 7.57728 | 239.264 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b027 | 5.99728 | 305.32 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b042 | 4.65684 | 411.134 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b052 | 5.71909 | 226.052 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b054 | 4.82893 | 361.597 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b056 | 4.42023 | 414.023 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b068 | 4.57454 | 404.754 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b074 | 3.96113 | 443.354 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b078 | 4.16551 | 394.862 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b091 | 3.99189 | 394.691 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b095 | 4.64196 | 353.145 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b107 | 3.73569 | 363.389 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b112 | 4.13704 | 324.09 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b118 | 7.09538 | 162.488 | pass | screening_only | screening_only |
| resnet50 | tensorrt | b119 | 7.01871 | 160.936 | pass | screening_only | screening_only |
| resnet50 | tensorrt | full | 6.34241 | 157.669 | pass | screening_only | screening_only |
| yolo26s | deepx_m1 | full | 37.5419 | 26.6369 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b001 | 115.739 | 11.9891 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b002 | 79.3226 | 18.4711 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b005 | 54.8872 | 30.9574 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b038 | 51.6618 | 28.2657 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b042 | 58.1959 | 23.6444 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b118 | 60.2391 | 21.9831 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b148 | 63.2141 | 19.6602 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b181 | 86.9026 | 13.5761 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | deepx_m1_to_tensorrt | b221 | 58.8932 | 20.5974 | pass | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | hailo10 | full | 100.841 | 9.91663 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | hailo10_to_tensorrt | b001 | 203.991 | 7.56694 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | hailo10_to_tensorrt | b002 | 130.126 | 8.22431 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | hailo10_to_tensorrt | b005 | 93.4803 | 11.7113 | inconclusive | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | hailo10_to_tensorrt | b038 | 88.868 | 12.187 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |
| yolo26s | hailo10_to_tensorrt | b042 | 106.597 | 11.8728 | fail | contract_fail_or_unavailable | contract_fail_or_unavailable |

_Only the first 100 of 206 rows are shown._

## Native setup-specific performance matrix

Eligible Native comparison rows use the median and 95-percent confidence interval of independently initialized repetitions, never as a best-of value. Rows without verified independence remain visible and explicitly ineligible. FPS remains independent from any theoretical stage-cycle rate. These observations still require final-protocol admission before thesis claims.

| Model | Setup | Backend | Case | Mode | Claim | Input claim | Claim structure | Claim structurally clamped | Physical evidence conflict | Physical conflict fields | Mean IoU | Mean IoU threshold | Source E2E scope | E2E scope | E2E eligible | E2E reason | Endpoint stratum | Concurrency | Physical stage | Output format | Physical contract | Contract source | Physical contract complete | Physical contract hash | Accelerator stage | Accelerator contract | Accelerator contract hash | Comparison endpoint | Physical endpoint | Physical endpoint match | Comparison endpoint match | Comparison stratum explicit | Host decode/NMS required | Postprocess included | Postprocess location | Host tail frozen | Host postprocess required | Host tail required | Host postprocess available | Host tail available | Host postprocess evidence | Host evidence source | Host alias conflict | Decoder contract | NMS | Decoder ID | Postprocess completed frames | Postprocess completion verified | Frozen host contract hash | Completed stage | Completed contract | Completed contract hash | Completed endpoint | Completed comparison contract hash | Completed comparison endpoint | Completion mode | Completed endpoint attested | Completed attestation status | FPS median | Latency median [ms] | Latency CI95 low [ms] | Latency CI95 high [ms] | valid n | Aggregation | Theoretical cycle rate | Structure | Numerical | Task quality |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | orin_nx_deepx_m1_01 | deepx_to_trt | b001 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  | 0 | False |  |  |  |  |  |  |  |  |  |  | 91.7429 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 100.875 |  |  |  |
| resnet50 | orin_nx_deepx_m1_01 | deepx_to_trt | b052 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  | 0 | False |  |  |  |  |  |  |  |  |  |  | 141.818 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 156.155 |  |  |  |
| resnet50 | orin_nx_deepx_m1_01 | deepx_to_trt | b095 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  | 0 | False |  |  |  |  |  |  |  |  |  |  | 213.358 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 234.11 |  |  |  |
| resnet50 | orin_nx_hailo10_01 | hailo10h_to_trt | b001 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  | 0 | False |  |  |  |  |  |  |  |  |  |  | 67.4913 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 67.5038 |  |  |  |
| resnet50 | orin_nx_hailo10_01 | hailo10h_to_trt | b052 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  | 0 | False |  |  |  |  |  |  |  |  |  |  | 141.829 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 141.858 |  |  |  |
| resnet50 | orin_nx_hailo10_01 | hailo10h_to_trt | b095 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  | False |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  | 0 | False |  |  |  |  |  |  |  |  |  |  | 281.691 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 281.759 |  |  |  |
| resnet50 | orin_nx_hailo8_01 | hailo8_to_trt | b001 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  |  |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 417.857 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 418.702 |  |  |  |
| resnet50 | orin_nx_hailo8_01 | hailo8_to_trt | b052 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  |  |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 561.936 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 563.202 |  |  |  |
| resnet50 | orin_nx_hailo8_01 | hailo8_to_trt | b095 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | classification_logits | classification_logits | classification_logits | authoritative_suite_contract_plus_runtime_tensor:v4 | True | 3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 |  |  |  | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | classification:classification_logits:3af2122851f19c5bf2b16b9c3ef78a6ba11452db33ff8fb915b76e3461bbcb28 | True | True | True |  |  |  |  | False | False | False | False | not_required | explicit_host_postprocess_not_required | False |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 355.538 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 355.871 |  |  |  |
| yolo26s | orin_nx_deepx_m1_01 | deepx_to_trt | b002 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | detection:decoded_nms:0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 23.5002 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 25.0805 |  |  |  |
| yolo26s | orin_nx_deepx_m1_01 | deepx_to_trt | b005 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | detection:decoded_nms:0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 45.9864 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 49.5036 |  |  |  |
| yolo26s | orin_nx_deepx_m1_01 | deepx_to_trt | b038 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | detection:decoded_nms:0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 38.7367 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 41.3906 |  |  |  |
| yolo26s | orin_nx_hailo10_01 | hailo10h_to_trt | b002 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | detection:decoded_nms:0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 15.7817 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 15.7839 |  |  |  |
| yolo26s | orin_nx_hailo10_01 | hailo10h_to_trt | b005 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | detection:decoded_nms:0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 31.7073 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 31.7153 |  |  |  |
| yolo26s | orin_nx_hailo10_01 | hailo10h_to_trt | b038 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | detection:decoded_nms:0ffb6ed284f37e7cbd6f5f32dabd1e64be8b43a29a3d12b39f2d096e62bc992d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 34.6748 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 34.6828 |  |  |  |
| yolo26s | orin_nx_hailo8_01 | hailo8_to_trt | b002 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 5aa0b51b69fb3bf202801f15e06ad49375f49467a8e957150095c6e22bcc256d | detection:decoded_nms:5aa0b51b69fb3bf202801f15e06ad49375f49467a8e957150095c6e22bcc256d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 85.0729 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 85.2913 |  |  |  |
| yolo26s | orin_nx_hailo8_01 | hailo8_to_trt | b005 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 5aa0b51b69fb3bf202801f15e06ad49375f49467a8e957150095c6e22bcc256d | detection:decoded_nms:5aa0b51b69fb3bf202801f15e06ad49375f49467a8e957150095c6e22bcc256d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 116.837 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 117.185 |  |  |  |
| yolo26s | orin_nx_hailo8_01 | hailo8_to_trt | b038 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | decoded_nms | bn6_detections | decoded_nms | explicit_endpoint_declaration_plus_runtime_values:v3 | True | d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 |  |  |  | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:d0972f0eb8de8e451288e18e2d2cd3497cf48cd3a02b854522aca5f2ae417e73 | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | attested_bn6_filter_padding_inverse_letterbox_materialize_no_nms_v1 | 1000 | True |  | decoded_nms | decoded_nms | 5aa0b51b69fb3bf202801f15e06ad49375f49467a8e957150095c6e22bcc256d | detection:decoded_nms:5aa0b51b69fb3bf202801f15e06ad49375f49467a8e957150095c6e22bcc256d | 0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection:decoded_nms:comparison:0153c6c2c964096ca2469182c8e2c0fd276d3b57166b737de759dbc39ca75dad | detection_completion_execution_v1 | True | passed | 130.649 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 131.055 |  |  |  |
| yolov7_paper | orin_nx_deepx_m1_01 | deepx_to_trt | b002 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc |  |  |  | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True |  | decoded_nms | decoded_nms | 9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | detection:decoded_nms:9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection_completion_execution_v1 | True | passed | 7.63919 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 8.24479 |  |  |  |
| yolov7_paper | orin_nx_deepx_m1_01 | deepx_to_trt | b044 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc |  |  |  | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True |  | decoded_nms | decoded_nms | 9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | detection:decoded_nms:9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection_completion_execution_v1 | True | passed | 12.4368 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 12.4489 |  |  |  |
| yolov7_paper | orin_nx_hailo10_01 | hailo10h_to_trt | b002 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc |  |  |  | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True |  | decoded_nms | decoded_nms | 9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | detection:decoded_nms:9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection_completion_execution_v1 | True | passed | 4.06304 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 4.06613 |  |  |  |
| yolov7_paper | orin_nx_hailo10_01 | hailo10h_to_trt | b044 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc |  |  |  | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True |  | decoded_nms | decoded_nms | 9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | detection:decoded_nms:9fcb6b365748948cb2fd02716900f72ee603093c7fa3c4ba8d326c04d7286ff0 | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection_completion_execution_v1 | True | passed | 16.186 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 16.2088 |  |  |  |
| yolov7_paper | orin_nx_hailo8_01 | hailo8_to_trt | b002 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc |  |  |  | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True |  | decoded_nms | decoded_nms | 40375eaa77cb7bc2efab7bd6bb0847ca4ea1cc3382bb54f519693e66b61cc9f8 | detection:decoded_nms:40375eaa77cb7bc2efab7bd6bb0847ca4ea1cc3382bb54f519693e66b61cc9f8 | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection_completion_execution_v1 | True | passed | 13.3142 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 13.3242 |  |  |  |
| yolov7_paper | orin_nx_hailo8_01 | hailo8_to_trt | b044 | native_split |  |  |  |  | False | [] |  |  | unavailable | unavailable |  |  |  |  | raw_head | raw_detection_tensors | raw_head | explicit_producer_export_contract | True | 051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc |  |  |  | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:raw_head:051f0d9e489355d312ad656532acf3ed8a2719774d8ef9843278818f5bd15adc | True | True | True |  | True |  |  | True | True | True | True | passed | detection_completion_execution_v1 | False | True | True | yolov7_paper_standard_anchor_classaware_nms_v2 | 1000 | True |  | decoded_nms | decoded_nms | 40375eaa77cb7bc2efab7bd6bb0847ca4ea1cc3382bb54f519693e66b61cc9f8 | detection:decoded_nms:40375eaa77cb7bc2efab7bd6bb0847ca4ea1cc3382bb54f519693e66b61cc9f8 | 43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | detection_completion_execution_v1 | True | passed | 15.9744 |  |  |  | 3 | median_with_deterministic_percentile_bootstrap_ci95 | 15.9841 |  |  |  |

## Development/screening energy observations

This table includes every Native energy attempt. Failed attempts remain visible, carry no invented numeric result and are always ineligible.

_No rows available._

## Ranking-method comparison (macro)

| Method | Groups | Validated hold-outs | MAE ms | MAPE % | Spearman | Kendall | Diagnostic groups | Diagnostic Spearman | Diagnostic Kendall | Hit@5 | Elite R@5 | Regret@5 | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cut bytes only | 36 | 0 |  |  | 0.255736 | 0.222993 | 8 | 0.74936 | 0.6492 |  |  |  | development_only |
| Weighted score | 36 | 0 |  |  | 0.777193 | 0.590643 | 8 | 0.508793 | 0.383827 |  |  |  | development_only |
| Cycle time without handover | 36 | 0 | 1.11009 | 34.9896 | 0.810526 | 0.614035 | 8 | 0.353608 | 0.266683 |  |  |  | development_only |
| Cycle time with runner/direction handover | 36 | 0 | 1.57275 | 50.6992 | 0.845614 | 0.660819 | 8 | 0.535811 | 0.39932 |  |  |  | development_only |
| Actual hardware-aware ONNX-boundary selector | 36 | 0 |  |  | 0.588855 | 0.44575 | 8 | 0.331963 | 0.260098 |  |  |  | development_only |

## Ranking-method comparison (per model/direction/runner)

| Model | Role | Direction | Runner | Method | n | Universe | Declared | Coverage | Frozen | MAE ms | MAPE % | Spearman | Kendall | Diagnostic n | Diagnostic Spearman | Diagnostic Kendall | Hit@5 | Elite R@5 | Regret@5 | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | development | deepx_m1_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.981495 | 0.934159 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | generic | Weighted score | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.280702 | 0.169591 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | -0.0649123 | -0.0409357 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.398246 | 0.239766 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.95 | True |  |  |  |  | 19 | -0.153576 | -0.105572 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.968268 | 0.897998 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | generic | Weighted score | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.298246 | 0.22807 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | -0.0210526 | 0.0175439 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | -0.0754386 | -0.0292398 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.95 | True |  |  |  |  | 19 | -0.370338 | -0.234605 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.550272 | 0.439959 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | generic | Weighted score | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.563158 | 0.403509 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.473684 | 0.309942 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.417544 | 0.28655 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.95 | True |  |  |  |  | 19 | -0.272927 | -0.105572 |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| resnet50 | development | hailo8_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| resnet50 | development | tensorrt_to_tensorrt | generic | Cut bytes only | 19 | False | True | 0.95 | False |  |  | 0.255736 | 0.222993 | 19 | 0.255736 | 0.222993 |  |  |  | candidate_universe_not_auditable |
| resnet50 | development | tensorrt_to_tensorrt | generic | Weighted score | 19 | False | True | 0.95 | False |  |  | 0.777193 | 0.590643 | 19 | 0.777193 | 0.590643 |  |  |  | candidate_universe_not_auditable |
| resnet50 | development | tensorrt_to_tensorrt | generic | Cycle time without handover | 19 | False | True | 0.95 | False | 1.11009 | 34.9896 | 0.810526 | 0.614035 | 19 | 0.810526 | 0.614035 |  |  |  | candidate_universe_not_auditable |
| resnet50 | development | tensorrt_to_tensorrt | generic | Cycle time with runner/direction handover | 19 | False | True | 0.95 | False | 1.57275 | 50.6992 | 0.845614 | 0.660819 | 19 | 0.845614 | 0.660819 |  |  |  | candidate_universe_not_auditable |
| resnet50 | development | tensorrt_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 19 | False | True | 0.95 | False |  |  | 0.588855 | 0.44575 | 19 | 0.588855 | 0.44575 |  |  |  | candidate_universe_not_auditable |
| yolo26s | development | deepx_m1_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | generic | Weighted score | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | generic | Weighted score | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | generic | Weighted score | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.4 | True |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolo26s | development | hailo8_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | tensorrt_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.4 | False |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | tensorrt_to_tensorrt | generic | Weighted score | 0 | False | True | 0.4 | False |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | tensorrt_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.4 | False |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | tensorrt_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.4 | False |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolo26s | development | tensorrt_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.4 | False |  |  |  |  | 8 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.968819 | 0.88499 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | generic | Weighted score | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.36595 | 0.269796 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.171128 | 0.140763 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.664327 | 0.44575 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.625713 | 0.387098 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolov7_paper | development | deepx_m1_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | generic | Cut bytes only | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.911727 | 0.790591 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | generic | Weighted score | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.355419 | 0.281526 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | generic | Cycle time without handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.185169 | 0.152493 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | generic | Cycle time with runner/direction handover | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.348398 | 0.258066 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | generic | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.95 | True |  |  |  |  | 19 | 0.615182 | 0.45748 |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0.05 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0.05 | False |  |  |  |  | 1 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Cut bytes only | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Weighted score | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Cycle time without handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Cycle time with runner/direction handover | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | handover_model_unavailable |
| yolov7_paper | development | hailo10h_to_tensorrt | native_fifo | Actual hardware-aware ONNX-boundary selector | 0 | False | True | 0 | False |  |  |  |  | 0 |  |  |  |  |  | insufficient_valid_audit_candidates |

_Only the first 160 of 180 rows are shown._

## Generic-to-Native ranking transfer

The same semantically valid candidate boundaries are compared under Generic and Native execution. Absolute Native throughput and energy remain Native-runner evidence; this section tests whether Generic ordering is a useful shortlist surrogate.

_No rows available._

## Open items

- **informational — campaign_development_mode**: Campaign status is development_ready; 13 final-only requirements remain deferred.
- **required_for_final — quality_profile_not_frozen**: Set quality_gate.frozen_before_final_campaign=true before the final campaign and archive the profile hash.
- **required_for_final — screening_dataset_only**: The configured task-quality tier is screening; these rows are not final task-quality evidence.
- **informational — ranking_generalization_out_of_scope**: The scientific claim is limited to the evaluated workload/hardware matrix; unseen-model ranking generalisation is not claimed.
