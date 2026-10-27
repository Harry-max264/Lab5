from pathlib import Path
import subprocess,sys
r=Path(__file__).resolve().parents[2]
for n in ['primary','contrast_1','contrast_2']:
 subprocess.run([sys.executable,str(r/'tools/build_prompt.py'),'--agent','agents/diffusion_agent','--case',f'agents/diffusion_agent/cases/{n}.json'],cwd=r,check=True)
 p=r/f'work/diffusion_agent_{n}_prompt.txt'
 p.write_text(p.read_text()+'\n# DATED EVIDENCE PACKET\n'+(r/'agents/diffusion_agent/records/evidence_register.md').read_text())
