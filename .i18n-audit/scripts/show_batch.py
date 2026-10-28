from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'.i18n-audit'
manifest=json.loads((OUT/'manifest/resources.json').read_text(encoding='utf-8'))
by_id={r['id']:r for r in manifest['records']}
batches=json.loads((OUT/'manifest/translation_batches.json').read_text(encoding='utf-8'))['batches']
if len(sys.argv)<2:
    for b in batches:
        print(b['batch_id'],b['namespace'],b['record_count'])
else:
    batch_id=sys.argv[1]
    batch=next(b for b in batches if b['batch_id']==batch_id)
    print(json.dumps({k:batch[k] for k in ('batch_id','source_kind','namespace','record_count')},ensure_ascii=False))
    for i,rid in enumerate(batch['record_ids'],1):
        r=by_id[rid]
        if r['source_kind']=='json-locale':
            key=r['key']
        else:
            key=f"{r['namespace']}.{r['key']}"
        zh=r['values'].get('zh') or ''
        ko=r['values'].get('ko') or ''
        print(f"{i:02d}\t{key}\t{zh}\t{ko}")
