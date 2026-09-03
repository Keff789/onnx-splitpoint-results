# Run Status Summary — paper_comparison_resnet50_hailo8_full_native_energy_b500_20260827_105134

Technical status: `failed`
Quality-evaluation technical status: `failed`
Aggregate quality decision: `not_evaluated`
Scientific status: `not_evaluated`
Legacy workflow status: `failed`
Workflow: `v2.78.2-immutable-management-reference-evidence-fixes`

## Native evidence axes
- Runtime: `complete`
- Semantics: `complete_pass`
- Claim: `ready`
- Energy: `complete`

## Stage counts
- failed: 1
- ok: 15
- partial: 1

## Blocking partial / failure reasons
- `resnet50` / `run_benchmarks` / `partial` — Remote benchmark suite dispatched per hardware target/run-profile.; preserved 4 measured row(s), but the requested hardware matrix is incomplete; duplicate logical profile row(s): hailo8:full:fullx2.
- `workflow` / `evaluate_quality` / `failed` — Central management quality: requests=4, completed=4, matched=2, summary_only_native_full=1, unmatched=1, failed=0; technical_status=failed, quality_decision=not_evaluated; workers=4. CPU reference rows remain semantic-only.

## Non-blocking warnings
- none recorded
