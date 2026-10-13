# Canonical selection and preserved historical scope

The single private entry point is `diss_results/CURRENT.json`. Relative paths beneath this archive select the current compact inputs, the dated immutable supplement, historical cohorts, methods, validation and limits. The source Fairness archive remains unchanged. Sprite is directly mounted network storage on Twix; it is not described as local disk.

## Scientific identities and generations

All 450 current completed-task identities map to existing historical Native/Generic identities. There are no B-only or F-only identities **within this narrowly matched completed-task universe**. Rev3 selects 444 three-process performance cohorts and retains six explicitly labelled historical singles. Of the matched FPS values, 448 differ and two are numerically equal; equal numbers do not establish equal cohort bytes. The selected counts are 1,338 performance observations including the six singles, 437 normal energy cohorts / 1,311 sensor repeats and 448 normal quality admissions. The 13 energy exclusions and two quality exclusions remain visible.

[`cohort_actions.json`](inputs/cohort_actions.json) lists every identity selection. [`cohort_axis_actions.json`](inputs/cohort_axis_actions.json) records performance, energy and quality decisions separately. Native energy matches 246 prior identities and selects 233 current admitted cohorts; the other 13 are not filled from old values. All 204 Generic energy cohorts are new on this historical energy axis. Historical quality generation is not inferred from logical identity alone.

| Preserved historical axis | Rows | Logical overlap with current model/setup/backend/case | Outside current logical scope |
|---|---:|---:|---:|
| coverage | 588 | 220 | 368 |
| energy_cases | 246 | 246 | 0 |
| energy_physical_attempts | 748 | 747 | 1 |
| generic_raw | 527 | 220 | 307 |
| generic_short_predecessors | 12 | 12 | 0 |
| native_unsupported | 228 | 0 | 228 |
| quality | 560 | 246 | 314 |

These are separate axes with overlapping observations, not additive cohort totals. A logical match does not assert identical input, completion, quality, measurement or generation contracts. 1691 broader historical rows retain an explicitly un-inferred generation relationship. The 560 historical dataset-quality rows, 527 raw-endpoint Generic rows, 37 failed builds, 24 policy exclusions, 12 short predecessors, 228 unsupported Native cases and 748 physical attempts (including a separate GUI test) are preserved. The 1,350 old performance repeats and 738 old Native energy repeats remain their own historical inputs. See the full [`historical_records.json`](inputs/historical_records.json) and [`historical_scope.json`](inputs/historical_scope.json).

## File actions and restoration

The file plan resolves 92,337 archive-path references to 63,207 distinct byte payloads. 185 existing identical B payloads were reused. 63,022 missing distinct payloads (19,392,124,588 bytes) were added, with SHA-256 source/target checks. Duplicate archive-path references share existing identical bytes. File counts are not scientific coverage. The private `COPY_RECEIPT.json`, action tables and resolver preserve exact locations and hashes; no blind directory overlay or deletion was used.

All 49 authoritative handoff entry points were verified. Fresh B-only extraction regenerated 16 compact input files byte-for-byte and created zero new payload copies or cohorts. The command is idempotent for the frozen canonical archive:

```bash
python -I -B scripts/guarded_replay.py scripts/extract_canonical.py \
  --base CANONICAL_DISS_RESULTS --output NEW_INPUT_DIRECTORY
```

This is the normal repeat-selection command after the one-time additive archive preparation. The frozen supplement receipt is the authority; replay does not rebuild or replace it. A new input directory is recommended to avoid unrelated files. The private archive also preserves the one-time copy-plan/apply scripts and their logs. The analysis dependencies are pinned in `requirements.txt`.

## Evidence boundaries

[Inherited SM2 handoff evidence](validation/INHERITED_SM2_HANDOFF.json) records the completed source transfer; it is not a second Twix full-inventory certification. [Canonical restoration](validation/CANONICAL_RESTORATION.json) describes the checks actually executed on Twix. [Reference limits](validation/REFERENCE_LIMITS.md) documents 17 unresolved direct administrative receipt versions, the historical missing Full-producer source hash and the broader unresolved lineage inventory. Current normal leaves remain independently bound and sensitivity analyses exclude the 17 affected Native/Generic identities. Complete raw-trace, dataset or runtime replay is not claimed; original datasets, models and SDK/runtime prerequisites remain private/external.
