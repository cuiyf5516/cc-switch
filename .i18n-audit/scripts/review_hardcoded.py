from __future__ import annotations
import json,re
from datetime import datetime,timezone
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'.i18n-audit'
CONFIG=json.loads((OUT/'config.json').read_text(encoding='utf-8'))
CANDIDATE_EXCLUSIONS={item['source_kind']:item for item in CONFIG.get('candidate_scope_exclusions',[]) if item.get('source_kind')}

def atomic(path:Path,data:Any)->None:
 path.parent.mkdir(parents=True,exist_ok=True); tmp=path.with_suffix(path.suffix+'.tmp'); tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); tmp.replace(path)
def safe(v:str)->str: return re.sub(r'[^a-zA-Z0-9._-]+','-',v).strip('-')
def has_cjk(s:str)->bool: return bool(re.search(r'[\u3400-\u9fff\uac00-\ud7af]',s))
def natural(s:str)->bool:
 s=s.strip()
 return bool(s) and (has_cjk(s) or (re.search(r'[A-Za-z]',s) and (len(s.split())>=2 or re.search(r'[.!?:…]$',s))))
def technical_literal(s:str)->bool:
 s=s.strip()
 if not s: return True
 if re.fullmatch(r"[0-9.%+\-*/()\s]+",s): return True
 if re.fullmatch(r"[A-Za-z0-9_$./:@#?&=+\-\s]+",s) and not has_cjk(s) and not re.search(r"[.!?…:]$",s): return True
 if re.match(r"^(?:https?://|data:|mailto:|file:|/|\./|\.\./|~/|[A-Za-z]:\\)",s): return True
 if re.fullmatch(r"[a-z][a-z0-9-]*(?:\.[a-z0-9-]+)+",s,re.I): return True
 if re.fullmatch(r"[A-Z][A-Z0-9_]+",s): return True
 return False

def line_context(path:str,line:int,radius:int=3)->str:
 try: lines=(ROOT/path).read_text(encoding='utf-8').splitlines()
 except Exception: return ''
 return '\n'.join(lines[max(0,line-radius-1):min(len(lines),line+radius)])

