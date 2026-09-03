# Task Quality Reference Comparison

| model | task | backend | variant | case_id | quality_decision | comparison_status | delta_vs_full_onnx_Top1 | delta_vs_full_onnx_Top5 | decision_Top1 | decision_Top5 | bootstrap_skipped_reason_Top1 | bootstrap_skipped_reason_Top5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | classification | hailo8 | vendor_full | b119 | inconclusive | ok | -0.002 | -0.002 | inconclusive | pass |  |  |
| resnet50 | classification | tensorrt | vendor_full | full | pass | ok | 0.0 | 0.0 | pass | pass | candidate_reference_identical | candidate_reference_identical |
| resnet50 | classification | tensorrt | split | b119 | pass | ok | 0.0 | 0.0 | pass | pass | candidate_reference_identical | candidate_reference_identical |
| resnet50 | classification | tensorrt | vendor_full | b119 | pass | ok | 0.0 | 0.0 | pass | pass | candidate_reference_identical | candidate_reference_identical |
