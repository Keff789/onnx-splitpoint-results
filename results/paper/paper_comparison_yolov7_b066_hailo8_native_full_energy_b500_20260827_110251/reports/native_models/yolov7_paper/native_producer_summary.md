# Native producer summary — yolov7_paper

Evidence status: **complete**


| backend | case | precision | E2E scope | completed endpoint | host postprocess | status | ok | FPS | note |
|---|---|---|---|---|---|---|---:|---:|---|
| hailo8_to_trt | b066 | uint8_dequant_fp16 | full_task_pipeline | decoded_nms:detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | :True | ok | True | 15.872 | native hailo8_python_vstreams_fifo FIFO E2E measured |
| native_full_hailo8 | full | uint8_dequant_fp16 | full_task_pipeline | decoded_nms:detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | serialized_host_tail_inside_measured_interval:True | ok | True | 16.153 | native full baseline measured |
| native_full_tensorrt | full | uint8_dequant_fp16 | full_task_pipeline | decoded_nms:detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | :True | ok | True | 18.848 | native full baseline measured |
