# 韩语翻译问题

- 审查资源总数：4448
- 已审核：4448
- 未审核：0
- 必改：3
- 建议改：79
- 待核实：4

> 只列出已实际审核并判定为必改、建议改或待核实的条目；可保留与未审核条目不在本报告展示。

## 必改（3）

### `json:src/i18n/locales#codexConfig.anthropicAuthFieldHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`codexConfig.anthropicAuthFieldHint`
- 中文：按网关读取 API Key 的请求头选择，两者只发其一。
- 现有韩文：게이트웨이가 API 키를 읽는 헤더를 선택합니다. 하나만 전송됩니다.
- 问题：原文是让用户根据网关读取 API Key 的请求头进行选择；韩文写成“网关选择请求头”，错误改变了动作主体。
- 建议韩文：게이트웨이가 API 키를 읽는 헤더에 맞춰 선택하세요. 둘 중 하나만 전송됩니다.
- 场景：Codex 认证字段选择提示

内容指纹：`8ba7003e365d2f8339ed6cbce9f68b92d4995feffb97f83c170aaa8a975ebde9`

### `json:src/i18n/locales#prompts.namePlaceholderHermes`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`prompts.namePlaceholderHermes`
- 中文：例如 中文搭档
- 现有韩文：예: 친절한 파트너
- 问题：示例“中文搭档”被译成「친절한 파트너」(friendly partner)，新增了“友好”含义且丢失“中文”语义。
- 建议韩文：예: 중국어 파트너
- 场景：Hermes 提示词名称占位符

内容指纹：`e9d537d48bfcb5e21c1924c026c7729b9d3d18b6832cd01a9a17076af11fb511`

### `json:src/i18n/locales#prompts.nameRequiredHermes`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`prompts.nameRequiredHermes`
- 中文：填写名称，例如 中文搭档
- 现有韩文：이름을 입력하세요. 예: 친절한 파트너
- 问题：示例“中文搭档”被译成「친절한 파트너」并加入“友好”含义，未忠实保留中文搭档语义。
- 建议韩文：이름을 입력하세요. 예: 중국어 파트너
- 场景：Hermes 提示词名称校验

内容指纹：`d07a5ba7d33222a37a65b20877a1b4d957d87a7aa5c6a91d29e7d99b346b7ea0`

## 建议改（79）

### `json:src/i18n/locales#codexConfig.promptCacheRoutingHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`codexConfig.promptCacheRoutingHint`
- 中文：自动：只对确认兼容的上游发送 prompt_cache_key。开启：用于其他兼容网关。关闭：避免严格网关因未知字段返回 400。
- 现有韩文：자동: 호환성이 확인된 업스트림에만 prompt_cache_key를 보냅니다. 켜짐: 다른 호환 게이트웨이에 사용할 수 있습니다. 꺼짐: 알 수 없는 필드를 거부하는 엄격한 게이트웨이의 400 오류를 방지합니다.
- 问题：同一控件选项分别使用「활성화됨/비활성화됨」，说明文字却用「켜짐/꺼짐」，控件内术语不一致。
- 建议韩文：자동: 호환성이 확인된 업스트림에만 prompt_cache_key를 보냅니다. 활성화: 다른 호환 게이트웨이에 사용할 수 있습니다. 비활성화: 알 수 없는 필드를 거부하는 엄격한 게이트웨이의 400 오류를 방지합니다.
- 场景：提示词缓存路由选项说明

内容指纹：`6ac1f566fc54a9f016a5b806fb670d64347f3454c1a59a7494b8e191d51b0086`

### `json:src/i18n/locales#codexConfig.subagentModelNotInCatalog`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`codexConfig.subagentModelNotInCatalog`
- 中文：该模型不在模型列表中：Codex 拿不到它的上下文窗口；经路由转成 Chat / Anthropic 协议时会被换成默认模型。
- 现有韩文：이 모델은 모델 목록에 없습니다. Codex는 컨텍스트 창을 가져올 수 없으며 라우팅이 요청을 Chat / Anthropic로 변환할 때 기본 모델로 대체됩니다.
- 问题：「Anthropic로」不符合韩语助词规则，且「Chat / Anthropic로」表达生硬。
- 建议韩文：이 모델은 모델 목록에 없습니다. Codex는 컨텍스트 창을 가져올 수 없으며 라우팅이 요청을 Chat 또는 Anthropic 프로토콜로 변환할 때 기본 모델로 대체됩니다.
- 场景：子代理模型配置警告

内容指纹：`5f4a983ddf42fd89582b57697d6f5f806e46eca15d7a43192285b93bae234cd0`

### `json:src/i18n/locales#codexOauth.loginExpired`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`codexOauth.loginExpired`
- 中文：登录已过期，请重试。
- 现有韩文：로그인 시간이 만료되었습니다. 다시 시도해 주세요.
- 问题：「로그인 시간이 만료되었습니다」表达不自然，登录本身或登录信息会过期，而不是“登录时间”过期。
- 建议韩文：로그인이 만료되었습니다. 다시 시도해 주세요.
- 场景：Codex 登录状态错误

内容指纹：`9759a5a55e65a06dde416f128287c699700697016f7b74bfc414cb83ddadb1c7`

### `json:src/i18n/locales#deeplink.skill.hint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`deeplink.skill.hint`
- 中文：此操作将添加 Skill 仓库到列表。
- 现有韩文：그러면 스킬 저장소가 목록에 추가됩니다.
- 问题：原文“此操作将…”在韩文中译为「그러면」缺少明确指代，单独作为确认提示时不够自然。
- 建议韩文：이 작업을 수행하면 스킬 저장소가 목록에 추가됩니다.
- 场景：添加 Skill 仓库确认提示

内容指纹：`18319e0ec0bd438d2b925308a052f7e9a09870d3ddbeb1db133d94a3c0c1928f`

### `json:src/i18n/locales#env.source.systemRegistry`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`env.source.systemRegistry`
- 中文：系统环境变量 (注册表)
- 现有韩文：시스템 환경변수(레지스트리)
- 问题：「환경변수」与同命名空间及其他界面的标准写法「환경 변수」不一致。
- 建议韩文：시스템 환경 변수(레지스트리)
- 场景：环境变量来源枚举

内容指纹：`84ac3731ab2df73aa828e66a41defc4acca8b4503a959399de4f3e276fb73dc4`

### `json:src/i18n/locales#env.source.userRegistry`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`env.source.userRegistry`
- 中文：用户环境变量 (注册表)
- 现有韩文：사용자 환경변수(레지스트리)
- 问题：「환경변수」与同命名空间及其他界面的标准写法「환경 변수」不一致。
- 建议韩文：사용자 환경 변수(레지스트리)
- 场景：环境变量来源枚举

