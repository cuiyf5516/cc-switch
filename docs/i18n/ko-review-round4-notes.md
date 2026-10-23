# 第四轮审查：以中文为主要语义来源

审查日期：2026-10-24。输入：ko-review-requests-2026-10-23-2.json。

已逐项对照中文检查全部 4,292 条界面文案及 71 条原生文案，共 4,363 条。本轮修改 193 条界面文案和 2 条原生文案。提交的 19 条备注中，16 条修改、3 条保留。对附带备注逐条评估，不把备注中的建议视为覆盖中文或实际行为的额外指令。

中文是本轮的主要语义来源。英文仅用于辅助核对代码标识、协议字段及运行时占位符；不因英文省略或改变中文信息而沿用偏差。以中文为准不等于逐字直译，韩文仍按自然语序表达。

## 重点修正

- 条件及范围：Google API 留空条件、聚合模型重选条件、没有模型时只影响该供应商。
- 操作场景：agy 打开终端前切换全局登录；旧进程可能把旧账号信息写回登录设置。已查 OpenTerminalDialog.tsx、agy_account/mod.rs。
- 省略与误替换：OMO 配置被写成供应商、授权中心被简化为账号、中文搭档被改成友好搭档、中文交流要求被改成简短回答偏好、CCSub 被改写为其他订阅的替代品。
- 重复术语：配置文件写入／写回用 저장／복원／변경 표현；日志记录保留 기록，缓存写入及工具写文件保留 쓰기。用量查询用 조회，URL 查询参数保留 쿼리；模型选择器按菜单语境用 모델 선택 메뉴。
- 动态名称：部分动态名称的宾格助词采用 을(를)，避免固定用 를。

## 占位符及来源差异

- providerPreset.matchedVersions：中文使用 name + n（总数），韩文沿用 name + more（其余数量），调用方同时传入 n 和 more，语义等价；补回“版本”名词，保留运行时契约。
- prompts.updatedOn：调用方同时提供 month/day 和本地化 date，韩文的 date 与中文月日表达具有相同日期语义，保留本地化形式。
- quota.tierLeft / tierUsedUp / tierUsed：中文用带空格的 labelSp，韩文用 label 并在译文中安排空格或助词，含义相同。
- 数字检查中折扣、千分位、中文“万”与韩文计数表达不同但数值相等的情况保留；未将九折误改为九个百分点优惠。

逐条审计保留最初 before；after 和累计状态为当前结果。新增 chineseSourceSha256、chineseReviewStatus 以及本轮范围元数据，可核对中文来源和本轮保留／修改状态。没有自动将全量条目标成用户已审查；仅[本次 19 条结果 JSON](ko-review-round4-results.json)供导入确认。浏览器会把已审查但译文变化的其他条目重新转为待复审。

## 本轮验证

- 16 项本地化测试通过（tests/config/localeCoverage.test.ts），覆盖占位符、技术标识、代码字面值等。
- 全部 4,363 条 HTML／Markdown／审计一致，4,292 条实际韩文资源一致，第二／三／四轮导入结果与当前资源一致。
- 中文及英文来源哈希校验通过；本轮未修改中英文原文和运行时占位符。
- 原生修改仅位于韩语覆盖分支，其他语言保持原样。
- 韩语 JSON 的 Prettier 检查及 git diff --check 通过。
- 未进行韩语母语者审校、桌面布局验收或完整 Tauri 构建。

## 提交的 19 条备注

### jsonEditor.mustBeObject

中文：配置必须是JSON对象，不能是数组或其他类型

处理：保留。现译明确要求设置为 JSON 对象，并排除数组及其他类型，与中文一致；设置用 설정，JSON 对象用 객체。

最终韩文：설정은 배열이나 다른 유형이 아닌 JSON 객체여야 합니다.

### provider.tabUniversal

中文：统一供应商

处理：修改为 범용 공급자，补全中文“供应商”的含义，避免仅跟随英文 Universal 而省略名词；与其他统一供应商条目一致，韩语词间保留空格。

最终韩文：범용 공급자

### provider.directProvider

中文：直连

处理：保留 직접 연결。这里指客户端直接连接供应商，与路由模式相对；直接连接比只写 직접 或音译 다이렉트 更完整、明确。

最终韩文：직접 연결

### provider.stackBadgeHint

中文：在 {{client}} 的模型选择器里选择：{{models}}

处理：将模型选择器统一为 모델 선택 메뉴。这里是客户端里选择模型的菜单，不需要机械翻译成选择器；并同步所有同类条目。

最终韩文：{{client}}의 모델 선택 메뉴에서 선택: {{models}}

### provider.stackBadgeNoModels

中文：这家没有配置模型，不会出现在模型选择器里

处理：修正主语及范围：这家供应商没有设置模型，所以它的模型不会显示；不是整个模型选择菜单都不显示任何内容。

最终韩文：이 공급자에는 설정된 모델이 없어 해당 모델이 모델 선택 메뉴에 표시되지 않습니다.

### provider.stackSaved

中文：已保存，重启 {{client}} 后生效

处理：修改为 {{client}}을(를)，兼容动态名称不同的收音；明确重启后生效，而非保存后立即生效。

最终韩文：저장되었습니다. {{client}}을(를) 다시 시작하면 적용됩니다.

### provider.stackReselectHint

中文：CC Switch 每次改写客户端配置后，如果模型选择器里选的是聚合的模型，需要重新选一次

处理：补回中文条件“如果选择了聚合模型”，明确每次 CC Switch 更改客户端配置之后，需要重新选择该模型。原译省略了条件，范围过大；用 변경 避免“写字”的联想。

最终韩文：CC Switch가 클라이언트 설정을 변경할 때마다, 모델 선택 메뉴에서 통합 모델을 선택해 둔 경우 해당 모델을 다시 선택해야 합니다.

### provider.stackPartial

中文：已部分写入，将在下次操作或重启 CC Switch 时补完

处理：改用 설정이 일부만 저장되었습니다。这里是配置写入，统一用保存 설정 저장，保留“下次操作或重启时补完”；日志记录才用 기록，缓存写入仍用 쓰기。

最终韩文：설정이 일부만 저장되었습니다. 다음 작업을 수행하거나 CC Switch를 다시 시작하면 나머지 설정이 저장됩니다.

### provider.stackDefaultHint

中文：它是默认供应商：列表里的第一个模型负责 Claude Code 启动和后台任务

处理：去掉指代生硬的 이것이，直接说明“是默认供应商”，并明确是这家供应商模型列表里的第一项负责启动及后台任务。

最终韩文：기본 공급자입니다. 이 공급자의 모델 목록에서 첫 번째 모델이 Claude Code의 시작 및 백그라운드 작업을 처리합니다.

### provider.officialModelsBundled

中文：官方模型列表暂未取到，暂用 Codex 内置列表，可能缺少账号专属模型

处理：修正“尚未取到”为 아직 가져오지 못해，而非“尚未提供”；账号专属模型写为 해당 계정에서만 제공되는 모델，保留专属含义。

最终韩文：공식 모델 목록을 아직 가져오지 못해 임시로 Codex 내장 목록을 사용합니다. 해당 계정에서만 제공되는 모델이 누락될 수 있습니다.

### provider.officialModelsOutdated

中文：本机 Codex 版本过旧，拿不到完整的官方模型列表：请把 Codex（包括命令行）升级到最新版

处理：补明 Codex 버전이 오래되어，明确是软件版本旧，不是电脑或 Codex 本身年代久；保留完整列表和升级要求。

最终韩文：이 컴퓨터에 설치된 Codex 버전이 오래되어 전체 공식 모델 목록을 가져올 수 없습니다. Codex(CLI 포함)를 최신 버전으로 업데이트하세요.

### provider.addProviderHint

中文：填写信息后即可在列表中快速切换供应商。

处理：原译语法并非错误，但改为“输入信息后即可在列表里快速切换”，更忠实表达中文的先后关系和结果。

最终韩文：정보를 입력하면 목록에서 공급자를 빠르게 전환할 수 있습니다.

### provider.sortUpdateFailed

中文：排序更新失败

处理：保留。这里是调整顺序后的保存／更新失败提示（useDragSort.ts、App.tsx），정렬 순서를 업데이트하지 못했습니다 准确；不应扩大成“排序功能不可用”。

最终韩文：정렬 순서를 업데이트하지 못했습니다.

### provider.openTerminalDialog.agySwitchTitle

中文：会切换 agy 的登录

处理：结合 OpenTerminalDialog 的 Notice 场景，标题改为“agy 登录账号将改变”，去掉没有前文指代的 그러면。

最终韩文：agy 로그인 계정이 변경됩니다

### provider.openTerminalDialog.agySwitchBody

中文：打开前把 agy 的登录切换到 {{account}}，之后新开的 agy 都用这个号。

处理：明确是在“打开终端之前”把 agy 登录账号切换至 {{account}}，后续新启动的所有 agy 都使用该账号，避免只写不明确的“打开前”。

最终韩文：터미널을 열기 전에 agy 로그인 계정을 {{account}}(으)로 변경합니다. 이후 새로 실행하는 모든 agy는 이 계정을 사용합니다.

### provider.openTerminalDialog.agySwitchRunning

中文：检测到 agy 正在运行：已打开的 agy 仍用原账号，还可能把原账号写回去，最好先退出它们。

