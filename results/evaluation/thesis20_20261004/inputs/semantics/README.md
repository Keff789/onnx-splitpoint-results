# Local semantic and terminal projection, 4 October 2026

All calculations use existing saved arrays, original commands and the installed
normal postprocessors. No model session, hardware runner, collector, quality
bootstrap or new measurement is executed. Original result flags are unchanged.

`yolo_energy_semantic_projection_24.csv` is a new audit projection. The historical
energy reporter used decoder/NMS identity hashes and reported 0/24 semantic pairs.
This audit validates each original frozen contract and its implementation through
the normal product verifier, compares primitive operators, maps declared tensors
only by unique shape/dtype and order, then runs both processors on each saved
Split and Full output. It preserves the original contract hashes and filenames.
The existing descriptive consumer supplies the checked model, input, preprocessing,
FS scope, calibration, command-window and duration bindings.

Before postprocessing, the audit independently checks both original command-file
SHA-256 values against the saved energy rows, then runs the existing Native and
Full command-contract verifiers. Full verification receives the original bound
execution context, including its artifact-role roots. Each output manifest is
checked against its original validation/Native row SHA-256. Every loaded raw file
is checked for size and SHA-256 against that manifest or, where the old manifest
has no per-file SHA, the existing base-run artifact index. Missing or conflicting
original hash authority fails the audit; the script never creates an expected SHA
from an unbound payload. The public evidence projects the original SHA values and
roles without publishing private filesystem paths.

The 24 pairs require 48 command checks and 48 manifest checks (30 distinct contracts
and 30 distinct manifest contents), plus 116 raw-output checks. Of those raw checks,
84 use hashes declared by their original output manifests and 32 use the existing
artifact index. Five negative checks reject a wrong command hash, wrong manifest
hash, a same-size changed raw file, missing raw hash authority and a foreign model
identity. Counts and rejection reasons are in `original_binding_audit.json`. The
reinforced binding checks leave all prior numerical results and pair decisions
unchanged. Only a literal boolean `True` from the normal similarity policy can
satisfy that gate; unavailable results cannot count as success.

Twenty pairs have equal primitive operators and equal numerical results on both
stored output sets. Their Full-output replay also reproduces the exact stored
hotloop detections. These are local semantic comparisons, not new scientific claim
releases. Runtime comparability and development/screening roles remain unchanged.
Forty input-set comparisons are documented in `yolo_energy_semantic_evidence.json`.

Four pairs remain limited: YOLO11l/H8 and H10 Vendor Full use a raw DFL/regression-
classification decoder whereas the Split uses decoded-pre-NMS output. They lack a
common primitive-input proof. Their local Full reprocessing also differs from the
stored records by at most 5.960464477539063e-08 in a score field; this is reported,
not rounded into exact identity. YOLO26s/H8 and H10 Vendor Full reproduce their
stored outputs exactly but match only 9/14 reference detections, below the original
0.8 threshold. Original mean IoU and thresholds are in `two_full_negative_replay.json`.
Those two records are valid negative results, not missing outputs or new jobs.

The normal `native_producer_validate_visualize.py --existing-outputs-only` two-Full
CLI was also run. That loader currently supports stored TRT Full references and
returns unavailable for these Vendor Fulls. The conclusive negative replay above
therefore uses the same frozen product postprocessor and normal detection matcher
on the already bound Vendor Full output/reference reports. This does not claim
that the unsupported CLI branch has been changed or has produced a semantic PASS.

`terminal_quality_projection_45.csv` joins all 45 historical secondary quality
warnings to the corrected 588-case scope by exact model/case/setup/run identity:
21 negative builds and 24 policy exclusions. Quality is not applicable, and none
is an outstanding quality request.

`scripts/replay_semantics.py` reproduces the private raw-output audit when its five
explicit original inputs are supplied (`--pairs`, `--native`, `--validation`,
`--base-validation`, `--base-artifact-index`; `--out` selects a new output folder).
It requires the released tool environment
and the original local arrays, which are deliberately not published in Git. The
compact JSON and CSV are the public numerical/contract evidence; public plot
reproduction consumes these small inputs without accessing private raw payloads.
