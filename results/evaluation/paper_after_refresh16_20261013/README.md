# Paper analysis after Refresh16 — 14 October 2026

This is the current offline paper analysis of the canonical `refresh16_20261013` generation. The broad selection contains 450 deployments with observed FPS, host-inclusive energy and existing numeric dataset quality, including all 42 host-specific Full configurations. It retains accuracy losses, original claim/provenance flags and actual differences in timed work.

Start with [findings](results/FINDINGS.md), [Table 2](results/tables/table2_full.md), [Table 3](results/tables/table3_top2_native.md), [methods](results/METHODS.md) and the [claim-to-evidence table](results/CLAIM_EVIDENCE.md). The [complete dataset](results/PAPER_DATASET.csv), [metric sources](results/METRIC_SOURCES.csv), [measurement generations](results/MEASUREMENT_GENERATIONS.csv), [figure captions](results/CAPTIONS.md) and [machine-readable summary](results/summary.json) share one selection.

## Offline reproduction

Use Python 3.10 with the package versions in [requirements.txt](requirements.txt). From this directory, choose an output directory that does not yet exist:

```bash
python -I -B scripts/reproduce.py --output /tmp/paper-refresh16-reproduction --verify
```

The command reads the compact checked-in inputs, verifies their existing manifest, regenerates every numerical table, report, SVG/PDF/PNG figure and manuscript asset archive, then compares all output bytes with `results/`. It uses no LLM, API, sensors, hardware SDK, models or dataset inference. Figure metadata and ZIP timestamps are fixed. Byte equality is tested in the pinned environment; different rendering packages can change figure bytes and will be reported as differences.

The configuration is in [config.json](config.json). Broad observation selection and calibrated raw J/image are the required primary analysis. Optional original strict flags, reference-close quality, administrative-receipt and existing comparison-energy sensitivities are separate outputs. `--numeric-only` is a development option and does not produce the complete deliverable. The [independent checker and targeted tests](validation/README.md) recalculate the core quantities separately.

The reader, serialization/statistical conventions, existing reproduction verifier, audit guard and legacy quantile implementation extend the previous Twix analysis. The Current-aware `scripts/extract_canonical.py` can restore these compact inputs from the private canonical archive. That restoration is not needed for public reproduction. Raw sensor traces, models, datasets and private manuscripts are excluded from this package.

## Manuscript assets

[MLSys and Dissertation packages](results/assets/README.md) contain LaTeX Tables 2/3, supplemental tables, PDF/SVG figures, PNG previews, captions, methods and claim evidence. Each archive has a standalone `preview.tex`. No existing manuscript is overwritten or submitted.

## Interpretive limits

Included means an observed deployment value, not proof of identical executed work. Native detector splits record an oracle outside timing, whereas Generic detector splits record decoded NMS. Refreshed YOLO26s Full implementations execute their recorded host-tail/integrated normalization paths. Quality remains visible and is not a hidden filter. In 53 Native DeepX classifier rows, the cached Current loss differs from the selected quality report's numerical metric; both are retained and named separately. All original quality selections and flags remain unchanged, and no new quality evaluation was performed.

The earlier [Revision-3 analysis](../rev3_consolidated_20261013/README.md) and [acquisition snapshot](../native_fairness_rev3_20261007/README.md) remain historical evidence. Prior administrative receipt-version and historical Full-producer source limits persist. The exact old clock profiles for three refreshed classifier cases remain unknown. None of these limitations authorizes new acquisition.