内容指纹：`17722de23ae4a043995eafada14f266e6984e3e62b93da6a23490c62a1c7c836`

### `json:src/i18n/locales#mcode.empty.description`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcode.empty.description`
- 中文：MiniMax 官方账号登录由 MiniMax Code 自行管理，无需导入；config.yaml 里已有的自定义供应商会自动显示在这里。点击右上角 +，从预设或自定义配置添加供应商。
- 现有韩文：MiniMax 계정 로그인은 MiniMax Code 자체에서 관리되므로 가져올 것이 없습니다. 이미 config.yaml에 있는 사용자 지정 공급자가 여기에 자동으로 표시됩니다. 프리셋 또는 사용자 지정 공급자를 추가하려면 오른쪽 상단에 있는 + 버튼을 사용하세요.
- 问题：中文明确写的是“MiniMax 官方账号登录”，韩文遗漏了“공식”，弱化了账号类型。
- 建议韩文：MiniMax 공식 계정 로그인은 MiniMax Code 자체에서 관리되므로 가져올 필요가 없습니다. 이미 config.yaml에 있는 사용자 지정 공급자가 여기에 자동으로 표시됩니다. 프리셋 또는 사용자 지정 공급자를 추가하려면 오른쪽 상단의 + 버튼을 사용하세요.
- 场景：MiniMax Code 空状态说明

内容指纹：`d55b4e0b541a41314a98452704be3f130c8c05ce47e1532915df334f03cfe615`

### `json:src/i18n/locales#mcp.error.commandRequired`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.error.commandRequired`
- 中文：请填写命令
- 现有韩文：명령어를 입력해주세요
- 问题：「입력해주세요」未按韩语辅助动词规范分写，且与该区其他提示的终结句风格不一致。
- 建议韩文：명령어를 입력해 주세요.
- 场景：MCP 服务器命令校验

内容指纹：`55d0b28d8372ded70ddc51e23126be76df775fea51edd7705836d94ff5d2dc81`

### `json:src/i18n/locales#mcp.error.idExists`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.error.idExists`
- 中文：该标识已存在，请更换
- 现有韩文：식별자가 이미 존재합니다. 다른 것을 선택하세요.
- 问题：原文要求“更换”标识，韩文「다른 것을 선택하세요」表示选择一个东西，可能被误解为选择现有项。
- 建议韩文：식별자가 이미 존재합니다. 다른 식별자를 사용하세요.
- 场景：MCP 服务器标识重复错误

内容指纹：`6c63848fd6bc3cc4fbc170ca2188f2395c84cd59bacfde1d1fa06692d376a63c`

### `json:src/i18n/locales#mcp.form.descriptionPlaceholder`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.form.descriptionPlaceholder`
- 中文：可选的描述信息
- 现有韩文：선택적 설명
- 问题：「선택적 설명」偏直译，作为输入框占位符不如「설명(선택 사항)」自然明确。
- 建议韩文：설명(선택 사항)
- 场景：MCP 描述输入框占位符

内容指纹：`1780ed15e4dabcd7bdea8093240bc5dd2cb31c33c52ac2b795f42922823806cf`

### `json:src/i18n/locales#mcp.presets.fetch.description`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.presets.fetch.description`
- 中文：通用 HTTP 请求工具，支持 GET/POST 等 HTTP 方法，适合快速请求接口/抓取网页数据
- 现有韩文：범용 HTTP 요청 도구는 GET/POST 및 기타 HTTP 방법을 지원하며 빠른 API 요청 및 웹 데이터 스크래핑에 적합합니다.
- 问题：「HTTP 방법」是直译，韩语软件术语通常使用「HTTP 메서드」。
- 建议韩文：GET/POST 등 HTTP 메서드를 지원하는 범용 HTTP 요청 도구로, API를 빠르게 호출하거나 웹 데이터를 가져오는 데 적합합니다.
- 场景：MCP fetch 预设说明

内容指纹：`6471e9030b9ce980af1982188c3825a333254f49b8b506db465ff6fa24c3be9b`

### `json:src/i18n/locales#mcp.presets.sequential-thinking.description`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.presets.sequential-thinking.description`
- 中文：顺序思考工具，帮助 AI 将复杂问题分解为多个步骤，逐步深入思考
- 现有韩文：AI가 더 깊은 사고를 위해 복잡한 문제를 여러 단계로 분류하는 데 도움이 되는 순차적 사고 도구
- 问题：原文是把复杂问题“分解为多个步骤”，韩文「분류」表示分类，改变了动作含义。
- 建议韩文：AI가 복잡한 문제를 여러 단계로 나누어 차례로 깊이 생각하도록 돕는 순차적 사고 도구
- 场景：MCP sequential-thinking 预设说明

内容指纹：`1712a9f31ef4e514f61a90ff1a19a292c8a273c6995d5c6f33807959bd8a1622`

### `json:src/i18n/locales#mcp.serverList`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.serverList`
- 中文：服务器列表
- 现有韩文：서버
- 问题：原文为“服务器列表”，韩文只写「서버」，遗漏列表语义并弱化区块标题。
- 建议韩文：서버 목록
- 场景：MCP 服务器列表标题

内容指纹：`af475f4cadc07a633ac2ddc0ee71b9715aadd2ab5500122682b8fdf4eb698ba2`

### `json:src/i18n/locales#mcp.unifiedPanel.noSearchResults`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.unifiedPanel.noSearchResults`
- 中文：未找到匹配的 MCP 服务器
- 现有韩文：검색과 일치하는 MCP 서버가 없습니다.
- 问题：「검색과 일치하는」搭配不自然，寻找结果时应对应「검색어와 일치하는」。
- 建议韩文：검색어와 일치하는 MCP 서버가 없습니다.
- 场景：MCP 搜索空状态

内容指纹：`3135c54dde04d8e99df20bf9bd42c822e01534f6504ed623335fed6df4e1149f`

### `json:src/i18n/locales#mcp.userLevelPath`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.userLevelPath`
- 中文：用户级 MCP 配置路径
- 现有韩文：사용자 수준 MCP 경로
- 问题：原文是“用户级 MCP 配置路径”，韩文遗漏「설정」，字段含义不完整。
- 建议韩文：사용자 수준 MCP 설정 경로
- 场景：MCP 配置路径标签

内容指纹：`e7f99080719e7112fe5fe903fffeea339d430d3178b3da30a6b13ac1a83318d0`

### `json:src/i18n/locales#mcp.wizard.headers`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcp.wizard.headers`
- 中文：请求头（可选）
- 现有韩文：헤더(선택사항)
- 问题：「선택사항」未按项目统一写法「선택 사항」分写。
- 建议韩文：헤더(선택 사항)
- 场景：MCP 向导请求头字段

内容指纹：`4e8c7538cc46c33944184ecbec9fd3c1ecc781cf918954cf1dd325e8930a7cfc`

