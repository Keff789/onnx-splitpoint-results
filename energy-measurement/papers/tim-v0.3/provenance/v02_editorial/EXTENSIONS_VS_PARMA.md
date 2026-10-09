# Technical relationship to PARMA v0.15.1

The companion is an **author manuscript**, not yet a published proceedings
article. This is a working extension map, not a submission eligibility ruling.

| Evidence or operation | PARMA v0.15.1 | TIM v0.2 use | Status |
|---|---|---|---|
| Native Jetson rate–duration and all-15 FP16 energy/spectral definitions | Main method and quantitative result | Concise, attributed reference; four duration rows and short FP16 interpretation | Reused baseline; not claimed as new |
| Compact Jetson 300-s deployed-meter comparison, including variable YOLO | Main practical result | Context for transfer to card input and scaled AC | Reused baseline; not claimed as new |
| Jetson duration and complementary FP16 rate control | Present | Compressed support for protocol validation | Reused baseline; fuller wording alone is not an extension |
| Hailo direct rates, duration and card-input/vendor/AC observations | Excluded from manuscript; retained in evidence | Central results for a second acquisition/deployment setting | Additional manuscript evidence |
| Hailo active versus excess spectral tails, 30 recordings | Excluded from manuscript | Central workload-specific temporal interpretation | Additional manuscript evidence |
| Hailo energy/power/span pairing at all ten requests | Not a PARMA main result | Explicit common per-run pairing and all-duration analysis; short-request divergence | Newly assembled analysis of existing stored outcomes; no new measurement |
| Separate fixed-rate FP32 pause diagnostic | Not a PARMA main result | Six scored executions, timing and pre-start state only | Additional bounded protocol evidence |
| Hailo same-trace energy thresholds, aligned host decomposition, matched bursts, dynamic telemetry, final GPU data | Not supplied as results | Not invented or converted into completed sections | Remaining decisions/data tasks |

The contribution claimed in the current manuscript is a connected measurement
validation argument across Jetson and Hailo with duration-wise interval checks.
It is not a demonstration that a Jetson numerical sampling threshold transfers
to Hailo, nor an accelerator-efficiency comparison under matched completed work.
Whether the final journal submission needs all previously proposed extension
components should be decided against the final scientific claim and available
evidence. Adding pages or rephrasing the PARMA baseline is not a replacement
for those components.
