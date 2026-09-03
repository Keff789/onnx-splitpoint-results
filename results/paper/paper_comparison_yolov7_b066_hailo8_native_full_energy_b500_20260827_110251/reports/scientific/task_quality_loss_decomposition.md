# Task Quality Loss Decomposition

| model | task | backend | case_id | status | split_extra_loss_AP50 | split_extra_loss_AP75 | split_extra_loss_COCO_AP_50_95 | total_split_loss_AP50 | total_split_loss_AP75 | total_split_loss_COCO_AP_50_95 | vendor_loss_AP50 | vendor_loss_AP75 | vendor_loss_COCO_AP_50_95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| yolov7_paper | detection | hailo8 | b066 | ok | 0.007605921716825725 | 0.029441994266344695 | 0.04307954025159744 | 0.007890534742117539 | 0.008200660696492834 | 0.005844129001592646 | 0.0002846130252918133 | -0.02124133356985186 | -0.03723541125000479 |
| yolov7_paper | detection | tensorrt | b066 | ok | 8.265081756175796e-05 | 4.314296316393351e-05 | 3.952024301678847e-05 | 0.012768770868677892 | 0.00999410644837534 | 0.009153877477447392 | 0.012686120051116134 | 0.009950963485211406 | 0.009114357234430603 |
