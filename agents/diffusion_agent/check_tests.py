from pathlib import Path
import json,hashlib
def validate(data,schema):
 kind=schema.get('type')
 types={'object':dict,'array':list,'string':str}
 if kind in types: assert isinstance(data,types[kind]), f'Wrong type {kind}'
 if kind=='object':
  assert set(schema.get('required',[]))<=set(data), 'Missing required field'
  props=schema.get('properties',{})
  if schema.get('additionalProperties') is False: assert set(data)<=set(props), 'Extra field'
  for k,v in data.items():
   if k in props: validate(v,props[k])
 if kind=='array':
  for item in data: validate(item,schema.get('items',{}))
# All supplied frozen schemas use only object/array/string, required, properties,
# items and additionalProperties constraints. This bounded checker covers them.
r=Path(__file__).resolve().parents[2];a=r/'agents/diffusion_agent'
s=json.loads((r/'core/output_schema.json').read_text());i=json.loads((r/'core/input_schema.json').read_text())
outs=[]
for n in ['primary','contrast_1','contrast_2']:
 c=json.loads((a/f'cases/{n}.json').read_text());validate(c,i)
 o=json.loads((a/f'responses/{n}_response.json').read_text());validate(o,s);outs.append(o)
 assert all(f in o['application_finding'] for f in ['Relative advantage','Compatibility','Complexity','Trialability','Observability'])
 assert {'S3','S4'}<=set(e['source_or_reference'].split()[0] for e in o['evidence'])
 assert 'roadmap' in o['application_finding'] and 'pilot' in o['application_finding']
for o in outs[1:]:
 assert o['evidence']==outs[0]['evidence']
 assert o['general_et_finding']==outs[0]['general_et_finding']
 assert o['recommendation_management_implication']!=outs[0]['recommendation_management_implication']
p=json.loads((a/'cases/primary.json').read_text())
for n in ['contrast_1','contrast_2']:
 c=json.loads((a/f'cases/{n}.json').read_text());assert [k for k in p if p[k]!=c[k]]==['adoption_posture']
m=json.loads((a/'records/run_manifest.json').read_text())
for item in m['runs']:
 for label in ['prompt','response']:
  assert hashlib.sha256((r/item[label+'_path']).read_bytes()).hexdigest()==item[label+'_sha256']
print('PASS full frozen input/output JSON schemas; five factors; application evidence; posture-only contrasts; stable evidence; changed timing; packet/response hashes')
print('LIMIT: automated checks do not prove truth, independence, operational results or professional quality')
