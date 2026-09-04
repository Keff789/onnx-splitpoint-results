# Claim exclusion summary

Performance claim-eligible: 0; excluded rows: 208.
Energy claim-eligible: 0; excluded rows: 0.
Detailed and grouped counts represent one reason assignment per excluded claim-kind/source row. A source row with multiple explicit reasons therefore has multiple detail rows.

## Performance exclusions by primary reason

- `contract_fail_or_unavailable`: 185
- `screening_only`: 21
- `terminal_process_failure`: 2

## Energy exclusions by primary reason

- none

## Grouped exclusions: model / backend / setup / reason

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

## Per-dimension counts

| Claim kind | Dimension | Value | Count |
|---|---|---|---|
| performance | model | resnet50 | 84 |
| performance | model | yolo26s | 40 |
| performance | model | yolov7_paper | 84 |
| performance | backend | deepx_m1 | 3 |
| performance | backend | deepx_m1_to_tensorrt | 49 |
| performance | backend | hailo10 | 3 |
| performance | backend | hailo10_to_tensorrt | 49 |
| performance | backend | hailo8 | 3 |
| performance | backend | hailo8_to_tensorrt | 49 |
| performance | backend | tensorrt | 52 |
| performance | setup | orin_nx_deepx_m1_01 | 104 |
| performance | setup | orin_nx_hailo10_01 | 52 |
| performance | setup | orin_nx_hailo8_01 | 52 |
| performance | reason | contract_fail_or_unavailable | 185 |
| performance | reason | screening_only | 21 |
| performance | reason | terminal_process_failure | 2 |

## Stable exclusion detail rows

| Claim kind | Model | Backend | Setup | Reason | Task | Case | Variant | Row status | Eligibility |
|---|---|---|---|---|---|---|---|---|---|
| performance | resnet50 | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | full | full | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b001 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b003 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b008 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b009 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b020 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b022 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b027 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b042 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b052 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b054 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b056 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b068 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b074 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b078 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b091 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b095 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b107 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b112 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b118 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | classification | b119 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | full | full | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b001 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b003 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b008 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b009 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b020 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b022 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b027 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b042 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b052 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b054 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b056 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b068 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b074 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b078 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b091 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b095 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b107 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b112 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b118 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | classification | b119 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | full | full | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b001 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b003 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b008 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b009 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b020 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b022 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b027 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b042 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b052 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b054 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b056 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b068 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b074 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b078 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b091 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b095 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b107 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b112 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b118 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | classification | b119 | split | available | contract_fail_or_unavailable |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b001 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b003 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b008 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b009 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b020 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b022 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b027 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b042 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b052 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b054 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b056 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b068 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b074 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b078 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b091 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b095 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b107 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b112 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b118 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | b119 | split | available | screening_only |
| performance | resnet50 | tensorrt | orin_nx_deepx_m1_01 | screening_only | classification | full | full | available | screening_only |
| performance | yolo26s | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b005 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b038 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b042 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b118 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b148 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b181 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b221 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b005 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b038 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b042 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b118 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b148 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b181 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b221 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b005 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b038 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b042 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b118 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b148 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b181 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b221 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b005 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b038 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b042 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b118 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b148 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b181 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b221 | split | available | contract_fail_or_unavailable |
| performance | yolo26s | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1 | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b013 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b044 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b049 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b065 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b088 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b092 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b114 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b134 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b155 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b165 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b186 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b189 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b222 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b228 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b262 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b270 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b306 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | deepx_m1_to_tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b307 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10 | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b013 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b044 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b049 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b065 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b088 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b092 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b114 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b134 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b155 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b165 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b186 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b189 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b222 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b228 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b262 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b270 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b306 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo10_to_tensorrt | orin_nx_hailo10_01 | contract_fail_or_unavailable | detection | b307 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8 | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | full | full | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b044 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b049 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b065 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b088 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b092 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b114 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b134 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b155 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b165 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b186 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b189 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b222 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b228 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b262 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b270 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | contract_fail_or_unavailable | detection | b307 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | terminal_process_failure | detection | b013 | split | terminal_process_failure | contract_fail_or_unavailable |
| performance | yolov7_paper | hailo8_to_tensorrt | orin_nx_hailo8_01 | terminal_process_failure | detection | b306 | split | terminal_process_failure | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b001 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b002 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b013 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b044 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b049 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b065 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b088 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b092 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b114 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b134 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b155 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b165 | split | available | contract_fail_or_unavailable |
| performance | yolov7_paper | tensorrt | orin_nx_deepx_m1_01 | contract_fail_or_unavailable | detection | b186 | split | available | contract_fail_or_unavailable |

_Only the first 200 of 208 rows are shown._

