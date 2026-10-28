from __future__ import annotations
import json,sys
from collections import Counter,defaultdict
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'.i18n-audit'
CONFIG=json.loads((OUT/'config.json').read_text(encoding='utf-8'))
TRANSLATION_STATUSES=set(CONFIG['translation_statuses'])
CANDIDATE_STATUSES=set(CONFIG['candidate_statuses'])
errors=[]; warnings=[]

def load(path:Path)->Any: return json.loads(path.read_text(encoding='utf-8'))
def pct(n:int,d:int)->float: return round(100*n/d,2) if d else 0.0

def validate_translation()->dict[str,Any]:
 manifest=load(OUT/'manifest/resources.json'); batches=load(OUT/'manifest/translation_batches.json')
 records=manifest['records']; by_id={r['id']:r for r in records}
 if len(by_id)!=len(records): errors.append('translation: duplicate resource IDs')
 if manifest.get('duplicate_keys'): errors.append(f'translation: {len(manifest["duplicate_keys"])} duplicate JSON keys')
 if manifest.get('parse_issues'): errors.append(f'translation: {len(manifest["parse_issues"])} parse issues')
 assigned=defaultdict(list)
 for b in batches['batches']:
  for rid in b['record_ids']: assigned[rid].append(b['batch_id'])
 for r in records:
  if len(assigned.get(r['id'],[]))!=1: errors.append(f'translation: resource not assigned exactly once: {r["id"]}')
 reviews={}; review_duplicates=[]
 for path in sorted((OUT/'reviews/translations').glob('*.json')):
  data=load(path)
  for rr in data.get('records',[]):
   if rr['id'] in reviews: review_duplicates.append(rr['id'])
   reviews[rr['id']]=rr
 if review_duplicates: errors.append(f'translation: duplicate review records: {len(review_duplicates)}')
 valid={}; stale=[]; malformed=[]
 for rid,rr in reviews.items():
  r=by_id.get(rid)
  if not r: stale.append(rid); continue
  if rr.get('combined_fingerprint')!=r['combined_fingerprint']: stale.append(rid); continue
  if rr.get('status') not in TRANSLATION_STATUSES: malformed.append(rid); continue
  if rr['status'] in {'必改','建议改'} and not rr.get('suggestion'): malformed.append(rid)
  if rr['status'] in {'必改','建议改','待核实'} and not rr.get('reason'): malformed.append(rid)
  if not rr.get('semantic_trace'): malformed.append(rid)
  valid[rid]=rr
 if stale: errors.append(f'translation: {len(stale)} stale/orphan reviews')
 if malformed: errors.append(f'translation: {len(malformed)} malformed review records')
 counts=Counter(valid[r['id']]['status'] for r in records if r['id'] in valid)
 unreviewed=sum(1 for r in records if r['id'] not in valid)
 batch_complete=0
 for b in batches['batches']:
  if all(rid in valid for rid in b['record_ids']): batch_complete+=1
 parsed=sum(1 for f in manifest['locale_files'] if f['string_count'])
 return {
  'resource_count':len(records),'locale_file_count':len(manifest['locale_files']),
  'parsed_locale_file_count':parsed,'duplicate_key_count':len(manifest['duplicate_keys']),
  'parse_issue_count':len(manifest['parse_issues']),'batch_count':len(batches['batches']),
  'complete_batch_count':batch_complete,'valid_review_count':len(valid),'unreviewed_count':unreviewed,
  'status_counts':dict(counts),'stale_review_count':len(stale),
  'batch_coverage_pct':pct(len([b for b in batches['batches'] if b['record_ids']]),len(batches['batches'])),
  'effective_review_coverage_pct':pct(len(valid),len(records)),
  'extraction_coverage_pct':pct(parsed,len(manifest['locale_files'])),
 }

