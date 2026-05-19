"""Emit a conservative JSON environment record without environment variables."""
import importlib.metadata as md,json,os,platform,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def git_revision():
    try:return subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,text=True,capture_output=True,check=True,timeout=2).stdout.strip()
    except Exception:return None
record={
 'python':sys.version,'python_executable':sys.executable,
 'platform':platform.platform(),'machine':platform.machine(),'processor':platform.processor() or None,
 'cpu_count':os.cpu_count(),'project_revision':git_revision(),
 'packages':sorted(({'name':d.metadata['Name'],'version':d.version} for d in md.distributions() if d.metadata['Name']),key=lambda x:x['name'].lower()),
 'note':'No environment variables are collected; record model, data, device, dtype, shapes and seed per experiment.'}
print(json.dumps(record,indent=2))
