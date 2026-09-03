# Native producer combined summary

Evidence status: **complete**

Roots:
- `/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/native_producers/hailo8`
- `/home/kmika/Models/EvaluationRuns/paper_comparison_yolov7_b066_hailo8_native_full_energy_b500_20260827_110251/native_producers/hailo8/yolov7_paper/benchmark_set`

| backend | impl | model | case | precision | E2E scope | completed endpoint | host postprocess | structure | numerical | task quality | status | ok | FPS | handoff ms | note |
|---|---|---|---|---|---|---|---|---:|---:|---:|---|---:|---:|---:|---|
| hailo8_to_trt | hailo8_python_vstreams_fifo | yolov7_paper | b066 | uint8_dequant_fp16 | full_task_pipeline | decoded_nms:detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | :True | True | True | True | ok | True | 15.872 | 0.413 | native hailo8_python_vstreams_fifo FIFO E2E measured |
| native_full_hailo8 | hailo8_vstreams_full | yolov7_paper | full | uint8_dequant_fp16 | full_task_pipeline | decoded_nms:detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | serialized_host_tail_inside_measured_interval:True | True | True | False | ok | True | 16.153 |  | native full baseline measured |
| native_full_tensorrt | native_tensorrt_full_completed_task | yolov7_paper | full | uint8_dequant_fp16 | full_task_pipeline | decoded_nms:detection:decoded_nms:comparison:43612439aff99a683e0c32f17d9bc70074301ae7445e83c8307439856fbf8a08 | :True | True | True | True | ok | True | 18.848 |  | native full baseline measured |
