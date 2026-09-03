# Native producer summary — resnet50

Evidence status: **complete**


| backend | case | precision | E2E scope | completed endpoint | host postprocess | status | ok | FPS | note |
|---|---|---|---|---|---|---|---:|---:|---|
| native_full_hailo8 | full | uint8_dequant_fp16 | full_task_pipeline | : | :False | ok | True | 121.986 | native full baseline measured |
| native_full_tensorrt | full | uint8_dequant_fp16 | full_task_pipeline | : | :False | ok | True | 589.630 | native full baseline measured |
