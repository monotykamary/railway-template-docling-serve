#!/usr/bin/env python3
"""Strict phase-aware product smoke. Test state is external to application volumes."""
import base64, hashlib, json, os, pathlib, re, secrets, time
import requests
BASE=os.environ['BASE_URL'].rstrip('/')
PHASE=os.environ['SMOKE_PHASE']
assert PHASE in ('boot','upgrade','redeploy'), PHASE
STATE=pathlib.Path(__file__).with_name('.state-'+hashlib.sha256(BASE.encode()).hexdigest()[:16]+'.json')
def seed(create):
    if PHASE=='boot':
        if STATE.exists(): return json.loads(STATE.read_text())
        data=create(); STATE.write_text(json.dumps(data)); return data
    assert STATE.exists(), 'missing boot seed; refusing to create during '+PHASE
    return json.loads(STATE.read_text())
def check(r, expected=200):
    assert r.status_code==expected, ('unexpected HTTP status', r.request.method, r.status_code); return r

# Docling's conversion endpoint is stateless: assert the same boot-authored input
# converts after upgrade/redeploy, not a claim of stored document persistence.
key=os.environ['API_KEY']; headers={'X-Api-Key':key}
check(requests.get(BASE+'/readyz',timeout=60))
assert check(requests.get(BASE+'/version',timeout=30)).json()
record=seed(lambda:{'marker':'Railway Docling '+secrets.token_hex(8)})
payload={'options':{'from_formats':['md'],'to_formats':['md','text'],'do_ocr':False,'do_table_structure':False},'sources':[{'kind':'file','base64_string':base64.b64encode(('# '+record['marker']+'\n\nConversion works.').encode()).decode(),'filename':'validation.md'}]}
assert requests.post(BASE+'/v1/convert/source',json=payload,timeout=30).status_code in (401,403)
r=check(requests.post(BASE+'/v1/convert/source',headers=headers,json=payload,timeout=300))
assert record['marker'] in r.text, 'conversion lost document content'
assert requests.post(BASE+'/v1/convert/source',headers=headers,json={'file_sources':[]},timeout=30).status_code in (400,422)
print(json.dumps({'phase':PHASE,'conversion':'passed','negative_auth':'passed','invalid_input':'passed','persistence':'not applicable: stateless conversion service'}))
