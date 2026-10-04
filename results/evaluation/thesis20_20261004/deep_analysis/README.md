# THESIS20 deep scientific analysis — review edition

Separate exploratory analysis of the closed campaign, prepared 04 October 2026. No inference, measurement, quality campaign, engine compilation or tool release is performed. Original published outputs remain in the parent THESIS20 release.

Start with `WISSENSCHAFTLICHE_ANALYSE.md` (German interpretation) and `PAPER_STORYLINE.md`. `DATEN_UND_KOHORTEN.md` defines exact populations. `CLAIM_EVIDENCE_MATRIX.csv` links every proposed finding to a table and row key. `CAPTIONS.md` gives English captions for six main and three supplement figures; vectors are in `figures/`, review PNGs in `previews/`, exact figure inputs in `tables/*_source.csv`.

## Offline reproduction

Use the existing scientific Python environment (validated with Python 3.12, NumPy 1.26.4, Matplotlib 3.5.2; pytest for tests). No dependency installation is required on the analysis controller.

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/reproduce.py
THESIS20_SOURCE_ROOT="$PWD/source" PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests
```

The first command only regenerates the new derived tables, figures, captions and result summaries. Frozen compact sources live in `source/`; the additional saved quality/graph/path projections are in `inputs/`. To keep this review directory untouched, use `--output-root /tmp/thesis20-deep-reproduction` (choose a new destination). The original product extraction is not repeated. The test temporary directory can likewise be selected via `--basetemp` outside a source-integrity checked tree.

`extract_quality_graph.py` is an optional private-source projection entry point with explicit `--base`, `--corrected`, `--yolo`, `--output-root`; it reads existing JSON/CSV reports and never loads an ONNX model. Portable review reproduction does not invoke it.

Scientific limitations: post-hoc selected candidates, three repetitions, shared Full baselines, uncontrolled runtime equivalence, 16 semantic limits and 21 missing historical attestor-source bindings. See `STATUS.md` for archival status; a software test PASS is not a hardware PASS. Existing claims/gates and quality decisions are unchanged.