### `json:src/i18n/locales#mcpPage.drawer.cwdPlaceholder`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcpPage.drawer.cwdPlaceholder`
- 中文：留空时由应用决定
- 现有韩文：앱이 결정하도록 하려면 비워두세요.
- 问题：「비워두세요」应按韩语辅助动词规范分写为「비워 두세요」。
- 建议韩文：앱이 결정하도록 하려면 비워 두세요.
- 场景：MCP 工作目录输入框占位符

内容指纹：`83faa3cb8f2074cbf83a2bc96c10c57520796faec86adad15528918bb7714759`

### `json:src/i18n/locales#mcpPage.drawer.jsonHelpTitle`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcpPage.drawer.jsonHelpTitle`
- 中文：JSON 和表单的关系
- 现有韩文：JSON과 양식
- 问题：原文是“JSON 和表单的关系”，韩文只写「JSON과 양식」，遗漏关系/说明语义。
- 建议韩文：JSON과 양식의 관계
- 场景：MCP JSON/表单帮助标题

内容指纹：`1d5fa163a65d367b441fdd13495a1a03b786125dc8bad6dcaca55f632d96bb6e`

### `json:src/i18n/locales#mcpPage.drawer.revealValue`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcpPage.drawer.revealValue`
- 中文：显示 {{name}} 的值
- 现有韩文：{{name}}의 값을 표시합니다.
- 问题：该资源用于按钮 aria-label；原文是操作命令，韩文的「표시합니다」是陈述句，不利于辅助技术准确播报按钮动作。
- 建议韩文：{{name}} 값 표시
- 场景：MCP 值显示按钮 aria-label

内容指纹：`4650e9be615e4ac0ecddeb4df1264bbe74d85d64b5a5ef58fdd199c75ffcac5b`

### `json:src/i18n/locales#mcpPage.listLabel`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`mcpPage.listLabel`
- 中文：MCP 列表
- 现有韩文：MCP 서버
- 问题：该资源是 MCP 列表的无障碍标签，韩文只写「MCP 서버」，遗漏「목록」，不能准确描述控件。
- 建议韩文：MCP 서버 목록
- 场景：MCP 列表 aria-label

内容指纹：`2acbefe0b270e3cbb4bd999b85a41fbedbfb3ce392c5d2a097687d9f1855dacc`

### `json:src/i18n/locales#omo.advancedJsonHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`omo.advancedJsonHint`
- 中文：temperature, top_p, budgetTokens, prompt_append, permission 等，留空使用默认值
- 现有韩文：temperature, top_p, budgetTokens, prompt_append, permission 등. 기본값을 사용하려면 비워 두세요
- 问题：当前韩文以「permission 등.」直接接下一句，列表后的标点和句子衔接不自然。
- 建议韩文：temperature, top_p, budgetTokens, prompt_append, permission 등의 값을 설정합니다. 기본값을 사용하려면 비워 두세요.
- 场景：OMO 高级参数说明

内容指纹：`fac382d348a1d0f0f8eeae688260f96b8abbf55a05a3e8969a6af00b825a5ef8`

### `json:src/i18n/locales#omo.agentTooltip.atlas`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`omo.agentTooltip.atlas`
- 中文：主编排器（持有 TODO 列表），负责执行阶段的任务分发与协调，不直接完成所有工作而是委派给专业代理。
- 现有韩文：실행 단계에서 작업 분배 및 조정을 담당하는 메인 오케스트레이터(TODO 목록 보유)입니다. 모든 업무를 직접 완료하기 보다는 전문 에이전트에게 위임합니다.
- 问题：「완료하기 보다는」未按韩语规范连写为「완료하기보다는」。
- 建议韩文：실행 단계에서 작업 분배 및 조정을 담당하는 메인 오케스트레이터(TODO 목록 보유)입니다. 모든 업무를 직접 완료하기보다는 전문 에이전트에게 위임합니다.
- 场景：OMO Atlas 代理说明

内容指纹：`118518f66a47f721a31918ed96b0a87201fc48077f460a45a4794a5772fbf46c`

### `json:src/i18n/locales#omo.enabledModelsCount`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`omo.enabledModelsCount`
- 中文：可选已配置模型 {{count}} 个
- 现有韩文：선택 가능한 설정 모델 {{count}}개
- 问题：「선택 가능한 설정 모델」修饰关系生硬，容易被理解为“可设置的模型”。
- 建议韩文：선택 가능한 구성 모델 {{count}}개
- 场景：OMO 模型数量提示

内容指纹：`e2fe7f628c40c87545c13b05c5769e3b78d62813cd27eb9324b41ae542668047`

### `json:src/i18n/locales#omo.imported`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`omo.imported`
- 中文：已导入为 "{{name}}"
- 现有韩文："{{name}}"로 가져옴
- 问题：变量后的「로」是否成立取决于名称末音节，显示时可能产生错误助词；使用「항목으로」可稳定规避。
- 建议韩文："{{name}}" 항목으로 가져옴
- 场景：OMO 导入成功提示

内容指纹：`e574d8be544e7ab3d42cef1c0a18277876af4af0241be1ba6b7742383e0bda2f`

### `json:src/i18n/locales#openclaw.agents.fallbackModelsHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`openclaw.agents.fallbackModelsHint`
- 中文：当主模型不可用时，按优先级依次尝试以下回退模型
- 现有韩文：기본 모델을 사용할 수 없는 경우 순서대로 대체가 시도됩니다.
- 问题：「대체가 시도됩니다」中的「대체」指代不清；原文是逐个尝试回退模型。
- 建议韩文：기본 모델을 사용할 수 없는 경우 대체 모델을 우선순위 순서대로 시도합니다.
- 场景：OpenClaw 回退模型说明

内容指纹：`4267dcb14208a7af4fa308dfb8af3d0464cfdb304ca0b54c5f878542f7bb221e`

### `json:src/i18n/locales#openclaw.health.stringifiedEnvVars`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`openclaw.health.stringifiedEnvVars`
- 中文：env.vars 应为对象，但当前值看起来像被字符串化或已损坏。
- 现有韩文：env.vars는 객체여야 하지만 현재 값이 문자열이거나 잘못된 형식으로 보입니다.
- 问题：「문자열이거나」只表示“是字符串”，遗漏了原文“被字符串化/序列化”的诊断含义。
- 建议韩文：env.vars는 객체여야 하지만 현재 값이 문자열로 직렬화되었거나 손상된 것으로 보입니다.
- 场景：OpenClaw 环境变量健康检查

内容指纹：`8766600599dc026918022982cdf289e9074007ed7d8a6973d0762888ce4085d2`

