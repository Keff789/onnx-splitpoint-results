# Inventory

`collect_from_smartmirror2.sh --collect` generates:

- `collected_files.tsv`: repository-relative path, byte size and mtime;
- `source_candidates.tsv`: existence and size of important source trees;
- `missing_sources.txt`: expected evidence not found during collection.

No new checksum or seal manifest is generated. Existing evidence-side
`SHA256SUMS.txt` files may be copied as ordinary historical records.

`COLLECTION=PASS_WITH_MISSING` means that the copy process completed safely but
one or more expected inputs were unavailable. Always inspect
`missing_sources.txt`; only `COLLECTION=PASS` means that every source explicitly
requested by the collector was found.
