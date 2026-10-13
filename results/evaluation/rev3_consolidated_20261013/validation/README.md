# Validation and scope

- [Independent scientific review](INDEPENDENT_REVIEW.md): separate implementation of arithmetic and gate checks; limitations retained.
- [Canonical archive restoration](CANONICAL_RESTORATION.json): fresh extraction using only B, identical compact inputs and no new payload/cohort creation.
- [Fresh-process reproduction](FRESH_PROCESS_REPRODUCTION.json): exact output hashes with the documented Python dependencies.
- [Reference limits](REFERENCE_LIMITS.md): direct receipt-version gaps, historical source gap and broader unresolved branches.
- [Inherited source handoff](INHERITED_SM2_HANDOFF.json): transfer evidence taken over from the completed handoff, not repeated by Twix.
- [Indexed file overlap](ARCHIVE_INDEX_OVERLAP.json): archive accounting, not scientific coverage.

The Python audit guard resolves symlinks and rejects network, subprocess and hidden source reads. It is an in-process Python check, not an operating-system sandbox. None of these checks integrates raw sensor traces anew or reruns model inference or dataset evaluation.

Fresh-clone and remote-commit confirmation are recorded in the canonical private publication receipt after the final commit and push; the committed numerical output manifest remains the independent public comparison target.