### `json:src/i18n/locales#openclaw.health.stringifiedShellEnv`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`openclaw.health.stringifiedShellEnv`
- 中文：env.shellEnv 应为对象，但当前值看起来像被字符串化或已损坏。
- 现有韩文：env.shellEnv는 객체여야 하지만 현재 값이 문자열이거나 잘못된 형식으로 보입니다.
- 问题：「문자열이거나」只表示“是字符串”，遗漏了原文“被字符串化/序列化”的诊断含义。
- 建议韩文：env.shellEnv는 객체여야 하지만 현재 값이 문자열로 직렬화되었거나 손상된 것으로 보입니다.
- 场景：OpenClaw shellEnv 健康检查

内容指纹：`95aa2a5b0c20abc2838901c667432d6cf0ac2ed1616069c5a1f12e04e310568b`

### `json:src/i18n/locales#openclaw.providerKeyDuplicate`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`openclaw.providerKeyDuplicate`
- 中文：此标识已被使用，请更换
- 现有韩文：이 키는 이미 사용 중입니다.
- 问题：原文要求“请更换”，韩文只陈述该键已在使用，缺少可执行动作。
- 建议韩文：이 키는 이미 사용 중입니다. 다른 키를 사용하세요.
- 场景：OpenClaw 供应商标识重复错误

内容指纹：`30251f856893e97a731ba1768414b37a596ddd781212b139ecafc7f26159a7c9`

### `json:src/i18n/locales#openclawConfig.defaultModel.primary`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`openclawConfig.defaultModel.primary`
- 中文：主模型
- 现有韩文：기본 모델
- 问题：原文是「主模型」，但韩文「기본 모델」与同组「默认模型」完全同义，导致主/默认概念混淆；项目其他位置使用「주 모델」表示 primary。
- 建议韩文：주 모델
- 场景：OpenClaw 默认模型字段

内容指纹：`49316649abe47f66cf73664394056168f1d3522a44f1c91a6b0e65fdc13f792f`

### `json:src/i18n/locales#opencode.baseUrl`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`opencode.baseUrl`
- 中文：Base URL
- 现有韩文：기본 URL
- 问题：「Base URL」是通用的技术标识，韩文「기본 URL」也可能被理解为“默认 URL”；保留原术语或使用「베이스 URL」更不易产生歧义。
- 建议韩文：Base URL
- 场景：OpenCode 供应商 API 地址字段

内容指纹：`9ab7a03f831e8bfdda2d0684ed5bee7dd6b8fde22c6cb8e8bfdae291ef09f348`

### `json:src/i18n/locales#opencode.providerKeyDuplicate`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`opencode.providerKeyDuplicate`
- 中文：此标识已被使用，请更换
- 现有韩文：이 키는 이미 사용 중입니다.
- 问题：原文明确要求更换标识，韩文只陈述已被占用，没有给出动作。
- 建议韩文：이 키는 이미 사용 중입니다. 다른 키를 사용하세요.
- 场景：OpenCode 供应商标识重复错误

内容指纹：`30251f856893e97a731ba1768414b37a596ddd781212b139ecafc7f26159a7c9`

### `json:src/i18n/locales#profiles.createDescription.claude-desktop`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`profiles.createDescription.claude-desktop`
- 中文：把 Claude Desktop 当前的供应商保存为一个项目，之后可一键切换。
- 现有韩文：현재 Claude Desktop 공급자를 나중에 전환할 수 있는 프로젝트로 저장하세요.
- 问题：同组其他两个 Claude/Codex 说明均用陈述句式，此处突然改为命令式「저장하세요」，弹窗内语气不一致。
- 建议韩文：현재 Claude Desktop 공급자를 나중에 전환할 수 있는 프로젝트로 저장합니다.
- 场景：新建项目说明

内容指纹：`302e8b7c7303687c17fa97b944838bef5ceb947d7871ed639813bd27d38ab9a6`

### `json:src/i18n/locales#prompts.deleteBlocked`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`prompts.deleteBlocked`
- 中文：启用中的不能删除，先停用
- 现有韩文：삭제하기 전에 비활성화하세요.
- 问题：原文先说明“启用中的不能删除”，韩文只留下“先停用”，遗漏了不可删除的前提原因。
- 建议韩文：활성화된 항목은 삭제할 수 없습니다. 먼저 비활성화하세요.
- 场景：提示词删除限制提示

内容指纹：`58f6109b199994432e48dd9e85b0b7a0073232f95793a66270ad8ed5f501714d`

### `json:src/i18n/locales#prompts.helpHermesTitle`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`prompts.helpHermesTitle`
- 中文：SOUL.md 怎么生效
- 现有韩文：SOUL.md의 효과
- 问题：原文问 SOUL.md“怎么生效”，韩文「효과」表示效果，没有表达生效机制。
- 建议韩文：SOUL.md 적용 방식
- 场景：Hermes 提示词帮助标题

内容指纹：`2d5cc3a6a39130ccce20e987fa0da070afac417a555bc27555e1639cbc521619`

### `json:src/i18n/locales#prompts.helpPiText`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`prompts.helpPiText`
- 中文：提示库同时只启用一条，它就是 AGENTS.md 的内容。系统提示文件存在就生效，模板在 Pi 里输入 /命令名 调用，这两类都不用启用。
- 现有韩文：프롬프트 라이브러리에서는 한 번에 하나만 활성화되며, 그 내용이 AGENTS.md에 저장됩니다. 시스템 프롬프트 파일은 존재하면 적용되고 템플릿은 Pi에서 /명령어이름을 입력하여 호출합니다. 이 두 유형은 별도로 활성화할 필요가 없습니다.
- 问题：「/명령어이름을」把说明词直接拼成命令形式，读起来不自然；应清楚说明在斜杠后输入命令名。
- 建议韩文：프롬프트 라이브러리에서는 한 번에 하나만 활성화되며, 그 내용이 AGENTS.md에 저장됩니다. 시스템 프롬프트 파일은 존재하면 적용되고, 템플릿은 Pi에서 슬래시와 명령 이름을 입력해 호출합니다. 이 두 유형은 별도로 활성화할 필요가 없습니다.
- 场景：Pi 提示词生效说明

内容指纹：`6d214f35ee26f2712a8bc0ebfb2535f739255d1e8dc48c1149bad361f3f41248`

### `json:src/i18n/locales#prompts.updatedToday`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`prompts.updatedToday`
- 中文：今天 {{time}} 更新
- 现有韩文：오늘 업데이트됨 {{time}}
- 问题：韩文语序不自然，「오늘 업데이트됨 {{time}}」应把时间放在更新时间之前。
- 建议韩文：오늘 {{time}}에 업데이트됨
- 场景：提示词更新时间

内容指纹：`8c19beb686dc10bd3409d273f65d0b7eea53796b80fbcc38bec4307653a564a0`