def classify(c:dict[str,Any])->dict[str,Any]:
 path=c['source_file']; expr=c['expression'].strip(); chain=' > '.join(c.get('property_chain',[])); ctx=line_context(path,c['line'])
 kind=c['source_kind']
 status='无需国际化'; reason=''; action=''; severity='低'; suggested_ko=None

 if len(expr)>500 or re.search(r'request:\s*\{|extractor:\s*function|\bSELECT\b|\bINSERT\b|fn\s+[A-Za-z_]', expr):
  reason='扫描器捕获到的是代码/脚本/配置片段而非可直接展示的自然语言；其内部可本地化短句需由所属功能单独处理，不能把整段代码翻译。'
  action='保留技术内容；若片段内存在用户可见说明，仅对其中的说明文字做资源化。'
 elif kind=='dynamic_i18n_key':
  status='待核实'; severity='中'
  reason=f'翻译键由运行时表达式“{expr}”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。'
  action='核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。'
 elif kind in CANDIDATE_EXCLUSIONS:
  rule=CANDIDATE_EXCLUSIONS[kind]
  status=rule.get('status','无需国际化'); severity=rule.get('severity','低')
  reason=rule.get('reason') or '该候选类别按产品决定不纳入国际化遗漏项。'
  action=None
 elif path.startswith('src/icons/'):
  reason='图标元数据中的中文是搜索别名，不直接渲染为界面文案；保留有助于中文品牌检索。'
 elif path.startswith('src/config/'):
  if path.endswith('universalProviderPresets.ts') and has_cjk(expr) and natural(expr):
   status='确认遗漏'; severity='中'; reason='通用供应商预设说明会直接展示给用户，但仍是硬编码中文。'; action='改为翻译键并在 zh/ko/en 资源中提供说明。'
   if 'NewAPI' in expr: suggested_ko='NewAPI는 Anthropic, OpenAI, Gemini 등 여러 프로토콜을 지원하는 자체 호스팅 가능한 API 게이트웨이입니다.'
   elif '自定义' in expr: suggested_ko='사용자 지정 구성의 API 게이트웨이'
  elif any(x in chain for x in ('activeClass','badgeClass','className','style','config')) or 'bg-' in expr or 'text-' in expr or 'border' in expr or 'grid ' in expr:
   reason='CSS 类名、样式或布局配置，不是用户文案。'
  elif path.endswith('presetSearchAliases.ts'):
   reason='供应商中文/拼音搜索别名，仅用于检索匹配，不作为界面文案展示。'
  elif 'models' in chain or chain in {'name','displayName'} or 'modelCatalog' in chain:
   reason='供应商或模型的品牌名、模型标识/展示名属于专有名词，当前产品策略保持原样。'
  elif technical_literal(expr) or any(tok in expr for tok in ('model_provider =','base_url =','wire_api =','You are ','User-Agent','@ai-sdk/','claude-cli/','codex_cli_rs/')):
   reason='预设中的配置片段、模型标识、User-Agent 或系统提示词，不属于界面自然语言。'
  elif has_cjk(expr) and natural(expr):
   status='确认遗漏'; severity='中'; reason='该预设字段可能展示给用户，但仍是硬编码中文。'; action='核实展示位置后迁入 i18n 资源。'
  else:
   reason='预设品牌/技术标识或内部配置值，不需要翻译。'
 elif path.endswith('components/sessions/reader/i18n.ts'):
  reason='这里是会话阅读器翻译键的简体中文 defaultValue；对应完整键已存在于四套前端资源，属于安全回退而非未国际化文案。'
 elif kind=='jsx_text':
  if expr in {'Auth:','TOML Config:'}:
   status='确认遗漏'; severity='中'; reason='对话框中的字段分组标题直接硬编码英文，切换韩语后仍显示英文。'; action='新增翻译键并在韩语资源中提供对应标签。'; suggested_ko={'Auth:':'인증:','TOML Config:':'TOML 설정:'}[expr]
  elif expr=='Reasoning Effort':
   status='确认遗漏'; severity='中'; reason='表单字段标签直接硬编码英文，未接入 i18n。'; action='使用字段标签翻译键。'; suggested_ko='추론 수준'
  elif expr=='API Key':
   status='确认遗漏'; severity='中'; reason='可见字段标签硬编码英文，现有韩语界面统一使用「API 키」。'; action='使用现有 API Key 标签翻译键。'; suggested_ko='API 키'
  elif expr in {'1 USD =','Linux / WSL','CC Switch','CC Switch v','Claude Code','OpenAI Codex','Gemini CLI','WSL:'}:
   reason='货币符号、平台名、产品名或品牌名，属于无需翻译的技术/专有名词。'
  else:
   status='待核实'; severity='低'; reason=f'JSX 文本“{expr}”是否需要本地化取决于运行时展示位置。'; action='结合组件布局确认后再决定是否抽取。'
 elif kind=='html_attribute':
  if has_cjk(expr) and natural(expr):
   status='确认遗漏'; severity='中'; reason='该可访问标签/占位符是面向用户的中文硬编码，切换语言后不会变化。'; action='改用 t() 资源键并补齐韩语。'
  elif expr=='Reasoning Effort':
   status='确认遗漏'; severity='中'; reason='字段标签硬编码英文。'; action='改用翻译键。'; suggested_ko='추론 수준'
  else:
   reason='URL、模型 ID、路径、示例值或纯技术属性，不承载自然语言。'
 elif path.startswith('src-tauri/'):
  near_localized='localized(' in ctx
  is_error_context=bool(re.search(r'return\s+Err|Err\(|map_err|bail!|anyhow!|ensure!|write!\(|write_str\(',ctx))
  is_log=bool(re.search(r'log::(?:trace|debug|info|warn|error)!|println!|eprintln!|dbg!',ctx))
  if near_localized:
   reason='该字面量属于 AppError::localized 的中英载荷或错误键，已由专门的后端 localized 候选统一审查。'
  elif path.endswith('src-tauri/src/error.rs') and has_cjk(expr):
   status='确认遗漏'; severity='高'; reason='AppError 的 Display 模板固定为中文，任何直接序列化给前端的错误都会在韩语界面显示中文。'; action='将错误显示模板改为语言感知渲染，或返回稳定错误键由前端本地化。'
  elif has_cjk(expr) and is_error_context:
   status='确认遗漏'; severity='高'; reason='该中文错误字符串位于返回错误的路径上，会经 Tauri 直接展示给前端用户，且没有韩语版本。'; action='改为稳定错误键并统一按语言渲染，或在 localized 载荷中补充韩语。'
  elif natural(expr) and is_error_context:
   status='待核实'; severity='中'; reason='该英文错误字符串位于后端返回路径，是否直接展示取决于调用方；目前没有韩语资源。'; action='追踪命令调用与前端展示链路，确认后改为结构化错误键。'
  elif is_log or re.search(r'log::',ctx):
   reason='日志/诊断文本，不作为用户界面文案。'
  elif natural(expr) and re.search(r'[A-Za-z]{3,}\s+[A-Za-z]{3,}',expr):
   status='待核实'; severity='中'; reason='该英文错误字符串不在日志宏中，但是否直接展示取决于后端调用方；当前无法仅凭局部代码排除用户可见性。'; action='追踪命令返回值及前端 toast/error boundary 展示链路，确认后使用结构化错误键。'
  elif has_cjk(expr):
   reason='该中文字符串未处于明确的用户错误返回路径，当前判断为日志、SQL、脚本、配置键或内部诊断值。'
  else:
   reason='协议字段、配置键、SQL、路径、命令或内部标识，不属于用户可见文案。'
 elif path.startswith('src/'):
  if path.endswith('src/components/UsageScriptModal.tsx') and ('t(' in expr or expr in {'sk-...','AKLT...'} or 'tier.name' in expr):
   reason='该字符串由已翻译片段与动态数据组合，或只是模型/API Key 示例占位符；不包含新的界面自然语言。'
  elif path.endswith('src/utils/providerConfigUtils.ts') and ('tomlBasicString' in expr or ' = ' in expr or re.search(r'\b(?:wire_api|name|base_url|model|experimental_bearer_token|model_provider) = ',expr) or r'\u${ch.charCodeAt' in expr):
   reason='该模板生成 TOML 配置语法或转义序列，不是用户界面文案。'
  elif path.endswith('src/lib/schemas/provider.ts') and expr == 'in JSON':
   reason='该片段用于拆分浏览器 JSON 解析错误消息，不直接展示给用户。'
  elif re.search(r'console\.|logger\.|call:console|call:log',chain,re.I) or re.search(r'logFrontend|console\.|logger\.',ctx):
   reason='控制台日志或诊断信息，不作为界面文案。'
  elif re.search(r'queryKey|data-testid|className|aria-hidden|activeClass|badgeClass',chain):
   reason='内部选择器、测试标识、CSS 类名或布局参数。'
  elif re.search(r'\|\|\s*["`]',ctx) and re.search(r'\bt\(',ctx):
   reason='该中文只是 t() 调用后的兜底字符串；当前所有对应翻译键均存在，正常韩语运行不会展示它。'
  elif path=='src/index.html' and has_cjk(expr):
   status='确认遗漏'; severity='中'; reason='HTML 文档标题硬编码中文，窗口首次加载或读取文档标题时不会随语言切换。'; action='在运行时根据 i18n 设置 document.title，并使用资源键。'
  elif path.endswith('src/utils/grokBuildConfig.ts') and natural(expr):
   status='确认遗漏'; severity='中'; reason='Grok Build 表单直接把该英文校验结果展示给用户，未经过 i18n。'; action='返回结构化错误码并在表单层本地化。'
  elif path.endswith('src/lib/requestOverrides.ts') and natural(expr):
   status='确认遗漏'; severity='中'; reason='请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。'; action='返回错误码并在展示层通过 t() 本地化。'
  elif path.endswith('src/components/UsageScriptModal.tsx') and natural(expr) and not technical_literal(expr):
   if re.search(r'\|\|\s*["`]',ctx) and 'toast.' in ctx:
    reason='该中文只是 toast 文案的兜底字符串；对应翻译键存在时不会展示。'
   else:
    status='确认遗漏'; severity='中'; reason='该用量脚本校验/调整提示直接硬编码中文并展示在 toast 中。'; action='迁入现有 usageScript 命名空间并补齐韩语。'
  elif path.endswith('src/lib/schemas/provider.ts') and natural(expr):
   status='确认遗漏'; severity='高'; reason='供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。'; action='错误码化并在表单层本地化。'
  elif path.endswith('src/utils/errorUtils.ts') and natural(expr):
   if ctx and ('includes(' in ctx or 'message' in ctx) and not re.search(r'throw new Error',ctx):
    reason='该文本用于匹配后端错误串或内部错误分类，不是直接展示文案。'
   else:
    status='确认遗漏'; severity='中'; reason='该工具函数生成的是用户可见错误消息或直接参与错误展示，但没有 i18n。'; action='改为错误码并在 UI 层使用翻译键。'
  elif path.endswith('src/utils/tomlUtils.ts') and natural(expr):
   status='确认遗漏'; severity='中'; reason='TOML/MCP 解析错误会反馈给用户，当前为硬编码中文。'; action='改为结构化错误码并通过 i18n 展示。'
  elif path.endswith('src/utils/providerConfigUtils.ts') and natural(expr):
   status='确认遗漏'; severity='中'; reason='供应商配置校验错误直接面向表单用户，未国际化。'; action='改为错误码/翻译键。'
  elif path.endswith('src/components/providers/forms/hooks/useCodexTomlValidation.ts') and natural(expr):
   status='确认遗漏'; severity='中'; reason='Codex TOML 校验错误显示在表单内，未接入 i18n。'; action='按错误类型映射到翻译键。'
  elif path.endswith('src/lib/query/mutations.ts') and natural(expr):
   status='待核实'; severity='中'; reason='该英文异常可能向上冒泡到通知层，但当前调用链没有本地化包装。'; action='追踪 toast/error boundary 展示路径并改为错误码。'
  elif path.endswith('src/lib/api/settings.ts') or path.endswith('src/lib/api/model-fetch.ts') or path.endswith('src/utils/uuid.ts'):
   if natural(expr): status='待核实'; severity='中'; reason='该英文错误可能经 API 调用方展示给用户，需结合实际 toast/error boundary 链路确认。'; action='核实展示链路；如需展示则改为结构化错误并本地化。'
  elif path.endswith('src/hooks/usePromptActions.ts') and natural(expr):
   status='确认遗漏'; severity='中'; reason='提示词操作异常会向上冒泡到用户通知，但消息固定为英文。'; action='使用错误码并在通知层翻译。'
  elif path.endswith('src/components/usage/providerLabel.ts'):
   status='确认遗漏'; severity='低'; reason='会话来源标签后缀固定为英文，会出现在用量筛选/表格的用户可见名称中。'; action='将后缀改为 i18n 片段。'
  elif path.endswith('src/contexts/UpdateContext.tsx'):
   reason='组件使用约束的开发期异常，不面向最终用户。'
  elif natural(expr) and has_cjk(expr):
   status='待核实'; severity='中'; reason=f'该中文自然语言“{expr}”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。'; action='检查组件引用和渲染路径；若用户可见则迁入 i18n。'
  elif natural(expr) and not technical_literal(expr):
   status='待核实'; severity='低'; reason=f'该英文字符串“{expr}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。'; action='追踪调用方并确认是否需要本地化。'
  else:
   reason='技术标识、命令、路径、协议值、配置片段或内部数据，不面向用户展示。'
 else:
  reason='非生产用户界面路径，或纯技术字面量。'

 if not reason:
  reason='已按实际代码上下文检查，该字面量不承担用户可见自然语言。'
 return {'status':status,'reason':reason,'suggested_action':action or None,'suggested_ko':suggested_ko,'severity':severity}

