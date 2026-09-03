# Native producer semantic validation / visual summary

`ok` / `claim` means the task/contract validation artifact passed. Structure, numerical similarity and dataset task quality are independent evidence axes. `contract` is the structural axis only; numerical mismatch never rewrites it. Ranking eligibility requires every axis that the versioned policy declares mandatory.

| backend | model | case | precision | task | ok | claim | eligible | structure | numerical | task quality | accuracy_gate | artifact | tensor | semantic | level | status | ap50/topk | artifact file |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| hailo8_to_trt | yolov7_paper | b066 | uint8_dequant_fp16 | detection | True | True | False | True | True | True | True | True | True | True | detection_yolo_full_self_reference_proxy | claim_ok | ap50p=0.8888888888888888 mode=completed_v2:decoded_nms:detection_completion_execution_same_hotloop_completed_artifact | detection_visual_validation.md |
| native_full_hailo8 | yolov7_paper | full | uint8_dequant_fp16 | detection | True | True | False | True | True | False | False | True | True | True | detection_yolo_full_self_reference_proxy | claim_ok | ap50p=0.8888888888888888 mode=completed_v2:frozen_host_tail | detection_visual_validation.md |
| native_full_tensorrt | yolov7_paper | full | uint8_dequant_fp16 | detection | True | True | False | True | True | True | True | True | True | True | detection_yolo_full_self_reference_proxy | claim_ok | ap50p=1.0 mode=completed_v2:frozen_host_tail | detection_visual_validation.md |
