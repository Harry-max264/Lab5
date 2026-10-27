from pathlib import Path
import json, hashlib
r=Path(__file__).resolve().parents[2]
a=r/'agents/diffusion_agent'
s=json.loads((r/'core/output_schema.json').read_text())
outs=[json.loads((a/f'responses/{n}_response.json').read_text()) for n in ['primary','contrast_1','contrast_2']]
for o in outs:
 assert set(o)==set(s['required'])
 assert all(x in o['application_finding'] for x in ['Relative advantage','Compatibility','Complexity','Trialability','Observability'])
for o in outs[1:]:
 assert o['general_et_finding']==outs[0]['general_et_finding']
 assert o['application_finding']==outs[0]['application_finding']
 assert o['evidence']==outs[0]['evidence']
 assert o['recommendation_management_implication']!=outs[0]['recommendation_management_implication']
p=json.loads((a/'cases/primary.json').read_text())
for n in ['contrast_1','contrast_2']:
 c=json.loads((a/f'cases/{n}.json').read_text())
 assert [k for k in p if p[k]!=c[k]]==['adoption_posture']
weak=json.loads((a/'responses/primary_weak_v1_0.json').read_text())
assert 'early majority' in weak['general_et_finding']
assert 'cannot be assigned' in outs[0]['general_et_finding']
print('PASS: exact output keys, five factors, posture-only contrasts, stable evidence, changed timing, preserved failure')
