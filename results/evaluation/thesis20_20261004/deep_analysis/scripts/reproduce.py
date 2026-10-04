"""One offline entry point; writes only under the explicit derived output root."""
import argparse,os,subprocess,sys
from pathlib import Path

def main():
    root=Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser();p.add_argument('--output-root',type=Path,default=root);p.add_argument('--source-root',type=Path,default=root/'source');a=p.parse_args()
    output=a.output_root.resolve();source=a.source_root.resolve()
    if output==source or output.is_relative_to(source):raise ValueError('Output cannot overwrite frozen source')
    output.mkdir(parents=True,exist_ok=True)
    # Three small additional projections are fixed inputs, not regenerated from
    # private originals during portable reproduction.
    if output!=root:
        import shutil
        (output/'inputs').mkdir(exist_ok=True)
        for f in (root/'inputs').glob('*.csv'):shutil.copy2(f,output/'inputs'/f.name)
    env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
    env.setdefault('MPLCONFIGDIR',str(output/'private/mpl'))
    for name in ['analyze_ranking.py','analyze_energy.py','analyze_quality_graph.py','render_figures.py']:
        subprocess.run([sys.executable,str(root/'scripts'/name),'--source-root',str(source),'--output-root',str(output)],check=True,env=env)
    print('Offline reproduction completed; no measurement or inference was executed.')
if __name__=='__main__':main()
