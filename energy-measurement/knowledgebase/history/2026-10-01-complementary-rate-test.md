# Knowledgebase addendum — 1 October 2026

## Complementary controlled GEMM-FP16 rate diagnostic

Two complete six-run sessions used the same engine, 250 fixed queries, 120-s
end-to-start pauses and complementary rate orders. Every sequence position contains
one 2-kS/s and one 5-MS/s run across the two sessions.

The raw per-session median difference changes sign with the order
(-0.508 % versus +0.441 %). The position-balanced estimate for Pico inner-load
power is -0.021363 W (-0.061 %), while Jetson VDD_IN shows +0.009 % and
TensorRT runtime -0.030 %.

The external Pico pre- and load-window levels rise together through both sessions;
the load-minus-pre estimate is -0.204 %. No correction is applied.

**Decision:** the historical multi-percent direct-sweep trends are not treated as a
deterministic sample-rate effect. They remain valid observations of the old protocol
but include session/order/acquisition-state contributions. The controlled diagnostic
does not replace the historical campaign, does not prove absolute calibration and
does not justify retroactive offset subtraction.

## Limits

- Two six-run sessions are diagnostic evidence, not a population-level uncertainty budget.
- The balanced estimate assumes a common sequence-position effect plus a session offset.
- Pico and VDD_IN use different physical measurement boundaries and are not hardware-time-synchronized.
- The unchanged INA225NVGPU/nvgpu scaling is not an independent electrical validation of the present Jetson wiring.
- No offset, gain, drift, time or magnitude correction was applied.