处理：按中文及 agy_account 的实现，明确旧 agy 可能将旧账号信息重新保存到登录设置，覆盖刚切换的登录状态；不是把配置写入某个旧账号。保留“最好先退出”的建议语气。

最终韩文：실행 중인 agy가 감지되었습니다. 이미 실행 중인 agy는 기존 계정을 계속 사용하며, 기존 계정 정보를 로그인 설정에 다시 저장할 수도 있습니다. 먼저 해당 agy를 모두 종료하는 것이 좋습니다.

### provider.usageSaved

中文：用量查询配置已保存

处理：统一“用量查询”为 사용량 조회，与 provider.configureUsage 和 usageScript.title 保持一致，配置用 설정。

最终韩文：사용량 조회 설정이 저장되었습니다.

### provider.usageSaveFailed

中文：用量查询配置保存失败

处理：同上一条统一 사용량 조회 설정，失败句沿用“无法保存”，不因中文出现“失败”就机械改成名词句。

最终韩文：사용량 조회 설정을 저장하지 못했습니다.

### provider.form.agy.endpointHelp

中文：留空用 Google 默认 API。第三方地址须兼容 Gemini API，并支持 agy 内置的 Gemini 模型。

处理：修正条件关系：留空时使用 Google 默认 API，而不是“把 Google 默认 API 留空”；保留第三方端点须兼容 Gemini API 并支持 agy 内置 Gemini 模型两个条件。

最终韩文：비워 두면 Google 기본 API를 사용합니다. 타사 엔드포인트는 Gemini API와 호환되어야 하며 agy에 내장된 Gemini 모델을 지원해야 합니다.

## 本轮全部修改