### `json:src/i18n/locales#provider.officialModelsReason.loginStale`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`provider.officialModelsReason.loginStale`
- 中文：官方列表：Codex 的登录超过 8 天没有刷新，打开 Codex 用一下即可自动刷新
- 现有韩文：공식 목록: Codex 로그인이 8일 이상 새로 고쳐지지 않았습니다. Codex를 한 번 사용하면 자동으로 새로 고쳐집니다.
- 问题：「로그인이 새로 고쳐지지 않았습니다」搭配不自然，登录信息应使用「갱신되다」。
- 建议韩文：공식 목록: Codex 로그인이 8일 이상 갱신되지 않았습니다. Codex를 한 번 사용하면 자동으로 갱신됩니다.
- 场景：Codex 官方模型列表状态提示

内容指纹：`a316c94f24afa8b0329cf01ca79a8eb6b4233097c9d0907712262a01640233a3`

### `json:src/i18n/locales#provider.stackBadgeNoModels`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`provider.stackBadgeNoModels`
- 中文：这家没有配置模型，不会出现在模型选择器里
- 现有韩文：이 공급자에는 설정된 모델이 없어 해당 모델이 모델 선택 메뉴에 표시되지 않습니다.
- 问题：「해당 모델이」指代不存在的模型，句子前后矛盾；应直接说明该供应商不会出现在模型选择器。
- 建议韩文：이 공급자에는 설정된 모델이 없어 모델 선택 메뉴에 표시되지 않습니다.
- 场景：聚合供应商徽标提示

内容指纹：`e8ee38bab02383a8cfbde2c0f8690f91a460e2f84668cdd0ebce24a9d5c34882`

### `json:src/i18n/locales#providerForm.anthropicModel`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`providerForm.anthropicModel`
- 中文：主模型
- 现有韩文：주요 모델
- 问题：同项目其他位置用「주 모델」表示 primary model，「주요 모델」会与普通“主要模型”混淆。
- 建议韩文：주 모델
- 场景：Anthropic 主模型字段

内容指纹：`82fdd657cfa5aa1cb056163e35d850bdc6b9807df0c4ea34a3d2c33640fff89f`

### `json:src/i18n/locales#providerForm.mainModel`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`providerForm.mainModel`
- 中文：主模型 (可选)
- 现有韩文：주요 모델(선택 사항)
- 问题：「主模型」在项目其他位置统一为「주 모델」；「주요 모델」语义偏离 primary model。
- 建议韩文：주 모델(선택 사항)
- 场景：供应商主模型字段

内容指纹：`a7c773ee8501ec3a7a4ba13033d76d6ad06cb2a5fa1a80aa8d90a83796fe5ba2`

### `json:src/i18n/locales#providerForm.modelHelper`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`providerForm.modelHelper`
- 中文：可选：指定默认使用的 Claude 模型，留空则使用系统默认。
- 现有韩文：선택사항: 사용할 기본 Claude 모델을 지정하고, 시스템 기본값을 사용하려면 비워 두세요.
- 问题：「선택사항」未按项目统一写法「선택 사항」分写。
- 建议韩文：선택 사항: 사용할 기본 Claude 모델을 지정하고, 시스템 기본값을 사용하려면 비워 두세요.
- 场景：模型选择说明

内容指纹：`488288f55752dbce88496d689a7c26adf968756516d43e3a7d09f1901e3e8f63`

### `json:src/i18n/locales#providerForm.websiteUrlPlaceholder`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`providerForm.websiteUrlPlaceholder`
- 中文：https://example.com（可选）
- 现有韩文：https://example.com(옵션)
- 问题：同一项目统一使用「선택 사항」，此处「옵션」造成术语和样式不一致。
- 建议韩文：https://example.com(선택 사항)
- 场景：官网 URL 输入框占位符

内容指纹：`55dc121cd9c3498854e5898880c7f5592f84f278eaf2b2aded890e374c8b94e1`

### `json:src/i18n/locales#proxy.panel.stats.totalRequests`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`proxy.panel.stats.totalRequests`
- 中文：总请求数
- 现有韩文：총 요청
- 问题：原文是“总请求数”，韩文「총 요청」遗漏数量含义。
- 建议韩文：총 요청 수
- 场景：路由服务统计

内容指纹：`29f6d236ead697604a80fd1e47bb6440ba086358455c7c5df1897a220d43bd61`

### `json:src/i18n/locales#proxy.settings.fields.nonStreamingTimeout.description`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`proxy.settings.fields.nonStreamingTimeout.description`
- 中文：非流式请求的总超时时间
- 现有韩文：스트리밍되지 않는 요청의 총 시간 초과
- 问题：「총 시간 초과」搭配不自然，时间限制应为「총 제한 시간」，与同页其他超时说明一致。
- 建议韩文：스트리밍되지 않는 요청의 총 제한 시간
- 场景：非流式超时说明

内容指纹：`4309b90568a02674d07d50b6e01648644dad2a23d8dae9580026897c1538987f`

### `json:src/i18n/locales#proxy.takeover.tooltip.inactive`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`proxy.takeover.tooltip.inactive`
- 中文：路由 {{appLabel}} 的请求，让该应用请求走本地路由
- 现有韩文：로컬 라우팅을 통해 {{appLabel}}의 요청 라우팅
- 问题：韩文只有名词短语，缺少“让请求走本地路由”的动作，作为 tooltip 不完整。
- 建议韩文：{{appLabel}}의 요청을 로컬 라우팅으로 전달합니다.
- 场景：本地路由接管状态提示

内容指纹：`8d38db8dbfded17703e7806fe3da214d7a61750a3f5070928d8e5688d202dc14`

### `json:src/i18n/locales#proxyConfig.circuitBreaker`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`proxyConfig.circuitBreaker`
- 中文：熔断器配置
- 现有韩文：서킷 브레이커
- 问题：原文为“熔断器配置”，韩文遗漏「설정」，且与相邻键「서킷 브레이커 설정」不一致。
- 建议韩文：서킷 브레이커 설정
- 场景：路由熔断器配置标题

内容指纹：`f0906ed4f9335d3e5ff5036b298c0ed7cf82a6c2d1adf4f7ee5da229a4089d6c`

### `json:src/i18n/locales#proxyConfig.minRequests`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`proxyConfig.minRequests`
- 中文：最小请求数
- 现有韩文：최소 요청
- 问题：原文是“最小请求数”，韩文「최소 요청」遗漏数量含义。
- 建议韩文：최소 요청 수
- 场景：路由熔断器字段

内容指纹：`7bac87e9e380db81b1b15a1cc585dd3622e003f0d9a2993cc3df1468ab5383b7`

