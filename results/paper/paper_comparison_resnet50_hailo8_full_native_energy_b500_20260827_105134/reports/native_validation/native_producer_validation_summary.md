# Native producer semantic validation / visual summary

`ok` / `claim` means the task/contract validation artifact passed. Structure, numerical similarity and dataset task quality are independent evidence axes. `contract` is the structural axis only; numerical mismatch never rewrites it. Ranking eligibility requires every axis that the versioned policy declares mandatory.

| backend | model | case | precision | task | ok | claim | eligible | structure | numerical | task quality | accuracy_gate | artifact | tensor | semantic | level | status | ap50/topk | artifact file |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| native_full_hailo8 | resnet50 | full | uint8_dequant_fp16 | classification | True | True | False | True | True | inconclusive | False | True | True | True | classification_full_self_reference | claim_ok | top1=True top5ov=4 | classification_validation.md |
| native_full_tensorrt | resnet50 | full | uint8_dequant_fp16 | classification | True | True | False | True | True | True | True | True | True | True | classification_full_self_reference | claim_ok | top1=True top5ov=5 | classification_validation.md |
