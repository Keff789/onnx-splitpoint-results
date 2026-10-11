# Controlled 2 kS/s / 5 MS/s evidence — 1 October 2026

Compact public evidence for the historical fixed-window audit and the complementary GEMM-FP16 control experiment. Raw NPY/Parquet channels, credentials and complete private review archives are intentionally excluded; their names and SHA-256 hashes are registered in `sources.json`.

## Evidence sequence

1. [`fixed-window/`](fixed-window/README.md): 225 historical traces, five workloads, three rates and 15 runs per rate were re-evaluated with the same fixed 20–80 s interval. The remaining multi-percent differences persist inside the load region and are already visible in the pre-load level.
2. Original six-run controlled session: 250 completed queries, fixed 120 s process pause, order `2k, 5M, 5M, 2k, 2k, 5M`.
3. Complementary six-run session: same engine, command, pause and Jetson boot, order `5M, 2k, 2k, 5M, 5M, 2k`.
4. [`complementary/`](complementary/REPORT.md): both sessions are balanced by sequence position. The raw session median changes sign with the order, while the balanced Pico load estimate is -0.061 %, Jetson VDD_IN +0.009 %, and TensorRT runtime -0.030 % at 5 MS/s versus 2 kS/s.

## Main conclusion

The historical multi-percent direct-sweep trends are not treated as a deterministic sampling-rate effect. They remain valid observations of the old protocol, but they contain session/order/acquisition-state contributions. The controlled experiment uses all twelve measured runs; no magnitude-based exclusions and no offset, gain, time or drift correction are applied.

The external Pico pre- and load-window levels drift together through both sessions. The load-minus-pre view reduces this common drift, but it is diagnostic evidence and not an automatic calibration correction. Pico and Jetson VDD_IN have different physical boundaries and are not hardware-time-synchronized.

## Files

- Existing `data/controlled-group-stats.csv`: first controlled six-run session.
- Existing `data/historical-endpoint-decomposition.csv`: historical endpoint decomposition.
- `fixed-window/data/`: fixed-window group, subwindow, pre-load and run-order evidence.
- `complementary/data/`: all twelve runs, position contrasts, sequence slopes, session summaries and the balanced model.

The public evidence is deliberately text-based and inspectable. Full compact review ZIPs and raw measurement channels remain in laboratory storage and are identified by hashes in `sources.json`.
