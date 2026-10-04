# Private raw archive: status at publication

The original primary campaign transfer is still running. It copies the base
contents directly into the established remote archive root. It was not stopped,
and no second full base copy or concurrent writer to the same destination was
started. Durable sequential copy jobs wait for its actual completion.

| Source role | Archive-relative destination | Status |
|---|---|---|
| Base campaign | `.` | User transfer in progress; target audit pending |
| Generic completion 192 | `_supplements/generic_completion_192_20261002/` | Sequential copy queued |
| Entire YOLO addition, all attempts/repairs | `_supplements/yolo_min3_20261002_222904/` | Sequential copy queued |
| Corrected base derivation | `_analysis/corrected_20261002_110429/` | Sequential copy queued |
| Joint analysis and review | `_analysis/final_20261004/` | Frozen final inputs queued |
| Historical and current source checkpoints | `_provenance/source_checkpoints/` | Private source snapshots and release kept separately |
| Original audit evidence | `_provenance/audits/` | Sequential copy queued |
| Exact external dependencies | `_external_artifacts/` | Bound local copies complete; remote archive copy queued |

204 original Completion plans and 246 original energy command contracts yield
3,817 explicit runtime-file bindings. 3,796 are locally available with matching
original bytes. 1,041 previously external references were downloaded read-only
as 1,023 files and verified against their pre-existing SHA identities. The actual
H8/b066 runtime library and all eight directly bound roles are preserved. Original
collector, dataset registry/manifests, reference paths and calibration evidence
are retained. This was not a model build or new data acquisition.

The 21 remaining references all identify one historical `native_output_endpoint.py`
source, SHA256 `aae20edc6a4bb19c40d00f82707e333d8c931a2ace23b641c426d099fb3a3d0e`.
Its original temporary suite paths no longer exist; targeted local source copies,
archives, original suite archives and available Git versions did not contain the
exact bytes. The original contracts and their recorded identity are preserved.
A current source version is not substituted for that historical identity. This
is a source-archive limitation, not an invented missing measurement or permission
to rerun the campaign.

Historical software-COW links retain their texts and provenance mapping. Identical
files are mapped to already retained primary paths; only differing software-test
evidence is copied separately. Broken negative-test links remain documented.
All 560 original quality requests and their saved CPU-reference paths were located
inside the retained source areas. Seven materialized validation manifests each
have 5,000 files with matching declared sizes; this is not a new image-content audit.

Directory type/size inventories and transfer byte counters are not full destination
content verification. No full rehash of the raw archive was required. The private
`archive_sources.tsv` and transfer logs hold exact original-to-archive mappings.
Complete archive acceptance remains pending until copies and destination checks
actually finish. No local or remote originals are deleted.
