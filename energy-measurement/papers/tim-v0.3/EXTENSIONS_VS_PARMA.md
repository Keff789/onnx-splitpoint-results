# Technical-extension register — TIM v0.3

**Internal working document, not yet a final submission statement.**
Reference basis: PARMA author manuscript v0.15.1 at evidence commit
`85eb488587a51659239c45d966f930f7c7b72a6e` (9 October 2026).
Do not describe that author manuscript as an already published proceedings article.

## Editorial principle

The journal presents its measurement design, analysis and central Jetson findings
in full enough detail to stand alone. Re-explaining those results is necessary
context, not the technical novelty claim. Their provenance is acknowledged in
the introduction and bibliography. Hailo and the additional measurements build
on that foundation rather than replacing it.

| Component | Relation to PARMA | Present v0.3 coverage |
|---|---|---|
| Native six-workload Jetson energy reconstruction | Reused foundation, not new evidence | Complete method, all nine durations, fixed/persistent rate distinction |
| All-15 FP16 energy/spectral comparison | Reused foundation, not new evidence | Separate energy and fluctuation objectives with matched-length spectral estimator |
| Jetson deployed-meter comparison and duration/direct-rate study | Reused foundation, not new evidence | Self-contained seven-workload comparison and execution context |
| Paired native-scope spectral comparison | Prior evidence, expanded explanation | Six-workload CDF figure and correct denominator/response limits |
| Hailo card-input deployed-meter comparison | Additional platform evidence beyond the Jetson-only PARMA manuscript | Three workloads, 15 paired executions each at 300 s; domain/scaling limits retained |
| Hailo energy/power/span comparisons across duration | Additional journal analysis of existing outcomes | Ten requests, per-run pairing and joint interpretation; not synchronised dynamic telemetry |
| Hailo active/excess spectra | Additional platform evidence | 15 GEMM plus 15 YOLO recordings, per-record metrics and estimator-specific interpretation |
| Hailo duration and direct-rate repeatability | Additional platform evidence | Continuous/variable/LLM-labelled series, missing intervals retained as missing |
| Complementary FP16 acquisition control | Already covered by PARMA; reused context | Same fixed-work rate/order comparison, not claimed as new |
| Separate fixed-rate FP32 pause diagnostic | Additional protocol evidence | Six scored executions, timing/temperature interpretation; not isolated causal throttling |
| Additional discrete-GPU measurements | Planned, not a completed result | No fabricated GPU/NVML values; integrate the final supplied measurements |
| Hailo same-trace energy-rate transfer, aligned component energy, synchronised telemetry and matched bursts | Further claims require corresponding evidence | Current boundaries remain explicit; not certified by aggregate agreement |

## Final submission preparation

The final extension list must be checked against the version of PARMA that is
actually published, not simply against this development snapshot. New GPU results
and other completed additions should be mapped to their figures, tables and
source evidence then. Merely expanding the recap does not satisfy the technical
extension requirement. The present document does not certify acceptance or
submission readiness of either manuscript.
