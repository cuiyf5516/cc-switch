from __future__ import annotations
import json,re
from collections import defaultdict
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'.i18n-audit'
CONFIG=json.loads((OUT/'config.json').read_text(encoding='utf-8'))

def atomic_json(path:Path,value:Any)->None:
 path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_suffix(path.suffix+'.tmp'); tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); tmp.replace(path)
def safe(v:str)->str: return re.sub(r'[^a-zA-Z0-9._-]+','-',v).strip('-')
def reviews()->dict[str,dict[str,Any]]:
 out={}
 for p in sorted((OUT/'reviews/hardcoded').glob('*.json')):
  try: data=json.loads(p.read_text(encoding='utf-8'))
  except Exception: continue
  for r in data.get('records',[]): out[r.get('id')]=r
 return out
def main()->int:
 path=OUT/'manifest/hardcoded_candidates.json'; data=json.loads(path.read_text(encoding='utf-8'))
 existing=reviews(); restored=stale=0
 for c in data['candidates']:
  r=existing.get(c['id'])
  if not r: continue
  if r.get('content_fingerprint')==c['content_fingerprint'] and r.get('status') in CONFIG['candidate_statuses']:
   c['status']=r['status']; c['review']=r; restored+=1
  else: stale+=1
 grouped=defaultdict(list)
 for c in data['candidates']:
  parts=c['source_file'].split('/')
  group='/'.join(parts[:3]) if len(parts)>2 else c['source_file']
  grouped[group].append(c)
 size=int(CONFIG.get('hardcoded_batch_size',40)); batches=[]; n=0
 for group,items in sorted(grouped.items()):
  items.sort(key=lambda x:(x['source_file'],x['line'],x['column'],x['id']))
  for idx,start in enumerate(range(0,len(items),size),1):
   n+=1; chunk=items[start:start+size]
   batch_id=f'hardcoded:{n:04d}:{safe(group)}'
   batch={'batch_id':batch_id,'kind':'hardcoded','group':group,'ordinal':idx,'record_count':len(chunk),'record_ids':[c['id'] for c in chunk]}
   batches.append(batch)
   for c in chunk: c['review_batch']=batch_id
   atomic_json(OUT/'batches/hardcoded'/f'{safe(batch_id)}.json',batch)
 atomic_json(path,data)
 atomic_json(OUT/'manifest/hardcoded_batches.json',{'schema_version':1,'batch_size':size,'batch_count':len(batches),'candidate_count':len(data['candidates']),'restored_valid_reviews':restored,'stale_reviews':stale,'batches':batches})
 print(json.dumps({'candidates':len(data['candidates']),'batches':len(batches),'restored':restored,'stale':stale},ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
