#!/usr/bin/env python3
"""Publish only the checked Figure-5 artifact; never replace an existing release."""
from pathlib import Path
import hashlib,json,os,sys,urllib.request,urllib.error,urllib.parse,zipfile
R=Path(__file__).resolve().parent
REPO='Keff789/onnx-splitpoint-results';TAG='parma-figure5-v0.15.1'

def api(method,path,payload=None,raw=None,mime='application/json'):
    url=path if path.startswith('https://uploads.github.com/') else 'https://api.github.com/repos/'+REPO+path
    body=raw if raw is not None else (json.dumps(payload).encode() if payload is not None else None)
    req=urllib.request.Request(url,data=body,method=method,headers={
        'Authorization':'Bearer '+os.environ['GITHUB_TOKEN'],
        'Accept':'application/vnd.github+json','Content-Type':mime,
        'X-GitHub-Api-Version':'2022-11-28','User-Agent':'parma-artifact-publisher'})
    try:
        with urllib.request.urlopen(req,timeout=120) as resp: return json.load(resp)
    except urllib.error.HTTPError as exc:
        if method=='GET' and exc.code==404:return None
        raise RuntimeError(f'GitHub {method} failed with HTTP {exc.code}') from exc

def main():
    if os.environ.get('GITHUB_REPOSITORY')!=REPO or not os.environ.get('GITHUB_SHA'):
        raise SystemExit('Run only in the authorized repository workflow.')
    qa=json.loads((R/'generated/device_figure_qa.json').read_text())
    assert qa['status']=='PASS' and qa['unique_executions']==105
    prov=json.loads((R/'PROVENANCE.json').read_text())
    assert hashlib.sha256((R/'pairs.json').read_bytes()).hexdigest()==prov['pairs_json_sha256']
    head=os.environ['GITHUB_SHA'];prior=api('GET','/releases/tags/'+TAG)
    if prior:
        if prior['target_commitish']!=head:raise SystemExit('Tag belongs to another commit; refusing replacement.')
        if prior['draft']:raise SystemExit('An incomplete draft exists; inspect it rather than overwrite it.')
        print('Existing release:',prior['html_url']);return
    (R/'BUILD_RECEIPT.json').write_text(json.dumps({'source_commit':head,'tag':TAG,'qa':qa,
        'scope':'Figure 5 and its paired data, not the complete manuscript'},indent=2)+'\n')
    out=R/'dist';out.mkdir(exist_ok=True)
    archive=out/'PARMA_Figure5_v0151.zip'
    fixed=['README.md','CITATION.cff','RIGHTS_AND_AVAILABILITY.md','PROVENANCE.json',
           'pairs.json','summary.csv','figure.py','reproduce.py','requirements.txt','BUILD_RECEIPT.json']
    files=[R/p for p in fixed]+sorted((R/'generated').glob('*'))+sorted((R/'figures').glob('*'))
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for p in files:
            if p.is_file():z.write(p,'PARMA_Figure5_v0151/'+str(p.relative_to(R)))
    assets=[archive,R/'figures/device_pair_medians.pdf',R/'figures/device_pair_medians.png',
            R/'summary.csv',R/'pairs.json',R/'BUILD_RECEIPT.json']
    sums=out/'SHA256SUMS.txt'
    sums.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in assets))
    assets.append(sums)
    release=api('POST','/releases',{'tag_name':TAG,'target_commitish':head,
        'name':'PARMA v0.15.1 — paired measurement artifact',
        'body':'Compact executable Figure-5 companion to the Jetson-only PARMA author draft. '
        '105 physical executions, 315 paired comparisons, all 21 medians and empirical percentiles; '
        'original recording IDs retained. Includes the vector figure, preview, paired data, generator and QA. '
        'The complete eleven-page manuscript and full source archive are separate deliverables; '
        'this release does not claim to reconstruct the entire paper or raw waveforms. '
        'No DOI, proceedings acceptance, new calibration or artifact-evaluation badge is claimed. '
        'Source commit: `'+head+'`. See the README and rights notice.',
        'draft':True,'prerelease':True,'make_latest':'false'})
    for p in assets:
        url='https://uploads.github.com/repos/'+REPO+'/releases/'+str(release['id'])+'/assets?name='+urllib.parse.quote(p.name)
        mime={'.pdf':'application/pdf','.png':'image/png','.zip':'application/zip'}.get(p.suffix,'application/octet-stream')
        api('POST',url,raw=p.read_bytes(),mime=mime)
    final=api('PATCH','/releases/'+str(release['id']),{'draft':False,'prerelease':True,'make_latest':'false'})
    print('Published release:',final['html_url'])
    for a in final.get('assets',[]):print(a['name'],a['browser_download_url'])

if __name__=='__main__':main()