| 翻译键 | 中文 | 本轮修改前韩文 | 当前韩文 |
|---|---|---|---|
| app.description | Claude Code / Codex / Gemini CLI 全方位辅助工具 | Claude Code, Codex 및 Gemini CLI용 통합 관리 도구 | Claude Code / Codex / Gemini CLI용 종합 지원 도구 |
| claudeConfig.configLabel | Claude Code 配置 (JSON) * | Claude Code settings.json (JSON) * | Claude Code 설정 (JSON) * |
| provider.tabUniversal | 统一供应商 | 범용 | 범용 공급자 |
| provider.noProvidersDescription | 如果你已有配置，请点击"导入当前配置"，所有数据将安全保存在 default 供应商中 | 이미 설정이 있는 경우 "현재 설정 가져오기"를 클릭하세요. 모든 데이터는 기본 공급자에 안전하게 저장됩니다. | 이미 설정이 있다면 "현재 설정 가져오기"를 클릭하세요. 모든 데이터는 "default" 공급자에 안전하게 저장됩니다. |
| provider.stackBadgeHint | 在 {{client}} 的模型选择器里选择：{{models}} | {{client}}의 모델 선택기에서 선택: {{models}} | {{client}}의 모델 선택 메뉴에서 선택: {{models}} |
| provider.stackBadgeNoModels | 这家没有配置模型，不会出现在模型选择器里 | 이 공급자에는 설정된 모델이 없으므로 모델 선택기에 아무 것도 표시되지 않습니다. | 이 공급자에는 설정된 모델이 없어 해당 모델이 모델 선택 메뉴에 표시되지 않습니다. |
| provider.stackSaved | 已保存，重启 {{client}} 后生效 | 저장되었습니다. 적용하려면 {{client}}를 다시 시작하세요. | 저장되었습니다. {{client}}을(를) 다시 시작하면 적용됩니다. |
| provider.stackReselectHint | CC Switch 每次改写客户端配置后，如果模型选择器里选的是聚合的模型，需要重新选一次 | CC Switch가 클라이언트 설정을 다시 쓸 때마다 모델 선택기에서 통합된 모델을 다시 선택하세요 | CC Switch가 클라이언트 설정을 변경할 때마다, 모델 선택 메뉴에서 통합 모델을 선택해 둔 경우 해당 모델을 다시 선택해야 합니다. |
| provider.stackPartial | 已部分写入，将在下次操作或重启 CC Switch 时补完 | 일부만 기록되었습니다. 다음 변경 시 또는 CC Switch를 다시 시작할 때 나머지 기록을 완료합니다 | 설정이 일부만 저장되었습니다. 다음 작업을 수행하거나 CC Switch를 다시 시작하면 나머지 설정이 저장됩니다. |
| provider.stackDefaultHint | 它是默认供应商：列表里的第一个模型负责 Claude Code 启动和后台任务 | 이것이 기본 공급자입니다. 목록의 첫 번째 모델이 Claude Code의 시작 및 백그라운드 작업을 처리합니다. | 기본 공급자입니다. 이 공급자의 모델 목록에서 첫 번째 모델이 Claude Code의 시작 및 백그라운드 작업을 처리합니다. |
| provider.officialModelsBundled | 官方模型列表暂未取到，暂用 Codex 内置列表，可能缺少账号专属模型 | 공식 모델 목록은 아직 제공되지 않으므로 현재 Codex에 내장된 목록이 사용되며 계정별 모델이 누락될 수 있습니다. | 공식 모델 목록을 아직 가져오지 못해 임시로 Codex 내장 목록을 사용합니다. 해당 계정에서만 제공되는 모델이 누락될 수 있습니다. |
| provider.officialModelsOutdated | 本机 Codex 版本过旧，拿不到完整的官方模型列表：请把 Codex（包括命令行）升级到最新版 | 이 컴퓨터의 Codex는 너무 오래되어 전체 공식 모델 목록을 얻을 수 없습니다. Codex(CLI 포함)를 최신 버전으로 업데이트하세요. | 이 컴퓨터에 설치된 Codex 버전이 오래되어 전체 공식 모델 목록을 가져올 수 없습니다. Codex(CLI 포함)를 최신 버전으로 업데이트하세요. |
| provider.addProviderHint | 填写信息后即可在列表中快速切换供应商。 | 목록에서 공급자를 빠르게 전환하려면 정보를 입력하세요. | 정보를 입력하면 목록에서 공급자를 빠르게 전환할 수 있습니다. |
| provider.openTerminalDialog.isolationBodyAgy | 「{{name}}」的 Key 和地址只传给这个终端里的 agy，不写进任何文件；在别的终端里直接运行 agy 仍是 Google 登录。 | ‘{{name}}’의 키와 엔드포인트는 이 터미널의 agy에만 전달되며 파일에 기록되지 않습니다. 다른 터미널에서 agy를 직접 실행하면 기존 Google 로그인을 사용합니다. | “{{name}}”의 API 키와 엔드포인트는 이 터미널에서 실행하는 agy에만 전달되고 어떤 파일에도 저장되지 않습니다. 다른 터미널에서 agy를 직접 실행하면 Google 로그인을 계속 사용합니다. |
| provider.openTerminalDialog.agySwitchTitle | 会切换 agy 的登录 | 그러면 agy의 로그인이 전환됩니다. | agy 로그인 계정이 변경됩니다 |
| provider.openTerminalDialog.agySwitchBody | 打开前把 agy 的登录切换到 {{account}}，之后新开的 agy 都用这个号。 | 열기 전에 agy의 로그인은 {{account}}로 전환되고 이후 시작된 agy 세션은 이 계정을 사용합니다. | 터미널을 열기 전에 agy 로그인 계정을 {{account}}(으)로 변경합니다. 이후 새로 실행하는 모든 agy는 이 계정을 사용합니다. |
| provider.openTerminalDialog.agySwitchRunning | 检测到 agy 正在运行：已打开的 agy 仍用原账号，还可能把原账号写回去，最好先退出它们。 | agy가 실행 중입니다. 열려 있는 agy 세션은 이전 계정을 계속 사용하며 해당 계정을 다시 기록할 수 있습니다. 가능하면 먼저 해당 세션을 종료하세요. | 실행 중인 agy가 감지되었습니다. 이미 실행 중인 agy는 기존 계정을 계속 사용하며, 기존 계정 정보를 로그인 설정에 다시 저장할 수도 있습니다. 먼저 해당 agy를 모두 종료하는 것이 좋습니다. |
| provider.usageSaved | 用量查询配置已保存 | 사용량 쿼리 설정이 저장되었습니다. | 사용량 조회 설정이 저장되었습니다. |
| provider.usageSaveFailed | 用量查询配置保存失败 | 사용량 쿼리 설정을 저장하지 못했습니다. | 사용량 조회 설정을 저장하지 못했습니다. |
| provider.form.agy.endpointHelp | 留空用 Google 默认 API。第三方地址须兼容 Gemini API，并支持 agy 内置的 Gemini 模型。 | Google의 기본 API는 비워 두세요. 타사 엔드포인트는 Gemini API 및 agy의 내장 Gemini 모델을 지원해야 합니다. | 비워 두면 Google 기본 API를 사용합니다. 타사 엔드포인트는 Gemini API와 호환되어야 하며 agy에 내장된 Gemini 모델을 지원해야 합니다. |
| provider.form.agy.modelHelp | 填模型列表里的显示名称，可点「获取模型列表」选择。只对那次会话生效。 | 모델 목록(모델 가져오기)에 표시된 이름을 사용하세요. 해당 세션에만 적용됩니다. | 모델 목록에 표시되는 이름을 입력하세요. ‘모델 목록 가져오기’를 눌러 선택할 수 있습니다. 해당 세션에만 적용됩니다. |
| provider.form.agy.keyFieldsHint | 模型、Key 和地址都只在「打开终端」时使用，不写进 Antigravity 自己的设置。 | 모델, 키 및 엔드포인트는 ‘터미널 열기’에서만 사용되며 Antigravity 자체 설정에는 기록되지 않습니다. | 모델, API 키 및 엔드포인트는 ‘터미널 열기’ 실행 시에만 사용되며 Antigravity 자체 설정에는 저장하지 않습니다. |
| provider.form.agy.envFile | 启动环境变量 | 런처 환경 변수 | 실행 환경 변수 |
| provider.form.agy.envFileHint | 从卡片「打开终端」启动 agy 时，CC Switch 只把 API Key 和请求地址传给那一个 agy 进程，不写进任何文件。其他环境变量不会应用。 | 카드의 ‘터미널 열기’로 agy를 시작하면 CC Switch가 API 키와 엔드포인트를 해당 agy 프로세스에만 전달하며 파일에 기록하지 않습니다. 다른 환경 변수는 적용되지 않습니다. | 카드의 ‘터미널 열기’로 agy를 실행하면 CC Switch는 API 키와 엔드포인트를 해당 agy 프로세스에만 전달하고 어떤 파일에도 저장하지 않습니다. 다른 환경 변수는 적용되지 않습니다. |
| provider.backToList | 返回供应商列表 | 공급자로 돌아가기 | 공급자 목록으로 돌아가기 |
| claudeDesktop.upstreamModelLabel | 实际请求模型 | 요청된 모델 | 실제 요청에 사용할 모델 |
| claudeDesktop.routeInvalid | 请选择模型角色并填写实际请求模型 | 모델 역할을 선택하고 요청한 모델을 입력하세요. | 모델 역할을 선택하고 실제 요청에 사용할 모델을 입력하세요. |
| claudeDesktop.statusUnsupported | 当前平台暂不支持 Claude Desktop 3P 配置写入。 | 이 플랫폼은 아직 Claude Desktop 3P 설정 작성을 지원하지 않습니다. | 현재 플랫폼에서는 아직 Claude Desktop 3P 설정 저장을 지원하지 않습니다. |
| claudeDesktop.statusGatewayTokenMissing | 当前本地路由 token 尚未生成；重新切换该供应商会写入新的本地 token。 | 로컬 라우팅 토큰이 아직 생성되지 않았습니다. 이 공급자로 다시 전환하면 새 로컬 토큰이 작성됩니다. | 현재 로컬 라우팅 토큰이 아직 생성되지 않았습니다. 이 공급자로 다시 전환하면 새 로컬 토큰이 저장됩니다. |
| notifications.removeFromConfigFailed | 无法移除供应商 | 공급자를 삭제할 수 없습니다. | 공급자를 제거할 수 없습니다. |
| notifications.openclawNoModels | 该供应商没有配置模型 | 설정된 모델이 없습니다. | 이 공급자에는 설정된 모델이 없습니다. |
| notifications.backfillWarning | 切换成功，但旧供应商配置回填失败，您手动修改的配置可能未保存 | 성공적으로 전환되었지만 변경 사항을 이전 공급자에 다시 저장하지 못했습니다. | 전환은 완료되었지만 이전 공급자의 설정을 다시 저장하지 못해 수동으로 변경한 설정이 저장되지 않았을 수 있습니다. |
| confirm.unifyCodexHistory.message | 开启后，Codex CLI 的 resume 列表会把官方订阅与第三方的会话合并显示（Codex 桌面版更新后已经可以显示全部会话，不受影响）。注意：跨供应商继续旧会话时，可能因对方后端无法解密 encrypted_content 推理内容而失败。<br><br>可选择同时把现有官方会话历史迁入共享列表（迁移前自动备份到 ~/.cc-switch/backups，关闭开关时可选择恢复）。 | 활성화되면 Codex CLI 재개 목록에 공식 구독과 타사 세션이 함께 표시됩니다(Codex 데스크톱 앱은 최근 업데이트 이후의 모든 세션을 표시할 수 있으며 영향을 받지 않습니다). 참고: 다른 백엔드가 encrypted_content 추론을 해독할 수 없기 때문에 공급자 간에 이전 세션을 재개하는 것이 실패할 수 있습니다.<br><br>기존 공식 세션 기록을 공유 목록으로 마이그레이션할 수도 있습니다(먼저 ~/.cc-switch/backups에 백업하고 이 기능을 끄면 복원할 수 있습니다). | 켜면 Codex CLI의 resume 목록에 공식 구독과 타사 공급자의 세션이 함께 표시됩니다(Codex 데스크톱 버전은 업데이트 후 이미 모든 세션을 표시하므로 영향을 받지 않습니다). 주의: 다른 공급자로 이전 세션을 이어갈 때 해당 백엔드가 encrypted_content 추론 내용을 복호화하지 못해 실패할 수 있습니다.<br><br>기존 공식 세션 기록도 공유 목록으로 옮길 수 있습니다(이전하기 전에 ~/.cc-switch/backups에 자동 백업되며, 이 옵션을 끌 때 복원 여부를 선택할 수 있습니다). |
| confirm.usage.title | 配置用量查询 | 사용량 쿼리 설정 | 사용량 조회 설정 |
| settings.general.quotaDisplayHelp | 供应商卡片、授权中心和托盘里，各档额度写还剩多少还是已经用了多少。余额和 Credits 始终写剩下的。 | 공급자 카드, 계정 및 트레이에서 각 할당량 구간의 남은 양과 사용한 양 중 무엇을 표시할지 선택합니다. 잔액과 크레딧은 항상 남은 양을 표시합니다. | 공급자 카드, 인증 센터 및 트레이에서 각 할당량 구간의 남은 양과 사용한 양 중 무엇을 표시할지 선택합니다. 잔액과 Credits는 항상 남은 양을 표시합니다. |
| settings.advanced.rectifier.thinkingBudgetDescription | 当 Anthropic 类型供应商返回 budget_tokens 约束错误（如至少 1024）时，自动将 thinking 规范为 enabled 并将 budget 设为 32000，同时在需要时将 max_tokens 设为 64000，然后重试一次 | Anthropic 유형 공급자가 budget_tokens 제약 오류(예: 최소 1024)를 반환하면 추론을 활성화하고 추론 예산을 32000으로 설정합니다. 필요하면 max_tokens를 64000으로 늘린 후 한 번 다시 시도합니다. | Anthropic 유형 공급자가 budget_tokens 제약 오류(예: 최소 1024)를 반환하면 thinking을 enabled로, budget_tokens를 32000으로 설정합니다. 필요한 경우 max_tokens도 64000으로 설정한 뒤 한 번 다시 시도합니다. |
| settings.importExportHint | 导入/导出数据库 SQL 备份（仅支持导入由 CC Switch 导出的备份），便于备份或迁移。 | 마이그레이션 또는 복원을 위해 데이터베이스 SQL 백업을 가져오거나 내보냅니다. 가져오기는 CC Switch에서 내보낸 백업만 지원합니다. | 데이터베이스 SQL 백업을 가져오거나 내보내어 백업 또는 이전에 사용할 수 있습니다(CC Switch에서 내보낸 백업만 가져올 수 있습니다). |
| settings.backupStorage.deleteConfirmMessage | 将永久删除 {{path}} 中的 {{size}} 备份，此操作无法撤消。 | {{path}}의 백업 중 {{size}}가 영구적으로 삭제됩니다. 이 작업은 취소할 수 없습니다. | {{path}}에 있는 {{size}} 용량의 백업을 영구적으로 삭제합니다. 이 작업은 취소할 수 없습니다. |
| settings.backupStorage.items.liveFirstWrite.name | 配置文件首次写入备份 | 설정 최초 기록 전 백업 | 설정 파일 최초 저장 전 백업 |
| settings.backupStorage.items.liveFirstWrite.hint | CC Switch 第一次改写各客户端配置文件前的原始文件。删除后无法再找回改写前的原文件，下次写入时会重新备份当时的文件。 | CC Switch가 처음으로 덮어쓰기 전에 보관한 클라이언트 설정 원본입니다. 삭제하면 해당 원본이 사라지며, 다음 기록 시에는 그 시점의 파일을 백업합니다. | CC Switch가 각 클라이언트의 설정 파일을 처음 변경하기 전에 보관한 원본입니다. 삭제하면 변경 전 원본을 복구할 수 없으며, 다음 저장 시에는 그 시점의 파일을 다시 백업합니다. |
| settings.backupStorage.items.proxyLiveBackup.name | 旧版路由接管备份 | 레거시 라우팅 인계 백업 | 이전 버전의 라우팅 관리 백업 |
| settings.backupStorage.items.proxyLiveBackup.hint | 升级时从旧版路由接管备份转存出的配置副本，CC Switch 不会再读取。 | 업그레이드 중에 설정 복사본이 이전 라우팅 인계 백업에서 이동되었습니다. CC Switch는 다시는 읽지 않습니다. | 업그레이드 시 이전 버전의 라우팅 관리 백업에서 옮겨 보관한 설정 복사본입니다. CC Switch는 더 이상 읽지 않습니다. |
| settings.webdavSync.baseUrlPlaceholder | https://dav.jianguoyun.com/dav/ | https://dav.example.com/dav/ | https://dav.jianguoyun.com/dav/ |
| settings.webdavSync.usernamePlaceholder | 邮箱账号 | 이메일 또는 사용자 이름 | 이메일 계정 |
| settings.webdavSync.passwordPlaceholder | 应用密码（坚果云请使用「第三方应用密码」） | 앱 비밀번호 | 앱 비밀번호(Jianguoyun에서는 ‘타사 앱 비밀번호’ 사용) |
| settings.webdavSync.presets.jianguoyunHint | 请在坚果云「安全选项」中生成「第三方应用密码」，不要使用登录密码。 | Jianguoyun 보안 설정에서 "앱 비밀번호"를 생성하세요. 로그인 비밀번호를 사용하지 마세요. | Jianguoyun의 ‘보안 옵션’에서 ‘타사 앱 비밀번호’를 생성하세요. 로그인 비밀번호를 사용하지 마세요. |
| settings.webdavSync.confirmDownload.legacyNotice | 检测到旧版云端路径。恢复完成后，下次上传将写入新路径 v2/db-v6。 | 레거시 원격 경로가 감지되었습니다. 복원 후 다음 업로드는 새 v2/db-v6 경로에 기록됩니다. | 이전 버전의 클라우드 경로가 감지되었습니다. 복원이 끝나면 다음 업로드부터 새 경로 v2/db-v6에 저장합니다. |
| settings.webdavSync.confirmUpload.legacyNotice | 检测到旧版云端路径数据。本次上传将写入新路径 v2/db-v6，不会覆盖旧路径。 | 기존 원격 데이터가 감지되었습니다. 이 업로드는 새 v2/db-v6 경로에 기록되며 기존 경로를 덮어쓰지 않습니다. | 이전 버전의 클라우드 경로에 있는 데이터가 감지되었습니다. 이번 업로드는 새 경로 v2/db-v6에 저장하며 이전 경로는 덮어쓰지 않습니다. |
| settings.s3Sync.secretAccessKeyPlaceholder | 留空则保持现有密钥 | 기존 비밀 키를 유지하려면 변경하지 마세요 | 비워 두면 기존 비밀 키 유지 |
| settings.s3Sync.enabledHint | 开启后可使用 S3 上传/下载和自动同步。 | 수동 및 자동 클라우드 작업을 위해 S3 동기화를 켜세요. | 켜면 S3 업로드/다운로드 및 자동 동기화를 사용할 수 있습니다. |
| settings.silentStartupDescription | 程序启动时不显示主窗口，仅在系统托盘运行 | 기본 창을 표시하지 않고 백그라운드 모드에서 시작 | 앱 시작 시 메인 창을 표시하지 않고 시스템 트레이에서만 실행합니다. |
| settings.preserveCodexOfficialAuthOnSwitchDescription | 控制未开启路由接管时切换第三方供应商是否保留 Codex 官方登录；路由接管期间始终保留 | 로컬 라우팅이 꺼진 상태에서 타사 공급자로 전환할 때 Codex 공식 로그인을 유지할지 정합니다. 라우팅 접관 중에는 항상 공식 로그인을 유지합니다. | 라우팅이 앱 설정을 관리하지 않는 상태에서 타사 공급자로 전환할 때 Codex 공식 로그인을 유지할지 정합니다. 라우팅이 앱 설정을 관리하는 동안에는 항상 공식 로그인을 유지합니다. |
| settings.toolUninstallConfirmTitle | 卸载 {{tool}}？ | {{tool}}를 제거하시겠습니까? | {{tool}}을(를) 제거하시겠습니까? |
| settings.toolDiagnose | 诊断安装冲突 | 설치 진단 | 설치 충돌 진단 |
| settings.globalProxy.pricingDefaultsDescription | 设置各应用按请求模型还是返回模型匹配定价，仅对经本地路由的请求生效。 | 각 앱이 요청 모델 또는 응답 모델에 따라 가격을 일치하는지 선택합니다. 로컬 라우팅을 통과하는 요청에만 적용됩니다. | 각 앱의 요금을 요청 모델과 응답 모델 중 어느 모델에 따라 적용할지 설정합니다. 로컬 라우팅을 통과하는 요청에만 적용됩니다. |
| settings.data.location | 存储位置 | 위치 | 저장 위치 |
| pi.form.fixJsonFirst | 请先修复下方配置 JSON，再编辑结构化字段。 | 구조화된 필드를 편집하기 전에 아래 설정 JSON를 수정하세요. | 구조화된 필드를 편집하기 전에 아래 설정 JSON을 수정하세요. |
| pi.form.removeModel | 移除模型 | 모델 삭제 | 모델 제거 |
| pi.prompts.usePromptSuccess | 已写入全局 AGENTS.md | 전역 AGENTS.md를 업데이트했습니다 | 전역 AGENTS.md에 저장했습니다 |
| pi.prompts.activateOverrideTitle | 配置 {{filename}}？ | {{filename}}를 설정하시겠습니까? | {{filename}}을(를) 설정하시겠습니까? |
| pi.prompts.activateOverrideMessage | 创建 {{filename}} 会替换 Pi 内置基础提示。上下文、AGENTS.md 和 Skills 等仍由 Pi 按自身规则加入。 | {{filename}}를 생성하면 Pi의 내장 기본 프롬프트가 대체됩니다. Pi는 여전히 자체 규칙에 따라 컨텍스트, AGENTS.md, Skills 및 기타 리소스를 추가합니다. | {{filename}}을(를) 생성하면 Pi의 내장 기본 프롬프트가 대체됩니다. Pi는 여전히 자체 규칙에 따라 컨텍스트, AGENTS.md, Skills 및 기타 리소스를 추가합니다. |
| pi.prompts.deletedUndoable | 撤销会把文件原样写回。 | 실행 취소는 파일을 원래대로 다시 씁니다. | 실행 취소하면 파일을 원래 내용으로 복원합니다. |
| pi.prompts.fileRestored | 已写回 ~/.pi/agent/{{filename}} | ~/.pi/agent/{{filename}}를 다시 작성했습니다. | ~/.pi/agent/{{filename}}에 원래 내용을 복원했습니다. |
| pi.prompts.templateSaveTo | 保存到 {{path}} | {{path}}에 저장되었습니다. | 저장 위치: {{path}} |
| pi.prompts.templateRestored | 已写回 ~/.pi/agent/prompts/{{slug}}.md | ~/.pi/agent/prompts/{{slug}}.md를 다시 작성했습니다. | ~/.pi/agent/prompts/{{slug}}.md에 원래 내용을 복원했습니다. |
| grokBuild.keyFieldsHint | 默认模型（models.default）和它指向的模型表随供应商切换；其余是 Grok Build 全局设置，保存后对所有供应商生效。 | 기본 모델(models.default)과 그것이 가리키는 모델 테이블은 공급자를 따릅니다. 다른 모든 것은 Grok Build 전역 설정이며 저장 후 모든 공급자에 적용됩니다. | 기본 모델(models.default)과 해당 모델 테이블은 공급자를 전환하면 함께 바뀝니다. 나머지는 Grok Build 전역 설정이며 저장하면 모든 공급자에 적용됩니다. |
| sessionManager.exitSelection | 退出选择 | 선택 완료 | 선택 모드 종료 |
| sessionManager.selectSessionLabel | 选择 {{title}} | {{title}}를 선택하세요 | {{title}}을(를) 선택하세요 |
| sessionManager.backToList | 返回会话列表 | 세션으로 돌아가기 | 세션 목록으로 돌아가기 |
| sessionManager.launchFailed | 无法打开 {{terminal}}：{{error}}。恢复命令已复制，可以粘贴到任意终端运行。 | {{terminal}}: {{error}}를 열 수 없습니다. 재개 명령이 복사되었습니다. 아무 터미널에나 붙여넣으세요. | {{terminal}}을(를) 열 수 없습니다: {{error}}. 이어가기 명령을 복사했으니 원하는 터미널에 붙여 넣어 실행하세요. |
| sessionManager.questions | 提问 | 프롬프트 | 질문 |
| sessionManager.questionsMenu | 跳到提问 | 프롬프트로 이동 | 질문으로 이동 |
| sessionManager.copyAsMarkdown | 复制整段为 Markdown | 마크다운으로 복사 | 전체 대화를 Markdown으로 복사 |
| sessionManager.reload | 重新读取 | 새로고침 | 다시 읽기 |
| sessionManager.copyQuestion | 复制这条提问 | 이 프롬프트 복사 | 이 질문 복사 |
| sessionManager.consequenceCodex | 只删除这一个会话文件。Codex 桌面版的任务列表里可能仍显示它，点开会提示无法继续。 | 이 세션 파일만 삭제합니다. Codex 데스크탑 앱은 여전히 ​​이를 나열하고 계속할 수 없다고 말할 수 있습니다. | 이 세션 파일만 삭제합니다. Codex 데스크톱 앱의 작업 목록에는 계속 표시될 수 있지만, 열면 이어갈 수 없다는 메시지가 나타납니다. |
| sessionManager.reader.params | 参数 | 입력 | 매개변수 |
| sessionManager.reader.note | 说明 | 메모 | 설명 |
| sessionManager.reader.noteExpand | 展开说明 | 전체 메모 표시 | 설명 펼치기 |
| sessionManager.reader.questionsCount | {{count}} 次提问 | {{count}} 프롬프트 | 질문 {{count}}회 |
| sessionManager.reader.outlineTitle | 对话目录 | 대화 | 대화 목차 |
| sessionManager.reader.outlineToggle | 对话目录 | 대화 개요 | 대화 목차 |
| providerForm.partnerPromotion.sudocode | SudoCode 让 Claude Code 与 Claude Desktop 接入 Claude Opus 5，Codex 接入 GPT-5.6，一个 Key 统一使用。CC Switch 用户注册并加入 QQ 群 726213516，联系群主领取 ¥10 试用额度。 | SudoCode 키 하나로 Claude Code와 Claude Desktop에서는 Claude Opus 5를, Codex에서는 GPT-5.6을 사용합니다. 가입 후 QQ 그룹 726213516에 참여하고 그룹 관리자에게 연락하면 체험 크레딧 10위안을 받을 수 있습니다. | SudoCode는 하나의 API 키로 Claude Code와 Claude Desktop에서는 Claude Opus 5를, Codex에서는 GPT-5.6을 사용할 수 있게 합니다. CC Switch 사용자는 가입 후 QQ 그룹 726213516에 참여하고 그룹 관리자에게 연락하면 체험 크레딧 10위안을 받을 수 있습니다. |
| providerForm.partnerPromotion.apinebula | APINEBULA 为 CC Switch 用户提供特别优惠：使用专属链接注册并在充值时填写 "ccswitch" 优惠码，可享九折优惠。 | APINEBULA는 CC Switch 사용자에게 특별 할인을 제공합니다. 링크를 사용하여 등록하고 첫 번째 충전 시 "ccswitch" 프로모션 코드를 입력하면 10% 할인을 받을 수 있습니다. | APINEBULA는 CC Switch 사용자에게 특별 할인을 제공합니다. 전용 링크로 가입하고 충전 시 "ccswitch" 할인 코드를 입력하면 10% 할인을 받을 수 있습니다. |
| providerForm.partnerPromotion.ccsub | CCSub 是稳定、实惠的 AI API 中转平台，Claude Code 官方订阅的超强平替，一个 Key 覆盖全部模型，价格约为官方 1/3。 | CCSub는 안정적이고 저렴한 AI API 중계 플랫폼입니다. Claude.ai 및 OpenAI 구독의 대안으로, 키 하나로 모든 모델을 직접 API 비용의 약 30%에 이용할 수 있습니다. | CCSub는 안정적이고 합리적인 가격의 AI API 중계 플랫폼으로, Claude Code 공식 구독을 대체할 수 있습니다. 키 하나로 모든 모델을 이용하며 가격은 공식 가격의 약 3분의 1입니다. |
| providerForm.stackModelsLabel | 模型列表 | 모델 | 모델 목록 |
| providerForm.stackModelsEmpty | 未配置模型：把这家加入聚合后，模型选择器里不会多出它的模型 | 설정된 모델이 없습니다. 통합에 추가해도 모델 선택기에 이 공급자의 모델이 표시되지 않습니다 | 설정된 모델이 없습니다. 통합에 추가해도 모델 선택 메뉴에 이 공급자의 모델이 표시되지 않습니다 |
| providerForm.stackLayout.noModels | 模型列表为空：把这家加入聚合后，模型选择器里不会多出它的模型 | 모델 목록이 비어 있습니다. 통합에 추가해도 모델 선택기에 이 공급자의 모델이 표시되지 않습니다 | 모델 목록이 비어 있습니다. 통합에 추가해도 모델 선택 메뉴에 이 공급자의 모델이 표시되지 않습니다 |
| providerForm.requestModelLabel | 实际请求模型 | 요청된 모델 | 실제 요청에 사용할 모델 |
| providerForm.fetchModels | 获取模型列表 | 모델 가져오기 | 모델 목록 가져오기 |
| providerForm.gptContextWindowHint | 中转站的 GPT 多来自 ChatGPT 订阅，窗口只有 272K。窗口写大了不会提前压缩，等上游拒收时这一轮会失败；确认这家支持更大窗口再这样填。 | 릴레이의 GPT는 일반적으로 창이 272K에 불과한 ChatGPT 구독에서 제공됩니다. 더 큰 창은 업스트림이 요청을 거부하고 차례가 실패할 때까지 압축을 지연합니다. 이 공급자가 지원하는 경우에만 사용하십시오. | 중계 서비스의 GPT는 대부분 ChatGPT 구독을 통해 제공되어 컨텍스트 창이 272K에 불과합니다. 창 크기를 실제보다 크게 입력하면 미리 압축되지 않아 업스트림이 요청을 거부할 때 해당 응답이 실패합니다. 이 공급자가 더 큰 컨텍스트 창을 지원하는지 확인한 후 입력하세요. |
| providerForm.modelPicker.fromProvider | 供应商返回的模型 | 공급자로부터 | 공급자가 반환한 모델 |
| xaiOauth.reauthRequired | 需要重新登录 | 로그인이 필요합니다 | 다시 로그인 필요 |
| managedAuth.selectedAccountUnavailable | 已绑定账号不存在或需要重新登录，请重新选择账号 | 연결된 계정이 없거나 다시 로그인해야 합니다. 다른 계정을 선택하세요. | 연결된 계정이 없거나 다시 로그인해야 합니다. 계정을 다시 선택하세요. |
| codexConfig.modelListTitle | 模型列表 | 모델 | 모델 목록 |
| codexConfig.keyFieldsHint | 地址、Key、模型、推理档位、上下文窗口和兼容开关随供应商切换；其余是 Codex 全局设置，保存后对所有供应商生效。 | 엔드포인트, 키, 모델, 추론 수준, 컨텍스트 창 및 호환성 옵션은 공급자별 설정입니다. 나머지는 전역 Codex 설정이며 저장하면 모든 공급자에 적용됩니다. | 엔드포인트, API 키, 모델, 추론 수준, 컨텍스트 창 및 호환성 옵션은 공급자를 전환하면 함께 바뀝니다. 나머지는 Codex 전역 설정이며 저장하면 모든 공급자에 적용됩니다. |
| geminiConfig.keyFieldsHint | 地址、Key、模型名和认证方式随供应商切换；其余环境变量和 settings.json 是 Gemini CLI 全局设置，保存后对所有供应商生效。 | 엔드포인트, 키, 모델 이름 및 인증 유형은 공급자를 따릅니다. 다른 환경 변수와 settings.json은 Gemini CLI 전역 설정이며 저장 후 모든 공급자에 적용됩니다. | 엔드포인트, API 키, 모델 이름 및 인증 방식은 공급자를 전환하면 함께 바뀝니다. 나머지 환경 변수와 settings.json은 Gemini CLI 전역 설정이며 저장하면 모든 공급자에 적용됩니다. |
| providerPreset.groupHint.local | 在本机运行的推理服务，先启动服务并下载模型。Key 填占位值即可。 | 이 컴퓨터에서 실행 중인 추론 서버입니다. 서버를 시작하고 먼저 모델을 가져옵니다. 키는 단지 자리 표시자일 뿐입니다. | 이 컴퓨터에서 실행하는 추론 서비스입니다. 먼저 서비스를 시작하고 모델을 다운로드하세요. API 키에는 임의의 자리 표시자 값을 입력하면 됩니다. |
| providerPreset.backToPick | 返回选择预设 | 프리셋으로 돌아가기 | 프리셋 선택으로 돌아가기 |
| providerPreset.matchedVersions | 匹配：{{name}} 等 {{n}} 个版本 | {{name}} 외 {{more}}개와 일치 | {{name}} 외 {{more}}개 버전과 일치 |
| usage.modelsDevAutoSync.configureDescription | 通过搜索和供应商筛选选择需要自动更新的模型，选择结果保存在本地。 | 모델을 검색하고 필터링하여 자동으로 업데이트하세요. 선택 사항은 로컬에 저장됩니다. | 검색과 공급자 필터를 사용하여 가격을 자동 업데이트할 모델을 선택하세요. 선택 결과는 로컬에 저장됩니다. |
| usage.modelsDevAutoSync.selectFiltered | 全选筛选结果（{{count}}） | 필터링됨({{count}}) 선택 | 필터 결과 모두 선택({{count}}) |
| usage.modelsDevAutoSync.neverSynced | 从未同步 | 안 함 | 동기화한 적 없음 |
| usage.detail.speedTooFew | 输出不到 100 token，不算速度 | 출력 토큰이 100개 미만이므로 속도가 없습니다. | 출력이 100토큰 미만이므로 속도를 계산하지 않습니다. |
| usage.detail.speedEstimateTooFew | 输出不到 200 token，不估速度 | 출력 토큰이 200개 미만이므로 추정할 수 없습니다. | 출력이 200토큰 미만이므로 속도를 추정하지 않습니다. |
| usage.detail.noFirstToken | 没有首字计时，不算速度 | 첫 번째 토큰 타이밍이 없으므로 속도가 없습니다. | 첫 토큰 시간 데이터가 없어 속도를 계산하지 않습니다. |
| usageScript.balanceHint | 自动使用供应商的 API Key 查询账户余额 | 공급자의 API 키를 자동으로 사용하여 계정 잔액을 쿼리합니다. | 공급자의 API 키를 자동으로 사용하여 계정 잔액을 조회합니다. |
| usageScript.officialSubscriptionHint | 读取本机 CLI 的 OAuth 凭据，并调用官方接口查询订阅额度。默认关闭，只有启用后才会请求。 | 로컬 CLI OAuth 자격 증명을 읽고 공식 API를 호출하여 구독 할당량을 쿼리합니다. 기본적으로 비활성화되어 있으며 활성화한 후에만 요청합니다. | 로컬 CLI OAuth 자격 증명을 읽고 공식 API를 호출하여 구독 할당량을 조회합니다. 기본적으로 비활성화되어 있으며 활성화한 후에만 요청합니다. |
| usageScript.accessToken | 访问令牌（在个人安全设置里获取） | 액세스 토큰 | 액세스 토큰(개인 보안 설정에서 발급) |
| usageScript.volcengineAkSkHint | 火山用量查询需账号级 AccessKey ID / Secret（与推理 API Key 不同）。请在火山引擎控制台右上角账号菜单 →「API访问密钥」中创建。 | Volcengine 사용 쿼리에는 계정 수준 AccessKey ID/Secret(추론 API 키와 다름)이 필요합니다. 오른쪽 상단 계정 메뉴 → 'API 액세스 키'를 통해 Volcengine 콘솔에서 생성하세요. | Volcengine 사용 조회에는 계정 수준 AccessKey ID/Secret(추론 API 키와 다름)이 필요합니다. 오른쪽 상단 계정 메뉴 → 'API 액세스 키'를 통해 Volcengine 콘솔에서 생성하세요. |
| usageScript.zhipuTeamHint | 智谱团队套餐用量查询需团队 API Key（沿用本供应商凭据）+ 组织 ID + 项目 ID（作为请求头 bigmodel-organization / bigmodel-project）。组织与项目 ID 可在团队管理后台用量页的 URL 中找到。 | Zhipu 팀 계획 사용 쿼리에는 팀 API 키(이 공급자의 자격 증명 재사용) + 조직 ID + 프로젝트 ID(bigmodel-organization / bigmodel-project 요청 헤더로 전송됨)가 필요합니다. 팀 관리 콘솔의 사용 페이지 URL에서 조직 및 프로젝트 ID를 찾으세요. | Zhipu 팀 계획 사용 조회에는 팀 API 키(이 공급자의 자격 증명 재사용) + 조직 ID + 프로젝트 ID(bigmodel-organization / bigmodel-project 요청 헤더로 전송됨)가 필요합니다. 팀 관리 콘솔의 사용 페이지 URL에서 조직 및 프로젝트 ID를 찾으세요. |
| usageScript.queryScript | 查询脚本（JavaScript） | 쿼리 스크립트(JavaScript) | 조회 스크립트(JavaScript) |
| usageScript.extractorHint | 返回对象需包含剩余额度等字段 | 반환 객체에는 나머지 할당량 필드가 포함되어야 합니다. | 반환 객체에는 남은 할당량 등의 필드가 포함되어야 합니다. |
| errors.usage_query_failed | 用量查询失败 | 사용량 쿼리 실패 | 사용량 조회 실패 |
| errors.configLoadFailedMessage | 无法读取配置文件：<br>{{path}}<br><br>错误详情：<br>{{detail}}<br><br>请手动检查 JSON 是否有效，或从同目录的备份文件（如 config.json.bak）恢复。<br><br>应用将退出以便您进行修复。 | 설정 파일을 읽을 수 없습니다.<br>{{path}}<br><br>오류 세부정보:<br>{{detail}}<br><br>JSON가 유효한지 확인하거나 동일한 디렉터리에 있는 백업 파일(예: config.json.bak)에서 복원하세요.<br><br>이 문제를 해결할 수 있도록 앱이 종료됩니다. | 설정 파일을 읽을 수 없습니다:<br>{{path}}<br><br>오류 세부정보:<br>{{detail}}<br><br>JSON이 유효한지 직접 확인하거나 같은 디렉터리의 백업 파일(예: config.json.bak)에서 복원하세요.<br><br>문제를 수정할 수 있도록 앱이 종료됩니다. |
| mcp.form.syncOtherSide | 同步到 {{target}} | {{target}}로 미러링 | {{target}}에 동기화 |
| mcp.form.willOverwriteWarning | 将覆盖 {{target}} 中的同名配置 | {{target}}의 기존 설정을 덮어씁니다. | {{target}}에 있는 같은 이름의 설정을 덮어씁니다. |
| mcp.env | 环境变量 (一行一个，KEY=VALUE) | 환경(한 줄에 하나씩, KEY=VALUE) | 환경 변수(한 줄에 하나씩, KEY=VALUE) |
| mcp.validation.fail | 命令不可用 | 명령을 찾을 수 없습니다 | 명령을 사용할 수 없습니다 |
| mcp.presets.time.description | 时间查询工具，提供当前时间、时区转换、日期计算等功能 | 현재 시간, 시간대 변환, 날짜 계산 기능을 제공하는 시간 쿼리 도구 | 현재 시간, 시간대 변환, 날짜 계산 기능을 제공하는 시간 조회 도구 |
| prompts.searchPlaceholder | 搜索名称、说明或正文 | 이름, 메모, 텍스트 검색 | 이름, 설명 또는 본문 검색 |
| prompts.noSearchResults | 没有名称、说明或正文匹配“{{query}}”的提示词 | 프롬프트 이름, 메모 또는 텍스트가 "{{query}}"와 일치하지 않습니다. | 이름, 설명 또는 본문이 “{{query}}”와 일치하는 프롬프트가 없습니다. |
| prompts.description | 说明 | 메모 | 설명 |
| prompts.helpPiText | 提示库同时只启用一条，它就是 AGENTS.md 的内容。系统提示文件存在就生效，模板在 Pi 里输入 /命令名 调用，这两类都不用启用。 | 한 번에 하나의 라이브러리 프롬프트가 활성화되어 AGENTS.md가 됩니다. 시스템 프롬프트 파일은 존재할 때마다 적용되며 템플릿은 /command를 입력하여 Pi에서 실행됩니다. 둘 다 활성화할 필요가 없습니다. | 프롬프트 라이브러리에서는 한 번에 하나만 활성화되며, 그 내용이 AGENTS.md에 저장됩니다. 시스템 프롬프트 파일은 존재하면 적용되고 템플릿은 Pi에서 /명령어이름을 입력하여 호출합니다. 이 두 유형은 별도로 활성화할 필요가 없습니다. |
| prompts.formDescription | 名称、说明和写进 {{file}} 的正文 | 이름, 메모 및 {{file}}에 작성된 텍스트 | 이름, 설명 및 {{file}}에 저장할 본문 |
| prompts.namePlaceholderHermes | 例如 中文搭档 | 예를 들어 친절한 파트너 | 예: 중국어 파트너 |
| prompts.nameRequiredHermes | 填写名称，例如 中文搭档 | 이름을 입력하세요. 친절한 파트너 | 이름을 입력하세요. 예: 중국어 파트너 |
| prompts.saveAndWritePi | 保存并写入 AGENTS.md | 저장 후 AGENTS.md에 기록 | 저장 후 AGENTS.md에 반영 |
| prompts.toast.enabledPi | 已启用「{{name}}」，已写入 AGENTS.md | "{{name}}"를 활성화하고 AGENTS.md를 작성했습니다. | “{{name}}”을(를) 활성화하고 AGENTS.md에 저장했습니다. |
| prompts.toast.savedActivePi | 已保存「{{name}}」，已写入 AGENTS.md | "{{name}}"를 저장하고 AGENTS.md를 작성했습니다. | “{{name}}”을(를) 저장하고 AGENTS.md에 반영했습니다. |
| workspace.files.memory | 长期记忆和决策记录 | 장기 기억과 결정 | 장기 기억 및 결정 기록 |
| openclaw.removeModel | 移除模型 | 모델 삭제 | 모델 제거 |
| openclaw.agents.primaryModelHint | 从已配置供应商的模型中选择默认模型 | 설정된 공급자 모델 중에서 선택 | 설정된 공급자의 모델 중에서 기본 모델 선택 |
| openclaw.agents.notInList | {{value}} (供应商未配置) | {{value}}(설정되지 않음) | {{value}}(공급자 미설정) |
| hermes.form.models | 模型列表 | 모델 | 모델 목록 |
| hermes.form.removeModel | 移除模型 | 모델 삭제 | 모델 제거 |
| hermes.memory.userDesc | 关于你的信息，会带进 Hermes 的系统提示 | Hermes가 당신에 대해 알고 있는 것; Hermes' 시스템 프롬프트로 들어갑니다. | 사용자에 관한 정보로, Hermes의 시스템 프롬프트에 포함됩니다 |
| hermes.memory.userPlaceholder | 称呼：octocat。<br>§<br>用中文交流，代码注释用英文。 | 이름 : 옥토캣<br>§<br>짧은 답변을 선호합니다. 결론이 먼저입니다. | 호칭: octocat.<br>§<br>중국어로 대화하고 코드 주석은 영어로 작성합니다. |
| skills.repo.addSuccess | 仓库 {{owner}}/{{name}} 已添加，识别到 {{count}} 个技能 | 저장소 {{owner}}/{{name}}를 추가하고 스킬 {{count}}개를 찾았습니다 | 저장소 {{owner}}/{{name}}을(를) 추가하고 스킬 {{count}}개를 찾았습니다 |
| deeplink.grokConfigScopeHint | 只导入 [models] default 指向的那张模型表（显示名、说明、接口类型、窗口等）；地址和 Key 用链接参数，其他模型表不导入。 | [models] default로 명명된 모델 테이블만 가져옵니다(표시 이름, 설명, API 백엔드, 컨텍스트 창 등). 끝점과 키는 링크 매개변수에서 나오며 다른 모델 테이블은 건너뜁니다. | [models]의 default가 가리키는 모델 테이블(표시 이름, 설명, API 유형, 컨텍스트 창 등)만 가져옵니다. 엔드포인트와 API 키는 링크 매개변수를 사용하며 다른 모델 테이블은 가져오지 않습니다. |
| deeplink.mcp.enabledWarning | 导入后将立即写入所有指定应用的配置文件 | 가져온 후 설정은 지정된 모든 앱에 즉시 기록됩니다. | 가져오면 지정한 모든 앱의 설정 파일에 즉시 저장됩니다. |
| deeplink.risk.envHijack | 该配置包含可改变进程加载行为的环境变量（如注入动态库、替换 CA 证书），请确认来源可信。 | 이 설정은 프로세스 로드 코드(예: 라이브러리 삽입 또는 CA 인증서 교체) 방법을 변경하는 환경 변수를 설정합니다. 신뢰할 수 있는 소스에서만 가져오세요. | 이 설정에는 프로세스의 로드 동작을 변경할 수 있는 환경 변수(예: 동적 라이브러리 주입, CA 인증서 교체)가 포함되어 있습니다. 출처를 신뢰할 수 있는지 확인하세요. |
| failover.tooltip.takeoverRequired | 请先接管 {{app}}，再启用故障转移 | 먼저 {{app}}의 요청을 접관한 다음 장애 조치를 켜세요 | 먼저 {{app}}의 요청을 라우팅 서비스에서 관리하도록 설정한 뒤 장애 조치를 켜세요 |
| omo.addProfile | 添加 OMO 配置 | OMO 공급자 추가 | OMO 설정 추가 |
| omo.advancedLabel | 高级参数 | 고급 | 고급 매개변수 |
| omo.advancedJsonInvalid | 高级参数 JSON 无效 | 고급 JSON가 유효하지 않습니다. | 고급 매개변수 JSON이 유효하지 않습니다. |
| omo.runtimeModelsFailedWarning | 读取 OpenCode 运行时模型失败，已仅展示已配置供应商模型。 | OpenCode 런타임 모델을 로드하지 못했습니다. 설정된 공급자만 표시됩니다. | OpenCode 런타임 모델을 읽지 못해 설정된 공급자의 모델만 표시합니다. |
| omo.fillRecommendedNoMatch | 推荐模型在已配置的供应商中未找到匹配（如 {{examples}}） | 설정된 공급자(예: {{examples}})에 권장 모델이 없습니다. | 설정된 공급자에서 권장 모델과 일치하는 모델을 찾지 못했습니다(예: {{examples}}). |
| omo.resetDefault | 重置默认 | 초기화 | 기본값으로 재설정 |
| subscription.short.copilotPremium | 高级请求 | 프리미엄 | 프리미엄 요청 |
| subscription.copilotPremium | 高级请求 | 프리미엄 | 프리미엄 요청 |
| nav.auth | 授权中心 | 계정 | 인증 센터 |
| mode.status.stackValue | {{name}} · 另有 {{count}} 家共 {{models}} 个模型 | {{name}} · 다른 공급자 {{count}}곳의 모델 {{models}}개 | {{name}} · 그 외 공급자 {{count}}곳, 총 모델 {{models}}개 |
| mode.toast.routeTargetChanged | 路由目标已设为 {{provider}}。 | 경로 대상이 {{provider}}로 설정되었습니다. | 라우팅 대상을 {{provider}}(으)로 설정했습니다. |
| mode.toast.routeSwitched | 路由已切换至 {{provider}}，后续新请求将使用该供应商。 | {{provider}}로 경로가 전환되었습니다. 새 요청에서는 이 공급자를 사용합니다. | 라우팅 대상을 {{provider}}(으)로 전환했습니다. 이후 새 요청은 이 공급자를 사용합니다. |
| mode.toast.clientConfigChanged | 客户端配置也已更新；重启 {{app}} 以加载更新后的配置。 | 클라이언트 설정도 변경되었습니다. 업데이트된 설정을 로드하려면 {{app}}를 다시 시작하세요. | 클라이언트 설정도 변경되었습니다. 업데이트된 설정을 로드하려면 {{app}}을(를) 다시 시작하세요. |
| mode.toast.restartHint | 重启 {{app}} 后生效。 | 적용하려면 {{app}}를 다시 시작하세요. | 적용하려면 {{app}}을(를) 다시 시작하세요. |
| mode.dialog.switchTitle | 把 {{app}} 从「{{from}}」切换到「{{to}}」？ | {{app}}를 "{{from}}"에서 "{{to}}"로 전환하시겠습니까? | {{app}}을(를) "{{from}}"에서 "{{to}}"로 전환하시겠습니까? |
| mode.dialog.stackLead | 默认供应商承接不带前缀的请求。 | 기본 공급자는 접두사 없이 요청을 받습니다. | 접두사가 없는 요청은 기본 공급자가 처리합니다. |
| mode.dialog.routeNoteFile | 会改写 {{file}} 里的地址和密钥；真实密钥留在 CC Switch 里，其他设置不动。 | {{file}}의 주소와 키를 다시 씁니다. 실제 키는 CC Switch에 있습니다. 다른 설정은 그대로 유지됩니다. | {{file}}의 주소와 API 키를 변경하여 저장합니다. 실제 API 키는 CC Switch에 보관하며 다른 설정은 변경하지 않습니다. |
| mode.dialog.routeNoteSwitch | 之后在「路由」页签里换供应商，不再改写配置文件。 | 나중에 라우팅 탭에서 공급자를 변경하면 설정 파일이 다시 작성되지 않습니다. | 이후 ‘라우팅’ 탭에서 공급자를 바꿀 때는 설정 파일을 다시 저장하지 않습니다. |
| mode.dialog.desktopRouteNoteModels | Claude Desktop 的模型列表换成路由那家的模型；之后换路由那家会改写配置文件。 | Claude Desktop의 모델 목록은 라우팅된 공급자의 모델이 됩니다. 나중에 라우팅된 공급자를 전환하면 설정 파일이 다시 작성됩니다. | Claude Desktop의 모델 목록을 라우팅 대상 공급자의 모델로 바꿉니다. 이후 라우팅 대상 공급자를 전환하면 설정 파일을 다시 저장합니다. |
| mode.dialog.desktopRouteNoteRestart | {{app}} 只在启动时读配置，确认后要重启 {{app}} 才生效。 | {{app}}는 시작 시 설정만 읽습니다. 확인 후 {{app}}를 다시 시작합니다. | {{app}}은(는) 시작할 때만 설정을 읽으므로 확인 후 {{app}}을(를) 다시 시작해야 적용됩니다. |
| providerCard.action.moveUp | {{name}} 上移一位 | {{name}}를 위로 이동 | {{name}}을(를) 위로 이동 |
| providerCard.action.moveDown | {{name}} 下移一位 | {{name}}를 아래로 이동 | {{name}}을(를) 아래로 이동 |
| providerCard.reason.currentCannotRemove | 正在用的这家不能移除，先启用别家。 | 사용 중인 공급자는 삭제할 수 없습니다. 먼저 다른 공급자를 활성화하세요. | 사용 중인 공급자는 제거할 수 없습니다. 먼저 다른 공급자를 활성화하세요. |
| providerCard.section.addedHelp | 已添加的供应商会同时写进 {{app}} 的配置，在 {{app}} 里选模型即可。 | 추가된 공급자는 모두 {{app}}의 설정에 기록됩니다. {{app}} 내부의 모델을 선택하세요. | 추가된 공급자는 모두 {{app}}의 설정에 함께 저장됩니다. {{app}}에서 모델을 선택하면 됩니다. |
| routingSettings.clientHostHelp | CC Switch 写进客户端配置的代理主机（含 Claude Desktop 的网关地址）。留空时按监听地址推导。客户端无法通过本机回环访问时填写，例如 WSL2（NAT 模式）里的 Claude Desktop 会话：把监听地址设为 0.0.0.0，在这里填 WSL 能访问到的 Windows IP（如 vEthernet (WSL) 网卡的地址），并在防火墙中放行端口。 | 호스트 CC Switch는 클라이언트 설정(Claude Desktop의 게이트웨이 URL 포함)에 기록합니다. 수신 주소에서 파생하려면 비워 두세요. 클라이언트가 루프백을 통해 이 컴퓨터에 연결할 수 없을 때 설정합니다. WSL2 내부의 Claude Desktop 세션(NAT 모드): 수신 주소를 0.0.0.0으로 설정하고 WSL이 연결할 수 있는 Windows IP(예: vEthernet(WSL) 어댑터 주소)를 입력하고 방화벽을 통과하는 포트를 허용합니다. | CC Switch가 클라이언트 설정에 저장하는 프록시 호스트 주소입니다(Claude Desktop의 게이트웨이 주소 포함). 비워 두면 수신 주소를 기준으로 결정합니다. 클라이언트가 이 컴퓨터의 루프백 주소로 연결할 수 없을 때 입력하세요. 예를 들어 WSL2(NAT 모드)의 Claude Desktop 세션에서는 수신 주소를 0.0.0.0으로 설정하고 여기에 WSL에서 접근할 수 있는 Windows IP(예: vEthernet (WSL) 어댑터 주소)를 입력한 뒤 방화벽에서 해당 포트를 허용하세요. |
| appMatrix.pop.failCount | 其中 {{count}} 个写入失败 | {{count}}개 쓰기 실패 | 그중 {{count}}개 저장 실패 |
| appMatrix.toast.partialFail | ，其中 {{count}} 个没有写入，已在列表里标出 | ; {{count}}를 쓸 수 없어 목록에 표시되어 있습니다. |  · 그중 {{count}}개를 저장하지 못해 목록에 표시했습니다. |
| appMatrix.cell.fail | {{name}} · {{app}}：写入失败，点按重试 | {{name}} · {{app}}: 쓰기 실패, 다시 시도하려면 클릭하세요. | {{name}} · {{app}}: 저장 실패, 클릭하여 다시 시도 |
| mcpPage.help | 以这里为准：写进你勾选的应用的配置文件，切换供应商时按这里重写。Claude Desktop、OpenClaw 不支持，所以表格里没有这两列；Pi 需要 1.0 及以上，且不支持 SSE。 | 이 목록은 정보의 원천입니다. 선택한 앱의 설정 파일에 기록되고 공급자를 전환하면 여기에서 다시 작성됩니다. Claude Desktop 및 OpenClaw는 지원되지 않으므로 열이 없습니다. Pi는 1.0 이상이 필요하며 SSE를 지원하지 않습니다. | 여기의 설정을 기준으로 선택한 앱의 설정 파일에 저장하며, 공급자를 전환할 때도 이 설정에 따라 다시 저장합니다. Claude Desktop과 OpenClaw는 지원되지 않아 해당 열이 없습니다. Pi는 1.0 이상이 필요하며 SSE를 지원하지 않습니다. |
| mcpPage.failNoticeTitle | 无法写入 {{app}} 的配置 | {{app}}의 설정을 쓸 수 없습니다. | {{app}}의 설정을 저장할 수 없습니다. |
| mcpPage.rowFail | 写入 {{apps}} 失败 | {{apps}}에 쓰는 데 실패했습니다. | {{apps}}에 저장 실패 |
| mcpPage.rowRetryAria | 重新写入 {{id}} 到 {{apps}} | {{id}}를 {{apps}}에 다시 씁니다. | {{id}}을(를) {{apps}}에 다시 저장 |
| mcpPage.toast.written | 已写入 {{app}} | {{app}}에 작성됨 | {{app}}에 저장했습니다 |
| mcpPage.toast.resynced | 已按这里的开关重新写入 {{count}} 个应用的配置 | 현재 스위치 상태에 따라 앱 {{count}}개의 설정을 다시 기록했습니다 | 여기의 스위치 상태에 따라 앱 {{count}}개의 설정을 다시 저장했습니다. |
| mcpPage.toast.resyncPartial | {{count}} 个应用写入失败：{{apps}} | 앱 {{count}}개에 설정을 기록하지 못했습니다: {{apps}} | 앱 {{count}}개에 설정을 저장하지 못했습니다: {{apps}} |
| mcpPage.drawer.nameHelp | 写进各应用配置文件里的键名。 | 각 앱의 설정 파일에 기록되는 키입니다. | 각 앱의 설정 파일에 저장되는 키 이름입니다. |
| mcpPage.drawer.writeTo | 写入到 | 기록 대상 | 저장 대상 |
| mcpPage.drawer.writeToHelpTitle | 怎么写进各应用 | 앱에 기록되는 방식 | 각 앱에 저장되는 방식 |
| mcpPage.drawer.writeToHelp | 同一份配置原样写进勾选的每个应用；某个应用要不同参数时，另建一条只勾它。MiniMax Code 只替换连接字段，mcp.json 里的其他字段保留。 | 선택한 모든 앱에 동일한 설정이 그대로 기록됩니다. 앱마다 다른 인수가 필요하면 별도 항목을 만드세요. MiniMax Code는 연결 필드만 교체하며 mcp.json의 다른 필드는 유지합니다. | 같은 설정을 선택한 모든 앱에 그대로 저장합니다. 특정 앱에 다른 매개변수가 필요하면 별도 항목을 만들고 해당 앱만 선택하세요. MiniMax Code에서는 연결 필드만 교체하며 mcp.json의 나머지 필드는 유지합니다. |
| mcpPage.drawer.displayNameHelp | 只在 CC Switch 里显示，不写进应用的配置。 | CC Switch에만 표시되며 앱 설정에는 기록되지 않습니다. | CC Switch에만 표시되며 앱 설정에는 저장하지 않습니다. |
| skillsPage.installTo.many | {{first}} 等 {{count}} 个 | {{first}} 외 {{count}}개 | {{first}} 등 {{count}}개 |
| newLayoutNotice.body | CC Switch 这一版重新设计了界面，常用功能的位置有变化：<br>• 模式移到了每个应用页的顶部<br>• 用量统计和授权中心移到了左侧边栏<br>想了解全部变化，可以看看这一版的更新说明。 | 이번 버전에서 인터페이스를 새롭게 디자인하여 일부 항목의 위치가 바뀌었습니다:<br>• 모드는 각 앱 페이지 상단에 있습니다<br>• 사용량과 계정은 사이드바에 있습니다<br>전체 변경 사항은 릴리스 노트를 확인하세요. | 이번 버전에서 CC Switch의 인터페이스를 새롭게 디자인하여 자주 사용하는 기능의 위치가 바뀌었습니다:<br>• 연결 모드는 각 앱 페이지 상단으로 이동했습니다<br>• 사용량 통계와 인증 센터는 왼쪽 사이드바로 이동했습니다<br>전체 변경 사항은 이번 버전의 릴리스 노트를 확인하세요. |
| authCenter.helpTitle | 授权中心是什么 | 계정이란? | 인증 센터란? |
| authCenter.needsReauth | 需要重新登录 | 로그인 필요 | 다시 로그인 필요 |
| authCenter.agy.switchedWhileRunning | 已切换。检测到 agy 正在运行：已打开的 agy 仍用原账号，还可能把原账号写回去，请退出后重新打开。 | 전환했습니다. agy가 실행 중이므로 기존 세션은 이전 계정을 계속 사용하며 해당 계정을 다시 기록할 수 있습니다. agy를 종료한 후 다시 실행하세요. | 전환했습니다. 실행 중인 agy가 감지되었습니다. 이미 실행 중인 agy는 기존 계정을 계속 사용하며 기존 계정 정보를 로그인 설정에 다시 저장할 수도 있습니다. agy를 모두 종료한 뒤 다시 실행하세요. |
| kimi.oauth.description | 可添加多个 Kimi 编程套餐账号，各自保存凭据和供应商。在此管理登录，再选择账号使用其官方模型。 | 별도의 자격 증명과 공급자를 사용하는 Kimi 코딩 요금제 계정을 추가합니다. 여기에서 로그인을 관리한 다음 계정을 선택하여 공식 모델을 사용하세요. | Kimi 코딩 요금제 계정을 여러 개 추가하고 각 계정의 자격 증명과 공급자를 별도로 저장할 수 있습니다. 여기에서 로그인을 관리한 다음 계정을 선택하여 해당 계정의 공식 모델을 사용하세요. |
| kimi.oauth.dismissAccount | 移出列表 | 목록에서 숨기기 | 목록에서 제거 |
| kimi.oauth.dismissConfirm | 把 {{name}} 移出列表？这是 Kimi Code 自己的登录，CC Switch 不会替它退出登录，凭据和模型都会保留；如需退出，请在 Kimi Code 里运行 /logout。之后重新登录会让它回到列表。 | {{name}}을(를) 목록에서 숨기시겠습니까? Kimi Code 자체 로그인 계정이므로 CC Switch는 로그아웃하지 않으며 자격 증명과 모델을 유지합니다. 로그아웃하려면 Kimi Code에서 /logout을 실행하세요. 다시 로그인하면 목록에 표시됩니다. | {{name}}을(를) 목록에서 제거하시겠습니까? Kimi Code 자체 로그인 계정이므로 CC Switch에서 대신 로그아웃하지 않으며 자격 증명과 모델도 유지됩니다. 로그아웃하려면 Kimi Code에서 /logout을 실행하세요. 이후 다시 로그인하면 목록에 다시 표시됩니다. |
| kimi.oauth.primaryHidden | Kimi Code 自己的登录已移出列表，重新登录同一账号即可找回 | Kimi Code 자체 로그인 계정을 목록에서 숨겼습니다. 같은 계정으로 로그인하면 다시 표시됩니다 | Kimi Code 자체 로그인 계정을 목록에서 제거했습니다. 같은 계정으로 다시 로그인하면 되찾을 수 있습니다. |
| kimi.modelSelectionHint | 点击供应商卡片的切换按钮选择默认供应商；需要指定其他模型时，在 Kimi Code 中使用 /model。 | 공급자 카드의 전환 버튼으로 선택하세요. 다른 모델을 선택하려면 Kimi Code에서 /model을 사용하세요. | 공급자 카드의 전환 버튼을 눌러 기본 공급자를 선택하세요. 다른 모델을 지정하려면 Kimi Code에서 /model을 사용하세요. |
| native.tray.rs.problem_attach_failed | {app}：上次的{mode}没能接上，已回到直连 | {app}: 시작 시 {mode}에 다시 연결하지 못해 직접 연결로 돌아갔습니다 | {app}: 이전 {mode} 연결에 실패하여 직접 연결로 돌아갔습니다 |
| native.tray.rs.tier_premium | 高级请求 | Premium | 프리미엄 요청 |