def main()->int:
 data=json.loads((OUT/'manifest/hardcoded_candidates.json').read_text(encoding='utf-8'))
 batches=json.loads((OUT/'manifest/hardcoded_batches.json').read_text(encoding='utf-8'))['batches']
 by_id={c['id']:c for c in data['candidates']}; counts={}; reviewed=0
 now=datetime.now(timezone.utc).isoformat()
 for batch in batches:
  records=[]
  for cid in batch['record_ids']:
   c=by_id[cid]; result=classify(c)
   status=result['status']; counts[status]=counts.get(status,0)+1
   record={'id':cid,'status':status,'content_fingerprint':c['content_fingerprint'],'reviewed_at':now,'reviewer':'primary','source_file':c['source_file'],'line':c['line'],'function':c['function'],'expression':c['expression'],'reason':result['reason'],'suggested_action':result['suggested_action'],'suggested_ko':result['suggested_ko'],'severity':result['severity'],'review_batch':batch['batch_id'],'round':1}
   records.append(record); c['status']=status; c['review']=record; reviewed+=1
  atomic(OUT/'reviews/hardcoded'/f'{safe(batch["batch_id"])}.json',{'schema_version':1,'batch_id':batch['batch_id'],'kind':'hardcoded','group':batch['group'],'reviewed_at':now,'review_count':len(records),'records':records})
 atomic(OUT/'manifest/hardcoded_candidates.json',data)
 print(json.dumps({'reviewed':reviewed,'status_counts':counts},ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
