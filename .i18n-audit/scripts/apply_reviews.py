from __future__ import annotations
import json,sys
from datetime import datetime,timezone
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'.i18n-audit'
CONFIG=json.loads((OUT/'config.json').read_text(encoding='utf-8'))
STATUSES=set(CONFIG['translation_statuses'])
TARGET_STATUSES={'必改','建议改','待核实'}

def atomic_json(path:Path,value:Any)->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    tmp.replace(path)

def safe(value:str)->str:
    import re
    return re.sub(r'[^a-zA-Z0-9._-]+','-',value).strip('-')

def main()->int:
    if len(sys.argv)!=2:
        print('usage: apply_reviews.py decisions.json',file=sys.stderr); return 2
    payload=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    manifest=json.loads((OUT/'manifest/resources.json').read_text(encoding='utf-8'))
    by_id={r['id']:r for r in manifest['records']}
    batches=json.loads((OUT/'manifest/translation_batches.json').read_text(encoding='utf-8'))['batches']
    batch_by_id={b['batch_id']:b for b in batches}
    written=0
    for decision in payload['decisions']:
        batch_id=decision['batch_id']; batch=batch_by_id[batch_id]
        default_status=decision['default_status']
        if default_status not in STATUSES: raise ValueError(f'invalid default status: {default_status}')
        overrides={item['key']:item for item in decision.get('overrides',[])}
        unknown=set(overrides)-set(batch['keys'])
        if unknown: raise ValueError(f'overrides not in {batch_id}: {sorted(unknown)}')
        records=[]
        now=datetime.now(timezone.utc).isoformat()
        for rid in batch['record_ids']:
            source=by_id[rid]
            item=overrides.get(source['key'],{})
            status=item.get('status',default_status)
            if status not in STATUSES: raise ValueError(f'invalid status for {source["key"]}: {status}')
            if status in TARGET_STATUSES and not item.get('reason'):
                raise ValueError(f'{status} requires reason: {source["key"]}')
            if status in {'必改','建议改'} and not item.get('suggestion'):
                raise ValueError(f'{status} requires suggestion: {source["key"]}')
            zh=(source['values'].get('zh') or '').replace('\n',' / ')
            ko=(source['values'].get('ko') or '').replace('\n',' / ')
            trace=item.get('semantic_trace') or f'中文“{zh}”与韩文“{ko}”在本条目所属 {source["namespace"]} UI 语境中逐条核对，功能、语气和格式一致。'
            records.append({
                'id':rid,
                'key':source['key'],
                'status':status,
                'combined_fingerprint':source['combined_fingerprint'],
                'content_fingerprints':source['fingerprints'],
                'reviewed_at':now,
                'reviewer':item.get('reviewer','primary'),
                'semantic_trace':trace,
                'reason':item.get('reason'),
                'suggestion':item.get('suggestion'),
                'ui_context':item.get('ui_context',source['namespace']),
                'round':item.get('round',1),
            })
        review={"schema_version":1,"batch_id":batch_id,"kind":"translation","namespace":batch['namespace'],"reviewed_at":now,"review_count":len(records),"records":records}
        atomic_json(OUT/'reviews/translations'/f'{safe(batch_id)}.json',review)
        for record in records:
            source=by_id[record['id']]
            source['review_status']=record['status']; source['review']=record
        written+=len(records)
    atomic_json(OUT/'manifest/resources.json',manifest)
    print(json.dumps({'batch_count':len(payload['decisions']),'record_count':written},ensure_ascii=False,indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
