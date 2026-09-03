# Task Quality Reference Comparison

| model | task | backend | variant | case_id | quality_decision | comparison_status | delta_vs_full_onnx_AP50 | delta_vs_full_onnx_AP75 | delta_vs_full_onnx_COCO_AP_50_95 | decision_AP50 | decision_AP75 | decision_COCO_AP_50_95 | bootstrap_skipped_reason_AP50 | bootstrap_skipped_reason_AP75 | bootstrap_skipped_reason_COCO_AP_50_95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| yolov7_paper | detection | hailo8 | vendor_full | b066 | fail | ok | 0.0002846130252918133 | -0.02124133356985186 | -0.03723541125000479 | pass | fail | fail | point_estimate_below_non_inferiority_margin | point_estimate_below_non_inferiority_margin | point_estimate_below_non_inferiority_margin |
| yolov7_paper | detection | hailo8 | split | b066 | pass | ok | 0.007890534742117539 | 0.008200660696492834 | 0.005844129001592646 | pass | pass | pass |  |  |  |
| yolov7_paper | detection | tensorrt | vendor_full | full | pass | ok | 0.012686120051116134 | 0.009950963485211406 | 0.009114357234430603 | pass | pass | pass |  |  |  |
| yolov7_paper | detection | tensorrt | split | b066 | pass | ok | 0.012768770868677892 | 0.00999410644837534 | 0.009153877477447392 | pass | pass | pass |  |  |  |
| yolov7_paper | detection | tensorrt | vendor_full | b066 | pass | ok | 0.012686120051116134 | 0.009950963485211406 | 0.009114357234430603 | pass | pass | pass |  |  |  |
