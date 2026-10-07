# Start here: final THESIS20 analysis

> **Current-view update, 7 October 2026:** [YOLOv7 native performance](../yolov7_native_completion_20261007/README.md)
> supersedes the nine matching split and six Full throughput aggregates for paper use.
> Their current energy values are unavailable. This dated directory and its
> reproductions retain the historical October-4 snapshot; do not mix its YOLOv7
> energy with the newer runtime. Other models are unchanged by this update.

This directory is the compact public analysis projection. It contains no model payloads, raw sensor traces, datasets, private machine paths or credentials. Original evidence remains in the separately documented private archive. Publication status and the released tool reference belong to the enclosing result-repository release notes.

Read `PAPER_FINDINGS.md` first, then `METHODS.md`. `tables/four_views_inventory.csv` separates:

- corrected original base measurements;
- the separate 192-case Generic completion supplement;
- the twelve YOLO additions, including their separate short predecessor inventory;
- the explicit augmented union, with Full baselines counted once.

The separate completion view introduces Generic timings and references existing Native observations; its zero new Native/Quality/Energy counts mean no new acquisitions of those kinds, not absent evidence. The union is a derived view and must not be added to the preceding rows.

For paper work:

| Question | Primary artifact |
|---|---|
| Coverage, support and negative terminal decisions | `tables/support_by_backend_and_origin.csv`, `inputs/coverage.csv` |
| Raw Generic versus completed endpoints | `inputs/generic_raw.csv`, `inputs/generic_short_predecessors.csv`, `tables/paired_completed_cases.csv` |
| Rank transfer within exact strata | `tables/rank_groups.csv`, `tables/yolo_base_vs_augmented.csv` |
| Throughput variation and Native/Generic ratio | `tables/paired_group_descriptives.csv`, `inputs/performance_repeats.csv` |
| Accuracy decisions and restricted subsets | `inputs/quality.csv`, `inputs/quality_transfer_exclusions.csv` |
| Energy per task, watts and measured workcounts | `inputs/energy_repeats.csv`, `inputs/energy_cases.csv` |
| Compatible descriptive Pareto membership | `tables/within_stratum_pareto.csv` |
| Original and added Split↔Full semantic evidence | `tables/energy_split_full_comparisons.csv`, `inputs/semantics/` |
| Invalid/interrupted attempts, separate diagnostic | `inputs/energy_physical_attempts.csv` |
| Exact figure inputs and captions | `figure_index.json` |

Reproduce all derived tables and PDF/SVG figures using a Python environment with NumPy and Matplotlib:

```bash
python scripts/reproduce.py
```

The command uses paths relative to this directory. It performs no network requests, inference, bootstrap or measurement. It replaces only derived files under `tables/`, `figures/`, `previews/` and the generated local indices. `input_manifest.json` identifies the small curated inputs. The included pure ranking code preserves the existing tie rules; it does not require the original tool checkout.

Original-data verification is separate. With access to the private archive and the corresponding installed tool, the documented `extract_inputs.py`, `extract_auxiliary.py`, `merge_semantics.py` and stored-output semantic replay reproduce the compact input projection using the existing normal readers. Supply source roots explicitly as described in `METHODS.md`. Never direct their output into an original run.

The five figures have vector PDF/SVG versions and PNG review previews. Their small exact plot tables accompany them; no figure depends on an external host path. PDF/SVG styling follows the existing project PSD paper figures (white background, DejaVu Sans, tab10 palette, thin gray grid); hardware aliases H8/H10/DeepX use blue/orange/green consistently. Semantic comparisons and the curated summaries are descriptive screening/development evidence, not final or held-out deployment claims.

