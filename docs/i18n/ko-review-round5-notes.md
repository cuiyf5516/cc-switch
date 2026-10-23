# 第五轮韩语审查

日期：2026-10-24。输入：ko-review-requests-2026-10-23-3.json。

已审查全部 34 条备注，其中 28 条修改、6 条保留；加上同类术语同步，共修改 48 条界面译文。原生文案无须修改。

以中文原意及实际控件场景为主要依据。附件中的 note 是待评估的审校建议，不是全局指令；通用 URL、密码占位符及 Friendly partner 示例作为本轮局部本地化选择采纳，整体审校仍以中文语义为准。品牌名及指定功能名称保留英文，不把所有普通技术叙述改成英文。

## 参考依据

- [S1 Microsoft：Hyper-V 故障转移，明确使用 장애 조치(failover)](https://learn.microsoft.com/ko-kr/windows-server/virtualization/hyper-v/replication-failover)
- [S2 Microsoft：Windows 语音识别，包含 설정 마법사](https://support.microsoft.com/ko-kr/windows/windows-10%EC%97%90%EC%84%9C-%EC%9D%8C%EC%84%B1-%EC%9D%B8%EC%8B%9D-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-83ff75bd-63eb-0b6c-18d4-6fae94050571)
- [S3 Anthropic：Claude Code 高级使用技巧，使用 서브에이전트](https://support.claude.com/ko/articles/14554000-claude-code-%EA%B3%A0%EA%B8%89-%EC%82%AC%EC%9A%A9%EC%9E%90-%ED%8C%81)
- [S4 OpenClaw：官方韩文采用 하위 에이전트，说明另一写法也成立](https://docs.openclaw.ai/ko/tools/subagents)

拼接场景已核对 src/components/providers/EditProviderDialog.tsx：前句 + 空格 + 文件名 code 元素 + 后句；修正后示例为：사용 중인 공급자입니다. 저장하면 settings.json에 즉시 저장되며, 다음 요청부터 적용됩니다.

## 逐条结论

### provider.editCurrentNoticeFile

中文：这是正在使用的供应商。保存后会立即写进

原备注：사용 중인 공급자입니다. 저장하면

结论：修改。已检查 EditProviderDialog.tsx：前半句、文件名、后半句依次拼接。前半句停在 저장하면，避免助词出现在文件名前。

最终韩文：사용 중인 공급자입니다. 저장하면

### provider.editCurrentNoticeFileEnd

中文：，下一次请求生效。

原备注：에 즉시 기록되며, 다음 요청부터 적용됩니다.

结论：修改。助词 에 移至文件名后、没有前导空格，完整显示为“저장하면 settings.json에 즉시 저장되며, 다음 요청부터 적용됩니다.”。文件写入延续已确认的 저장 用词。

最终韩文：에 즉시 저장되며, 다음 요청부터 적용됩니다.

### confirm.failover.title

中文：启用故障转移功能

原备注：장애?

结论：保留。장애 在这里指系统／服务故障，장애 조치 是微软官方的 failover 用语，不是误用表示人的障碍。见来源 S1。

最终韩文：장애 조치 활성화

### confirm.failover.message

中文：故障转移是一项高级功能，启用前请确保您已了解其工作原理。

建议先在故障转移队列中配置好供应商优先级。

原备注：장애?

结论：保留。故障转移统一为 장애 조치；大意是请求失败时按优先级换用其他供应商，与此处功能一致。见 S1。

最终韩文：장애 조치는 고급 기능입니다. 활성화하기 전에 작동 방식을 이해했는지 확인하세요.

먼저 장애 조치 대기열에서 공급자 우선 순위를 설정하는 것이 좋습니다.

### settings.advanced.proxy.enableStackModeDescription

中文：开启后，Claude Code 和 Codex 的主页面开关换成聚合模式：像 OpenCode 一样添加多家供应商，它们的模型都会出现在客户端的模型列表里（Codex 需要重启后生效），不做故障转移。和本地路由开关二选一，切换时已开启的 Claude Code、Codex 会先退回直连

原备注：장애 ?

结论：保留正确的 장애 조치 术语；同时修正语义细节：Codex 重启后生效、只让已经开启相关模式的应用退回直连，避免把条件扩展为所有应用。

最终韩文：켜면 Claude Code와 Codex의 메인 페이지 스위치가 통합 모드로 바뀝니다. OpenCode처럼 여러 공급자를 추가하면 해당 공급자들의 모델이 클라이언트 모델 목록에 표시됩니다(Codex는 다시 시작한 후 적용). 장애 조치는 사용하지 않습니다. 이 옵션과 로컬 라우팅 스위치는 둘 중 하나만 선택할 수 있으며, 전환 시 활성화되어 있던 Claude Code와 Codex는 먼저 직접 연결로 돌아갑니다.

### settings.advanced.proxy.enableFailoverToggle

中文：在主页面显示故障转移开关

原备注：장애 ?

结论：장애 조치 本身保留；主页面统一为 메인 페이지、开关为 스위치，使这个选项读起来更一致。

最终韩文：메인 페이지에 장애 조치 스위치 표시

### settings.advanced.proxy.enableFailoverToggleDescription

中文：开启后，主页面顶部将独立显示故障转移开关

原备注：장애 ?

结论：同上一条保留 장애 조치，并统一主页面和开关的用词，保留“顶部单独显示”。

最终韩文：켜면 메인 페이지 상단에 장애 조치 스위치가 별도로 표시됩니다.

### settings.advanced.failover.title

中文：自动故障转移

原备注：장애 ?

结论：保留 자동 장애 조치。微软官方将自动 failover 写为 자동 장애 조치，此处表达准确。见 S1。

最终韩文：자동 장애 조치

### settings.advanced.failover.description

中文：配置故障转移队列和熔断策略

原备注：장애 ?

结论：保留。故障转移队列用 장애 조치 대기열，熔断策略用 서킷 브레이커 정책，两者是不同功能，未混为一谈。

最终韩文：장애 조치 대기열 및 서킷 브레이커 정책 설정

### settings.advanced.rectifier.thinkingSignatureDescription

中文：当 Anthropic 类型供应商返回 thinking 签名不兼容或非法请求等错误时，自动移除不兼容的 thinking 相关块并对同一供应商重试一次

原备注：추론 -> thinking

结论：采纳。这里指协议中的 thinking 块和签名，保留 thinking 更便于与协议字段对应；相关标题一起改为 Thinking 서명 보정。不会把一般“推理”概念的 추론 全部改英文。

最终韩文：Anthropic 유형 공급자가 thinking 서명 비호환 또는 잘못된 요청 등의 오류를 반환하면 호환되지 않는 thinking 관련 블록을 자동으로 제거한 뒤 같은 공급자로 한 번 다시 시도합니다.

### settings.advanced.rectifier.thinkingBudget

中文：Thinking Budget 整流

原备注：추론 예산 -> Thinking Budget

结论：采纳 Thinking Budget，整流按本项目既有用语保留 보정。同步同一功能区域的 Thinking 优化及 Adaptive Thinking / Extended Thinking 名称，协议字段仍保留原样。

最终韩文：Thinking Budget 보정

### settings.webdavSync.baseUrlPlaceholder

中文：https://dav.jianguoyun.com/dav/

原备注：用https://dav.example.com/dav/

结论：采纳通用示例 https://dav.example.com/dav/。这是占位示例的本地化选择，不改变默认服务或实际请求地址；坚果云的专用说明仍在预设帮助中保留。

最终韩文：https://dav.example.com/dav/

### settings.webdavSync.passwordPlaceholder

中文：应用密码（坚果云请使用「第三方应用密码」）

原备注：用 앱 비밀번호

结论：采纳简洁的 앱 비밀번호。此处是通用密码输入框，Jianguoyun 的第三方应用密码说明仍保留在该服务预设帮助里。

最终韩文：앱 비밀번호

### settings.webdavSync.presets.synology

中文：群晖 NAS

原备注：Synology NAS

结论：采纳 Synology NAS。品牌标识保留英文；相关韩语音译一起统一。

最终韩文：Synology NAS

### settings.s3Sync.presets.oss

中文：阿里云 OSS

原备注：Alibaba Cloud OSS

结论：采纳 Alibaba Cloud OSS，保留品牌及产品英文名称。

最终韩文：Alibaba Cloud OSS

### settings.s3Sync.presets.cos

中文：腾讯云 COS

原备注：Tencent Cloud COS

结论：采纳 Tencent Cloud COS；相同品牌的预设家族名同时更新为 Tencent Cloud。

最终韩文：Tencent Cloud COS

### settings.s3Sync.presets.obs

中文：华为云 OBS

原备注：Huawei OBS

结论：采纳 Huawei OBS，按产品英文名称显示。

最终韩文：Huawei OBS

### settings.codexStackClassicSubagents

中文：聚合模式下子 agent 用经典工具

原备注：하위 에이전트？서브 에이전트?

结论：하위 에이전트 和 서브에이전트 都有官方产品用例；选择 Anthropic 韩文资料采用的 서브에이전트（S3），并在全部相关条目统一。主代理仍用 주 에이전트。

最终韩文：통합 모드에서 기존 서브에이전트 도구 사용

### settings.appVisibility.geminiDesc

中文：Google Gemini CLI

原备注：Google Gemini CLI

结论：采纳 Google Gemini CLI，保留完整产品及品牌英文拼写。

最终韩文：Google Gemini CLI

### settings.envBadge.linux

中文：Linux

原备注：Linux

结论：采纳 Linux。系统徽标文字保留正式名称。

最终韩文：Linux

### settings.wslShell

中文：Shell

原备注：Shell

结论：采纳 Shell，作为该控件标签保留英文。普通说明中的“通过 shell 执行命令”仍可自然使用 셸，不机械将韩文说明全部英文化。

最终韩文：Shell

### providerForm.apiFormatGeminiNative

中文：Gemini Native generateContent (需开启路由)

原备注：Gemini Native generateContent 

结论：保留 Gemini Native generateContent 英文协议名称；同时保留中文“需开启路由”的限制，最终为 Gemini Native generateContent (라우팅 필요)。

最终韩文：Gemini Native generateContent (라우팅 필요)

### providerPreset.loginWith.claude

中文：用 Claude 账号登录

原备注：Claude

结论：采纳 Claude，统一品牌名：Claude 계정으로 로그인。

最终韩文：Claude 계정으로 로그인

### providerPreset.family.tencent

中文：腾讯云

原备注：Tencent Cloud

结论：采纳 Tencent Cloud，与 S3 服务名称一致。

最终韩文：Tencent Cloud

### providerPreset.plan.enterpriseLite

中文：企业 Lite

原备注：Enterprise Lite

结论：采纳 Enterprise Lite，作为套餐名称完整保留英文。

最终韩文：Enterprise Lite

### providerPreset.plan.enterprisePro

中文：企业 Pro

原备注：Enterprise Pro

结论：采纳 Enterprise Pro，作为套餐名称完整保留英文。

最终韩文：Enterprise Pro

### usage.sources.scanHelpTitle

中文：会话日志是什么

原备注：세션 로그란?

结论：采纳更简洁的 세션 로그란?；用于帮助提示标题，不损失“会话日志是什么”的含义。

最终韩文：세션 로그란?

### usage.sources.codexHelpTitle

中文：Codex 用量维护做什么

原备注：Codex 사용량 유지관리란?

结论：采纳 Codex 사용량 유지관리란?，作为功能说明标题简化问句，正文继续解释功能做什么。

最终韩文：Codex 사용량 유지관리란?

### usageScript.accessKeyId

中文：AccessKey ID

原备注：AccessKey ID

结论：采纳 AccessKey ID，保留接口凭据名称，避免与普通 API Key 混淆。

最终韩文：AccessKey ID

### mcp.form.useWizard

中文：配置向导

原备注：?

结论：保留 설정 마법사。마법사 是软件 Wizard 的既有韩文译法，用于引导用户选择步骤并生成配置，不是魔法功能。见 S2。

最终韩文：설정 마법사

### mcp.wizard.title

中文：MCP 配置向导

原备注：?

结论：保留 MCP 설정 마법사，与按钮及“配置”使用 설정 的统一约定一致。见 S2。

最终韩文：MCP 설정 마법사

### prompts.namePlaceholderHermes

中文：例如 中文搭档

原备注：这个条目参考英文做翻译

结论：采纳英文示例 Friendly partner，改为 예: 친절한 파트너。这里是可任意命名的示例，作为局部本地化选择，不改变中文优先的整体审校原则。

最终韩文：예: 친절한 파트너

### prompts.nameRequired

中文：填写名称，例如 团队编码规范

原备注：少了个 예

结论：修改，补回 예:，明确“团队编码规范”只是示例，不是要求用户必须填写的固定名称。

最终韩文：이름을 입력하세요. 예: 팀 코딩 규칙

### prompts.nameRequiredHermes

中文：填写名称，例如 中文搭档

原备注：该条目参考英文翻译

结论：采纳 Friendly partner 的本地化示例，改为 이름을 입력하세요. 예: 친절한 파트너，与同一输入框占位提示一致。

最终韩文：이름을 입력하세요. 예: 친절한 파트너

## 本轮全部修改

| 翻译键 | 修改前 | 修改后 |
|---|---|---|
| provider.editCurrentNoticeFile | 사용 중인 공급자입니다. 저장하면 다음 파일에 | 사용 중인 공급자입니다. 저장하면 |
| provider.editCurrentNoticeFileEnd |  즉시 기록되며, 다음 요청부터 적용됩니다. | 에 즉시 저장되며, 다음 요청부터 적용됩니다. |
| claudeDesktop.routeMapHint | Sonnet, Opus, Haiku 각 등급에서 실제로 요청할 모델을 입력하세요. DeepSeek나 Kimi 같은 모델은 메뉴 표시 이름도 지정하세요. 비워 둔 등급은 Sonnet 등급의 모델 또는 처음 입력한 등급의 모델을 이어받으므로 하위 에이전트가 호출하는 Haiku도 항상 사용할 수 있습니다. | Sonnet, Opus, Haiku 각 등급에서 실제로 요청할 모델을 입력하세요. DeepSeek나 Kimi 같은 모델은 메뉴 표시 이름도 지정하세요. 비워 둔 등급은 Sonnet 등급의 모델 또는 처음 입력한 등급의 모델을 이어받으므로 서브에이전트가 호출하는 Haiku도 항상 사용할 수 있습니다. |
| settings.advanced.proxy.enableStackModeDescription | 켜면 Claude Code와 Codex의 메인 페이지 스위치가 통합 모드로 바뀝니다. OpenCode처럼 여러 공급자를 추가하면 모든 모델이 클라이언트 모델 목록에 표시됩니다. Codex는 먼저 다시 시작해야 합니다. 장애 조치는 지원하지 않습니다. 이 옵션과 로컬 라우팅 옵션은 동시에 켤 수 없으며, 전환 시 Claude Code와 Codex를 먼저 직접 연결로 되돌립니다. | 켜면 Claude Code와 Codex의 메인 페이지 스위치가 통합 모드로 바뀝니다. OpenCode처럼 여러 공급자를 추가하면 해당 공급자들의 모델이 클라이언트 모델 목록에 표시됩니다(Codex는 다시 시작한 후 적용). 장애 조치는 사용하지 않습니다. 이 옵션과 로컬 라우팅 스위치는 둘 중 하나만 선택할 수 있으며, 전환 시 활성화되어 있던 Claude Code와 Codex는 먼저 직접 연결로 돌아갑니다. |
| settings.advanced.proxy.enableFailoverToggle | 기본 페이지에 장애 조치 토글 표시 | 메인 페이지에 장애 조치 스위치 표시 |
| settings.advanced.proxy.enableFailoverToggleDescription | 활성화되면 장애 조치 토글이 기본 페이지 상단에 독립적으로 나타납니다. | 켜면 메인 페이지 상단에 장애 조치 스위치가 별도로 표시됩니다. |
| settings.advanced.rectifier.thinkingSignature | 추론 서명 보정 | Thinking 서명 보정 |
| settings.advanced.rectifier.thinkingSignatureDescription | Anthropic 유형 공급자가 추론 서명 비호환 또는 잘못된 요청 오류를 반환하면 호환되지 않는 추론 관련 블록을 자동으로 제거한 후 같은 공급자로 한 번 다시 시도합니다. | Anthropic 유형 공급자가 thinking 서명 비호환 또는 잘못된 요청 등의 오류를 반환하면 호환되지 않는 thinking 관련 블록을 자동으로 제거한 뒤 같은 공급자로 한 번 다시 시도합니다. |
| settings.advanced.rectifier.thinkingBudget | 추론 예산 보정 | Thinking Budget 보정 |
| settings.advanced.optimizer.description | 요청 전송 전에 추론 및 캐시 설정을 자동으로 최적화합니다. Bedrock 공급자에만 적용됩니다. | 요청을 보내기 전에 Thinking 및 Cache 설정을 자동으로 최적화합니다(Bedrock 공급자에만 적용). |
| settings.advanced.optimizer.thinkingOptimizer | 추론 최적화 | Thinking 최적화 |
| settings.advanced.optimizer.thinkingOptimizerDescription | Opus/Sonnet에는 적응형 추론(Adaptive Thinking)을 자동으로 활성화하고 구형 모델에는 확장 추론(Extended Thinking)을 추가합니다. | Opus/Sonnet에는 Adaptive Thinking을 자동으로 활성화하고 이전 모델에는 Extended Thinking을 추가합니다. |
| settings.webdavSync.baseUrlPlaceholder | https://dav.jianguoyun.com/dav/ | https://dav.example.com/dav/ |
| settings.webdavSync.passwordPlaceholder | 앱 비밀번호(Jianguoyun에서는 ‘타사 앱 비밀번호’ 사용) | 앱 비밀번호 |
| settings.webdavSync.presets.synology | 시놀로지 NAS | Synology NAS |
| settings.s3Sync.presets.oss | 알리바바 클라우드 OSS | Alibaba Cloud OSS |
| settings.s3Sync.presets.cos | 텐센트 클라우드 COS | Tencent Cloud COS |
| settings.s3Sync.presets.obs | 화웨이 OBS | Huawei OBS |
| settings.codexStackClassicSubagents | 통합 모드에서 기존 하위 에이전트 도구 사용 | 통합 모드에서 기존 서브에이전트 도구 사용 |
| settings.codexStackClassicSubagentsDescription | 주 에이전트와 하위 에이전트가 서로 다른 공급자를 사용한다면 반드시 켜야 합니다. 그렇지 않으면 하위 에이전트가 작업을 받지 못합니다. | 주 에이전트와 서브에이전트가 서로 다른 공급자를 사용한다면 반드시 켜야 합니다. 그렇지 않으면 서브에이전트가 작업을 받지 못합니다. |
| settings.appVisibility.geminiDesc | 구글 Gemini CLI | Google Gemini CLI |
| settings.envBadge.linux | 리눅스 | Linux |
| settings.wslShell | 셸 | Shell |
| sessionManager.reader.event.subAgent | 하위 에이전트 {{name}} | 서브에이전트 {{name}} |
| sessionManager.reader.verb.agent | 하위 에이전트 | 서브에이전트 |
| providerForm.apiFormatGeminiNative | Gemini 네이티브 generateContent(라우팅 필요) | Gemini Native generateContent (라우팅 필요) |
| providerForm.modelRoleSubagent | 하위 에이전트 | 서브에이전트 |
| codexConfig.subagentModelLabel | 하위 에이전트 모델 | 서브에이전트 모델 |
| codexConfig.subagentReasoningEffortLabel | 하위 에이전트 추론 수준 | 서브에이전트 추론 수준 |
| codexConfig.subagentModelHint | Codex 하위 에이전트가 기본으로 사용할 모델과 추론 수준입니다. 비워 두면 주 에이전트의 설정을 따르며, 모델만 입력하면 해당 모델의 기본 추론 수준을 사용합니다. 통합 모드에서는 적용되지 않고 통합 탭 설정의 하위 에이전트 모델을 사용합니다. | Codex 서브에이전트가 기본으로 사용할 모델과 추론 수준입니다. 비워 두면 주 에이전트의 설정을 따르며, 모델만 입력하면 해당 모델의 기본 추론 수준을 사용합니다. 통합 모드에서는 적용되지 않고 통합 탭 설정의 서브에이전트 모델을 사용합니다. |
| providerPreset.loginWith.claude | 클로드 계정으로 로그인 | Claude 계정으로 로그인 |
| providerPreset.family.tencent | 텐센트 클라우드 | Tencent Cloud |
| providerPreset.plan.enterpriseLite | 엔터프라이즈 라이트 | Enterprise Lite |
| providerPreset.plan.enterprisePro | 엔터프라이즈 프로 | Enterprise Pro |
| usage.sources.scanHelpTitle | 세션 로그란 무엇입니까? | 세션 로그란? |
| usage.sources.codexHelpTitle | Codex 사용량 유지관리는 무엇을 하나요? | Codex 사용량 유지관리란? |
| usageScript.accessKeyId | 액세스키 ID | AccessKey ID |
| prompts.namePlaceholderHermes | 예: 중국어 파트너 | 예: 친절한 파트너 |
| prompts.nameRequired | 이름을 입력하세요. 팀 코딩 규칙 | 이름을 입력하세요. 예: 팀 코딩 규칙 |
| prompts.nameRequiredHermes | 이름을 입력하세요. 예: 중국어 파트너 | 이름을 입력하세요. 예: 친절한 파트너 |
| omo.subAgents | 하위 에이전트 | 서브에이전트 |
| mode.stackSettings.subagentDescription | 하위 에이전트는 기본으로 주 모델을 따릅니다. 통합된 모델을 선택하면 주 에이전트가 생성하는 하위 에이전트가 기본으로 해당 모델을 사용합니다. 단, 생성할 때 주 에이전트가 모델을 직접 지정한 경우는 제외합니다. Codex를 다시 시작할 필요 없이 새 대화부터 적용되며, 이미 열린 대화는 이전 설정을 유지합니다. | 서브에이전트는 기본으로 주 모델을 따릅니다. 통합된 모델을 선택하면 주 에이전트가 생성하는 서브에이전트가 기본으로 해당 모델을 사용합니다. 단, 생성할 때 주 에이전트가 모델을 직접 지정한 경우는 제외합니다. Codex를 다시 시작할 필요 없이 새 대화부터 적용되며, 이미 열린 대화는 이전 설정을 유지합니다. |
| mode.stackSettings.subagentModel | 하위 에이전트 모델 | 서브에이전트 모델 |
| mode.stackSettings.subagentEffort | 하위 에이전트 추론 수준 | 서브에이전트 추론 수준 |
| mode.stackSettings.unavailable | 선택한 모델이 통합 목록에서 제외되었습니다. 공급자가 제거되었거나 모델 제공을 중단했으므로 하위 에이전트는 일시적으로 주 모델을 따릅니다. 다시 추가하면 기존 설정이 복원됩니다. | 선택한 모델이 통합 목록에서 제외되었습니다. 공급자가 제거되었거나 모델 제공을 중단했으므로 서브에이전트는 일시적으로 주 모델을 따릅니다. 다시 추가하면 기존 설정이 복원됩니다. |
| mode.stackSettings.classicOff | 하위 에이전트와 주 에이전트의 공급자가 다릅니다. Codex의 새 하위 에이전트 도구는 주 에이전트의 공급자만 해독할 수 있게 작업을 암호화하므로 하위 에이전트가 작업을 받지 못합니다. 아래의 ‘통합 모드에서 기존 하위 에이전트 도구 사용’을 반드시 켜세요. | 서브에이전트와 주 에이전트의 공급자가 다릅니다. Codex의 새 서브에이전트 도구는 주 에이전트의 공급자만 해독할 수 있게 작업을 암호화하므로 서브에이전트가 작업을 받지 못합니다. 아래의 ‘통합 모드에서 기존 서브에이전트 도구 사용’을 반드시 켜세요. |
| mode.dialog.stackSubagentLead | 하위 에이전트는 기본으로 주 모델을 따릅니다. 통합된 모델을 따로 선택할 수도 있으며 나중에 통합 설정에서 언제든지 바꿀 수 있습니다. | 서브에이전트는 기본으로 주 모델을 따릅니다. 통합된 모델을 따로 선택할 수도 있으며 나중에 통합 설정에서 언제든지 바꿀 수 있습니다. |
| kimi.error.secondaryModelInUse | Kimi Code의 하위 에이전트가 이 공급자의 모델을 사용 중입니다. 먼저 Kimi Code에서 /secondary-model로 변경하세요. | Kimi Code의 서브에이전트가 이 공급자의 모델을 사용 중입니다. 먼저 Kimi Code에서 /secondary-model로 변경하세요. |

## 验证

16 项本地化测试、韩语 JSON 格式检查、git diff --check 通过。全部 4,363 条对照页／Markdown／审计与实际资源一致，第二至第五轮导入结果与当前译文一致；中文来源哈希、占位符及动态值 을(를) 风格保持正确。已校验文件名插入后的完整句子，并确认 Gemini Native 的路由限制仍在。未进行桌面布局验收或完整 Tauri 构建。
