# Experimental configuration detail

This is the detailed configuration table moved out of the manuscript's main
experimental-design table. It preserves the supplied v0.12 specifications;
missing fields have not been inferred. The source excerpts are in
`metadata/THESIS_WORKLOAD_EXCERPTS.txt` and `metadata/WORKLOAD_PROVENANCE.json`.

| Experiment | Recorded configuration |
|---|---|
| Jetson system | Orin NX 16 GB on u.RECS; L4T 36.4.7 / JetPack 6.2.1; MAXN-SUPER, fixed maximum clocks; nominal 19-V supply. |
| Jetson GEMM direct-rate study | Eight 1×1 convolutions with ReLU, global average pooling and final convolution; input 512×2048×14×14; 2048 channels. TensorRT FP32/FP16/INT8 requests 100/200/400 engine iterations. FP32 permits TensorRT TF32. |
| Jetson YOLO direct-rate study | YOLO11n, TensorRT FP32/FP16/INT8; 15,000/26,000/33,000 requested iterations. Input resolution and batch are not fully specified by these records. |
| Jetson LLM direct study | Gemma3-12B via Ollama; seed 0, temperature 0, top-k 1, reset context; no fixed output-token cap. Prompt: “Please write a Sudoku solver in Python. Keep it short”. Rate-study execution runs to completion. |
| Jetson variable YOLO | FP32 YOLO11n; requested activity 0.1–1.5 s, pauses 0.1–1.0 s; seeds 42 and 420; script-duration argument 100 s. |
| Paired-scope cohort | GEMM-FP32/INT8, YOLO-FP32/INT8, Gemma3-4B and ResNet-50 FP32. Ten Tek/Pico pairs per workload except ResNet-50 with nine; IDs stated in METHOD_DETAILS. Gemma3-4B is not the direct-study Gemma3-12B. |
| Long-window FP16 | 15 physical GEMM-FP16 recordings, IDs 0–14; native stored power at 5 MS/s; 104-s nominal energy interval, separately chosen active/idle spectral segments. |
| Direct sample-rate grid | 27 rates from 50 S/s to 5 MS/s, 15 repetitions/rate; Jetson YOLO-FP32 has 26 rate groups. Exact rate lists are in the per-group input tables. |
| Duration requests | 5, 10, 20, 50, 100, 200, 300, 400, 500 and 600 s. Requested duration is not substituted for the actual integrated span. Jetson duration studies are time controlled. |
| Rate-order control | Two complementary sessions ABBAAB and BAABBA, A=2 kS/s, B=5 MS/s. Same FP16 engine, 250 completed queries, useSpinWait, 120-s process pauses. |

The variable-YOLO script duration quoted above belongs to the direct-rate
configuration; the duration study uses its separately declared requests. The
paper does not assume every workload uses the same input or execution schedule.

## Supporting TIM-only configuration

The following row is retained from the original source package but is outside
the PARMA manuscript's experimental scope. It does not establish matched
cross-platform workloads or an accelerator-efficiency ranking.

| Experiment | Recorded configuration |
|---|---|
| Hailo direct studies | Hailo-10 M.2 card input, excluding host; GEMM, YOLO, variable YOLO and LLM as labelled in the records; time-controlled execution. The supplied manifests do not establish every compiled-model/batch/precision parameter. |
