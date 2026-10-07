# THESIS20 completed analysis, 4 October 2026

> **Current-view update, 7 October 2026:** [YOLOv7 native performance](../yolov7_native_completion_20261007/README.md)
> supersedes the nine matching split and six Full throughput aggregates for paper use.
> Their current energy values are unavailable. This dated directory and its
> reproductions retain the historical October-4 snapshot; do not mix its YOLOv7
> energy with the newer runtime. Other models are unchanged by this update.

[Start here](START_HERE.md) · [Paper findings](PAPER_FINDINGS.md) · [Methods](METHODS.md) · [Input schema](INPUT_SCHEMA.md) · [Reproduction proof](REPRODUCTION_STATUS.json)

This is the curated joint derivation of the corrected original campaign, the
separate 192-case Generic completion and the twelve-case YOLO addition. The four
views remain distinct. Original failures, accuracy losses and methodological
exclusions are retained; no new measurement was performed for this publication.

- 527 historical Generic observations, plus 37 terminal build failures and 24 policy exclusions.
- 560 quality results: 521 reference-close and 39 accuracy-loss decisions.
- 246 Native cases / 738 repetitions; 42 Full baselines counted once.
- 204 Generic completed-task cases / 612 repetitions / 612,000 measured completions.
- 246 energy cases / 738 valid repetitions; unsuccessful physical attempts remain separately visible.

There are 204 technically paired cases, 201 passing the existing Quality-transfer
gates and no scientifically released transfer claims. Local Split–Full semantic
projection supports 392 of 408 descriptive comparisons; the remaining sixteen
limits are case-specific. Acquisition completeness does not turn development
measurements into a controlled causal or hold-out study.

## Tool and source provenance

The cumulative tool release is [v2.92.0](https://github.com/Keff789/ONNX-Splitpoint-Tool/releases/tag/v2.92.0),
main commit `d164aad6d7c7ef68c1b371c49a1fdea0a3b27dd7`, with its verified annotated tag,
ZIP, TAR and checksum list. [Publication evidence](evidence/tool-release-publication.json)
records the exact remote references and asset digests. The current release does
not retrospectively replace the historical source snapshots used during each
measurement. Those originals remain in the private archive.

396 distinct focused software tests passed, followed by normal source package,
installed-source, CLI/GUI-version import and profile-resolution checks. No new
hardware acceptance, compiler run, inference or energy capture was performed.
Five additional raw-provenance negative checks protect the local semantic audit.

## Reproduce and archive boundary

```bash
python scripts/reproduce.py
```

This reads only the compact inputs and rebuilds the tables and figures. NumPy and
Matplotlib are the only scientific dependencies; it does not require a device,
private raw payload or a tool installation. The isolated local reproduction
matched all 32 CSV/LaTeX/PDF/SVG outputs byte-for-byte plus three generated indices.

The [raw archive status](ARCHIVE_STATUS.md) explicitly distinguishes locally
preserved evidence, running transfer and the one unresolved historical source
byte identity. This public projection is not a substitute for original tensors,
models, engines, datasets, sensor traces, calibration payloads or private profiles.
No new data licence or public raw-data hosting arrangement is asserted.

