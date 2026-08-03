#!/usr/bin/env python3
import os,requests,base64
base=os.environ['BASE_URL'].rstrip('/');key=os.environ['API_KEY'];headers={'X-Api-Key':key}
ready=requests.get(base+'/readyz',timeout=60);assert ready.status_code==200
version=requests.get(base+'/version',timeout=30);assert version.status_code==200 and version.json()
payload={'options':{'from_formats':['md'],'to_formats':['md','text'],'do_ocr':False,'do_table_structure':False},'sources':[{'kind':'file','base64_string':base64.b64encode(b'# Railway Docling Validation\n\nConversion works.').decode(),'filename':'railway-validation.md'}]}
blocked=requests.post(base+'/v1/convert/source',json=payload,timeout=30);assert blocked.status_code in (401,403)
converted=requests.post(base+'/v1/convert/source',headers=headers,json=payload,timeout=300);assert converted.status_code==200 and 'Railway Docling Validation' in converted.text
invalid=requests.post(base+'/v1/convert/source',headers=headers,json={'file_sources':[]},timeout=30);assert invalid.status_code in (400,422)
print('Docling Serve smoke checks passed')
