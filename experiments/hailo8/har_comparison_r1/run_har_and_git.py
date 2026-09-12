#!/usr/bin/env python3
"""Compare existing Hailo8 HARs, collect compact original evidence, then review/push.

No HEF build, optimization, hardware inference, installation, profile or cache changes.
The executable is intentionally independent of ONNX-Splitpoint-Tool v2.80.4.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, stat, subprocess, sys, tempfile, time, zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import (TEXT_SUFFIXES, MAX_TEXT, child_env, identity, immutable_copy,
                    interlock, plain, read_json, safe_rel, supervised, text_bytes, write_json)

HERE=Path(__file__).resolve().parent
PREFIX='results/hailo8/20260912_mobilenet_gpu'
ALLOWED_REMOTES={
 'https://github.com/Keff789/onnx-splitpoint-results',
 'https://github.com/Keff789/onnx-splitpoint-results.git',
 'git@github.com:Keff789/onnx-splitpoint-results',
 'git@github.com:Keff789/onnx-splitpoint-results.git',
 'ssh://git@github.com/Keff789/onnx-splitpoint-results.git'}


def git(repo,*args,check=True,input=None,env=None):
    p=subprocess.run(['git','-C',str(repo),*args],input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
    if check and p.returncode:
        raise RuntimeError('git '+args[0]+': '+p.stderr.decode('utf-8','replace').strip())
    return p


def validate_repo(repo):
    repo=plain(repo)
    if git(repo,'rev-parse','--show-toplevel').stdout.decode().strip()!=str(repo):
        raise ValueError('Pfad ist nicht die Wurzel des Ergebnisrepositorys')
    if git(repo,'diff','--cached','--name-only','-z').stdout:
        raise ValueError('Es gibt bereits vorgemerkte Aenderungen. Nicht veraendert; bitte separat pruefen.')
    if git(repo,'ls-files','--unmerged','-z').stdout:raise ValueError('Ungelöster Git-Merge')
    for name in ['MERGE_HEAD','CHERRY_PICK_HEAD','REVERT_HEAD','rebase-merge','rebase-apply']:
        p=Path(git(repo,'rev-parse','--git-path',name).stdout.decode().strip())
        if not p.is_absolute():p=repo/p
        if p.exists():raise ValueError('Laufende Git-Operation: '+name)
    branch=git(repo,'symbolic-ref','--quiet','--short','HEAD').stdout.decode().strip()
    head=git(repo,'rev-parse','HEAD').stdout.decode().strip()
    urls=git(repo,'remote','get-url','--push','--all','origin').stdout.decode().splitlines()
    fetch=git(repo,'remote','get-url','origin').stdout.decode().strip()
    if len(urls)!=1 or urls[0] not in ALLOWED_REMOTES or fetch not in ALLOWED_REMOTES:
        raise ValueError('origin ist nicht eindeutig Keff789/onnx-splitpoint-results; kein automatischer Remotewechsel')
    if git(repo,'config','--bool','--get','remote.origin.mirror',check=False).stdout.strip()==b'true':
        raise ValueError('Mirror-Remote nicht erlaubt')
    checker=plain(repo/'scripts/check_before_commit.py')
    if not checker.is_file():raise ValueError('Vorhandener scripts/check_before_commit.py fehlt')
    return {'repo':str(repo),'branch':branch,'head':head,'origin':urls[0],'checker':str(checker)}


def archive_candidates(home,block):
    downloads=home/'Downloads'
    if block['id']=='compute':
        p=downloads/'hailo8_gpu_test_20260912T062240Z_hx7b7hcq.zip'
        return [p,*sorted(downloads.glob(p.stem+'([0-9]*).zip'))]
    if block['id']=='build':
        p=downloads/'hailo8_mobilenet_gpu_20260912T083456Z_a_10a8wv.zip'
        return [p,*sorted(downloads.glob(p.stem+'([0-9]*).zip'))]
    if block['id']=='runtime':
        return [downloads/'hailo8_mobilenet_runtime_8FehkBqO/runtime_evidence.zip']
    return [downloads/'quality_snapshot.zip',*sorted(downloads.glob('v2803_quality_snapshot_*/quality_snapshot.zip'))]


def extract_selected(source,block,dest):
    """Strict member allowlist, text-only, exact original bytes; never extractall."""
    source=plain(source);inventory=[];total=0
    with zipfile.ZipFile(source) as z:
        infos={}
        for i in z.infolist():
            if i.filename in infos:raise ValueError('Doppeltes ZIP-Mitglied '+i.filename)
            infos[i.filename]=i
        for row in block['members']:
            name=row['member'];safe_rel(name)
            i=infos.get(name)
            if i is None:raise ValueError('Fehlendes originales ZIP-Mitglied '+name)
            if stat.S_ISLNK(i.external_attr>>16) or i.is_dir():raise ValueError('Kein regulaeres Ergebnis '+name)
            if i.file_size!=row['size_bytes'] or i.file_size>MAX_TEXT:raise ValueError('Groesse abweichend '+name)
            rel=safe_rel(row['destination'])
            if rel.suffix.lower() not in TEXT_SUFFIXES:raise ValueError('Nicht freigegebener Ergebnisdateityp '+str(rel))
            raw=z.read(i)
            if hashlib.sha256(raw).hexdigest()!=row['sha256']:raise ValueError('Originale Ergebnisbytes abweichend '+name)
            if b'\x00' in raw:raise ValueError('Binaerdatei nicht erlaubt '+name)
            raw.decode('utf8');total+=len(raw)
            if total>512*1024*1024:raise ValueError('Kuratierter Quellenblock ueber 512 MiB')
            immutable_copy(raw,dest/rel)
            inventory.append({'source_archive':str(source),'member':name,'destination':str(rel),
                'size_bytes':len(raw),'sha256':row['sha256']})
    return inventory


def collect_originals(home,out,runtime_dir,build_dir):
    spec=read_json(HERE/'selection.json');dest=out/'git_payload';dest.mkdir(exist_ok=True)
    report={'blocks':{},'files':[]}
    for block in spec['sources']:
        candidates=archive_candidates(home,block)
        if block['id']=='runtime':candidates.insert(0,runtime_dir.parent/'runtime_evidence.zip')
        if block['id']=='build':candidates.insert(0,build_dir.with_suffix('.zip'))
        found=[]
        for p in candidates:
            if p.is_file() and str(p) not in [str(x) for x in found]:found.append(p)
        if not found:
            report['blocks'][block['id']]={'status':'missing','required':block['required'],'searched':list(map(str,candidates))}
            continue
        selected=None;errors=[]
        # Select only the exact already reviewed archive content. No newest-file guessing.
        for p in found:
            try:
                rows=extract_selected(p,block,dest);report['files']+=rows;selected=p;break
            except Exception as exc:errors.append(str(p)+': '+str(exc))
        report['blocks'][block['id']]={'status':'collected' if selected else 'invalid',
            'required':block['required'],'source':str(selected) if selected else None,'errors':errors}
    report['required_complete']=all(v['status']=='collected' for v in report['blocks'].values() if v['required'])
    write_json(out/'collection.json',report)
    return report


def validate_input_snapshot(out, build, runtime):
    """Bind the new HAR test to the same original evidence being archived."""
    payload=out/'git_payload'/PREFIX
    pairs=[
        (build/'request.json',payload/'build_metadata/request.json'),
        (build/'summary.json',payload/'build_metadata/summary.json'),
        (build/'build_result.json',payload/'build_metadata/build_result.json'),
        (build/'private_hef_receipt.json',payload/'build_metadata/private_hef_receipt.json'),
        (runtime/'runtime_request.json',payload/'runtime/runtime_request.json'),
        (runtime/'comparison.json',payload/'runtime/comparison.json'),
        (runtime/'results/runtime_result.json',payload/'runtime/results/runtime_result.json')]
    for local,archived in pairs:
        if not archived.is_file():
            raise ValueError('Originaler Archivbeleg fehlt fuer HAR-Bindung: '+str(archived))
        if text_bytes(local)!=text_bytes(archived):
            raise ValueError('Lokale Diagnosequelle weicht vom Originalarchiv ab: '+str(local))


def run_comparison(a,out):
    diag=out/'har_comparison';diag.mkdir(exist_ok=True)
    env=child_env(out/'private_workspace')
    phases={};interrupted=False
    try:
        with interlock(a.home):
            validate_input_snapshot(out,a.build_dir,a.runtime_dir)
            cmd=[sys.executable,'-I','-B',str(HERE/'array_compare.py'),'prepare','--build',str(a.build_dir),
                 '--runtime',str(a.runtime_dir),'--out',str(diag)]
            phases['prepare']=supervised(cmd,out/'private_workspace',env,300,diag/'prepare.log')
            write_json(diag/'prepare_process.json',phases['prepare'])
            interrupted=phases['prepare']['cancelled']
            if phases['prepare']['returncode']==0 and phases['prepare']['process_cleanup_complete'] and not interrupted and not phases['prepare']['timed_out']:
                req=read_json(diag/'comparison_request.json')
                py=Path(req['venv_python']).expanduser()
                # Venv python is normally a symlink: executable path stays inside selected venv,
                # realpath must NOT replace it with the system interpreter.
                if not py.is_absolute() or not os.access(py,os.X_OK):raise ValueError('Hailo8-Venv-Python nicht ausführbar: '+str(py))
                for stage in ('parsed_native','quantized'):
                    d=diag/stage;d.mkdir(exist_ok=True)
                    print('HAR_STAGE_START='+stage+' (CPU-Emulation, kein Neubau)',flush=True)
                    cmd=[str(py),'-I','-B',str(HERE/'har_worker.py'),'--request',str(diag/'comparison_request.json'),
                         '--stage',stage,'--out',str(d)]
                    phases[stage]=supervised(cmd,out/'private_workspace',env,a.stage_timeout,d/'console.log')
                    write_json(d/'process.json',phases[stage])
                    result=read_json(d/'result.json') if (d/'result.json').exists() else {}
                    print('HAR_STAGE_STATUS='+stage+':'+str(result.get('status','no_result')),flush=True)
                    if result.get('error'):print('HAR_STAGE_ERROR='+str(result['error']),flush=True)
                    if phases[stage]['cancelled'] or not phases[stage]['process_cleanup_complete']:
                        interrupted=phases[stage]['cancelled'];break
                cmd=[sys.executable,'-I','-B',str(HERE/'array_compare.py'),'compare',
                     '--request',str(diag/'comparison_request.json'),'--out',str(diag)]
                phases['compare']=supervised(cmd,out/'private_workspace',env,120,diag/'compare.log')
                write_json(diag/'compare_process.json',phases['compare'])
            else:
                print('HAR_COMPARE_PREPARATION=failed; keine HAR-Emulation gestartet',flush=True)
                if (diag/'prepare_error.json').exists():
                    print('HAR_COMPARE_ERROR='+str(read_json(diag/'prepare_error.json').get('error')),flush=True)
    except KeyboardInterrupt:interrupted=True
    except Exception as exc:
        write_json(diag/'controller_error.json',{'error':type(exc).__name__+': '+str(exc)})
        print('HAR_COMPARE_ERROR='+type(exc).__name__+': '+str(exc),flush=True)
    result=read_json(diag/'comparison.json') if (diag/'comparison.json').exists() else {}
    status='cancelled' if interrupted else result.get('status','incomplete')
    write_json(diag/'controller_summary.json',{'status':status,'phases':phases,'hef_build':'NOT_RUN',
        'hardware_inference':'NOT_RUN','energy':'NOT_RUN','product_configuration_modified':False})
    return status


def finish_payload(out,collection,status):
    payload=out/'git_payload';stamp=out.name
    # Copy only reviewed small report names from the new diagnostic, never raw NPY/NPZ/HAR.
    fixed=['comparison_request.json','prepare_result.json','prepare_error.json','compare_error.json',
           'prepare.log','prepare_process.json','compare.log','compare_process.json','controller_error.json',
           'controller_summary.json','comparison.json','per_image.csv','REPORT.md']
    fixed += [s+'/'+n for s in ('parsed_native','quantized') for n in ('result.json','process.json','console.log','api_and_model.json')]
    for rel in fixed:
        p=out/'har_comparison'/rel
        if p.is_file():immutable_copy(text_bytes(p),payload/PREFIX/'har_emulation'/stamp/rel)
    for name in ('run_har_and_git.py','array_compare.py','har_worker.py','common.py','selection.json','README.md','TEST_REPORT.md','run.sh'):
        p=HERE/name
        if p.is_file():immutable_copy(text_bytes(p),payload/'experiments/hailo8/har_comparison_r1'/name)
    index={'schema':'hailo8-evidence-addition-r1','har_comparison_status':status,
        'original_sources':collection,'model_files_in_git':False,'raw_arrays_in_git':False,
        'original_results_modified':False,'comparison_is_not_quality_gate':True,
        'local_har_results':str(out/'har_comparison')}
    write_json(payload/PREFIX/'har_emulation'/stamp/'INDEX.json',index)
    (payload/PREFIX/'har_emulation'/stamp/'CLAIM_BOUNDARIES.md').write_text(
      '# Abgrenzung\n\nOriginale Compute-, GPU-Build- und Fixed16-Nachweise bleiben getrennt erhalten.\n'
      'HAR-Emulation ist eine neue Diagnose auf denselben 16 bereits geöffneten Developmentbildern.\n'
      'Kein neuer HEF-Build, keine erneute Hailo-Hardwaremessung, kein Bootstrap, keine finale Qualitätsfreigabe.\n'
      'Die HARs gehören laut originalem Buildbericht zum privaten GPU-Build. Ihre Inhaltsprüfsummen wurden erst jetzt erfasst.\n'
      'Quantized-HAR versus CPU-HEF ist ein Vergleich verschiedener Builds, keine Rekonstruktion des alten CPU-HAR.\n'
      'Ein negativer numerischer Befund wird weder entfernt noch als neuer Produktfehler vorentschieden.\n')
    archive=out/'har_and_git_evidence.zip';temporary=out/'.har_and_git_evidence.zip.tmp'
    with zipfile.ZipFile(temporary,'x',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(payload.rglob('*')):
            if p.is_file():
                plain(p)
                if p.suffix.lower() not in TEXT_SUFFIXES:raise ValueError('Nicht-Text im Git-Payload')
                z.writestr(p.relative_to(payload).as_posix(),text_bytes(p))
    os.link(temporary,archive);temporary.unlink()
    write_json(out/'ready_for_git.json',{'payload':str(payload),'status':status,'required_complete':collection['required_complete']})
    print('HAR_COMPARISON_STATUS='+status,flush=True)
    print('EVIDENCE_ZIP='+str(archive),flush=True)
    return archive


def payload_rows(payload):
    rows=[];total=0
    for p in sorted(payload.rglob('*')):
        if not p.is_file():continue
        plain(p);rel=p.relative_to(payload)
        safe_rel(rel.as_posix())
        if p.suffix.lower() not in TEXT_SUFFIXES:raise ValueError('Dateityp nicht erlaubt: '+str(rel))
        raw=text_bytes(p);total+=len(raw)
        if total>512*1024*1024:raise ValueError('Git-Payload groesser als 512 MiB')
        rows.append((rel,raw))
    return rows


def publish(out,repo,push):
    cfg=validate_repo(repo);payload=plain(out/'git_payload');rows=payload_rows(payload)
    # Pre-check every destination before creating any new result file.
    for rel,raw in rows:
        dest=plain(repo/rel)
        if dest.exists() and text_bytes(dest)!=raw:raise ValueError('Zielkonflikt; nicht ersetzt: '+str(rel))
    for rel,raw in rows:immutable_copy(raw,repo/rel)
    paths=[rel.as_posix() for rel,_ in rows]
    raw_paths=b''.join(s.encode()+b'\0' for s in paths)
    pathfile=out/'git_paths.nul';pathfile.write_bytes(raw_paths)
    # Check only the curated payload (same repository checker), not unrelated local files.
    p=subprocess.run([sys.executable,'-I','-B',cfg['checker'],str(payload)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (out/'pre_commit_check.log').write_bytes(p.stdout);print(p.stdout.decode('utf8','replace'),flush=True)
    if p.returncode:raise RuntimeError('Pre-Commit-Prüfung blockiert; kein Commit/Push')
    dirty=git(repo,'status','--short','--',PREFIX,'experiments/hailo8/har_comparison_r1').stdout.decode('utf8','replace')
    print(dirty or 'Ergebnisdateien bereits vorhanden.',flush=True)
    print(f"GIT_TARGET={cfg['origin']} BRANCH={cfg['branch']}\nSELECTED_FILES={len(rows)}",flush=True)
    if not push:
        print('GIT_COMMIT=NOT_RUN; GIT_PUSH=NOT_RUN');return
    state=read_json(out/'ready_for_git.json')
    print('HAR_STATUS='+state['status']+'; auch negative/unvollständige Diagnose wird ehrlich archiviert.',flush=True)
    if not state['required_complete']:print('WARNUNG: mindestens ein ursprünglicher Evidenzblock fehlt; INDEX.json beachten.',flush=True)
    print('Die Originalprotokolle enthalten lokale Pfade und Netzwerkadressen. Vor Veröffentlichung prüfen.',flush=True)
    print('Es werden keine bestehenden Ergebnisdateien ersetzt, keine Modelle/HARs/Arrays aufgenommen.',flush=True)
    if input('Zum Commit und Push exakt PUSH eingeben: ').strip()!='PUSH':
        print('GIT_PUSH=NOT_CONFIRMED; Dateien nur lokal gesammelt');return
    # A normal push publishes every ancestor. Refuse pre-existing, unreviewed outgoing commits.
    current=validate_repo(repo)
    if current['head']!=cfg['head'] or current['branch']!=cfg['branch'] or current['origin']!=cfg['origin']:
        raise RuntimeError('Git-Zustand hat sich während der Prüfung geändert')
    remote=git(repo,'ls-remote','--heads','origin','refs/heads/'+cfg['branch']).stdout.decode().splitlines()
    remote_heads=[line.split()[0] for line in remote if line.endswith('\trefs/heads/'+cfg['branch'])]
    if remote_heads != [cfg['head']]:
        raise RuntimeError('Lokaler HEAD und origin/'+cfg['branch']+' sind nicht synchron. Kein automatisches Pull/Rebase/Force-Push. '
                           'Ergebnisse bleiben lokal; Repository separat abgleichen und --publish-existing verwenden.')
    for rel,raw in rows:
        if text_bytes(repo/rel)!=raw:raise RuntimeError('Ausgewählte Ergebnisdatei wurde verändert: '+str(rel))
    git(repo,'add','--pathspec-from-file='+str(pathfile),'--pathspec-file-nul')
    staged=git(repo,'diff','--cached','--name-only','-z').stdout.split(b'\0')
    staged={x.decode() for x in staged if x}
    if not staged.issubset(set(paths)):raise RuntimeError('Fremde Git-Stagingänderung erkannt; kein Commit')
    if not staged:
        print('GIT_STATUS=already_archived; kein leerer Commit');return
    print(git(repo,'diff','--cached','--stat').stdout.decode(),flush=True)
    # --only ensures unrelated staged edits cannot enter this commit.
    git(repo,'commit','--only','-m','Archive Hailo8 GPU evidence and fixed16 HAR comparison',
        '--pathspec-from-file='+str(pathfile),'--pathspec-file-nul')
    commit=git(repo,'rev-parse','HEAD').stdout.decode().strip()
    parents=git(repo,'rev-list','--parents','-n','1',commit).stdout.decode().split()
    changed=set(x.decode() for x in git(repo,'diff-tree','--no-commit-id','--name-only','-r','-z',commit).stdout.split(b'\0') if x)
    if parents != [commit,cfg['head']] or not changed.issubset(set(paths)):
        raise RuntimeError('Commit enthält unerwarteten Umfang; nicht gepusht')
    (out/'git_commit.txt').write_text(commit+'\n')
    for rel,raw in rows:
        if git(repo,'show',commit+':'+rel.as_posix()).stdout!=raw:
            raise RuntimeError('Commitdatei weicht von geprüften Bytes ab; nicht gepusht: '+str(rel))
    # Fixed commit and full refspec, no force, no implicit tags or other branches.
    p=git(repo,'-c','push.followTags=false','push','--porcelain','--no-follow-tags','origin',
          commit+':refs/heads/'+cfg['branch'],check=False)
    (out/'git_push.log').write_bytes(p.stdout+p.stderr);print((p.stdout+p.stderr).decode('utf8','replace'),flush=True)
    if p.returncode:
        raise RuntimeError('Push fehlgeschlagen; lokaler Commit bleibt erhalten. NICHT Force-Push verwenden. '
                           'Nach Klärung genau diesen Commit normal pushen: '+commit+':refs/heads/'+cfg['branch'])
    print('GIT_PUSH=PASS\nCOMMIT='+commit,flush=True)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path.home()/'onnx-splitpoint-results')
    p.add_argument('--home',type=Path,default=Path.home())
    p.add_argument('--build-dir',type=Path,default=Path.home()/'Downloads/hailo8_mobilenet_gpu_20260912T083456Z_a_10a8wv')
    p.add_argument('--runtime-dir',type=Path,default=Path.home()/'Downloads/hailo8_mobilenet_runtime_8FehkBqO/runtime')
    p.add_argument('--stage-timeout',type=int,default=600)
    p.add_argument('--push',action='store_true')
    p.add_argument('--publish-existing',type=Path,help='Nur vorhandenen kuratierten Nachtrag übernehmen; keine erneute HAR-Emulation')
    a=p.parse_args(argv)
    for key in ('repo','home','build_dir','runtime_dir'):setattr(a,key,getattr(a,key).expanduser().absolute())
    if a.stage_timeout<30 or a.stage_timeout>3600:raise ValueError('stage-timeout muss 30..3600 Sekunden sein')
    out=None
    try:
        if a.publish_existing:
            out=plain(a.publish_existing);read_json(out/'ready_for_git.json');publish(out,a.repo,a.push);return 0
        # No Git writes before long diagnosis; error here prevents wasted work.
        validate_repo(a.repo)
        a.home.joinpath('Downloads').mkdir(exist_ok=True)
        out=Path(tempfile.mkdtemp(prefix='hailo8_har_git_'+time.strftime('%Y%m%dT%H%M%SZ',time.gmtime())+'_',dir=a.home/'Downloads'))
        print('WORK_DIRECTORY='+str(out),flush=True)
        print('MODE=HAR_inference_only; no new HEF; no install; no hardware; CPU_emulation',flush=True)
        collection=collect_originals(a.home,out,a.runtime_dir,a.build_dir)
        status=run_comparison(a,out)
        finish_payload(out,collection,status)
        if status=='cancelled':print('Benutzerabbruch: kein automatischer Git-Push');return 130
        publish(out,a.repo,a.push)
        return 0 if status=='diagnostic_evaluated' else 2
    except KeyboardInterrupt:
        print('ABORTED; kein weiterer Git-Schritt',file=sys.stderr);return 130
    except Exception as exc:
        print('STOP='+type(exc).__name__+': '+str(exc),file=sys.stderr)
        if out:
            print('RESULTS_KEPT='+str(out),flush=True)
            if (out/'git_commit.txt').exists():
                print('LOKALER_COMMIT_BLEIBT_ERHALTEN='+text_bytes(out/'git_commit.txt').decode().strip(),flush=True)
                print('Git-Push separat wiederholen; kein HAR-Neulauf und kein Force-Push.',flush=True)
            elif (out/'ready_for_git.json').exists():
                print('RETRY_WITHOUT_HAR=\n'+str(sys.executable)+' -I -B '+str(HERE/'run_har_and_git.py')+
                      ' --publish-existing '+str(out)+' --repo '+str(a.repo)+' --push',flush=True)
        return 2
if __name__=='__main__':raise SystemExit(main())
