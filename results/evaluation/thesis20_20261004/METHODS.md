# Methods and reproducibility boundaries

## Source views and reader path

The private source roles are the original base evaluation, its corrected F01–F06 derivation, the 192-case Generic completion supplement, and the complete YOLO addition. The final YOLO result-source index selects its current 12-case Native summary and two normal energy block roots, whose completed rows retain references to successful earlier attempts. The latest terminal evidence is complete, exit 0. Historical workflow `partial` fields are preserved as history; the audited matrix and scientific comparability are separate concepts.

`extract_inputs.py` invokes the existing `write_completion_reports` on each original execution plan and actual result files in a new derivation directory; both 192 and 12 cases validate. It then invokes the normal `write_augmentation_reports`, `rate_endpoint_fields`, and `collect_native_energy`. It selects only the bound 234 corrected Native cases plus 12 additions, not copied summaries or maximum-FPS alternatives. Forty-two Fulls occur once. The nine inactive reserve identities are not measurements or outstanding jobs. The 228 original `not_supported` Native entries remain terminal and do not expand the measurement cohort.

Small public files project explicit numeric and semantic fields from these existing readers. `input_manifest.json` hashes these files for portable reproduction. `rank_function_provenance.json` records the verbatim existing pure rank functions. This local input manifest is a small analysis-file index, not a replacement identity or scientific-admission system.

Original-data extraction, with roots supplied by the archive operator:

```bash
python scripts/extract_inputs.py --base "$BASE" --corrected "$CORRECTED" \
  --completion "$COMPLETION192" --yolo "$YOLO" \
  --output "$DERIVED_PUBLIC" --private-index "$DERIVED_PRIVATE/native-source-index.json"
python scripts/extract_auxiliary.py --base "$BASE" --yolo-run "$YOLO_RUN" \
  --output "$DERIVED_PUBLIC" --reporter-replay "$DERIVED_PRIVATE/reporter_replay"
python scripts/merge_semantics.py --corrected "$CORRECTED" \
  --semantic-source "$SEMANTIC_REPLAY_PUBLIC" --output "$DERIVED_PUBLIC"
python "$DERIVED_PUBLIC/scripts/reproduce.py" --root "$DERIVED_PUBLIC"
```

The first command requires the matching tool environment and forbids subprocess dispatch. The auxiliary command only reads original budget chains and normalized short-run rows. The semantic replay command is documented separately in `inputs/semantics/README.md`; it uses preserved tensors and postprocessors, not inference. These original-data checks require archived artifacts; ordinary compact-input reproduction does not.

## Arithmetic and timing boundaries

Each Native and Generic completed-task repetition completes 1,000 tasks. FPS is checked against count / measured makespan, then the three-repetition median is checked against the original aggregate. Sample SD uses the three repetition FPS values; CV is sample SD divided by their mean. Min/max are empirical ranges, not confidence limits. Rank functions internally use an inverse-throughput coordinate solely to preserve order; no single-task latency is derived.

Each energy repetition uses its own actual workcount, joules and primary active interval. Per-repetition J/task and watts are independently checked; the case J/task is the mean of the three per-repetition ratios. Energy-window throughput is the mean of per-repetition workcount/time ratios, rather than a separate Native performance value. The stored Native FPS is retained only as explicitly named context. Measurement request duration (60 s) and realized primary active window are distinguished. Full-system calibrated primary energy has no idle subtraction; optional host/idle-normalized estimates do not replace it in any supplied figure.

`inputs/arithmetic_checks.csv` retains every recomputation with original value, derived value and absolute error. The acceptance tolerance for FPS accounts only for stored decimal rounding (absolute 10⁻⁶, relative 10⁻⁸); energy ratios and watts use tighter 10⁻¹⁰ checks. No original measurement or quality decision is overwritten. N, B and seed are verified from all actual central result policies, not assigned from expected totals. No new bootstrap or inference is performed.

## Ranking, quality, and Pareto

The strata are exactly `(model, setup, direction, precision, comparison backend, completed output endpoint, boundary class)`. Existing average-rank tie handling, Spearman, Kendall tau-b and pairwise concordance functions are reused. Top-1 selects the highest Generic FPS, with the existing stable tie order, and measures Native cycle regret `(best Native FPS / selected Native FPS) - 1`. Correlations and Top-1 metrics require at least three eligible candidates. `technical`, `quality`, `claim`, and additional `reference_close` cohorts are separate. A quality-valid result may be `accuracy_loss`; `reference_close` requires both runners close plus the existing quality-transfer eligibility. No candidate replacement or margin change occurs.

The historical raw proxy is evaluated separately on the same selected base cases, but its logits/P2 endpoint is explicitly different. It is not a completed-task comparison. No correlation is pooled over models/setups. Descriptive cross-case distributions are labelled as inventories rather than causal estimates.

The split Pareto tables maximize energy-window throughput and minimize J/task only within the exact ranking stratum plus calibration and energy window; all cases share full-system scope. All-valid-quality and `reference_close` frontiers are separate. Original time/thread/thermal controls are not established as identical, so these are descriptive candidate tradeoffs. Full comparisons use the separately documented semantic pair projection and never enter a split frontier implicitly.

## Scope limits and preserved negatives

The historical 45 `quality_missing_or_unbound` labels resolve through the corrected F06 index to 21 build failures and 24 policy exclusions. They are not pending quality tasks. The three starter Quality-transfer exclusions are retained independently from their valid accuracy results and strict technical pair bindings. All 204 technical comparisons are available; only 201 pass the stricter original Quality-transfer gates, and none passes scientific claim transfer.

All twelve YOLO groups end at n=3; Top-3 is therefore trivial. The addition was selected after inspecting capability and is development evidence. Current H8/b066 has an actual prepared-input three-stage path, current engine, and current postprocessing. It cannot stand for a different historical engine or timer boundary. Original source checkpoints remain part of the private archive; a new software release is not retroactive provenance for old measurements.

Budget chains, not summed copied aggregates, define physical energy attempts. The old 2→5 retry authorization affected only the three H8 rest rows; cumulative chains and failed/unknown source endings remain recorded. The independent GUI diagnostic is separate from the 738 scientific repetitions. No new measurement is needed to reproduce these counts.

## Figure style and files

The existing project PSD paper figures provided the visual baseline: DejaVu Sans, white axes, tab10 palette, thin gray grid, readable units, and compact multi-panel layouts. No PSD datasets were used or modified. `figure_index.json` binds each PDF/SVG to its exact small CSV and caption. Fixed SVG IDs and omitted creation timestamps make same-environment rendering repeatable. Scientific dependencies for portable reproduction are NumPy and Matplotlib; the standard library handles all table input and arithmetic. LaTeX tables use standard `tabular` without external macro packages.
