#!/usr/bin/env python3
"""Read-only verification of preserved files and generated catalogue targets."""
from pathlib import Path
import argparse, csv, hashlib, json, os, sys


def verify(repo):
    state=json.loads((repo/'energy-measurement/tools/reorganization.json').read_text())
    for old,entry in state['files'].items():
        p=repo/entry['new_path']
        if not p.exists() and not p.is_symlink():raise ValueError('Missing: '+entry['new_path'])
        data=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
        sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        mode='120000' if p.is_symlink() else ('100755' if p.stat().st_mode&0o111 else '100644')
        if sha!=entry['sha'] or mode!=entry['mode']:raise ValueError('Changed original: '+old)
    with (repo/'energy-measurement/CATALOG.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    for row in rows:
        if not (repo/row['path']).is_file():raise ValueError('Missing catalogue target: '+row['path'])
    return len(state['files']),len(rows)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    a=p.parse_args()
    try:
        n,m=verify(a.repo.resolve());print(f'PASS: {n} original files preserved; {m} catalogue targets present.')
    except (OSError,ValueError,KeyError) as e:
        print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
