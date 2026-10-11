# Experiment configuration and binding status — TIM v0.2

This register distinguishes supplied configuration from missing execution-bound
identity. It does not turn model names into equivalent completed inference work.
The previous detailed Jetson configuration is preserved in
`provenance/parma_v0151_EXPERIMENT_CONFIGURATIONS.md`; its supporting thesis and
provenance excerpts are under `provenance/parma_v0151_metadata/`.

| Experiment | Supported information | Not inferred |
|---|---|---|
| Jetson direct study | Orin NX 16 GB on u.RECS; nominal 19 V; L4T 36.4.7 / JetPack 6.2.1, MAXN-SUPER and fixed maximum clocks as documented for that study | Same software/electrical setup for every separate later control |
| Jetson GEMM/YOLO | Direct-study precision labels and requested iterations; thesis GEMM architecture and YOLO11n description retained | Every engine's runtime input, batch or complete execution-bound build identity |
| Separate language-model cohorts | Direct Jetson Gemma3-12B and paired-scope Gemma3-4B are distinct | Same model or exact compute across them |
| Hailo direct studies | Hailo-10 complete M.2 card input, excluding host; GEMM/YOLO/variable-YOLO/LLM labels; time-controlled requests and same-run sensor values | All HEF/model IDs, batch/shape/precision, compiler/runtime binding or output-validity/completed-work counts |
| Hailo spectral cohort | 15 GEMM and 15 YOLO native records; matched 10-s prefix; same-record idle; stored estimator parameters | Identity with every direct-study executable or semantic matching to Jetson |
| Jetson paired scopes | 59 simultaneous pairs, six workloads, native 5-MS/s source, exact rate/duration/offset configuration | Fully calibrated absolute dynamic-power uncertainty |
| FP16 reference | All 15 recordings; nominal 104-s energy window; explicit 4-s/4-s spectral branch | The superseded 13-run selection as current primary evidence |
| Complementary FP16 rate control | 12 runs, 250 completed queries, engine, useSpinWait, 120-s process gaps, two complementary sequences | 250 queries equal a universal image count; interactions absent from the additive design |
| FP32 pause diagnostic | 6 scored runs plus conditioner; 100 completed queries; 20/120-s pauses; continuous 2-kS/s acquisition; timing and temperature logs | Causal throttling threshold, waiting-energy optimum or independently calibrated absolute energy |
| Discrete GPU | Some earlier GPU source rows are retained in the inherited inputs | A completed updated GPU result or NVML observations absent from that source |

Complete unresolved runtime/HEF/model/host information should be supplied as a
separate bound source record before making the corresponding stronger claim.
The current manuscript stays within observations supported without that claim.