### `json:src/i18n/locales#quota.resetCredits.label`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`quota.resetCredits.label`
- 中文：重置
- 现有韩文：재설정
- 问题：同一组 resetCredits 文案其余条目统一使用「초기화」，此处却使用「재설정」，在重置次数弹层中造成术语不一致。
- 建议韩文：초기화
- 场景：额度重置次数标签

内容指纹：`0acb327b9611098293595aa5a1346055845560cc6d780e60e350a008bf4b6aab`

### `json:src/i18n/locales#quota.resetCredits.title`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`quota.resetCredits.title`
- 中文：存下的限额重置
- 现有韩文：저장된 한도 재설정
- 问题：「재설정」与该组其他文案的「초기화」不一致，且「저장된 한도 초기화」更准确表达“存下的限额重置”。
- 建议韩文：저장된 한도 초기화
- 场景：额度重置次数弹层标题

内容指纹：`b6cd1d8cb34e1cc37c5333133c5997cf5bd39b4db9b3ed21cffa0e1af2481f0b`

### `json:src/i18n/locales#routingSettings.totalRequests`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`routingSettings.totalRequests`
- 中文：总请求数
- 现有韩文：요청 수
- 问题：原文是“总请求数”，韩文「요청 수」遗漏“总计”，与同项目其他统计标签不一致。
- 建议韩文：총 요청 수
- 场景：路由服务统计

内容指纹：`cd3602c6c5f5463bf4a8dc8efd5b259ac51e39f04f201f956f4b0e1ac6cb2eab`

### `json:src/i18n/locales#sessionManager.reader.status.success`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`sessionManager.reader.status.success`
- 中文：成功
- 现有韩文：성공함
- 问题：同组状态均为简短名词「실패/중단됨/실행 중」，「성공함」是动词化完成形，与其他状态徽标风格不一致。
- 建议韩文：성공
- 场景：会话步骤状态徽标

内容指纹：`07af5dd8dec87d16ba047d98a1fd0f1728f9b75312e06aabe8b1cbd4ca150747`

### `json:src/i18n/locales#sessionManager.selectSessionLabel`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`sessionManager.selectSessionLabel`
- 中文：选择 {{title}}
- 现有韩文：{{title}}을(를) 선택하세요
- 问题：该资源用于选择控件的无障碍标签，韩文使用带句号的命令句；标签应简洁描述动作对象。
- 建议韩文：{{title}} 선택
- 场景：会话选择控件 aria-label

内容指纹：`e4e3b33af0a6ab68cc6ff886ae26c0608ce8ca9f7e8475ed8927bdf842548c7c`

### `json:src/i18n/locales#sessionManager.sessionList`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`sessionManager.sessionList`
- 中文：会话列表
- 现有韩文：세션
- 问题：原文是“会话列表”，韩文只有「세션」，遗漏列表语义，作为标题/标签不够准确。
- 建议韩文：세션 목록
- 场景：会话列表标题

内容指纹：`53e45e60f0ed4e70f2c5e9fb0ab0817a180ecfe1f3f4fb0e2e830f2781ce57cc`

### `json:src/i18n/locales#settings.codexSessionCompressionUsage`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`settings.codexSessionCompressionUsage`
- 中文：会话目录当前占用 {{size}}
- 现有韩文：세션 파일의 디스크 사용량: {{size}}
- 问题：原文统计的是“会话目录当前占用”，韩文写成“세션 파일의 디스크 사용량”，把目录范围收窄为文件。
- 建议韩文：세션 디렉터리 사용량: {{size}}
- 场景：Codex 会话压缩设置容量信息

内容指纹：`04a8dd92b66723b42f0374e236b35fa3c3d78e6d453f19129ad1be0b3b64790c`

### `json:src/i18n/locales#settings.globalProxy.hint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`settings.globalProxy.hint`
- 中文：代理所有请求（API、Skills 下载等）。开启本地路由时，应用的请求也会经过此代理。留空表示直连。
- 现有韩文：모든 요청(API, 스킬 다운로드 등)을 프록시합니다. 로컬 라우팅이 활성화되면 앱 트래픽도 이 프록시를 통해 라우팅됩니다. 직접 연결하려면 비워두세요.
- 问题：「비워두세요」应按韩语辅助动词规范分写为「비워 두세요」。
- 建议韩文：모든 요청(API, 스킬 다운로드 등)을 프록시합니다. 로컬 라우팅이 활성화되면 앱 트래픽도 이 프록시를 통해 라우팅됩니다. 직접 연결하려면 비워 두세요.
- 场景：全局出站代理说明

内容指纹：`f79c817c400fe06f40cf5c4abde2ebf32234a197533f8794f7bae2b1cf8389be`

### `json:src/i18n/locales#settings.globalProxy.password`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`settings.globalProxy.password`
- 中文：密码（可选）
- 现有韩文：비밀번호(선택사항)
- 问题：「선택사항」与项目统一写法「선택 사항」不一致。
- 建议韩文：비밀번호(선택 사항)
- 场景：全局代理密码字段

内容指纹：`536e18ba3e5f68b5005f893849059984c2630277fc02e21a20bc8c6cb525f7c2`

### `json:src/i18n/locales#settings.toolUninstallReinstalledByUpdater`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`settings.toolUninstallReinstalledByUpdater`
- 中文：这份是 {{tool}} 自动更新时一并安装的，单独卸载后，下次更新还会装回来。
- 现有韩文：{{tool}}의 업데이터는 이 복사본을 다른 복사본과 함께 설치했습니다. 이 복사본만 제거하면 다음 업데이트에서 다시 설치됩니다.
- 问题：原文表示“这份副本是工具自动更新时一并安装的”，韩文主语变成 updater 主动安装副本，语义不够准确。
- 建议韩文：{{tool}} 자동 업데이트 과정에서 함께 설치된 복사본입니다. 이 복사본만 제거하면 다음 업데이트에서 다시 설치됩니다.
- 场景：工具卸载说明

内容指纹：`910606b48aa9eb3110d0f8119c9abdbc5f59c278d3288d8cd83a120e0732b109`

### `json:src/i18n/locales#skills.count`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`skills.count`
- 中文：共 {{count}} 个技能
- 现有韩文：{{count}} 스킬
- 问题：原文是“共 count 个技能”，韩文「count 스킬」缺少量词且语序不自然。
- 建议韩文：스킬 {{count}}개
- 场景：技能数量徽标

内容指纹：`bb2d966540ef5153f1dc27a76cbaf3a51b077dd0f9d9491858527523db5651bd`

### `json:src/i18n/locales#skills.error.suggestion.checkNetwork`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`skills.error.suggestion.checkNetwork`
- 中文：请检查网络连接
- 现有韩文：네트워크 연결을 확인해주세요
- 问题：「확인해주세요」未按韩语辅助动词规范分写，与同组「확인하세요」风格不一致。
- 建议韩文：네트워크 연결을 확인해 주세요.
- 场景：技能下载失败建议

