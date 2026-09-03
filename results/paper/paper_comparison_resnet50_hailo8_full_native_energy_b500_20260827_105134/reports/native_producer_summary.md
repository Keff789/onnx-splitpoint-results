# Native producer combined summary

Evidence status: **complete**

Roots:
- `/home/kmika/Models/EvaluationRuns/paper_comparison_resnet50_hailo8_full_native_energy_b500_20260827_105134/native_producers/hailo8`

| backend | impl | model | case | precision | E2E scope | completed endpoint | host postprocess | structure | numerical | task quality | status | ok | FPS | handoff ms | note |
|---|---|---|---|---|---|---|---|---:|---:|---:|---|---:|---:|---:|---|
| native_full_hailo8 | hailo8_vstreams_full | resnet50 | full | uint8_dequant_fp16 | full_task_pipeline | : | :False | True | True | inconclusive | ok | True | 121.986 |  | native full baseline measured |
| native_full_tensorrt | native_tensorrt_full | resnet50 | full | uint8_dequant_fp16 | full_task_pipeline | : | :False | True | True | True | ok | True | 589.630 |  | native full baseline measured |
