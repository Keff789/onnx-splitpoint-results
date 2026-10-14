#!/usr/bin/env python3
"""Run an offline script with Python audit guards against hidden source access."""
import json,os,runpy,sys
from pathlib import Path
script=Path(sys.argv[1]).resolve();sys.argv=sys.argv[1:]
original_repo=Path.home()/'onnx-splitpoint-results'
canonical_archive=Path.home()/'diss_results'
# Historical SM2 namespace, neighboring F archive, network and subprocess are forbidden.
def guard(event,args):
 if event in ['socket.connect','socket.getaddrinfo','subprocess.Popen','os.system']:
  raise RuntimeError('Offline replay rejected '+event)
 if event=='open' and isinstance(args[0],(str,bytes,os.PathLike)):
  p=os.path.realpath(os.fsdecode(args[0]))
  if (p.startswith('/home/') or '/diss_results_native_fairness_rev3_20261007/' in p
      or Path(p).is_relative_to(original_repo) and not script.is_relative_to(original_repo)
      or Path(p).is_relative_to(canonical_archive) and not script.is_relative_to(canonical_archive)):
   raise RuntimeError('Hidden source read rejected: '+p)
sys.addaudithook(guard)
runpy.run_path(str(script),run_name='__main__')
