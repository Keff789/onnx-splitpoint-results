#!/usr/bin/env python3
"""Verify exact public Git blobs and table structure; no raw/hardware claim."""
import csv,hashlib,json
from pathlib import Path,PurePosixPath
root=Path(__file__).resolve().parent
manifest=json.loads((root/'GIT_BLOBS.json').read_text())
for name,expected in manifest['git_blob_sha1'].items():
    rel=PurePosixPath(name)
    if rel.is_absolute() or '..' in rel.parts:
        raise SystemExit('Unsafe manifest path')
    b=(root/name).read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if actual!=expected: raise SystemExit('FAIL: '+name)
q=json.loads((root/'EVIDENCE.json').read_text())
b=q['full_batch']
if b['integrated']+b['time_axis_failures']!=b['planned_npy_paths']:
    raise SystemExit('FAIL: file counts')
if b['legacy_reproduced']+b['legacy_mismatches']!=b['integrated']:
    raise SystemExit('FAIL: legacy counts')
for name in ('duration_examples.csv','sweep_endpoints.csv'):
    with (root/'data'/name).open() as f:
        if not list(csv.DictReader(f)):raise SystemExit('FAIL: empty table')
print('PASS: exact public Git blobs and table structure; no raw/hardware verification')
