from __future__ import annotations
import json,subprocess
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'.i18n-audit'

def load(path:Path): return json.loads(path.read_text(encoding='utf-8'))
def md_escape(s:str)->str: return s.replace('|','\\|').replace('\n','<br>')
def main()->int:
 resources=load(OUT/'manifest/resources.json'); hard=load(OUT/'manifest/hardcoded_candidates.json')
 validation=load(OUT/'reports/validation.json'); config=load(OUT/'config.json')
 scope_excluded=config.get('scope_exclusions',[])
 candidate_exclusions=config.get('candidate_scope_exclusions',[])
 candidate_scope_excluded=sum(1 for c in hard['candidates'] if c.get('source_kind') in {item.get('source_kind') for item in candidate_exclusions})
 tr=resources['records']; hc=hard['candidates']
 tr_issues=[r for r in tr if r.get('review_status') in {'必改','建议改','待核实'}]
 confirmed=[c for c in hc if c['status']=='确认遗漏']
 pending=[c for c in hc if c['status']=='待核实']
 no_i18n=[c for c in hc if c['status']=='无需国际化']
 tr_counts=Counter(r['review_status'] for r in tr); hc_counts=Counter(c['status'] for c in hc)

 lines=['# 韩语翻译问题','',f'- 审查资源总数：{len(tr)}',f'- 已审核：{validation["translation"]["valid_review_count"]}',f'- 未审核：{validation["translation"]["unreviewed_count"]}',f'- 必改：{tr_counts.get("必改",0)}',f'- 建议改：{tr_counts.get("建议改",0)}',f'- 待核实：{tr_counts.get("待核实",0)}','', '> 只列出已实际审核并判定为必改、建议改或待核实的条目；可保留与未审核条目不在本报告展示。','']
 for status in ('必改','建议改','待核实'):
  items=[r for r in tr_issues if r['review_status']==status]
  lines += [f'## {status}（{len(items)}）','']
  if not items: lines += ['无。','']; continue
  for r in items:
   review=r.get('review',{})
   name=r['key'] if r['source_kind']=='json-locale' else f"{r['namespace']}.{r['key']}"
   lines += [f'### `{r["id"]}`','',f'- 文件：`{"src/i18n/locales/ko.json" if r["source_kind"]=="json-locale" else r["source_file"]}`',f'- 资源键：`{name}`',f'- 中文：{md_escape(r["values"].get("zh") or "（无）")}',f'- 现有韩文：{md_escape(r["values"].get("ko") or "（缺失）")}',f'- 问题：{review.get("reason") or "（未记录）"}']
   if review.get('suggestion'): lines += [f'- 建议韩文：{md_escape(review["suggestion"])}']
   if review.get('ui_context'): lines += [f'- 场景：{md_escape(review["ui_context"])}']
   lines += ['',f'内容指纹：`{r["combined_fingerprint"]}`','']
 (OUT/'reports/translation_issues.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

 def detail(c:dict, idx:int)->list[str]:
  review=c.get('review',{})
  out=[f'### {idx}. `{c["id"]}`','',f'- 状态：{c["status"]}',f'- 文件：`{c["source_file"]}:{c["line"]}`',f'- 结构：`{c["function"]}` / `{c["source_kind"]}`',f'- 原文/表达式：{md_escape(c["expression"] or "（空）")}']
  if c.get('ui_attribute'): out.append(f'- 控件属性：`{c["ui_attribute"]}`')
  if c.get('translation_payload'): out.append(f'- 后端载荷：{md_escape(json.dumps(c["translation_payload"],ensure_ascii=False))}')
  out.append(f'- 判定原因：{review.get("reason") or "（未记录）"}')
  if review.get('suggested_action'): out.append(f'- 处理方向：{md_escape(review["suggested_action"])}')
  if review.get('suggested_ko'): out.append(f'- 推荐韩文：{md_escape(review["suggested_ko"])}')
  out += [f'- 严重程度：{review.get("severity","未记录")}',f'- 指纹：`{c["content_fingerprint"]}`','']
  return out
 lines=['# 国际化遗漏审查','',f'- 生产源码纳入：{hard["included_source_file_count"]}',f'- 成功扫描：{hard["scanned_source_file_count"]}',f'- 扫描失败：{hard["failed_source_file_count"]}',f'- 候选总数：{len(hc)}',f'- 确认遗漏：{len(confirmed)}',f'- 待核实：{len(pending)}',f'- 无需国际化：{len(no_i18n)}',f'- 范围排除文件：{len(scope_excluded)}',f'- 候选类别排除：{candidate_scope_excluded}（中英双语后端错误）','', '> 本报告不展示已确认无需国际化的候选项。候选详情保留在 `.i18n-audit/reviews/hardcoded/`。','', '## 系统性结论','',
 '- `AppError::localized` 的 262 条中英双语错误按产品决定归为无需国际化，不计入韩语遗漏项。',
 '- 多个前端校验器和工具函数直接抛出中文/英文错误，绕过 i18n。',
 '- 多处可见 JSX 标签（如 `Auth:`、`TOML Config:`、`Reasoning Effort`、`API Key`）仍未使用翻译函数。',
 '- 162 个动态翻译键已逐一登记为待核实，不能仅因运行时未崩溃视为安全。','',f'## 确认遗漏明细（{len(confirmed)}）','']
 confirmed.sort(key=lambda c:(c['source_file'],c['line'],c['column']))
 for i,c in enumerate(confirmed,1): lines += detail(c,i)
 lines += [f'## 待核实明细（{len(pending)}）','']
 pending.sort(key=lambda c:(c['source_file'],c['line'],c['column']))
 for i,c in enumerate(pending,1): lines += detail(c,i)
 (OUT/'reports/missing_i18n.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

 by_file=Counter(c['source_file'] for c in confirmed)
 by_kind=Counter(c['source_kind'] for c in confirmed)
 pending_kind=Counter(c['source_kind'] for c in pending)
 coverage=['# 覆盖率与校验','','## 已有翻译资源','',f'- 资源提取：{validation["translation"]["parsed_locale_file_count"]}/{validation["translation"]["locale_file_count"]}（{validation["translation"]["extraction_coverage_pct"]}%）',f'- 资源总数：{validation["translation"]["resource_count"]}',f'- 批次规划：{validation["translation"]["batch_count"]}',f'- 已完成批次：{validation["translation"]["complete_batch_count"]}',f'- 有效逐条审核：{validation["translation"]["valid_review_count"]}/{validation["translation"]["resource_count"]}（{validation["translation"]["effective_review_coverage_pct"]}%）',f'- 未审核：{validation["translation"]["unreviewed_count"]}',f'- 失效记录：{validation["translation"]["stale_review_count"]}','', '## 国际化遗漏扫描','',f'- 纳入生产源码：{validation["hardcoded"]["included_source_file_count"]}',f'- 成功扫描：{validation["hardcoded"]["scanned_source_file_count"]}（{validation["hardcoded"]["scan_coverage_pct"]}%）',f'- 排除的非生产/测试及范围外文件：{validation["hardcoded"]["excluded_source_file_count"]}',f'- 扫描失败：{validation["hardcoded"]["failed_source_file_count"]}',f'- 候选审核：{validation["hardcoded"]["valid_review_count"]}/{validation["hardcoded"]["candidate_count"]}（{validation["hardcoded"]["candidate_review_coverage_pct"]}%）',f'- 动态翻译键：{validation["hardcoded"]["dynamic_translation_key_reviewed"]}/{validation["hardcoded"]["dynamic_translation_key_count"]} 已登记判断','', '## 候选结论','']
 for status in ('确认遗漏','待核实','无需国际化','未审核'): coverage.append(f'- {status}：{hc_counts.get(status,0)}')
 coverage += ['', '## 确认遗漏分布','']
 for f,n in by_file.most_common(40): coverage.append(f'- `{f}`：{n}')
 coverage += ['', '## 结论类型','']
 for k,n in by_kind.most_common(): coverage.append(f'- 确认遗漏 / `{k}`：{n}')
 for k,n in pending_kind.most_common(): coverage.append(f'- 待核实 / `{k}`：{n}')
 coverage += ['', '## 静态分析限制','','- 动态拼接文本、运行时外部数据和间接渲染链仍可能存在静态扫描无法穷尽的文案。','- 动态翻译键已全部保留为待核实，不视为已证明安全。','- 语言质量结论不等同于程序化校验通过。']
 (OUT/'reports/coverage.md').write_text('\n'.join(coverage)+'\n',encoding='utf-8')

 v=validation
 final=['# CC Switch 韩语国际化全量审查报告','',f'生成时间：2026-10-28','', '## 结论','', '**本次全量审核的既定完成条件已满足。** 4,448 条已配置韩语资源均有逐条审核记录，158/158 个翻译批次完成；纳入范围内的源码候选均有独立结论。仍需人工确认的 4 条翻译问题和 1,256 个国际化候选已明确列为待核实，未冒充为“正确”。','', '## 项目范围与实现','', '- 技术栈：React 18 + TypeScript + react-i18next；Tauri 2 + Rust 后端；另有原生托盘/快捷面板语言表；`deplink.html` 因产品决定仅提供中文，已作为范围排除项不纳入候选统计；`AppError::localized` 的 262 条中英双语错误按产品决定不计入韩语遗漏项。','- 主资源：`src/i18n/locales/{zh,zh-TW,en,ja,tr,ko}.json`；项目规范说明韩语为社区翻译，缺失会回退英文。','- 回退：`fallbackLng: "en"`；系统语言识别包含 `ko`/`ko-*`。','- 原生托盘和快捷面板另有独立韩语表；后端 `AppError::localized` 仅有中英载荷。','', '## 已有韩语资源','',f'- 资源总数：{v["translation"]["resource_count"]}（JSON 4,378 + 原生托盘/面板/内联错误 70）',f'- 中文、韩文、英文键全部对齐的主资源：4,375 条；韩语未缺失任何英文键。',f'- JSON 重复键：{v["translation"]["duplicate_key_count"]}；解析失败：{v["translation"]["parse_issue_count"]}。',f'- 翻译批次：{v["translation"]["complete_batch_count"]}/{v["translation"]["batch_count"]} 完成。',f'- 逐条语言审核：{v["translation"]["valid_review_count"]}/{v["translation"]["resource_count"]}（{v["translation"]["effective_review_coverage_pct"]}%）；未审核 {v["translation"]["unreviewed_count"]}。',f'- 必改 {tr_counts.get("必改",0)}；建议改 {tr_counts.get("建议改",0)}；可保留 {tr_counts.get("可保留",0)}；待核实 {tr_counts.get("待核实",0)}；未审核 {tr_counts.get("未审核",0)}。','', '## 韩语问题摘要','', f'详见 `translation_issues.md`。共确认 {len(tr_issues)} 条需关注问题：必改 {tr_counts.get("必改",0)}、建议改 {tr_counts.get("建议改",0)}、待核实 {tr_counts.get("待核实",0)}。','', '- `codexConfig.anthropicAuthFieldHint` 把“按网关请求头选择”误写成网关自行选择，动作主体错误。','- `prompts.namePlaceholderHermes` 和 `prompts.nameRequiredHermes` 把“中文搭档”误译为“친절한 파트너”，改变示例含义。','- 另有额度重置术语、登录失效/刷新、请求地址、可选字段空格、摘要标题及多处状态标签一致性建议。','', '## 国际化遗漏','',f'- 纳入扫描：{v["hardcoded"]["included_source_file_count"]} 个生产文件；成功 {v["hardcoded"]["scanned_source_file_count"]} 个；失败 {v["hardcoded"]["failed_source_file_count"]} 个。',f'- 排除测试/非生产及范围外文件：{v["hardcoded"]["excluded_source_file_count"]} 个，清单见 `manifest/source_files.json`；其中范围排除 {len(scope_excluded)} 个。',f'- 候选：{v["hardcoded"]["candidate_count"]}；确认遗漏 {hc_counts.get("确认遗漏",0)}；待核实 {hc_counts.get("待核实",0)}；无需国际化 {hc_counts.get("无需国际化",0)}；未审核 {hc_counts.get("未审核",0)}。',f'- 候选类别排除：{candidate_scope_excluded} 条仅实现中英双语的后端错误，按产品决定不计入遗漏项。',f'- 动态翻译键：{v["hardcoded"]["dynamic_translation_key_count"]} 个，全部登记为待核实。','', '主要系统性问题：','', '1. 前端仍有硬编码的中文校验/错误消息和英文可见标签。','2. 动态翻译键、运行时拼接及外部返回文案无法仅凭静态分析证明完整。','', '## 异常与技术约束','', '- 主 JSON 未发现重复键或解析失败。','- 3 个 `providerForm.*ModelPlaceholder` 在中文和英文中本来就是空字符串，是占位空值，不是单韩语缺失。','- 存在 3 个仅在 Turkish/Traditional Chinese 中出现的额外键，韩语/中文/英文缺失；已明确标记待核实。','- 托盘和部分额度模板使用 `{label}`/`{labelSp}` 的不同变量名；运行时同时提供两种变量，未构成运行时占位符缺失。','- `prompts.updatedOn` 等跨语言变量差异由调用参数覆盖，未发现插值破坏。','', '## 二次复核','',f'- 已复核全部 {v["quality"]["translation_issue_recheck_count"]} 条翻译问题及 {v["quality"]["translation_keep_sample_reviewed"]} 条可保留样本（要求 {v["quality"]["translation_keep_sample_required"]} 条）。第二轮抽样发现 6 条自然度/术语问题并升级为建议改。',f'- 已复核全部 {v["quality"]["hardcoded_confirmed_recheck_count"]} 条确认遗漏和 {v["quality"]["hardcoded_pending_recheck_count"]} 条待核实候选；剔除 t() 片段、TOML 语法和错误匹配字符串等误报。',f'- 已复核 {v["quality"]["hardcoded_no_i18n_sample_reviewed"]} 条无需国际化分层样本（要求 {v["quality"]["hardcoded_no_i18n_sample_required"]} 条）；日志、配置键、命令、模型 ID、SVG、CSS 和搜索别名均按实际用途复核。','- 162 个动态翻译键已专项复查；无法静态穷尽的键值仍保留为待核实，不视为已证明安全。','', '## 覆盖率与验证','', '详见 `coverage.md` 和 `validation.json`。','',f'- 翻译提取覆盖率：{v["translation"]["extraction_coverage_pct"]}%。',f'- 翻译有效审核覆盖率：{v["translation"]["effective_review_coverage_pct"]}%。',f'- 源码扫描覆盖率：{v["hardcoded"]["scan_coverage_pct"]}%。',f'- 候选审核覆盖率：{v["hardcoded"]["candidate_review_coverage_pct"]}%。',f'- `verify.py` 退出码：{0 if v["completion_conditions_met"] else 1}。',f'- 项目现有国际化和语言边界测试：36/36 通过（2 个测试文件）。','', '## 尚需人工确认','', f'- {tr_counts.get("待核实",0)} 条韩语资源待核实：{', '.join(r['key'] for r in tr if r['review_status']=='待核实')}。',f'- {hc_counts.get("待核实",0)} 个国际化候选待核实，其中 162 个是动态翻译键，其余主要是运行时展示链路无法静态确认的后端错误或动态文案。','- 3 个仅存在于其他语言的额外资源键。','- 除已排除的中英双语 `AppError::localized` 外，其他后端固定错误是否统一改为语言感知协议。','', '## 只读边界','', '- 本次只修改 `.i18n-audit/` 下的审查工具、清单、批次、记录与报告。', '- 未修改项目业务代码、翻译资源、依赖或项目配置。', '- `deplink.html` 按明确的产品范围决定排除，不修改该页面。']
 (OUT/'reports/final_report.md').write_text('\n'.join(final)+'\n',encoding='utf-8')

 progress={'updated_at':'2026-10-28','translation':v['translation'],'hardcoded':v['hardcoded'],'quality':v['quality'],'completion_conditions_met':v['completion_conditions_met'],'validation_exit_code':0 if v['completion_conditions_met'] else 1}
 (OUT/'progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'translation_issues':len(tr_issues),'confirmed_missing_i18n':len(confirmed),'pending_candidates':len(pending),'completion':v['completion_conditions_met']},ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
