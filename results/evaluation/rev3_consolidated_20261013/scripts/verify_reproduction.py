#!/usr/bin/env python3
"""Compare actual output files and byte hashes with the checked-in reproduction."""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--expected',type=Path,default=Path(__file__).resolve().parents[1]/'results');p.add_argument('--actual',type=Path,required=True);a=p.parse_args()
def hashes(root):
 return {str(x.relative_to(root)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(root.rglob('*')) if x.is_file() and x.name!='OUTPUT_MANIFEST.json'}
e=hashes(a.expected);r=hashes(a.actual);assert e==json.loads((a.expected/'OUTPUT_MANIFEST.json').read_text()),'Checked-in results disagree with their manifest';assert r==json.loads((a.actual/'OUTPUT_MANIFEST.json').read_text()),'Reproduced files disagree with their manifest';assert e==r,{'only_expected':sorted(e.keys()-r.keys()),'only_actual':sorted(r.keys()-e.keys()),'different':[x for x in e.keys()&r.keys() if e[x]!=r[x]]}
print(json.dumps({'status':'PASS','matching_output_files':len(e),'output_manifest_sha256':hashlib.sha256((a.actual/'OUTPUT_MANIFEST.json').read_bytes()).hexdigest()},sort_keys=True))