内容指纹：`e9969cf37c04011e7726de3538ebe25fd72b9e24f64e8b4dd6c1de43bb7dc471`

### `json:src/i18n/locales#skills.installFromZip.skippedItem`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`skills.installFromZip.skippedItem`
- 中文：{{directory}}（已被 {{name}} 使用）
- 现有韩文：{{directory}}({{name}}에서 사용)
- 问题：「{{name}}에서 사용」缺少状态词，且“在名称中”搭配不自然；应明确该目录已被同名技能占用。
- 建议韩文：{{directory}}(사용 중인 이름: {{name}})
- 场景：ZIP 安装目录冲突列表

内容指纹：`d7ef34579b80b9982d020babed3a7910cd03ab00019a1b1f8c1bca6139cd48e9`

### `json:src/i18n/locales#skills.installFromZip.successMultiple`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`skills.installFromZip.successMultiple`
- 中文：成功安装 {{count}} 个技能
- 现有韩文：{{count}} 스킬을 성공적으로 설치했습니다.
- 问题：「{{count}} 스킬」量词和语序不自然，项目其他位置统一为「스킬 N개」。
- 建议韩文：스킬 {{count}}개를 설치했습니다.
- 场景：ZIP 多技能安装成功提示

内容指纹：`5c10e7cd31c6c08d48e0b863dcf47f7a3efc703932219c9c2e47cfb79ce38951`

### `json:src/i18n/locales#streamCheck.error`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`streamCheck.error`
- 中文：{{providerName}} 检查出错: {{error}}
- 现有韩文：{{providerName}} 확인 오류: {{error}}
- 问题：「확인 오류」容易被理解为“确认时出错”，原文是连通性检查本身出错。
- 建议韩文：{{providerName}} 검사 오류: {{error}}
- 场景：端点连通性检查错误

内容指纹：`3984ae48efe7425b8d1f2671e2436398495dad66b713821e3c1e306ac7bc6f71`

### `json:src/i18n/locales#streamCheck.unreachableHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`streamCheck.unreachableHint`
- 中文：无法建立连接（DNS / 连接 / TLS / 超时）。请检查 base_url 与网络。
- 现有韩文：연결을 설정할 수 없습니다(DNS/연결/TLS/시간 초과). base_url과 네트워크를 확인하세요.
- 问题：「연결을 설정할 수 없습니다」会被理解为“无法配置连接”，原文是无法建立连接。
- 建议韩文：연결할 수 없습니다(DNS/연결/TLS/시간 초과). base_url과 네트워크를 확인하세요.
- 场景：端点连通性测试失败提示

内容指纹：`519283f7059a06ca259cf6101d45389feab1099c679a189481ad4ff7b70551d1`

### `json:src/i18n/locales#subscription.expiredHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`subscription.expiredHint`
- 中文：请运行 {{tool}} 命令刷新登录
- 现有韩文：{{tool}} 명령을 실행하여 로그인을 새로 고치세요.
- 问题：「로그인을 새로 고치세요」在韩语中不自然，登录通常说「갱신하다」或「다시 로그인하다」；命令用途是刷新登录凭据。
- 建议韩文：{{tool}} 명령을 실행해 로그인을 갱신하세요.
- 场景：订阅额度失效提示

内容指纹：`0467ae1f647a5aebcfd5f60c50f79e93ae99a23dff4b46a7da2a5a1449b9f67a`

### `json:src/i18n/locales#universalProvider.notesPlaceholder`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`universalProvider.notesPlaceholder`
- 中文：可选：添加备注信息
- 现有韩文：선택사항: 메모 추가
- 问题：「선택사항」与项目统一写法「선택 사항」不一致。
- 建议韩文：선택 사항: 메모 추가
- 场景：统一供应商备注输入框

内容指纹：`54c5dee94fced4eed05ff06083aa02f79b10736e654df160e37f02fbe2387631`

### `json:src/i18n/locales#usage.costBreakdown`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.costBreakdown`
- 中文：成本明细
- 现有韩文：비용 분석
- 问题：原文是“成本明细”，韩文「비용 분석」表示成本分析，不是明细拆分。
- 建议韩文：비용 내역
- 场景：用量成本明细标题

内容指纹：`ab89dd2a645f8888f0ee09b0c84c65a06cce0b68df3d3cb314ffe2e2b8ae6087`

### `json:src/i18n/locales#usage.detail.costTitle`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.detail.costTitle`
- 中文：成本明细（{{currency}}）
- 现有韩文：비용 분석({{currency}})
- 问题：原文是“成本明细”，韩文「비용 분석」改变了含义；应与明细类标题统一为「비용 내역」。
- 建议韩文：비용 내역({{currency}})
- 场景：请求详情成本明细

内容指纹：`40b6e60a10ea82e462cf223e393c5ebf041303ebb8f6574f1d8dcb7907ed34fd`

### `json:src/i18n/locales#usage.detail.sourceProxy`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.detail.sourceProxy`
- 中文：路由服务 · 状态码 {{code}}
- 现有韩文：라우팅 서비스 · 상태 {{code}}
- 问题：原文是“状态码”，韩文只写「상태」，遗漏 code。
- 建议韩文：라우팅 서비스 · 상태 코드 {{code}}
- 场景：请求来源详情

内容指纹：`4345673077d80f3ba5d8b8ac6fa143ad2e56cdcc59c0cd9b8c1b3e5c5538c656`

### `json:src/i18n/locales#usage.modelsDevAutoSync.selectionHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.modelsDevAutoSync.selectionHint`
- 中文：归一化模型 ID 相同的选项只会导入一次。
- 现有韩文：정규화된 모델 ID가 동일한 선택 항목을 한 번 가져옵니다.
- 问题：「동일한 선택 항목을 한 번 가져옵니다」把“相同模型 ID 的选项只导入一次”译得主谓不清。
- 建议韩文：정규화된 모델 ID가 같은 항목은 한 번만 가져옵니다.
- 场景：models.dev 自动同步选择规则

内容指纹：`7932042885d0d494822601683ceeda10d71fb34783a2a0cc718a36a8802e6d06`

### `json:src/i18n/locales#usage.perMillion`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.perMillion`
- 中文：(每百万)
- 现有韩文：(백만개당)
- 问题：「백만개당」未按韩语数量单位规范分写。
- 建议韩文：(백만 개당)
- 场景：定价单位

内容指纹：`cb5c3e3c4c2cd7770981d58cb981498e778b58a879e3100bd8426e1d68127275`

