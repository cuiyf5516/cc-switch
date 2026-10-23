# 配置／设置韩语术语检查

检查日期：2026-10-23。检查全部 4,292 条界面译文及 71 条原生译文，并对照英文确认语义。

在 260 条包含 구성 的界面译文中，将 253 条表示 configuration/config/configure 的用法统一为 설정。包括设置内容、设置文件、设置目录、导入／导出设置、模型设置和设置完成状态。구성 并非错误翻译，本次是按 CC Switch 的产品语境统一用词，不把两者机械区分为唯一正确或错误。

同时将 providerForm.configContent、codexConfig.authJsonHint 中的“配置内容”写为 설정 내용，使字段说明自然一致。中英文原文、代码标识和占位符保持原样。

保留以下 7 条中不同含义的词：

- `providerForm.partnerPromotion.alltokens_si`：AllTokens SI는 안정성과 정직성을 바탕으로 구축되었으며 기업용 AI 토큰 릴레이 및 팀 협업 플랫폼입니다. 구성원, 키, 사용량 및 잔액은 모두 하나의 회사 콘솔에 있으며 명확한 권한과 지출 한도를 통해 팀 사용량을 추적하고 제어할 수 있습니다.
- `usage.rebuildCodex.description`：로컬 rollout 로그에서 Codex 세션 사용량을 재구성합니다
- `usage.rebuildCodex.action`：Codex 사용량 재구성
- `usage.rebuildCodex.confirmTitle`：Codex 사용량을 재구성하시겠습니까?
- `usage.rebuildCodex.completed`：재구성 완료: {{imported}}개 가져옴, 오류 {{errors}}개, 중복 의심 {{suspected}}개, 보류 파일 {{deferred}}개
- `usage.rebuildCodex.failed`：Codex 사용량 재구성 실패: {{error}}
- `usage.rebuildCodex.actionEllipsis`：Codex 사용량 재구성

구성원 表示成员，재구성 表示重建，均不改为 설정。原生韩语文案中未发现需要调整的 구성。

已同步实际译文、HTML／Markdown 对照表、审计的 after／状态／计数，并保留原始 before 供比较。浏览器中已确认但译文变动的条目会按现有机制转回待复审。