def validate_hardcoded()->dict[str,Any]:
 manifest=load(OUT/'manifest/hardcoded_candidates.json'); plans=load(OUT/'manifest/hardcoded_batches.json')
 candidates=manifest['candidates']; by_id={c['id']:c for c in candidates}
 if len(by_id)!=len(candidates): errors.append('hardcoded: duplicate candidate IDs')
 assigned=defaultdict(list)
 for b in plans['batches']:
  for cid in b['record_ids']: assigned[cid].append(b['batch_id'])
 for c in candidates:
  if len(assigned.get(c['id'],[]))!=1: errors.append(f'hardcoded: candidate not assigned exactly once: {c["id"]}')
 reviews={}; dups=[]
 for path in sorted((OUT/'reviews/hardcoded').glob('*.json')):
  data=load(path)
  for rr in data.get('records',[]):
   if rr['id'] in reviews: dups.append(rr['id'])
   reviews[rr['id']]=rr
 if dups: errors.append(f'hardcoded: duplicate review records: {len(dups)}')
 valid={}; stale=[]; malformed=[]
 for cid,rr in reviews.items():
  c=by_id.get(cid)
  if not c: stale.append(cid); continue
  if rr.get('content_fingerprint')!=c['content_fingerprint']: stale.append(cid); continue
  if rr.get('status') not in CANDIDATE_STATUSES: malformed.append(cid); continue
  if not rr.get('reason'): malformed.append(cid)
  valid[cid]=rr
 if stale: errors.append(f'hardcoded: {len(stale)} stale/orphan reviews')
 if malformed: errors.append(f'hardcoded: {len(malformed)} malformed reviews')
 counts=Counter(valid[c['id']]['status'] for c in candidates if c['id'] in valid)
 failed=manifest['failed_source_file_count']
 if failed: errors.append(f'hardcoded: {failed} source files failed scanning')
 if manifest['scanned_source_file_count']+failed != manifest['included_source_file_count']:
  errors.append('hardcoded: source file accounting mismatch')
 batch_complete=sum(1 for b in plans['batches'] if all(cid in valid for cid in b['record_ids']))
 return {
  'source_file_count':manifest['source_file_count'],'included_source_file_count':manifest['included_source_file_count'],
  'excluded_source_file_count':manifest['excluded_source_file_count'],'scanned_source_file_count':manifest['scanned_source_file_count'],
  'failed_source_file_count':failed,'candidate_count':len(candidates),'batch_count':len(plans['batches']),
  'complete_batch_count':batch_complete,'valid_review_count':len(valid),
  'unreviewed_count':len(candidates)-len(valid),'status_counts':dict(counts),
  'scan_coverage_pct':pct(manifest['scanned_source_file_count'],manifest['included_source_file_count']),
  'candidate_review_coverage_pct':pct(len(valid),len(candidates)),
  'dynamic_translation_key_count':sum(1 for c in candidates if c['source_kind']=='dynamic_i18n_key'),
  'dynamic_translation_key_reviewed':sum(1 for c in candidates if c['source_kind']=='dynamic_i18n_key' and c['id'] in valid),
 }

def validate_quality(tr:dict[str,Any])->dict[str,Any]:
 tr_manifest=load(OUT/'manifest/resources.json'); hc_manifest=load(OUT/'manifest/hardcoded_candidates.json')
 tr_keep=[r['id'] for r in tr_manifest['records'] if r.get('review_status')=='可保留']
 tr_issues={r['id'] for r in tr_manifest['records'] if r.get('review_status') in {'必改','建议改','待核实'}}
 hc_confirmed={c['id'] for c in hc_manifest['candidates'] if c['status']=='确认遗漏'}
 hc_pending={c['id'] for c in hc_manifest['candidates'] if c['status']=='待核实'}
 hc_no_i18n=[c['id'] for c in hc_manifest['candidates'] if c['status']=='无需国际化']
 qpath=OUT/'reviews/quality/second_round.json'
 if not qpath.exists():
  errors.append('quality: second-round review file is absent')
  return {'present':False}
 q=load(qpath)
 tq=q.get('translation',{}); hq=q.get('hardcoded',{})
 t_sample=set(tq.get('keep_sample_ids',[])); t_issue=set(tq.get('issue_recheck_ids',[]))
 h_sample=set(hq.get('no_i18n_sample_ids',[])); h_confirmed=set(hq.get('confirmed_recheck_ids',[])); h_pending=set(hq.get('pending_recheck_ids',[]))
 t_required=(len(tr_keep)*15+99)//100; h_required=(len(hc_no_i18n)*15+99)//100
 if len(t_sample)<t_required: errors.append(f'quality: translation keep sample {len(t_sample)} < required {t_required}')
 if tr_issues-t_issue: errors.append(f'quality: {len(tr_issues-t_issue)} translation issues not rechecked')
 if hc_confirmed-h_confirmed: errors.append(f'quality: {len(hc_confirmed-h_confirmed)} confirmed hardcoded items not rechecked')
 if hc_pending-h_pending: errors.append(f'quality: {len(hc_pending-h_pending)} pending hardcoded items not rechecked')
 if len(h_sample)<h_required: errors.append(f'quality: no-i18n sample {len(h_sample)} < required {h_required}')
 invalid_t=t_sample-set(tr_keep); invalid_h=h_sample-set(hc_no_i18n)
 if invalid_t: errors.append(f'quality: {len(invalid_t)} translation sample IDs are no longer kept')
 if invalid_h: errors.append(f'quality: {len(invalid_h)} hardcoded sample IDs are no longer no-i18n')
 return {
  'present':True,
  'translation_keep_sample_required':t_required,
  'translation_keep_sample_reviewed':len(t_sample),
  'translation_issue_recheck_count':len(t_issue),
  'hardcoded_confirmed_recheck_count':len(h_confirmed),
  'hardcoded_pending_recheck_count':len(h_pending),
  'hardcoded_no_i18n_sample_required':h_required,
  'hardcoded_no_i18n_sample_reviewed':len(h_sample),
 }

def main()->int:
 tr=validate_translation(); hc=validate_hardcoded(); q=validate_quality(tr)
 report={'translation':tr,'hardcoded':hc,'quality':q,'errors':errors,'warnings':warnings,
         'completion_conditions_met':not errors and tr['unreviewed_count']==0 and hc['unreviewed_count']==0 and q.get('present')}
 path=OUT/'reports/validation.json'; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))
 return 0 if report['completion_conditions_met'] else 1
if __name__=='__main__': raise SystemExit(main())