### `json:src/i18n/locales#usage.realTotalHint`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.realTotalHint`
- 中文：Input + Output + 缓存写入 + 缓存命中
- 现有韩文：입력 + 출력 + 캐시 쓰기 + 캐시 읽기
- 问题：原文最后一项是缓存命中，韩文写成「캐시 읽기」，与本项目统一的「캐시 적중」术语不一致。
- 建议韩文：입력 + 출력 + 캐시 쓰기 + 캐시 적중
- 场景：真实消耗 Token 说明

内容指纹：`b6bfab081636e103cf999d130848a1f205de5701ac56109caa8a30fed4d8ba59`

### `json:src/i18n/locales#usage.rebuildCodex.confirmAction`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.rebuildCodex.confirmAction`
- 中文：备份并重建
- 现有韩文：백업 및 재구축
- 问题：同组其他文案使用「재구성」，此处按钮却用「재구축」，同一功能术语不一致。
- 建议韩文：백업 및 재구성
- 场景：Codex 用量重建确认按钮

内容指纹：`c903e956ad60aab5795cf9a4f44c1c8fdf9d6f7e6361022b70461629e319f904`

### `json:src/i18n/locales#usage.timeRangeTooLarge`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.timeRangeTooLarge`
- 中文：时间范围过大，请缩小范围
- 现有韩文：시간 범위가 너무 큽니다. 범위를 좁혀주세요.
- 问题：「좁혀주세요」应按项目统一写法分写为「좁혀 주세요」。
- 建议韩文：시간 범위가 너무 큽니다. 범위를 좁혀 주세요.
- 场景：用量时间范围校验

内容指纹：`7e94e4d3c5a96584d29f10407b57ffb19f7b4d37ca9fa1d3f86d4384fb476725`

### `json:src/i18n/locales#usage.totalRequests`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usage.totalRequests`
- 中文：总请求数
- 现有韩文：총 요청
- 问题：原文是“总请求数”，韩文「총 요청」遗漏数量含义。
- 建议韩文：총 요청 수
- 场景：用量统计指标

内容指纹：`49cc95ac3c88cb0af4d060c61dbc9bad347d13ec2493ed6cae01b948330a3d54`

### `json:src/i18n/locales#usageScript.baseUrl`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usageScript.baseUrl`
- 中文：请求地址
- 现有韩文：기본 URL
- 问题：原文是“请求地址”，韩文「기본 URL」可能被理解为默认 URL，字段用途不够直观。
- 建议韩文：요청 URL
- 场景：用量脚本请求地址字段

内容指纹：`13ad772849568fd0473be47143fe2192a44dd283a89cc37dec0a65a0b8246f67`

### `json:src/i18n/locales#usageScript.baseUrlPlaceholder`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usageScript.baseUrlPlaceholder`
- 中文：留空则使用供应商的请求地址
- 现有韩文：공급자의 기본 URL을 사용하려면 비워두세요.
- 问题：同字段应统一表达为“请求 URL”，避免「기본 URL」与“默认 URL”混淆。
- 建议韩文：공급자의 요청 URL을 사용하려면 비워 두세요.
- 场景：用量脚本请求地址占位符

内容指纹：`73cdab1f820798b053d0dc22d7a94c750506edf99d1fde4b40560dcc1ae798a9`

### `json:src/i18n/locales#usageScript.method`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usageScript.method`
- 中文：HTTP 方法
- 现有韩文：HTTP 방식
- 问题：HTTP 方法在韩语软件术语中通常为「HTTP 메서드」，「방식」更像方式/模式。
- 建议韩文：HTTP 메서드
- 场景：用量脚本请求方法字段

内容指纹：`b389f4fcd267f981ebc6b53612b3e3cb91794af3b24a209e001fe65e5d9e84c5`

### `json:src/i18n/locales#usageScript.scriptEmpty`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usageScript.scriptEmpty`
- 中文：脚本配置不能为空
- 现有韩文：스크립트 설정은 비워둘 수 없습니다.
- 问题：「비워둘 수 없습니다」应按韩语辅助动词规范分写为「비워 둘 수 없습니다」。
- 建议韩文：스크립트 설정은 비워 둘 수 없습니다.
- 场景：用量脚本空值校验

内容指纹：`ba35ea2014855645deca295b8ba9e835b8b5ff41ea2a59a4165d124f89402ffe`

### `json:src/i18n/locales#usageScript.templateGeneral`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`usageScript.templateGeneral`
- 中文：通用模板
- 现有韩文：일반
- 问题：原文是“通用模板”，韩文只写「일반」，遗漏模板类型语义。
- 建议韩文：일반 템플릿
- 场景：用量脚本模板类型

内容指纹：`5c82c26b48e1d9e48983297a0699e1887df04e0062455c89cd37268b61e37c2b`

## 待核实（4）

### `json:src/i18n/locales#providerCard.reason.currentCannotRemove`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`providerCard.reason.currentCannotRemove`
- 中文：（无）
- 现有韩文：（缺失）
- 问题：该键仅存在于 Turkish 资源，中文、英文、韩文均缺失；无法判断它是已废弃的土耳其语独有键，还是遗漏了其他语言资源。
- 场景：供应商卡片状态/移除原因

内容指纹：`0448da6fef04a53dc61abe31a7c2619770434e3e2d4808bc753f8b3f575f78ad`

### `json:src/i18n/locales#providerCard.status.current`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`providerCard.status.current`
- 中文：（无）
- 现有韩文：（缺失）
- 问题：该键仅存在于 Turkish 资源，中文、英文、韩文均缺失；无法确认是否仍被当前界面引用。
- 场景：供应商卡片当前状态

内容指纹：`33984f1b1e458ac047f7bf952f77dc81d0446eb7c570b2f01b758d6ee0a21161`

### `json:src/i18n/locales#proxy.settings.validation.portMax`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`proxy.settings.validation.portMax`
- 中文：端口必须小于65535
- 现有韩文：포트는 65535 이하여야 합니다.
- 问题：中文消息写“小于 65535”，但同页说明写 1024~65535，韩文写“65535 이하”（允许 65535）；原文与技术范围存在边界冲突，需确认端口 65535 是否合法。
- 场景：路由服务端口校验

内容指纹：`92e11b074c3b4538d8dceb708ee2be3078b879a306f79052b8b0ec1422a2543b`

### `json:src/i18n/locales#proxy.settings.validation.portMin`

- 文件：`src/i18n/locales/ko.json`
- 资源键：`proxy.settings.validation.portMin`
- 中文：端口必须大于1024
- 现有韩文：포트는 1024 이상이어야 합니다.
- 问题：中文消息写“大于 1024”，但同页说明写 1024~65535，韩文写“1024 이상”（允许 1024）；原文与技术范围存在边界冲突，需确认端口 1024 是否合法。
- 场景：路由服务端口校验

内容指纹：`6ad24d19314b4ee0dc853c3d50a5de575cec1a5e26b888a50a40929386c3e1a8`

