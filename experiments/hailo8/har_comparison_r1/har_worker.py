#!/usr/bin/env python3
"""Execute exactly one pre-existing HAR using the installed DFC emulator.

This script calls no optimize, parser/translation, compile or HAR-save API.
SDK_NATIVE and SDK_QUANTIZED are deliberately not substituted for each other.
"""
from __future__ import annotations
import argparse, inspect, json, os, sys, time, traceback
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import bound, identity, read_json, write_json

def output_array(result,count,classes):
    import numpy as np
    selected=None
    if isinstance(result,dict):
        if len(result)!=1:raise ValueError('Mehrdeutige HAR-Ausgaenge; keine Auswahl nach Accuracy')
        selected,result=next(iter(result.items()))
    elif isinstance(result,(list,tuple)):
        if len(result)!=1:raise ValueError('Mehrdeutige HAR-Ausgangsliste')
        result=result[0]
    if hasattr(result,'numpy'):result=result.numpy()
    a=np.asarray(result)
    original=list(a.shape)
    if a.shape not in {(count,classes),(count,1,1,classes),(count,1,classes)}:
        raise ValueError('HAR-Ausgangsform nicht explizit NC-kompatibel: '+repr(a.shape))
    a=a.reshape(count,classes)
    if a.dtype.kind!='f' or not np.isfinite(a).all():raise ValueError('HAR-Ausgabe nicht finite Floatwerte; keine erratene Dequantisierung')
    return a,{'selected_output':str(selected) if selected is not None else None,'original_shape':original}

def run(req,stage,out):
    import numpy as np
    from importlib.metadata import version
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    report={'status':'started','stage':stage,'context':'SDK_NATIVE' if stage=='parsed_native' else 'SDK_QUANTIZED',
      'new_hef_build':False,'new_optimization':False,'hardware_inference':False,
      'requested_execution':'CPU emulation (not performance measurement)','cuda_visible_devices':os.environ.get('CUDA_VISIBLE_DEVICES')}
    started=time.monotonic();har=req['hars'][stage]
    try:
        sdk_version=version('hailo-dataflow-compiler');report['sdk_version']=sdk_version
        if sdk_version!=req['sdk_version']:raise ValueError('DFC-Version gegenueber Originalbuild geaendert: '+sdk_version)
        path=bound(har);feed=np.load(bound(req['feed']),allow_pickle=False)
        if feed.shape!=(16,224,224,3) or feed.dtype!=np.float32:raise ValueError('Eingangsformat falsch')
        before=feed.copy()
        from hailo_sdk_client import ClientRunner, InferenceContext
        enum=getattr(InferenceContext,report['context'],None)
        if enum is None:raise RuntimeError('Installierte SDK-Version bietet '+report['context']+' nicht; keine Ersetzung')
        report['api']={k:str(inspect.signature(getattr(ClientRunner,k))) for k in ('infer_context','infer','get_hn')}
        runner=ClientRunner(har=str(path),hw_arch='hailo8')
        report['runner_state_before']=str(getattr(runner,'state','not_exposed'))
        hn=runner.get_hn()
        if isinstance(hn,(bytes,str)):hn=json.loads(hn)
        if not isinstance(hn,dict) or hn.get('name')!=req['net_name']:
            raise ValueError('HAR-Netzname stimmt nicht mit Originalbuild ueberein')
        layers=hn.get('layers',{})
        inputs={k:v for k,v in layers.items() if isinstance(v,dict) and v.get('type')=='input_layer'}
        outputs={k:v for k,v in layers.items() if isinstance(v,dict) and v.get('type')=='output_layer'}
        report['hn']={'name':hn['name'],'layer_count':len(layers),'input_layers':inputs,'output_layers':outputs}
        if len(inputs)!=1 or len(outputs)!=1:raise ValueError('Expliziter Single-Input-/Single-Output-HAR erforderlich')
        write_json(out/'api_and_model.json',report)
        # Public inference context only. No modification of the saved HAR.
        with runner.infer_context(enum) as context:
            result=runner.infer(context,np.ascontiguousarray(feed))
        value,output_info=output_array(result,16,1000)
        if not np.array_equal(feed,before):raise ValueError('SDK hat den Eingangsbuffer veraendert')
        bound(har);bound(req['feed'])
        array_path=out/'logits.npy';np.save(array_path,value,allow_pickle=False)
        report.update(status='evaluated',output=identity(array_path),output_info=output_info,
            image_ids=req['image_ids'],feed_sha256=req['feed']['sha256'],feed_unchanged=True,
            har=har,har_unchanged=True,elapsed_s=time.monotonic()-started,
            runner_state_after=str(getattr(runner,'state','not_exposed')))
    except Exception as exc:
        report.update(status='failed',error=type(exc).__name__+': '+str(exc),traceback=traceback.format_exc(),elapsed_s=time.monotonic()-started)
        traceback.print_exc()
    write_json(out/'result.json',report)
    return 0 if report['status']=='evaluated' else 2

def main():
    p=argparse.ArgumentParser();p.add_argument('--request',required=True,type=Path);p.add_argument('--stage',required=True,choices=['parsed_native','quantized']);p.add_argument('--out',required=True,type=Path);a=p.parse_args()
    return run(read_json(a.request),a.stage,a.out)
if __name__=='__main__':raise SystemExit(main())
