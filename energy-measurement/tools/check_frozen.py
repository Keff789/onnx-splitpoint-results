#!/usr/bin/env python3
"""Run known standard-library result checks in temporary copies, never on raw data.

Existing script paths and bytes stay frozen. Uses the local pre-move Git commit
for their original layout; this is also the entry point for legacy path-dependent
checks after reorganisation. Requires no network or third-party Python modules.
"""
from pathlib import Path, PurePosixPath
import argparse, io, json, shutil, stat, subprocess, sys, tempfile, zipfile

CHECKS=[
 'energy-measurement/2026-09-30-offline-windows/verify.py',
 'energy-measurement/2026-10-01-controlled-rate-test/verify.py',
 'energy-measurement/2026-09-29-jetson-window-pause/verify.py',
 'energy-measurement/2026-10-09-offline-robustness/review/audit_scope_results.py',
]


def run(repo,required=False):
    state=json.loads((repo/'energy-measurement/tools/reorganization.json').read_text())
    base=state['source_commit']
    out=subprocess.run(['git','-C',str(repo),'archive','--format=zip',base,'--','energy-measurement'],capture_output=True)
    if out.returncode:raise RuntimeError('Local base commit unavailable: '+out.stderr.decode(errors='replace'))
    reports=[]
    with tempfile.TemporaryDirectory(prefix='energy-layout-check-') as t:
        scratch=Path(t)
        with zipfile.ZipFile(io.BytesIO(out.stdout)) as z:
            for info in z.infolist():
                rel=PurePosixPath(info.filename)
                if rel.is_absolute() or '..' in rel.parts or stat.S_ISLNK(info.external_attr>>16):
                    raise RuntimeError('Unsafe original snapshot member')
                if info.is_dir():continue
                p=scratch.joinpath(*rel.parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(info))
        for rel in CHECKS:
            path=scratch/rel
            if not path.is_file():
                if required:raise RuntimeError('Required original check missing: '+rel)
                reports.append({'script':rel,'status':'not present'});continue
            result=subprocess.run([sys.executable,str(path)],cwd=path.parent,capture_output=True,text=True,timeout=180)
            if result.returncode:raise RuntimeError('Original check failed: '+rel+'\n'+(result.stdout+result.stderr)[-6000:])
            reports.append({'script':rel,'status':'PASS','output':(result.stdout+result.stderr)[-3000:]})
        tim=repo/'energy-measurement/papers/tim-v0.3'
        timcopy=scratch/'TIM';shutil.copytree(tim,timcopy)
        result=subprocess.run([sys.executable,str(timcopy/'scripts/verify_results.py')],cwd=timcopy,capture_output=True,text=True,timeout=180)
        if result.returncode:raise RuntimeError('TIM numerical audit failed:\n'+(result.stdout+result.stderr)[-6000:])
        reports.append({'script':'TIM v0.3 scripts/verify_results.py','status':'PASS','output':(result.stdout+result.stderr)[-3000:]})
    return reports

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    p.add_argument('--required',action='store_true')
    a=p.parse_args()
    try:
        results=run(a.repo.resolve(),a.required)
        for r in results:print(r['status']+': '+r['script'])
        print('No source files, raw waveforms or measurement settings changed.')
    except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired) as e:
        print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
