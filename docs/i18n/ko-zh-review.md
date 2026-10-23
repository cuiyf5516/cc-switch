# 韩语逐条审查：中韩对照

2026-10-24：已以中文为主要语义来源重新逐项检查全部条目；英文仅辅助核对代码与占位符。

基于 upstream/main `e5b04221`。已由 LLM 逐条审查 4292 条界面文案和 71 条原生文案，共修订 1579 条，其余保留。尚未进行韩语母语者审校或桌面布局验收。

| 翻译键 | 中文 | 审查后韩文 | 英文原文 | 审查结果 |
|---|---|---|---|---|
| app.title | CC Switch | CC Switch | CC Switch | 保留 |
| app.description | Claude Code / Codex / Gemini CLI 全方位辅助工具 | Claude Code / Codex / Gemini CLI용 종합 지원 도구 | All-in-One Assistant for Claude Code, Codex & Gemini CLI | 已修订 |
| common.unsavedLeaveTitle | 有未保存的修改 | 저장되지 않은 변경 사항 | Unsaved changes | 已修订 |
| common.unsavedLeaveMessage | 离开后，当前编辑页里的修改不会保存。 | 이 페이지를 나가면 변경 사항이 저장되지 않습니다. | If you leave, the changes on this editor page will not be saved. | 已修订 |
| common.unsavedLeaveConfirm | 放弃修改并离开 | 저장하지 않고 나가기 | Discard and leave | 已修订 |
| common.unsavedLeaveCancel | 继续编辑 | 계속 편집 | Keep editing | 保留 |
| common.add | 添加 | 추가 | Add | 保留 |
| common.edit | 编辑 | 편집 | Edit | 保留 |
| common.delete | 删除 | 삭제 | Delete | 保留 |
| common.save | 保存 | 저장 | Save | 保留 |
| common.saving | 保存中... | 저장 중... | Saving... | 保留 |
| common.cancel | 取消 | 취소 | Cancel | 保留 |
| common.confirm | 确定 | 확인 | Confirm | 保留 |
| common.close | 关闭 | 닫기 | Close | 保留 |
| common.done | 完成 | 완료 | Done | 保留 |
| common.settings | 设置 | 설정 | Settings | 保留 |
| common.about | 关于 | 정보 | About | 保留 |
| common.version | 版本 | 버전 | Version | 保留 |
| common.loading | 加载中... | 불러오는 중... | Loading... | 保留 |
| common.notInstalled | 未安装 | 설치되지 않음 | Not installed | 保留 |
| common.success | 成功 | 성공 | Success | 保留 |
| common.error | 错误 | 오류 | Error | 保留 |
| common.unknown | 未知 | 알 수 없음 | Unknown | 保留 |
| common.enterValidValue | 请输入有效的内容 | 유효한 값을 입력하세요. | Please enter a valid value | 保留 |
| common.clear | 清除 | 지우기 | Clear | 保留 |
| common.format | 格式化 | 포맷팅 | Format | 已修订 |
| common.formatSuccess | 格式化成功 | 포맷팅이 완료되었습니다 | Formatted successfully | 已修订 |
| common.formatError | 格式化失败：{{error}} | 포맷팅 실패: {{error}} | Format failed: {{error}} | 已修订 |
| common.copy | 复制 | 복사 | Copy | 保留 |
| common.view | 查看 | 보기 | View | 保留 |
| common.back | 返回 | 뒤로 | Back | 保留 |
| common.refresh | 刷新 | 새로 고침 | Refresh | 保留 |
| common.refreshing | 刷新中... | 새로 고치는 중... | Refreshing... | 保留 |
| common.import | 导入 | 가져오기 | Import | 保留 |
| common.all | 全部 | 모두 | All | 保留 |
| common.search | 查询 | 검색 | Search | 保留 |
| common.enableAllForApp | 为 {{app}} 全部启用 | {{app}}에서 모두 활성화 | Enable all for {{app}} | 已修订 |
| common.disableAllForApp | 为 {{app}} 全部停用 | {{app}}에서 모두 비활성화 | Disable all for {{app}} | 已修订 |
| common.bulkToggleFailed | 有 {{count}} 项更新失败 | 항목 {{count}}개를 업데이트하지 못했습니다 | Failed to update {{count}} item(s) | 已修订 |
| common.reset | 重置 | 초기화 | Reset | 保留 |
| common.actions | 操作 | 작업 | Actions | 保留 |
| common.deleting | 删除中... | 삭제 중... | Deleting... | 保留 |
| common.auto | 自动 | 자동 | Auto | 保留 |
| common.enabled | 已开启 | 활성화됨 | Enabled | 保留 |
| common.notSet | 未设置 | 설정되지 않음 | Not Set | 保留 |
| common.collapse | 收起 | 접기 | Collapse | 保留 |
| common.more | 更多 | 더 보기 | More | 保留 |
| common.retry | 重试 | 다시 시도 | Retry | 保留 |
| common.required | 必填 | 필수 | required | 保留 |
| firstRunNotice.title | 欢迎使用 CC Switch | CC Switch에 오신 것을 환영합니다 | Welcome to CC Switch | 保留 |
| firstRunNotice.bodyDefault | CC Switch 可以帮你在 Claude Code / Codex / Gemini CLI 的多个供应商之间一键切换。如果你之前已经配置过这些工具，CC Switch 会自动把现有设置保存为名为 “default” 的供应商，保证你的配置不会丢失。 | CC Switch를 사용하면 Claude Code / Codex / Gemini CLI의 여러 공급자 간에 클릭 한 번으로 전환할 수 있습니다. 이러한 도구가 이미 설정되어 있다면 CC Switch가 기존 설정을 "default"라는 공급자로 자동 저장하므로 기존 설정이 손실되지 않습니다. | CC Switch lets you switch between multiple Claude Code / Codex / Gemini CLI providers with a single click. If you already had these tools configured, CC Switch has saved your existing setup as a provider named “default” so none of your previous configuration is lost. | 已修订 |
| firstRunNotice.bodyOfficial | 列表里还预置了 “官方（Official）” 供应商，随时点一下即可切回官方默认配置。切换前 CC Switch 会自动把当前配置备份回 default，可以放心来回切。CC Switch 就是这样工作的 😊 | 목록에는 ‘공식(Official)’ 공급자도 미리 등록되어 있습니다. 언제든지 선택하여 공식 기본 설정으로 돌아갈 수 있습니다. CC Switch는 전환 전에 현재 설정을 ‘default’에 자동으로 백업하므로 안심하고 전환할 수 있습니다. CC Switch는 이렇게 작동합니다 😊 | An “Official” preset is also included in the list — click it any time you want to switch back to the official default. CC Switch automatically backs up your current config to “default” before switching, so you can move back and forth freely. That's how CC Switch works 😊 | 已修订 |
| firstRunNotice.confirm | 我知道了 | 확인했습니다 | Got it | 已修订 |
| apiKeyInput.placeholder | 请输入API Key | API 키를 입력하세요 | Enter API Key | 保留 |
| apiKeyInput.show | 显示API Key | API 키 표시 | Show API Key | 保留 |
| apiKeyInput.hide | 隐藏API Key | API 키 숨기기 | Hide API Key | 保留 |
| jsonEditor.mustBeObject | 配置必须是JSON对象，不能是数组或其他类型 | 설정은 배열이나 다른 유형이 아닌 JSON 객체여야 합니다. | Configuration must be a JSON object, not an array or other type | 已修订 |
| jsonEditor.invalidJson | JSON格式错误 | 잘못된 JSON 형식 | Invalid JSON format | 保留 |
| claudeConfig.configLabel | Claude Code 配置 (JSON) * | Claude Code 설정 (JSON) * | Claude Code settings.json (JSON) * | 已修订 |
| claudeConfig.fullSettingsHint | 完整的 Claude Code settings.json 配置内容 | Claude Code settings.json 파일의 전체 설정 내용 | Full Claude Code settings.json content | 已修订 |
| claudeConfig.hideAttribution | 隐藏 AI 署名 | AI 기여 표시 숨기기 | Hide AI Attribution | 已修订 |
| claudeConfig.hideAttributionHelp | Claude Code 生成的提交和 PR 不再带 Co-Authored-By 署名和会话链接。全局设置，对所有供应商生效。 | Claude Code가 생성한 커밋과 PR에서 Co-Authored-By 표시와 세션 링크를 제외합니다. 모든 공급자에 적용되는 전역 설정입니다. | Commits and PRs created by Claude Code no longer carry the Co-Authored-By trailer or the session link. Global: applies to every provider. | 已修订 |
| claudeConfig.enableToolSearch | 启用 Tool Search | Tool Search 활성화 | Enable Tool Search | 已修订 |
| claudeConfig.enableToolSearchHelp | MCP 工具多时按需加载工具定义，节省上下文。第三方地址默认关闭，上游支持 tool_reference 才能开。随供应商切换。 | 컨텍스트 사용량을 줄이기 위해 필요할 때 MCP 도구 정의를 불러옵니다. 타사 엔드포인트에서는 기본으로 꺼져 있습니다. 업스트림이 tool_reference를 지원할 때만 켜세요. 공급자를 전환하면 이 설정도 함께 바뀝니다. | Loads MCP tool definitions on demand to save context. Off by default on third-party endpoints; enable it only if the upstream supports tool_reference. Switches with the provider. | 已修订 |
| claudeConfig.disableAutoUpgrade | 禁用自动升级 | 자동 업그레이드 비활성화 | Disable Auto-Upgrade | 保留 |
| claudeConfig.disableAutoUpgradeHelp | Claude Code 保持当前版本，不再自动更新，需要时手动运行 claude update。全局设置。 | 자동 업데이트를 끄고 Claude Code를 현재 버전으로 유지합니다. 필요할 때 claude update를 직접 실행하세요. 전역 설정입니다. | Keeps Claude Code on its current version instead of updating automatically; run claude update yourself when needed. Global. | 已修订 |
| claudeConfig.disableArtifact | 禁用 Artifact 工具 | Artifact Tool 비활성화 | Disable Artifact Tool | 已修订 |
| claudeConfig.disableArtifactHelp | 不把 Artifact 工具发给模型。部分第三方网关会因它的 schema 对每个请求报 400。随供应商切换。 | 요청에서 Artifact Tool을 제외합니다. 일부 타사 게이트웨이는 이 도구의 스키마를 거부하여 모든 요청에 400 오류를 반환합니다. 공급자를 전환하면 이 설정도 함께 바뀝니다. | Leaves the Artifact tool out of requests. Some third-party gateways reject its schema and return 400 on every request. Switches with the provider. | 已修订 |
| claudeConfig.disableAutoModeServer | 关闭 auto mode 服务端检查 | 자동 모드 서버 검사 비활성화 | Disable Auto Mode Server Checks | 保留 |
| claudeConfig.disableAutoModeServerHelp | 网关不支持服务端检查，auto mode 每个会话会先停下提示一次「不符合条件」，回车后改用本机检查。勾选后直接用本机检查，不再提示。官方端点不要勾选。 | 게이트웨이는 서버 측 검사를 실행할 수 없어 자동 모드가 세션마다 한 번씩 ‘사용 자격 없음’ 알림과 함께 일시 중지됩니다. Enter를 누르면 로컬 검사로 전환됩니다. 이 옵션을 켜면 알림 없이 바로 로컬 검사를 사용합니다. 공식 엔드포인트에서는 꺼 두세요. | Gateways can't run the server-side check, so auto mode pauses once per session with a "not eligible" notice, then falls back to the local check after you press Enter. Checked, it uses the local check right away with no notice. Leave it unchecked on official endpoints. | 已修订 |
| claudeConfig.keyFieldsHint | 地址、Key、模型、上下文窗口和兼容开关随供应商切换；其余字段是 Claude Code 全局设置，保存后对所有供应商生效。 | 엔드포인트, API 키, 모델, 컨텍스트 창 및 호환성 옵션은 공급자를 전환하면 함께 바뀝니다. 나머지 필드는 Claude Code 전역 설정이며 저장하면 모든 공급자에 적용됩니다. | Endpoint, key, models, context window and compatibility switches follow the provider; everything else is a global Claude Code setting and applies to every provider once saved. | 已修订 |
| claudeConfig.inactiveFieldsHint | 这些是旧版存进卡里的设置，现在切换不会写出去。点一下加入上方，保存后对所有供应商生效。 | 이전 버전에서 이 공급자에 저장한 설정으로, 이제 공급자를 전환해도 적용되지 않습니다. 항목을 선택하면 위의 전역 설정에 추가됩니다. 저장한 후에는 모든 공급자에 적용됩니다. | Saved in this provider by an older version; switching no longer applies them. Click one to add it above; after saving it applies to every provider. | 已修订 |
| claudeConfig.addToGlobalSettings | 加入全局设置 | 전역 설정에 추가 | Add to global settings | 保留 |
| header.viewOnGithub | 在 GitHub 上查看 | GitHub에서 보기 | View on GitHub | 保留 |
| header.toggleDarkMode | 切换到暗色模式 | 다크 모드로 전환 | Switch to Dark Mode | 保留 |
| header.toggleLightMode | 切换到亮色模式 | 라이트 모드로 전환 | Switch to Light Mode | 已修订 |
| header.addProvider | 添加供应商 | 공급자 추가 | Add Provider | 已修订 |
| header.switchToChinese | 切换到中文 | 중국어로 전환 | Switch to Chinese | 保留 |
| header.switchToEnglish | 切换到英文 | 영어로 전환 | Switch to English | 保留 |
| header.enterEditMode | 进入编辑模式 | 편집 모드로 들어가기 | Enter Edit Mode | 保留 |
| header.exitEditMode | 退出编辑模式 | 편집 모드 종료 | Exit Edit Mode | 保留 |
| header.windowMinimize | 最小化窗口 | 창 최소화 | Minimize window | 保留 |
| header.windowMaximize | 最大化窗口 | 창 최대화 | Maximize window | 保留 |
| header.windowRestore | 还原窗口 | 창 이전 크기로 복원 | Restore window | 已修订 |
| header.windowClose | 关闭窗口 | 창 닫기 | Close window | 保留 |
| provider.connectivityCheck | 检测连通 | 연결 확인 | Connectivity check | 保留 |
| provider.tabProvider | 供应商 | 공급자 | Provider | 已修订 |
| provider.tabUniversal | 统一供应商 | 범용 공급자 | Universal | 已修订 |
| provider.noProviders | 还没有供应商 | 아직 공급자가 없습니다. | No providers yet | 已修订 |
| provider.noProvidersDescription | 如果你已有配置，请点击"导入当前配置"，所有数据将安全保存在 default 供应商中 | 이미 설정이 있다면 "현재 설정 가져오기"를 클릭하세요. 모든 데이터는 "default" 공급자에 안전하게 저장됩니다. | If you already have a config, click "Import Current Config" — all data will be safely saved in a default provider | 已修订 |
| provider.noProvidersDescriptionKeyFields | 切换供应商只替换 Key、请求地址和模型，插件等其他设置保留在配置文件里，对所有供应商生效 | 공급자 전환은 키, 엔드포인트 및 모델만 대체합니다. 플러그인 및 기타 설정은 설정 파일에 유지되며 모든 공급자에 적용됩니다. | Switching providers only replaces the key, endpoint and model; plugins and other settings stay in the config file and apply to every provider | 已修订 |
| provider.importCurrent | 导入当前配置 | 현재 설정 가져오기 | Import Current Config | 已修订 |
| provider.importFromClaude | 将 Claude Code 中已有的供应商导入 | Claude Code에서 기존 공급자 가져오기 | Import existing providers from Claude Code | 已修订 |
| provider.importCurrentDescription | 将当前正在使用的配置导入为默认供应商 | 현재 적용 중인 설정을 기본 공급자로 가져오기 | Import current live config as default provider | 已修订 |
| provider.currentlyUsing | 当前使用 | 현재 사용 중 | Currently Using | 保留 |
| provider.enable | 启用 | 활성화 | Enable | 保留 |
| provider.inUse | 使用中 | 사용 중 | In Use | 保留 |
| provider.needsRouting | 需要路由 | 라우팅 필요 | Needs Routing | 保留 |
| provider.directProvider | 直连 | 직접 연결 | Direct | 保留 |
| provider.directProviderHint | 退出路由后恢复为这个供应商 | 라우팅 모드를 종료하면 이 공급자로 다시 전환됩니다. | Leaving routing mode switches back to this provider | 已修订 |
| provider.stackBadge | 聚合 | 통합 | Aggregation | 保留 |
| provider.stackBadgeHint | 在 {{client}} 的模型选择器里选择：{{models}} | {{client}}의 모델 선택 메뉴에서 선택: {{models}} | Pick in {{client}}'s model picker: {{models}} | 已修订 |
| provider.stackBadgeNoModels | 这家没有配置模型，不会出现在模型选择器里 | 이 공급자에는 설정된 모델이 없어 해당 모델이 모델 선택 메뉴에 표시되지 않습니다. | This provider has no models configured, so nothing shows up in the model picker | 已修订 |
| provider.stackSaved | 已保存，重启 {{client}} 后生效 | 저장되었습니다. {{client}}을(를) 다시 시작하면 적용됩니다. | Saved. Restart {{client}} to apply | 已修订 |
| provider.stackSavedLive | 已保存，{{client}} 里立即生效 | 저장되었습니다. {{client}}에서 즉시 적용됩니다. | Saved. Takes effect in {{client}} right away | 保留 |
| provider.stackReselectHint | CC Switch 每次改写客户端配置后，如果模型选择器里选的是聚合的模型，需要重新选一次 | CC Switch가 클라이언트 설정을 변경할 때마다, 모델 선택 메뉴에서 통합 모델을 선택해 둔 경우 해당 모델을 다시 선택해야 합니다. | Whenever CC Switch rewrites the client config, pick the aggregated model again in the model picker | 已修订 |
| provider.stackPartial | 已部分写入，将在下次操作或重启 CC Switch 时补完 | 설정이 일부만 저장되었습니다. 다음 작업을 수행하거나 CC Switch를 다시 시작하면 나머지 설정이 저장됩니다. | Partly written; it will be finished on the next change or when CC Switch restarts | 已修订 |
| provider.stackFailed | 聚合的模型保存失败：{{error}} | 통합된 모델 저장 실패: {{error}} | Failed to save aggregated models: {{error}} | 已修订 |
| provider.stackDefaultCannotRemove | 默认供应商不能移除，请先把别的供应商设为默认 | 기본 공급자는 제거할 수 없습니다. 먼저 다른 공급자를 기본값으로 설정하세요 | The default provider cannot be removed; set another provider as the default first | 已修订 |
| provider.stackDefaultHint | 它是默认供应商：列表里的第一个模型负责 Claude Code 启动和后台任务 | 기본 공급자입니다. 이 공급자의 모델 목록에서 첫 번째 모델이 Claude Code의 시작 및 백그라운드 작업을 처리합니다. | This is the default provider: the first model in its list handles Claude Code's startup and background tasks | 已修订 |
| provider.officialModelsBundled | 官方模型列表暂未取到，暂用 Codex 内置列表，可能缺少账号专属模型 | 공식 모델 목록을 아직 가져오지 못해 임시로 Codex 내장 목록을 사용합니다. 해당 계정에서만 제공되는 모델이 누락될 수 있습니다. | The official model list isn't available yet, so Codex's built-in list is used for now and account-specific models may be missing | 已修订 |
| provider.officialModelsUnavailable | 聚合的模型暂不可用：读取不到 Codex 模型列表 | 현재 통합된 모델을 사용할 수 없습니다. Codex 모델 목록을 읽을 수 없습니다 | Aggregated models are unavailable for now: the Codex model list can't be read | 已修订 |
| provider.officialModelsOutdated | 本机 Codex 版本过旧，拿不到完整的官方模型列表：请把 Codex（包括命令行）升级到最新版 | 이 컴퓨터에 설치된 Codex 버전이 오래되어 전체 공식 모델 목록을 가져올 수 없습니다. Codex(CLI 포함)를 최신 버전으로 업데이트하세요. | Codex on this computer is too old to get the full official model list: update Codex (including the CLI) to the latest version | 已修订 |
| provider.officialModelsReason.noLogin | 官方列表：Codex 没有可用的 ChatGPT 登录，请在 Codex 里用 ChatGPT 账号登录 | 공식 목록: Codex에는 사용 가능한 ChatGPT 로그인이 없습니다. ChatGPT 계정으로 Codex에 로그인하세요. | Official list: Codex has no usable ChatGPT login. Sign in to Codex with a ChatGPT account | 保留 |
| provider.officialModelsReason.loginStale | 官方列表：Codex 的登录超过 8 天没有刷新，打开 Codex 用一下即可自动刷新 | 공식 목록: Codex 로그인이 8일 이상 새로 고쳐지지 않았습니다. Codex를 한 번 사용하면 자동으로 새로 고쳐집니다. | Official list: the Codex login hasn't been refreshed for over 8 days. Use Codex once and it refreshes automatically | 保留 |
| provider.officialModelsReason.loginIncomplete | 官方列表：Codex 的登录信息不完整（缺少工作区或用户 ID），请在 Codex 里重新登录 | 공식 목록: Codex 로그인이 불완전합니다(작업공간 또는 사용자 ID가 누락됨). Codex에 다시 로그인하세요. | Official list: the Codex login is incomplete (missing the workspace or user ID). Sign in to Codex again | 保留 |
| provider.officialModelsReason.noVersion | 官方列表：读不到本机 Codex 的版本，用 Codex 开始一次对话后会自动重试 | 공식 목록: 이 컴퓨터에서 Codex 버전을 읽을 수 없습니다. Codex에서 대화를 시작한 후 다시 시도합니다. | Official list: can't read the Codex version on this computer. It will retry after you start a conversation in Codex | 保留 |
| provider.officialModelsReason.fetchFailed | 官方列表：联网获取失败，会每 15 分钟自动重试（详情见日志） | 공식 목록: 가져오기에 실패하여 15분마다 다시 시도합니다 (자세한 내용은 로그 참조) | Official list: fetching it failed; retrying every 15 minutes (see the log for details) | 已修订 |
| provider.officialModelsReason.invalidList | 官方列表：返回的数据不完整（详情见日志） | 공식 목록: 반환된 데이터가 불완전합니다(자세한 내용은 로그 참조). | Official list: the returned data is incomplete (see the log for details) | 保留 |
| provider.officialModelsReason.noCli | Codex 自带列表：本机找不到 Codex 命令行 | Codex 내장 목록: 이 컴퓨터에서 Codex CLI를 찾을 수 없습니다. | Codex built-in list: no Codex CLI found on this computer | 保留 |
| provider.officialModelsReason.cliFailed | Codex 自带列表：Codex 命令行没能输出模型列表（详情见日志） | Codex 내장 목록: Codex CLI가 모델 목록을 출력하지 않았습니다(자세한 내용은 로그 참조). | Codex built-in list: the Codex CLI didn't output a model list (see the log for details) | 保留 |
| provider.officialModelsReason.nothingUsable | Codex 自带列表：里面没有能用的模型，请把 Codex 升级到最新版 | Codex 내장 목록: 사용 가능한 모델이 없습니다. Codex를 최신 버전으로 업데이트하세요 | Codex built-in list: it has no usable models. Update Codex to the latest version | 保留 |
| provider.routeOwnsCatalog | 聚合的模型不会出现在 Codex 里：路由供应商使用自己的模型目录文件（model_catalog_json） | 라우팅된 공급자가 자체 모델 카탈로그 파일(model_catalog_json)을 사용하므로 통합된 모델이 Codex에 표시되지 않습니다 | Aggregated models won't show up in Codex: the routed provider uses its own model catalog file (model_catalog_json) | 已修订 |
| provider.adoptCatalog | 改用 CC Switch 的模型目录 | CC Switch 모델 카탈로그 사용 | Use CC Switch's model catalog | 已修订 |
| provider.adoptCatalogDone | 已改用 CC Switch 的模型目录，重启 Codex 后生效 | 이제 CC Switch의 모델 카탈로그를 사용하고 있습니다. 적용하려면 Codex를 다시 시작하세요. | Now using CC Switch's model catalog. Restart Codex to apply | 保留 |
| provider.adoptCatalogFailed | 改用 CC Switch 的模型目录失败：{{error}} | CC Switch의 모델 카탈로그로 전환하지 못했습니다: {{error}} | Failed to switch to CC Switch's model catalog: {{error}} | 保留 |
| provider.noRoutingSupport | 不支持路由 | 라우팅 지원 없음 | No Routing Support | 保留 |
| provider.blockedByProxyHint | 路由模式下不能切换到官方供应商 | 라우팅 모드에서는 공식 공급자로 전환할 수 없습니다. | Can't switch to an official provider in Routing mode | 已修订 |
| provider.editProvider | 编辑供应商 | 공급자 편집 | Edit Provider | 已修订 |
| provider.editProviderHint | 更新配置后将立即应用到当前供应商。 | 업데이트 후 즉시 현재 공급자에 설정이 적용됩니다. | Configuration will be applied to the current provider immediately after update. | 已修订 |
| provider.deleteProvider | 删除供应商 | 공급자 삭제 | Delete Provider | 已修订 |
| provider.addNewProvider | 添加供应商 | 공급자 추가 | Add provider | 已修订 |
| provider.addFooterHint | 💡 选择预设后，请在下方填写 API Key 等字段 | 💡 프리셋을 선택한 후 아래 필드를 입력하세요(예: API 키) | 💡 After choosing a preset, fill in the fields below (e.g. API Key) | 保留 |
| provider.addClaudeProvider | 添加 Claude Code 供应商 | Claude Code 공급자 추가 | Add Claude Code Provider | 已修订 |
| provider.addCodexProvider | 添加 Codex 供应商 | Codex 공급자 추가 | Add Codex Provider | 已修订 |
| provider.addGeminiProvider | 添加 Gemini 供应商 | Gemini 공급자 추가 | Add Gemini Provider | 已修订 |
| provider.addOpenCodeProvider | 添加 OpenCode 供应商 | OpenCode 공급자 추가 | Add OpenCode Provider | 已修订 |
| provider.addToConfig | 添加 | 추가 | Add | 已修订 |
| provider.removeFromConfig | 移除 | 제거 | Remove | 保留 |
| provider.setAsDefault | 设为默认 | 기본값 설정 | Set Default | 保留 |
| provider.isDefault | 当前默认 | 현재 기본값 | Current Default | 保留 |
| provider.inConfig | 已添加 | 추가됨 | Added | 保留 |
| provider.addProviderHint | 填写信息后即可在列表中快速切换供应商。 | 정보를 입력하면 목록에서 공급자를 빠르게 전환할 수 있습니다. | Fill in the information to quickly switch providers in the list. | 已修订 |
| provider.editClaudeProvider | 编辑 Claude Code 供应商 | Claude Code 공급자 편집 | Edit Claude Code Provider | 已修订 |
| provider.editCodexProvider | 编辑 Codex 供应商 | Codex 공급자 편집 | Edit Codex Provider | 已修订 |
| provider.configError | 配置错误 | 설정 오류 | Configuration Error | 已修订 |
| provider.notConfigured | 未配置官网地址 | 공식 웹사이트가 설정되지 않았습니다 | Not configured for official website | 已修订 |
| provider.applyToClaudePlugin | 应用到 Claude 插件 | Claude 플러그인에 적용 | Apply to Claude plugin | 保留 |
| provider.removeFromClaudePlugin | 从 Claude 插件移除 | Claude 플러그인에서 제거 | Remove from Claude plugin | 保留 |
| provider.dragToReorder | 拖拽以重新排序 | 드래그하여 재정렬하세요. | Drag to reorder | 保留 |
| provider.dragHandle | 拖拽排序 | 드래그하여 재정렬하세요. | Drag to reorder | 保留 |
| provider.searchPlaceholder | 按名称/备注/网址搜索供应商... | 이름, 메모, URL 검색... | Search name, notes, or URL... | 保留 |
| provider.searchAriaLabel | 搜索供应商 | 공급자 검색 | Search providers | 已修订 |
| provider.searchScopeHint | 根据名称、备注、官网和请求地址匹配结果。 | 공급자 이름, 메모, 웹사이트 및 API 주소와 일치합니다. | Matches provider name, notes, website, and API address. | 已修订 |
| provider.searchButtonTip | 搜索供应商（{{shortcut}}） | 공급자 검색 ({{shortcut}}) | Search providers ({{shortcut}}) | 已修订 |
| provider.searchCloseHint | 按 Esc 关闭 | 닫으려면 Esc를 누르세요. | Press Esc to close | 保留 |
| provider.searchCloseAriaLabel | 关闭供应商搜索 | 공급자 검색 닫기 | Close provider search | 已修订 |
| provider.noSearchResults | 没有符合搜索条件的供应商。 | 검색어와 일치하는 공급자가 없습니다. | No providers match your search. | 已修订 |
| provider.duplicate | 复制 | 복제 | Duplicate | 已修订 |
| provider.sortUpdateFailed | 排序更新失败 | 정렬 순서를 업데이트하지 못했습니다. | Failed to update sort order | 保留 |
| provider.configureUsage | 配置用量查询 | 사용량 조회 설정 | Configure usage query | 已修订 |
| provider.managedByHermes | Hermes 托管 | Hermes에서 관리 | Hermes Managed | 已修订 |
| provider.managedByHermesHint | 该条目定义在 Hermes 的 providers: dict，请在 Hermes Web UI 中编辑或删除。 | Hermes의 providers: 사전에 정의된 항목입니다. Hermes 웹 UI에서 편집하거나 제거하세요. | Defined in Hermes' providers: dict. Edit or remove it via Hermes Web UI. | 已修订 |
| provider.openTerminal | 打开终端 | 터미널 열기 | Open Terminal | 保留 |
| provider.openTerminalWithProvider | 使用此供应商打开终端 | 이 공급자를 사용하여 터미널 열기 | Open Terminal with This Provider | 已修订 |
| provider.terminalOpened | 终端已打开 | 터미널을 열었습니다 | Terminal opened | 已修订 |
| provider.terminalOpenFailed | 打开终端失败 | 터미널을 열지 못했습니다. | Failed to open terminal | 保留 |
| provider.openTerminalDialog.title | 在哪个目录打开终端？ | 어떤 폴더에서 터미널을 열까요? | Open a terminal in which folder? | 保留 |
| provider.openTerminalDialog.description | 会在你选的目录里打开一个终端，并用「{{name}}」的配置启动 {{app}}。一般选你的项目文件夹。 | 선택한 폴더에 터미널이 열리고 "{{name}}"의 설정으로 {{app}}가 시작됩니다. 일반적으로 프로젝트 폴더를 선택합니다. | A terminal opens in the folder you pick and starts {{app}} with "{{name}}"'s settings. Usually you'd pick your project folder. | 保留 |
| provider.openTerminalDialog.isolationTitle | 这个终端是隔离的 | 이 터미널은 별도로 격리되어 있습니다 | This terminal is isolated | 已修订 |
| provider.openTerminalDialog.isolationBody | 它固定使用「{{name}}」，之后在 CC Switch 里切换供应商不会影响它；它也不会改动 CC Switch 里正在使用的供应商。 | 이 터미널은 ‘{{name}}’ 설정을 계속 사용합니다. 이후 CC Switch에서 공급자를 전환해도 영향을 받지 않으며, CC Switch에서 현재 사용 중인 공급자도 바꾸지 않습니다. | It stays on "{{name}}": switching providers in CC Switch later won't affect it, and it won't change the provider CC Switch is currently using. | 已修订 |
| provider.openTerminalDialog.isolationBodyAgy | 「{{name}}」的 Key 和地址只传给这个终端里的 agy，不写进任何文件；在别的终端里直接运行 agy 仍是 Google 登录。 | “{{name}}”의 API 키와 엔드포인트는 이 터미널에서 실행하는 agy에만 전달되고 어떤 파일에도 저장되지 않습니다. 다른 터미널에서 agy를 직접 실행하면 Google 로그인을 계속 사용합니다. | The key and endpoint of "{{name}}" go only to agy in this terminal and are never written to a file; running agy directly in another terminal still uses your Google sign-in. | 已修订 |
| provider.openTerminalDialog.noDir | 还没选目录 | 선택한 폴더가 없습니다. | No folder selected | 保留 |
| provider.openTerminalDialog.choose | 选择文件夹… | 폴더 선택… | Choose Folder… | 保留 |
| provider.openTerminalDialog.change | 更换… | 변경… | Change… | 已修订 |
| provider.openTerminalDialog.recent | 最近用过 | 최근 항목 | Recent | 已修订 |
| provider.openTerminalDialog.forget | 从最近用过里移除 | 최근 항목에서 삭제 | Remove from recent | 保留 |
| provider.openTerminalDialog.confirm | 打开终端 | 터미널 열기 | Open Terminal | 保留 |
| provider.openTerminalDialog.agySwitchTitle | 会切换 agy 的登录 | agy 로그인 계정이 변경됩니다 | This switches agy's sign-in | 已修订 |
| provider.openTerminalDialog.agySwitchBody | 打开前把 agy 的登录切换到 {{account}}，之后新开的 agy 都用这个号。 | 터미널을 열기 전에 agy 로그인 계정을 {{account}}(으)로 변경합니다. 이후 새로 실행하는 모든 agy는 이 계정을 사용합니다. | Before opening, agy's sign-in switches to {{account}}, and agy sessions started afterwards use this account. | 已修订 |
| provider.openTerminalDialog.agySwitchRunning | 检测到 agy 正在运行：已打开的 agy 仍用原账号，还可能把原账号写回去，最好先退出它们。 | 실행 중인 agy가 감지되었습니다. 이미 실행 중인 agy는 기존 계정을 계속 사용하며, 기존 계정 정보를 로그인 설정에 다시 저장할 수도 있습니다. 먼저 해당 agy를 모두 종료하는 것이 좋습니다. | agy is running: open agy sessions keep the previous account and may write it back. Quit them first if you can. | 已修订 |
| provider.name | 名称 | 이름 | Name | 保留 |
| provider.namePlaceholder | 例如：Claude 官方 | 예: Claude 공식 | e.g., Claude Official | 已修订 |
| provider.websiteUrl | 官网链接 | 웹사이트 URL | Website URL | 保留 |
| provider.notes | 备注 | 메모 | Notes | 保留 |
| provider.notesPlaceholder | 例如：公司专用账号 | 예: 회사 전용 계정 | e.g., Company dedicated account | 保留 |
| provider.configJson | 配置 JSON | JSON 설정 | Config JSON | 已修订 |
| provider.configJsonHint | 请填写完整的 Claude Code 配置 | 전체 Claude Code 설정을 입력하세요. | Please fill in complete Claude Code configuration | 已修订 |
| provider.addProvider | 添加供应商 | 공급자 추가 | Add Provider | 已修订 |
| provider.sortUpdated | 排序已更新 | 정렬 순서가 업데이트되었습니다. | Sort order updated | 保留 |
| provider.usageSaved | 用量查询配置已保存 | 사용량 조회 설정이 저장되었습니다. | Usage query configuration saved | 已修订 |
| provider.usageSaveFailed | 用量查询配置保存失败 | 사용량 조회 설정을 저장하지 못했습니다. | Failed to save usage query configuration | 已修订 |
| provider.geminiConfig | Gemini 配置 | Gemini 설정 | Gemini Configuration | 已修订 |
| provider.geminiConfigHint | 使用 .env 格式配置 Gemini | .env 형식을 사용하여 Gemini 설정 | Use .env format to configure Gemini | 已修订 |
| provider.form.agy.endpointHelp | 留空用 Google 默认 API。第三方地址须兼容 Gemini API，并支持 agy 内置的 Gemini 模型。 | 비워 두면 Google 기본 API를 사용합니다. 타사 엔드포인트는 Gemini API와 호환되어야 하며 agy에 내장된 Gemini 모델을 지원해야 합니다. | Leave empty for Google's default API. Third-party endpoints must support the Gemini API and agy's built-in Gemini models. | 已修订 |
| provider.form.agy.modelHelp | 填模型列表里的显示名称，可点「获取模型列表」选择。只对那次会话生效。 | 모델 목록에 표시되는 이름을 입력하세요. ‘모델 목록 가져오기’를 눌러 선택할 수 있습니다. 해당 세션에만 적용됩니다. | Use the display name from the model list (Fetch Models). Applies to that session only. | 已修订 |
| provider.form.agy.keyFieldsHint | 模型、Key 和地址都只在「打开终端」时使用，不写进 Antigravity 自己的设置。 | 모델, API 키 및 엔드포인트는 ‘터미널 열기’ 실행 시에만 사용되며 Antigravity 자체 설정에는 저장하지 않습니다. | The model, key and endpoint are only used by "Open Terminal" and are never written to Antigravity's own settings. | 已修订 |
| provider.form.agy.envFile | 启动环境变量 | 실행 환경 변수 | Launcher environment variables | 已修订 |
| provider.form.agy.envFileHint | 从卡片「打开终端」启动 agy 时，CC Switch 只把 API Key 和请求地址传给那一个 agy 进程，不写进任何文件。其他环境变量不会应用。 | 카드의 ‘터미널 열기’로 agy를 실행하면 CC Switch는 API 키와 엔드포인트를 해당 agy 프로세스에만 전달하고 어떤 파일에도 저장하지 않습니다. 다른 환경 변수는 적용되지 않습니다. | When agy is started from the card's "Open Terminal", CC Switch passes the API key and endpoint to that one agy process only and never writes them to a file. Other environment variables are not applied. | 已修订 |
| provider.form.agy.configJson | 模型配置（CC Switch 格式） | 모델 설정(CC Switch 형식) | Model configuration (CC Switch format) | 已修订 |
| provider.form.agy.configJsonHint | 这里仅支持模型设置，其他 Antigravity 选项请在 agy 中调整；MCP 在 MCP 面板中管理。 | 여기서는 모델 설정만 지원합니다. 다른 Antigravity 옵션은 agy에서 변경하고 MCP는 MCP 패널에서 관리하세요. | Only model settings are supported here. Change other Antigravity options in agy; manage MCP in the MCP panel. | 已修订 |
| provider.form.agy.account | 账号 | 계정 | Account | 保留 |
| provider.form.agy.accountFollow | 跟随 agy 当前登录 | agy의 현재 로그인 따르기 | Follow agy's current sign-in | 已修订 |
| provider.form.agy.accountMissing | 不在这台电脑上的账号 | 이 컴퓨터에 없는 계정 | An account not on this computer | 保留 |
| provider.form.agy.accountHelp | 选了账号的话，「打开终端」前会先把 agy 的登录切到它（全局生效，之后新开的 agy 都用它）。账号在授权中心添加。 | 계정을 선택하면 ‘터미널 열기’ 실행 전에 agy의 로그인을 해당 계정으로 전환합니다. 이는 전역적으로 적용되며 이후 시작한 agy 세션도 이 계정을 사용합니다. 계정은 인증 센터에서 추가하세요. | With an account selected, Open Terminal first switches agy's sign-in to it (this applies globally: agy sessions started afterwards use it). Add accounts in the Auth Center. | 已修订 |
| provider.form.gemini.model | 模型 | 모델 | Model | 保留 |
| provider.form.gemini.oauthTitle | OAuth 认证模式 | OAuth 인증 모드 | OAuth Authentication Mode | 保留 |
| provider.form.gemini.oauthHint | Google 官方使用 OAuth 个人认证，无需填写 API Key。首次使用时会自动打开浏览器进行登录。 | Google 공식은 OAuth 개인 인증을 사용하므로 API 키를 입력할 필요가 없습니다. 처음 사용할 때 로그인을 위해 브라우저가 자동으로 열립니다. | Google official uses OAuth personal authentication, no need to fill in API Key. The browser will automatically open for login on first use. | 保留 |
| provider.form.gemini.apiKeyPlaceholder | 请输入 Gemini API Key | Gemini API 키를 입력하세요 | Enter Gemini API Key | 保留 |
| provider.duplicateLiveIdsLoadFailed | 读取配置中的供应商标识失败，请先修复配置后再试 | 설정에서 공급자 식별자를 읽지 못했습니다. 설정을 수정하고 다시 시도해 주세요. | Failed to read provider identifiers from config, please fix the config and try again | 已修订 |
| provider.editorViewFailed | 无法读取客户端配置文件，下面显示的是保存的供应商配置：{{error}} | 클라이언트 설정 파일을 읽을 수 없으므로 저장된 공급자 설정이 아래와 같습니다: {{error}} | Cannot read the client config file, so the saved provider configuration is shown below: {{error}} | 已修订 |
| provider.editConflict.title | 配置文件在编辑期间被修改 | 편집하는 동안 설정 파일이 변경되었습니다. | The config file changed while you were editing | 已修订 |
| provider.editConflict.message | 打开编辑器之后，下面这些设置被其他程序（比如 Claude Code）改过。要用你的修改覆盖，还是保留外部的修改？其余改动都会照常保存。 | 편집기를 연 후 다른 프로그램(예: Claude Code)에 의해 아래 설정이 변경되었습니다. 수정사항으로 덮어쓰시겠습니까, 아니면 외부 변경사항을 유지하시겠습니까? 다른 편집 내용은 어느 쪽이든 저장됩니다. | After the editor opened, the settings below were changed by another program (such as Claude Code). Overwrite them with your edits, or keep the external changes? Your other edits are saved either way. | 保留 |
| provider.editConflict.keepTheirs | 保留外部修改 | 외부 변경사항 유지 | Keep external changes | 保留 |
| provider.editConflict.keepMine | 用我的修改覆盖 | 내 편집 내용으로 덮어쓰기 | Overwrite with my edits | 保留 |
| provider.backToList | 返回供应商列表 | 공급자 목록으로 돌아가기 | Back to providers | 已修订 |
| provider.editProviderNamed | 编辑 {{name}} | {{name}} 편집 | Edit {{name}} | 保留 |
| provider.formSubtitleStack | {{app}}（聚合模式） | {{app}} (통합 모드) | {{app}} (Aggregation mode) | 已修订 |
| provider.editCurrentNoticeFile | 这是正在使用的供应商。保存后会立即写进 | 사용 중인 공급자입니다. 저장하면 | This is the provider in use. Saving writes it to | 已修订 |
| provider.editCurrentNoticeFileEnd | ，下一次请求生效。 | 에 즉시 저장되며, 다음 요청부터 적용됩니다. |  right away; the next request uses it. | 已修订 |
| provider.editCurrentNotice | 这是正在使用的供应商。保存后立即生效，下一次请求就用新的设置。 | 사용중인 공급자입니다. 저장은 즉시 적용됩니다. 다음 요청에서는 새 설정을 사용합니다. | This is the provider in use. Saving takes effect right away; the next request uses the new settings. | 已修订 |
| claudeCode.needsRouting | 需要路由 | 라우팅 필요 | Needs Routing | 保留 |
| claudeCode.noRoutingSupport | 不支持路由 | 라우팅 지원 없음 | No Routing Support | 保留 |
| codex.needsRouting | 需要路由 | 라우팅 필요 | Needs Routing | 保留 |
| codex.noRoutingSupport | 不支持路由 | 라우팅 지원 없음 | No Routing Support | 保留 |
| codex.officialRouting | 官方账号路由 | 공식 계정 라우팅 | Official Account Routing | 保留 |
| codex.nativeLogin | Codex 登录 | Codex 로그인 | Codex Sign-in | 保留 |
| codex.followCodexLogin | 跟随 Codex 登录 | Codex 로그인 따르기 | Follow Codex login | 已修订 |
| codex.followCodexLoginDescription | 账号会随 Codex CLI 当前登录变化 | 현재 Codex CLI 로그인으로 계정이 변경됩니다. | The account changes with the current Codex CLI login | 保留 |
| codex.openAiAccount | OpenAI 账号 | OpenAI 계정 | OpenAI account | 保留 |
| codex.accountNotSelected | 尚未选择账号 | 선택한 계정이 없습니다. | No account selected | 保留 |
| codex.chooseAccount | 选择账号 | 계정 선택 | Choose account | 保留 |
| codex.accountStatusUnavailable | 无法读取账号信息 | 계정 세부정보를 로드할 수 없습니다. | Unable to load account details | 保留 |
| codex.boundAccountUnavailable | 绑定的账号不可用 | 연결된 계정을 사용할 수 없습니다. | The linked account is unavailable | 保留 |
| codex.accountLoading | 正在加载账号… | 계정 로드 중… | Loading account… | 保留 |
| claudeDesktop.modelConfigTitle | 模型配置 | 모델 설정 | Model Configuration | 已修订 |
| claudeDesktop.modelModeLabel | 接入方式 | 연결 모드 | Connection Mode | 保留 |
| claudeDesktop.modelModeDirect | 直连 | 직접 연결 | Direct | 保留 |
| claudeDesktop.modelModeProxy | 模型映射 | 모델 매핑 | Model Mapping | 保留 |
| claudeDesktop.officialNotice | Claude Desktop 官方供应商使用应用内置的 1P 登录，无需配置 API Key 和接口地址。 | Claude Desktop 공식 공급자는 내장된 1P 로그인을 사용합니다. API 키 또는 엔드포인트 URL은 필요하지 않습니다. | Claude Desktop official providers use the built-in 1P sign-in. No API key or endpoint URL is required. | 已修订 |
| claudeDesktop.mode | 模型处理方式 | 모델 처리 | Model handling | 保留 |
| claudeDesktop.modeDirect | 直连 | 직접 연결 | Direct | 保留 |
| claudeDesktop.modeProxy | 需要路由 | 라우팅 필요 | Requires routing | 保留 |
| claudeDesktop.modelMappingToggle | 需要模型映射 | 모델 매핑 필요 | Needs model mapping | 保留 |
| claudeDesktop.modelModeHint | 如果你的供应商提供原生 Claude 系列模型，可以使用直连；如果是 DeepSeek、Kimi 等第三方模型，请使用模型映射。 | 공급자가 네이티브 Claude 모델을 제공하면 직접 연결을 사용할 수 있습니다. DeepSeek나 Kimi 같은 타사 모델에는 모델 매핑을 사용하세요. | If your provider offers native Claude models, you can use Direct. For third-party models such as DeepSeek or Kimi, use Model Mapping. | 已修订 |
| claudeDesktop.routeMapTitle | 模型映射 | 모델 매핑 | Model mapping | 保留 |
| claudeDesktop.routeMapHint | 为 Sonnet、Opus、Haiku 三档分别填写实际请求模型；菜单显示名可写 DeepSeek、Kimi 等品牌名。留空的档会自动沿用 Sonnet（或第一个已填档）的模型，确保子 agent 调用的 Haiku 始终可用。 | Sonnet, Opus, Haiku 각 등급에서 실제로 요청할 모델을 입력하세요. DeepSeek나 Kimi 같은 모델은 메뉴 표시 이름도 지정하세요. 비워 둔 등급은 Sonnet 등급의 모델 또는 처음 입력한 등급의 모델을 이어받으므로 서브에이전트가 호출하는 Haiku도 항상 사용할 수 있습니다. | Fill in the actual request model for each of the Sonnet, Opus, and Haiku tiers. Use the menu display name for branded models such as DeepSeek or Kimi. Any tier left blank inherits the Sonnet tier's model (or the first tier you filled in), so the Haiku that sub-agents call is always available. | 已修订 |
| claudeDesktop.routeModelLabel | 模型角色 | 모델 역할 | Model role | 保留 |
| claudeDesktop.routeRoleSonnet | Sonnet | Sonnet | Sonnet | 已修订 |
| claudeDesktop.routeRoleOpus | Opus | Opus | Opus | 已修订 |
| claudeDesktop.routeRoleFable | Fable | Fable | Fable | 已修订 |
| claudeDesktop.routeRoleHaiku | Haiku | Haiku | Haiku | 已修订 |
| claudeDesktop.labelOverrideLabel | 菜单显示名 | 메뉴 표시 이름 | Menu display name | 保留 |
| claudeDesktop.upstreamModelLabel | 实际请求模型 | 실제 요청에 사용할 모델 | Requested model | 已修订 |
| claudeDesktop.supports1mLabel | 声明支持 1M | 1M 컨텍스트 지원 명시 | Declare 1M | 已修订 |
| claudeDesktop.supports1mShort | 1M | 1M | 1M | 已修订 |
| claudeDesktop.directModelListTitle | 模型列表 | 모델 목록 | Model List | 保留 |
| claudeDesktop.directModelListCollapsedHint | 原生 Claude 模型供应商通常不用填写，Claude Desktop 会自动读取 /v1/models。 | 네이티브 Claude 모델 공급자는 일반적으로 설정할 필요가 없습니다. Claude Desktop이 /v1/models를 자동으로 가져옵니다. | Native Claude model providers usually do not need this. Claude Desktop will fetch /v1/models automatically. | 已修订 |
| claudeDesktop.directModelListHint | 配置 Claude Desktop 可用的 Sonnet、Opus、Haiku 模型。留空时 Claude Desktop 会自动读取 /v1/models；勾选 1M 会声明支持 1M 上下文。 | Claude Desktop에 사용할 수 있는 Sonnet, Opus 및 Haiku 모델을 설정합니다. Claude Desktop가 /v1/models를 자동으로 가져오도록 하려면 이 항목을 비워 두세요. 1M을 선택하면 1M 컨텍스트 지원이 선언됩니다. | Configure the Sonnet, Opus, and Haiku models available to Claude Desktop. Leave this empty to let Claude Desktop fetch /v1/models automatically. Checking 1M declares 1M context support. | 已修订 |
| claudeDesktop.directModelInvalid | 直连模型必须使用 Claude Desktop 可识别的 Sonnet / Opus / Haiku 模型名 | 직접 연결 모델에는 Claude Desktop이 인식하는 Sonnet / Opus / Haiku 모델 ID를 사용해야 합니다 | Direct models must use Claude Desktop-recognized Sonnet / Opus / Haiku model IDs | 已修订 |
| claudeDesktop.addModel | 添加模型 | 모델 추가 | Add model | 保留 |
| claudeDesktop.addRoute | 添加模型 | 모델 추가 | Add model | 保留 |
| claudeDesktop.routeInvalid | 请选择模型角色并填写实际请求模型 | 모델 역할을 선택하고 실제 요청에 사용할 모델을 입력하세요. | Choose a model role and enter the requested model | 已修订 |
| claudeDesktop.routesRequired | 至少填写一个模型映射 | 모델 매핑이 하나 이상 필요합니다. | At least one model mapping is required | 保留 |
| claudeDesktop.statusTitle | Claude Desktop 配置需要检查 | Claude Desktop 설정에 주의가 필요합니다. | Claude Desktop configuration needs attention | 已修订 |
| claudeDesktop.statusUnsupported | 当前平台暂不支持 Claude Desktop 3P 配置写入。 | 현재 플랫폼에서는 아직 Claude Desktop 3P 설정 저장을 지원하지 않습니다. | This platform does not support writing Claude Desktop 3P configuration yet. | 已修订 |
| claudeDesktop.statusStaleRawModels | Claude Desktop profile 中存在非 Sonnet / Opus / Haiku 角色模型名，新版 Claude Desktop 可能拒绝加载；重新切换当前供应商可修复。 | Claude Desktop 프로필에는 Sonnet/Opus/Haiku 역할 계열 외부의 모델 ID가 포함되어 있습니다. 최신 Claude Desktop 버전에서는 이를 거부할 수 있습니다. 현재 공급자로 다시 전환하여 복구하세요. | The Claude Desktop profile contains model IDs outside the Sonnet / Opus / Haiku role families. Newer Claude Desktop versions may reject it; switch to the current provider again to repair it. | 已修订 |
| claudeDesktop.statusMissingRouteMappings | 路由那家没有有效的模型映射；请编辑它，补全至少一个模型映射。 | 라우팅된 공급자에 유효한 모델 매핑이 없습니다. 이를 편집하고 하나 이상의 매핑을 추가하십시오. | The routed provider has no valid model mapping. Edit it and add at least one mapping. | 已修订 |
| claudeDesktop.statusGatewayTokenMissing | 当前本地路由 token 尚未生成；重新切换该供应商会写入新的本地 token。 | 현재 로컬 라우팅 토큰이 아직 생성되지 않았습니다. 이 공급자로 다시 전환하면 새 로컬 토큰이 저장됩니다. | The local routing token has not been generated yet. Switching to this provider again will write a new local token. | 已修订 |
| claudeDesktop.statusBaseUrlMismatch | Claude Desktop profile 指向的地址与当前供应商不一致；当前为 {{actual}}，应为 {{expected}}。重新切换当前供应商可修复。 | Claude Desktop 프로필의 URL이 현재 공급자와 다릅니다. 현재: {{actual}}, 예상: {{expected}}. 현재 공급자로 다시 전환하여 복구하세요. | The Claude Desktop profile points to a different URL than the current provider. Current: {{actual}}; expected: {{expected}}. Switch to the current provider again to repair it. | 已修订 |
| claudeDesktop.route.tooltip.active | Claude Desktop 本地路由已开启 - {{address}}:{{port}} | Claude Desktop 로컬 라우팅이 실행 중입니다 - {{address}}:{{port}} | Claude Desktop local routing is running - {{address}}:{{port}} | 保留 |
| claudeDesktop.route.tooltip.inactive | 开启 Claude Desktop 本地路由，用于需要模型映射或格式转换的供应商。当前配置地址：{{address}}:{{port}} | 모델 매핑 또는 형식 변환이 필요한 공급자를 위해 Claude Desktop 로컬 라우팅을 활성화합니다. 설정된 주소: {{address}}:{{port}} | Turn on Claude Desktop local routing for providers that need model mapping or format conversion. Configured address: {{address}}:{{port}} | 已修订 |
| claudeDesktop.route.stopBlockedByTakeover | 还有其他应用在路由模式。请先让这些应用回到直连，再停止路由服务。 | 다른 앱이 아직 라우팅 모드입니다. 라우팅 서비스를 중지하려면 먼저 해당 앱을 직접 연결로 전환하세요. | Other apps are still in Routing mode. Switch them back to Direct before stopping the routing service. | 已修订 |
| notifications.providerAdded | 供应商已添加 | 공급자가 추가됨 | Provider added | 已修订 |
| notifications.providerSaved | 供应商配置已保存 | 공급자 설정이 저장되었습니다. | Provider configuration saved | 已修订 |
| notifications.providerDeleted | 供应商删除成功 | 공급자가 삭제되었습니다. | Provider deleted successfully | 已修订 |
| notifications.switchSuccess | 切换成功！ | 전환 성공! | Switch successful! | 保留 |
| notifications.codexRestartRequired | 切换成功，请重启客户端以生效 | 성공적으로 전환되었습니다. 변경 사항을 적용하려면 클라이언트를 다시 시작하세요. | Switched successfully. Restart the client to apply changes. | 保留 |
| notifications.geminiRestartRequired | 切换成功，请重启 Gemini CLI 以生效 | 성공적으로 전환되었습니다. 변경 사항을 적용하려면 Gemini CLI를 다시 시작하세요. | Switched successfully. Restart Gemini CLI to apply changes. | 保留 |
| notifications.grokBuildRestartRequired | 切换成功，请重启 Grok Build 以生效 | 성공적으로 전환되었습니다. 변경 사항을 적용하려면 Grok Build를 다시 시작하세요. | Switched successfully. Restart Grok Build to apply changes. | 保留 |
| notifications.claudeDesktopRestartRequired | 切换成功，重启 Claude Desktop 后生效 | 성공적으로 전환되었습니다. 변경 사항을 적용하려면 Claude Desktop를 다시 시작하세요. | Switched successfully. Restart Claude Desktop to apply changes. | 保留 |
| notifications.addToConfigSuccess | 已添加到配置 | 설정에 추가됨 | Added to config | 已修订 |
| notifications.removeFromConfigSuccess | 已从配置移除 | 설정에서 제거됨 | Removed from config | 已修订 |
| notifications.removeFromConfigFailed | 无法移除供应商 | 공급자를 제거할 수 없습니다. | Could not remove provider | 已修订 |
| notifications.switchFailedTitle | 切换失败 | 전환 실패 | Switch failed | 保留 |
| notifications.switchFailed | 切换失败：{{error}} | 전환 실패: {{error}} | Switch failed: {{error}} | 已修订 |
| notifications.autoImported | 已从现有配置创建默认供应商 | 기존 설정에서 기본 공급자를 생성했습니다 | Default provider created from existing configuration | 已修订 |
| notifications.addFailed | 添加供应商失败：{{error}} | 공급자 추가 실패: {{error}} | Failed to add provider: {{error}} | 已修订 |
| notifications.saveFailed | 保存失败：{{error}} | 저장 실패: {{error}} | Save failed: {{error}} | 保留 |
| notifications.saveFailedGeneric | 保存失败，请重试 | 저장하지 못했습니다. 다시 시도해 주세요. | Save failed, please try again | 保留 |
| notifications.appliedToClaudePlugin | 已应用到 Claude 插件 | Claude 플러그인에 적용 | Applied to Claude plugin | 保留 |
| notifications.removedFromClaudePlugin | 已从 Claude 插件移除 | Claude 플러그인에서 제거됨 | Removed from Claude plugin | 保留 |
| notifications.syncClaudePluginFailed | 同步 Claude 插件失败 | Claude 플러그인 동기화 실패 | Sync Claude plugin failed | 已修订 |
| notifications.skipClaudeOnboardingFailed | 跳过 Claude Code 初次安装确认失败 | Claude Code 첫 실행 확인을 건너뛰지 못했습니다. | Failed to skip Claude Code first-run confirmation | 保留 |
| notifications.clearClaudeOnboardingSkipFailed | 恢复 Claude Code 初次安装确认失败 | Claude Code 첫 실행 확인을 복원하지 못했습니다. | Failed to restore Claude Code first-run confirmation | 保留 |
| notifications.updateSuccess | 供应商更新成功 | 공급자가 업데이트되었습니다. | Provider updated successfully | 已修订 |
| notifications.updateFailed | 更新供应商失败：{{error}} | 공급자 업데이트 실패: {{error}} | Failed to update provider: {{error}} | 已修订 |
| notifications.deleteSuccess | 供应商已删除 | 공급자가 삭제되었습니다. | Provider deleted | 已修订 |
| notifications.deleteFailed | 删除供应商失败：{{error}} | 공급자 삭제 실패: {{error}} | Failed to delete provider: {{error}} | 已修订 |
| notifications.settingsSaved | 设置已保存 | 설정이 저장되었습니다. | Settings saved | 保留 |
| notifications.settingsSaveFailed | 保存设置失败：{{error}} | 설정 저장 실패: {{error}} | Failed to save settings: {{error}} | 保留 |
| notifications.proxyRequiredForSwitch | 此供应商{{reason}}，需要路由服务才能正常使用，请先启动路由 | 이 공급자는 {{reason}}. 정상 작동하려면 라우팅 서비스가 필요하므로 먼저 라우팅을 시작하세요. | This provider {{reason}}, requires the routing service to work properly. Start routing first. | 已修订 |
| notifications.proxyReasonCopilot | 使用 GitHub Copilot 作为 Claude 供应商 | GitHub Copilot을 Claude 공급자로 사용합니다 | uses GitHub Copilot as a Claude provider | 已修订 |
| notifications.proxyReasonOpenAIChat | 使用 OpenAI Chat 接口格式 | OpenAI Chat API 형식을 사용합니다 | uses OpenAI Chat API format | 已修订 |
| notifications.proxyReasonOpenAIResponses | 使用 OpenAI Responses 接口格式 | OpenAI Responses API 형식을 사용합니다 | uses OpenAI Responses API format | 已修订 |
| notifications.proxyReasonAnthropicMessages | 使用 Anthropic Messages 接口格式 | Anthropic Messages API 형식을 사용합니다 | uses Anthropic Messages API format | 已修订 |
| notifications.proxyReasonFullUrl | 开启了完整 URL 连接模式 | 전체 URL 연결 모드가 활성화되어 있습니다 | has full URL connection mode enabled | 保留 |
| notifications.proxyReasonDesktopMapping | 使用模型映射（Claude Desktop 只认 Claude 模型名） | 모델 매핑을 사용합니다 (Claude Desktop은 Claude 모델 이름만 허용) | uses model mapping (Claude Desktop only accepts Claude model names) | 已修订 |
| notifications.proxyReasonManagedOAuth | 使用托管 OAuth 登录（令牌由本地路由注入） | 관리형 OAuth 로그인을 사용합니다 (로컬 라우팅이 토큰을 주입) | uses managed OAuth login (token injected by local routing) | 已修订 |
| notifications.proxyReasonRoutingRequired | 需要本地路由处理请求 | 요청 처리에 로컬 라우팅이 필요합니다 | requires local routing to process requests | 已修订 |
| notifications.openAIFormatHint | 此供应商使用 OpenAI 兼容格式，需要开启路由服务才能正常使用 | 이 공급자는 OpenAI 호환 형식을 사용하며 라우팅 서비스를 활성화해야 합니다. | This provider uses OpenAI-compatible format and requires the routing service to be enabled | 已修订 |
| notifications.copilotProxyHint | GitHub Copilot 作为 Claude 供应商时始终需要本地路由；路由会根据当前模型自动选择 Chat Completions 或 Responses。 | GitHub Copilot을 Claude 공급자로 사용하려면 항상 로컬 라우팅이 필요합니다. 현재 모델에 따라 Chat Completions 또는 Responses를 자동으로 선택합니다. | GitHub Copilot as a Claude provider always requires local routing; routing automatically selects Chat Completions or Responses based on the current model. | 已修订 |
| notifications.openLinkFailed | 链接打开失败 | 링크를 열지 못했습니다. | Failed to open link | 保留 |
| notifications.openclawModelsRegistered | 模型已注册到 /model 列表 | 모델이 /model 목록에 등록되었습니다. | Models have been registered to /model list | 保留 |
| notifications.openclawDefaultModelSet | 已设为默认模型 | 기본 모델로 설정 | Set as default model | 保留 |
| notifications.openclawDefaultModelSetFailed | 设置默认模型失败 | 기본 모델을 설정하지 못했습니다. | Failed to set default model | 保留 |
| notifications.openclawNoModels | 该供应商没有配置模型 | 이 공급자에는 설정된 모델이 없습니다. | No models configured | 已修订 |
| notifications.openclawModelNotFound | 所选模型已不存在，请刷新后重试 | 선택한 모델이 더 이상 존재하지 않습니다. 새로고침하고 다시 시도하세요. | The selected model no longer exists. Refresh and try again. | 保留 |
| notifications.backfillWarning | 切换成功，但旧供应商配置回填失败，您手动修改的配置可能未保存 | 전환은 완료되었지만 이전 공급자의 설정을 다시 저장하지 못해 수동으로 변경한 설정이 저장되지 않았을 수 있습니다. | Switched successfully, but failed to save changes back to the previous provider | 已修订 |
| notifications.codexAuthCleanupFailed | 切换成功，但未能删除 auth.json，官方登录凭据仍留在磁盘上；如需彻底移除请手动删除 Codex 配置目录中的 auth.json | 성공적으로 전환되었지만 auth.json을 제거할 수 없습니다. 공식 로그인 자격 증명은 여전히 ​​디스크에 있습니다. Codex 설정 디렉터리에서 auth.json을 삭제하여 제거하세요. | Switched successfully, but auth.json could not be removed — the official login credentials are still on disk; delete auth.json from the Codex config directory to remove them | 已修订 |
| notifications.windowControlFailed | 窗口控制失败：{{error}} | 창 제어 실패: {{error}} | Window control failed: {{error}} | 保留 |
| notifications.officialBlockedByProxy | 本地路由模式下不能切换到官方供应商，使用路由访问官方 API 可能导致账号被封禁 | 로컬 라우팅이 활성화된 동안에는 공식 공급자로 전환할 수 없습니다. 공식 API와 함께 라우팅을 사용하면 계정이 차단될 수 있습니다. | Cannot switch to official provider while local routing is active. Using routing with official APIs may cause account bans. | 已修订 |
| notifications.proxyOfficialWarning | 当前供应商 {{name}} 是官方供应商，建议切换到第三方供应商后再使用本地路由 | 현재 공급자 {{name}}는 공식입니다. 로컬 라우팅을 사용하기 전에 타사 공급자로 전환하는 것을 고려하십시오. | Current provider {{name}} is official. Consider switching to a third-party provider before using local routing. | 已修订 |
| confirm.deleteProvider | 删除供应商 | 공급자 삭제 | Delete Provider | 已修订 |
| confirm.deleteProviderMessage | 确定要删除供应商 "{{name}}" 吗？此操作无法撤销。 | "{{name}}" 공급자를 삭제하시겠습니까? 이 작업은 취소할 수 없습니다. | Are you sure you want to delete provider "{{name}}"? This action cannot be undone. | 已修订 |
| confirm.removeProvider | 移除供应商 | 공급자 제거 | Remove Provider | 已修订 |
| confirm.removeProviderMessage | 确定要从配置中移除供应商 "{{name}}" 吗？<br><br>移除后该供应商将不再生效，但配置数据会保留在 CC Switch 中，您可以随时重新添加。 | 설정에서 "{{name}}" 공급자를 제거하시겠습니까?<br><br>제거 후에는 이 공급자가 더 이상 활성화되지 않지만 설정 데이터는 CC Switch에 유지됩니다. 언제든지 다시 추가할 수 있습니다. | Are you sure you want to remove provider "{{name}}" from the configuration?<br><br>After removal, this provider will no longer be active, but the configuration data will be retained in CC Switch. You can re-add it at any time. | 已修订 |
| confirm.piDefaultProviderWarning | Pi 的全局默认项当前指向此供应商。继续后，Pi 会尝试其他可用模型；你可以在 Pi 中使用 /model 重新选择，或使用 /login 登录其他供应商。 | Pi의 전역 기본값은 현재 이 공급자를 가리킵니다. 계속하면 Pi는 사용 가능한 다른 모델을 시도합니다. /model을 사용하여 하나를 선택하거나 /login을 사용하여 다른 공급자에 로그인하세요. | Pi's global default currently points to this provider. If you continue, Pi will try another available model; use /model to choose one or /login to sign in to another provider. | 已修订 |
| confirm.proxy.title | 启用本地路由服务 | 로컬 라우팅 활성화 | Enable Local Routing | 保留 |
| confirm.proxy.message | 本地路由是一项高级功能，启用前请确保您已了解其工作原理。<br><br>建议先查阅相关文档或咨询您的供应商，以获取正确的配置方式。 | 로컬 라우팅은 고급 기능입니다. 활성화하기 전에 작동 방식을 이해했는지 확인하세요.<br><br>적절한 설정을 위해 관련 문서나 공급자에 문의하는 것이 좋습니다. | Local routing is an advanced feature. Please make sure you understand how it works before enabling.<br><br>We recommend consulting the relevant documentation or your provider for proper configuration. | 已修订 |
| confirm.proxy.confirm | 我已了解，继续启用 | 이해했습니다. 활성화 | I understand, enable | 已修订 |
| confirm.failover.title | 启用故障转移功能 | 장애 조치 활성화 | Enable Failover | 保留 |
| confirm.failover.message | 故障转移是一项高级功能，启用前请确保您已了解其工作原理。<br><br>建议先在故障转移队列中配置好供应商优先级。 | 장애 조치는 고급 기능입니다. 활성화하기 전에 작동 방식을 이해했는지 확인하세요.<br><br>먼저 장애 조치 대기열에서 공급자 우선 순위를 설정하는 것이 좋습니다. | Failover is an advanced feature. Please make sure you understand how it works before enabling.<br><br>We recommend configuring provider priorities in the failover queue first. | 已修订 |
| confirm.failover.confirm | 我已了解，继续启用 | 이해했습니다. 활성화 | I understand, enable | 已修订 |
| confirm.unifyCodexHistory.title | 统一 Codex 会话历史 | 통합 Codex 세션 기록 | Unified Codex session history | 保留 |
| confirm.unifyCodexHistory.message | 开启后，Codex CLI 的 resume 列表会把官方订阅与第三方的会话合并显示（Codex 桌面版更新后已经可以显示全部会话，不受影响）。注意：跨供应商继续旧会话时，可能因对方后端无法解密 encrypted_content 推理内容而失败。<br><br>可选择同时把现有官方会话历史迁入共享列表（迁移前自动备份到 ~/.cc-switch/backups，关闭开关时可选择恢复）。 | 켜면 Codex CLI의 resume 목록에 공식 구독과 타사 공급자의 세션이 함께 표시됩니다(Codex 데스크톱 버전은 업데이트 후 이미 모든 세션을 표시하므로 영향을 받지 않습니다). 주의: 다른 공급자로 이전 세션을 이어갈 때 해당 백엔드가 encrypted_content 추론 내용을 복호화하지 못해 실패할 수 있습니다.<br><br>기존 공식 세션 기록도 공유 목록으로 옮길 수 있습니다(이전하기 전에 ~/.cc-switch/backups에 자동 백업되며, 이 옵션을 끌 때 복원 여부를 선택할 수 있습니다). | When enabled, the Codex CLI resume list shows official subscription and third-party sessions together (the Codex desktop app can show all sessions since a recent update and is unaffected). Note: resuming an old session across providers may fail because the other backend cannot decrypt its encrypted_content reasoning.<br><br>You can also migrate your existing official session history into the shared list (backed up to ~/.cc-switch/backups first; you can restore it when turning this off). | 已修订 |
| confirm.unifyCodexHistory.migrateExisting | 同时迁入现有官方会话历史 | 기존 공식 세션 기록도 마이그레이션 | Also migrate existing official session history | 保留 |
| confirm.unifyCodexHistory.confirm | 我已了解，继续开启 | 이해했습니다. 활성화 | I understand, enable | 已修订 |
| confirm.unifyCodexHistoryOff.title | 关闭统一会话历史 | 통합 세션 기록 끄기 | Turn off unified session history | 保留 |
| confirm.unifyCodexHistoryOff.message | 关闭后，Codex CLI 中官方订阅与第三方将恢复各自独立的会话列表（桌面版仍显示全部会话）。开启期间产生的会话因无法区分来源，将留在第三方历史中，CLI 在官方订阅下将看不到它们。 | 끄면 Codex CLI는 공식 구독 및 타사 공급자에 대한 별도의 세션 목록으로 돌아갑니다(데스크톱 앱에는 여전히 모든 세션이 표시됨). 이 기능이 켜져 있는 동안 생성된 세션은 구분할 수 없으므로 타사 기록에 유지되며 CLI는 공식 구독에 표시하지 않습니다. | When turned off, the Codex CLI goes back to separate session lists for the official subscription and third-party providers (the desktop app still shows all sessions). Sessions created while this was on can't be told apart, so they stay in the third-party history and the CLI won't show them under the official subscription. | 已修订 |
| confirm.unifyCodexHistoryOff.restoreBackup | 把开启时迁入的官方会话还原回官方历史（按备份精确还原） | 활성화 시점에 마이그레이션된 공식 세션을 공식 기록으로 복원(백업에서 정확한 복원) | Restore the official sessions migrated at enable time back to the official history (exact restore from backup) | 保留 |
| confirm.unifyCodexHistoryOff.confirm | 关闭 | 끄기 | Turn off | 已修订 |
| confirm.usage.title | 配置用量查询 | 사용량 조회 설정 | Configure Usage Query | 已修订 |
| confirm.usage.message | 用量查询需要配置专用的查询脚本或 API 参数，请确保您已从供应商处获取相关信息。<br><br>如不确定如何配置，请先查阅供应商文档。 | 사용량 조회에는 사용자 지정 스크립트 또는 API 매개변수가 필요합니다. 공급자에서 필요한 정보를 받았는지 확인하세요.<br><br>설정 방법을 모르면 먼저 공급자의 문서를 참고하세요. | Usage query requires a custom script or API parameters. Please make sure you have obtained the necessary information from your provider.<br><br>If unsure how to configure, please consult your provider's documentation first. | 已修订 |
| confirm.usage.confirm | 我已了解，继续配置 | 이해했습니다. 설정 | I understand, configure | 已修订 |
| confirm.autoSync.title | 开启自动同步 | 자동 동기화 활성화 | Enable Auto Sync | 保留 |
| confirm.autoSync.message | 开启自动同步后，每次数据库变更都会自动上传到 WebDAV 服务器。<br><br>这可能会产生较高的网络流量消耗，请确保您的网络环境和 WebDAV 服务支持频繁的数据传输。 | 자동 동기화가 활성화되면 모든 데이터베이스 변경 사항이 WebDAV 서버에 자동으로 업로드됩니다.<br><br>이로 인해 상당한 네트워크 트래픽이 발생할 수 있습니다. 네트워크와 WebDAV 서비스가 빈번한 데이터 전송을 처리할 수 있는지 확인하십시오. | When auto sync is enabled, every database change will be automatically uploaded to the WebDAV server.<br><br>This may result in significant network traffic. Please ensure your network and WebDAV service can handle frequent data transfers. | 保留 |
| confirm.autoSync.confirm | 我已了解，继续开启 | 이해했습니다. 활성화 | I understand, enable | 已修订 |
| settings.title | 设置 | 설정 | Settings | 保留 |
| settings.general.appearance | 外观 | 화면 모양 | Appearance | 已修订 |
| settings.general.quotaDisplay | 额度显示 | 할당량 표시 | Quota display | 保留 |
| settings.general.quotaDisplayLeft | 剩余 | 남음 | Left | 已修订 |
| settings.general.quotaDisplayUsed | 已用 | 사용됨 | Used | 保留 |
| settings.general.quotaDisplayHelp | 供应商卡片、授权中心和托盘里，各档额度写还剩多少还是已经用了多少。余额和 Credits 始终写剩下的。 | 공급자 카드, 인증 센터 및 트레이에서 각 할당량 구간의 남은 양과 사용한 양 중 무엇을 표시할지 선택합니다. 잔액과 Credits는 항상 남은 양을 표시합니다. | Whether each quota window on provider cards, in Accounts and in the tray shows how much is left or how much is used. Balances and Credits always show what is left. | 已修订 |
| settings.general.sidebarAndHeader | 侧栏与页头 | 사이드바 및 헤더 | Sidebar and header | 保留 |
| settings.general.visibleApps | 在侧栏显示哪些应用 | 사이드바에 표시되는 앱 | Apps shown in the sidebar | 保留 |
| settings.general.goToApps | 前往「应用」 | ‘앱’ 페이지 열기 | Open Apps | 已修订 |
| settings.general.updates | 各应用的新版本 | 앱의 새 버전 | New versions of your apps | 保留 |
| settings.general.checkToolUpdates | 启动时检查各应用的新版本 | 시작 시 앱의 새 버전 확인 | Check for new versions of your apps at launch | 已修订 |
| settings.general.checkToolUpdatesHelp | 打开后，每次启动 CC Switch 会查一次已安装的命令行应用有没有新版本，查到了就在侧栏「应用」上显示一个圆点。不会自动升级。 | 켜면 CC Switch가 시작할 때마다 설치된 명령줄 앱의 새 버전을 확인하며, 새 버전이 있으면 사이드바의 ‘앱’에 점을 표시합니다. 자동으로 업그레이드하지는 않습니다. | When on, CC Switch checks your installed command-line apps for new versions each time it starts, and shows a dot on Apps in the sidebar if it finds one. Nothing is upgraded automatically. | 已修订 |
| settings.general.windowAndTerminal | 窗口与终端 | 창 및 터미널 | Window and terminal | 已修订 |
| settings.general.trayStyle | 托盘样式 | 트레이 스타일 | Tray style | 保留 |
| settings.general.trayStylePanel | 面板 | 패널 | Panel | 保留 |
| settings.general.trayStyleMenu | 菜单 | 메뉴 | Menu | 保留 |
| settings.general.trayStyleHelp | 点托盘图标时弹出什么（Windows 上左键始终打开主界面，右键弹出所选样式）。面板：各应用在用的供应商、额度和用量，可以搜索、切换。菜单：系统原生菜单。切换后立即生效。 | 트레이 아이콘을 클릭할 때 열리는 화면입니다. Windows에서는 왼쪽 클릭으로 항상 메인 창을 열고, 오른쪽 클릭으로 선택한 스타일을 엽니다. 패널에서는 각 앱의 사용 중인 공급자, 할당량 및 사용량을 확인하고 검색과 전환을 할 수 있습니다. 메뉴는 시스템 기본 메뉴를 사용합니다. 즉시 적용됩니다. | What opens when you click the tray icon (on Windows, left-click always opens the main window and right-click opens the selected style). Panel: each app's in-use provider, quota and usage, with search and switching. Menu: the system's native menu. Takes effect right away. | 已修订 |
| settings.general.minimizeToTrayHelp | 打开时，点关闭按钮只隐藏窗口，CC Switch 留在系统托盘里继续运行（轻量模式在托盘菜单里）；关闭时点关闭按钮直接退出。 | 켜져 있으면 닫기 버튼은 창만 숨기고 CC Switch는 시스템 트레이에서 계속 실행됩니다(경량 모드는 트레이 메뉴에 있음). 끄면 닫기 버튼이 종료됩니다. | When on, the close button only hides the window and CC Switch keeps running in the system tray (lightweight mode is in the tray menu). When off, the close button quits. | 保留 |
| settings.general.terminalHelp | 点供应商卡片上的「打开终端」时用哪个终端。选的终端不可用时，改用系统默认终端。 | 공급자 카드의 ‘터미널 열기’에 사용할 터미널입니다. 사용할 수 없으면 시스템 기본 터미널을 사용합니다. | The terminal used by “Open terminal” on provider cards. If it isn't available, the system default terminal is used. | 已修订 |
| settings.tabGeneral | 通用 | 일반 | General | 保留 |
| settings.tabAuth | 认证 | 인증 | Auth | 保留 |
| settings.tabAdvanced | 高级 | 고급 | Advanced | 保留 |
| settings.tabProxy | 路由 | 라우팅 | Routing | 保留 |
| settings.authCenter.description | 把 GitHub Copilot、ChatGPT、xAI 订阅当作供应商用。凭据由路由服务注入，相关供应商要在路由模式下使用（Codex 官方登录绑定除外）。Antigravity 账号用来切换 agy 的官方登录。 | GitHub Copilot, ChatGPT 및 xAI 구독을 공급자로 사용하세요. 라우팅 서비스는 자격 증명을 삽입하므로 이러한 공급자는 라우팅 모드에서 실행됩니다(Codex의 공식 로그인 바인딩 제외). Antigravity 계정은 agy의 공식 로그인을 전환합니다. | Use GitHub Copilot, ChatGPT and xAI subscriptions as providers. The routing service injects their credentials, so these providers run in Routing mode (except Codex's official-login binding). Antigravity accounts switch agy's official sign-in. | 已修订 |
| settings.authCenter.beta | Beta | 베타 | Beta | 保留 |
| settings.authCenter.copilotDescription | 管理 GitHub Copilot 账号 | GitHub Copilot 계정 관리 | Manage GitHub Copilot accounts | 保留 |
| settings.authCenter.codexOauthDescription | 管理 ChatGPT 账号 | ChatGPT 계정 관리 | Manage ChatGPT accounts | 保留 |
| settings.authCenter.xaiOauthDescription | 管理 xAI / Grok 账号 | xAI/Grok 계정 관리 | Manage xAI / Grok accounts | 保留 |
| settings.advanced.configDir.title | 配置文件目录 | 설정 디렉터리 | Configuration Directory | 已修订 |
| settings.advanced.configDir.description | 管理 Claude、Codex 和 Gemini 的配置存储路径 | Claude, Codex 및 Gemini 설정에 대한 스토리지 경로 관리 | Manage storage paths for Claude, Codex and Gemini configurations | 已修订 |
| settings.advanced.proxy.title | 本地路由 | 로컬 라우팅 | Local Routing | 保留 |
| settings.advanced.proxy.description | 控制路由服务开关、查看状态与端口信息 | 라우팅 서비스 토글 제어, 상태 및 포트 정보 보기 | Control routing service toggle, view status and port info | 保留 |
| settings.advanced.proxy.enableFeature | 在主页面显示本地路由开关 | 메인 페이지에 라우팅 토글 표시 | Show Routing Toggle on Main Page | 保留 |
| settings.advanced.proxy.enableFeatureDescription | 开启后，主页面顶部将显示路由和故障转移开关 | 활성화되면 라우팅 및 장애 조치 토글이 기본 페이지 상단에 나타납니다. | When enabled, the routing and failover toggles will appear at the top of the main page | 保留 |
| settings.advanced.proxy.enableStackMode | 在主页面显示聚合模式开关 | 메인 페이지에 통합 모드 스위치 표시 | Show the Aggregation mode switch on the main page | 已修订 |
| settings.advanced.proxy.enableStackModeDescription | 开启后，Claude Code 和 Codex 的主页面开关换成聚合模式：像 OpenCode 一样添加多家供应商，它们的模型都会出现在客户端的模型列表里（Codex 需要重启后生效），不做故障转移。和本地路由开关二选一，切换时已开启的 Claude Code、Codex 会先退回直连 | 켜면 Claude Code와 Codex의 메인 페이지 스위치가 통합 모드로 바뀝니다. OpenCode처럼 여러 공급자를 추가하면 해당 공급자들의 모델이 클라이언트 모델 목록에 표시됩니다(Codex는 다시 시작한 후 적용). 장애 조치는 사용하지 않습니다. 이 옵션과 로컬 라우팅 스위치는 둘 중 하나만 선택할 수 있으며, 전환 시 활성화되어 있던 Claude Code와 Codex는 먼저 직접 연결로 돌아갑니다. | When on, the main-page switch for Claude Code and Codex becomes the Aggregation mode: add several providers like in OpenCode, and all their models appear in the client's model list (Codex needs a restart first). No failover. This and the local routing switch are mutually exclusive; switching sends Claude Code and Codex back to direct first | 已修订 |
| settings.advanced.proxy.enableFailoverToggle | 在主页面显示故障转移开关 | 메인 페이지에 장애 조치 스위치 표시 | Show Failover Toggle on Main Page | 已修订 |
| settings.advanced.proxy.enableFailoverToggleDescription | 开启后，主页面顶部将独立显示故障转移开关 | 켜면 메인 페이지 상단에 장애 조치 스위치가 별도로 표시됩니다. | When enabled, the failover toggle will appear independently at the top of the main page | 已修订 |
| settings.advanced.proxy.running | 运行中 | 실행 중 | Running | 已修订 |
| settings.advanced.proxy.stopped | 已停止 | 중지됨 | Stopped | 保留 |
| settings.advanced.failover.title | 自动故障转移 | 자동 장애 조치 | Auto Failover | 保留 |
| settings.advanced.failover.description | 配置故障转移队列和熔断策略 | 장애 조치 대기열 및 서킷 브레이커 정책 설정 | Configure failover queue and circuit breaker strategy | 已修订 |
| settings.advanced.pricing.title | 成本定价 | 모델 요금 | Cost Pricing | 已修订 |
| settings.advanced.pricing.description | 管理各模型 Token 计费规则 | 모델별 토큰 가격 책정 규칙 관리 | Manage token pricing rules for each model | 保留 |
| settings.advanced.globalProxy.title | 全局出站代理 | 전역 아웃바운드 프록시 | Global Outbound Proxy | 已修订 |
| settings.advanced.globalProxy.description | 配置 CC Switch 访问外部 API 时使用的代理 | 외부 API에 액세스하도록 CC Switch용 프록시 설정 | Configure proxy for CC Switch to access external APIs | 已修订 |
| settings.advanced.data.title | 数据管理 | 데이터 관리 | Data Management | 保留 |
| settings.advanced.data.description | 导入和导出本地配置数据 | 로컬 설정 데이터 가져오기 및 내보내기 | Import and export local configuration data | 已修订 |
| settings.advanced.backup.title | 备份与恢复 | 백업 및 복원 | Backup & Restore | 保留 |
| settings.advanced.backup.description | 管理自动备份，查看和恢复数据库快照 | 자동 백업 관리, 데이터베이스 스냅샷 보기 및 복원 | Manage automatic backups, view and restore database snapshots | 保留 |
| settings.advanced.cloudSync.title | 云同步 | 클라우드 동기화 | Cloud Sync | 保留 |
| settings.advanced.cloudSync.description | 通过 WebDAV 在多设备间同步数据 | WebDAV를 통해 장치 간 데이터 동기화 | Sync data across devices via WebDAV | 保留 |
| settings.advanced.rectifier.title | 整流器 | 호환성 보정 | Rectifier | 已修订 |
| settings.advanced.rectifier.description | 自动修复 API 请求中的兼容性问题 | API 요청 호환성 문제 자동 수정 | Automatically fix API request compatibility issues | 保留 |
| settings.advanced.rectifier.enabled | 启用整流器 | 호환성 보정 활성화 | Enable Rectifier | 已修订 |
| settings.advanced.rectifier.requestGroup | 请求整流 | 요청 보정 | Request Rectification | 已修订 |
| settings.advanced.rectifier.responseGroup | 响应整流 | 응답 보정 | Response Rectification | 已修订 |
| settings.advanced.rectifier.thinkingSignature | Thinking 签名整流 | Thinking 서명 보정 | Thinking Signature Rectification | 已修订 |
| settings.advanced.rectifier.thinkingSignatureDescription | 当 Anthropic 类型供应商返回 thinking 签名不兼容或非法请求等错误时，自动移除不兼容的 thinking 相关块并对同一供应商重试一次 | Anthropic 유형 공급자가 thinking 서명 비호환 또는 잘못된 요청 등의 오류를 반환하면 호환되지 않는 thinking 관련 블록을 자동으로 제거한 뒤 같은 공급자로 한 번 다시 시도합니다. | When an Anthropic-type provider returns thinking signature incompatibility or illegal request errors, automatically removes incompatible thinking-related blocks and retries once with the same provider | 已修订 |
| settings.advanced.rectifier.thinkingBudget | Thinking Budget 整流 | Thinking Budget 보정 | Thinking Budget Rectification | 已修订 |
| settings.advanced.rectifier.thinkingBudgetDescription | 当 Anthropic 类型供应商返回 budget_tokens 约束错误（如至少 1024）时，自动将 thinking 规范为 enabled 并将 budget 设为 32000，同时在需要时将 max_tokens 设为 64000，然后重试一次 | Anthropic 유형 공급자가 budget_tokens 제약 오류(예: 최소 1024)를 반환하면 thinking을 enabled로, budget_tokens를 32000으로 설정합니다. 필요한 경우 max_tokens도 64000으로 설정한 뒤 한 번 다시 시도합니다. | When an Anthropic-type provider returns budget_tokens constraint errors (such as at least 1024), automatically normalizes thinking to enabled, sets thinking budget to 32000, and raises max_tokens to 64000 if needed, then retries once | 已修订 |
| settings.advanced.rectifier.mediaFallback | 不支持图片降级 | 지원되지 않는 이미지 대체 | Unsupported Image Fallback | 保留 |
| settings.advanced.rectifier.mediaFallbackDescription | 当供应商不支持图片输入时（已声明纯文本能力，或上游返回不支持图片的错误），自动将图片块替换为 [Unsupported Image] 标记，使对话不中断 | 공급자가 텍스트 전용 기능을 선언하거나 업스트림이 이미지 미지원 오류를 반환하면 이미지 블록을 [Unsupported Image] 표시로 자동 교체하여 대화가 중단되지 않게 합니다. | When a provider does not support image input (it declares text-only capability, or the upstream returns an unsupported-image error), automatically replaces image blocks with an [Unsupported Image] marker so the conversation is not interrupted | 已修订 |
| settings.advanced.rectifier.mediaHeuristic | 纯文本模型预判 | 텍스트 전용 모델 사전 검사 | Text-Only Model Preflight | 已修订 |
| settings.advanced.rectifier.mediaHeuristicDescription | 发送前根据内置的已确认纯文本模型注册表剥离图片。关闭仅停用代理的注册表预判；已声明纯文本模型的处理和上游报错兜底仍保留，且不会改变 Codex 模型目录的能力声明 | 전송 전에, 내장 목록에서 텍스트 전용으로 확인된 모델의 요청에서 이미지를 제거합니다. 이 옵션을 꺼도 프록시의 목록 기반 사전 검사만 중지됩니다. 선언된 텍스트 전용 모델 처리와 업스트림 오류 시 대체 처리는 유지되며 Codex 모델 카탈로그의 기능 선언은 바뀌지 않습니다. | Before sending, strips images for models in the built-in confirmed text-only registry. Turning this off only disables the proxy's registry-based preflight; declared text-only handling and upstream-error fallback remain, and Codex model-catalog capability declarations are unchanged | 已修订 |
| settings.advanced.optimizer.title | Bedrock 请求优化器 | Bedrock 요청 최적화 | Bedrock Request Optimizer | 已修订 |
| settings.advanced.optimizer.description | 在请求发送前自动优化 Thinking 和 Cache 配置（仅 Bedrock 供应商生效） | 요청을 보내기 전에 Thinking 및 Cache 설정을 자동으로 최적화합니다(Bedrock 공급자에만 적용). | Automatically optimize Thinking and Cache configuration before sending requests (only applies to Bedrock providers) | 已修订 |
| settings.advanced.optimizer.enabled | 启用优化器 | 최적화 도구 활성화 | Enable Optimizer | 保留 |
| settings.advanced.optimizer.thinkingOptimizer | Thinking 优化 | Thinking 최적화 | Thinking Optimization | 已修订 |
| settings.advanced.optimizer.thinkingOptimizerDescription | 自动为 Opus/Sonnet 启用 Adaptive Thinking，为旧模型注入 Extended Thinking | Opus/Sonnet에는 Adaptive Thinking을 자동으로 활성화하고 이전 모델에는 Extended Thinking을 추가합니다. | Automatically enable Adaptive Thinking for Opus/Sonnet, and inject Extended Thinking for legacy models | 已修订 |
| settings.advanced.optimizer.cacheInjection | Cache 注入 | 캐시 주입 | Cache Injection | 保留 |
| settings.advanced.optimizer.cacheInjectionDescription | 自动在请求关键位置注入标准 5 分钟 Cache 断点，减少重复 token 计费 | 중복 토큰 청구를 줄이기 위해 주요 위치에 표준 5분 캐시 중단점을 자동으로 삽입합니다. | Automatically inject standard 5-minute cache breakpoints at key positions to reduce duplicate token billing | 保留 |
| settings.advanced.logConfig.title | 应用诊断日志 | 애플리케이션 진단 로그 | Application Diagnostic Logs | 保留 |
| settings.advanced.logConfig.description | 控制应用诊断日志的输出级别 | 애플리케이션 진단 로그의 출력 수준 제어 | Control the output level for application diagnostic logs | 保留 |
| settings.advanced.logConfig.enabled | 启用应用诊断日志 | 진단 로그 활성화 | Enable Diagnostic Logs | 保留 |
| settings.advanced.logConfig.enabledDescription | 控制 cc-switch.log；不影响请求用量记录和 crash.log | cc-switch.log를 제어합니다. 요청 사용 기록과 crash.log는 영향을 받지 않습니다. | Controls cc-switch.log; request usage records and crash.log are unaffected | 保留 |
| settings.advanced.logConfig.openLog | 打开日志 | 로그 열기 | Open log | 保留 |
| settings.advanced.logConfig.openLogFailed | 打开日志所在位置失败：{{error}} | 로그 위치를 열지 못했습니다: {{error}} | Failed to open the log location: {{error}} | 保留 |
| settings.advanced.logConfig.level | 日志级别 | 로그 수준 | Log Level | 保留 |
| settings.advanced.logConfig.levelDescription | 设置输出的最低日志级别 | 출력할 최소 로그 수준을 설정합니다 | Set the minimum log level to output | 已修订 |
| settings.advanced.logConfig.levels.error | 错误 | 오류 | Error | 保留 |
| settings.advanced.logConfig.levels.warn | 警告 | 경고 | Warning | 保留 |
| settings.advanced.logConfig.levels.info | 信息 | 정보 | Info | 保留 |
| settings.advanced.logConfig.levels.debug | 调试 | 디버그 | Debug | 保留 |
| settings.advanced.logConfig.levels.trace | 跟踪 | 추적 | Trace | 已修订 |
| settings.advanced.logConfig.levelDesc.error | 仅严重错误 | 심각한 오류만 | Critical errors only | 保留 |
| settings.advanced.logConfig.levelDesc.warn | 错误 + 警告信息 | 오류 + 경고 | Errors + warnings | 保留 |
| settings.advanced.logConfig.levelDesc.info | 一般操作信息（默认） | 일반 작업 정보(기본값) | General operation info (default) | 保留 |
| settings.advanced.logConfig.levelDesc.debug | 详细信息，包含 SSE 流和请求/响应详情 | SSE 스트림 및 요청/응답을 포함한 세부 정보 | Detailed info including SSE stream and request/response | 保留 |
| settings.advanced.logConfig.levelDesc.trace | 全部日志，最详细 | 모든 로그, 가장 자세한 로그 | All logs, most verbose | 保留 |
| settings.language | 界面语言 | 언어 | Language | 保留 |
| settings.languageHint | 切换后立即预览界面语言，保存后永久生效。 | 전환하면 인터페이스 언어를 즉시 미리 볼 수 있으며, 저장하면 변경 사항이 유지됩니다. | Preview interface language immediately after switching, takes effect permanently after saving. | 已修订 |
| settings.theme | 明暗 | 라이트 및 다크 모드 | Light & dark | 已修订 |
| settings.themeHint | 选择应用的外观主题，立即生效。 | 앱의 모양 테마를 선택하면 즉시 적용됩니다. | Choose the appearance theme for the app, takes effect immediately. | 保留 |
| settings.themeLight | 月之亮面 | 달의 밝은 면 | Light Side of the Moon | 已修订 |
| settings.themeDark | 月之暗面 | 달의 어두운 면 | Dark Side of the Moon | 已修订 |
| settings.themeSystem | 跟随系统 | 시스템 설정 따르기 | System | 已修订 |
| settings.importExport | SQL 导入导出 | SQL 가져오기/내보내기 | SQL Import/Export | 保留 |
| settings.importExportHint | 导入/导出数据库 SQL 备份（仅支持导入由 CC Switch 导出的备份），便于备份或迁移。 | 데이터베이스 SQL 백업을 가져오거나 내보내어 백업 또는 이전에 사용할 수 있습니다(CC Switch에서 내보낸 백업만 가져올 수 있습니다). | Import or export database SQL backups for migration or restore (import supports only backups exported by CC Switch). | 已修订 |
| settings.exportConfig | 导出 SQL 备份 | SQL 백업 내보내기 | Export SQL Backup | 保留 |
| settings.selectConfigFile | 选择 SQL 文件 | SQL 파일 선택 | Select SQL File | 保留 |
| settings.noFileSelected | 尚未选择配置文件。 | 선택한 설정 파일이 없습니다. | No configuration file selected. | 已修订 |
| settings.import | 导入 | 가져오기 | Import | 保留 |
| settings.importing | 导入中... | 가져오는 중... | Importing... | 保留 |
| settings.importSuccess | 导入成功！ | 가져오기 성공! | Import Successful! | 保留 |
| settings.importFailed | 导入失败 | 가져오기 실패 | Import Failed | 保留 |
| settings.syncLiveFailed | 已导入，但同步到当前供应商失败，请手动重新选择一次供应商。 | 가져왔지만 현재 공급자와 동기화하지 못했습니다. 공급자를 수동으로 다시 선택하십시오. | Imported, but failed to sync to the current provider. Please reselect the provider manually. | 已修订 |
| settings.importPartialSuccess | 配置已导入，但同步到当前供应商失败。 | 설정을 가져왔지만 현재 공급자와 동기화하지 못했습니다. | Config imported, but failed to sync to the current provider. | 已修订 |
| settings.importPartialHint | 请手动重新选择一次供应商以刷新对应配置。 | 현재 적용 중인 설정을 갱신하려면 공급자를 직접 다시 선택하세요. | Please manually reselect the provider to refresh the live configuration. | 已修订 |
| settings.configExported | 配置已导出到： | 설정을 다음으로 내보냈습니다. | Config exported to: | 已修订 |
| settings.exportFailed | 导出失败 | 내보내기 실패 | Export failed | 保留 |
| settings.selectFileFailed | 请选择有效的 SQL 备份文件 | 유효한 SQL 백업 파일을 선택하세요. | Please choose a valid SQL backup file | 保留 |
| settings.configCorrupted | SQL 文件可能已损坏或格式不正确 | SQL 파일이 손상되었거나 잘못되었을 수 있습니다. | SQL file may be corrupted or invalid | 保留 |
| settings.backupId | 备份ID | 백업 ID | Backup ID | 已修订 |
| settings.backupManager.title | 数据库备份 | 데이터베이스 백업 | Database Backups | 保留 |
| settings.backupManager.description | 自动备份的数据库快照，可用于恢复到之前的状态 | 이전 상태로 복원하기 위한 자동 데이터베이스 스냅샷 | Automatic database snapshots for restoring to a previous state | 保留 |
| settings.backupManager.empty | 暂无备份 | 아직 백업이 없습니다. | No backups yet | 保留 |
| settings.backupManager.restore | 恢复 | 복원 | Restore | 已修订 |
| settings.backupManager.restoring | 恢复中... | 복원 중... | Restoring... | 保留 |
| settings.backupManager.confirmTitle | 确认恢复备份 | 복원 확인 | Confirm Restore | 保留 |
| settings.backupManager.confirmMessage | 恢复到此备份将覆盖当前数据库。恢复前会自动创建安全备份。 | 이 백업을 복원하면 현재 데이터베이스를 덮어쓰게 됩니다. 먼저 안전 백업이 생성됩니다. | Restoring this backup will overwrite the current database. A safety backup will be created first. | 保留 |
| settings.backupManager.restoreSuccess | 恢复成功！安全备份已创建 | 복원에 성공했습니다! 안전 백업이 생성되었습니다. | Restore successful! Safety backup created | 保留 |
| settings.backupManager.restoreFailed | 恢复失败 | 복원 실패 | Restore failed | 保留 |
| settings.backupManager.safetyBackupId | 安全备份ID | 안전 백업 ID | Safety Backup ID | 已修订 |
| settings.backupManager.intervalLabel | 自动备份间隔 | 자동 백업 간격 | Auto-backup Interval | 保留 |
| settings.backupManager.retainLabel | 备份保留数量 | 보존할 백업 수 | Backup Retention | 已修订 |
| settings.backupManager.intervalDisabled | 禁用 | 비활성화됨 | Disabled | 保留 |
| settings.backupManager.intervalHours | {{hours}} 小时 | {{hours}}시간 | {{hours}} hours | 保留 |
| settings.backupManager.intervalDays | {{days}} 天 | {{days}}일 | {{days}} days | 保留 |
| settings.backupManager.rename | 重命名 | 이름 바꾸기 | Rename | 保留 |
| settings.backupManager.renameSuccess | 备份重命名成功 | 백업 이름이 변경됨 | Backup renamed | 保留 |
| settings.backupManager.renameFailed | 重命名失败 | 이름 바꾸기 실패 | Rename failed | 保留 |
| settings.backupManager.namePlaceholder | 输入新名称 | 새 이름을 입력하세요 | Enter new name | 保留 |
| settings.backupManager.createBackup | 立即备份 | 지금 백업 | Backup Now | 保留 |
| settings.backupManager.creating | 备份中... | 백업 중... | Backing up... | 保留 |
| settings.backupManager.createSuccess | 备份创建成功 | 백업이 성공적으로 생성되었습니다. | Backup created successfully | 保留 |
| settings.backupManager.createFailed | 备份创建失败 | 백업 실패 | Backup failed | 保留 |
| settings.backupManager.delete | 删除 | 삭제 | Delete | 保留 |
| settings.backupManager.deleting | 删除中... | 삭제 중... | Deleting... | 保留 |
| settings.backupManager.deleteSuccess | 备份已删除 | 백업이 삭제되었습니다. | Backup deleted | 保留 |
| settings.backupManager.deleteFailed | 删除失败 | 삭제 실패 | Delete failed | 保留 |
| settings.backupManager.deleteConfirmTitle | 确认删除备份 | 삭제 확인 | Confirm Delete | 保留 |
| settings.backupManager.deleteConfirmMessage | 此备份将被永久删除，此操作无法撤消。 | 이 백업은 영구적으로 삭제됩니다. 이 작업은 취소할 수 없습니다. | This backup will be permanently deleted. This action cannot be undone. | 保留 |
| settings.backupStorage.title | 其他备份 | 기타 백업 | Other Backups | 保留 |
| settings.backupStorage.total | 合计 {{size}} | 총 {{size}} | {{size}} total | 已修订 |
| settings.backupStorage.itemCount | {{count}} 项 | 항목: {{count}}개 | Items: {{count}} | 已修订 |
| settings.backupStorage.reveal | 在文件管理器中显示 | 파일 관리자에 표시 | Show in file manager | 保留 |
| settings.backupStorage.delete | 删除 | 삭제 | Delete | 保留 |
| settings.backupStorage.deleting | 删除中... | 삭제 중... | Deleting... | 保留 |
| settings.backupStorage.managedAbove | 在上方列表中管理 | 위 목록에서 관리됨 | Managed in the list above | 保留 |
| settings.backupStorage.legacy | 旧版遗留 | 이전 버전 | Legacy | 已修订 |
| settings.backupStorage.loadFailed | 读取备份占用失败 | 백업 디스크 사용량을 읽지 못했습니다 | Failed to read backup usage | 已修订 |
| settings.backupStorage.revealFailed | 打开文件夹失败 | 폴더를 열지 못했습니다. | Failed to open folder | 保留 |
| settings.backupStorage.deleteConfirmTitle | 删除「{{name}}」？ | '{{name}}'을(를) 삭제하시겠습니까? | Delete "{{name}}"? | 已修订 |
| settings.backupStorage.deleteConfirmMessage | 将永久删除 {{path}} 中的 {{size}} 备份，此操作无法撤消。 | {{path}}에 있는 {{size}} 용량의 백업을 영구적으로 삭제합니다. 이 작업은 취소할 수 없습니다. | {{size}} of backups in {{path}} will be permanently deleted. This cannot be undone. | 已修订 |
| settings.backupStorage.deleteSuccess | 已删除，释放 {{size}} | 삭제하여 {{size}}을(를) 확보했습니다 | Deleted, freed {{size}} | 已修订 |
| settings.backupStorage.deleteFailed | 删除失败 | 삭제 실패 | Delete failed | 保留 |
| settings.backupStorage.items.database.name | 数据库备份 | 데이터베이스 백업 | Database backups | 保留 |
| settings.backupStorage.items.database.hint | 自动备份与手动备份的数据库快照。 | 자동 및 수동 데이터베이스 스냅샷. | Automatic and manual database snapshots. | 保留 |
| settings.backupStorage.items.skills.name | Skill 卸载备份 | Skill 제거 시 백업 | Skill uninstall backups | 已修订 |
| settings.backupStorage.items.skills.hint | 卸载 Skill 前留的副本，可在 Skills 页恢复。删除后这些已卸载的 Skill 无法再恢复。 | Skills를 제거할 때 보관한 복사본으로, Skills 페이지에서 복원할 수 있습니다. 삭제하면 제거된 Skills를 더 이상 복원할 수 없습니다. | Copies kept when uninstalling skills, restorable from the Skills page. After deleting, those uninstalled skills can no longer be restored. | 已修订 |
| settings.backupStorage.items.codexHistoryUnify.name | Codex 会话统一迁移备份 | Codex 세션 통합 마이그레이션 백업 | Codex session unify migration backups | 已修订 |
| settings.backupStorage.items.codexHistoryUnify.hint | 开启「统一 Codex 会话历史」并迁入既有会话时留的会话副本。关闭该开关时的「恢复备份」依赖它，删除后无法再把迁移过的官方会话还原回原分组。 | ‘Codex 세션 기록 통합’으로 기존 세션을 옮길 때 보관한 복사본입니다. 해당 기능을 끌 때 ‘백업 복원’에 사용합니다. 삭제하면 옮긴 공식 세션을 원래 그룹으로 되돌릴 수 없습니다. | Session copies kept when "Unified Codex session history" migrated existing sessions. "Restore backup" when turning that switch off depends on them; after deleting, migrated official sessions can no longer be moved back to their original group. | 已修订 |
| settings.backupStorage.items.codexHistoryUnifyRestore.name | Codex 会话统一还原备份 | Codex 세션 통합 복원 전 백업 | Codex session unify restore backups | 已修订 |
| settings.backupStorage.items.codexHistoryUnifyRestore.hint | 执行「恢复备份」前留的会话副本，CC Switch 不会再读取。 | "백업 복원"이 실행되기 전에 보관된 세션 복사본입니다. CC Switch는 다시는 읽지 않습니다. | Session copies kept before "Restore backup" ran. CC Switch never reads them again. | 保留 |
| settings.backupStorage.items.codexHistoryProviderMigration.name | Codex 会话分组迁移备份 | Codex 세션 그룹 마이그레이션 백업 | Codex session group migration backups | 保留 |
| settings.backupStorage.items.codexHistoryProviderMigration.hint | 会话分组迁移前留的副本，CC Switch 不会再读取。 | 세션 그룹이 마이그레이션되기 전에 보관된 복사본입니다. CC Switch는 다시는 읽지 않습니다. | Copies kept before session groups were migrated. CC Switch never reads them again. | 保留 |
| settings.backupStorage.items.liveFirstWrite.name | 配置文件首次写入备份 | 설정 파일 최초 저장 전 백업 | Config first-write backups | 已修订 |
| settings.backupStorage.items.liveFirstWrite.hint | CC Switch 第一次改写各客户端配置文件前的原始文件。删除后无法再找回改写前的原文件，下次写入时会重新备份当时的文件。 | CC Switch가 각 클라이언트의 설정 파일을 처음 변경하기 전에 보관한 원본입니다. 삭제하면 변경 전 원본을 복구할 수 없으며, 다음 저장 시에는 그 시점의 파일을 다시 백업합니다. | Original client config files from before CC Switch first rewrote them. After deleting, those originals are gone; the next write backs up the file as it is then. | 已修订 |
| settings.backupStorage.items.hermes.name | Hermes 配置备份 | Hermes 설정 백업 | Hermes config backups | 已修订 |
| settings.backupStorage.items.hermes.hint | 保存 Hermes 配置前的副本，按「备份保留数量」自动裁剪。 | Hermes 설정 저장 전에 보관한 복사본으로, 백업 보존 정책에 따라 정리됩니다. | Copies kept before saving Hermes config, pruned by Backup Retention. | 已修订 |
| settings.backupStorage.items.openclaw.name | OpenClaw 配置备份 | OpenClaw 설정 백업 | OpenClaw config backups | 已修订 |
| settings.backupStorage.items.openclaw.hint | 保存 OpenClaw 配置前的副本，按「备份保留数量」自动裁剪。 | OpenClaw 설정 저장 전에 보관한 복사본으로, 백업 보존 정책에 따라 정리됩니다. | Copies kept before saving OpenClaw config, pruned by Backup Retention. | 已修订 |
| settings.backupStorage.items.proxyLiveBackup.name | 旧版路由接管备份 | 이전 버전의 라우팅 관리 백업 | Legacy routing takeover backups | 已修订 |
| settings.backupStorage.items.proxyLiveBackup.hint | 升级时从旧版路由接管备份转存出的配置副本，CC Switch 不会再读取。 | 업그레이드 시 이전 버전의 라우팅 관리 백업에서 옮겨 보관한 설정 복사본입니다. CC Switch는 더 이상 읽지 않습니다. | Config copies moved out of the old routing takeover backups during upgrade. CC Switch never reads them again. | 已修订 |
| settings.backupStorage.items.envVars.name | 环境变量清理备份 | 환경 변수 정리 백업 | Environment variable cleanup backups | 保留 |
| settings.backupStorage.items.envVars.hint | 清理冲突环境变量前记录的原值。删除后无法再查到被清理变量的原值。 | 충돌하는 환경 변수가 제거되기 전에 기록된 원래 값입니다. 삭제한 후에는 해당 값을 더 이상 조회할 수 없습니다. | Original values recorded before conflicting environment variables were removed. After deleting, those values can no longer be looked up. | 保留 |
| settings.backupStorage.items.legacyConfigBackups.name | 旧版 config.json 备份 | 레거시 config.json 백업 | Legacy config.json backups | 保留 |
| settings.backupStorage.items.legacyConfigBackups.hint | 旧版本留下的文件，当前版本不会再读取。 | 이전 버전에서 남았습니다. 현재 버전에서는 더 이상 읽지 않습니다. | Left by older versions; the current version no longer reads them. | 保留 |
| settings.backupStorage.items.legacyConfigArchive.name | 旧版 config.json 归档 | 레거시 config.json 아카이브 | Legacy config.json archive | 保留 |
| settings.backupStorage.items.legacyConfigArchive.hint | 迁移到数据库前的旧配置文件，当前版本不会再读取。 | 데이터베이스 마이그레이션 전의 이전 설정 파일. 현재 버전에서는 더 이상 읽지 않습니다. | The old config file from before the database migration; the current version no longer reads it. | 已修订 |
| settings.backupStorage.items.legacyDbUpgrade.name | 旧版数据库升级备份 | 레거시 데이터베이스 업그레이드 백업 | Legacy database upgrade backups | 保留 |
| settings.backupStorage.items.legacyDbUpgrade.hint | 旧版本升级数据库时留的副本，当前版本不会再读取。 | 데이터베이스를 업그레이드할 때 이전 버전에서 만들어진 복사본. 현재 버전에서는 더 이상 읽지 않습니다. | Copies made by older versions when upgrading the database; the current version no longer reads them. | 保留 |
| settings.backupStorage.items.legacyToolSearch.name | 旧版 Tool Search 补丁备份 | 레거시 Tool Search 패치 백업 | Legacy Tool Search patch backups | 已修订 |
| settings.backupStorage.items.legacyToolSearch.hint | 已移除的 Tool Search 补丁功能留下的文件，当前版本不会再读取。 | 제거된 Tool Search 패치 기능으로 인해 남았습니다. 현재 버전에서는 더 이상 읽지 않습니다. | Left by the removed Tool Search patch feature; the current version no longer reads them. | 已修订 |
| settings.webdavSync.title | WebDAV 云同步 | WebDAV 클라우드 동기화 | WebDAV Cloud Sync | 保留 |
| settings.webdavSync.baseUrl | WebDAV 服务器地址 | WebDAV 서버 URL | WebDAV Server URL | 保留 |
| settings.webdavSync.baseUrlPlaceholder | https://dav.jianguoyun.com/dav/ | https://dav.example.com/dav/ | https://dav.example.com/dav/ | 保留 |
| settings.webdavSync.username | WebDAV 账户 | WebDAV 계정 | WebDAV Account | 保留 |
| settings.webdavSync.usernamePlaceholder | 邮箱账号 | 이메일 계정 | Email or username | 已修订 |
| settings.webdavSync.password | WebDAV 密码 | WebDAV 비밀번호 | WebDAV Password | 保留 |
| settings.webdavSync.passwordPlaceholder | 应用密码（坚果云请使用「第三方应用密码」） | 앱 비밀번호 | App password | 保留 |
| settings.webdavSync.remoteRoot | 远程根目录 | 원격 루트 디렉터리 | Remote Root Directory | 保留 |
| settings.webdavSync.profile | 同步配置名 | 동기화 프로필 이름 | Sync Profile Name | 保留 |
| settings.webdavSync.autoSync | 自动同步 | 자동 동기화 | Auto Sync | 保留 |
| settings.webdavSync.autoSyncHint | 开启后每次数据库变更都会自动上传到 WebDAV。 | 활성화되면 각 데이터베이스 변경으로 인해 자동 WebDAV 업로드가 트리거됩니다. | When enabled, each database change triggers an automatic WebDAV upload. | 保留 |
| settings.webdavSync.test | 测试连接 | 연결 테스트 | Test Connection | 保留 |
| settings.webdavSync.testing | 测试中... | 테스트 중... | Testing... | 保留 |
| settings.webdavSync.testSuccess | 连接成功 | 연결 성공 | Connection successful | 保留 |
| settings.webdavSync.testFailed | 连接失败：{{error}} | 연결 실패: {{error}} | Connection failed: {{error}} | 保留 |
| settings.webdavSync.save | 保存配置 | 설정 저장 | Save Config | 已修订 |
| settings.webdavSync.saving | 保存中... | 저장 중... | Saving... | 保留 |
| settings.webdavSync.saveFailed | 保存配置失败：{{error}} | 설정 저장 실패: {{error}} | Failed to save config: {{error}} | 已修订 |
| settings.webdavSync.upload | 上传到云端 | 클라우드에 업로드 | Upload to Cloud | 保留 |
| settings.webdavSync.uploading | 上传中... | 업로드 중... | Uploading... | 保留 |
| settings.webdavSync.uploadSuccess | 已上传到 WebDAV | WebDAV에 업로드됨 | Uploaded to WebDAV | 保留 |
| settings.webdavSync.uploadFailed | 上传失败：{{error}} | 업로드 실패: {{error}} | Upload failed: {{error}} | 保留 |
| settings.webdavSync.autoSyncFailedToast | 自动同步失败：{{error}} | 자동 동기화 실패: {{error}} | Auto sync failed: {{error}} | 保留 |
| settings.webdavSync.download | 从云端下载 | 클라우드에서 다운로드 | Download from Cloud | 保留 |
| settings.webdavSync.downloading | 下载中... | 다운로드 중... | Downloading... | 保留 |
| settings.webdavSync.downloadSuccess | 已从 WebDAV 下载并恢复 | WebDAV에서 다운로드 및 복원됨 | Downloaded and restored from WebDAV | 保留 |
| settings.webdavSync.downloadFailed | 下载失败：{{error}} | 다운로드 실패: {{error}} | Download failed: {{error}} | 保留 |
| settings.webdavSync.lastSync | 上次同步：{{time}} | 마지막 동기화: {{time}} | Last sync: {{time}} | 保留 |
| settings.webdavSync.autoSyncLastErrorTitle | 上次自动同步失败 | 마지막 자동 동기화 실패 | Last auto sync failed | 保留 |
| settings.webdavSync.autoSyncLastErrorHint | 请检查网络或 WebDAV 配置，系统会在后续变更时继续自动重试。 | 네트워크 또는 WebDAV 설정을 확인하세요. 다음 데이터 변경 시 자동 동기화를 다시 시도합니다. | Please check network or WebDAV settings. Auto sync will retry on future changes. | 已修订 |
| settings.webdavSync.missingUrl | 请填写 WebDAV 服务器地址 | WebDAV 서버 URL을 입력하세요 | Please enter the WebDAV server URL | 保留 |
| settings.webdavSync.presets.label | 服务商 | 공급자 | Provider | 已修订 |
| settings.webdavSync.presets.jianguoyun | 坚果云 | Jianguoyun | Jianguoyun | 已修订 |
| settings.webdavSync.presets.jianguoyunHint | 请在坚果云「安全选项」中生成「第三方应用密码」，不要使用登录密码。 | Jianguoyun의 ‘보안 옵션’에서 ‘타사 앱 비밀번호’를 생성하세요. 로그인 비밀번호를 사용하지 마세요. | Generate an "App Password" in Jianguoyun security settings. Do not use your login password. | 已修订 |
| settings.webdavSync.presets.nextcloud | Nextcloud | Nextcloud | Nextcloud | 已修订 |
| settings.webdavSync.presets.nextcloudHint | 请将 your-server 替换为你的 Nextcloud 服务器地址，USERNAME 替换为你的用户名。 | your-server를 Nextcloud 도메인으로 바꾸고 USERNAME을 사용자 이름으로 바꾸세요. | Replace your-server with your Nextcloud domain and USERNAME with your username. | 保留 |
| settings.webdavSync.presets.synology | 群晖 NAS | Synology NAS | Synology NAS | 已修订 |
| settings.webdavSync.presets.synologyHint | 请先在群晖「套件中心」安装并启用 WebDAV Server 套件。 | 먼저 Synology 패키지 센터에서 WebDAV Server 패키지를 설치하고 활성화하세요. | Install and enable the WebDAV Server package in Synology Package Center first. | 已修订 |
| settings.webdavSync.presets.custom | 自定义 | 사용자 지정 | Custom | 保留 |
| settings.webdavSync.saveAndTestSuccess | 配置已保存，连接正常 | 설정이 저장되었습니다. 연결이 정상입니다. | Config saved, connection OK | 已修订 |
| settings.webdavSync.saveAndTestFailed | 配置已保存，但连接测试失败：{{error}} | 설정이 저장되었지만 연결 테스트에 실패했습니다: {{error}} | Config saved, but connection test failed: {{error}} | 已修订 |
| settings.webdavSync.noRemoteData | 云端没有找到同步数据 | 원격 서버에서 동기화 데이터를 찾을 수 없습니다. | No sync data found on the remote server | 保留 |
| settings.webdavSync.incompatibleVersion | 远端数据版本不兼容（协议 v{{protocolVersion}}，数据库 {{dbCompatVersion}}），当前支持协议 v2 / db-v6 | 원격 데이터가 호환되지 않습니다(프로토콜 v{{protocolVersion}}, 데이터베이스 {{dbCompatVersion}}). 이 클라이언트는 프로토콜 v2 / db-v6을 지원합니다. | Remote data is incompatible (protocol v{{protocolVersion}}, database {{dbCompatVersion}}). This client supports protocol v2 / db-v6. | 保留 |
| settings.webdavSync.unsaved | 未保存 | 저장되지 않음 | Unsaved | 保留 |
| settings.webdavSync.saved | 已保存 | 저장됨 | Saved | 保留 |
| settings.webdavSync.unsavedChanges | 请先保存配置 | 먼저 설정을 저장하세요. | Please save config first | 已修订 |
| settings.webdavSync.saveBeforeSync | 请先保存配置，再使用上传/下载。 | 업로드/다운로드를 활성화하려면 먼저 설정을 저장하세요. | Save configuration first to enable upload/download. | 已修订 |
| settings.webdavSync.fetchingRemote | 获取远端信息... | 원격 정보를 가져오는 중... | Fetching remote info... | 保留 |
| settings.webdavSync.fetchRemoteFailed | 获取远端信息失败，请检查配置和网络后重试。 | 원격 정보를 가져오지 못했습니다. 설정과 네트워크를 확인하세요. | Failed to fetch remote info. Please check configuration and network. | 已修订 |
| settings.webdavSync.confirmDownload.title | 从云端恢复 | 클라우드에서 복원 | Restore from Cloud | 保留 |
| settings.webdavSync.confirmDownload.deviceName | 上传设备 | 업로드한 기기 | Uploaded by | 已修订 |
| settings.webdavSync.confirmDownload.createdAt | 上传时间 | 업로드 시간 | Uploaded at | 保留 |
| settings.webdavSync.confirmDownload.path | 远端路径 | 원격 경로 | Remote path | 保留 |
| settings.webdavSync.confirmDownload.dbCompat | 数据库兼容层 | DB 호환성 | DB compatibility | 保留 |
| settings.webdavSync.confirmDownload.artifacts | 包含内容 | 포함된 항목 | Contents | 已修订 |
| settings.webdavSync.confirmDownload.legacyNotice | 检测到旧版云端路径。恢复完成后，下次上传将写入新路径 v2/db-v6。 | 이전 버전의 클라우드 경로가 감지되었습니다. 복원이 끝나면 다음 업로드부터 새 경로 v2/db-v6에 저장합니다. | A legacy remote path was detected. After restoring, the next upload will write to the new v2/db-v6 path. | 已修订 |
| settings.webdavSync.confirmDownload.warning | 恢复将覆盖本地所有数据和技能配置 | 모든 로컬 데이터와 Skills 설정을 덮어씁니다 | This will overwrite all local data and skill configurations | 已修订 |
| settings.webdavSync.confirmDownload.confirm | 确认恢复 | 복원 확인 | Confirm Restore | 保留 |
| settings.webdavSync.confirmUpload.title | 上传到云端 | 클라우드에 업로드 | Upload to Cloud | 保留 |
| settings.webdavSync.confirmUpload.content | 将同步以下内容到 WebDAV 服务器： | 다음은 WebDAV 서버에 동기화됩니다. | The following will be synced to the WebDAV server: | 保留 |
| settings.webdavSync.confirmUpload.dbItem | 数据库（所有 Provider 配置和数据） | 데이터베이스(모든 공급자 설정 및 데이터) | Database (all provider configs and data) | 已修订 |
| settings.webdavSync.confirmUpload.skillsItem | 技能包（所有自定义技能） | Skills (모든 사용자 지정 Skills) | Skills (all custom skills) | 已修订 |
| settings.webdavSync.confirmUpload.targetPath | 目标路径 | 대상 경로 | Target path | 保留 |
| settings.webdavSync.confirmUpload.existingData | 云端已有数据 | 기존 클라우드 데이터 | Existing cloud data | 保留 |
| settings.webdavSync.confirmUpload.deviceName | 上传设备 | 업로드한 기기 | Uploaded by | 已修订 |
| settings.webdavSync.confirmUpload.createdAt | 上传时间 | 업로드 시간 | Uploaded at | 保留 |
| settings.webdavSync.confirmUpload.path | 远端路径 | 원격 경로 | Remote path | 保留 |
| settings.webdavSync.confirmUpload.dbCompat | 数据库兼容层 | DB 호환성 | DB compatibility | 保留 |
| settings.webdavSync.confirmUpload.warning | 将覆盖云端已有的同步数据 | 원격 서버의 기존 동기화 데이터를 덮어쓰게 됩니다. | This will overwrite existing sync data on the remote server | 保留 |
| settings.webdavSync.confirmUpload.legacyNotice | 检测到旧版云端路径数据。本次上传将写入新路径 v2/db-v6，不会覆盖旧路径。 | 이전 버전의 클라우드 경로에 있는 데이터가 감지되었습니다. 이번 업로드는 새 경로 v2/db-v6에 저장하며 이전 경로는 덮어쓰지 않습니다. | Legacy remote data was detected. This upload will write to the new v2/db-v6 path and will not overwrite the legacy path. | 已修订 |
| settings.webdavSync.confirmUpload.confirm | 确认上传 | 업로드 확인 | Confirm Upload | 保留 |
| settings.syncType.label | 同步方式 | 동기화 유형 | Sync Type | 保留 |
| settings.syncType.webdav | WebDAV | WebDAV | WebDAV | 保留 |
| settings.syncType.s3 | S3 兼容存储 | S3 호환 | S3 Compatible | 保留 |
| settings.s3Sync.presets.label | 服务商 | 공급자 | Provider | 已修订 |
| settings.s3Sync.presets.awsS3 | AWS S3 | AWS S3 | AWS S3 | 保留 |
| settings.s3Sync.presets.awsS3Hint | 使用 IAM Access Key，需要 s3:PutObject/GetObject/HeadObject 权限。Region 示例：us-east-1, ap-northeast-1 | s3:PutObject/GetObject/HeadObject 권한이 있는 IAM 액세스 키를 사용하세요. 지역: us-east-1, ap-northeast-1 등 | Use IAM Access Key with s3:PutObject/GetObject/HeadObject permissions. Region: us-east-1, ap-northeast-1, etc. | 保留 |
| settings.s3Sync.presets.minio | MinIO | MinIO | MinIO | 已修订 |
| settings.s3Sync.presets.minioHint | 需要自定义 Endpoint，如 http://minio.local:9000。Region 可设为 us-east-1 | 커스텀 엔드포인트가 필요합니다. 예: http://minio.local:9000. 지역은 'us-east-1'일 수 있습니다. | Custom endpoint required, e.g. http://minio.local:9000. Region can be 'us-east-1'. | 保留 |
| settings.s3Sync.presets.r2 | Cloudflare R2 | Cloudflare R2 | Cloudflare R2 | 已修订 |
| settings.s3Sync.presets.r2Hint | Endpoint: https://<account_id>.r2.cloudflarestorage.com，Region 设为 auto | 엔드포인트: https://<account_id>.r2.cloudflarestorage.com. 리전: 'auto'. | Endpoint: https://<account_id>.r2.cloudflarestorage.com. Region: 'auto'. | 已修订 |
| settings.s3Sync.presets.oss | 阿里云 OSS | Alibaba Cloud OSS | Alibaba Cloud OSS | 已修订 |
| settings.s3Sync.presets.ossHint | Endpoint: https://oss-<region>.aliyuncs.com，Region 示例：cn-hangzhou, cn-shanghai | 엔드포인트: https://oss-<region>.aliyuncs.com. 리전: cn-hangzhou, cn-shanghai 등 | Endpoint: https://oss-<region>.aliyuncs.com. Region: cn-hangzhou, cn-shanghai, etc. | 已修订 |
| settings.s3Sync.presets.cos | 腾讯云 COS | Tencent Cloud COS | Tencent Cloud COS | 已修订 |
| settings.s3Sync.presets.cosHint | Endpoint: https://cos.<region>.myqcloud.com，Region 示例：ap-guangzhou, ap-beijing | 엔드포인트: https://cos.<region>.myqcloud.com. 지역: ap-guangzhou, ap-beijing 등 | Endpoint: https://cos.<region>.myqcloud.com. Region: ap-guangzhou, ap-beijing, etc. | 保留 |
| settings.s3Sync.presets.obs | 华为云 OBS | Huawei OBS | Huawei OBS | 已修订 |
| settings.s3Sync.presets.obsHint | Endpoint: https://obs.<region>.myhuaweicloud.com，Region 示例：cn-north-4, cn-east-3 | 엔드포인트: https://obs.<region>.myhuaweicloud.com. 리전: cn-north-4, cn-east-3 등 | Endpoint: https://obs.<region>.myhuaweicloud.com. Region: cn-north-4, cn-east-3, etc. | 已修订 |
| settings.s3Sync.presets.custom | S3 兼容服务（自定义） | S3 호환 (사용자 지정) | S3 Compatible (Custom) | 已修订 |
| settings.s3Sync.presets.customHint | 任意 S3 兼容服务，需要自定义 Endpoint | 모든 S3 호환 서비스를 지원합니다. 사용자 지정 엔드포인트가 필요합니다. | Any S3-compatible service. Custom endpoint required. | 已修订 |
| settings.s3Sync.region | 区域 (Region) | 리전 | Region | 已修订 |
| settings.s3Sync.regionPlaceholder | 例如 us-east-1 | 예: us-east-1 | e.g. us-east-1 | 已修订 |
| settings.s3Sync.bucket | 存储桶 (Bucket) | 버킷 | Bucket | 保留 |
| settings.s3Sync.bucketPlaceholder | 例如 my-cc-switch-bucket | 예: my-cc-switch-bucket | e.g. my-cc-switch-bucket | 已修订 |
| settings.s3Sync.accessKeyId | Access Key ID | 액세스 키 ID | Access Key ID | 保留 |
| settings.s3Sync.accessKeyIdPlaceholder | 例如 AKIA... | 예: AKIA... | e.g. AKIA... | 已修订 |
| settings.s3Sync.secretAccessKey | Secret Access Key | 비밀 액세스 키 | Secret Access Key | 保留 |
| settings.s3Sync.secretAccessKeyPlaceholder | 留空则保持现有密钥 | 비워 두면 기존 비밀 키 유지 | Leave unchanged to keep the existing secret | 已修订 |
| settings.s3Sync.endpoint | Endpoint（AWS 可留空） | 엔드포인트(AWS의 경우 선택 사항) | Endpoint (optional for AWS) | 保留 |
| settings.s3Sync.endpointHint | 多数 S3 兼容服务需要填写 | 대부분의 S3 호환 서비스에 필요 | Required for most S3-compatible services | 保留 |
| settings.s3Sync.endpointPlaceholder | 例如 https://s3-compatible.example.com | 예를 들어 https://s3-compatible.example.com | e.g. https://s3-compatible.example.com | 保留 |
| settings.s3Sync.remoteRoot | 远程根目录 | 원격 루트 디렉터리 | Remote Root Directory | 保留 |
| settings.s3Sync.profile | 同步配置名 | 동기화 프로필 이름 | Sync Profile Name | 保留 |
| settings.s3Sync.autoSync | 自动同步 | 자동 동기화 | Auto Sync | 保留 |
| settings.s3Sync.autoSyncHint | 开启后每次数据库变更都会自动上传到 S3。 | 활성화되면 각 데이터베이스 변경으로 인해 자동 S3 업로드가 트리거됩니다. | When enabled, each database change triggers an automatic S3 upload. | 保留 |
| settings.s3Sync.enabled | 启用 S3 同步 | S3 동기화 활성화 | Enable S3 Sync | 保留 |
| settings.s3Sync.enabledHint | 开启后可使用 S3 上传/下载和自动同步。 | 켜면 S3 업로드/다운로드 및 자동 동기화를 사용할 수 있습니다. | Turn on S3 sync for manual and automatic cloud operations. | 已修订 |
| settings.s3Sync.mutualExclusionTitle | 切换同步方式 | 동기화 유형 전환 | Switch Sync Type | 已修订 |
| settings.s3Sync.mutualExclusionMessage | 启用 S3 同步将禁用当前的 WebDAV 同步，是否继续？ | S3 동기화를 켜면 현재 WebDAV 동기화가 꺼집니다. 계속하시겠습니까? | Enabling S3 sync will disable the current WebDAV sync. Continue? | 已修订 |
| settings.s3Sync.mutualExclusionMessageReverse | 启用 WebDAV 同步将禁用当前的 S3 同步，是否继续？ | WebDAV 동기화를 켜면 현재 S3 동기화가 꺼집니다. 계속하시겠습니까? | Enabling WebDAV sync will disable the current S3 sync. Continue? | 已修订 |
| settings.s3Sync.mutualExclusionFailed | 切换同步方式失败：{{error}} | 동기화 유형 전환 실패: {{error}} | Failed to switch sync type: {{error}} | 保留 |
| settings.s3Sync.testConnection | 测试连接 | 연결 테스트 | Test Connection | 保留 |
| settings.s3Sync.connectionOk | S3 连接成功 | S3 연결 성공 | S3 connection successful | 保留 |
| settings.s3Sync.test | 测试连接 | 연결 테스트 | Test Connection | 保留 |
| settings.s3Sync.testing | 测试中... | 테스트 중... | Testing... | 保留 |
| settings.s3Sync.testSuccess | S3 连接成功 | S3 연결 성공 | S3 connection successful | 保留 |
| settings.s3Sync.testFailed | S3 连接失败：{{error}} | S3 연결 실패: {{error}} | S3 connection failed: {{error}} | 保留 |
| settings.s3Sync.save | 保存配置 | 설정 저장 | Save Config | 已修订 |
| settings.s3Sync.saving | 保存中... | 저장 중... | Saving... | 保留 |
| settings.s3Sync.saveFailed | 保存配置失败：{{error}} | 설정 저장 실패: {{error}} | Failed to save config: {{error}} | 已修订 |
| settings.s3Sync.saveAndTestSuccess | 配置已保存，S3 连接正常 | 설정이 저장되었습니다. S3 연결이 정상입니다. | Config saved, S3 connection OK | 已修订 |
| settings.s3Sync.saveAndTestFailed | 配置已保存，但 S3 连接测试失败：{{error}} | 설정이 저장되었지만 S3 연결 테스트 실패: {{error}} | Config saved, but S3 connection test failed: {{error}} | 已修订 |
| settings.s3Sync.upload | 上传到云端 | 클라우드에 업로드 | Upload to Cloud | 保留 |
| settings.s3Sync.uploading | 上传中... | 업로드 중... | Uploading... | 保留 |
| settings.s3Sync.uploadSuccess | 已上传到 S3 | S3에 업로드됨 | Uploaded to S3 | 保留 |
| settings.s3Sync.uploadFailed | S3 上传失败：{{error}} | S3 업로드 실패: {{error}} | S3 upload failed: {{error}} | 保留 |
| settings.s3Sync.autoSyncFailedToast | S3 自动同步失败：{{error}} | S3 자동 동기화 실패: {{error}} | S3 auto sync failed: {{error}} | 保留 |
| settings.s3Sync.download | 从云端下载 | 클라우드에서 다운로드 | Download from Cloud | 保留 |
| settings.s3Sync.downloading | 下载中... | 다운로드 중... | Downloading... | 保留 |
| settings.s3Sync.downloadSuccess | 已从 S3 下载并恢复 | S3에서 다운로드 및 복원됨 | Downloaded and restored from S3 | 保留 |
| settings.s3Sync.downloadFailed | S3 下载失败：{{error}} | S3 다운로드 실패: {{error}} | S3 download failed: {{error}} | 保留 |
| settings.s3Sync.lastSync | 上次同步：{{time}} | 마지막 동기화: {{time}} | Last sync: {{time}} | 保留 |
| settings.s3Sync.autoSyncLastErrorTitle | 上次 S3 自动同步失败 | 마지막 S3 자동 동기화 실패 | Last S3 auto sync failed | 保留 |
| settings.s3Sync.autoSyncLastErrorHint | 请检查网络或 S3 配置，系统会在后续变更时继续自动重试。 | 네트워크 또는 S3 설정을 확인하세요. 다음 데이터 변경 시 자동 동기화를 다시 시도합니다. | Please check network or S3 settings. Auto sync will retry on future changes. | 已修订 |
| settings.s3Sync.missingBucket | 请填写 S3 存储桶 | S3 버킷을 입력하세요. | Please enter the S3 bucket | 保留 |
| settings.s3Sync.noRemoteData | S3 存储桶中没有找到同步数据 | S3 버킷에 동기화 데이터가 없습니다. | No sync data found in the S3 bucket | 保留 |
| settings.s3Sync.incompatibleVersion | 远端数据版本不兼容（版本 {{version}}），当前支持协议 v2 / db-v6 | 원격 데이터가 호환되지 않습니다(버전 {{version}}). 이 클라이언트는 프로토콜 v2 / db-v6을 지원합니다. | Remote data is incompatible (version {{version}}). This client supports protocol v2 / db-v6. | 保留 |
| settings.s3Sync.unsaved | 未保存 | 저장되지 않음 | Unsaved | 保留 |
| settings.s3Sync.saved | 已保存 | 저장됨 | Saved | 保留 |
| settings.s3Sync.unsavedChanges | 请先保存配置 | 먼저 설정을 저장하세요. | Please save config first | 已修订 |
| settings.s3Sync.saveBeforeSync | 请先保存配置，再使用上传/下载。 | 업로드/다운로드를 활성화하려면 먼저 설정을 저장하세요. | Save configuration first to enable upload/download. | 已修订 |
| settings.s3Sync.fetchingRemote | 获取远端信息... | 원격 정보를 가져오는 중... | Fetching remote info... | 保留 |
| settings.s3Sync.fetchRemoteFailed | 获取远端信息失败，请检查配置和网络后重试。 | 원격 정보를 가져오지 못했습니다. 설정과 네트워크를 확인하세요. | Failed to fetch remote info. Please check configuration and network. | 已修订 |
| settings.s3Sync.notConfigured | 未配置 S3 同步 | S3 동기화가 설정되지 않았습니다. | S3 sync is not configured | 已修订 |
| settings.s3Sync.disabled | S3 同步未启用 | S3 동기화가 비활성화되었습니다 | S3 sync is disabled | 保留 |
| settings.s3Sync.confirmDownload.title | 从 S3 恢复 | S3에서 복원 | Restore from S3 | 保留 |
| settings.s3Sync.confirmDownload.deviceName | 上传设备 | 업로드한 기기 | Uploaded by | 已修订 |
| settings.s3Sync.confirmDownload.createdAt | 上传时间 | 업로드 시간 | Uploaded at | 保留 |
| settings.s3Sync.confirmDownload.artifacts | 包含内容 | 포함된 항목 | Contents | 已修订 |
| settings.s3Sync.confirmDownload.warning | 恢复将覆盖本地所有数据和技能配置 | 모든 로컬 데이터와 Skills 설정을 덮어씁니다 | This will overwrite all local data and skill configurations | 已修订 |
| settings.s3Sync.confirmDownload.confirm | 确认恢复 | 복원 확인 | Confirm Restore | 保留 |
| settings.s3Sync.confirmUpload.title | 上传到 S3 | S3에 업로드 | Upload to S3 | 保留 |
| settings.s3Sync.confirmUpload.content | 将同步以下内容到 S3 存储桶： | 다음은 S3 버킷에 동기화됩니다. | The following will be synced to the S3 bucket: | 保留 |
| settings.s3Sync.confirmUpload.dbItem | 数据库（所有 Provider 配置和数据） | 데이터베이스(모든 공급자 설정 및 데이터) | Database (all provider configs and data) | 已修订 |
| settings.s3Sync.confirmUpload.skillsItem | 技能包（所有自定义技能） | Skills (모든 사용자 지정 Skills) | Skills (all custom skills) | 已修订 |
| settings.s3Sync.confirmUpload.targetPath | 目标对象路径 | 대상 개체 경로 | Target object path | 保留 |
| settings.s3Sync.confirmUpload.existingData | 云端已有数据 | 기존 클라우드 데이터 | Existing cloud data | 保留 |
| settings.s3Sync.confirmUpload.deviceName | 上传设备 | 업로드한 기기 | Uploaded by | 已修订 |
| settings.s3Sync.confirmUpload.createdAt | 上传时间 | 업로드 시간 | Uploaded at | 保留 |
| settings.s3Sync.confirmUpload.warning | 将覆盖该 S3 路径下已有的同步数据 | 이렇게 하면 S3 경로의 기존 동기화 데이터가 덮어쓰여집니다. | This will overwrite existing sync data at the S3 path | 保留 |
| settings.s3Sync.confirmUpload.confirm | 确认上传 | 업로드 확인 | Confirm Upload | 保留 |
| settings.autoReload | 数据已刷新 | 데이터를 새로 고쳤습니다 | Data refreshed | 已修订 |
| settings.languageOptionChinese | 简体中文 | 简体中文 | 简体中文 | 保留 |
| settings.languageOptionTraditionalChinese | 繁體中文 | 繁體中文 | 繁體中文 | 保留 |
| settings.languageOptionEnglish | English | English | English | 已修订 |
| settings.languageOptionJapanese | 日本語 | 日本語 | 日本語 | 保留 |
| settings.languageOptionTurkish | Türkçe | Türkçe | Türkçe | 已修订 |
| settings.languageOptionKorean | 한국어 | 한국어 | 한국어 | 保留 |
| settings.windowBehavior | 窗口行为 | 창 동작 | Window Behavior | 保留 |
| settings.windowBehaviorHint | 配置窗口最小化与 Claude 插件联动策略。 | 창 최소화 및 Claude 플러그인 통합 정책을 설정합니다. | Configure window minimize and Claude plugin integration policies. | 已修订 |
| settings.launchOnStartup | 开机自启 | 시작 시 실행 | Launch on Startup | 保留 |
| settings.launchOnStartupDescription | 随系统启动自动运行 CC Switch | 시스템 시작 시 자동으로 CC Switch 실행 | Automatically run CC Switch when system starts | 保留 |
| settings.silentStartup | 静默启动 | 백그라운드 시작 | Silent Startup | 已修订 |
| settings.silentStartupDescription | 程序启动时不显示主窗口，仅在系统托盘运行 | 앱 시작 시 메인 창을 표시하지 않고 시스템 트레이에서만 실행합니다. | Start in background mode without showing main window | 已修订 |
| settings.autoLaunchFailed | 设置开机自启失败 | 자동 실행을 설정하지 못했습니다. | Failed to set auto-launch | 保留 |
| settings.minimizeToTray | 关闭时最小化到托盘 | 닫을 때 트레이로 최소화 | Minimize to tray on close | 保留 |
| settings.minimizeToTrayDescription | 勾选后点击关闭按钮会隐藏到系统托盘，取消则直接退出应用。 | 켜면 닫기 버튼을 눌러도 앱이 종료되지 않고 시스템 트레이로 숨겨집니다. 끄면 앱이 바로 종료됩니다. | When checked, clicking the close button will hide to system tray, otherwise the app will exit directly. | 已修订 |
| settings.useAppWindowControls | 启用应用级窗口按钮 | 앱 수준 창 컨트롤 활성화 | Enable app-level window controls | 保留 |
| settings.useAppWindowControlsDescription | 开启后使用应用自建的最小化、最大化/还原、关闭按钮；关闭后沿用系统窗口模式。 | 앱 상단에 내장된 최소화, 최대화/복원 및 닫기 버튼을 사용합니다. 끄면 시스템 창 모드를 사용합니다. | Use built-in minimize, maximize/restore, and close buttons in the app header. | 已修订 |
| settings.enableClaudePluginIntegration | 应用到 Claude Code 插件 | Claude Code 확장에 적용 | Apply to Claude Code extension | 保留 |
| settings.enableClaudePluginIntegrationDescription | 开启后 VS Code Claude Code 插件的供应商将随本软件切换 | 켜면 VS Code의 Claude Code 확장도 이 앱에서 선택한 공급자로 함께 전환됩니다 | When enabled, the VS Code Claude Code extension provider will switch with this app | 已修订 |
| settings.skipClaudeOnboarding | 跳过 Claude Code 初次安装确认 | Claude Code 첫 실행 확인 건너뛰기 | Skip Claude Code first-run confirmation | 保留 |
| settings.skipClaudeOnboardingDescription | Claude Code 第一次启动时会先走一遍引导流程，要求选主题并登录 Anthropic 账号。如果你用的是第三方供应商，不需要登录官方账号，开启后就能跳过这一步直接使用。原理是在 ~/.claude.json 里写入 hasCompletedOnboarding: true；关闭时删除该字段，下次启动会重新出现引导。 | 처음 실행 시 Claude Code는 테마를 선택하고 Anthropic 계정에 로그인하라는 온보딩 흐름을 실행합니다. 타사 공급자를 사용하는 경우 해당 로그인이 필요하지 않으므로 이 기능을 켜면 바로 건너뜁니다. hasCompletedOnboarding: true를 ~/.claude.json에 작성하여 작동합니다. 끄면 해당 필드가 제거되고 다음 실행 시 온보딩이 다시 나타납니다. | On first launch, Claude Code runs an onboarding flow that asks you to pick a theme and sign in to an Anthropic account. If you use a third-party provider you don't need that sign-in, so turning this on skips straight past it. It works by writing hasCompletedOnboarding: true to ~/.claude.json; turning it off removes that field, and the onboarding appears again on the next launch. | 已修订 |
| settings.codexAuth | Codex 应用增强 | Codex 앱 개선 | Codex App Enhancements | 保留 |
| settings.preserveCodexOfficialAuthOnSwitch | 非接管切换时保留官方登录 | 직접 연결 전환 시 공식 로그인 유지 | Keep official login for direct switches | 已修订 |
| settings.preserveCodexOfficialAuthOnSwitchDescription | 控制未开启路由接管时切换第三方供应商是否保留 Codex 官方登录；路由接管期间始终保留 | 라우팅이 앱 설정을 관리하지 않는 상태에서 타사 공급자로 전환할 때 Codex 공식 로그인을 유지할지 정합니다. 라우팅이 앱 설정을 관리하는 동안에는 항상 공식 로그인을 유지합니다. | Controls third-party switches when local routing is off. Takeover routing always preserves the Codex official login. | 已修订 |
| settings.unifyCodexSessionHistory | 统一 Codex 会话历史 | 통합 Codex 세션 기록 | Unified Codex session history | 保留 |
| settings.unifyCodexSessionHistoryDescription | 只影响 Codex CLI：CLI 的 resume 列表只显示当前供应商的会话，开启后官方订阅改以共享的 custom 供应商标识运行，官方与第三方会话出现在同一列表中。Codex 桌面版更新后已经可以显示全部会话，只用桌面版无需开启。可选择把现有官方会话一并迁入（迁移前自动备份），关闭时可按备份恢复。注意：跨供应商继续旧会话时，对方后端可能无法解密会话中的 encrypted_content 推理内容，导致继续失败 | Codex CLI에만 영향을 줍니다. CLI의 재개 목록에는 현재 공급자의 세션만 표시됩니다. 켜면 공식 구독도 공유된 ‘custom’ 공급자 ID를 사용하므로 공식 세션과 타사 세션이 한 목록에 표시됩니다. Codex 데스크톱 앱은 업데이트 후 모든 세션을 표시하므로 데스크톱만 사용한다면 켤 필요가 없습니다. 기존 공식 세션도 함께 옮길 수 있으며, 옮기기 전에 자동 백업하고 기능을 끌 때 복원할 수 있습니다. 주의: encrypted_content 추론 내용은 생성한 백엔드만 해독할 수 있으므로 다른 공급자에서 이전 세션을 이어가면 실패할 수 있습니다. | Affects the Codex CLI only: its resume list shows only the current provider's sessions. When enabled, the official subscription runs under the shared "custom" provider id so official and third-party sessions appear in one list. The Codex desktop app can show all sessions since a recent update, so desktop-only users don't need this. You can optionally migrate existing official sessions in (backed up first) and restore them from backup when turning it off. Note: resuming an old session across providers may fail because its encrypted_content reasoning can only be decrypted by the backend that created it. | 已修订 |
| settings.codexStackClassicSubagents | 聚合模式下子 agent 用经典工具 | 통합 모드에서 기존 서브에이전트 도구 사용 | Classic sub-agent tools in aggregation | 已修订 |
| settings.codexStackClassicSubagentsDescription | 主、子 agent 不在同一家供应商时必须打开，否则子 agent 收不到任务。 | 주 에이전트와 서브에이전트가 서로 다른 공급자를 사용한다면 반드시 켜야 합니다. 그렇지 않으면 서브에이전트가 작업을 받지 못합니다. | Must be on when the main agent and a sub-agent use different providers, or the sub-agent cannot receive its task. | 已修订 |
| settings.codexStackClassicSubagentsForcedV2 | Codex 的 config.toml 里打开了 [features] multi_agent_v2，它比这个开关优先，开关不会生效 | Codex의 config.toml에서 [features] multi_agent_v2가 켜져 있습니다. 이 설정보다 우선하므로 해당 스위치는 적용되지 않습니다. | Codex config.toml turns on [features] multi_agent_v2, which takes precedence over this setting, so it has no effect. | 已修订 |
| settings.codexSessionCompression | 压缩 Codex 历史会话 | 이전 Codex 세션 압축 | Compress old Codex sessions | 保留 |
| settings.codexSessionCompressionDescription | 打开后，Codex 每次启动时会在后台把 7 天以上没动过的会话文件压缩保存，明显减少占用的磁盘空间；在这些会话上继续对话时 Codex 会自动解压。CC Switch 照常显示和统计压缩过的会话，只是列表里不显示它们最后一条回复的预览。这是 Codex 还在开发中的功能，打开后 Codex 每次启动会显示一条提示；需要较新版本的 Codex，重启 Codex 后生效。关闭后不再压缩，已压缩的会话保持原样 | 켜져 있으면 Codex는 시작할 때마다 백그라운드에서 7일 동안 변경되지 않은 세션 파일을 압축하여 디스크 공간을 많이 절약합니다. Codex는 세션을 계속할 때 자동으로 세션의 압축을 해제합니다. CC Switch는 여전히 압축된 세션을 나열하고 계산합니다. 목록에는 마지막 답변의 미리보기가 표시되지 않습니다. 이것은 아직 개발 중인 Codex 기능입니다. Codex는 켜져 있는 동안 시작할 때마다 알림을 표시합니다. 최신 Codex 버전이 필요하며 Codex를 다시 시작한 후에 적용됩니다. 끄면 압축이 중지됩니다. 이미 압축된 세션은 그대로 유지됩니다. | When on, Codex compresses session files that haven't changed for 7 days in the background each time it starts, which saves a lot of disk space. Codex decompresses a session automatically when you continue it. CC Switch still lists and counts compressed sessions; the list just doesn't show a preview of their last reply. This is a Codex feature still under development: Codex shows a notice on every start while it's on. Requires a recent Codex version and takes effect after restarting Codex. Turning it off stops compressing; sessions already compressed stay as they are. | 保留 |
| settings.codexSessionCompressionUsage | 会话目录当前占用 {{size}} | 세션은 현재 {{size}}을(를) 사용합니다. | Sessions currently use {{size}} | 已修订 |
| settings.codexSessionCompressionFailed | 修改 Codex 会话压缩设置失败 | Codex 세션 압축 설정을 변경하지 못했습니다. | Failed to change the Codex session compression setting | 保留 |
| settings.unifyCodexHistoryRestoreCompleted | 已按备份还原官方会话历史（{{files}} 个会话文件、{{rows}} 条索引记录） | 백업에서 복원된 공식 세션 기록({{files}} 세션 파일, {{rows}} 인덱스 행) | Official session history restored from backup ({{files}} session files, {{rows}} index rows) | 保留 |
| settings.unifyCodexHistoryRestoreFailed | 还原官方会话历史失败，请重试 | 공식 세션 기록을 복원하지 못했습니다. 다시 시도해 주세요. | Failed to restore official session history, please try again | 保留 |
| settings.unifyCodexHistoryRestoreNothing | 当前 Codex 目录没有可恢复的迁移备份 | 현재 Codex 디렉터리에 대한 복원 가능한 마이그레이션 백업이 없습니다. | No restorable migration backup for the current Codex directory | 保留 |
| settings.unifyCodexHistoryRestoreSkippedToggleOn | 统一会话历史开关已重新开启，已跳过还原 | 통합 세션 기록이 다시 활성화되었습니다. 복원을 건너뛰었습니다. | Unified session history was re-enabled; restore skipped | 保留 |
| settings.appVisibility.title | 主页面显示 | 메인 페이지 표시 | Homepage Display | 已修订 |
| settings.appVisibility.description | 选择在主页面显示的应用 | 메인 페이지에 표시할 앱을 선택하세요 | Choose which apps to show on the homepage | 已修订 |
| settings.appVisibility.claudeDesc | Anthropic Claude Code CLI | Anthropic Claude Code CLI | Anthropic Claude Code CLI | 保留 |
| settings.appVisibility.codexDesc | OpenAI Codex CLI | OpenAI Codex CLI | OpenAI Codex CLI | 保留 |
| settings.appVisibility.geminiDesc | Google Gemini CLI | Google Gemini CLI | Google Gemini CLI | 已修订 |
| settings.appVisibility.opencodeDesc | OpenCode CLI | OpenCode CLI | OpenCode CLI | 保留 |
| settings.appVisibility.showProfileSwitcher | 显示项目切换 | 프로젝트 전환기 표시 | Show project switcher | 保留 |
| settings.appVisibility.showProfileSwitcherDescription | 在主页面顶部显示项目切换入口 | 기본 페이지 헤더에 프로젝트 전환기 표시 | Show the project switcher in the main page header | 保留 |
| settings.appVisibility.showProviderSearch | 显示供应商搜索 | 공급자 검색 표시 | Show provider search | 已修订 |
| settings.appVisibility.showProviderSearchDescription | 在供应商页顶部显示搜索按钮，可按名称、备注、官网和请求地址查找。关掉后仍可用 ⌘F / Ctrl+F 打开搜索 | 이름, 메모, 웹 사이트 또는 API 주소로 공급자를 찾으려면 공급자 페이지 상단에 검색 버튼을 표시하십시오. 숨겨진 경우에도 ⌘F / Ctrl+F를 누르면 검색이 열립니다. | Show a search button at the top of the provider page to find providers by name, notes, website, or API address. When hidden, ⌘F / Ctrl+F still opens search | 已修订 |
| settings.terminal.title | 首选终端 | 선호하는 터미널 | Preferred Terminal | 保留 |
| settings.terminal.description | 选择点击终端按钮时使用的终端应用 | 터미널 버튼을 클릭할 때 사용할 터미널 앱을 선택하세요 | Choose which terminal app to use when clicking the terminal button | 保留 |
| settings.terminal.fallbackHint | 如果选择的终端不可用，将自动使用系统默认终端 | 선택한 터미널을 사용할 수 없는 경우 시스템 기본값이 사용됩니다. | If the selected terminal is unavailable, the system default will be used | 保留 |
| settings.terminal.options.macos.terminal | Terminal.app | Terminal.app | Terminal.app | 保留 |
| settings.terminal.options.macos.iterm2 | iTerm2 | iTerm2 | iTerm2 | 保留 |
| settings.terminal.options.macos.alacritty | Alacritty | Alacritty | Alacritty | 已修订 |
| settings.terminal.options.macos.kitty | Kitty | Kitty | Kitty | 已修订 |
| settings.terminal.options.macos.ghostty | Ghostty | Ghostty | Ghostty | 已修订 |
| settings.terminal.options.macos.otty | Otty | Otty | Otty | 已修订 |
| settings.terminal.options.macos.wezterm | WezTerm | WezTerm | WezTerm | 保留 |
| settings.terminal.options.macos.kaku | Kaku | Kaku | Kaku | 已修订 |
| settings.terminal.options.macos.warp | Warp | Warp | Warp | 已修订 |
| settings.terminal.options.windows.cmd | 命令提示符 | 명령 프롬프트 | Command Prompt | 保留 |
| settings.terminal.options.windows.powershell | PowerShell | PowerShell | PowerShell | 保留 |
| settings.terminal.options.windows.wt | Windows Terminal | Windows Terminal | Windows Terminal | 已修订 |
| settings.terminal.options.linux.gnomeTerminal | GNOME Terminal | GNOME Terminal | GNOME Terminal | 已修订 |
| settings.terminal.options.linux.konsole | Konsole | Konsole | Konsole | 已修订 |
| settings.terminal.options.linux.xfce4Terminal | Xfce4 Terminal | Xfce4 Terminal | Xfce4 Terminal | 已修订 |
| settings.terminal.options.linux.alacritty | Alacritty | Alacritty | Alacritty | 已修订 |
| settings.terminal.options.linux.kitty | Kitty | Kitty | Kitty | 已修订 |
| settings.terminal.options.linux.ghostty | Ghostty | Ghostty | Ghostty | 已修订 |
| settings.configDirectoryOverride | 配置目录覆盖（高级） | 설정 디렉터리 재정의(고급) | Configuration Directory Override (Advanced) | 已修订 |
| settings.configDirectoryDescription | 在 WSL 等环境使用 Claude Code 或 Codex 的时候，可手动指定为 WSL 里的配置目录，供应商数据与主环境保持一致。 | WSL과 같은 환경에서 Claude Code 또는 Codex를 사용하는 경우 설정 디렉터리를 WSL의 설정 디렉터리로 수동으로 지정하여 공급자 데이터를 기본 환경과 일관되게 유지할 수 있습니다. | When using Claude Code or Codex in environments like WSL, you can manually specify the configuration directory to the one in WSL to keep provider data consistent with the main environment. | 已修订 |
| settings.appConfigDir | CC Switch 配置目录 | CC Switch 설정 디렉토리 | CC Switch Configuration Directory | 已修订 |
| settings.appConfigDirDescription | 自定义 CC Switch 的配置存储位置（指定到云同步文件夹即可云同步配置） | CC Switch 설정을 위한 저장 위치 사용자 정의(설정 동기화를 활성화하려면 클라우드 동기화 폴더를 가리킴) | Customize the storage location for CC Switch configuration (point to cloud sync folder to enable config sync) | 已修订 |
| settings.browsePlaceholderApp | 例如：C:\Users\Administrator\.cc-switch | 예: C:\\Users\\Administrator\\.cc-switch | e.g., C:\Users\Administrator\.cc-switch | 保留 |
| settings.claudeConfigDir | Claude Code 配置目录 | Claude Code 설정 디렉토리 | Claude Code Configuration Directory | 已修订 |
| settings.claudeConfigDirDescription | 覆盖 Claude 配置目录 (settings.json)。真正自定义目录会在目录内存放 Claude MCP 的 .claude.json；默认 ~/.claude 目录仍使用 Claude 默认的 ~/.claude.json。 | Claude 설정 디렉터리(settings.json)를 변경합니다. 사용자 지정 디렉터리에서는 그 안에 .claude.json(MCP)을 저장합니다. 기본 ~/.claude 디렉터리에서는 Claude Code의 기본 동작대로 별도 경로인 ~/.claude.json을 사용합니다. | Override Claude configuration directory (settings.json). Custom directories store .claude.json (MCP) inside the directory; the default ~/.claude directory keeps Claude Code's split ~/.claude.json path. | 已修订 |
| settings.codexConfigDir | Codex 配置目录 | Codex 설정 디렉토리 | Codex Configuration Directory | 已修订 |
| settings.codexConfigDirDescription | 覆盖 Codex 配置目录。 | Codex 설정 디렉터리를 재정의합니다. | Override Codex configuration directory. | 已修订 |
| settings.geminiConfigDir | Gemini 配置目录 | Gemini 설정 디렉토리 | Gemini Configuration Directory | 已修订 |
| settings.geminiConfigDirDescription | 覆盖 Gemini 配置目录 (.env)。 | Gemini 설정 디렉터리(.env)를 재정의합니다. | Override Gemini configuration directory (.env). | 已修订 |
| settings.grokConfigDir | Grok Build 配置目录 | Grok Build 설정 디렉토리 | Grok Build Configuration Directory | 已修订 |
| settings.grokConfigDirDescription | 覆盖 Grok Build 配置目录 (config.toml)。 | Grok Build 설정 디렉터리(config.toml)를 재정의합니다. | Override Grok Build configuration directory (config.toml). | 已修订 |
| settings.opencodeConfigDir | OpenCode 配置目录 | OpenCode 설정 디렉토리 | OpenCode Configuration Directory | 已修订 |
| settings.opencodeConfigDirDescription | 覆盖 OpenCode 配置目录 (opencode.json / opencode.jsonc)。 | OpenCode 설정 디렉터리(opencode.json / opencode.jsonc)를 재정의합니다. | Override OpenCode configuration directory (opencode.json / opencode.jsonc). | 已修订 |
| settings.openclawConfigDir | OpenClaw 配置目录 | OpenClaw 설정 디렉토리 | OpenClaw Configuration Directory | 已修订 |
| settings.openclawConfigDirDescription | 覆盖 OpenClaw 配置目录 (openclaw.json)。 | OpenClaw 설정 디렉터리(openclaw.json)를 재정의합니다. | Override OpenClaw configuration directory (openclaw.json). | 已修订 |
| settings.hermesConfigDir | Hermes 配置目录 | Hermes 설정 디렉토리 | Hermes Configuration Directory | 已修订 |
| settings.hermesConfigDirDescription | 覆盖 Hermes 配置目录 (config.yaml)。 | Hermes 설정 디렉터리(config.yaml)를 재정의합니다. | Override Hermes configuration directory (config.yaml). | 已修订 |
| settings.piConfigDir | Pi 配置目录 | Pi 설정 디렉토리 | Pi Configuration Directory | 已修订 |
| settings.piConfigDirDescription | 覆盖 Pi 配置目录（models.json、指令文件、提示词、Skills 与会话）。 | Pi 설정 디렉터리(models.json, 지침 파일, 프롬프트, Skills 및 세션)를 변경합니다. | Override the Pi configuration directory (models.json, instruction files, prompts, skills, and sessions). | 已修订 |
| settings.browsePlaceholderClaude | 例如：/home/<你的用户名>/.claude | 예: /home/<사용자 이름>/.claude | e.g., /home/<your-username>/.claude | 保留 |
| settings.browsePlaceholderCodex | 例如：/home/<你的用户名>/.codex | 예: /home/<사용자 이름>/.codex | e.g., /home/<your-username>/.codex | 保留 |
| settings.browsePlaceholderGemini | 例如：/home/<你的用户名>/.gemini | 예: /home/<사용자 이름>/.gemini | e.g., /home/<your-username>/.gemini | 保留 |
| settings.browsePlaceholderGrok | 例如：/home/<你的用户名>/.grok | 예: /home/<사용자 이름>/.grok | e.g., /home/<your-username>/.grok | 保留 |
| settings.browsePlaceholderOpencode | 例如：/home/<你的用户名>/.config/opencode | 예: /home/<사용자 이름>/.config/opencode | e.g., /home/<your-username>/.config/opencode | 保留 |
| settings.browsePlaceholderOpenclaw | 例如：/home/<你的用户名>/.openclaw | 예: /home/<사용자 이름>/.openclaw | e.g., /home/<your-username>/.openclaw | 保留 |
| settings.browsePlaceholderHermes | 例如：/home/<你的用户名>/.hermes | 예: /home/<사용자 이름>/.hermes | e.g., /home/<your-username>/.hermes | 保留 |
| settings.browsePlaceholderPi | 例如：/home/<你的用户名>/.pi/agent | 예: /home/<사용자 이름>/.pi/agent | e.g., /home/<your-username>/.pi/agent | 保留 |
| settings.browseDirectory | 浏览目录 | 디렉토리 찾아보기 | Browse Directory | 保留 |
| settings.resetDefault | 恢复默认目录（需保存后生效） | 기본 디렉터리로 재설정(저장 후 적용) | Reset to default directory (takes effect after saving) | 保留 |
| settings.checkForUpdates | 检查更新 | 업데이트 확인 | Check for Updates | 保留 |
| settings.updateTo | 更新到 v{{version}} | v{{version}}로 업데이트 | Update to v{{version}} | 保留 |
| settings.updating | 更新中... | 업데이트 중... | Updating... | 保留 |
| settings.checking | 检查中... | 확인 중... | Checking... | 保留 |
| settings.upToDate | 已是最新 | 최신 | Up to Date | 保留 |
| settings.aboutHint | 查看版本信息与更新状态。 | 버전 정보 및 업데이트 상태를 확인하세요. | View version information and update status. | 保留 |
| settings.portableMode | 当前为便携版，更新需手动下载。 | 휴대용 모드: 업데이트를 수동으로 다운로드해야 합니다. | Portable mode: updates require manual download. | 保留 |
| settings.portableUpdateHint | 便携版：点击上方按钮会下载新版压缩包，解压后覆盖原来的 cc-switch.exe 即可。配置和数据保存在用户目录下的 .cc-switch，不会因覆盖而丢失。 | 휴대용 모드: 위의 버튼을 누르면 새 zip이 다운로드됩니다. 압축을 풀고 기존 cc-switch.exe를 교체하세요. 귀하의 설정과 데이터는 사용자 폴더 아래의 .cc-switch에 있으며 영향을 받지 않습니다. | Portable mode: the button above downloads the new zip. Extract it and replace your existing cc-switch.exe. Your settings and data live in .cc-switch under your user folder and are not affected. | 保留 |
| settings.updateAvailable | 检测到新版本：{{version}} | 새 버전 사용 가능: {{version}} | New version available: {{version}} | 保留 |
| settings.updateBadge | 有更新可用 | 업데이트 가능 | Update available | 保留 |
| settings.updateFailed | 更新安装失败，已尝试打开下载页面。 | 업데이트 설치에 실패했습니다. 다운로드 페이지를 열려고 했습니다. | Update installation failed, attempted to open download page. | 保留 |
| settings.checkUpdateFailed | 检查更新失败，请稍后重试。 | 업데이트를 확인하지 못했습니다. 나중에 다시 시도해 주세요. | Failed to check for updates, please try again later. | 保留 |
| settings.openReleaseNotesFailed | 打开更新日志失败 | 릴리스 노트를 열지 못했습니다 | Failed to open release notes | 已修订 |
| settings.releaseNotes | 更新日志 | 릴리스 노트 | Release Notes | 保留 |
| settings.viewReleaseNotes | 查看该版本更新日志 | 이 버전의 릴리스 노트 보기 | View release notes for this version | 已修订 |
| settings.viewCurrentReleaseNotes | 查看当前版本更新日志 | 현재 버전 릴리스 노트 보기 | View current version release notes | 保留 |
| settings.officialWebsite | 官方网站 | 공식 홈페이지 | Official Website | 保留 |
| settings.github | GitHub | GitHub | GitHub | 保留 |
| settings.starPrompt | 如果 CC Switch 帮到了你，请在 GitHub 点个 Star，这对我们意义重大 | CC Switch가 도움이 되었다면 GitHub에 별표를 표시해 주세요. 이는 우리에게 큰 의미가 있습니다. | If CC Switch has helped you, please star us on GitHub — it means a lot to us | 保留 |
| settings.starOnGithub | 去点 Star | GitHub에 별표 표시 | Star on GitHub | 保留 |
| settings.manualInstallCommands | 手动安装命令 | 수동 설치 명령 | Manual Install Commands | 保留 |
| settings.manualUninstallCommands | 手动卸载命令 | 수동 제거 명령 | Manual uninstall commands | 保留 |
| settings.manualUninstallHint | 默认自动侦测各应用的运行环境，也可手动切换。请选择安装时使用的方式，再复制所需应用的命令到终端执行。完成后点击“检查更新”刷新安装状态。 | 각 앱의 환경은 기본적으로 자동으로 감지되며, 다른 환경을 수동으로 선택할 수 있습니다. 원래 설치 방법을 선택한 다음, 제거하려는 앱에 대한 명령을 복사하여 터미널에서 실행하세요. 상태를 새로 고치려면 나중에 “업데이트 확인”을 클릭하세요. | Each app’s environment is detected automatically by default, and you can select a different environment manually. Select the original installation method, then copy the command for the app you want to remove and run it in a terminal. Click “Check for updates” afterwards to refresh its status. | 保留 |
| settings.manualUninstallMethod | 安装方式 | 설치 방법 | Installation method | 已修订 |
| settings.manualUninstallBunLauncherHint | Bun 可能留下 OpenClaw 启动器。请先核对文件中的“OpenClaw Bun launcher”标记及包路径，再删除该文件，保留共享 bin 目录。 | Bun은 OpenClaw 런처를 남겨둘 수 있습니다. 해당 파일을 제거하기 전에 "OpenClaw Bun launcher" 헤더와 패키지 경로를 검사하십시오. 공유 bin 디렉토리를 유지하십시오. | Bun can leave an OpenClaw launcher behind. Inspect its “OpenClaw Bun launcher” header and package path before removing that file; keep the shared bin directory. | 保留 |
| settings.manualUninstallOpenClawHint | 请先成功执行 openclaw uninstall --service --yes --non-interactive，仅卸载 Gateway 服务并保留配置和工作区，再执行下方命令移除 CLI。 | 먼저 openclaw uninstall --service --yes --non-interactive를 성공적으로 실행하여 설정 및 작업 공간을 유지하면서 게이트웨이 서비스를 제거하십시오. 그런 다음 아래 명령을 사용하여 CLI를 제거합니다. | First run openclaw uninstall --service --yes --non-interactive successfully to remove the Gateway service while keeping configuration and workspaces. Then remove the CLI with the command below. | 已修订 |
| settings.manualUninstallEnvironment | 运行环境 | 환경 | Environment | 保留 |
| settings.manualUninstallEnvironmentHint | 请使用安装时的 Node 环境和包管理器，仅在确认全局 npm 安装前缀后添加 --prefix。WSL 应用请在对应发行版内执行。 | 설치할 때와 동일한 Node 환경과 패키지 관리자를 사용하세요. npm 전역 설치 경로를 확인한 경우에만 --prefix를 추가하세요. WSL 앱의 명령은 해당 배포판 안에서 실행하세요. | Use the same Node environment and package manager as the original installation. Only add --prefix for a verified global npm prefix. Run commands for WSL apps inside the corresponding distribution. | 已修订 |
| settings.manualUninstallOtherMethods | 仅列出已按官方安装说明核实的方式。以上命令保留配置和会话数据。脚本管理的安装、手动下载或其他方式请按原安装器说明卸载，不要套用全局 npm 命令。通过脚本安装的 Pi，请重新运行其安装器并选择“Uninstall Pi”。 | 공식 설치 안내로 확인된 방법만 표시합니다. 명령을 실행해도 설정과 세션 데이터는 유지됩니다. 스크립트로 설치했거나 직접 다운로드한 경우 등에는 원래 설치 프로그램의 제거 안내를 따르세요. npm 전역 명령을 대신 사용하지 마세요. 스크립트로 설치한 Pi는 설치 프로그램을 다시 실행하여 ‘Uninstall Pi’를 선택하세요. | Only methods verified against official installation instructions are listed. Commands retain configuration and session data. For script-managed installations, downloads or other methods, use the original installer’s instructions; do not substitute a global npm command. For Pi installed by script, rerun its installer and select “Uninstall Pi”. | 已修订 |
| settings.copyToolUninstallCommand | 复制 {{tool}} 的卸载命令 | {{tool}}에 대한 제거 명령을 복사합니다. | Copy the uninstall command for {{tool}} | 保留 |
| settings.uninstallCommandCopied | 卸载命令已复制 | 제거 명령이 복사되었습니다. | Uninstall command copied | 保留 |
| settings.uninstallCommandCopyFailed | 复制失败，请手动选择并复制命令。 | 복사에 실패했습니다. 명령을 수동으로 선택하고 복사하십시오. | Copy failed. Please select and copy the command manually. | 保留 |
| settings.oneClickInstallHint | 安装或升级 Claude Code / Codex / Gemini CLI / Grok Build / OpenCode / OpenClaw / Hermes / Pi / MiniMax Code | Claude Code / Codex / Gemini CLI / Grok Build / OpenCode / OpenClaw / Hermes / Pi / MiniMax Code 설치 또는 업그레이드 | Install or upgrade Claude Code / Codex / Gemini CLI / Grok Build / OpenCode / OpenClaw / Hermes / Pi / MiniMax Code | 保留 |
| settings.localEnvCheck | 本地环境检查 | 로컬 환경 확인 | Local environment check | 保留 |
| settings.updateAllTools | 全部升级（{{count}}） | 모두 업데이트({{count}}) | Update All ({{count}}) | 保留 |
| settings.currentVersion | 当前版本 | 현재 버전 | Current Version | 保留 |
| settings.latestVersion | 最新版本 | 최신 버전 | Latest Version | 保留 |
| settings.updateAvailableShort | 可升级 | 업데이트 | Update | 保留 |
| settings.toolInstall | 安装 | 설치 | Install | 保留 |
| settings.toolUninstall | 卸载 | 제거 | Uninstall | 保留 |
| settings.toolUninstallConfirmTitle | 卸载 {{tool}}？ | {{tool}}을(를) 제거하시겠습니까? | Uninstall {{tool}}? | 已修订 |
| settings.toolUninstallConfirmHint | 选择要卸载的那处安装。配置和会话数据会保留，其他安装不受影响。 | 제거할 설치를 선택합니다. 설정 및 세션 데이터는 유지되며 다른 설치에는 영향을 미치지 않습니다. | Choose the installation to remove. Configuration and session data are kept, and other installations are not affected. | 已修订 |
| settings.toolUninstallPreparing | 正在检查安装… | 설치 확인 중… | Checking the installation… | 保留 |
| settings.toolUninstallManualRequired | 无法自动卸载，请手动卸载此应用。 | 자동으로 제거할 수 없습니다. 이 앱을 수동으로 제거해 주세요. | Cannot uninstall automatically. Please uninstall this app manually. | 保留 |
| settings.toolUninstallChooseInstall | 要卸载的安装 | 제거할 설치 항목 | Installation to remove | 已修订 |
| settings.toolUninstallNativeHint | 只删除上面命令列出的文件，不删除目录，配置和会话数据会保留。 | 위 명령에 나열된 파일만 제거되고 디렉터리는 제거되지 않습니다. 설정 및 세션 데이터는 유지됩니다. | Only the files listed in the command above are removed, never directories. Configuration and session data are kept. | 已修订 |
| settings.toolUninstallReinstalledByUpdater | 这份是 {{tool}} 自动更新时一并安装的，单独卸载后，下次更新还会装回来。 | {{tool}}의 업데이터는 이 복사본을 다른 복사본과 함께 설치했습니다. 이 복사본만 제거하면 다음 업데이트에서 다시 설치됩니다. | {{tool}}'s updater installed this copy alongside the other one. If you remove only this copy, the next update will install it again. | 保留 |
| settings.toolUninstallFailed | 卸载失败 | 제거 실패 | Uninstall failed | 保留 |
| settings.toolUninstallWarningTitle | 卸载命令已完成，请检查结果 | 제거 명령이 완료되었습니다. 결과를 확인하세요 | Uninstall command completed; check the result | 保留 |
| settings.toolUninstallHermesWindowsHint | Windows 上 Hermes 卸载时可能因正在运行的 Python 被锁定而留下部分程序文件。命令结束后请检查原安装目录中的残留；清理时请保留配置和会话数据。 | Windows에서 Hermes는 제거 중에 실행 중인 Python이 잠겨 있기 때문에 일부 프로그램 파일을 남겨둘 수 있습니다. 명령이 완료된 후 원래 설치 디렉터리에 남은 파일이 있는지 확인하세요. 정리할 때 설정 및 세션 데이터를 유지하십시오. | On Windows, Hermes may leave some program files behind because its running Python is locked during uninstall. After the command finishes, check the original installation directory for leftover files; keep configuration and session data when cleaning up. | 已修订 |
| settings.toolUninstallRemaining | 所选安装已卸载，仍检测到其他安装 | 선택한 설치가 제거되었습니다. 다른 설치는 남아 있습니다 | The selected installation was removed; other installations remain | 保留 |
| settings.toolUninstallCheckFailed | 卸载后无法确认安装状态，请点击“检查更新”重试。 | 제거 후 설치 상태를 확인할 수 없습니다. 다시 시도하려면 '업데이트 확인'을 클릭하세요. | Could not verify the installation status after uninstalling. Click “Check for updates” to try again. | 保留 |
| settings.toolUpdate | 升级 | 업데이트 | Update | 保留 |
| settings.toolReady | 已就绪 | 준비됨 | Ready | 已修订 |
| settings.toolActionDone | {{count}} 个工具{{action}}完成 | 도구 {{count}}개 {{action}} 완료 | {{action}} completed for {{count}} tool(s) | 已修订 |
| settings.toolActionPartial | {{succeeded}} 个{{action}}成功，{{failed}} 个失败 | {{action}}: {{succeeded}}개 성공, {{failed}}개 실패 | {{action}} succeeded for {{succeeded}}, failed for {{failed}} | 已修订 |
| settings.toolActionFailed | 安装/升级命令执行失败 | 설치/업데이트 명령이 실패했습니다. | Install/update command failed | 保留 |
| settings.toolActionInProgress | 应用操作仍在进行中 | 앱 작업이 아직 실행 중입니다. | An app operation is still running | 保留 |
| settings.toolActionInProgressDetail | {{tool}} 已有安装、升级或卸载任务正在后台处理，请等待完成，无需重复操作。 | {{tool}}에는 이미 백그라운드에서 설치, 업데이트 또는 제거가 실행 중입니다. 완료될 때까지 기다려 주십시오. | {{tool}} already has an installation, update or uninstall running in the background. Please wait for it to finish. | 保留 |
| settings.toolNotRunnable | 已安装但无法运行（未探测到版本） | 설치되었지만 실행할 수 없음(버전이 감지되지 않음) | Installed but not runnable (no version detected) | 保留 |
| settings.toolActionVersionUnchangedTitle | 版本没有变化 | 버전이 변경되지 않았습니다. | Version did not change | 保留 |
| settings.toolActionVersionUnchanged | 仍是 {{version}}（最新：{{latest}}）。上游升级器可能报告成功但没有实际更新。 | 아직 {{version}}(최신: {{latest}})을(를) 사용하고 있습니다. 업데이트 프로그램이 업데이트를 적용하지 않고 성공했다고 보고했을 수 있습니다. | Still on {{version}} (latest: {{latest}}). The updater may have reported success without applying the update. | 已修订 |
| settings.toolActionInstalledNotRunnable | 已安装，但当前环境无法运行，请检查 | 설치되었지만 현재 환경에서 실행할 수 없습니다. 확인하세요. | Installed, but it can't run in the current environment — please check | 保留 |
| settings.installedNotRunnable | 已安装·无法运行 | 설치됨 · 실행할 수 없음 | Installed · can't run | 保留 |
| settings.toolCheckEnv | 请检查运行环境 | 환경 확인 | Check environment | 保留 |
| settings.toolDiagnose | 诊断安装冲突 | 설치 충돌 진단 | Diagnose installs | 已修订 |
| settings.toolDiagnosing | 诊断中… | 진단 중… | Diagnosing… | 保留 |
| settings.toolConflictTitle | 检测到多处安装 | 여러 설치가 감지됨 | Multiple installations detected | 保留 |
| settings.toolConflictHint | 命令行实际使用标「默认」的那处；升级可能写到了别处。 | 명령줄은 ‘기본값’으로 표시된 설치를 사용합니다. 업그레이드가 다른 설치 위치에 적용되었을 수 있습니다. | The command line uses the one marked Default; an upgrade may have written to another. | 已修订 |
| settings.toolConflictDefault | 默认 | 기본값 | Default | 保留 |
| settings.toolConflictNotRunnable | 无法运行 | 실행할 수 없습니다 | can't run | 保留 |
| settings.toolDiagnoseNoConflict | 未发现安装冲突 | 충돌하는 설치가 발견되지 않았습니다. | No conflicting installations found | 保留 |
| settings.toolDiagnoseConflicts | {{count}} 个工具有多处安装，冲突列表已在对应行展开 | 도구 {{count}}개에서 여러 설치가 발견되었습니다. 해당 행에 설치 목록을 펼쳤습니다 | {{count}} tool(s) have multiple installations; the lists are expanded on their rows | 已修订 |
| settings.toolDiagnoseFailed | 诊断失败 | 진단 실패 | Diagnosis failed | 保留 |
| settings.toolUpgradeConfirmTitle | 确认升级位置 | 업그레이드 대상 확인 | Confirm upgrade target | 保留 |
| settings.toolUpgradeConfirmHint | 检测到多处安装。本次升级不会全部更新，具体作用的位置以下方各项为准。 | 여러 설치가 감지되었습니다. 이 업그레이드는 모든 항목을 업데이트하지는 않습니다. 실제 대상이 무엇인지 알아보려면 아래의 각 도구를 참조하세요. | Multiple installations detected. This upgrade won't update all of them; refer to each tool below for what it actually targets. | 保留 |
| settings.toolUpgradeWillRun | 将执行： | 실행 예정: | Will run: | 保留 |
| settings.toolUpgradeConfirmBtn | 确认升级 | 업그레이드 확인 | Confirm upgrade | 保留 |
| settings.toolUpgradeUnanchoredHint | 无法确定命令行实际使用哪处，将执行默认升级命令（可能装到 PATH 上第一个 npm）。 | 명령줄에서 어떤 설치를 사용하는지 확인할 수 없습니다. 기본 업그레이드 명령을 실행합니다(PATH의 첫 번째 npm에 설치할 수 있음). | Can't determine which install your command line uses; will run the default upgrade command (may install to the first npm on PATH). | 保留 |
| settings.toolUpgradeUnmanagedTitle | 以下工具已跳过升级 | 이 도구 업그레이드를 건너뛰었습니다. | Skipped upgrading these tools | 保留 |
| settings.toolUpgradeUnmanagedDetail | {{tool}}（{{path}}）不是通过 npm 或可识别的安装器安装的，CC Switch 无法判断如何升级它。请用你原来的安装方式升级（例如 winget、Scoop 或重新运行官方安装脚本）。 | {{tool}}({{path}})는 npm이나 인식된 설치 프로그램으로 설치되지 않았으므로 CC Switch는 업그레이드 방법을 알 수 없습니다. 설치한 방식으로 업그레이드하세요(예: Winget, Scoop 또는 공식 설치 스크립트 다시 실행). | {{tool}} ({{path}}) wasn't installed by npm or a recognized installer, so CC Switch can't tell how to upgrade it. Upgrade it the way you installed it (e.g. winget, Scoop, or re-running the official install script). | 保留 |
| settings.envBadge.wsl | WSL | WSL | WSL | 保留 |
| settings.envBadge.windows | Win | Win | Win | 已修订 |
| settings.envBadge.macos | macOS | macOS | macOS | 保留 |
| settings.envBadge.linux | Linux | Linux | Linux | 已修订 |
| settings.wslShell | Shell | Shell | Shell | 已修订 |
| settings.wslShellFlag | 标志 | 플래그 | Flag | 已修订 |
| settings.installCommandsCopied | 安装命令已复制 | 설치 명령이 복사되었습니다. | Install commands copied | 保留 |
| settings.installCommandsCopyFailed | 复制失败，请手动复制。 | 복사하지 못했습니다. 수동으로 복사하세요. | Copy failed, please copy manually. | 保留 |
| settings.importFailedError | 导入配置失败：{{message}} | 설정 가져오기 실패: {{message}} | Import config failed: {{message}} | 已修订 |
| settings.exportFailedError | 导出配置失败: | 설정 내보내기 실패: | Export config failed: | 已修订 |
| settings.restartRequired | 需要重启应用 | 다시 시작 필요 | Restart Required | 保留 |
| settings.restartRequiredMessage | 修改 CC Switch 配置目录后需要重启应用才能生效，是否立即重启？ | CC Switch 설정 디렉터리 변경 사항은 앱을 다시 시작해야 적용됩니다. 지금 다시 시작하시겠습니까? | Modifying the CC Switch configuration directory requires restarting the application to take effect. Restart now? | 已修订 |
| settings.restartNow | 立即重启 | 지금 다시 시작 | Restart Now | 保留 |
| settings.restartLater | 稍后重启 | 나중에 다시 시작 | Restart Later | 保留 |
| settings.restartFailed | 应用重启失败，请手动关闭后重新打开。 | 애플리케이션을 다시 시작하지 못했습니다. 수동으로 닫았다가 다시 열어보세요. | Application restart failed, please manually close and reopen. | 保留 |
| settings.devModeRestartHint | 开发模式下不支持自动重启，请手动重新启动应用。 | 개발자 모드: 자동 다시 시작이 지원되지 않습니다. 애플리케이션을 수동으로 다시 시작하세요. | Dev Mode: Automatic restart not supported, please manually restart the application. | 保留 |
| settings.saving | 正在保存... | 저장 중... | Saving... | 保留 |
| settings.globalProxy.label | 全局代理 | 전역 프록시 | Global Proxy | 已修订 |
| settings.globalProxy.hint | 代理所有请求（API、Skills 下载等）。开启本地路由时，应用的请求也会经过此代理。留空表示直连。 | 모든 요청(API, Skills 다운로드 등)을 프록시합니다. 로컬 라우팅이 활성화되면 앱 트래픽도 이 프록시를 통해 라우팅됩니다. 직접 연결하려면 비워두세요. | Proxy all requests (API, Skills download, etc.). When local routing is enabled, app traffic is also routed through this proxy. Leave empty for direct connection. | 保留 |
| settings.globalProxy.username | 用户名（可选） | 사용자 이름(선택 사항) | Username (optional) | 保留 |
| settings.globalProxy.password | 密码（可选） | 비밀번호(선택사항) | Password (optional) | 保留 |
| settings.globalProxy.test | 测试连接 | 연결 테스트 | Test Connection | 保留 |
| settings.globalProxy.scan | 扫描本地代理 | 로컬 프록시 스캔 | Scan Local Proxies | 保留 |
| settings.globalProxy.clear | 清除 | 지우기 | Clear | 保留 |
| settings.globalProxy.scanFailed | 扫描失败：{{error}} | 스캔 실패: {{error}} | Scan failed: {{error}} | 保留 |
| settings.globalProxy.saved | 代理设置已保存 | 프록시 설정이 저장되었습니다. | Proxy settings saved | 保留 |
| settings.globalProxy.saveFailed | 保存失败：{{error}} | 저장 실패: {{error}} | Save failed: {{error}} | 保留 |
| settings.globalProxy.testSuccess | 连接成功！延迟 {{latency}}ms | 연결되었습니다! 지연 시간 {{latency}}ms | Connected! Latency {{latency}}ms | 保留 |
| settings.globalProxy.testFailed | 连接失败：{{error}} | 연결 실패: {{error}} | Connection failed: {{error}} | 保留 |
| settings.globalProxy.pricingDefaultsTitle | 计费默认配置 | 기본 요금 설정 | Pricing Defaults | 已修订 |
| settings.globalProxy.pricingDefaultsDescription | 设置各应用按请求模型还是返回模型匹配定价，仅对经本地路由的请求生效。 | 각 앱의 요금을 요청 모델과 응답 모델 중 어느 모델에 따라 적용할지 설정합니다. 로컬 라우팅을 통과하는 요청에만 적용됩니다. | Choose whether each app matches pricing by the request model or the response model. Only applies to requests that go through local routing. | 已修订 |
| settings.globalProxy.pricingAppLabel | 应用 | 앱 | App | 保留 |
| settings.globalProxy.pricingModelSourceLabel | 计费模式 | 요금 적용 기준 모델 | Pricing Model Source | 已修订 |
| settings.globalProxy.pricingModelSourceRequest | 请求模型 | 요청 모델 | Request model | 保留 |
| settings.globalProxy.pricingModelSourceResponse | 返回模型 | 응답 모델 | Response model | 保留 |
| settings.globalProxy.pricingSave | 保存计费配置 | 기본 요금 설정 저장 | Save Pricing Defaults | 已修订 |
| settings.globalProxy.pricingSaved | 计费配置已保存 | 기본 요금 설정을 저장했습니다 | Pricing defaults saved | 已修订 |
| settings.globalProxy.pricingSaveFailed | 保存计费配置失败：{{error}} | 기본 요금 설정 저장 실패: {{error}} | Failed to save pricing defaults: {{error}} | 已修订 |
| settings.globalProxy.pricingLoadFailed | 加载计费配置失败：{{error}} | 기본 요금 설정을 불러오지 못했습니다: {{error}} | Failed to load pricing defaults: {{error}} | 已修订 |
| settings.saveFailedGeneric | 保存失败，请重试 | 저장하지 못했습니다. 다시 시도해 주세요. | Save failed, please try again | 保留 |
| settings.sections.general | 通用 | 일반 | General | 保留 |
| settings.sections.appConfig | 应用配置 | 앱 설정 | App config | 已修订 |
| settings.sections.routing | 本地路由 | 로컬 라우팅 | Local routing | 保留 |
| settings.sections.network | 网络 | 네트워크 | Network | 已修订 |
| settings.sections.data | 数据 | 데이터 | Data | 保留 |
| settings.sections.about | 关于 | 정보 | About | 保留 |
| settings.appConfig.configDir | 配置目录 | 설정 디렉토리 | Config directory | 已修订 |
| settings.routing.service | 服务 | 서비스 | Service | 保留 |
| settings.data.location | 存储位置 | 저장 위치 | Location | 已修订 |
| apps.claude | Claude | Claude | Claude | 已修订 |
| apps.claudeCode | Claude Code | Claude Code | Claude Code | 保留 |
| apps.claudeDesktop | Claude Desktop | Claude Desktop | Claude Desktop | 保留 |
| apps.claude-desktop | Claude Desktop | Claude Desktop | Claude Desktop | 保留 |
| apps.codex | Codex | Codex | Codex | 保留 |
| apps.gemini | Gemini | Gemini | Gemini | 已修订 |
| apps.grokbuild | Grok Build | Grok Build | Grok Build | 保留 |
| apps.opencode | OpenCode | OpenCode | OpenCode | 保留 |
| apps.openclaw | OpenClaw | OpenClaw | OpenClaw | 保留 |
| apps.hermes | Hermes | Hermes | Hermes | 保留 |
| apps.pi | Pi | Pi | Pi | 保留 |
| apps.mcode | MiniMax Code | MiniMax Code | MiniMax Code | 保留 |
| apps.agy | Antigravity | Antigravity | Antigravity | 已修订 |
| mcode.empty.title | 还没有添加自定义供应商 | 아직 맞춤 공급자가 없습니다. | No custom providers yet | 已修订 |
| mcode.empty.description | MiniMax 官方账号登录由 MiniMax Code 自行管理，无需导入；config.yaml 里已有的自定义供应商会自动显示在这里。点击右上角 +，从预设或自定义配置添加供应商。 | MiniMax 계정 로그인은 MiniMax Code 자체에서 관리되므로 가져올 것이 없습니다. 이미 config.yaml에 있는 사용자 지정 공급자가 여기에 자동으로 표시됩니다. 프리셋 또는 사용자 정의 공급자를 추가하려면 오른쪽 상단에 있는 + 버튼을 사용하세요. | Your MiniMax account sign-in is managed by MiniMax Code itself, so there is nothing to import. Custom providers already in config.yaml appear here automatically. Use the + button in the top-right corner to add a preset or custom provider. | 已修订 |
| pi.empty.title | 还没有添加 API Key 供应商 | 아직 API 키 공급자가 없습니다. | No API key providers yet | 已修订 |
| pi.empty.description | 点击右上角 +，从预设或自定义配置添加供应商。 | 프리셋 또는 사용자 정의 공급자를 추가하려면 오른쪽 상단에 있는 + 버튼을 사용하세요. | Use the + button in the top-right corner to add a preset or custom provider. | 已修订 |
| pi.provider.enabled | 已在 Pi 中启用 | Pi에서 활성화됨 | Enabled in Pi | 保留 |
| pi.provider.enableFailed | 无法在 Pi 中启用此供应商 | Pi에서 이 공급자를 활성화할 수 없습니다. | Could not enable this provider in Pi | 已修订 |
| pi.provider.removed | 已从 Pi 移除 | Pi에서 제거됨 | Removed from Pi | 保留 |
| pi.provider.writeConflict | Pi 配置正在被其他进程修改，请稍后再试。 | 다른 프로세스가 Pi 설정을 수정 중입니다. 잠시 후 다시 시도하세요. | Another process is updating Pi's configuration. Try again shortly. | 已修订 |
| pi.form.providerKey | 供应商标识 | 공급자 키 | Provider key | 已修订 |
| pi.form.providerKeyRequired | 供应商标识不能为空 | 공급자 키가 필요합니다. | Provider key is required | 已修订 |
| pi.form.selectPresetRequired | 请先选择一个预设或自定义配置 | 프리셋 또는 사용자 정의 설정을 먼저 선택하세요. | Select a preset or custom configuration first | 已修订 |
| pi.form.fixJsonFirst | 请先修复下方配置 JSON，再编辑结构化字段。 | 구조화된 필드를 편집하기 전에 아래 설정 JSON을 수정하세요. | Fix the configuration JSON below before editing the structured fields. | 已修订 |
| pi.form.nameRequired | 显示名称不能为空 | 표시 이름은 필수 항목입니다. | Display name is required | 保留 |
| pi.form.credential | API Key | API 키 | API Key | 保留 |
| pi.form.credentialRequired | 请填写此预设的 API Key | 이 프리셋에 대해 API 키를 입력하세요. | Enter the API key for this preset | 保留 |
| pi.form.absoluteHttpUrlRequired | {{label}} 必须是绝对 HTTP 或 HTTPS 地址 | {{label}}는 절대 HTTP 또는 HTTPS URL이어야 합니다. | {{label}} must be an absolute HTTP or HTTPS URL | 保留 |
| pi.form.positiveNumberRequired | {{label}} 必须是大于 0 的数字 | {{label}}는 0보다 큰 숫자여야 합니다. | {{label}} must be a number greater than 0 | 保留 |
| pi.form.models | 模型配置 | 모델 설정 | Model configuration | 已修订 |
| pi.form.noModels | 暂无模型配置 | 설정된 모델이 없습니다. | No models configured | 已修订 |
| pi.form.addModel | 添加模型 | 모델 추가 | Add model | 保留 |
| pi.form.removeModel | 移除模型 | 모델 제거 | Remove model | 已修订 |
| pi.form.modelId | 模型 ID | 모델 ID | Model ID | 保留 |
| pi.form.modelIdRequired | 第 {{index}} 个模型缺少 ID | 모델 {{index}}에는 ID가 필요합니다 | Model {{index}} needs an ID | 保留 |
| pi.form.modelName | 显示名称 | 표시 이름 | Display name | 保留 |
| pi.form.modelNameRequired | 第 {{index}} 个模型缺少显示名称 | 모델 {{index}}에는 표시 이름이 필요합니다. | Model {{index}} needs a display name | 保留 |
| pi.form.modelNamePlaceholder | 显示名称 | 표시 이름 | Display name | 保留 |
| pi.form.toggleModelDetails | 展开或收起模型详情 | 모델 세부 정보 펼치기/접기 | Toggle model details | 已修订 |
| pi.form.reasoning | 支持扩展思考 | 확장 추론 지원 | Supports extended thinking | 已修订 |
| pi.form.imageInput | 支持图片输入 | 이미지 입력 지원 | Supports image input | 已修订 |
| pi.form.thinkingLevelsLabel | 思考档位 | 추론 수준 | Thinking levels | 已修订 |
| pi.form.customizeThinkingLevels | 自定义 | 사용자 정의 | Customize | 保留 |
| pi.form.thinkingLevelDefault | Pi 默认 | Pi 기본값 | Pi default | 保留 |
| pi.form.thinkingLevelUnsupported | 不可用 | 사용 불가 | Unavailable | 已修订 |
| pi.form.thinkingLevelValue | {{level}}的上游值 | {{level}}의 업스트림 값 | Upstream value for {{level}} | 保留 |
| pi.form.editThinkingLevel | 编辑{{level}}档位 | {{level}} 레벨 편집 | Edit {{level}} level | 保留 |
| pi.form.thinkingLevelFollowDefault | 跟随 Pi 默认 | Pi 기본값을 따릅니다. | Follow Pi default | 保留 |
| pi.form.thinkingLevelMapTo | 映射为 | 다음으로 매핑 | Map to | 保留 |
| pi.form.thinkingLevelMarkUnavailable | 此档位不可用 | 이 수준은 사용할 수 없습니다 | This level is unavailable | 保留 |
| pi.form.thinkingLevelMapInvalid | 思考档位只能使用 Pi 原生档位键，值必须是字符串或 null。 | 추론 수준에는 Pi의 기본 수준 키만 사용할 수 있으며, 값은 문자열 또는 null이어야 합니다. | Thinking levels may only use Pi's native keys, with string or null values. | 已修订 |
| pi.form.thinkingLevels.off | 关闭 | 꺼짐 | Off | 保留 |
| pi.form.thinkingLevels.minimal | Minimal | 최소 | Minimal | 已修订 |
| pi.form.thinkingLevels.low | Low | 낮음 | Low | 已修订 |
| pi.form.thinkingLevels.medium | Medium | 중간 | Medium | 保留 |
| pi.form.thinkingLevels.high | High | 높음 | High | 已修订 |
| pi.form.thinkingLevels.xhigh | XHigh | 매우 높음 | Extra high | 保留 |
| pi.form.thinkingLevels.max | Max | 최대 | Maximum | 已修订 |
| pi.form.contextWindow | 上下文长度 | 컨텍스트 창 | Context window | 保留 |
| pi.form.maxTokens | 最大输出 Token 数 | 최대 출력 토큰 | Max output tokens | 保留 |
| pi.form.compatibility | 接口兼容性 | 호환성 | Compatibility | 保留 |
| pi.form.compatibilityHint | 调整兼容端点或本地服务的请求行为。 | 호환 가능하거나 로컬 엔드포인트에 대한 요청 동작을 조정합니다. | Adjust request behavior for compatible or local endpoints. | 保留 |
| pi.form.addCompatibilityOption | 添加 | 추가 | Add | 已修订 |
| pi.form.noCompatibilityOptions | 暂无兼容性选项 | 설정된 호환성 옵션이 없습니다. | No compatibility options configured | 已修订 |
| pi.form.optionKey | 选项 | 옵션 | Option | 保留 |
| pi.form.optionValue | 值 | 값 | Value | 保留 |
| pi.form.removeCompatibilityOption | 移除兼容性选项 | 호환성 옵션 제거 | Remove compatibility option | 保留 |
| pi.form.effectiveApiRequired | 模型 {{id}} 必须直接配置或继承一个 API | 모델 {{id}}에 API를 직접 설정하거나 공급자에서 상속해야 합니다 | Model {{id}} needs an API, either directly or from the provider | 已修订 |
| pi.form.effectiveBaseUrlRequired | 模型 {{id}} 必须直接配置或继承一个基础地址 | 모델 {{id}}에 기본 URL을 직접 설정하거나 공급자에서 상속해야 합니다 | Model {{id}} needs a base URL, either directly or from the provider | 已修订 |
| pi.form.duplicateModel | 模型 ID {{id}} 重复 | 모델 ID {{id}}가 중복되었습니다. | Model ID {{id}} is duplicated | 保留 |
| pi.form.modelRequired | 请至少添加一个模型 | 모델을 하나 이상 추가하세요. | Add at least one model | 保留 |
| pi.form.providerKeyDuplicate | 该供应商标识已存在 | 이 공급자 키가 이미 존재합니다. | This provider key already exists | 已修订 |
| pi.current.readFailed | 无法读取 Pi 供应商配置 | Pi의 공급자 설정을 읽을 수 없습니다. | Could not read Pi's provider configuration | 已修订 |
| pi.current.stateUnavailableHint | CC Switch 读取到 Pi 供应商配置前，供应商变更已暂时禁用。 | CC Switch가 Pi의 공급자 설정을 읽을 수 있을 때까지 공급자 변경은 비활성화됩니다. | Provider changes are disabled until CC Switch can read Pi's provider configuration. | 已修订 |
| pi.prompts.globalTab | 提示库 | 프롬프트 라이브러리 | Library | 已修订 |
| pi.prompts.systemTab | 系统提示 | 시스템 프롬프트 | System prompt | 保留 |
| pi.prompts.templatesTab | 模板 | 템플릿 | Templates | 保留 |
| pi.prompts.usePromptSuccess | 已写入全局 AGENTS.md | 전역 AGENTS.md에 저장했습니다 | Global AGENTS.md updated | 已修订 |
| pi.prompts.stopUsingSuccess | 已移除全局 AGENTS.md | 전역 AGENTS.md를 제거했습니다 | Global AGENTS.md removed | 已修订 |
| pi.prompts.systemAppend | 系统提示追加 | 시스템 프롬프트에 추가 | System append | 已修订 |
| pi.prompts.systemAppendDescription | 追加在 Pi 内置的基础提示之后 | Pi의 내장 기본 프롬프트 뒤에 추가됨 | Appended after Pi's built-in base prompt | 保留 |
| pi.prompts.systemOverride | 系统提示替换 | 시스템 프롬프트 교체 | System replacement | 已修订 |
| pi.prompts.systemOverrideDescription | 替换 Pi 内置的基础提示 | Pi의 내장 기본 프롬프트를 대체합니다. | Replaces Pi's built-in base prompt | 保留 |
| pi.prompts.systemOverrideWarning | SYSTEM.md 会替换 Pi 内置的基础提示；不需要完全控制基础指令时，用 APPEND_SYSTEM.md。 | SYSTEM.md는 Pi의 내장 기본 프롬프트를 대체합니다. 기본 명령어에 대한 전체 제어가 필요하지 않은 경우 APPEND_SYSTEM.md를 사용하세요. | SYSTEM.md replaces Pi's built-in base prompt. Unless you need full control of the base instructions, use APPEND_SYSTEM.md. | 保留 |
| pi.prompts.recommended | 推荐 | 추천 | Recommended | 保留 |
| pi.prompts.configuredEmpty | 已配置但为空 | 설정되었지만 비어 있음 | Configured but empty | 已修订 |
| pi.prompts.notConfigured | 未配置 | 설정되지 않음 | Not configured | 已修订 |
| pi.prompts.unavailable | 读取失败 | 읽기 실패 | Unavailable | 已修订 |
| pi.prompts.instructionPlaceholder | 给 Pi 的 Markdown 内容 | Pi에 전달할 Markdown 내용 | Markdown for Pi | 已修订 |
| pi.prompts.blankInstruction | 请输入非空白内容；不想用了就点左下角「删除文件」 | 비어 있지 않은 내용을 입력하세요. 사용을 중지하려면 왼쪽 하단의 파일 삭제를 클릭하세요. | Enter some non-blank content. To stop using it, click Delete file at the bottom left | 保留 |
| pi.prompts.saveAndConfigure | 保存并配置 | 저장 및 설정 | Save and configure | 已修订 |
| pi.prompts.activateOverrideTitle | 配置 {{filename}}？ | {{filename}}을(를) 설정하시겠습니까? | Configure {{filename}}? | 已修订 |
| pi.prompts.activateOverrideMessage | 创建 {{filename}} 会替换 Pi 内置基础提示。上下文、AGENTS.md 和 Skills 等仍由 Pi 按自身规则加入。 | {{filename}}을(를) 생성하면 Pi의 내장 기본 프롬프트가 대체됩니다. Pi는 여전히 자체 규칙에 따라 컨텍스트, AGENTS.md, Skills 및 기타 리소스를 추가합니다. | Creating {{filename}} replaces Pi's built-in base prompt. Pi still adds context, AGENTS.md, Skills, and other resources according to its own rules. | 已修订 |
| pi.prompts.fileSaved | {{filename}} 已保存 | {{filename}} 저장됨 | {{filename}} saved | 保留 |
| pi.prompts.saveFailed | 保存 Pi 指令文件失败 | Pi 지침 파일을 저장하지 못했습니다. | Failed to save the Pi instruction file | 保留 |
| pi.prompts.deleteFailed | 删除 Pi 指令文件失败 | Pi 지침 파일을 삭제하지 못했습니다. | Failed to delete the Pi instruction file | 保留 |
| pi.prompts.reloadNotice | 已打开的 Pi 不会自动热更新，空闲时运行 /reload；新启动的 Pi 会自动读取。 | 열린 Pi 세션은 핫 리로드되지 않습니다. 유휴 상태에서 /reload를 실행하세요. 새 세션에서는 자동으로 읽습니다. | Open Pi sessions don't hot-reload; run /reload while idle. New sessions read it automatically. | 保留 |
| pi.prompts.templatesDescription | 模板保存后可在 Pi 中通过 /命令名 调用，无需启用。 | 저장된 템플릿은 Pi에서 /command-name으로 사용할 수 있습니다. 활성화 단계가 필요하지 않습니다. | Saved templates are available in Pi as /command-name. No enable step is needed. | 保留 |
| pi.prompts.newTemplate | 新建模板 | 새 템플릿 | New template | 保留 |
| pi.prompts.editTemplate | 编辑 /{{slug}} | /{{slug}} 편집 | Edit /{{slug}} | 保留 |
| pi.prompts.templateCommand | 斜杠命令 | 슬래시 명령 | Slash command | 保留 |
| pi.prompts.templateSlug | 一个词，例如 review | 한 단어 (예: review) | One word, e.g. review | 已修订 |
| pi.prompts.templateSlugInvalid | 只能是一个词：字母、数字、- _ .，不能有空格或 / \ : * ? 等字符 | 영문자, 숫자, - _ .으로 된 한 단어를 사용하세요. 공백이나 / \\ : * ? 등의 문자는 사용할 수 없습니다. | Use one word: letters, digits, - _ . — no spaces or characters like / \ : * ? | 已修订 |
| pi.prompts.templateSlugExists | 已经有 /{{slug}} 了，换一个名字 | /{{slug}}가 이미 있습니다. 다른 이름을 선택하세요 | /{{slug}} already exists; pick another name | 已修订 |
| pi.prompts.templateDescription | 备注 | 메모 | Notes | 保留 |
| pi.prompts.templateDescriptionPlaceholder | 可选，写进模板开头的 description | 선택 사항. 템플릿 시작 부분의 description에 기록됩니다 | Optional, written to the template's description | 已修订 |
| pi.prompts.templateContent | 模板正文 | 템플릿 텍스트 | Template text | 保留 |
| pi.prompts.templateContentPlaceholder | 输入 Pi 将展开的 Markdown | Pi가 펼쳐 사용할 Markdown을 입력하세요 | Markdown that Pi will expand | 已修订 |
| pi.prompts.templateSyntax | 模板正文怎么写 | 템플릿 텍스트 작성 | Writing template text | 保留 |
| pi.prompts.templateSyntaxDescription | 可用 $1、$2、$@ 或 $ARGUMENTS 替换参数；开头可以写 frontmatter（description、argument-hint）。 | 인수에 $1, $2, $@ 또는 $ARGUMENTS를 사용할 수 있습니다. 문서 시작에 frontmatter(description, argument-hint)를 작성할 수도 있습니다. | Use $1, $2, $@ or $ARGUMENTS for arguments; you can start with frontmatter (description, argument-hint). | 已修订 |
| pi.prompts.createTemplate | 创建模板 | 템플릿 만들기 | Create template | 保留 |
| pi.prompts.templateCreated | 已创建 /{{slug}} | 생성됨 /{{slug}} | Created /{{slug}} | 保留 |
| pi.prompts.templateSaved | /{{slug}} 已保存 | /{{slug}}가 저장되었습니다. | /{{slug}} saved | 保留 |
| pi.prompts.templateLoadFailed | 读取 Pi 提示词模板失败 | Pi 프롬프트 템플릿을 로드하지 못했습니다. | Failed to load Pi prompt templates | 保留 |
| pi.prompts.templateSaveFailed | 保存 Pi 提示词模板失败 | Pi 프롬프트 템플릿을 저장하지 못했습니다. | Failed to save the Pi prompt template | 保留 |
| pi.prompts.templateDeleteFailed | 删除 Pi 提示词模板失败 | Pi 프롬프트 템플릿을 삭제하지 못했습니다. | Failed to delete the Pi prompt template | 保留 |
| pi.prompts.searchTemplates | 搜索命令或正文 | 명령 또는 텍스트 검색 | Search command or text | 保留 |
| pi.prompts.noTemplates | 还没有模板 | 아직 템플릿이 없습니다. | No templates yet | 保留 |
| pi.prompts.noTemplatesDescription | 保存后在 Pi 里输入 /命令名 调用。 | 저장 후 /command를 입력하여 Pi에서 실행합니다. | After saving, run it in Pi by typing /command. | 保留 |
| pi.prompts.noTemplateResults | 没有命令名、备注或正文匹配“{{query}}”的模板 | "{{query}}"와 일치하는 템플릿 명령, 메모 또는 텍스트가 없습니다. | No template command, note or text matches "{{query}}" | 保留 |
| pi.prompts.kindLabel | Pi 的提示词类型 | Pi 프롬프트 유형 | Pi prompt type | 保留 |
| pi.prompts.libraryLabel | Pi 的提示库 | Pi 프롬프트 라이브러리 | Pi prompt library | 保留 |
| pi.prompts.systemFilesLabel | Pi 的系统提示文件 | Pi 시스템 프롬프트 파일 | Pi system prompt files | 保留 |
| pi.prompts.templatesLabel | Pi 的提示词模板 | Pi 프롬프트 템플릿 | Pi prompt templates | 保留 |
| pi.prompts.externalTitle | AGENTS.md 在 CC Switch 之外改过 | AGENTS.md가 CC Switch 외부에서 변경되었습니다. | AGENTS.md was changed outside CC Switch | 保留 |
| pi.prompts.externalDetail | 内容（{{size}}）和提示库里的每一条都不同，所以没有哪条显示为已启用；启用别的之前会先存进提示库。 | 내용({{size}})이 라이브러리의 모든 프롬프트와 달라 활성화된 항목이 없습니다. 다른 프롬프트를 활성화하기 전에 현재 내용을 라이브러리에 저장합니다. | Its content ({{size}}) differs from every library prompt, so none shows as enabled. It's saved to the library before another one is enabled. | 已修订 |
| pi.prompts.saveToLibrary | 存进提示库 | 라이브러리에 저장 | Save to library | 保留 |
| pi.prompts.reloadAfterDelete | 已打开的 Pi 空闲时运行 /reload 后生效。 | 열려 있는 Pi 세션에서는 작업이 없을 때 /reload를 실행하면 적용됩니다. | Open Pi sessions pick this up after /reload while idle. | 已修订 |
| pi.prompts.configuredSize | 已配置 · {{size}} | 설정됨 · {{size}} | Configured · {{size}} | 已修订 |
| pi.prompts.create | 创建 | 만들기 | Create | 已修订 |
| pi.prompts.createFile | 创建 {{filename}} | {{filename}} 생성 | Create {{filename}} | 保留 |
| pi.prompts.editFile | 编辑 {{filename}} | {{filename}} 편집 | Edit {{filename}} | 保留 |
| pi.prompts.saveAndConfigureEllipsis | 保存并配置 | 저장 및 설정 | Save and configure | 已修订 |
| pi.prompts.deleteFile | 删除文件 | 파일 삭제 | Delete file | 保留 |
| pi.prompts.appendDeleted | 已删除 APPEND_SYSTEM.md，Pi 不再追加这段内容 | APPEND_SYSTEM.md가 삭제되었습니다. Pi는 더 이상 추가하지 않습니다. | Deleted APPEND_SYSTEM.md; Pi no longer appends it | 保留 |
| pi.prompts.overrideDeleted | 已删除 SYSTEM.md，Pi 改回使用内置的基础提示 | SYSTEM.md가 삭제되었습니다. Pi가 내장된 기본 프롬프트로 돌아왔습니다. | Deleted SYSTEM.md; Pi is back to its built-in base prompt | 保留 |
| pi.prompts.deletedUndoable | 撤销会把文件原样写回。 | 실행 취소하면 파일을 원래 내용으로 복원합니다. | Undo writes the file back as it was.  | 已修订 |
| pi.prompts.deletedBlank | 这个文件原本是空的，所以不能撤销。 | 파일이 비어 있으므로 이 작업은 실행취소할 수 없습니다. | The file was empty, so this can't be undone.  | 保留 |
| pi.prompts.fileRestored | 已写回 ~/.pi/agent/{{filename}} | ~/.pi/agent/{{filename}}에 원래 내용을 복원했습니다. | Wrote ~/.pi/agent/{{filename}} back | 已修订 |
| pi.prompts.templateSlugRequired | 填写命令名，例如 review | 명령 이름을 입력하세요 (예: review) | Enter a command name, e.g. review | 已修订 |
| pi.prompts.templateSaveTo | 保存到 {{path}} | 저장 위치: {{path}} | Saved to {{path}} | 已修订 |
| pi.prompts.templateRename | 保存后 /{{from}} 改名为 /{{to}} | 저장하면 /{{from}}의 이름이 /{{to}}로 바뀝니다 | Saving renames /{{from}} to /{{to}} | 已修订 |
| pi.prompts.searchTemplatesLabel | 搜索模板 | 템플릿 검색 | Search templates | 保留 |
| pi.prompts.copyCommand | 复制命令名 | 명령 이름 복사 | Copy command | 已修订 |
| pi.prompts.copiedCommand | 已复制 /{{slug}} | 복사됨 /{{slug}} | Copied /{{slug}} | 保留 |
| pi.prompts.templateDeletedUndo | 已删除 /{{slug}}，Pi 里不再有这个命令 | 삭제됨 /{{slug}}; Pi에는 더 이상 이 명령이 없습니다. | Deleted /{{slug}}; Pi no longer has this command | 保留 |
| pi.prompts.templateDeletedSub | 撤销会把 prompts/{{slug}}.md 原样写回。 | 실행 취소하면 prompts/{{slug}}.md를 원래 내용으로 복원합니다.  | Undo writes prompts/{{slug}}.md back as it was.  | 已修订 |
| pi.prompts.templateRestored | 已写回 ~/.pi/agent/prompts/{{slug}}.md | ~/.pi/agent/prompts/{{slug}}.md에 원래 내용을 복원했습니다. | Wrote ~/.pi/agent/prompts/{{slug}}.md back | 已修订 |
| appSwitcher.more | 更多应用 | 더 많은 앱 | More apps | 保留 |
| grokBuild.apiBackend | API Backend | API 백엔드 | API backend | 保留 |
| grokBuild.contextWindow | 上下文窗口 | 컨텍스트 창 | Context window | 保留 |
| grokBuild.contextWindowInvalid | 上下文窗口必须是正整数 | 컨텍스트 창은 양의 정수여야 합니다. | Context window must be a positive integer | 保留 |
| grokBuild.profile | 客户端模型档位 | 클라이언트 모델 프로필 | Client model profile | 保留 |
| grokBuild.rawConfig | config.toml | config.toml | config.toml | 保留 |
| grokBuild.invalidToml | config.toml 格式错误：{{error}} | 잘못된 config.toml: {{error}} | Invalid config.toml: {{error}} | 保留 |
| grokBuild.defaultModelPlaceholder | 例如: grok-4.5 | 예: grok-4.5 | e.g. grok-4.5 | 已修订 |
| grokBuild.defaultModelHint | Grok Build 默认请求的模型，随时可改。 | Grok Build가 기본으로 요청할 모델입니다. 언제든지 변경할 수 있습니다. | The model Grok Build requests by default; change it anytime. | 已修订 |
| grokBuild.reasoningEffortHint | 上游支持 low/high/max 等思考深度时打开。会同时打开思考模式，并把请求中的 reasoning effort 转成上游 Chat 参数。 | 업스트림이 low/high/max 같은 추론 수준을 지원할 때 켜세요. 추론 모드도 함께 켜고 요청의 reasoning effort를 업스트림 Chat 매개변수로 변환합니다. | Turn on when the upstream supports thinking depth such as low/high/max. Also turns on thinking mode and maps the request's reasoning effort to the upstream Chat parameter. | 已修订 |
| grokBuild.maxOutputTokensHint | 默认上限 8192，长回答或深度思考容易被截断。这里的值会作为 Anthropic 的 max_tokens 发出。 | 기본 제한인 8192에서는 긴 답변이나 깊은 추론이 잘릴 수 있습니다. 이 값은 Anthropic의 max_tokens로 전송됩니다. | The default limit of 8192 can cut off long answers or deep thinking. This value is sent as Anthropic's max_tokens. | 已修订 |
| grokBuild.keyFieldsHint | 默认模型（models.default）和它指向的模型表随供应商切换；其余是 Grok Build 全局设置，保存后对所有供应商生效。 | 기본 모델(models.default)과 해당 모델 테이블은 공급자를 전환하면 함께 바뀝니다. 나머지는 Grok Build 전역 설정이며 저장하면 모든 공급자에 적용됩니다. | The default model (models.default) and the model table it points to follow the provider; everything else is Grok Build global settings and applies to every provider after saving. | 已修订 |
| grokBuild.inactiveFieldsHint | 这些是旧版存进卡里的设置，现在切换不会写出去。点一下复制 TOML，需要时粘贴到上方。 | 이전 버전에 의해 이 공급자에 저장되었습니다. 전환하면 더 이상 적용되지 않습니다. 하나를 클릭하여 TOML를 복사하고 필요한 경우 위에 붙여넣습니다. | Saved in this provider by an older version; switching no longer applies them. Click one to copy its TOML and paste it above if you need it. | 已修订 |
| grokBuild.inactiveFieldCopied | 已复制 | 복사됨 | Copied | 保留 |
| grokBuild.routeOnlySettingsHint | 以下两项只在路由模式下生效。 | 아래 두 가지 설정은 라우팅 모드에서만 적용됩니다. | The two settings below only apply in routing mode. | 保留 |
| sessionManager.searchPlaceholder | 搜索标题、目录、首末消息或会话 ID | 제목, 폴더, 첫 번째/마지막 메시지 또는 세션 ID 검색 | Search titles, folders, first/last messages or session IDs | 保留 |
| sessionManager.searchSessions | 搜索会话 | 세션 검색 | Search sessions | 保留 |
| sessionManager.sessionList | 会话列表 | 세션 | Sessions | 保留 |
| sessionManager.unknownDirectory | 未知目录 | 알 수 없는 디렉터리 | Unknown directory | 保留 |
| sessionManager.batchDeleting | 删除中... | 삭제 중... | Deleting... | 保留 |
| sessionManager.loadingSessions | 加载会话中... | 세션 로드 중... | Loading sessions... | 保留 |
| sessionManager.piRelativeSessionDir | Pi 的 sessionDir 相对于启动 Pi 时的目录，全局浏览器无法安全枚举。请改用绝对 sessionDir，之后即可在此浏览全部 Pi 会话： | Pi sessionDir은 Pi가 시작된 디렉터리에 상대적이므로 글로벌 브라우저는 이를 안전하게 열거할 수 없습니다. 여기에서 모든 Pi 세션을 검색하려면 절대 sessionDir을 설정하세요. | Pi sessionDir is relative to the directory where Pi is launched, so a global browser cannot enumerate it safely. Set an absolute sessionDir to browse all Pi sessions here: | 保留 |
| sessionManager.piDiscoveryUnavailable | 无法检查 Pi 会话：{{error}} | Pi 세션을 검사할 수 없습니다: {{error}} | Pi sessions could not be inspected: {{error}} | 保留 |
| sessionManager.copyResumeCommand | 复制恢复命令 | 재개 명령 복사 | Copy resume command | 保留 |
| sessionManager.resumeCommandCopied | 已复制恢复命令 | 재개 명령이 복사되었습니다. | Resume command copied | 保留 |
| sessionManager.copySourcePath | 复制源文件路径 | 소스 파일 경로 복사 | Copy source file path | 保留 |
| sessionManager.sourcePathCopied | 已复制源文件路径 | 소스 파일 경로가 복사되었습니다. | Source file path copied | 保留 |
| sessionManager.deleteConfirmAction | 删除会话 | 세션 삭제 | Delete session | 保留 |
| sessionManager.sessionDeleted | 会话已删除 | 세션이 삭제되었습니다. | Session deleted | 保留 |
| sessionManager.deleteFailed | 删除会话失败: {{error}} | 세션 삭제 실패: {{error}} | Failed to delete session: {{error}} | 保留 |
| sessionManager.batchDeleteSuccess | 已删除 {{count}} 个会话 | {{count}} 세션을 삭제했습니다. | Deleted {{count}} sessions | 保留 |
| sessionManager.batchDeleteFailed | {{failed}} 个会话删除失败 | {{failed}} 세션을 삭제할 수 없습니다. | {{failed}} sessions could not be deleted | 保留 |
| sessionManager.batchDeleteRequestFailed | 批量删除失败，请稍后重试 | 일괄 삭제에 실패했습니다. 나중에 다시 시도해 주세요. | Batch delete failed. Please try again later. | 保留 |
| sessionManager.loadingMessages | 加载会话内容中... | 대화 내용 불러오는 중... | Loading transcript... | 已修订 |
| sessionManager.emptySession | 这个会话没有可显示的消息 | 이 세션에는 표시할 메시지가 없습니다. | This session has no messages to show | 保留 |
| sessionManager.justNow | 刚刚 | 방금 | Just now | 保留 |
| sessionManager.minutesAgo | {{count}} 分钟前 | {{count}}분 전 | {{count}} min ago | 保留 |
| sessionManager.hoursAgo | {{count}} 小时前 | {{count}}시간 전 | {{count}} hr ago | 保留 |
| sessionManager.daysAgo | {{count}} 天前 | {{count}}일 전 | {{count}} days ago | 保留 |
| sessionManager.roleSystem | 系统 | 시스템 | System | 已修订 |
| sessionManager.roleTool | 工具 | 도구 | Tool | 保留 |
| sessionManager.noResumeCommand | 此会话无法恢复 | 이 세션을 재개할 수 없습니다. | This session cannot be resumed | 保留 |
| sessionManager.messageCopied | 已复制这条消息 | 메시지가 복사되었습니다. | Message copied | 保留 |
| sessionManager.expandContent | 展开完整内容 | 전체 콘텐츠 펼치기 | Expand full content | 保留 |
| sessionManager.collapseContent | 收起 | 접기 | Collapse | 保留 |
| sessionManager.helpTitle | 会话从哪里来 | 세션의 출처 | Where sessions come from | 保留 |
| sessionManager.helpBody | CC Switch 读取各个应用保存在本机的会话记录，位置见右上角 ⋯ 里的「会话记录在哪里」。Claude Desktop 没有单独的会话记录。 | CC Switch는 각 앱이 이 컴퓨터에 보관하는 세션 기록을 읽습니다. ⋯ 메뉴에서 “세션이 저장되는 위치”를 참조하세요. Claude Desktop에는 자체 세션 기록이 없습니다. | CC Switch reads the session records each app keeps on this computer. See “Where sessions are stored” in the ⋯ menu. Claude Desktop has no session records of its own. | 保留 |
| sessionManager.moreActions | 会话的更多操作 | 추가 세션 작업 | More session actions | 保留 |
| sessionManager.refreshList | 刷新列表 | 목록 새로 고침 | Refresh list | 保留 |
| sessionManager.listRefreshed | 已刷新会话列表 | 세션 목록이 새로 고쳐졌습니다. | Session list refreshed | 保留 |
| sessionManager.selectMany | 选择多个 | 여러 개 선택 | Select multiple | 保留 |
| sessionManager.preferredTerminal | 首选终端 | 선호하는 터미널 | Preferred terminal | 保留 |
| sessionManager.whereMenu | 会话记录在哪里 | 세션이 저장되는 위치 | Where sessions are stored | 保留 |
| sessionManager.whereTitle | 会话记录在哪里 | 세션이 저장되는 위치 | Where sessions are stored | 保留 |
| sessionManager.whereLead | CC Switch 从这些位置读取会话。Claude Desktop 没有单独的会话记录。 | CC Switch는 이러한 위치에서 세션을 읽습니다. Claude Desktop에는 자체 세션 기록이 없습니다. | CC Switch reads sessions from these locations. Claude Desktop has no session records of its own. | 保留 |
| sessionManager.whereNote | 在设置里改过配置目录的应用，按改过的目录读取。 | 설정에 사용자 정의 설정 디렉터리가 있는 앱은 해당 디렉터리에서 읽혀집니다. | Apps with a custom config directory in Settings are read from that directory. | 已修订 |
| sessionManager.appPrefix | 应用： | 앱: | App:  | 保留 |
| sessionManager.chooseApp | 选择应用 | 앱 선택 | Choose app | 保留 |
| sessionManager.allApps | 全部应用 | 모든 앱 | All apps | 保留 |
| sessionManager.noSessionsCount | 无会话 | 없음 | None | 保留 |
| sessionManager.clearSearch | 清空搜索 | 검색 지우기 | Clear search | 保留 |
| sessionManager.foundCount | 找到 {{count}} 个会话 | {{count}} 세션을 찾았습니다. | {{count}} sessions found | 保留 |
| sessionManager.groupBy | 分组方式 | 그룹화 기준 | Group by | 保留 |
| sessionManager.groupByTime | 按时间 | 시간별 | By time | 保留 |
| sessionManager.groupByProject | 按项目 | 프로젝트별 | By project | 保留 |
| sessionManager.desktopNote | Claude Desktop 没有单独的会话记录，这里显示 Claude Code 的会话。 | Claude Desktop에는 자체 세션 기록이 없습니다. Claude Code 세션을 표시합니다. | Claude Desktop has no session records of its own. Showing Claude Code sessions. | 保留 |
| sessionManager.matchCount | 匹配 {{count}} 个会话 | 일치하는 세션 {{count}}개 | {{count}} matching sessions | 已修订 |
| sessionManager.totalCount | 共 {{count}} 个会话 | 세션 {{count}}개 | {{count}} sessions | 已修订 |
| sessionManager.selectAllMatches | 全选匹配结果 | 모든 일치 항목 선택 | Select all matches | 保留 |
| sessionManager.clearSelectionShort | 清空 | 지우기 | Clear | 保留 |
| sessionManager.exitSelection | 退出选择 | 선택 모드 종료 | Done selecting | 已修订 |
| sessionManager.selectedSessions | 已选 {{count}} 个会话 | {{count}} 세션이 선택되었습니다. | {{count}} sessions selected | 保留 |
| sessionManager.noneSelected | 还没有选择会话 | 선택된 세션이 없습니다. | No sessions selected | 保留 |
| sessionManager.hiddenSelected |  · 其中 {{count}} 个不在当前结果里 |  · 이 중 {{count}}개는 현재 검색 결과에 없음 |  · {{count}} not in the current results | 已修订 |
| sessionManager.deleteCountEllipsis | 删除 {{count}} 个会话 | {{count}} 세션 삭제 | Delete {{count}} sessions | 保留 |
| sessionManager.deleteSessionEllipsis | 删除会话 | 세션 삭제 | Delete sessions | 保留 |
| sessionManager.deleteEllipsis | 删除 | 삭제 | Delete | 保留 |
| sessionManager.selectSessionLabel | 选择 {{title}} | {{title}}을(를) 선택하세요 | Select {{title}} | 已修订 |
| sessionManager.agyDeleteHint | 请在 Antigravity 中删除会话，以同步清理运行状态 | 런타임 상태도 제거하려면 Antigravity에서 이 세션을 삭제하세요. | Delete this session in Antigravity to also remove its runtime state | 保留 |
| sessionManager.mcodeDeleteHint | 请在 MiniMax Code 中删除 | MiniMax Code에서 삭제하세요. | Delete it in MiniMax Code | 保留 |
| sessionManager.groupMeta | {{count}} 个会话 · {{time}} | {{count}} 세션 · {{time}} | {{count}} sessions · {{time}} | 保留 |
| sessionManager.bucketToday | 今天 | 오늘 | Today | 保留 |
| sessionManager.bucketYesterday | 昨天 | 어제 | Yesterday | 保留 |
| sessionManager.bucketThisWeek | 本周 | 이번 주 | This week | 已修订 |
| sessionManager.bucketEarlier | 更早 | 이전 | Earlier | 已修订 |
| sessionManager.lastPrefix | 最后：{{text}} | 마지막: {{text}} | Last: {{text}} | 保留 |
| sessionManager.archived | 已归档 | 보관됨 | Archived | 保留 |
| sessionManager.rowTimes | 最近活跃 {{last}} · 创建 {{created}} | 최근 활동 {{last}} · 생성 {{created}} | Last active {{last}} · Created {{created}} | 已修订 |
| sessionManager.resumeIn | 在 {{terminal}} 中恢复 | {{terminal}}에서 이어가기 | Resume in {{terminal}} | 已修订 |
| sessionManager.resumeInFor | 在 {{terminal}} 中恢复 {{title}} | {{terminal}}에서 {{title}} 재개 | Resume {{title}} in {{terminal}} | 保留 |
| sessionManager.copyResumeFor | 复制「{{title}}」的恢复命令 | "{{title}}"에 대한 재개 명령을 복사합니다. | Copy the resume command for “{{title}}” | 保留 |
| sessionManager.resumeCopiedNoLaunch | 已复制恢复命令。这个平台暂不支持一键恢复，请在项目目录下粘贴到终端运行 | 이어가기 명령을 복사했습니다. 이 플랫폼에서는 한 번의 클릭으로 세션을 이어갈 수 없습니다. 프로젝트 폴더에서 터미널을 열어 명령을 붙여 넣으세요. | Resume command copied. One-click resume isn’t available on this platform; paste it into a terminal in the project folder. | 已修订 |
| sessionManager.moreFor | {{title}} 的更多操作 | {{title}}에 대한 추가 작업 | More actions for {{title}} | 保留 |
| sessionManager.copySessionId | 复制会话 ID | 세션 ID 복사 | Copy session ID | 保留 |
| sessionManager.sessionIdCopied | 已复制会话 ID | 세션 ID가 복사되었습니다. | Session ID copied | 保留 |
| sessionManager.hermesLimit | Hermes 只显示最近 500 个会话 | Hermes는 최근 500개의 세션만 표시합니다. | Hermes shows only the latest 500 sessions | 保留 |
| sessionManager.emptyApp | 还没有 {{app}} 的会话记录 | 아직 {{app}} 세션이 없습니다. | No {{app}} sessions yet | 保留 |
| sessionManager.emptyAll | 还没有会话记录 | 아직 세션이 없습니다. | No sessions yet | 保留 |
| sessionManager.emptyAppHint | CC Switch 读取 {{path}} 下的会话数据 | CC Switch는 {{path}}에서 세션 데이터를 읽습니다. | CC Switch reads session data from {{path}} | 保留 |
| sessionManager.emptySearch | 没有标题、目录或首末消息匹配“{{query}}”的会话 | 세션 제목, 폴더 또는 첫 번째/마지막 메시지가 "{{query}}"와 일치하지 않습니다. | No session titles, folders or first/last messages match “{{query}}” | 保留 |
| sessionManager.clearSearchAction | 清除搜索 | 검색 지우기 | Clear search | 保留 |
| sessionManager.backToList | 返回会话列表 | 세션 목록으로 돌아가기 | Back to sessions | 已修订 |
| sessionManager.back | 返回 | 뒤로 | Back | 保留 |
| sessionManager.sessionOf | {{app}} 的会话 | {{app}} 세션 | {{app}} session | 保留 |
| sessionManager.prevSession | 上一个会话 | 이전 세션 | Previous session | 保留 |
| sessionManager.nextSession | 下一个会话 | 다음 세션 | Next session | 保留 |
| sessionManager.prevShort | 上一个 | 이전 | Previous | 保留 |
| sessionManager.nextShort | 下一个 | 다음 | Next | 保留 |
| sessionManager.copyPathAria | 复制路径 {{path}} | 경로 {{path}} 복사 | Copy path {{path}} | 保留 |
| sessionManager.copyPathTitle | 复制路径 | 경로 복사 | Copy path | 保留 |
| sessionManager.pathCopied | 已复制路径 {{path}} | {{path}}을(를) 복사했습니다. | Copied {{path}} | 已修订 |
| sessionManager.messageCount | {{count}} 条消息 | 메시지 {{count}}개 | {{count}} messages | 已修订 |
| sessionManager.moreResumeOptions | 更多恢复方式 | 재개하는 다양한 방법 | More ways to resume | 保留 |
| sessionManager.copyCdResume | 复制「进入目录并恢复」命令 | "cd 및 재개" 명령 복사 | Copy “cd and resume” command | 保留 |
| sessionManager.cdResumeCopied | 已复制「进入目录并恢复」命令 | "cd 및 재개" 명령이 복사되었습니다. | “cd and resume” command copied | 保留 |
| sessionManager.changeTerminal | 更换首选终端 | 선호하는 터미널 변경 | Change preferred terminal | 保留 |
| sessionManager.changeTerminalAction | 更换终端 | 터미널 변경 | Change terminal | 保留 |
| sessionManager.codexResumeNote | 切换过供应商后，旧会话可能无法继续：Codex 按供应商分开保存历史。 | 공급자를 전환한 후에는 이전 세션이 재개되지 않을 수 있습니다. Codex는 공급자별로 기록을 별도로 유지합니다. | Older sessions may not resume after switching providers: Codex keeps history separately per provider. | 已修订 |
| sessionManager.noResumeOpenclaw | OpenClaw 会话由网关管理，不能在终端恢复 | OpenClaw 세션은 게이트웨이에 의해 관리되며 터미널에서 재개될 수 없습니다. | OpenClaw sessions are managed by its gateway and can’t be resumed in a terminal | 保留 |
| sessionManager.noResumeHermes | 暂不支持从命令行恢复 Hermes 会话 | 명령줄에서 Hermes 세션 재개는 아직 지원되지 않습니다. | Resuming Hermes sessions from the command line isn’t supported yet | 保留 |
| sessionManager.launchedIn | 已在 {{terminal}} 中运行恢复命令 | {{terminal}}에서 재개 명령을 실행했습니다. | Ran the resume command in {{terminal}} | 保留 |
| sessionManager.launchFailed | 无法打开 {{terminal}}：{{error}}。恢复命令已复制，可以粘贴到任意终端运行。 | {{terminal}}을(를) 열 수 없습니다: {{error}}. 이어가기 명령을 복사했으니 원하는 터미널에 붙여 넣어 실행하세요. | Couldn’t open {{terminal}}: {{error}}. The resume command was copied; paste it into any terminal. | 已修订 |
| sessionManager.onlyChat | 只看对话 | 대화만 보기 | Chat only | 已修订 |
| sessionManager.questions | 提问 | 질문 | Prompts | 已修订 |
| sessionManager.questionsMenu | 跳到提问 | 질문으로 이동 | Jump to a prompt | 已修订 |
| sessionManager.findInSession | 在会话中查找 | 세션에서 찾기 | Find in session | 保留 |
| sessionManager.findShort | 查找 | 찾기 | Find | 已修订 |
| sessionManager.findLabel | 查找内容 | 텍스트 찾기 | Find text | 保留 |
| sessionManager.findPrev | 上一个匹配 | 이전 일치 항목 | Previous match | 已修订 |
| sessionManager.findNext | 下一个匹配 | 다음 일치 항목 | Next match | 已修订 |
| sessionManager.findClose | 关闭查找 | 찾기 닫기 | Close find | 保留 |
| sessionManager.copyAsMarkdown | 复制整段为 Markdown | 전체 대화를 Markdown으로 복사 | Copy as Markdown | 已修订 |
| sessionManager.markdownCopied | 已复制整段对话（Markdown） | 대화가 Markdown으로 복사되었습니다. | Conversation copied as Markdown | 保留 |
| sessionManager.reload | 重新读取 | 다시 읽기 | Reload | 已修订 |
| sessionManager.reloaded | 已重新读取这个会话 | 세션이 다시 로드되었습니다. | Session reloaded | 保留 |
| sessionManager.readFailed | 无法读取这个会话 | 이 세션을 읽을 수 없습니다. | Couldn’t read this session | 保留 |
| sessionManager.you | 你 | 사용자 | You | 已修订 |
| sessionManager.copyQuestion | 复制这条提问 | 이 질문 복사 | Copy this prompt | 已修订 |
| sessionManager.copyReply | 复制这条回复 | 이 답글 복사 | Copy this reply | 保留 |
| sessionManager.copyShort | 复制 | 복사 | Copy | 保留 |
| sessionManager.copyCode | 复制代码 | 코드 복사 | Copy code | 保留 |
| sessionManager.codeCopied | 已复制代码 | 코드가 복사되었습니다. | Code copied | 保留 |
| sessionManager.codeRegion | {{lang}} 代码 | {{lang}} 코드 | {{lang}} code | 保留 |
| sessionManager.toolCalls | 工具调用： | 도구 호출: | Tool calls:  | 保留 |
| sessionManager.toolOutput | 工具输出 · {{size}} 字 | 도구 출력 · {{size}} 문자 | Tool output · {{size}} chars | 保留 |
| sessionManager.toolOutputRegion | 工具输出 | 도구 출력 | Tool output | 保留 |
| sessionManager.toolOutputMore | 还有 {{count}} 行 | {{count}}줄 더 있음 | {{count}} more lines | 已修订 |
| sessionManager.showAll | 显示全部 | 모두 표시 | Show all | 保留 |
| sessionManager.jumpLatest | 跳到最新消息 | 최신 메시지로 이동 | Jump to latest message | 保留 |
| sessionManager.latest | 最新 | 최신 | Latest | 保留 |
| sessionManager.deleteOneTitle | 删除会话「{{title}}」？ | '{{title}}' 세션을 삭제하시겠습니까? | Delete session “{{title}}”? | 保留 |
| sessionManager.deleteManyTitle | 删除 {{count}} 个会话？ | {{count}} 세션을 삭제하시겠습니까? | Delete {{count}} sessions? | 保留 |
| sessionManager.deleteLead | 会从磁盘上永久删除，不经过废纸篓，无法撤销。 | 휴지통을 건너뛰고 디스크에서 영구적으로 삭제됩니다. 이 작업은 취소할 수 없습니다. | They’ll be permanently deleted from disk, skipping the Trash. This can’t be undone. | 保留 |
| sessionManager.deleteAppCount | {{app}} {{count}} 个 | {{app}} ({{count}}) | {{app}} ({{count}}) | 保留 |
| sessionManager.deleteManyAction | 删除 {{count}} 个会话 | {{count}} 세션 삭제 | Delete {{count}} sessions | 保留 |
| sessionManager.consequenceClaude | 删除会话文件和同名附属目录。Claude Code 的 Agents 面板里可能还会留一条记录。 | 세션 파일과 동일한 이름의 폴더를 삭제합니다. Claude Code의 에이전트 패널에는 여전히 표시될 수 있습니다. | Deletes the session file and its same-named folder. Claude Code’s Agents panel may still list it. | 保留 |
| sessionManager.consequenceCodex | 只删除这一个会话文件。Codex 桌面版的任务列表里可能仍显示它，点开会提示无法继续。 | 이 세션 파일만 삭제합니다. Codex 데스크톱 앱의 작업 목록에는 계속 표시될 수 있지만, 열면 이어갈 수 없다는 메시지가 나타납니다. | Deletes only this session file. The Codex desktop app may still list it and say it can’t be continued. | 已修订 |
| sessionManager.consequenceGrok | 删除这个会话的整个目录。 | 이 세션의 전체 폴더를 삭제합니다. | Deletes this session’s entire folder. | 保留 |
| sessionManager.consequenceGeneric | 从 {{app}} 的本地记录中永久删除。 | {{app}}의 로컬 기록에서 영구적으로 제거됩니다. | Permanently removed from {{app}}’s local records. | 已修订 |
| sessionManager.sessionDeletedNamed | 已删除会话「{{title}}」 | ‘{{title}}’ 세션을 삭제했습니다 | Deleted session “{{title}}” | 已修订 |
| sessionManager.remoteImage | 远程图片 | 원격 이미지 | Remote image | 保留 |
| sessionManager.reader.timelineSummary | 执行过程 · {{steps}} 步 | 실행 과정 · {{steps}}단계 | Steps · {{steps}} | 已修订 |
| sessionManager.reader.summaryCommands | {{count}} 个命令 | {{count}} 명령 | {{count}} commands | 保留 |
| sessionManager.reader.summaryFiles | 改了 {{count}} 个文件 | {{count}} 파일이 변경되었습니다. | {{count}} files changed | 保留 |
| sessionManager.reader.summaryErrors | {{count}} 个失败 | {{count}} 실패 | {{count}} failed | 保留 |
| sessionManager.reader.summaryDuration | ⏱ {{duration}} | ⏱ {{duration}} | ⏱ {{duration}} | 保留 |
| sessionManager.reader.summaryTokens | {{tokens}} tok | {{tokens}} tok | {{tokens}} tok | 已修订 |
| sessionManager.reader.expandTimeline | 展开执行过程 | 실행 단계 펼치기 | Expand steps | 已修订 |
| sessionManager.reader.collapseTimeline | 收起执行过程 | 실행 단계 접기 | Collapse steps | 已修订 |
| sessionManager.reader.expandAllTimelines | 展开全部过程 | 모든 실행 단계 펼치기 | Expand all steps | 已修订 |
| sessionManager.reader.moreFailures | 还有 {{count}} 个失败 | 실패 {{count}}개 더 있음 | {{count}} more failed | 已修订 |
| sessionManager.reader.stepExpand | 展开 {{title}} 的详情 | {{title}}에 대한 세부정보 표시 | Show details for {{title}} | 保留 |
| sessionManager.reader.stepCollapse | 收起 | 접기 | Hide | 已修订 |
| sessionManager.reader.status.success | 成功 | 성공함 | Succeeded | 保留 |
| sessionManager.reader.status.error | 失败 | 실패 | Failed | 已修订 |
| sessionManager.reader.status.interrupted | 已中断 | 중단됨 | Interrupted | 已修订 |
| sessionManager.reader.status.pending | 进行中 | 실행 중 | Running | 已修订 |
| sessionManager.reader.status.unknown | 未知 | 알 수 없음 | Unknown | 保留 |
| sessionManager.reader.exitCode | exit {{code}} | 종료 코드 {{code}} | exit {{code}} | 已修订 |
| sessionManager.reader.lines | {{count}} 行 | {{count}}줄 | {{count}} lines | 已修订 |
| sessionManager.reader.moreLines | 还有 {{count}} 行 | {{count}}줄 더 있음 | {{count}} more lines | 已修订 |
| sessionManager.reader.showAll | 显示全部 | 모두 표시 | Show all | 保留 |
| sessionManager.reader.loadMore | 加载更多 | 더 로드하기 | Load more | 保留 |
| sessionManager.reader.tooLarge | 内容超过 2 MB，请复制源文件路径后在本地查看 | 콘텐츠가 2MB를 초과합니다. 소스 파일 경로를 복사하고 로컬에서 봅니다. | Content exceeds 2 MB. Copy the source file path and view it locally. | 保留 |
| sessionManager.reader.loading | 加载中… | 로드 중… | Loading… | 保留 |
| sessionManager.reader.loadFailed | 无法读取完整内容 | 전체 콘텐츠를 로드할 수 없습니다. | Couldn't load the full content | 保留 |
| sessionManager.reader.params | 参数 | 매개변수 | Input | 已修订 |
| sessionManager.reader.output | 输出 | 출력 | Output | 已修订 |
| sessionManager.reader.diff | 改动 | 변경 사항 | Changes | 保留 |
| sessionManager.reader.thinking.claude | 思考中… | 추론 중… | Thinking… | 已修订 |
| sessionManager.reader.thinking.codex | 推理 | 추론 | Reasoning | 已修订 |
| sessionManager.reader.thinking.gemini | 想法 | 추론 내용 | Thoughts | 已修订 |
| sessionManager.reader.thinking.opencode | Thought | 추론 내용 | Thought | 已修订 |
| sessionManager.reader.thinking.pi | Thinking… | 추론 중… | Thinking… | 已修订 |
| sessionManager.reader.thinking.generic | 思考 | 추론 | Thinking | 已修订 |
| sessionManager.reader.thinkingMeta | {{chars}} 字 · {{duration}} | {{chars}} 문자 · {{duration}} | {{chars}} chars · {{duration}} | 保留 |
| sessionManager.reader.thinkingChars | {{chars}} 字 | {{chars}} 문자 | {{chars}} chars | 保留 |
| sessionManager.reader.thinkingRedacted | 思考内容不可见 | 추론 내용을 볼 수 없음 | Thinking not visible | 已修订 |
| sessionManager.reader.note | 说明 | 설명 | Note | 已修订 |
| sessionManager.reader.noteExpand | 展开说明 | 설명 펼치기 | Show full note | 已修订 |
| sessionManager.reader.noFinalReply | 这一轮没有最终回复 | 이번 차례에는 최종 답변이 없습니다. | No final reply in this turn | 保留 |
| sessionManager.reader.turnAborted | 已中断 | 중단됨 | Interrupted | 已修订 |
| sessionManager.reader.event.compaction | 上下文已压缩 | 컨텍스트가 압축됨 | Context compacted | 保留 |
| sessionManager.reader.event.modelChange | 模型切换为 {{model}} | {{model}}로 모델 변경 | Switched model to {{model}} | 保留 |
| sessionManager.reader.event.thinkingLevel | 思考强度：{{level}} | 추론 수준: {{level}} | Thinking level: {{level}} | 已修订 |
| sessionManager.reader.event.hookError | Hook 执行出错 | 후크 실패 | Hook failed | 保留 |
| sessionManager.reader.event.prLink | 已关联 PR #{{number}} | 연결된 PR #{{number}} | Linked PR #{{number}} | 保留 |
| sessionManager.reader.event.prLinkPlain | 已关联 PR | PR을 연결했습니다 | Linked a PR | 保留 |
| sessionManager.reader.event.slashCommand | 运行了 {{command}} | {{command}}을(를) 실행 | Ran {{command}} | 已修订 |
| sessionManager.reader.event.subAgent | 子代理 {{name}} | 서브에이전트 {{name}} | Subagent {{name}} | 保留 |
| sessionManager.reader.injectedToggle | 显示注入的上下文 | 주입된 컨텍스트 표시 | Show injected context | 保留 |
| sessionManager.reader.injectedRow | 上下文 · {{label}} · {{chars}} 字 | 컨텍스트 · {{label}} · {{chars}} 문자 | Context · {{label}} · {{chars}} chars | 保留 |
| sessionManager.reader.image.alt | 图 {{index}} | 이미지 {{index}} | Image {{index}} | 保留 |
| sessionManager.reader.image.open | 放大查看 | 크게 보기 | View larger | 保留 |
| sessionManager.reader.image.close | 关闭图片 | 이미지 닫기 | Close image | 保留 |
| sessionManager.reader.image.copy | 复制图片 | 이미지 복사 | Copy image | 保留 |
| sessionManager.reader.image.copied | 已复制图片 | 이미지가 복사되었습니다. | Image copied | 保留 |
| sessionManager.reader.image.failed | 无法加载图片 | 이미지를 로드할 수 없습니다. | Couldn't load image | 保留 |
| sessionManager.reader.image.loadRemote | 加载远程图片 | 원격 이미지 로드 | Load remote image | 保留 |
| sessionManager.reader.image.fit | 适应窗口 | 창에 맞추기 | Fit to window | 保留 |
| sessionManager.reader.image.actualSize | 原始大小 | 실제 크기 | Actual size | 保留 |
| sessionManager.reader.link.openExternal | 在浏览器中打开 {{url}} | 브라우저에서 {{url}} 열기 | Open {{url}} in browser | 保留 |
| sessionManager.reader.path.copy | 复制路径 | 경로 복사 | Copy path | 保留 |
| sessionManager.reader.path.reveal | 在 Finder 中显示 | Finder에 표시 | Show in Finder | 保留 |
| sessionManager.reader.merged.explored | 查看了 {{files}} 个文件、搜索 {{searches}} 次 | {{files}} 파일 읽기, {{searches}}회 검색 | Read {{files}} files, searched {{searches}} times | 保留 |
| sessionManager.reader.merged.mcpTimes | 调用 {{server}} {{count}} 次 | {{server}} {{count}} 번 호출 | Called {{server}} {{count}} times | 保留 |
| sessionManager.reader.turnsCount | {{turns}} 轮 · {{messages}} 条 | {{turns}}턴 · 메시지 {{messages}}개 | {{turns}} turns · {{messages}} messages | 已修订 |
| sessionManager.reader.questionsCount | {{count}} 次提问 | 질문 {{count}}회 | {{count}} prompts | 已修订 |
| sessionManager.reader.toolsCount | {{count}} 次工具调用 | {{count}} 도구 호출 | {{count}} tool calls | 保留 |
| sessionManager.reader.usage.tokens | {{tokens}} Tokens | {{tokens}} 토큰 | {{tokens}} tokens | 保留 |
| sessionManager.reader.usage.detail | {{requests}} 次请求 · 按 API 价估算<br>输入 {{input}} · 输出 {{output}}<br>缓存写入 {{cacheWrite}} · 缓存读取 {{cacheRead}} | {{requests}} 요청 · API 가격으로 추정<br>입력 {{input}} · 출력 {{output}}<br>캐시 쓰기 {{cacheWrite}} · 캐시 읽기 {{cacheRead}} | {{requests}} requests · estimated at API prices<br>Input {{input}} · Output {{output}}<br>Cache write {{cacheWrite}} · Cache read {{cacheRead}} | 保留 |
| sessionManager.reader.loadingProgress | 已加载 {{loaded}} / {{total}} | {{loaded}} / {{total}} 로드됨 | Loaded {{loaded}} / {{total}} | 保留 |
| sessionManager.reader.verb.run | 运行 | 실행 | Run | 已修订 |
| sessionManager.reader.verb.read | 读取 | 읽기 | Read | 已修订 |
| sessionManager.reader.verb.search | 搜索 | 검색 | Search | 已修订 |
| sessionManager.reader.verb.edit | 修改 | 편집 | Edit | 已修订 |
| sessionManager.reader.verb.write | 写入 | 쓰기 | Write | 已修订 |
| sessionManager.reader.verb.web | 网页 | 웹 | Web | 已修订 |
| sessionManager.reader.verb.mcp | MCP | MCP | MCP | 保留 |
| sessionManager.reader.verb.agent | 子代理 | 서브에이전트 | Subagent | 已修订 |
| sessionManager.reader.verb.ask | 提问 | 질문 | Ask | 已修订 |
| sessionManager.reader.verb.todo | 待办 | 할 일 | Todos | 已修订 |
| sessionManager.reader.verb.other | 工具 | 도구 | Tool | 保留 |
| sessionManager.reader.verb.output | 工具输出 | 도구 출력 | Tool output | 保留 |
| sessionManager.reader.copyTurn | 复制这一轮 | 이번 턴 복사 | Copy this turn | 保留 |
| sessionManager.reader.turnCopied | 已复制这一轮 | 이번 턴을 복사했습니다 | Copied this turn | 已修订 |
| sessionManager.reader.copyWithThinking | 复制时包含思考 | 복사할 때 추론 내용 포함 | Include thinking when copying | 已修订 |
| sessionManager.reader.filterAll | 全部 | 모두 | All | 保留 |
| sessionManager.reader.filterChat | 对话 | 채팅 | Chat | 保留 |
| sessionManager.reader.filterChanges | 改动 | 변경 사항 | Changes | 保留 |
| sessionManager.reader.filterLabel | 视图 | 보기 | View | 保留 |
| sessionManager.reader.exportMarkdown | 导出为 Markdown 文件 | 마크다운 파일로 내보내기 | Export as Markdown file | 保留 |
| sessionManager.reader.exportShort | 导出 | 내보내기 | Export | 保留 |
| sessionManager.reader.exported | 已导出到 {{path}} | {{path}}로 내보냈습니다. | Exported to {{path}} | 保留 |
| sessionManager.reader.exportFailed | 导出失败：{{error}} | 내보내기 실패: {{error}} | Export failed: {{error}} | 保留 |
| sessionManager.reader.conversationRegion | 对话内容 | 대화 내용 | Conversation content | 保留 |
| sessionManager.reader.outlineTitle | 对话目录 | 대화 목차 | Conversation | 已修订 |
| sessionManager.reader.outlineToggle | 对话目录 | 대화 목차 | Conversation outline | 已修订 |
| sessionManager.reader.outlineEmptyQuestion | （只有图片） | (이미지만) | (images only) | 保留 |
| sessionManager.reader.outlineSteps | {{count}} 步 | {{count}} 단계 | {{count}} steps | 保留 |
| sessionManager.reader.outlineFailed | 有失败步骤 | 실패한 단계가 있음 | Has failed steps | 保留 |
| sessionManager.reader.outlineAborted | 已中断 | 중단됨 | Interrupted | 已修订 |
| sessionManager.reader.outlineNoReply | 没有回复 | 답장 없음 | No reply | 保留 |
| sessionManager.reader.viewOptions | 显示选项 | 디스플레이 옵션 | Display options | 保留 |
| sessionManager.reader.noChanges | 这个会话没有文件改动 | 이 세션에는 파일 변경 사항이 없습니다 | No file changes in this session | 已修订 |
| sessionManager.reader.rawMatch | 原文中的匹配 | 원문에서 일치하는 내용 | Matches in source | 已修订 |
| sessionManager.reader.expandContent | 展开完整内容 | 전체 콘텐츠 표시 | Show full content | 保留 |
| sessionManager.reader.collapseContent | 收起 | 접기 | Collapse | 保留 |
| console.providerSwitchReceived | 收到供应商切换事件: | 수신된 공급자 전환 이벤트: | Received provider switch event: | 已修订 |
| console.setupListenerFailed | 设置供应商切换监听器失败: | 공급자 전환 이벤트 수신기 설정 실패: | Failed to setup provider switch listener: | 已修订 |
| console.updateProviderFailed | 更新供应商失败: | 공급자 업데이트 실패: | Update provider failed: | 已修订 |
| console.autoImportFailed | 自动导入默认配置失败: | 기본 설정 자동 가져오기 실패: | Auto import default configuration failed: | 已修订 |
| console.openLinkFailed | 打开链接失败: | 링크를 열지 못했습니다: | Failed to open link: | 保留 |
| console.getVersionFailed | 获取版本信息失败: | 버전 정보를 가져오지 못했습니다: | Failed to get version info: | 保留 |
| console.loadSettingsFailed | 加载设置失败: | 설정을 로드하지 못했습니다: | Failed to load settings: | 保留 |
| console.getConfigPathFailed | 获取配置路径失败: | 설정 경로를 가져오지 못했습니다. | Failed to get config path: | 已修订 |
| console.getConfigDirFailed | 获取配置目录失败: | 설정 디렉터리를 가져오지 못했습니다. | Failed to get config directory: | 已修订 |
| console.detectPortableFailed | 检测便携模式失败: | 휴대용 모드를 감지하지 못했습니다. | Failed to detect portable mode: | 保留 |
| console.saveSettingsFailed | 保存设置失败: | 설정을 저장하지 못했습니다. | Failed to save settings: | 保留 |
| console.updateFailed | 更新失败: | 업데이트 실패: | Update failed: | 保留 |
| console.checkUpdateFailed | 检查更新失败: | 업데이트 확인 실패: | Check for updates failed: | 保留 |
| console.openConfigFolderFailed | 打开配置文件夹失败: | 설정 폴더를 열지 못했습니다: | Failed to open config folder: | 已修订 |
| console.selectConfigDirFailed | 选择配置目录失败: | 설정 디렉터리를 선택하지 못했습니다. | Failed to select config directory: | 已修订 |
| console.getDefaultConfigDirFailed | 获取默认配置目录失败: | 기본 설정 디렉터리를 가져오지 못했습니다. | Failed to get default config directory: | 已修订 |
| console.openReleaseNotesFailed | 打开更新日志失败: | 릴리스 노트를 열지 못했습니다: | Failed to open release notes: | 已修订 |
| providerForm.supplierName | 供应商名称 | 공급자 이름 | Provider Name | 已修订 |
| providerForm.supplierNameRequired | 供应商名称 * | 공급자 이름 * | Provider Name * | 已修订 |
| providerForm.supplierNamePlaceholder | 例如：Anthropic 官方 | 예: Anthropic 공식 | e.g., Anthropic Official | 保留 |
| providerForm.websiteUrl | 官网地址 | 웹사이트 URL | Website URL | 保留 |
| providerForm.websiteUrlPlaceholder | https://example.com（可选） | https://example.com(옵션) | https://example.com (optional) | 保留 |
| providerForm.apiEndpoint | 请求地址 | API 엔드포인트 | API Endpoint | 保留 |
| providerForm.apiEndpointPlaceholder | https://your-api-endpoint.com | https://your-api-endpoint.com | https://your-api-endpoint.com | 保留 |
| providerForm.codexApiEndpointPlaceholder | https://your-api-endpoint.com/v1 | https://your-api-endpoint.com/v1 | https://your-api-endpoint.com/v1 | 保留 |
| providerForm.manageAndTest | 管理与测速 | 관리 및 테스트 | Manage & Test | 保留 |
| providerForm.configContent | 配置内容 | 설정 내용 | Config Content | 已修订 |
| providerForm.officialNoApiKey | 官方登录无需填写 API Key，直接保存即可 | 공식 로그인에는 API 키가 필요하지 않습니다. 바로 저장하세요 | Official login does not require API Key, save directly | 已修订 |
| providerForm.codexOfficialNoApiKey | 官方无需填写 API Key，直接保存即可 | 공식 공급자에는 API 키가 필요하지 않습니다. 바로 저장하세요 | Official does not require API Key, save directly | 已修订 |
| providerForm.codexApiKeyAutoFill | 只需要填这里，下方 auth.json 会自动填充 | 여기에 입력하면 아래 auth.json이 자동으로 채워집니다. | Just fill in here, auth.json below will be auto-filled | 保留 |
| providerForm.apiKeyAutoFill | 只需要填这里，下方配置会自动填充 | 여기에만 입력하면 아래 설정이 자동으로 채워집니다. | Just fill in here, config below will be auto-filled | 已修订 |
| providerForm.cnOfficialApiKeyHint | 💡 只需填写 API Key，请求地址已预设 | 💡 API 키만 입력하면 됩니다. 엔드포인트는 미리 설정되어 있습니다. | 💡 Only need to fill in API Key, endpoint is preset | 保留 |
| providerForm.aggregatorApiKeyHint | 💡 只需填写 API Key，请求地址已预设 | 💡 API 키만 입력하면 됩니다. 엔드포인트는 미리 설정되어 있습니다. | 💡 Only need to fill in API Key, endpoint is preset | 保留 |
| providerForm.thirdPartyApiKeyHint | 💡 只需填写 API Key，请求地址已预设 | 💡 API 키만 입력하면 됩니다. 엔드포인트는 미리 설정되어 있습니다. | 💡 Only need to fill in API Key, endpoint is preset | 保留 |
| providerForm.customApiKeyHint | 💡 自定义配置需手动填写所有必要字段 | 💡 맞춤 설정을 위해서는 모든 필수 필드를 수동으로 입력해야 합니다. | 💡 Custom configuration requires manually filling all necessary fields | 已修订 |
| providerForm.omoHint | 💡 OMO 配置管理 Agent 模型分配，兼容 oh-my-openagent.jsonc / oh-my-opencode.jsonc | 💡 OMO 설정은 에이전트 모델 할당을 관리하고 oh-my-openagent.jsonc 및 oh-my-opencode.jsonc를 모두 지원합니다. | 💡 OMO config manages Agent model assignments and supports both oh-my-openagent.jsonc and oh-my-opencode.jsonc | 已修订 |
| providerForm.officialHint | 💡 官方供应商使用浏览器登录，无需配置 API Key | 💡 공식 공급자는 브라우저 로그인을 사용하므로 API 키가 필요하지 않습니다. | 💡 Official provider uses browser login, no API Key needed | 已修订 |
| providerForm.providerKeyStatusLoading | 正在加载供应商标识状态，请稍后再试 | 공급자 식별자 상태가 아직 로드 중입니다. 잠시 후 다시 시도해 주세요. | Provider identifier status is still loading. Please try again shortly. | 已修订 |
| providerForm.getApiKey | 获取 API Key | API 키 가져오기 | Get API Key | 保留 |
| providerForm.partnerPromotion.kimi | Kimi 新用户首次成功充值，即可获赠充值金额 10% 的 API 额度，最高赠送 ¥1000。 | 신규 Kimi 사용자는 첫 충전 성공 금액의 10%를 보너스 API 크레딧으로 최대 1,000위안까지 돌려받습니다. | New Kimi users get 10% of their first successful top-up back as bonus API credit, up to CNY ¥1,000. | 保留 |
| providerForm.partnerPromotion.a6api | A6API 是一家 Token 聚合站，内置实时价格排行自动筛选全网最低价，丝滑稳定不卡顿，简易操作省去比价繁琐，注册获得体验金！ | A6API는 시장에서 자동으로 가장 낮은 가격을 선택하는 실시간 가격 리더보드가 내장된 토큰 집계 플랫폼입니다. 부드럽고 안정적이며 작동이 간편하며 더 이상 지루한 가격 비교가 필요하지 않습니다. 지금 등록하여 무료 평가판 크레딧을 받으세요! | A6API is a token aggregation platform with a built-in real-time price leaderboard that automatically picks the lowest price on the market. Smooth and stable, simple to operate, and no more tedious price comparisons. Register now to claim free trial credits! | 保留 |
| providerForm.partnerPromotion.sudocode | SudoCode 让 Claude Code 与 Claude Desktop 接入 Claude Opus 5，Codex 接入 GPT-5.6，一个 Key 统一使用。CC Switch 用户注册并加入 QQ 群 726213516，联系群主领取 ¥10 试用额度。 | SudoCode는 하나의 API 키로 Claude Code와 Claude Desktop에서는 Claude Opus 5를, Codex에서는 GPT-5.6을 사용할 수 있게 합니다. CC Switch 사용자는 가입 후 QQ 그룹 726213516에 참여하고 그룹 관리자에게 연락하면 체험 크레딧 10위안을 받을 수 있습니다. | With one SudoCode key, Claude Code and Claude Desktop use Claude Opus 5, while Codex uses GPT-5.6. Sign up, join QQ group 726213516, and contact the group owner to claim CNY ¥10 in trial credit. | 已修订 |
| providerForm.partnerPromotion.packycode | PackyCode 是 CC Switch 的官方合作伙伴，使用此链接注册并在充值时填写 "cc-switch" 优惠码，可以享受9折优惠 | PackyCode는 CC Switch의 공식 파트너입니다. 이 링크를 사용하여 등록하고 충전 시 "cc-switch" 프로모션 코드를 입력하면 10% 할인을 받을 수 있습니다. | PackyCode is an official partner of CC Switch. Register using this link and enter "cc-switch" promo code during recharge to get 10% off | 保留 |
| providerForm.partnerPromotion.apikeyfun | APIKEY.FUN 为 CC Switch 的用户提供了特别优惠，通过专属链接注册，可享受最高充值永久 95 折优惠。 | APIKEY.FUN은 CC Switch 사용자에게 특별 혜택을 제공합니다. 전용 링크로 가입하면 충전 시 최대 5% 할인을 영구적으로 받을 수 있습니다. | APIKEY.FUN offers a special deal for CC Switch users. Register through the exclusive link to enjoy up to permanent 5% off top-ups. | 已修订 |
| providerForm.partnerPromotion.apinebula | APINEBULA 为 CC Switch 用户提供特别优惠：使用专属链接注册并在充值时填写 "ccswitch" 优惠码，可享九折优惠。 | APINEBULA는 CC Switch 사용자에게 특별 할인을 제공합니다. 전용 링크로 가입하고 충전 시 "ccswitch" 할인 코드를 입력하면 10% 할인을 받을 수 있습니다. | APINEBULA offers CC Switch users a special discount: register using the link and enter the "ccswitch" promo code during your first top-up to get 10% off. | 已修订 |
| providerForm.partnerPromotion.patewayai | PatewayAI 为 CC Switch 的用户提供了特别福利，通过此链接注册可以获得3美元额度。 | PatewayAI는 CC Switch 사용자에게 특별한 혜택을 제공합니다. 이 링크를 통해 등록하시면 $3 크레딧을 받으실 수 있습니다. | PatewayAI offers special benefits for CC Switch users. Register via this link to receive $3 credit. | 保留 |
| providerForm.partnerPromotion.claudecn | ClaudeCN 是一家实体企业运营的企业级AI中转平台，支持企业采购流程，可对公打款、签约，服务合规有保障。 | ClaudeCN은 등록된 회사가 운영하는 엔터프라이즈급 AI 게이트웨이로, 기업 지불, 계약 및 규정 준수 보장을 통해 기업 조달 프로세스를 지원합니다. | ClaudeCN is an enterprise-grade AI gateway operated by a registered company, supporting enterprise procurement processes with corporate payments, contracts, and compliance guarantees. | 保留 |
| providerForm.partnerPromotion.runapi | RunAPI 为 CC Switch 的用户提供了特别福利，通过此链接注册，首次充值即可享受 9 折优惠。 | RunAPI는 CC Switch 사용자에게 특별한 혜택을 제공합니다. 이 링크를 통해 등록하고 첫 충전 시 10% 할인을 받으세요. | RunAPI offers special benefits for CC Switch users. Register via this link and enjoy 10% off your first top-up. | 保留 |
| providerForm.partnerPromotion.opencode_go | OpenCode Go 提供多款编程模型的订阅服务，可通过此链接查看套餐详情并订阅。 | OpenCode Go는 다양한 코딩 모델에 대한 구독 액세스를 제공합니다. 이 링크를 통해 요금제 세부정보를 확인하고 구독하세요. | OpenCode Go offers subscription access to a range of coding models. View plan details and subscribe via this link. | 保留 |
| providerForm.partnerPromotion.dmxapi | Claude Code 专属模型 3.4 折优惠进行中！ | Claude Code 독점 모델 66% OFF! | Claude Code exclusive model 66% OFF now! | 保留 |
| providerForm.partnerPromotion.cubence | Cubence 是 CC Switch 的官方合作伙伴，使用此链接注册并在充值时填写 "CCSWITCH" 优惠码，每次充值均可享受9折优惠 | Cubence는 CC Switch의 공식 파트너입니다. 이 링크로 가입하고 충전 시 프로모션 코드 ‘CCSWITCH’를 입력하면 매번 10% 할인을 받을 수 있습니다. | Cubence is an official partner of CC Switch. Register using this link and enter "CCSWITCH" promo code during recharge to get 10% off every top-up | 已修订 |
| providerForm.partnerPromotion.aigocode | AIGoCode 是 CC Switch 的官方合作伙伴，使用此链接注册首次充值时可以获得10%额度奖励！ | AIGoCode는 CC Switch의 공식 파트너입니다. 이 링크를 사용하여 등록하고 첫 번째 충전 시 10% 보너스 크레딧을 받으세요! | AIGoCode is an official partner of CC Switch. Register using this link and get 10% bonus credit on your first top-up! | 保留 |
| providerForm.partnerPromotion.rightcode | RightCode 是 CC Switch 的官方合作伙伴，使用此链接注册每次充值均可赠送5%额外额度！ | RightCode는 CC Switch의 공식 파트너입니다. 이 링크를 사용하여 등록하고 충전할 때마다 5% 보너스 크레딧을 받으세요! | RightCode is an official partner of CC Switch. Register using this link and get 5% bonus credit on every top-up! | 保留 |
| providerForm.partnerPromotion.aicodemirror | AICodeMirror 是 CC Switch 的官方合作伙伴，使用此链接注册可享受8折优惠！ | AICodeMirror는 CC Switch의 공식 파트너입니다. 이 링크를 통해 등록하시면 20% 할인을 받으실 수 있습니다! | AICodeMirror is an official partner of CC Switch. Register using this link to get 20% off! | 保留 |
| providerForm.partnerPromotion.aicoding | AI Coding 为 CC Switch 的用户提供了特殊优惠，首次充值可以享受 9 折优惠！ | AI Coding은 CC Switch 사용자에게 독점 할인을 제공합니다. 첫 충전 시 10% 할인이 제공됩니다! | AI Coding offers an exclusive discount for CC Switch users — 10% off your first top-up! | 保留 |
| providerForm.partnerPromotion.crazyrouter | CrazyRouter 为 CC Switch 的用户提供了特殊优惠，首次充值赠予 30% 额外额度！ | CrazyRouter는 CC Switch 사용자에게 독점적인 보너스를 제공합니다 — 첫 번째 충전 시 30% 추가 크레딧! | CrazyRouter offers an exclusive bonus for CC Switch users — 30% extra credit on your first top-up! | 保留 |
| providerForm.partnerPromotion.sssaicode | SSAI Code 为 CC Switch 的用户提供了特殊优惠，每次充值赠予额外 $10 额度！ | SSAI Code는 CC Switch 사용자에게 특별 혜택을 제공합니다. 충전할 때마다 추가 크레딧 10달러를 드립니다! | SSAI Code offers an exclusive bonus for CC Switch users — $10 extra credit on every top-up! | 已修订 |
| providerForm.partnerPromotion.siliconflow | 硅基流动是 CC Switch 的官方合作伙伴 | SiliconFlow는 CC Switch의 공식 파트너입니다. | SiliconFlow is an official partner of CC Switch | 保留 |
| providerForm.partnerPromotion.ucloud | 优云智算为CC Switch 的用户提供了特殊优惠，通过此链接注册，可以获得五元平台体验金！ | Compshare는 CC Switch 사용자에게 특별 혜택을 제공합니다. 이 링크로 가입하면 플랫폼 체험 크레딧 5위안을 받을 수 있습니다! | Compshare offers an exclusive bonus for CC Switch users — register via this link to get ¥5 platform trial credit! | 已修订 |
| providerForm.partnerPromotion.micu | Micu 是 CC Switch 的官方合作伙伴 | Micu는 CC Switch의 공식 파트너입니다 | Micu is an official partner of CC Switch | 保留 |
| providerForm.partnerPromotion.shengsuanyun | 胜算云为 CC Switch 的用户提供了特别福利，使用此链接注册的新用户可获 10 元模力及首充 10% 赠送！ | Shengsuanyun은 CC Switch 사용자에게 특별 혜택을 제공합니다. 이 링크로 가입하는 신규 사용자는 무료 크레딧 10위안과 첫 충전 금액의 10%를 추가로 받습니다! | Shengsuanyun offers exclusive benefits for CC Switch users. New users who register via this link get ¥10 free credits and 10% bonus on first top-up! | 已修订 |
| providerForm.partnerPromotion.doubaoseed | 豆包大模型为 CC Switch 的用户提供了专属福利：通过此链接注册即可获取豆包全系列文本模型 50万tokens推理额度以及Seedance2.0的500万tokens免费额度 | DouBao는 CC Switch 사용자에게 독점적인 혜택을 제공합니다. 이 링크를 통해 등록하면 모든 DouBao 텍스트 모델에 대한 추론 크레딧 500K 토큰과 무료 Seedance 2.0 크레딧 500만 토큰을 받을 수 있습니다. | DouBao offers exclusive benefits for CC Switch users: register via this link to get 500K tokens of inference credits for all DouBao text models and 5M tokens of free Seedance 2.0 credits. | 保留 |
| providerForm.partnerPromotion.volcengine_agentplan | 火山方舟 Agent Plan 为 CC Switch 的用户提供了专属福利：通过此链接订阅方舟 Agent Plan，新客户首两个月享 2.5 折优惠，再用专属邀请码 6J6FV5N2 领取奖励叠加 9.5 折，低至 9.4 元/月！ | Volcengine Ark Agent Plan은 CC Switch 사용자에게 특별 혜택을 제공합니다. 이 링크로 구독하는 신규 고객은 첫 두 달 동안 75% 할인을 받고, 전용 초대 코드 6J6FV5N2로 추가 5% 할인을 적용하면 월 최저 9.4위안에 이용할 수 있습니다! | Volcengine Ark Agent Plan offers exclusive benefits for CC Switch users: subscribe via this link and new customers get 75% off for the first two months, plus an extra 5% off with the exclusive invite code 6J6FV5N2 — as low as ¥9.4/month! | 已修订 |
| providerForm.partnerPromotion.volcengine_codingplan | 火山方舟 Coding Plan 为 CC Switch 的用户提供了专属福利：通过此链接订阅方舟 Coding Plan，新客户首两个月享 2.5 折优惠，再用专属邀请码 6J6FV5N2 领取奖励叠加 9.5 折，低至 9.4 元/月！ | Volcengine Ark Coding Plan은 CC Switch 사용자에게 특별 혜택을 제공합니다. 이 링크로 구독하는 신규 고객은 첫 두 달 동안 75% 할인을 받고, 전용 초대 코드 6J6FV5N2로 추가 5% 할인을 적용하면 월 최저 9.4위안에 이용할 수 있습니다! | Volcengine Ark Coding Plan offers exclusive benefits for CC Switch users: subscribe via this link and new customers get 75% off for the first two months, plus an extra 5% off with the exclusive invite code 6J6FV5N2 — as low as ¥9.4/month! | 已修订 |
| providerForm.partnerPromotion.byteplus | 通过此链接注册即可获取每个模型50万tokens的免费推理额度。 | 이 링크를 통해 등록하면 모델당 500,000개의 무료 추론 할당량 토큰을 받을 수 있습니다. | Register via this link to get 500,000 tokens of free inference quota per model. | 保留 |
| providerForm.partnerPromotion.ccsub | CCSub 是稳定、实惠的 AI API 中转平台，Claude Code 官方订阅的超强平替，一个 Key 覆盖全部模型，价格约为官方 1/3。 | CCSub는 안정적이고 합리적인 가격의 AI API 중계 플랫폼으로, Claude Code 공식 구독을 대체할 수 있습니다. 키 하나로 모든 모델을 이용하며 가격은 공식 가격의 약 3분의 1입니다. | CCSub is a stable, affordable AI API relay — a drop-in replacement for Claude.ai & OpenAI subscriptions, with one key for all models at ~30% of direct API cost. | 已修订 |
| providerForm.partnerPromotion.subrouter | SubRouter 是中转站聚合平台，一个 Key 可接入多个模型与供应商。 | SubRouter는 하나의 키가 여러 모델과 공급자에 액세스할 수 있게 해주는 AI 릴레이 수집기입니다. | SubRouter is an AI relay aggregator that lets one key access multiple models and providers. | 已修订 |
| providerForm.partnerPromotion.qiniu | 七牛云是多协议 AI 中转平台，一个 Key 即可调用原生 Claude、GPT、Gemini 模型，兼容 Anthropic、OpenAI、Gemini 多种接口。 | Qiniu Cloud는 다중 프로토콜 AI 릴레이입니다. 기본 Claude, GPT 및 Gemini 모델을 위한 하나의 키이며 Anthropic, OpenAI 및 Gemini API가 모두 지원됩니다. | Qiniu Cloud is a multi-protocol AI relay: one key for native Claude, GPT, and Gemini models, with the Anthropic, OpenAI, and Gemini APIs all supported. | 保留 |
| providerForm.partnerPromotion.haoai | hao.ai 是面向开发者与团队的高速、稳定大模型统一 API 网关：一个 Key 即可接入 GPT、Claude、Grok 等主流模型，兼容 OpenAI、Anthropic 协议，提供模型路由、故障回退与完整调用日志，价格低至官方参考价的 1.5 折。CC Switch 用户通过此链接注册，首单可享 5% 赠送额度！ | hao.ai는 개발자와 팀을 위한 빠르고 안정적인 통합 LLM API 게이트웨이입니다. 하나의 키는 모델 라우팅, 장애 조치 및 전체 요청 로그를 통해 OpenAI 및 Anthropic 호환 API를 통해 GPT, Claude, Grok 및 기타 주요 모델에 도달하며 공식 참조 요금의 15%만큼 낮은 가격으로 제공됩니다. 이 링크를 통해 등록한 CC Switch 사용자는 첫 주문 시 5% 보너스 크레딧을 받습니다! | hao.ai is a fast, stable unified LLM API gateway for developers and teams: one key reaches GPT, Claude, Grok, and other leading models over OpenAI- and Anthropic-compatible APIs, with model routing, failover, and full request logs, at prices as low as 15% of official reference rates. CC Switch users who register via this link get 5% bonus credit on their first order! | 保留 |
| providerForm.partnerPromotion.fenno | Fenno.ai 是稳定高效的 API 中转服务商，可接入多种主流模型。CC Switch 用户专属福利：通过此链接订阅 1.99 刀 /50 刀额度的 Trial 计划，有效期 7 天！ | Fenno.ai는 다양한 주류 모델에 대한 액세스를 제공하는 안정적이고 효율적인 API 릴레이입니다. 독점 CC Switch 제안: 이 링크를 통해 7일 동안 유효한 $50 크레딧 상당의 $1.99 평가판 플랜을 구독하세요! | Fenno.ai is a stable, efficient API relay giving you access to a wide range of mainstream models. Exclusive CC Switch offer: subscribe via this link to the $1.99 Trial Plan worth $50 in credits, valid for 7 days! | 保留 |
| providerForm.partnerPromotion.teamorouter | TeamoRouter 是企业级 Agentic LLM 网关，价格最高可达 90% 折扣。为 CC Switch 的用户提供了特别福利：新用户通过此链接注册，首次充值享 10% 折扣！ | TeamoRouter는 최대 90% 할인된 가격으로 제공되는 엔터프라이즈급 Agentic LLM 게이트웨이입니다. CC Switch 사용자에게 독점적인 혜택을 제공합니다. 이 링크를 통해 신규 사용자로 등록하면 첫 충전 시 10% 할인을 받을 수 있습니다! | TeamoRouter is an enterprise-grade Agentic LLM gateway with pricing up to 90% off. It offers exclusive benefits for CC Switch users: register via this link as a new user for 10% off your first top-up! | 保留 |
| providerForm.partnerPromotion.ppio | PPIO 是国内领先的独立 Agentic Cloud 服务商，一个 API Key 调用全部旗舰开源模型。通过此链接注册并完成实名认证，即可获得 ¥10 代金券。 | PPIO는 중국의 선도적인 독립 Agentic Cloud 공급자로, API 키 하나로 모든 대표 오픈 소스 모델을 호출할 수 있습니다. 이 링크로 가입하고 실명 인증을 완료하면 10위안 이용권을 받을 수 있습니다. | PPIO is a leading independent Agentic Cloud provider in China, serving every flagship open-source model through a single API key. Register via this link and complete identity verification to receive a ¥10 credit voucher. | 已修订 |
| providerForm.partnerPromotion.xycai | XycAi 企业级 Token 工厂：200+ 全球模型一键接入，SLA 自动赔付，异常缓存 100% 退还！ | XycAi는 엔터프라이즈급 토큰 팩토리입니다. 200개 이상의 글로벌 모델에 대한 원클릭 액세스, 자동 SLA 보상, 비정상적인 캐시 요금에 대한 100% 환불이 가능합니다! | XycAi is an enterprise-grade token factory: one-click access to 200+ global models, automatic SLA compensation, and 100% refunds for abnormal cache charges! | 保留 |
| providerForm.partnerPromotion.9527code | 9527 CODE 是企业级满血 AI 中转平台，为 Claude Code、Codex 等主流模型提供高速稳定的中转服务。持续运营一年，服务稳定性达 99.9%，提供 7×24 小时人工技术支持。新人福利联系客服赠送体验额度，拉新返现无上限！ | 9527 CODE는 Claude Code, Codex 등 주요 모델을 빠르고 안정적으로 연결하는 기업용 AI 중계 플랫폼입니다. 1년간 지속 운영하며 99.9% 서비스 안정성과 연중무휴 상담원 기술 지원을 제공합니다. 신규 사용자는 고객 지원에 체험 크레딧을 요청할 수 있으며, 신규 사용자 초대 캐시백에는 상한이 없습니다! | 9527 CODE is an enterprise-grade, full-capability AI relay platform delivering fast, stable relay for Claude Code, Codex and other mainstream models. One year of continuous operation, 99.9% service stability, and 7×24 human technical support. New users can contact support for trial credit, with unlimited referral cashback! | 已修订 |
| providerForm.partnerPromotion.soleapi | SoleAPI 是面向开发者与企业的 AI 模型网关，一个 API Key 直达 Claude、GPT、Gemini 等 30+ 主流模型，原生兼容 OpenAI 与 Anthropic 协议，智能选路毫秒级故障切换，可用性 99.99%，7×24 技术支持。通过专属链接注册即送体验额度，邀请好友充值持续返现！ | SoleAPI는 개발자와 기업을 위한 AI 모델 게이트웨이입니다. 하나의 API 키는 Claude, GPT, Gemini를 포함한 30개 이상의 주요 모델에 연결되며 기본적으로 OpenAI 및 Anthropic 프로토콜과 호환되며 실시간 스마트 라우팅, 밀리초 장애 조치, 99.99% 가용성 및 연중무휴 지원을 제공합니다. 무료 평가판 크레딧을 받으려면 추천 링크를 통해 가입하고 충전한 친구를 초대하기 위한 지속적인 캐시백을 받으세요! | SoleAPI is an AI model gateway for developers and enterprises: one API key reaches 30+ leading models including Claude, GPT and Gemini, natively compatible with the OpenAI and Anthropic protocols, with real-time smart routing, millisecond failover, 99.99% availability and 24/7 support. Sign up via the referral link for free trial credits and ongoing cashback for inviting friends who top up! | 保留 |
| providerForm.partnerPromotion.fluxa | FluxA 与百度智能云联合推出 AgenticPlan，让 AI Agent 能自主购买、管理和使用模型、API 与工具。内含百度千帆 TokenPlan，低至 6 折，可使用 DeepSeek V4、GLM 5.2、Kimi 等旗舰模型，并获赠 FluxA AgentMarket API 调用额度，解锁搜索、数据抓取、社交媒体、金融、加密、生图、视频等 13000+ 付费 API。 | FluxA와 Baidu AI Cloud는 AI 에이전트가 모델, API 및 도구를 스스로 구매, 관리 및 사용할 수 있도록 AgenticPlan을 공동 출시했습니다. 여기에는 DeepSeek V4, GLM 5.2 및 Kimi와 같은 주력 모델에 대해 최대 40% 할인된 Baidu Qianfan TokenPlan과 검색, 데이터 스크래핑, 소셜 미디어, 금융, 암호화폐, 이미지 생성 및 비디오를 위한 13,000개 이상의 유료 API를 잠금 해제하는 보너스 FluxA AgentMarket API 크레딧이 포함됩니다. | FluxA and Baidu AI Cloud jointly launched AgenticPlan, letting AI agents buy, manage and use models, APIs and tools on their own. It includes Baidu Qianfan TokenPlan at up to 40% off with flagship models such as DeepSeek V4, GLM 5.2 and Kimi, plus bonus FluxA AgentMarket API credits that unlock 13,000+ paid APIs for search, data scraping, social media, finance, crypto, image generation and video. | 保留 |
| providerForm.partnerPromotion.88api | 88API 是由香港企业运营的一站式多模型 API 平台，通过统一接口接入文本、图片、语音和视频模型，支持国际主流付款方式，可提供发票，提供企业级稳定服务。通过专属链接注册可获取专属赠送额度！ | 88API는 홍콩 회사가 운영하는 원스톱 다중 모델 API 플랫폼으로, 텍스트, 이미지, 음성 및 비디오 모델에 대한 통합 액세스를 제공합니다. 주요 국제 결제 수단을 수용하고 송장 발행이 가능하며 기업 수준의 안정적인 서비스를 제공합니다. 보너스 크레딧을 받으시려면 전용 링크를 통해 가입하세요! | 88API is a one-stop multi-model API platform run by a Hong Kong company, giving unified access to text, image, speech and video models. It accepts major international payment methods, can issue invoices and provides enterprise-grade stable service. Sign up through the exclusive link to receive bonus credits! | 保留 |
| providerForm.partnerPromotion.modelflare | Modelflare 是稳定、低成本的 AI 模型网关，一个 Key 即可调用 GPT、Claude、Gemini、Grok 等主流模型。CC Switch 用户专享福利：首次充值使用优惠码 "CCSWITCH" 可享 9 折优惠！ | Modelflare는 안정적이고 저렴한 AI 모델 게이트웨이입니다. 하나의 키가 GPT, Claude, Gemini, Grok 및 기타 주요 모델에 도달합니다. CC Switch 사용자 전용: 첫 번째 충전 시 "CCSWITCH" 코드를 사용하면 10% 할인을 받을 수 있습니다! | Modelflare is a stable, lower-cost AI model gateway: one key reaches GPT, Claude, Gemini, Grok, and other leading models. Exclusive for CC Switch users: use the code "CCSWITCH" on your first top-up for 10% off! | 保留 |
| providerForm.partnerPromotion.everyapi | EveryAPI 自带桌面客户端，Claude Code、Codex、Cursor 等 20 多个工具一键自动配置；一把密钥直接调用 Claude、GPT、DeepSeek、GLM、MiniMax、Kimi、豆包，换模型不用改配置。注册即送 14 元额度，GPT 低至 1.5 折；CC Switch 用户专享：首充时使用折扣码 "ccswitch" 享 20% 优惠，不限时！ | EveryAPI는 Claude Code, Codex, Cursor 등 20개 이상의 도구를 한 번의 클릭으로 자동 설정하는 데스크톱 클라이언트를 제공합니다. 키 하나로 Claude, GPT, DeepSeek, GLM, MiniMax, Kimi, Doubao를 호출하며 모델을 바꿀 때 설정을 수정할 필요가 없습니다. 가입 시 무료 크레딧 14위안을 받고 GPT 모델을 공식 가격의 최저 15%에 이용할 수 있습니다. CC Switch 사용자는 첫 충전 시 코드 ‘ccswitch’로 20% 할인을 받을 수 있으며, 이 혜택에는 기한이 없습니다! | EveryAPI ships its own desktop client that auto-configures Claude Code, Codex, Cursor, and 20+ other tools in one click; one key reaches Claude, GPT, DeepSeek, GLM, MiniMax, Kimi, and Doubao, so switching models needs no config changes. Get ¥14 in free credit on sign-up, with GPT models from just 15% of the official price. Exclusive for CC Switch users: use the code "ccswitch" on your first top-up for 20% off, with no expiry! | 已修订 |
| providerForm.partnerPromotion.alltokens | AllTokens 秉持「稳定为基，真实为本」，致力于让每一次 AI 调用都稳定、真实、值得托付：服务可靠、计费透明，一个平台接入 GPT、Claude、Gemini、Grok、DeepSeek、GLM、Kimi 等主流模型，按量计费、支持配额上限。注册即送 1 美元体验金！ | AllTokens는 모든 AI 호출을 안정적이고 진실되고 신뢰할 수 있게 만드는 것을 목표로 안정성과 정직성을 기반으로 구축되었습니다. 신뢰할 수 있는 서비스, 투명한 청구, GPT, Claude, Gemini, Grok, DeepSeek, GLM, Kimi 및 기타 주요 모델을 위한 단일 플랫폼과 종량제 가격 책정 및 지출 한도가 적용됩니다. 가입 시 무료 평가판 크레딧 1달러를 받으세요! | AllTokens is built on stability and honesty, aiming to make every AI call stable, genuine, and trustworthy: reliable service, transparent billing, and one platform for GPT, Claude, Gemini, Grok, DeepSeek, GLM, Kimi, and other leading models, with pay-as-you-go pricing and spending caps. Get $1 in free trial credit when you sign up! | 保留 |
| providerForm.partnerPromotion.alltokens_si | AllTokens SI 秉持「稳定为基，真实为本」，是专为企业打造的 AI Token 中转与团队协作平台：成员、密钥、用量与余额统一纳入企业控制台，以清晰的权限与额度配置，让团队协作有据可查、安心可控。 | AllTokens SI는 안정성과 정직성을 바탕으로 구축되었으며 기업용 AI 토큰 릴레이 및 팀 협업 플랫폼입니다. 구성원, 키, 사용량 및 잔액은 모두 하나의 회사 콘솔에 있으며 명확한 권한과 지출 한도를 통해 팀 사용량을 추적하고 제어할 수 있습니다. | AllTokens SI is built on stability and honesty: an enterprise AI token relay and team collaboration platform. Members, keys, usage, and balance all live in one company console, and clear permissions and spending limits keep team usage traceable and under control. | 保留 |
| providerForm.partnerPromotion.openmodel | OpenModel 为 Codex 和 Claude Code 提供客户端专属折扣，所支持的模型通过 Codex 调用最高优惠 90%、通过 Claude Code 调用最高优惠 60%。CC Switch 用户通过此链接注册并使用优惠码 "cc-switch"，即可享受首次充值九折优惠！ | OpenModel은 지원되는 모델 전반에 걸쳐 Codex의 경우 최대 90%, Claude Code의 경우 최대 60%의 클라이언트별 할인을 제공합니다. 이 링크를 통해 등록하고 프로모션 코드 "cc-switch"를 사용하는 CC Switch 사용자는 첫 충전 시 10% 할인을 받습니다! | OpenModel offers client-specific discounts of up to 90% for Codex and 60% for Claude Code across supported models. CC Switch users who register via this link and use promo code "cc-switch" get 10% off their first top-up! | 保留 |
| providerForm.partnerPromotion.grooroute | GrooRoute Pro 是可靠流畅的 AI API 中转服务平台，接入 OpenAI、Claude、DeepSeek 等主流大模型，支持按量计费与订阅套餐。CC Switch 用户通过此链接注册即可获得免费 5 元体验额度！ | GrooRoute Pro는 OpenAI, Claude, DeepSeek 등 주요 모델을 지원하는 안정적인 AI API 중계 플랫폼으로, 종량제와 구독 요금제를 제공합니다. CC Switch 사용자는 이 링크로 가입하면 체험 크레딧 5위안을 무료로 받을 수 있습니다! | GrooRoute Pro is a reliable AI API relay with access to OpenAI, Claude, DeepSeek, and other mainstream models, offering pay-as-you-go and subscription plans. CC Switch users get ¥5 in free trial credit by registering via this link! | 已修订 |
| providerForm.partnerPromotion.dit | DIT.ai 是面向多供应商低价路由的 AI Token 交易市场：一个 OpenAI 兼容 API 即可调用 GPT、Claude、Gemini、DeepSeek、Grok、Llama 等 50 多个主流模型，160 多条线路实时竞价，价格通常比官方低 30–70%。CC Switch 用户通过此链接注册并使用优惠码 "ccswitch"，可领取 5 美元新人券！ | DIT.ai는 저비용 다중 공급자 라우팅을 위한 AI 토큰 교환입니다. 하나의 OpenAI 호환 API는 GPT, Claude, Gemini, DeepSeek, Grok 및 Llama를 포함한 50개 이상의 주요 모델에 도달하며 공급자는 160개 이상의 경로에서 경쟁하며 일반적으로 공식 가격보다 30~70% 저렴합니다. CC Switch 사용자는 이 링크를 통해 등록하고 프로모션 코드 "ccswitch"를 사용하여 $5 환영 쿠폰을 받을 수 있습니다! | DIT.ai is an AI token exchange for lower-cost multi-provider routing: one OpenAI-compatible API reaches 50+ leading models including GPT, Claude, Gemini, DeepSeek, Grok, and Llama, with providers competing across 160+ routes, typically 30–70% below official pricing. CC Switch users can register via this link and use promo code "ccswitch" to claim a $5 welcome coupon! | 已修订 |
| providerForm.partnerPromotion.buytoken | BuyToken 提供 Claude Code、Codex、DeepSeek 等各类中转服务，支持企业级并发、可极速开票，专注做稳定长久站。CC Switch 用户通过此链接注册可得 3 元体验额度，首充享 9 折！ | BuyToken은 Claude Code, Codex, DeepSeek 등의 중계 서비스를 제공하며 기업용 동시 처리와 빠른 세금계산서 발행을 지원합니다. 안정적이고 장기적인 서비스 운영을 지향합니다. CC Switch 사용자는 이 링크로 가입하면 체험 크레딧 3위안과 첫 충전 10% 할인을 받을 수 있습니다! | BuyToken offers relay access for Claude Code, Codex, DeepSeek, and more, with enterprise-grade concurrency and fast invoicing, built to be a stable, long-running service. CC Switch users who register via this link get ¥3 in trial credit and 10% off their first top-up! | 已修订 |
| providerForm.partnerPromotion.vapi | V-API 是三年老品牌，为个人、开发者和企业提供稳定、快速、安全的高品质大语言模型 API 服务，支持合同签约、正规开票（普票 / 专票）。CC Switch 用户通过此链接注册，首单立减 2 元并享 9 折优惠！ | V-API는 3년간 운영해 온 브랜드로, 개인·개발자·기업에 안정적이고 빠르며 안전한 LLM API 서비스를 제공합니다. 계약 체결과 중국의 정식 세금계산서 발행(일반/전용 부가가치세)을 지원합니다. CC Switch 사용자는 이 링크로 가입하면 첫 주문에서 2위안 즉시 할인과 10% 할인을 받을 수 있습니다! | V-API is a three-year-old brand offering stable, fast, and secure high-quality LLM API services for individuals, developers, and businesses, with formal contracts and official invoices (general / special VAT). CC Switch users who register via this link get ¥2 off and 10% off their first order! | 已修订 |
| providerForm.presets.ucloud | 优云智算 | Compshare | Compshare | 已修订 |
| providerForm.presets.ucloudCoding | 优云智算Coding Plan | Compshare Coding Plan | Compshare Coding Plan | 已修订 |
| providerForm.presets.shengsuanyun | 胜算云 | Shengsuanyun | Shengsuanyun | 已修订 |
| providerForm.presets.qiniu | 七牛云 | Qiniu | Qiniu | 已修订 |
| providerForm.presets.doubaoseed | 火山 豆包AI | Volcengine Doubao | Volcengine Doubao | 已修订 |
| providerForm.presets.openrouter | OpenRouter | OpenRouter | OpenRouter | 已修订 |
| providerForm.presets.deepseek | DeepSeek | DeepSeek | DeepSeek | 保留 |
| providerForm.presets.together | Together AI | Together AI | Together AI | 已修订 |
| providerForm.presets.tuzi | 兔子API | Tu-zi | Tu-zi | 已修订 |
| providerForm.presets.yylx | 鱼鱼连线 | YYLX | YYLX | 保留 |
| providerForm.presets.tokenfactory | 词元工厂 | TokenFactory | TokenFactory | 已修订 |
| providerForm.parameterConfig | 参数配置 - {{name}} * | 매개변수 설정 - {{name}} * | Parameter Config - {{name}} * | 已修订 |
| providerForm.mainModel | 主模型 (可选) | 주요 모델(선택 사항) | Main Model (optional) | 保留 |
| providerForm.mainModelPlaceholder | 例如: GLM-4.6 | 예: GLM-4.6 | e.g., GLM-4.6 | 保留 |
| providerForm.fastModel | 快速模型 (可选) | 빠른 모델(선택 사항) | Fast Model (optional) | 保留 |
| providerForm.fastModelPlaceholder | 例如: GLM-4.5-Air | 예: GLM-4.5-Air | e.g., GLM-4.5-Air | 保留 |
| providerForm.modelHint | 💡 留空将使用供应商的默认模型 | 💡 공급자의 기본 모델을 사용하려면 비워 두세요. | 💡 Leave blank to use provider's default model | 已修订 |
| providerForm.apiHint | 💡 填写兼容 Claude API 的服务端点地址，不要以斜杠结尾 | 💡 Claude API 호환 서비스의 엔드포인트를 입력하세요. 끝에 슬래시를 붙이지 마세요 | 💡 Fill in Claude API compatible service endpoint, avoid trailing slash | 已修订 |
| providerForm.apiHintOAI | 💡 填写兼容 OpenAI Chat Completions 的服务端点地址，不要以斜杠结尾 | 💡 OpenAI Chat Completions 호환 서비스의 엔드포인트를 입력하세요. 끝에 슬래시를 붙이지 마세요 | 💡 Fill in OpenAI Chat Completions compatible service endpoint, avoid trailing slash | 已修订 |
| providerForm.apiHintGeminiNative | 💡 建议填写 Gemini Native 的 base URL，例如 https://generativelanguage.googleapis.com 或 https://generativelanguage.googleapis.com/v1beta；代理会自动补全 models/*:generateContent | 💡 https://generativelanguage.googleapis.com 또는 https://generativelanguage.googleapis.com/v1beta 같은 Gemini Native 기본 URL을 권장합니다. 프록시가 models/*:generateContent를 자동으로 추가합니다 | 💡 Prefer a Gemini Native base URL such as https://generativelanguage.googleapis.com or https://generativelanguage.googleapis.com/v1beta; the proxy will append models/*:generateContent automatically | 已修订 |
| providerForm.codexApiHint | 💡 填写兼容 OpenAI Response 格式的服务端点地址 | 💡 OpenAI Responses 형식과 호환되는 서비스 엔드포인트를 입력하세요 | 💡 Fill in service endpoint compatible with OpenAI Response format | 已修订 |
| providerForm.fillSupplierName | 请填写供应商名称 | 공급자 이름을 입력하세요. | Please fill in provider name | 已修订 |
| providerForm.fillConfigContent | 请填写配置内容 | 설정 내용을 입력해 주세요. | Please fill in configuration content | 已修订 |
| providerForm.fillParameter | 请填写 {{label}} | {{label}}을(를) 입력하세요. | Please fill in {{label}} | 已修订 |
| providerForm.fillTemplateValue | 请填写 {{label}} | {{label}}을(를) 입력하세요. | Please fill in {{label}} | 已修订 |
| providerForm.endpointRequired | 非官方供应商请填写 API 端点 | 비공식 공급자에는 API 엔드포인트가 필요합니다. | API endpoint is required for non-official providers | 已修订 |
| providerForm.apiKeyRequired | 非官方供应商请填写 API Key | 비공식 공급자에는 API 키가 필요합니다. | API Key is required for non-official providers | 已修订 |
| providerForm.softValidation.title | 配置存在以下问题 | 설정에 다음과 같은 문제가 있습니다. | Configuration has the following issues | 已修订 |
| providerForm.softValidation.hint | 仍要保存吗？保存后切换此供应商时可能失败，可以之后再补全。 | 저장하시겠습니까? 이 공급자로 전환하는 데 실패할 수 있습니다. 나중에 입력할 수 있습니다. | Save anyway? Switching to this provider may fail; you can fill these in later. | 已修订 |
| providerForm.softValidation.saveAnyway | 仍要保存 | 무시하고 저장 | Save anyway | 保留 |
| providerForm.configJsonError | 配置JSON格式错误，请检查语法 | 설정 JSON 형식 오류입니다. 구문을 확인하세요. | Config JSON format error, please check syntax | 已修订 |
| providerForm.authJsonRequired | auth.json 必须是 JSON 对象 | auth.json은 JSON 객체여야 합니다. | auth.json must be a JSON object | 保留 |
| providerForm.authJsonError | auth.json 格式错误，请检查JSON语法 | auth.json 형식 오류입니다. JSON 구문을 확인하세요. | auth.json format error, please check JSON syntax | 保留 |
| providerForm.fillAuthJson | 请填写 auth.json 配置 | auth.json 설정을 입력하세요. | Please fill in auth.json configuration | 已修订 |
| providerForm.fillApiKey | 请填写 OPENAI_API_KEY | OPENAI_API_KEY를 입력하세요. | Please fill in OPENAI_API_KEY | 保留 |
| providerForm.visitWebsite | 访问 {{url}} | {{url}} 방문 | Visit {{url}} | 保留 |
| providerForm.anthropicModel | 主模型 | 주요 모델 | Main Model | 保留 |
| providerForm.anthropicSmallFastModel | 快速模型 | 빠른 모델 | Fast Model | 保留 |
| providerForm.apiFormat | 上游格式 | 업스트림 형식 | Upstream Format | 保留 |
| providerForm.customUserAgent | 自定义 User-Agent | 사용자 지정 User-Agent | Custom User-Agent | 已修订 |
| providerForm.customUserAgentInvalid | User-Agent 不能包含控制字符（如换行符），否则将被忽略。 | User-Agent에 줄 바꿈 등의 제어 문자가 있으면 무시됩니다. | User-Agent must not contain control characters (e.g. line breaks); otherwise it will be ignored. | 已修订 |
| providerForm.customUserAgentPresets | 预设 | 프리셋 | Presets | 保留 |
| providerForm.localProxyRequestOverrides | 本地代理请求覆盖 | 로컬 프록시 요청 재정의 | Local proxy request overrides | 保留 |
| providerForm.localProxyRequestOverridesInvalid | 本地代理请求覆盖格式错误：{{error}} | 로컬 프록시 요청 재정의 형식 오류: {{error}} | Local proxy request overrides format error: {{error}} | 保留 |
| providerForm.localProxyHeaderOverrides | Header 覆盖 | 헤더 재정의 | Header overrides | 保留 |
| providerForm.localProxyHeaderOverridesInvalidDetail | Header 覆盖格式错误：{{error}} | 헤더 재정의 형식 오류: {{error}} | Header overrides format error: {{error}} | 保留 |
| providerForm.localProxyBodyOverrides | Body 覆盖 | 본문 재정의 | Body overrides | 已修订 |
| providerForm.localProxyBodyOverridesInvalidDetail | Body 覆盖格式错误：{{error}} | 본문 재정의 형식 오류: {{error}} | Body overrides format error: {{error}} | 保留 |
| providerForm.fullUrlLabel | 完整 URL | 전체 URL | Full URL | 保留 |
| providerForm.fullUrlHelp | 端点路径不标准的网关才需要：地址填完整请求地址，路由原样使用、不再拼接路径。直连下用不了。 | 엔드포인트 경로가 비표준인 게이트웨이에만 사용하세요. 전체 요청 URL을 입력하면 경로를 덧붙이지 않고 그대로 라우팅에 사용합니다. 직접 연결 모드에서는 사용할 수 없습니다. | Only for gateways with a non-standard endpoint path: enter the full request URL and routing uses it as is, without appending a path. Not usable in direct mode. | 已修订 |
| providerForm.fullUrlHelpGeminiNative | Gemini Native 下：标准 Gemini 地址按模型自动规范化，自定义中转的完整地址原样使用、只补查询参数。直连下用不了。 | Gemini Native에서는 표준 Gemini URL을 모델에 맞게 정규화합니다. 사용자 지정 중계 서비스의 전체 URL은 그대로 사용하며 쿼리 매개변수만 추가합니다. 직접 연결 모드에서는 사용할 수 없습니다. | With Gemini Native, standard Gemini URLs are normalized per model, and a custom relay's full URL is used as is with only query parameters added. Not usable in direct mode. | 已修订 |
| providerForm.apiFormatAnthropic | Anthropic Messages (原生) | Anthropic Messages (네이티브) | Anthropic Messages (Native) | 已修订 |
| providerForm.apiFormatOpenAIChat | OpenAI Chat Completions (需开启路由) | OpenAI Chat Completions (라우팅 필요) | OpenAI Chat Completions (Requires routing) | 已修订 |
| providerForm.apiFormatOpenAIResponses | OpenAI Responses API (需开启路由) | OpenAI Responses API (라우팅 필요) | OpenAI Responses API (Requires routing) | 已修订 |
| providerForm.apiFormatGeminiNative | Gemini Native generateContent (需开启路由) | Gemini Native generateContent (라우팅 필요) | Gemini Native generateContent (Requires routing) | 已修订 |
| providerForm.codexApiFormatResponses | OpenAI Responses API (原生) | OpenAI Responses API (네이티브) | OpenAI Responses API (Native) | 已修订 |
| providerForm.codexApiFormatOpenAIChat | OpenAI Chat Completions (需开启路由) | OpenAI Chat Completions (라우팅 필요) | OpenAI Chat Completions (Requires routing) | 已修订 |
| providerForm.codexApiFormatHint | 选择供应商真实支持的 Codex API 格式；配置仍保持 Responses 以兼容新版 Codex，Chat Completions 会通过本地路由自动转换。 | 이 공급자가 실제로 지원하는 Codex API 형식을 선택하세요. 최신 Codex와 호환되도록 설정에는 Responses를 유지하며, Chat Completions는 로컬 라우팅에서 변환합니다. | Select the Codex API format actually supported by this provider; the config stays on Responses for newer Codex versions, while Chat Completions is converted through local routing. | 已修订 |
| providerForm.authField | 认证字段 | 인증 필드 | Auth Field | 保留 |
| providerForm.authFieldAuthToken | ANTHROPIC_AUTH_TOKEN（默认） | ANTHROPIC_AUTH_TOKEN(기본값) | ANTHROPIC_AUTH_TOKEN (Default) | 保留 |
| providerForm.authFieldApiKey | ANTHROPIC_API_KEY | ANTHROPIC_API_KEY | ANTHROPIC_API_KEY | 保留 |
| providerForm.authFieldHint | 直连时是写进 settings.json 的变量名；经过路由时，AUTH_TOKEN 以 Bearer、API_KEY 以 x-api-key 发给上游。 | 직접 모드에서는 settings.json에 기록된 변수 이름입니다. 라우팅을 통해 AUTH_TOKEN은 Bearer로 업스트림으로, API_KEY는 x-api-key로 전송됩니다. | In direct mode this is the variable name written to settings.json; through routing, AUTH_TOKEN is sent upstream as Bearer and API_KEY as x-api-key. | 保留 |
| providerForm.apiHintResponses | 💡 填写兼容 OpenAI Responses API 的服务端点地址，不要以斜杠结尾 | 💡 OpenAI Responses API 호환 서비스의 엔드포인트를 입력하세요. 끝에 슬래시를 붙이지 마세요 | 💡 Fill in OpenAI Responses API compatible service endpoint, avoid trailing slash | 已修订 |
| providerForm.anthropicDefaultHaikuModel | Haiku 默认模型 | 기본 Haiku 모델 | Default Haiku Model | 已修订 |
| providerForm.anthropicDefaultSonnetModel | Sonnet 默认模型 | 기본 Sonnet 모델 | Default Sonnet Model | 已修订 |
| providerForm.anthropicDefaultOpusModel | Opus 默认模型 | 기본 Opus 모델 | Default Opus Model | 保留 |
| providerForm.modelPlaceholder |  |  |  | 保留 |
| providerForm.smallModelPlaceholder |  |  |  | 保留 |
| providerForm.haikuModelPlaceholder |  |  |  | 保留 |
| providerForm.modelHelper | 可选：指定默认使用的 Claude 模型，留空则使用系统默认。 | 선택사항: 사용할 기본 Claude 모델을 지정하고, 시스템 기본값을 사용하려면 비워 두세요. | Optional: Specify default Claude model to use, leave blank to use system default. | 保留 |
| providerForm.modelMappingLabel | 模型映射 | 모델 매핑 | Model Mapping | 保留 |
| providerForm.modelMappingHint | 显示名称只影响 /model 菜单；1M 只是给 Claude Code 的上下文能力声明。 | 표시 이름은 /model 메뉴에만 영향을 미칩니다. 1M은 Claude Code 컨텍스트 기능 선언일 뿐입니다. | Display names only affect the /model menu; 1M is only a Claude Code context-capability declaration. | 保留 |
| providerForm.stackModelsLabel | 模型列表 | 모델 목록 | Models | 已修订 |
| providerForm.addStackModel | 手动添加 | 수동으로 추가 | Add manually | 保留 |
| providerForm.stackModelDefaultHelp | 这些模型会出现在 Claude Code 的 /model 里，选中后请求直达这家。第一行是默认模型，也会写成这张卡的 ANTHROPIC_MODEL。 | 이러한 모델은 Claude Code의 /model 메뉴에 표시되며 하나를 선택하면 이 공급자에게 바로 요청이 전송됩니다. 첫 번째 행은 기본 모델이며 이 카드의 ANTHROPIC_MODEL로도 작성됩니다. | These models appear in Claude Code's /model menu and picking one sends requests straight to this provider. The first row is the default model and is also written as this card's ANTHROPIC_MODEL. | 已修订 |
| providerForm.stackModelsEmpty | 未配置模型：把这家加入聚合后，模型选择器里不会多出它的模型 | 설정된 모델이 없습니다. 통합에 추가해도 모델 선택 메뉴에 이 공급자의 모델이 표시되지 않습니다 | No models configured: this provider won't appear in the model picker once added to the aggregation | 已修订 |
| providerForm.stackModelPlaceholder | 例如 deepseek-v4-pro | 예를 들어 deepseek-v4-pro | e.g. deepseek-v4-pro | 保留 |
| providerForm.stackModelDefault | 默认模型 | 기본 모델 | Default model | 保留 |
| providerForm.stackLayout.noModels | 模型列表为空：把这家加入聚合后，模型选择器里不会多出它的模型 | 모델 목록이 비어 있습니다. 통합에 추가해도 모델 선택 메뉴에 이 공급자의 모델이 표시되지 않습니다 | The model list is empty: this provider won't appear in the model picker once added to the aggregation | 已修订 |
| providerForm.modelRoleLabel | 模型角色 | 모델 역할 | Model role | 保留 |
| providerForm.modelRoleSonnet | Sonnet | Sonnet | Sonnet | 已修订 |
| providerForm.modelRoleOpus | Opus | Opus | Opus | 已修订 |
| providerForm.modelRoleFable | Fable | Fable | Fable | 已修订 |
| providerForm.modelRoleHaiku | Haiku | Haiku | Haiku | 已修订 |
| providerForm.modelRoleSubagent | Subagent | 서브에이전트 | Subagent | 已修订 |
| providerForm.modelDisplayNameLabel | 显示名称 | 표시 이름 | Display name | 保留 |
| providerForm.modelDisplayNamePlaceholder | 例如 DeepSeek V4 Pro | 예: DeepSeek V4 Pro | e.g. DeepSeek V4 Pro | 已修订 |
| providerForm.modelNoDisplayName | 不显示在 /model 菜单 | /model에 표시되지 않음 | Not shown in /model | 保留 |
| providerForm.requestModelLabel | 实际请求模型 | 실제 요청에 사용할 모델 | Requested model | 已修订 |
| providerForm.modelOneMHeader | 声明支持 1M | 1M 컨텍스트 지원 명시 | Declare 1M | 已修订 |
| providerForm.modelOneMLabel | 1M | 1M | 1M | 已修订 |
| providerForm.fallbackModelLabel | 默认兜底模型 | 기본 대체 모델 | Default fallback model | 保留 |
| providerForm.fallbackModelHelpDirect | 写进 ANTHROPIC_MODEL，是 Claude Code 启动时用的主模型。后台任务另用 Haiku 那一档。 | ANTHROPIC_MODEL에 기록되며 Claude Code 시작 시 사용할 주 모델입니다. 백그라운드 작업은 별도로 Haiku 등급을 사용합니다. | Written to ANTHROPIC_MODEL: the main model Claude Code starts with. Background tasks use the Haiku tier instead. | 已修订 |
| providerForm.fallbackModelHelp | 没落到 Sonnet、Opus、Fable、Haiku 任一档的请求，改用这个模型发给上游。 | Sonnet, Opus, Fable 또는 Haiku 계층에 매핑되지 않는 요청은 이 모델을 통해 업스트림으로 전송됩니다. | Requests that don't map to the Sonnet, Opus, Fable, or Haiku tier are sent upstream with this model. | 保留 |
| providerForm.fallbackModelHaikuMissing | Haiku 一档没填：后台任务会用原始 Claude 模型名请求上游，第三方端点可能报错。 | Haiku 계층이 비어 있습니다. 백그라운드 작업은 원래 Claude 모델 이름을 업스트림으로 보내며, 타사 엔드포인트는 이를 거부할 수 있습니다. | Haiku tier is empty: background tasks will send the original Claude model name upstream, which third-party endpoints may reject. | 保留 |
| providerForm.fallbackModelMissing | 没填：没落到任何一档的请求会用原始 Claude 模型名发给上游，可能报错。 | 비어 있음: 어떤 계층에도 매핑되지 않는 요청은 원래 Claude 모델 이름을 업스트림으로 보내고 실패할 수 있습니다. | Empty: requests that don't map to any tier will send the original Claude model name upstream and may fail. | 保留 |
| providerForm.quickSetModels | 一键设置 | 빠른 설정 | Quick Set | 保留 |
| providerForm.quickSetSuccess | 已将模型名称应用到所有角色 | 모든 역할에 모델 이름을 적용했습니다 | Model name applied to all roles | 已修订 |
| providerForm.advancedOptionsToggle | 高级选项 | 고급 옵션 | Advanced Options | 保留 |
| providerForm.categoryOfficial | 官方 | 공식 | Official | 已修订 |
| providerForm.categoryCnOfficial | 开源官方 | 오픈소스 공식 | Opensource Official | 保留 |
| providerForm.categoryAggregation | 聚合服务 | 통합 | Aggregation | 保留 |
| providerForm.categoryThirdParty | 第三方 | 타사 | Third Party | 已修订 |
| providerForm.fetchModels | 获取模型列表 | 모델 목록 가져오기 | Fetch Models | 已修订 |
| providerForm.fetchingModels | 正在获取... | 가져오는 중... | Fetching... | 保留 |
| providerForm.searchModelPlaceholder | 搜索模型... | 모델 검색... | Search models... | 保留 |
| providerForm.searchModelEmpty | 没有匹配的模型 | 일치하는 모델이 없습니다. | No matching models. | 保留 |
| providerForm.searchModelAriaLabel | 选择模型 | 모델 선택 | Select model | 保留 |
| providerForm.fetchModelsSuccess | 获取到 {{count}} 个模型 | {{count}} 모델 발견 | Found {{count}} models | 保留 |
| providerForm.modelMetadataFilled | 已补全 {{model}} 的上下文等参数（来源：{{source}}），请核对 | {{model}}에 대한 컨텍스트 창 및 기타 매개변수가 채워졌습니다(출처: {{source}}). 다시 한번 확인해 주세요. | Filled in context window and other parameters for {{model}} (source: {{source}}). Please double-check. | 保留 |
| providerForm.modelMetadataFilledMany | 已补全 {{count}} 个模型的上下文等参数（来源：{{source}}），请核对 | {{count}} 모델에 대한 컨텍스트 창 및 기타 매개변수가 채워져 있습니다(출처: {{source}}). 다시 한번 확인해 주세요. | Filled in context window and other parameters for {{count}} models (source: {{source}}). Please double-check. | 保留 |
| providerForm.gptContextWindowHint | 中转站的 GPT 多来自 ChatGPT 订阅，窗口只有 272K。窗口写大了不会提前压缩，等上游拒收时这一轮会失败；确认这家支持更大窗口再这样填。 | 중계 서비스의 GPT는 대부분 ChatGPT 구독을 통해 제공되어 컨텍스트 창이 272K에 불과합니다. 창 크기를 실제보다 크게 입력하면 미리 압축되지 않아 업스트림이 요청을 거부할 때 해당 응답이 실패합니다. 이 공급자가 더 큰 컨텍스트 창을 지원하는지 확인한 후 입력하세요. | GPT on relays usually comes from ChatGPT subscriptions, whose window is only 272K. A larger window delays compaction until the upstream rejects the request and the turn fails; only use it if this provider supports it. | 已修订 |
| providerForm.modelMetadataSourcePreset | 预设 | 프리셋 | preset | 保留 |
| providerForm.modelMetadataSourceBoth | 预设和 models.dev | 프리셋 및 models.dev | preset and models.dev | 保留 |
| providerForm.modelPicker.title | 选择模型 | 모델 선택 | Select models | 保留 |
| providerForm.modelPicker.lead | 勾选的模型会加入列表，取消勾选会从列表中移除。 | 선택한 모델이 목록에 추가됩니다. 모델을 선택 취소하면 목록에서 해당 모델이 제거됩니다. | Checked models are added to the list; unchecking a model removes it from the list. | 保留 |
| providerForm.modelPicker.refresh | 重新获取 | 다시 가져오기 | Fetch again | 保留 |
| providerForm.modelPicker.selectAll | 全选 | 모두 선택 | Select all | 保留 |
| providerForm.modelPicker.selectNone | 全不选 | 모두 선택 해제 | Select none | 已修订 |
| providerForm.modelPicker.selectedCount | 已选 {{selected}} / 共 {{total}} | {{total}} 중 {{selected}}가 선택됨 | {{selected}} of {{total}} selected | 保留 |
| providerForm.modelPicker.reasoning | 推理 | 추론 | Reasoning | 已修订 |
| providerForm.modelPicker.image | 图片 | 이미지 | Image | 已修订 |
| providerForm.modelPicker.onlySelected | 只看已选 | 선택된 것만 | Selected only | 保留 |
| providerForm.modelPicker.notInProvider | 不在供应商列表中 | 공급자 목록에 없음 | Not in the provider's list | 已修订 |
| providerForm.modelPicker.fromProvider | 供应商返回的模型 | 공급자가 반환한 모델 | From the provider | 已修订 |
| providerForm.modelPicker.apply | 应用 | 적용 | Apply | 保留 |
| providerForm.fetchModelsFailed | 获取模型列表失败 | 모델을 가져오지 못했습니다. | Failed to fetch models | 保留 |
| providerForm.fetchModelsEmpty | 未找到可用模型 | 모델을 찾을 수 없습니다. | No models found | 保留 |
| providerForm.fetchModelsNeedApiKey | 请先填写 API Key | 먼저 API 키를 입력하세요. | Please fill in API Key first | 保留 |
| providerForm.fetchModelsNeedEndpoint | 请先填写 API 端点 | 먼저 API 엔드포인트를 입력하세요. | Please fill in API endpoint first | 保留 |
| providerForm.fetchModelsNeedConfig | 请先填写 API 端点和 API Key | 먼저 API 엔드포인트와 API 키를 입력하세요. | Please fill in API endpoint and API Key first | 保留 |
| providerForm.fetchModelsAuthFailed | API Key 无效或无权限 | API 키가 유효하지 않거나 권한이 부족합니다. | API Key is invalid or lacks permission | 保留 |
| providerForm.fetchModelsNotSupported | 该供应商不支持获取模型列表 | 이 공급자는 모델 목록 가져오기를 지원하지 않습니다. | This provider does not support fetching model list | 已修订 |
| providerForm.fetchModelsEndpointNotFound | 未找到可用的模型列表端点，请检查 Base URL 或确认供应商是否开放该接口 | 연결할 수 있는 모델 엔드포인트가 없습니다. 기본 URL을 확인하거나 공급자가 이 API를 노출하는지 확인하세요. | No reachable models endpoint found. Please check the Base URL or confirm whether the provider exposes this API. | 已修订 |
| providerForm.fetchModelsTimeout | 请求超时，请检查网络连接 | 요청 시간이 초과되었습니다. 네트워크 연결을 확인하세요. | Request timed out, please check network connection | 保留 |
| providerForm.requiredFields | 请填写供应商名称、API 地址、API Key 和模型 | 공급자 이름, API 엔드포인트, API 키 및 모델을 입력하세요. | Please fill in provider name, API endpoint, API Key and model | 已修订 |
| providerForm.customUserAgentHelp | 替换转发到供应商的请求里的 User-Agent。 | 공급자로 전달하는 요청의 User-Agent를 바꿉니다. | Replaces the User-Agent of requests forwarded to the provider. | 已修订 |
| providerForm.localProxyRequestOverridesHelp | 作用于格式转换后发给上游的请求。 | 형식 변환 후 업스트림 요청에 적용됩니다. | Applies to the upstream request after format conversion. | 保留 |
| providerForm.apiFormatHelp | 看供应商原生支持哪种协议：Anthropic Messages 原样转发、不转换格式；其余三种由路由转成 Anthropic Messages。 | 공급자가 네이티브로 지원하는 프로토콜을 선택하세요. Anthropic Messages는 형식 변환 없이 그대로 전달하며, 나머지 세 형식은 라우팅에서 Anthropic Messages로 변환합니다. | Pick the protocol the provider supports natively: Anthropic Messages is forwarded as is without conversion; routing converts the other three to Anthropic Messages. | 已修订 |
| providerForm.directModeFormatInUse | 这张卡正在直连使用：改成这种格式后保存，请求会失败。请先切到路由或聚合。 | 이 카드는 현재 직접 연결로 사용 중입니다. 이 형식으로 저장하면 요청이 실패합니다. 먼저 라우팅 또는 통합 모드로 전환하세요. | This card is in use in direct mode: saving it with this format makes requests fail. Switch to routing or Aggregation first. | 已修订 |
| providerForm.directModeFormatSwitch | 直连模式下用不了这种格式，切到路由或聚合后才能用这张卡。 | 이 형식은 직접 연결 모드에서 사용할 수 없습니다. 이 카드를 사용하려면 라우팅 또는 통합 모드로 전환하세요. | This format doesn't work in direct mode; switch to routing or Aggregation to use this card. | 已修订 |
| copilot.authSection | GitHub Copilot 认证 | GitHub Copilot 인증 | GitHub Copilot Authentication | 已修订 |
| copilot.authStatus | 认证状态 | 인증 상태 | Authentication Status | 已修订 |
| copilot.authenticated | 已认证: {{username}} | {{username}}로 인증됨 | Authenticated as {{username}} | 保留 |
| copilot.notAuthenticated | 未认证 | 인증되지 않음 | Not authenticated | 保留 |
| copilot.loginWithGitHub | 使用 GitHub 登录 | GitHub로 로그인 | Login with GitHub | 保留 |
| copilot.githubAccount | GitHub 账号 | GitHub 계정 | GitHub account | 保留 |
| copilot.manageAccounts | 管理账号 | 계정 관리 | Manage accounts | 保留 |
| copilot.loginRequired | 请先登录 GitHub Copilot | 먼저 GitHub Copilot에 로그인하십시오. | Please login to GitHub Copilot first | 保留 |
| copilot.statusLoading | 正在加载账号状态... | 계정 상태 로드 중... | Loading account status... | 保留 |
| copilot.statusUnavailable | 状态不可用 | 상태를 알 수 없음 | Status unavailable | 保留 |
| copilot.statusLoadFailed | 无法加载 GitHub Copilot 账号状态，请重试。 | GitHub Copilot 계정 상태를 로드하지 못했습니다. 다시 시도해 주세요. | Failed to load GitHub Copilot account status. Please retry. | 保留 |
| copilot.waitingForAuth | 等待授权中... | 승인을 기다리는 중... | Waiting for authorization... | 保留 |
| copilot.enterCode | 请在浏览器中输入验证码： | 브라우저에 코드를 입력하세요: | Please enter the code in your browser: | 保留 |
| copilot.logout | 注销 | 로그아웃 | Logout | 保留 |
| copilot.authSuccess | GitHub Copilot 认证成功 | GitHub Copilot 인증 성공 | GitHub Copilot authentication successful | 已修订 |
| copilot.authFailed | 认证失败: {{error}} | 인증 실패: {{error}} | Authentication failed: {{error}} | 保留 |
| copilot.authTimeout | 认证超时，请重试 | 인증 시간이 초과되었습니다. 다시 시도해 주세요. | Authentication timed out, please try again | 保留 |
| copilot.tokenExpired | 令牌已过期，请重新认证 | 토큰이 만료되었습니다. 다시 인증하세요. | Token expired, please re-authenticate | 保留 |
| copilot.accountCount | {{count}} 个账号 | 계정 {{count}}개 | {{count}} account(s) | 已修订 |
| copilot.selectAccount | 选择账号 | 계정 선택 | Select Account | 保留 |
| copilot.selectAccountPlaceholder | 选择一个 GitHub 账号 | GitHub 계정을 선택하세요 | Select a GitHub account | 保留 |
| copilot.useDefaultAccount | 使用默认账号 | 기본 계정 사용 | Use default account | 保留 |
| copilot.loggedInAccounts | 已登录账号 | 로그인된 계정 | Logged in accounts | 保留 |
| copilot.defaultAccount | 默认 | 기본값 | Default | 保留 |
| copilot.selected | 已选中 | 선택됨 | Selected | 已修订 |
| copilot.removeAccount | 移除账号 | 계정 삭제 | Remove account | 保留 |
| copilot.setAsDefault | 设为默认 | 기본값으로 설정 | Set as default | 保留 |
| copilot.addAnotherAccount | 添加其他账号 | 다른 계정 추가 | Add another account | 保留 |
| copilot.retry | 重试 | 다시 시도 | Retry | 保留 |
| copilot.copyCode | 复制代码 | 코드 복사 | Copy code | 保留 |
| copilot.migrationFailed | 旧认证数据迁移失败：{{error}} | 레거시 인증 마이그레이션 실패: {{error}} | Legacy auth migration failed: {{error}} | 保留 |
| copilot.loadModelsFailed | 加载 Copilot 模型列表失败 | Copilot 모델을 로드하지 못했습니다. | Failed to load Copilot models | 保留 |
| copilot.deploymentType | GitHub 部署类型 | GitHub 배포 유형 | GitHub Deployment Type | 保留 |
| copilot.deploymentGitHubCom | GitHub.com | GitHub.com | GitHub.com | 保留 |
| copilot.deploymentEnterprise | GitHub Enterprise Server | GitHub Enterprise Server | GitHub Enterprise Server | 已修订 |
| copilot.enterpriseDomainPlaceholder | 例如：company.ghe.com | 예를 들어 company.ghe.com | e.g. company.ghe.com | 保留 |
| codexOauth.authStatus | 认证状态 | 인증 상태 | Auth status | 保留 |
| codexOauth.notAuthenticated | 未认证 | 인증되지 않음 | Not authenticated | 保留 |
| codexOauth.loginWithChatGPT | 使用 ChatGPT 登录 | ChatGPT로 로그인 | Sign in with ChatGPT | 保留 |
| codexOauth.loginRequired | 请先登录 ChatGPT 账号 | 먼저 ChatGPT에 로그인하세요. | Please sign in to ChatGPT first | 保留 |
| codexOauth.statusLoading | 正在加载账号状态... | 계정 상태 로드 중... | Loading account status... | 保留 |
| codexOauth.statusUnavailable | 状态不可用 | 상태를 알 수 없음 | Status unavailable | 保留 |
| codexOauth.statusLoadFailed | 无法加载 ChatGPT 账号状态，请重试。 | ChatGPT 계정 상태를 로드하지 못했습니다. 다시 시도해 주세요. | Failed to load ChatGPT account status. Please retry. | 保留 |
| codexOauth.waitingForAuth | 等待授权中... | 승인을 기다리는 중... | Waiting for authorization... | 保留 |
| codexOauth.enterCode | 请在浏览器中输入以下验证码： | 브라우저에 코드를 입력하세요: | Enter the code in your browser: | 保留 |
| codexOauth.accountCount | {{count}} 个账号 | 계정 {{count}}개 | {{count}} account(s) | 已修订 |
| codexOauth.selectAccount | 选择账号 | 계정 선택 | Select account | 保留 |
| codexOauth.chatgptAccount | ChatGPT 账号 | ChatGPT 계정 | ChatGPT account | 已修订 |
| codexOauth.accountToUse | 使用的账号 | 사용할 계정 | Account to use | 保留 |
| codexOauth.signInMethod | 登录方式 | 로그인 방법 | Sign-in method | 保留 |
| codexOauth.manageAccounts | 管理账号 | 계정 관리 | Manage accounts | 保留 |
| codexOauth.selectAccountPlaceholder | 选择一个 ChatGPT 账号 | ChatGPT 계정 선택 | Choose a ChatGPT account | 保留 |
| codexOauth.officialAccountPlaceholder | 请选择登录方式 | 로그인 방법을 선택하세요 | Choose a sign-in method | 保留 |
| codexOauth.addOrManageAccounts | 添加或管理 ChatGPT 账号 | ChatGPT 계정 추가 또는 관리 | Add or manage ChatGPT accounts | 保留 |
| codexOauth.explicitSelectionRequired | 请先选择登录方式 | 로그인 방법을 선택하세요 | Choose a sign-in method | 保留 |
| codexOauth.useDefaultAccount | 使用默认账号 | 기본 계정 사용 | Use default account | 保留 |
| codexOauth.noneOptionLabel | 跟随 Codex 登录 | Codex 로그인 따르기 | Follow Codex login | 已修订 |
| codexOauth.reauthDescription | 为与浏览器登录行为保持一致，这些账号需要重新登录以补全所需的登录凭据（id_token）。重新登录后即可正常用于托管绑定。 | 브라우저 로그인 동작을 일치시키려면 해당 계정에 다시 로그인하여 필수 로그인 자격 증명(id_token)을 복원해야 합니다. 다시 인증되면 관리형 바인딩에 사용할 수 있습니다. | To match the browser-login behavior, these accounts must sign in again to restore the required login credential (id_token). Once re-authenticated they can be used for managed binding. | 保留 |
| codexOauth.reauthBadge | 需要重新登录 | 재로그인이 필요합니다 | Re-login required | 保留 |
| codexOauth.reauthLogin | 重新登录 | 재로그인 | Re-login | 保留 |
| codexOauth.reauthSelectHint | 该账号需重新登录以启用托管绑定。 | 관리형 바인딩을 활성화하려면 이 계정에 다시 로그인해야 합니다. | This account needs to sign in again to enable managed binding. | 保留 |
| codexOauth.reauthNow | 立即重新登录 | 지금 다시 로그인하세요 | Re-login now | 保留 |
| codexOauth.duplicateAccount | 该 ChatGPT 账号已添加，请直接使用现有账号。 | 이 ChatGPT 계정은 이미 추가되었습니다. 기존 계정을 사용하세요. | This ChatGPT account has already been added. Use the existing account. | 保留 |
| codexOauth.loggedInAccounts | 已登录账号 | 로그인된 계정 | Logged in accounts | 保留 |
| codexOauth.defaultAccount | 默认 | 기본값 | Default | 保留 |
| codexOauth.selected | 已选中 | 선택됨 | Selected | 已修订 |
| codexOauth.removeAccount | 移除账号 | 계정 삭제 | Remove account | 保留 |
| codexOauth.setAsDefault | 设为默认 | 기본값으로 설정 | Set as default | 保留 |
| codexOauth.addAnotherAccount | 添加其他账号 | 다른 계정 추가 | Add another account | 保留 |
| codexOauth.logoutAll | 注销所有账号 | 모든 계정 로그아웃 | Logout all accounts | 保留 |
| codexOauth.retry | 重试 | 다시 시도 | Retry | 保留 |
| codexOauth.copyCode | 复制代码 | 코드 복사 | Copy code | 保留 |
| codexOauth.fastMode | FAST 模式 | FAST 모드 | FAST mode | 已修订 |
| codexOauth.fastModeDescription | 发送 service_tier="priority" 换取更低延迟。默认关闭——开启后会按更高速率消耗 ChatGPT 配额。 | 대기 시간을 줄이려면 service_tier="priority"를 보내세요. 기본적으로 꺼져 있습니다. 활성화하면 ChatGPT 할당량이 더 높은 비율로 소모됩니다. | Send service_tier="priority" for lower latency. Off by default — enabling it consumes your ChatGPT quota at a higher rate. | 保留 |
| xaiOauth.authStatus | xAI OAuth 认证 | xAI OAuth 인증 | xAI OAuth authentication | 保留 |
| xaiOauth.accountCount | {{count}} 个可用账号 | 사용 가능한 계정: {{count}} | Usable accounts: {{count}} | 保留 |
| xaiOauth.reauthRequired | 需要重新登录 | 다시 로그인 필요 | Sign-in required | 已修订 |
| xaiOauth.notAuthenticated | 未认证 | 인증되지 않음 | Not authenticated | 保留 |
| xaiOauth.selectAccount | 选择账号 | 계정 선택 | Select account | 保留 |
| xaiOauth.selectAccountPlaceholder | 选择 xAI 账号 | xAI 계정을 선택하세요 | Select an xAI account | 保留 |
| xaiOauth.useDefaultAccount | 使用默认账号 | 기본 계정 사용 | Use default account | 保留 |
| xaiOauth.accounts | xAI 账号 | xAI 계정 | xAI accounts | 保留 |
| xaiOauth.defaultAccount | 默认 | 기본값 | Default | 保留 |
| xaiOauth.expired | 凭据已失效 | 자격 증명이 만료되었습니다. | Credentials expired | 保留 |
| xaiOauth.setAsDefault | 设为默认 | 기본값으로 설정 | Set as default | 保留 |
| xaiOauth.removeAccount | 移除账号 | 계정 삭제 | Remove account | 保留 |
| xaiOauth.addOrReauth | 添加账号或重新登录 | 계정을 추가하거나 다시 로그인하세요. | Add account or sign in again | 保留 |
| xaiOauth.login | 使用 xAI 登录 | xAI로 로그인 | Sign in with xAI | 保留 |
| xaiOauth.waitingForAuth | 等待 xAI 授权中… | xAI 인증을 기다리는 중… | Waiting for xAI authorization… | 保留 |
| xaiOauth.enterCode | 若浏览器未自动填入，请输入： | 브라우저가 자동으로 입력하지 않은 경우 다음을 입력하십시오. | If the browser did not fill it in automatically, enter: | 保留 |
| xaiOauth.retry | 重试 | 다시 시도 | Retry | 保留 |
| xaiOauth.logoutAll | 删除全部 xAI 账号 | 모든 xAI 계정 삭제 | Delete all xAI accounts | 保留 |
| xaiOauth.loginRequired | 请先登录 xAI 账号 | 먼저 xAI 계정에 로그인하세요 | Sign in to an xAI account first | 保留 |
| managedAuth.accountRemoved | 账号已删除 | 계정이 삭제되었습니다 | Account deleted | 保留 |
| managedAuth.selectedAccountNeedsReauth | 已绑定账号不存在或需要重新登录 | 연결된 계정이 없거나 다시 로그인해야 합니다. | The linked account is missing or needs you to sign in again | 保留 |
| managedAuth.selectedAccountUnavailable | 已绑定账号不存在或需要重新登录，请重新选择账号 | 연결된 계정이 없거나 다시 로그인해야 합니다. 계정을 다시 선택하세요. | The linked account is missing or needs you to sign in again. Select another account. | 已修订 |
| managedAuth.usedBy | {{count}} 个供应商在用 | {{count}} 공급자가 사용함 | Used by {{count}} provider(s) | 已修订 |
| managedAuth.usedByTitle | 在用的供应商：{{names}} | 사용처: {{names}} | Used by: {{names}} | 保留 |
| managedAuth.remove.titleOne | 删除账号「{{login}}」？ | '{{login}}' 계정을 삭제하시겠습니까? | Delete account “{{login}}”? | 保留 |
| managedAuth.remove.titleAll | 删除全部 {{service}} 账号？ | 모든 {{service}} 계정을 삭제하시겠습니까? | Delete all {{service}} accounts? | 保留 |
| managedAuth.remove.leadOne | 会删除这个账号保存在 CC Switch 里的登录凭据，无法撤销。 | 이렇게 하면 이 계정에 대해 CC Switch가 유지하는 로그인 자격 증명이 삭제됩니다. 이 작업은 취소할 수 없습니다. | This deletes the sign-in credentials CC Switch keeps for this account. This can’t be undone. | 保留 |
| managedAuth.remove.leadAll | 会删除这 {{count}} 个账号保存在 CC Switch 里的登录凭据，无法撤销。 | 이렇게 하면 CC Switch가 이러한 {{count}} 계정에 대해 유지하는 로그인 자격 증명이 삭제됩니다. 이 작업은 취소할 수 없습니다. | This deletes the sign-in credentials CC Switch keeps for these {{count}} accounts. This can’t be undone. | 保留 |
| managedAuth.remove.brokenOne | 这些供应商会无法使用，直到重新登录或改选别的账号： | 다음 공급자는 다시 로그인하거나 다른 계정을 선택할 때까지 사용할 수 없습니다: | These providers will stop working until you sign in again or pick another account: | 已修订 |
| managedAuth.remove.brokenAll | 这些供应商会无法使用，直到重新登录： | 다음 공급자는 다시 로그인할 때까지 사용할 수 없습니다: | These providers will stop working until you sign in again: | 已修订 |
| managedAuth.remove.moved | 这些供应商用的是默认账号，删除后改用新的默认账号： | 다음 공급자는 기본 계정을 사용하므로 삭제 후 새 기본 계정으로 전환됩니다: | These providers use the default account and will switch to the new default: | 已修订 |
| managedAuth.remove.noneOne | 没有供应商在用这个账号。 | 어떤 공급자도 이 계정을 사용하지 않습니다. | No provider uses this account. | 已修订 |
| managedAuth.remove.noneAll | 没有供应商在用这些账号。 | 이 계정들을 사용하는 공급자가 없습니다. | No provider uses these accounts. | 已修订 |
| managedAuth.remove.confirmOne | 删除账号 | 계정 삭제 | Delete account | 保留 |
| managedAuth.remove.confirmAll | 删除 {{count}} 个账号 | {{count}} 계정 삭제 | Delete {{count}} accounts | 保留 |
| managedAuth.remove.appSeparator | ： | :  | :  | 保留 |
| managedAuth.remove.nameSeparator | 、 | ,  | ,  | 保留 |
| endpointTest.title | 请求地址管理 | API 엔드포인트 관리 | API Endpoint Management | 保留 |
| endpointTest.endpoints | 个端点 | 엔드포인트 | endpoints | 保留 |
| endpointTest.autoSelect | 自动选择 | 자동 선택 | Auto Select | 保留 |
| endpointTest.testSpeed | 测速 | 속도 테스트 | Test | 已修订 |
| endpointTest.testing | 测速中 | 테스트 중 | Testing | 已修订 |
| endpointTest.addEndpointPlaceholder | https://api.example.com | https://api.example.com | https://api.example.com | 保留 |
| endpointTest.done | 完成 | 완료 | Done | 保留 |
| endpointTest.noEndpoints | 暂无端点 | 엔드포인트 없음 | No endpoints | 保留 |
| endpointTest.failed | 失败 | 실패 | Failed | 已修订 |
| endpointTest.enterValidUrl | 请输入有效的 URL | 유효한 URL을 입력하세요. | Please enter a valid URL | 保留 |
| endpointTest.invalidUrlFormat | URL 格式不正确 | 잘못된 URL 형식 | Invalid URL format | 保留 |
| endpointTest.onlyHttps | 仅支持 HTTP/HTTPS | HTTP/HTTPS만 지원됨 | Only HTTP/HTTPS supported | 保留 |
| endpointTest.urlExists | 该地址已存在 | 이 URL은 이미 존재합니다. | This URL already exists | 保留 |
| endpointTest.saveFailed | 保存失败，请重试 | 저장하지 못했습니다. 다시 시도해 주세요. | Save failed, please try again | 保留 |
| endpointTest.loadEndpointsFailed | 加载自定义端点失败: | 커스텀 엔드포인트를 로드하지 못했습니다. | Failed to load custom endpoints: | 保留 |
| endpointTest.addEndpointFailed | 添加自定义端点失败: | 커스텀 엔드포인트를 추가하지 못했습니다. | Failed to add custom endpoint: | 保留 |
| endpointTest.removeEndpointFailed | 删除自定义端点失败: | 커스텀 엔드포인트를 제거하지 못했습니다. | Failed to remove custom endpoint: | 保留 |
| endpointTest.removeFailed | 删除失败: {{error}} | 제거 실패: {{error}} | Remove failed: {{error}} | 保留 |
| endpointTest.updateLastUsedFailed | 更新端点使用时间失败 | 엔드포인트 마지막 사용 시간을 업데이트하지 못했습니다. | Failed to update endpoint last used time | 保留 |
| endpointTest.pleaseAddEndpoint | 请先添加端点 | 먼저 엔드포인트를 추가하세요. | Please add an endpoint first | 保留 |
| endpointTest.testUnavailable | 测速功能不可用 | 속도 테스트 불가 | Speed test unavailable | 保留 |
| endpointTest.noResult | 未返回结果 | 반환된 결과가 없습니다. | No result returned | 保留 |
| endpointTest.testFailed | 测速失败: {{error}} | 속도 테스트 실패: {{error}} | Speed test failed: {{error}} | 保留 |
| endpointTest.empty | 暂无端点 | 엔드포인트 없음 | No endpoints | 保留 |
| codexConfig.authJson | auth.json (JSON) * | auth.json (JSON) * | auth.json (JSON) * | 保留 |
| codexConfig.authJsonPlaceholder | {<br>  "OPENAI_API_KEY": "sk-your-api-key-here"<br>} | {<br>  "OPENAI_API_KEY": "sk-your-api-key-here"<br>} | {<br>  "OPENAI_API_KEY": "sk-your-api-key-here"<br>} | 已修订 |
| codexConfig.authJsonHint | Codex auth.json 配置内容 | Codex auth.json 설정 내용 | Codex auth.json configuration content | 已修订 |
| codexConfig.authJsonStorageHint | 路由模式下显示的是存储的 auth 配置，不是实时的 auth.json | 라우팅 모드에서는 현재 적용 중인 auth.json이 아닌 저장된 인증 설정을 표시합니다. | In Routing mode this shows the stored auth, not the live auth.json. | 已修订 |
| codexConfig.configToml | config.toml (TOML) | config.toml (TOML) | config.toml (TOML) | 保留 |
| codexConfig.configTomlHint | Codex config.toml 配置内容 | Codex config.toml 설정 내용 | Codex config.toml configuration content | 已修订 |
| codexConfig.configTomlStorageHint | 路由模式下显示的是存储的 config 配置，不是实时的 config.toml | 라우팅 모드에서는 현재 적용 중인 config.toml이 아닌 저장된 설정을 표시합니다. | In Routing mode this shows the stored config, not the live config.toml. | 已修订 |
| codexConfig.proxyTakeoverStorageNotice | 💡 当前应用处于路由模式。这里编辑的是存储的供应商配置，实际的 live 配置暂由路由服务接管 | 💡 이 앱은 라우팅 모드입니다. 저장된 공급자 설정을 편집하고 있습니다. 라이브 설정은 라우팅 서비스에 의해 일시적으로 관리됩니다. | 💡 This app is in Routing mode. You are editing the stored provider config; the live config is temporarily managed by the routing service. | 已修订 |
| codexConfig.enableRemoteCompaction | 启用远程压缩 | 원격 압축 활성화 | Enable remote compaction | 保留 |
| codexConfig.remoteCompactionHint | 开启后会将当前 model_providers 条目的 name 写为 OpenAI，使 Codex 尝试使用远程压缩。 | 활성화되면 활성 model_providers 항목 이름이 OpenAI로 기록되므로 Codex는 원격 압축을 시도할 수 있습니다. | When enabled, the active model_providers entry name is written as OpenAI so Codex can try remote compaction. | 保留 |
| codexConfig.apiUrlLabel | API 请求地址 | API 요청 URL | API Request URL | 保留 |
| codexConfig.saveFailed | 保存失败: {{error}} | 저장 실패: {{error}} | Save failed: {{error}} | 保留 |
| codexConfig.upstreamFormatLabel | 上游格式 | 업스트림 형식 | Upstream Format | 保留 |
| codexConfig.upstreamFormatAuto | 自动（按模型能力） | 자동(모델 기능) | Automatic (model capabilities) | 保留 |
| codexConfig.upstreamFormatCopilotResponses | Responses（需开启路由） | Responses (라우팅 필요) | Responses (routing required) | 已修订 |
| codexConfig.upstreamFormatCopilotHint | 自动模式按模型能力优先用 Responses，否则用 Chat Completions；也可以手动指定协议。 | 자동 모드에서는 모델이 지원하면 Responses를 우선 사용하고, 그렇지 않으면 Chat Completions를 사용합니다. 프로토콜을 직접 지정할 수도 있습니다. | Auto prefers Responses when the model supports it, otherwise Chat Completions. You can also pick a protocol explicitly. | 已修订 |
| codexConfig.upstreamFormatHint | 看供应商原生支持哪种协议：Responses 原样转发、不转换格式；Chat 或 Anthropic 由路由转成 Responses。 | 공급자가 네이티브로 지원하는 프로토콜을 선택하세요. Responses는 변환 없이 그대로 전달하며, Chat 또는 Anthropic 형식은 라우팅에서 Responses로 변환합니다. | Pick the protocol the provider supports natively: Responses is forwarded as is without conversion; routing converts Chat or Anthropic to Responses. | 已修订 |
| codexConfig.upstreamFormatChat | Chat Completions（需转换） | Chat Completions (변환 필요) | Chat Completions (conversion required) | 已修订 |
| codexConfig.upstreamFormatResponses | Responses（原生） | Responses (네이티브) | Responses (native) | 已修订 |
| codexConfig.upstreamFormatAnthropic | Anthropic Messages（需转换） | Anthropic Messages (변환 필요) | Anthropic Messages (conversion required) | 已修订 |
| codexConfig.anthropicAuthFieldLabel | 认证字段 | 인증 필드 | Auth field | 保留 |
| codexConfig.anthropicAuthFieldAuthToken | ANTHROPIC_AUTH_TOKEN（Authorization） | ANTHROPIC_AUTH_TOKEN (Authorization) | ANTHROPIC_AUTH_TOKEN (Authorization) | 已修订 |
| codexConfig.anthropicAuthFieldApiKey | ANTHROPIC_API_KEY（x-api-key） | ANTHROPIC_API_KEY (x-api-key) | ANTHROPIC_API_KEY (x-api-key) | 已修订 |
| codexConfig.anthropicAuthFieldHint | 按网关读取 API Key 的请求头选择，两者只发其一。 | 게이트웨이가 API 키를 읽는 헤더를 선택합니다. 하나만 전송됩니다. | Pick the header the gateway reads the API key from. Only one is sent. | 保留 |
| codexConfig.impersonateClaudeCodeLabel | 模拟 Claude Code 客户端 | Claude Code 클라이언트 에뮬레이션 | Emulate Claude Code client | 保留 |
| codexConfig.impersonateClaudeCodeHint | 网关只允许 Claude Code 使用时打开：伪装 Claude Code 的请求头，并在系统提示首行注入它的身份。 | 게이트웨이가 Claude Code만 수락할 때 켜기: Claude Code의 요청 헤더를 보내고 해당 ID를 시스템 프롬프트의 첫 번째 줄에 넣습니다. | Turn on when the gateway only accepts Claude Code: sends Claude Code's request headers and puts its identity on the first line of the system prompt. | 保留 |
| codexConfig.maxOutputTokensLabel | 最大输出 tokens | 최대 출력 토큰 | Max output tokens | 保留 |
| codexConfig.maxOutputTokensPlaceholder | 留空则使用默认 8192 | 기본값 8192를 사용하려면 비워 두세요. | Leave empty to use the default 8192 | 保留 |
| codexConfig.maxOutputTokensHint | Codex 不带输出上限，默认 8192，长回答或深度思考容易被截断。这里的值会作为 Anthropic 的 max_tokens 发出。 | Codex는 출력 제한을 보내지 않으므로 기본 8192는 긴 답변이나 깊은 사고를 차단할 수 있습니다. 이 값은 Anthropic의 max_tokens로 전송됩니다. | Codex sends no output limit, so the default 8192 can cut off long answers or deep thinking. This value is sent as Anthropic's max_tokens. | 保留 |
| codexConfig.promptCacheRoutingLabel | 提示词缓存路由 | 프롬프트 캐시 라우팅 | Prompt cache routing | 已修订 |
| codexConfig.promptCacheRoutingAuto | 自动（推荐） | 자동(권장) | Auto (recommended) | 保留 |
| codexConfig.promptCacheRoutingEnabled | 开启 | 활성화됨 | Enabled | 保留 |
| codexConfig.promptCacheRoutingDisabled | 关闭 | 비활성화됨 | Disabled | 保留 |
| codexConfig.promptCacheRoutingHint | 自动：只对确认兼容的上游发送 prompt_cache_key。开启：用于其他兼容网关。关闭：避免严格网关因未知字段返回 400。 | 자동: 호환성이 확인된 업스트림에만 prompt_cache_key를 보냅니다. 켜짐: 다른 호환 게이트웨이에 사용할 수 있습니다. 꺼짐: 알 수 없는 필드를 거부하는 엄격한 게이트웨이의 400 오류를 방지합니다. | Auto: send prompt_cache_key only to known-compatible upstreams. On: for other compatible gateways. Off: avoid 400s from strict gateways that reject unknown fields. | 已修订 |
| codexConfig.contextWindow1M | 1M 上下文窗口 | 1M 컨텍스트 창 | 1M Context Window | 保留 |
| codexConfig.contextWindowPlaceholder | 例如: 128000 | 예: 128000 | e.g., 128000 | 保留 |
| codexConfig.autoCompactLimit | 压缩阈值 | 자동 압축 임계값 | Auto Compact Limit | 已修订 |
| codexConfig.autoCompactLimitPlaceholder | 例如: 90000 | 예: 90000 | e.g., 90000 | 保留 |
| codexConfig.defaultModelLabel | 默认模型 | 기본 모델 | Default Model | 保留 |
| codexConfig.defaultModelPlaceholder | 例如: gpt-5.6-sol | 예를 들어 gpt-5.6-sol | e.g. gpt-5.6-sol | 保留 |
| codexConfig.defaultModelHint | Codex 默认请求的模型。添加模型列表后，列表第一行就是默认模型。 | Codex가 기본으로 요청할 모델입니다. 모델 목록을 추가하면 첫 번째 행이 기본 모델이 됩니다. | The model Codex requests by default. Once you add a model list, its first row is the default model. | 已修订 |
| codexConfig.subagentModelLabel | 子代理模型 | 서브에이전트 모델 | Sub-agent Model | 已修订 |
| codexConfig.subagentModelPlaceholder | 留空则跟随主模型 | 기본 모델을 따르려면 비워 두세요. | Leave empty to follow the main model | 保留 |
| codexConfig.subagentReasoningEffortLabel | 子代理推理强度 | 서브에이전트 추론 수준 | Sub-agent reasoning effort | 已修订 |
| codexConfig.subagentReasoningEffortDefault | 默认强度 | 기본 수준 | Default effort | 已修订 |
| codexConfig.subagentModelHint | Codex 派出的子代理默认用的模型和推理强度。留空时沿用主代理的；只填模型时用该模型自己的默认强度。聚合模式下不生效，改用聚合页签「聚合设置」里的子代理模型。 | Codex 서브에이전트가 기본으로 사용할 모델과 추론 수준입니다. 비워 두면 주 에이전트의 설정을 따르며, 모델만 입력하면 해당 모델의 기본 추론 수준을 사용합니다. 통합 모드에서는 적용되지 않고 통합 탭 설정의 서브에이전트 모델을 사용합니다. | The model and reasoning effort Codex sub-agents use by default. Empty follows the main agent; a model alone uses its own default effort. Ignored in Aggregation mode, where the sub-agent model in the Aggregation tab's settings applies instead. | 已修订 |
| codexConfig.subagentModelNotInCatalog | 该模型不在模型列表中：Codex 拿不到它的上下文窗口；经路由转成 Chat / Anthropic 协议时会被换成默认模型。 | 이 모델은 모델 목록에 없습니다. Codex는 컨텍스트 창을 가져올 수 없으며 라우팅이 요청을 Chat / Anthropic로 변환할 때 기본 모델로 대체됩니다. | This model is not in the model list: Codex can't get its context window, and when routing converts requests to Chat / Anthropic it is replaced by the default model. | 保留 |
| codexConfig.autoReviewModelLabel | 自动审批模型 | 자동 승인 모델 | Auto Review model | 已修订 |
| codexConfig.autoReviewModelHint | Codex 开了自动审批（Approve for me）时，判断操作能不能放行用的模型。审批请求和主对话发给同一家，所以只能选这张卡模型列表里的。聚合模式下不生效，改用聚合页签「聚合设置」里的自动审批模型。改完需要重启 Codex。 | 자동 승인(Approve for me)이 켜져 있을 때 작업 허용 여부를 판단하는 모델입니다. 승인 요청도 주 대화와 같은 공급자로 보내므로 이 카드의 모델 목록에서만 선택할 수 있습니다. 통합 모드에서는 적용되지 않고 통합 탭 설정의 자동 승인 모델을 사용합니다. 변경 후 Codex를 다시 시작하세요. | The model Codex uses to decide whether an action may go ahead when automatic approval (Approve for me) is on. Approval requests go to the same provider as the conversation, so only models in this card's model list can be picked. Ignored in Aggregation mode, where the Auto Review model in the Aggregation tab's settings applies instead. Restart Codex after changes. | 已修订 |
| codexConfig.autoReviewModelCodexDefault | Codex 默认（codex-auto-review） | Codex 기본값(codex-auto-review) | Codex default (codex-auto-review) | 保留 |
| codexConfig.autoReviewModelMainDefault | 主模型自己审批（默认） | 주 모델이 직접 승인 (기본값) | Main model reviews itself (default) | 已修订 |
| codexConfig.autoReviewModelNoList | 这张卡没有模型列表：Codex 会用官方的 codex-auto-review 审批，只有部分转发 ChatGPT 账号的中转认它，不认就会报 404。在上面的模型列表里加上模型后就能选。 | 이 카드에는 모델 목록이 없습니다. Codex는 공식 codex-auto-review로 승인 여부를 판단하며, ChatGPT 계정으로 전달하는 일부 중계 서비스만 이 모델을 지원합니다. 지원하지 않으면 404 오류가 발생합니다. 위 모델 목록에 모델을 추가하면 선택할 수 있습니다. | This card has no model list: Codex reviews approvals with the official codex-auto-review, which only some relays that forward to ChatGPT accounts accept; the rest return 404. Add models to the list above to pick one. | 已修订 |
| codexConfig.modelListHint | 修改后需要重启 Codex。 | 변경 후 Codex를 다시 시작하십시오. | Restart Codex after changes. | 保留 |
| codexConfig.modelListDefaultHelp | 这些模型会出现在 Codex 的 /model 里，第一行是默认模型。名字是官方 GPT 模型的行按官方条目生成，行里的显示名、窗口和思考等级不生效。 | 이 모델은 Codex의 /model 메뉴에 나타납니다. 첫 번째 행은 기본 모델입니다. 공식 GPT 모델의 이름을 딴 행은 공식 항목을 사용하므로 표시 이름, 창 및 추론 수준은 무시됩니다. | These models appear in Codex's /model menu; the first row is the default model. Rows named after an official GPT model use the official entry, so their display name, window and reasoning levels are ignored. | 保留 |
| codexConfig.addCatalogModel | 手动添加 | 수동으로 추가 | Add manually | 保留 |
| codexConfig.modelListTitle | 模型列表 | 모델 목록 | Models | 已修订 |
| codexConfig.stackModelDefaultHelp | 这些模型会出现在 Codex 的 /model 里，选中后请求直达这家。第一行是默认模型：这家被设为默认时，Codex 默认用它。 | 이러한 모델은 Codex의 /model 메뉴에 표시되며 하나를 선택하면 이 공급자에게 바로 요청이 전송됩니다. 첫 번째 행은 기본 모델이며 이 공급자가 기본값인 동안 사용됩니다. | These models appear in Codex's /model menu and picking one sends requests straight to this provider. The first row is the default model, used while this provider is the default. | 已修订 |
| codexConfig.defaultModelNotInList | 默认模型 {{model}} 不在列表里：Codex 默认仍请求它，但 /model 里没有这一项。 | 기본 모델 {{model}}는 목록에 없습니다. Codex는 여전히 기본 모델을 요청하지만 /model에서는 이를 표시하지 않습니다. | The default model {{model}} is not in the list: Codex still requests it by default, but /model won't show it. | 保留 |
| codexConfig.addToModelList | 加入列表 | 목록에 추가 | Add to list | 保留 |
| codexConfig.modelListEmpty | 未配置模型：聚合模式下只发布下面的默认模型。 | 설정된 모델이 없습니다. 통합 모드에서는 아래 기본 모델만 제공됩니다. | No models configured: in Aggregation mode only the default model below is published. | 已修订 |
| codexConfig.catalogDisplayNamePlaceholder | 例如: DeepSeek V4 Flash | 예: DeepSeek V4 Flash | e.g., DeepSeek V4 Flash | 已修订 |
| codexConfig.catalogModelPlaceholder | 例如: deepseek-v4-flash | 예: deepseek-v4-flash | e.g., deepseek-v4-flash | 保留 |
| codexConfig.catalogColumnDisplay | 菜单显示名 | 메뉴 표시 이름 | Menu Display Name | 保留 |
| codexConfig.catalogColumnModel | 实际请求模型 | 실제 요청 모델 | Actual Request Model | 保留 |
| codexConfig.catalogColumnContext | 上下文窗口 | 컨텍스트 창 | Context Window | 保留 |
| codexConfig.catalogColumnReasoning | 思考等级 | 추론 수준 | Reasoning Levels | 保留 |
| codexConfig.reasoningLevelsNotSet | 未设置 | 설정되지 않음 | Not set | 保留 |
| codexConfig.reasoningLevelsSearch | 搜索思考等级... | 추론 수준 검색... | Search reasoning levels... | 保留 |
| codexConfig.reasoningLevelsEmpty | 无等级 | 레벨 없음 | No levels | 保留 |
| codexConfig.defaultReasoningLevelLabel | 默认等级 | 기본 수준 | Default level | 保留 |
| codexConfig.defaultReasoningLevelPlaceholder | 自动 | 자동 | Auto | 保留 |
| codexConfig.defaultReasoningLevelTip | 默认等级：{{level}} | 기본 레벨: {{level}} | Default level: {{level}} | 保留 |
| codexConfig.reasoningModeToggle | 支持思考模式 | 추론 모드 지원 | Supports Thinking Mode | 已修订 |
| codexConfig.reasoningModeHint | 上游 Chat 接口能开关 thinking 时打开，Kimi、GLM、Qwen 等通常属于这一类。 | 업스트림 Chat API에서 thinking을 켜고 끌 수 있을 때 활성화하세요. Kimi, GLM, Qwen 등이 일반적으로 해당합니다. | Turn on when the upstream Chat API can switch thinking on and off. Kimi, GLM and Qwen usually can. | 已修订 |
| codexConfig.reasoningEffortToggle | 支持思考等级 | 추론 수준 조절 지원 | Supports Reasoning Effort | 已修订 |
| codexConfig.reasoningEffortHint | 上游支持 low/high/max 等思考深度时打开。会同时打开思考模式，并把 Codex 的 reasoning.effort 转成上游 Chat 参数。 | 업스트림이 low/high/max 같은 추론 수준을 지원할 때 켜세요. 추론 모드도 함께 켜고 Codex의 reasoning.effort를 업스트림 Chat 매개변수로 변환합니다. | Turn on when the upstream supports thinking depth such as low/high/max. Also turns on thinking mode and maps Codex's reasoning.effort to the upstream Chat parameter. | 已修订 |
| codexConfig.reasoningGroupTitle | 思考能力 | 추론 능력 | Reasoning Capability | 保留 |
| codexConfig.keyFieldsHint | 地址、Key、模型、推理档位、上下文窗口和兼容开关随供应商切换；其余是 Codex 全局设置，保存后对所有供应商生效。 | 엔드포인트, API 키, 모델, 추론 수준, 컨텍스트 창 및 호환성 옵션은 공급자를 전환하면 함께 바뀝니다. 나머지는 Codex 전역 설정이며 저장하면 모든 공급자에 적용됩니다. | The endpoint, key, model, reasoning effort, context window and compatibility switches follow the provider; everything else is a global Codex setting that applies to every provider once saved. | 已修订 |
| codexConfig.inactiveFieldsHint | 这些是旧版存进卡里的设置，现在切换不会写出去。点一下复制 TOML，需要时粘贴到上方。 | 이전 버전에 의해 이 공급자에 저장되었습니다. 전환하면 더 이상 적용되지 않습니다. 하나를 클릭하여 TOML를 복사하고 필요한 경우 위에 붙여넣습니다. | Saved in this provider by an older version; switching no longer applies them. Click one to copy its TOML and paste it above if you need it. | 已修订 |
| codexConfig.inactiveFieldCopied | 已复制 | 복사됨 | Copied | 保留 |
| codexConfig.upstreamFormatCopilotRouteHint | 所有模式都需要开启路由，由路由注入 Copilot 账号凭据；手动指定的协议模型不支持时会报错。 | 모든 모드에는 Copilot 계정 자격 증명을 삽입하는 라우팅이 필요합니다. 명시적으로 선택한 프로토콜은 해당 프로토콜을 지원하지 않는 모델에서는 실패합니다. | Every mode requires routing, which injects the Copilot account credentials. A protocol you pick explicitly fails for models that don't support it. | 保留 |
| codexConfig.maxOutputTokensWarning | 不要超过模型或网关的真实输出上限，否则会返回 400。 | 모델이나 게이트웨이의 실제 출력 한도를 초과하면 요청에 400 오류가 반환됩니다. | Don't exceed the real output limit of the model or gateway, or requests return 400. | 已修订 |
| codexConfig.routeOnlySettingsHint | 以下两项只在路由、聚合模式下生效。 | 아래 두 설정은 라우팅 및 통합 모드에서만 적용됩니다. | The two settings below only apply in routing and Aggregation modes. | 已修订 |
| geminiConfig.envFile | 环境变量 (.env) | 환경 변수(.env) | Environment Variables (.env) | 保留 |
| geminiConfig.envFileHint | 使用 .env 格式配置 Gemini 环境变量 | .env 형식으로 Gemini 환경 변수 설정 | Configure Gemini environment variables in .env format | 已修订 |
| geminiConfig.configJson | 配置文件 (settings.json) | 설정 파일(settings.json) | Settings file (settings.json) | 保留 |
| geminiConfig.configJsonHint | Gemini CLI 的 settings.json（MCP 服务器在 MCP 面板里管理） | Gemini CLI의 settings.json(MCP 서버는 MCP 패널에서 관리됩니다) | Gemini CLI's settings.json (MCP servers are managed in the MCP panel) | 保留 |
| geminiConfig.keyFieldsHint | 地址、Key、模型名和认证方式随供应商切换；其余环境变量和 settings.json 是 Gemini CLI 全局设置，保存后对所有供应商生效。 | 엔드포인트, API 키, 모델 이름 및 인증 방식은 공급자를 전환하면 함께 바뀝니다. 나머지 환경 변수와 settings.json은 Gemini CLI 전역 설정이며 저장하면 모든 공급자에 적용됩니다. | The endpoint, key, model name and auth type follow the provider; the other environment variables and settings.json are Gemini CLI global settings and apply to every provider after saving. | 已修订 |
| geminiConfig.inactiveFieldsHint | 这些是旧版存进卡里的设置，现在切换不会写出去。点一下加入上方，保存后对所有供应商生效。 | 이전 버전에서 이 공급자에 저장한 설정으로, 이제 공급자를 전환해도 적용되지 않습니다. 항목을 선택하여 위에 추가한 후 저장하면 모든 공급자에 적용됩니다. | Saved in this provider by an older version; switching no longer applies them. Click one to add it above; after saving it applies to every provider. | 已修订 |
| geminiConfig.addToGlobalSettings | 加入全局设置 | 전역 설정에 추가 | Add to global settings | 保留 |
| opencode.npmPackage | 接口格式 | API 형식 | API Format | 保留 |
| opencode.nativeConfigHint | 请在下方以 JSON 编辑 OpenCode V2 原生配置。保存时保留供应商和模型字段。 | 아래의 기본 OpenCode V2 설정을 JSON로 편집하세요. 저장 시 공급자 및 모델 필드가 유지됩니다. | Edit native OpenCode V2 configuration as JSON below. Provider and model fields are preserved when saving. | 已修订 |
| opencode.selectPackage | 选择接口格式 | API 형식 선택 | Select API format | 保留 |
| opencode.builtinDefaults | 使用 OpenCode 内置供应商默认值 | OpenCode 내장 공급자 기본값 사용 | Use OpenCode built-in provider defaults | 已修订 |
| opencode.customProviderRequired | 新的供应商标识需要填写 npm 包和至少一个模型；只有配置中已有的同名供应商可以沿用默认定义 | 새 공급자 ID에는 npm 패키지와 하나 이상의 모델이 필요합니다. 라이브 설정의 기존 ID만 기본값을 상속할 수 있습니다. | A new provider ID requires an npm package and at least one model. Only an existing ID in the live config may inherit defaults. | 已修订 |
| opencode.duplicateRequiresDefinition | 此供应商缺少 npm 包或模型定义，无法直接复制。请先补全 npm 包和至少一个模型，再复制为自定义供应商。 | 이 공급자에는 npm 패키지 또는 모델 정의가 누락되어 직접 복제할 수 없습니다. 사용자 정의 공급자로 복사하기 전에 npm 패키지와 하나 이상의 모델을 지정하세요. | This provider is missing an npm package or model definitions and cannot be duplicated directly. Specify an npm package and at least one model before copying it as a custom provider. | 已修订 |
| opencode.duplicateRequiresNativeDefinition | 此 V2 原生供应商缺少 package 或模型定义，无法直接复制。请先补全 package 和至少一个模型，再以新的标识复制。 | 이 기본 V2 공급자에는 패키지 또는 모델 정의가 누락되어 직접 복제할 수 없습니다. 새 ID로 복사하기 전에 패키지와 하나 이상의 모델을 추가하세요. | This native V2 provider is missing a package or model definitions and cannot be duplicated directly. Add a package and at least one model before copying it under a new ID. | 已修订 |
| opencode.nativeCustomProviderRequired | 新的供应商标识需要填写 package 和至少一个模型；只有配置中已有的同名供应商可以沿用默认定义 | 새 공급자 ID에는 패키지와 하나 이상의 모델이 필요합니다. 라이브 설정의 기존 ID만 기본값을 상속할 수 있습니다. | A new provider ID requires a package and at least one model. Only an existing ID in the live config may inherit defaults. | 已修订 |
| opencode.baseUrl | Base URL | 기본 URL | Base URL | 保留 |
| opencode.models | 模型配置 | 모델 | Models | 保留 |
| opencode.addModel | 手动添加 | 수동으로 추가 | Add manually | 保留 |
| opencode.modelId | 模型 ID | 모델 ID | Model ID | 保留 |
| opencode.modelName | 显示名称 | 표시 이름 | Display Name | 保留 |
| opencode.noModels | 暂无模型配置 | 설정된 모델이 없습니다. | No models configured | 已修订 |
| opencode.modelsRequired | 请至少添加一个模型配置 | 모델을 하나 이상 추가하세요. | Please add at least one model | 保留 |
| opencode.toggleModelDetails | 展开或收起模型详情 | 모델 세부 정보 펼치기/접기 | Toggle model details | 已修订 |
| opencode.providerKey | 供应商标识 | 공급자 키 | Provider Key | 已修订 |
| opencode.providerKeyPlaceholder | my-provider | my-provider | my-provider | 保留 |
| opencode.providerKeyHint | 配置文件中的唯一标识符，只能使用小写字母、数字和连字符 | 설정 파일의 고유 식별자입니다. 소문자, 숫자, 하이픈만 사용하세요. | Unique identifier in config file. Use lowercase letters, numbers, and hyphens only. | 已修订 |
| opencode.providerKeyLockedHint | 该供应商已添加到应用配置中，供应商标识不可修改 | 이 공급자는 이미 앱 설정에 추가되었으므로 해당 키를 더 이상 변경할 수 없습니다. | This provider has already been added to the app config, so its key can no longer be changed. | 已修订 |
| opencode.providerKeyRequired | 请填写供应商标识 | 공급자 키가 필요합니다. | Provider key is required | 已修订 |
| opencode.providerKeyDuplicate | 此标识已被使用，请更换 | 이 키는 이미 사용 중입니다. | This key is already in use | 保留 |
| opencode.providerKeyInvalid | 标识格式无效，只能使用小写字母、数字和连字符 | 형식이 잘못되었습니다. 소문자, 숫자, 하이픈만 사용하세요. | Invalid format. Use lowercase letters, numbers, and hyphens only. | 保留 |
| opencode.headers | 请求头 | 헤더 | Headers | 保留 |
| opencode.headersHint | 随供应商请求发送的可选 HTTP 请求头，如 HTTP-Referer 或 X-Title。 | HTTP-Referer 또는 X-Title과 같은 공급자 요청과 함께 전송되는 선택적 HTTP 헤더입니다. | Optional HTTP headers sent with provider requests, such as HTTP-Referer or X-Title. | 已修订 |
| opencode.addHeader | 添加请求头 | 헤더 추가 | Add header | 保留 |
| opencode.headerName | 请求头 | 헤더 | Header | 保留 |
| opencode.headerValue | 值 | 값 | Value | 保留 |
| opencode.headerNamePlaceholder | X-Title | X-Title | X-Title | 已修订 |
| opencode.headerValuePlaceholder | CC Switch | CC Switch | CC Switch | 保留 |
| opencode.removeHeader | 删除请求头 | 헤더 제거 | Remove header | 保留 |
| opencode.noHeaders | 暂无自定义请求头 | 설정된 맞춤 헤더가 없습니다. | No custom headers configured | 已修订 |
| opencode.extraOptions | 额外选项 | 추가 옵션 | Extra Options | 保留 |
| opencode.extraOptionsHint | 配置额外的 SDK 选项，如 timeout、setCacheKey 等。值会自动解析类型（数字、布尔值等）。 | timeout, setCacheKey 등의 추가 SDK 옵션을 설정합니다. 값은 숫자나 불리언 등 알맞은 형식으로 자동 해석됩니다. | Configure extra SDK options like timeout, setCacheKey, etc. Values are auto-parsed to appropriate types (number, boolean, etc.). | 已修订 |
| opencode.addExtraOption | 添加 | 추가 | Add | 已修订 |
| opencode.extraOptionKey | 键名 | 키 | Key | 已修订 |
| opencode.extraOptionValue | 值 | 값 | Value | 保留 |
| opencode.extraOptionKeyPlaceholder | timeout | timeout | timeout | 保留 |
| opencode.extraOptionValuePlaceholder | 600000 | 600000 | 600000 | 保留 |
| opencode.noExtraOptions | 暂无额外选项 | 추가 옵션이 설정되지 않았습니다. | No extra options configured | 已修订 |
| opencode.noModelOptions | 模型选项，点击 + 添加 | 모델 옵션, 추가하려면 +를 클릭하세요. | Model options, click + to add | 保留 |
| opencode.modelLimits | Token 限制 | 토큰 한도 | Token Limits | 保留 |
| opencode.limitContext | 上下文 | 컨텍스트 | Context | 已修订 |
| opencode.limitOutput | 输出 | 출력 | Output | 已修订 |
| opencode.modelExtraFields | 模型属性 | 모델 속성 | Model Properties | 保留 |
| opencode.noModelExtraFields | 模型属性 (variants, cost 等)，点击 + 添加 | 모델 속성(variants, cost 등). +를 눌러 추가하세요 | Model properties (variants, cost, etc.), click + to add | 已修订 |
| opencode.modelExtraFieldKeyPlaceholder | variants | variants | variants | 保留 |
| opencode.sdkOptions | SDK 选项 | SDK 옵션 | SDK Options | 保留 |
| opencode.modelOptionKeyPlaceholder | provider | provider | provider | 保留 |
| opencode.modelOptionValuePlaceholder | {"order": ["baseten"]} | {"order": ["baseten"]} | {"order": ["baseten"]} | 保留 |
| providerPreset.label | 预设供应商 | 공급자 프리셋 | Provider Preset | 已修订 |
| providerPreset.custom | 自定义配置 | 사용자 지정 설정 | Custom Configuration | 已修订 |
| providerPreset.other | 其他 | 기타 | Other | 已修订 |
| providerPreset.hint | 选择预设后可继续调整下方字段。 | 프리셋을 선택한 후에도 아래 필드를 계속해서 조정할 수 있습니다. | You can continue to adjust the fields below after selecting a preset. | 保留 |
| providerPreset.searchTooltip | 搜索预设 | 프리셋 검색 | Search presets | 保留 |
| providerPreset.searchAriaLabel | 搜索预设供应商 | 공급자 프리셋 검색 | Search provider presets | 已修订 |
| providerPreset.searchPlaceholder | 搜索名称或网址，例如 kimi、智谱、openrouter | 이름 또는 URL 검색 (예: kimi, zhipu, openrouter) | Search name or URL, e.g. kimi, zhipu, openrouter | 已修订 |
| providerPreset.sortAriaLabel | 切换预设排序 | 프리셋 정렬 전환 | Toggle preset sorting | 保留 |
| providerPreset.sortNameAscTooltip | 按名称 A-Z 排序 | 이름 A-Z로 정렬 | Sort by name A-Z | 保留 |
| providerPreset.sortOriginalTooltip | 恢复原始顺序 | 원래 순서 복원 | Restore original order | 保留 |
| providerPreset.noSearchResults | 没有匹配的预设供应商。 | 검색어와 일치하는 공급자 프리셋이 없습니다. | No provider presets match your search. | 已修订 |
| providerPreset.clearSearch | 清空搜索 | 검색 지우기 | Clear search | 保留 |
| providerPreset.categoriesLabel | 预设分类 | 프리셋 카테고리 | Preset categories | 保留 |
| providerPreset.group.all | 全部 | 모두 | All | 保留 |
| providerPreset.group.login | 账号登录 | 계정 로그인 | Account sign-in | 保留 |
| providerPreset.group.vendor | 模型厂商 | 모델 공급업체 | Model vendors | 保留 |
| providerPreset.group.thirdparty | 第三方平台 | 타사 플랫폼 | Third-party platforms | 保留 |
| providerPreset.group.cloud | 云服务商 | 클라우드 공급자 | Cloud providers | 已修订 |
| providerPreset.group.local | 本地 | 로컬 | Local | 已修订 |
| providerPreset.group.plugin | 插件配置 | 플러그인 설정 | Plugin configs | 已修订 |
| providerPreset.group.universal | 统一供应商 | 범용 공급자 | Universal providers | 已修订 |
| providerPreset.crossApp | 跨应用 | 앱 전반에 걸쳐 | Across apps | 保留 |
| providerPreset.groupHint.login | 不用 API Key，用已有账号登录。除 Claude 以外都要经过路由。 | API 키 없음: 기존 계정으로 로그인하세요. Claude를 제외한 모든 것은 라우팅을 거칩니다. | No API key: sign in with an existing account. Everything except Claude goes through routing. | 保留 |
| providerPreset.groupHint.vendor | 厂商自己的 API 和编程套餐。同一家的国内站、海外站、套餐合成一行，下一步再选版本。 | 모델 제조사의 공식 API와 코딩 요금제입니다. 같은 업체의 중국 사이트, 글로벌 사이트 및 요금제를 한 행으로 묶었으며 다음 단계에서 버전을 선택합니다. | The vendors' own APIs and coding plans. A vendor's China site, global site and plans share one row; pick the version in the next step. | 已修订 |
| providerPreset.groupHint.thirdparty | 聚合多家模型的平台，或转售官方模型的中转服务。 | 다수의 모델을 모아 놓은 플랫폼이거나, 공식 모델을 재판매하는 중개 플랫폼입니다. | Platforms that aggregate many models, or relays reselling official models. | 保留 |
| providerPreset.groupHint.cloud | 用云厂商账号调用模型。 | 클라우드 공급자 계정으로 모델을 호출합니다. | Call models with a cloud provider account. | 已修订 |
| providerPreset.groupHint.local | 在本机运行的推理服务，先启动服务并下载模型。Key 填占位值即可。 | 이 컴퓨터에서 실행하는 추론 서비스입니다. 먼저 서비스를 시작하고 모델을 다운로드하세요. API 키에는 임의의 자리 표시자 값을 입력하면 됩니다. | Inference servers running on this computer. Start the server and pull a model first; the key is just a placeholder. | 已修订 |
| providerPreset.groupHint.plugin | OpenCode 插件的模型分配配置。 | OpenCode 플러그인에 대한 모델 할당 설정입니다. | Model assignment configs for OpenCode plugins. | 已修订 |
| providerPreset.groupHint.universal | 一次配置，同步到 Claude Code、Codex、Gemini CLI。 | 한 번 설정하면 Claude Code, Codex 및 Gemini CLI에 동기화됩니다. | Configure once, synced to Claude Code, Codex and Gemini CLI. | 已修订 |
| providerPreset.noResults | 没有找到「{{query}}」 | “{{query}}”에 대한 검색 결과가 없습니다. | Nothing found for “{{query}}” | 保留 |
| providerPreset.noResultsHint | 可以用自定义配置，手动填写请求地址和 API Key。 | 사용자 정의 설정을 사용하고 요청 URL과 API 키를 직접 입력할 수 있습니다. | You can use a custom config and fill in the request URL and API key yourself. | 已修订 |
| providerPreset.useCustom | 用自定义配置添加 | 사용자 지정 설정으로 추가 | Add with a custom config | 已修订 |
| providerPreset.customDetail | 手动填写请求地址和 API Key | 요청 URL과 API 키를 직접 입력하세요. | Fill in the request URL and API key yourself | 保留 |
| providerPreset.customBar | 自定义配置 · 手动填写所有字段 | 사용자 지정 설정 · 모든 필드를 직접 입력 | Custom config · fill in every field yourself | 已修订 |
| providerPreset.change | 更换 | 변경 | Change | 已修订 |
| providerPreset.backToPick | 返回选择预设 | 프리셋 선택으로 돌아가기 | Back to presets | 已修订 |
| providerPreset.universalDetail | 同步到 Claude Code、Codex、Gemini CLI | Claude Code, Codex, Gemini CLI에 동기화됨 | Synced to Claude Code, Codex, Gemini CLI | 保留 |
| providerPreset.manageUniversal | 管理已有的统一供应商 › | 기존 범용 공급자 관리 › | Manage existing universal providers › | 已修订 |
| providerPreset.loginWith.kimi | 使用 Kimi 账号登录 | Kimi 계정으로 로그인 | Sign in with a Kimi account | 保留 |
| providerPreset.loginWith.claude | 用 Claude 账号登录 | Claude 계정으로 로그인 | Sign in with a Claude account | 已修订 |
| providerPreset.loginWith.chatgpt | 用 ChatGPT 账号登录 | ChatGPT 계정으로 로그인 | Sign in with a ChatGPT account | 保留 |
| providerPreset.loginWith.github | 用 GitHub 账号登录 | GitHub 계정으로 로그인 | Sign in with a GitHub account | 保留 |
| providerPreset.loginWith.xai | 用 xAI 账号登录 | xAI 계정으로 로그인 | Sign in with an xAI account | 保留 |
| providerPreset.loginWith.google | 用 Google 账号登录 | Google 계정으로 로그인 | Sign in with a Google account | 保留 |
| providerPreset.versionCount | {{domain}} · {{n}} 个版本 | {{domain}} · {{n}} 버전 | {{domain}} · {{n}} versions | 保留 |
| providerPreset.matchedVersion | 匹配：{{name}} | {{name}}와 일치 | Matches {{name}} | 保留 |
| providerPreset.matchedVersions | 匹配：{{name}} 等 {{n}} 个版本 | {{name}} 외 {{more}}개 버전과 일치 | Matches {{name}} and {{more}} more | 已修订 |
| providerPreset.versionLabel | 版本 | 버전 | Version | 保留 |
| providerPreset.family.volcengine | 火山引擎 | Volcengine | Volcengine | 已修订 |
| providerPreset.family.tencent | 腾讯云 | Tencent Cloud | Tencent Cloud | 已修订 |
| providerPreset.switchVersionTitle | 切换到 {{version}}？ | {{version}}로 전환하시겠습니까? | Switch to {{version}}? | 保留 |
| providerPreset.switchVersionMessage | 表单会按新版本重新填写，已填的 API Key 和其他修改会清空。 | 양식은 새 버전으로 다시 작성됩니다. 입력한 API 키와 기타 변경 사항은 모두 지워집니다. | The form will be refilled for the new version. The API key you entered and any other changes will be cleared. | 保留 |
| providerPreset.switchVersionConfirm | 切换 | 전환 | Switch | 已修订 |
| providerPreset.plan.payg | 按量付费 | 종량제 | Pay-as-you-go | 保留 |
| providerPreset.plan.coding | 编程订阅 | 코딩 구독 | Coding subscription | 保留 |
| providerPreset.plan.codingPlan | Coding Plan | Coding Plan | Coding Plan | 已修订 |
| providerPreset.plan.agentPlan | Agent Plan | Agent Plan | Agent Plan | 已修订 |
| providerPreset.plan.tokenPlan | Token Plan | Token Plan | Token Plan | 已修订 |
| providerPreset.plan.enterpriseLite | 企业 Lite | Enterprise Lite | Enterprise Lite | 已修订 |
| providerPreset.plan.enterprisePro | 企业 Pro | Enterprise Pro | Enterprise Pro | 已修订 |
| providerPreset.plan.stepPlan | Step Plan | Step Plan | Step Plan | 已修订 |
| providerPreset.plan.aksk | AKSK | AKSK | AKSK | 保留 |
| providerPreset.plan.apiKey | API Key | API 키 | API Key | 保留 |
| providerPreset.region.cn | 国内 | 중국 | China | 保留 |
| providerPreset.region.intl | 海外 | 글로벌 | Global | 保留 |
| providerPreset.planLabel | 套餐 | 요금제 | Plan | 已修订 |
| providerPreset.regionLabel | 地区 | 지역 | Region | 保留 |
| usage.title | 使用统计 | 사용 통계 | Usage Statistics | 保留 |
| usage.subtitle | 查看 AI 模型的使用情况和成本统计 | AI 모델 사용량 및 비용 통계 보기 | View AI model usage and cost statistics | 保留 |
| usage.today | 24小时 | 24시간 | 24 Hours | 保留 |
| usage.last7days | 7天 | 7일 | 7 Days | 保留 |
| usage.last30days | 30天 | 30일 | 30 Days | 保留 |
| usage.presetToday | 当天 | 오늘 | Today | 保留 |
| usage.preset1d | 近 24 小时 | 지난 24시간 | Last 24 hours | 保留 |
| usage.preset7d | 近 7 天 | 지난 7일 | Last 7 days | 保留 |
| usage.preset14d | 近 14 天 | 지난 14일 | Last 14 days | 保留 |
| usage.preset30d | 近 30 天 | 지난 30일 | Last 30 days | 保留 |
| usage.presetAll | 全部 | 모두 | All | 保留 |
| usage.totalRequests | 总请求数 | 총 요청 | Total Requests | 保留 |
| usage.totalCost | 总成本 | 총 비용 | Total Cost | 保留 |
| usage.cost | 成本 | 비용 | Cost | 保留 |
| usage.unpriced | 未定价 | 가격 없음 | Unpriced | 保留 |
| usage.perMillion | (每百万) | (백만개당) | (per million) | 保留 |
| usage.trends | 使用趋势 | 사용 동향 | Usage Trends | 保留 |
| usage.rangeToday | 过去 24 小时 (按小时) | 지난 24시간(시간별) | Last 24 hours (hourly) | 保留 |
| usage.rangeLast7Days | 过去 7 天 | 지난 7일 | Last 7 days | 保留 |
| usage.rangeLast30Days | 过去 30 天 | 지난 30일 | Last 30 days | 保留 |
| usage.totalTokens | 新生成 Token (Input+Output) | 새 토큰(입력+출력) | New Tokens (Input+Output) | 保留 |
| usage.cacheTokens | 缓存 Token | 캐시 토큰 | Cache Tokens | 保留 |
| usage.realTotal | 真实消耗 Tokens | 처리된 토큰 | Tokens Processed | 保留 |
| usage.realTotalHint | Input + Output + 缓存写入 + 缓存命中 | 입력 + 출력 + 캐시 쓰기 + 캐시 읽기 | Input + Output + Cache Write + Cache Read | 保留 |
| usage.freshInput | 新增输入 | 새로운 입력 | Fresh Input | 保留 |
| usage.cacheHitRate | 缓存命中率 | 캐시 적중률 | Cache Hit Rate | 保留 |
| usage.requestLogs | 请求日志 | 요청 로그 | Request Logs | 保留 |
| usage.providerStats | Provider 统计 | 공급자 통계 | Provider Stats | 已修订 |
| usage.modelStats | 模型统计 | 모델 통계 | Model Stats | 保留 |
| usage.time | 时间 | 시간 | Time | 保留 |
| usage.provider | 供应商 | 공급자 | Provider | 已修订 |
| usage.billingModel | 计费模型 | 청구 모델 | Billing Model | 保留 |
| usage.inputTokens | 输入 | 입력 | Input | 保留 |
| usage.outputTokens | 输出 | 출력 | Output | 已修订 |
| usage.cacheReadTokens | 缓存命中 | 캐시 적중 | Cache Hit | 保留 |
| usage.cacheCreationTokens | 缓存创建 | 캐시 생성 | Cache Creation | 保留 |
| usage.timingInfo | 用时/首字 | 소요 시간/첫 토큰 지연 | Duration/TTFT | 已修订 |
| usage.status | 状态 | 상태 | Status | 保留 |
| usage.multiplier | 倍率 | 배율 | Multiplier | 已修订 |
| usage.requestModel | 请求模型 | 요청 모델 | Request Model | 保留 |
| usage.responseModel | 返回模型 | 응답 모델 | Response Model | 保留 |
| usage.noData | 暂无数据 | 데이터 없음 | No data | 保留 |
| usage.unknownProvider | 未知供应商 | 알 수 없는 공급자 | Unknown Provider | 已修订 |
| usage.sessionProvider.short | 会话日志 | 세션 로그 | Session logs | 保留 |
| usage.sessionProvider.label | {{app}} · 会话日志 | {{app}} · 세션 로그 | {{app}} · Session logs | 保留 |
| usage.sessionProvider.hint | 没开路由时从客户端的会话日志读取，分不出具体是哪家供应商 | 라우팅이 꺼져 있는 동안 클라이언트의 세션 로그를 읽어 공급자를 구분할 수 없습니다. | Read from the client's session logs while routing is off, so the provider can't be told apart | 已修订 |
| usage.stream | 流 | 스트리밍 | Stream | 已修订 |
| usage.nonStream | 非流 | 비스트리밍 | Non-stream | 已修订 |
| usage.source | 来源 | 출처 | Source | 保留 |
| usage.requestsLabel | 次请求 | 요청 | requests | 保留 |
| usage.costLabel | 总成本 | 총 비용 | total cost | 保留 |
| usage.appFilter.all | 全部 | 모두 | All | 保留 |
| usage.appFilter.claude | Claude Code | Claude Code | Claude Code | 保留 |
| usage.appFilter.codex | Codex | Codex | Codex | 保留 |
| usage.appFilter.gemini | Gemini | Gemini | Gemini | 已修订 |
| usage.appFilter.opencode | OpenCode | OpenCode | OpenCode | 保留 |
| usage.appFilter.grokbuild | Grok Build | Grok Build | Grok Build | 保留 |
| usage.appFilter.pi | Pi | Pi | Pi | 保留 |
| usage.appFilter.mcode | MiniMax Code | MiniMax Code | MiniMax Code | 保留 |
| usage.appFilter.label | 按应用筛选 | 앱으로 필터링 | Filter by app | 保留 |
| usage.rawInputLabel | 原始 | 원본 | Raw | 已修订 |
| usage.sessionSync.title | 自动扫描会话记录 | 세션 로그 자동 스캔 | Auto-Scan Session Logs | 已修订 |
| usage.sessionSync.description | 定期扫描各客户端的本地会话记录以统计用量；关闭后仅在手动同步时扫描 | 각 클라이언트의 로컬 세션 로그를 주기적으로 스캔하여 사용량을 추적합니다. 끄면 로그는 수동 동기화 시에만 검사됩니다. | Periodically scans each client's local session logs to track usage; when off, logs are only scanned on manual sync | 保留 |
| usage.sessionSync.syncNow | 立即同步 | 지금 동기화 | Sync Now | 保留 |
| usage.sessionSync.syncCompleted | 同步完成：新增 {{imported}} 条，扫描 {{files}} 个文件，错误 {{errors}} | 동기화 완료: {{imported}}개 가져옴, 파일 {{files}}개 검사, 오류 {{errors}}개 | Sync completed: {{imported}} imported, {{files}} files scanned, {{errors}} errors | 已修订 |
| usage.sessionSync.syncFailed | 会话用量同步失败：{{error}} | 세션 사용량 동기화 실패: {{error}} | Session usage sync failed: {{error}} | 保留 |
| usage.rebuildCodex.title | Codex 用量维护 | Codex 사용량 관리 | Codex Usage Maintenance | 已修订 |
| usage.rebuildCodex.description | 从本地 rollout 日志重新构建 Codex 会话用量 | 로컬 rollout 로그에서 Codex 세션 사용량을 재구성합니다 | Rebuild Codex session usage from local rollout logs | 已修订 |
| usage.rebuildCodex.warning | 重建前会自动备份数据库。若源 JSONL 已删除，对应历史将无法重新导入。 | 데이터베이스가 먼저 백업됩니다. 소스 JSONL이 삭제된 기록은 다시 가져올 수 없습니다. | The database is backed up first. History whose source JSONL has been deleted cannot be re-imported. | 保留 |
| usage.rebuildCodex.action | 重建 Codex 用量 | Codex 사용량 재구성 | Rebuild Codex Usage | 已修订 |
| usage.rebuildCodex.confirmTitle | 确认重建 Codex 用量 | Codex 사용량을 재구성하시겠습니까? | Rebuild Codex usage? | 已修订 |
| usage.rebuildCodex.confirmMessage | 此操作会清除现有 Codex 会话明细与汇总，再从本地 Codex 日志重新导入。<br><br>已删除日志对应的历史将丢失；缺少父 rollout 的 fork 会暂缓导入。 | 기존 Codex 세션 세부 내역과 집계를 지운 후 로컬 Codex 로그에서 다시 가져옵니다.<br><br>로그가 삭제된 기록은 사라집니다. 상위 rollout이 없는 분기 세션은 가져오기를 보류합니다. | This clears existing Codex session details and rollups, then imports them again from local Codex logs.<br><br>History with deleted logs will be lost. Forks whose parent rollout is missing will be deferred. | 已修订 |
| usage.rebuildCodex.confirmAction | 备份并重建 | 백업 및 재구축 | Back Up and Rebuild | 保留 |
| usage.rebuildCodex.completed | 重建完成：导入 {{imported}} 条，错误 {{errors}}，疑似重复 {{suspected}}，暂缓文件 {{deferred}} | 재구성 완료: {{imported}}개 가져옴, 오류 {{errors}}개, 중복 의심 {{suspected}}개, 보류 파일 {{deferred}}개 | Rebuild complete: {{imported}} imported, {{errors}} errors, {{suspected}} suspected duplicates, {{deferred}} deferred files | 已修订 |
| usage.rebuildCodex.failed | Codex 用量重建失败：{{error}} | Codex 사용량 재구성 실패: {{error}} | Codex usage rebuild failed: {{error}} | 已修订 |
| usage.rebuildCodex.actionEllipsis | 重建 Codex 用量 | Codex 사용량 재구성 | Rebuild Codex Usage | 已修订 |
| usage.totalRecords | 共 {{total}} 条记录 | 총 기록 {{total}}개 | {{total}} records total | 已修订 |
| usage.pageSize | 每页 {{count}} 条 | 페이지당 {{count}} | {{count}} per page | 保留 |
| usage.pageSizeLabel | 每页条数 | 페이지당 행 수 | Rows per page | 保留 |
| usage.goToPage | 跳转 | 이동 | Go | 已修订 |
| usage.pageInputPlaceholder | 页码 | 페이지 | Page | 保留 |
| usage.modelPricing | 模型定价 | 모델 가격 | Model Pricing | 保留 |
| usage.loadPricingError | 加载定价数据失败 | 가격 데이터를 로드하지 못했습니다. | Failed to load pricing data | 保留 |
| usage.modelPricingDesc | 配置各模型的 Token 成本 | 각 모델의 토큰 비용 설정 | Configure token costs for each model | 已修订 |
| usage.noPricingData | 暂无定价数据。点击"新增"添加模型定价配置。 | 가격 데이터가 없습니다. 모델 가격 설정을 추가하려면 "추가"를 클릭하세요. | No pricing data. Click "Add" to add model pricing configuration. | 已修订 |
| usage.model | 模型 | 모델 | Model | 保留 |
| usage.pricingModel | 计价模型 | 가격 모델 | Pricing Model | 保留 |
| usage.displayName | 显示名称 | 표시 이름 | Display Name | 保留 |
| usage.inputCost | 输入成本 | 입력 비용 | Input Cost | 已修订 |
| usage.outputCost | 输出成本 | 출력 비용 | Output Cost | 保留 |
| usage.cacheReadCost | 缓存命中 | 캐시 적중 | Cache Hit | 保留 |
| usage.cacheWriteCost | 缓存创建 | 캐시 생성 | Cache Creation | 保留 |
| usage.deleteConfirmTitle | 确认删除 | 삭제 확인 | Confirm Delete | 保留 |
| usage.deleteConfirmDesc | 确定要删除此模型定价配置吗？此操作无法撤销。 | 이 모델 가격을 삭제하시겠습니까? 이 작업은 취소할 수 없습니다. | Are you sure you want to delete this model pricing? This action cannot be undone. | 保留 |
| usage.queryFailed | 查询失败 | 조회 실패 | Query failed | 已修订 |
| usage.refreshUsage | 刷新用量 | 사용량 새로 고침 | Refresh usage | 保留 |
| usage.planUsage | 套餐用量 | 요금제 사용량 | Plan usage | 保留 |
| usage.invalid | 已失效 | 만료됨 | Expired | 保留 |
| usage.total | 总： | 총: | Total: | 保留 |
| usage.used | 已使用： | 사용량: | Used: | 已修订 |
| usage.remaining | 剩余： | 남은 양: | Remaining: | 已修订 |
| usage.justNow | 刚刚 | 방금 | Just now | 保留 |
| usage.minutesAgo | {{count}} 分钟前 | {{count}}분 전 | {{count}} min ago | 保留 |
| usage.hoursAgo | {{count}} 小时前 | {{count}}시간 전 | {{count}} hr ago | 保留 |
| usage.daysAgo | {{count}} 天前 | {{count}}일 전 | {{count}} day ago | 保留 |
| usage.multiplePlans | {{count}} 个套餐 | 요금제 {{count}}개 | {{count}} plans | 已修订 |
| usage.expand | 展开 | 펼치기 | Expand | 保留 |
| usage.collapse | 收起 | 접기 | Collapse | 保留 |
| usage.modelIdPlaceholder | 例如: claude-3-5-sonnet-20241022 | 예: claude-3-5-sonnet-20241022 | e.g., claude-3-5-sonnet-20241022 | 已修订 |
| usage.displayNamePlaceholder | 例如: Claude 3.5 Sonnet | 예: Claude 3.5 Sonnet | e.g., Claude 3.5 Sonnet | 已修订 |
| usage.appType | 应用类型 | 앱 유형 | App Type | 保留 |
| usage.statusCode | 状态码 | 상태 코드 | Status Code | 保留 |
| usage.allSources | 全部来源 | 모든 소스 | All Sources | 保留 |
| usage.allModels | 全部模型 | 모든 모델 | All Models | 保留 |
| usage.filterBySource | 按来源筛选 | 소스별로 필터링 | Filter by source | 保留 |
| usage.filterByModel | 按模型筛选 | 모델별로 필터링 | Filter by model | 保留 |
| usage.refreshInterval | 会话日志扫描间隔 | 세션 로그 검사 간격 | Session log scan interval | 保留 |
| usage.timeRange | 时间范围 | 시간 범위 | Time Range | 保留 |
| usage.customRange | 日历筛选 | 달력 필터 | Calendar Filter | 保留 |
| usage.customRangeHint | 支持日期与时间 | 날짜와 시간을 모두 지원합니다. | Supports both date and time | 保留 |
| usage.startTime | 开始时间 | 시작 시간 | Start Time | 保留 |
| usage.endTime | 结束时间 | 종료 시간 | End Time | 保留 |
| usage.liveEndTime | 结束时间跟随当前时刻 | 종료 시간은 현재 시간을 따릅니다. | End time follows current time | 保留 |
| usage.liveEndTimeNow | 现在 | 지금 | Now | 保留 |
| usage.input | Input | 입력 | Input | 保留 |
| usage.output | Output | 출력 | Output | 已修订 |
| usage.cacheWrite | 创建 | 생성 | Creation | 已修订 |
| usage.cacheWriteNotReported | OpenAI 协议不区分缓存写入，仅上报缓存命中 | OpenAI 프로토콜은 캐시 생성을 구별하지 않습니다. 캐시 적중만 보고됩니다. | OpenAI protocol doesn't distinguish cache creation; only cache hits are reported | 保留 |
| usage.cacheWritePartial | 部分协议（如 OpenAI）不上报缓存写入，数值可能偏低 | 일부 프로토콜(예: OpenAI)은 캐시 생성을 보고하지 않습니다. 값이 불완전할 수 있습니다. | Some protocols (e.g. OpenAI) don't report cache creation; the value may be incomplete | 保留 |
| usage.cacheRead | 命中 | 적중 | Hit | 已修订 |
| usage.baseCost | 基础 | 기본 | Base | 已修订 |
| usage.costMultiplier | 成本倍率 | 비용 배율 | Cost Multiplier | 已修订 |
| usage.withMultiplier | 含倍率 | 배율 포함 | with multiplier | 已修订 |
| usage.requestDetail | 请求详情 | 요청 세부정보 | Request Detail | 保留 |
| usage.requestNotFound | 请求未找到 | 요청을 찾을 수 없습니다 | Request not found | 保留 |
| usage.requestLoadFailed | 请求详情加载失败 | 요청 세부정보를 로드할 수 없습니다. | Couldn't load request details | 保留 |
| usage.basicInfo | 基本信息 | 기본 정보 | Basic Info | 保留 |
| usage.tokenUsage | Token 使用量 | 토큰 사용량 | Token Usage | 已修订 |
| usage.cacheCreationCost | 缓存写入成本 | 캐시 생성 비용 | Cache Creation Cost | 保留 |
| usage.costBreakdown | 成本明细 | 비용 분석 | Cost Breakdown | 保留 |
| usage.performance | 性能信息 | 성능 | Performance | 保留 |
| usage.latency | 延迟 | 지연 시간 | Latency | 已修订 |
| usage.errorMessage | 错误信息 | 오류 메시지 | Error Message | 保留 |
| usage.requests | 请求数 | 요청 수 | Requests | 已修订 |
| usage.tokens | Tokens | 토큰 | Tokens | 保留 |
| usage.avgCost | 平均成本 | 평균 비용 | Average Cost | 保留 |
| usage.avgLatency | 平均延迟 | 평균 지연 시간 | Average Latency | 保留 |
| usage.successRate | 成功率 | 성공률 | Success Rate | 保留 |
| usage.requestId | 请求 ID | 요청 ID | Request ID | 保留 |
| usage.never | 从不 | 안 함 | Never | 保留 |
| usage.modelId | 模型 ID | 모델 ID | Model ID | 保留 |
| usage.modelIdRequired | 模型 ID 不能为空 | 모델 ID가 필요합니다 | Model ID is required | 保留 |
| usage.inputCostPerMillion | 输入成本 (每百万 tokens, USD) | 입력 비용(백만개 토큰당, USD) | Input Cost (per million tokens, USD) | 保留 |
| usage.outputCostPerMillion | 输出成本 (每百万 tokens, USD) | 출력 비용(백만개 토큰당, USD) | Output Cost (per million tokens, USD) | 保留 |
| usage.invalidPrice | 价格必须为非负数 | 가격은 음수가 아니어야 합니다. | Price must be non-negative | 保留 |
| usage.invalidTimeRange | 请选择完整的开始/结束时间 | 전체 시작/종료 시간을 선택하세요. | Please select complete start/end time | 保留 |
| usage.invalidTimeRangeOrder | 开始时间不能晚于结束时间 | 시작 시간은 종료 시간보다 이후일 수 없습니다. | Start time cannot be later than end time | 保留 |
| usage.timeRangeTooLarge | 时间范围过大，请缩小范围 | 시간 범위가 너무 큽니다. 범위를 좁혀주세요. | Time range is too large, please narrow it down | 保留 |
| usage.addPricing | 新增定价 | 가격 추가 | Add Pricing | 保留 |
| usage.editPricing | 编辑定价 | 가격 수정 | Edit Pricing | 保留 |
| usage.pricingAdded | 定价已添加 | 가격이 추가되었습니다 | Pricing added | 保留 |
| usage.pricingUpdated | 定价已更新 | 가격이 업데이트되었습니다. | Pricing updated | 保留 |
| usage.importFromModelsDev | 从 models.dev 导入 | models.dev에서 가져오기 | Import from models.dev | 保留 |
| usage.modelsDevHint | 无需手动填写，可从 models.dev 选择模型定价 | 수동 입력 건너뛰기 — models.dev에서 모델 가격 선택 | Skip manual entry — pick model pricing from models.dev | 保留 |
| usage.modelsDevPickerTitle | 从 models.dev 导入定价 | models.dev에서 요금 가져오기 | Import Pricing from models.dev | 已修订 |
| usage.modelsDevPickerDesc | 选择要导入的模型（价格单位：USD / 百万 tokens），每次导入一个 | 가져올 모델을 선택하세요(백만 토큰당 USD 가격). 가져오기당 하나의 모델입니다. | Select a model to import (prices in USD per million tokens). One model per import. | 保留 |
| usage.modelsDevSearchPlaceholder | 搜索模型或供应商（全量搜索）... | 모델 또는 공급자 검색(전체 검색)... | Search models or providers (full search)... | 已修订 |
| usage.modelsDevAllProviders | 全部供应商 | 모든 공급자 | All providers | 已修订 |
| usage.modelsDevLoadError | 加载 models.dev 数据失败 | models.dev 데이터를 로드하지 못했습니다. | Failed to load models.dev data | 保留 |
| usage.modelsDevRetry | 重试 | 다시 시도 | Retry | 保留 |
| usage.modelsDevImportButton | 导入 | 가져오기 | Import | 保留 |
| usage.modelsDevImporting | 导入中... | 가져오는 중... | Importing... | 保留 |
| usage.modelsDevImported | 已导入 {{name}} 的定价 | {{name}}의 요금을 가져왔습니다 | Imported pricing for {{name}} | 已修订 |
| usage.modelsDevNoResults | 没有匹配的模型 | 일치하는 모델이 없습니다. | No matching models | 保留 |
| usage.modelsDevTruncated | 仅显示前 {{shown}} 条，共 {{total}} 条结果，请缩小搜索范围 | 결과 {{total}}개 중 처음 {{shown}}개만 표시합니다. 검색 범위를 좁혀 주세요 | Showing first {{shown}} of {{total}} results — refine your search | 已修订 |
| usage.modelsDevDefaultHint | 默认展示最新发布的 {{shown}} 个模型（共 {{total}} 个），输入关键字可全量搜索 | {{shown}} 가장 최근에 출시된 모델({{total}} 중) 표시 — 모두 검색하려면 입력하세요. | Showing the {{shown}} most recently released models (of {{total}}) — type to search all | 保留 |
| usage.modelsDevAutoSync.title | 自动同步 models.dev 定价 | 자동 models.dev 가격 동기화 | Automatic models.dev pricing sync | 保留 |
| usage.modelsDevAutoSync.description | 开启后，CC Switch 会在启动时定期拉取所选模型的最新价格，并保存到本地定价文件。 | 켜면 CC Switch 시작 시 선택한 모델의 요금을 주기적으로 가져와 로컬 요금 파일에 저장합니다. | When enabled, periodically fetch selected prices when CC Switch launches and keep them in your local pricing file. | 已修订 |
| usage.modelsDevAutoSync.enabled | 已开启 | 활성화됨 | Enabled | 保留 |
| usage.modelsDevAutoSync.disabled | 已关闭 | 비활성화됨 | Disabled | 保留 |
| usage.modelsDevAutoSync.enableConfirmTitle | 开启自动同步定价？ | 자동 가격 동기화를 활성화하시겠습니까? | Enable automatic pricing sync? | 保留 |
| usage.modelsDevAutoSync.enableConfirmMessage | 开启后，CC Switch 会在启动时定期从 models.dev 更新所选模型的价格（最多每 6 小时一次）。同一模型 ID 的软件内置价格和手动设置价格都会被覆盖。 | 켜면 CC Switch 시작 시 models.dev에서 선택한 모델의 요금을 주기적으로 업데이트합니다 (최대 6시간에 한 번). 같은 모델 ID의 내장 요금과 직접 설정한 요금은 모두 덮어씁니다. | After enabling, CC Switch will periodically update prices for the selected models from models.dev when it launches (at most once every 6 hours). Built-in and manually configured prices with the same model ID will be overwritten. | 已修订 |
| usage.modelsDevAutoSync.enableConfirmAction | 开启自动同步 | 자동 동기화 활성화 | Enable automatic sync | 保留 |
| usage.modelsDevAutoSync.configure | 选择模型 | 모델 선택 | Choose models | 保留 |
| usage.modelsDevAutoSync.configureTitle | 选择自动同步定价的模型 | 자동 가격 동기화를 위한 모델 선택 | Choose models for automatic pricing sync | 保留 |
| usage.modelsDevAutoSync.configureDescription | 通过搜索和供应商筛选选择需要自动更新的模型，选择结果保存在本地。 | 검색과 공급자 필터를 사용하여 가격을 자동 업데이트할 모델을 선택하세요. 선택 결과는 로컬에 저장됩니다. | Search and filter models to update automatically. Your choices are stored locally. | 已修订 |
| usage.modelsDevAutoSync.commonModels | 自动包含常用模型 | 자주 사용하는 모델 자동 포함 | Automatically include common models | 已修订 |
| usage.modelsDevAutoSync.commonModelsDescription | 自动选择 {{count}} 个近期 Claude、GPT、Gemini、Grok、DeepSeek、Qwen、MiMo、LongCat、Kimi、MiniMax 和 GLM 模型。 | {{count}} 최근 Claude, GPT, Gemini, Grok, DeepSeek, Qwen, MiMo, LongCat, Kimi, MiniMax 및 GLM 모델을 선택합니다. | Selects {{count}} recent Claude, GPT, Gemini, Grok, DeepSeek, Qwen, MiMo, LongCat, Kimi, MiniMax, and GLM models. | 保留 |
| usage.modelsDevAutoSync.selectFiltered | 全选筛选结果（{{count}}） | 필터 결과 모두 선택({{count}}) | Select filtered ({{count}}) | 已修订 |
| usage.modelsDevAutoSync.clearFiltered | 清空筛选结果 | 필터링된 항목 선택 해제 | Clear filtered | 已修订 |
| usage.modelsDevAutoSync.selectedCount | 已选择 {{count}} 个模型 | {{count}} 모델 선택됨 | {{count}} models selected | 保留 |
| usage.modelsDevAutoSync.selectionHint | 归一化模型 ID 相同的选项只会导入一次。 | 정규화된 모델 ID가 동일한 선택 항목을 한 번 가져옵니다. | Selections with the same normalized model ID are imported once. | 保留 |
| usage.modelsDevAutoSync.commonBadge | 常用 | 자주 사용 | Common | 已修订 |
| usage.modelsDevAutoSync.selectionSaved | 自动定价同步选择已保存 | 자동 가격 선택이 저장되었습니다. | Automatic pricing selection saved | 保留 |
| usage.modelsDevAutoSync.syncSuccess | 定价同步完成：检查 {{imported}} 个模型，更新 {{changed}} 个 | 가격 동기화 완료: {{imported}} 모델 확인, {{changed}} 업데이트 | Pricing sync complete: {{imported}} models checked, {{changed}} updated | 保留 |
| usage.modelsDevAutoSync.syncFailed | 定价同步失败：{{error}} | 가격 동기화 실패: {{error}} | Pricing sync failed: {{error}} | 保留 |
| usage.modelsDevAutoSync.configLoadFailed | 加载本地定价配置失败：{{error}} | 로컬 요금 설정을 불러오지 못했습니다: {{error}} | Failed to load local pricing configuration: {{error}} | 已修订 |
| usage.modelsDevAutoSync.neverSynced | 从未同步 | 동기화한 적 없음 | Never | 已修订 |
| usage.modelsDevAutoSync.lastSync | 上次同步 | 마지막 동기화 | Last sync | 保留 |
| usage.modelsDevAutoSync.commonStatus | 常用模型 | 자주 사용하는 모델 | Common models | 已修订 |
| usage.modelsDevAutoSync.lastError | 上次自动同步失败：{{error}} | 마지막 자동 동기화 실패: {{error}} | Last automatic sync failed: {{error}} | 保留 |
| usage.modelsDevAutoSync.localFile | 本地定价文件 | 로컬 요금 파일 | Local pricing file | 已修订 |
| usage.modelsDevAutoSync.openFolder | 打开目录 | 폴더 열기 | Open folder | 保留 |
| usage.modelsDevAutoSync.openFolderFailed | 打开本地定价文件目录失败：{{error}} | 로컬 가격 폴더를 열지 못했습니다: {{error}} | Failed to open the local pricing folder: {{error}} | 保留 |
| usage.modelsDevAutoSync.reloadLocalFile | 重新加载文件 | 파일 다시 로드 | Reload file | 保留 |
| usage.modelsDevAutoSync.localFileReloaded | 本地定价文件已重新加载 | 로컬 요금 파일을 다시 불러왔습니다 | Local pricing file reloaded | 已修订 |
| usage.modelsDevAutoSync.localFileReloadFailed | 重新加载本地定价文件失败：{{error}} | 로컬 가격 파일을 다시 로드하지 못했습니다: {{error}} | Failed to reload local pricing file: {{error}} | 保留 |
| usage.modelsDevAutoSync.syncNow | 立即同步 | 지금 동기화 | Sync now | 保留 |
| usage.cacheReadCostPerMillion | 缓存读取成本 (每百万 tokens, USD) | 캐시 읽기 비용(백만 개 토큰당, USD) | Cache Read Cost (per million tokens, USD) | 保留 |
| usage.cacheCreationCostPerMillion | 缓存写入成本 (每百万 tokens, USD) | 캐시 쓰기 비용(백만 개 토큰당, USD) | Cache Write Cost (per million tokens, USD) | 保留 |
| usage.syncStatus.justNow | 刚刚同步 | 방금 동기화됨 | Synced just now | 保留 |
| usage.syncStatus.minutesAgo | {{count}} 分钟前同步 | {{count}}분 전에 동기화됨 | Synced {{count}} min ago | 保留 |
| usage.syncStatus.syncing | 同步中… | 동기화 중… | Syncing… | 保留 |
| usage.syncStatus.tip | 点击立即同步 | 지금 동기화하려면 클릭하세요. | Click to sync now | 保留 |
| usage.syncStatus.tipOff | 自动扫描已关闭，点击立即同步 | 자동 스캔이 꺼져 있습니다. 지금 동기화하려면 클릭하세요. | Auto scan is off. Click to sync now | 保留 |
| usage.refreshMenu.label | 每 {{seconds}} 秒扫描 | {{seconds}}초마다 스캔 | Scan every {{seconds}}s | 已修订 |
| usage.dataSources | 数据来源 | 데이터 소스 | Data sources | 保留 |
| usage.display.title | 显示 | 표시 | Display | 已修订 |
| usage.display.currency | 币种 | 통화 | Currency | 保留 |
| usage.display.rate | 汇率 | 환율 | Exchange rate | 保留 |
| usage.display.rateHint | 手动填写，只用于换算显示；费用仍按美元记录。 | 직접 입력하고 표시용으로만 사용됩니다. 비용은 여전히 ​​USD로 기록됩니다. | Entered by hand and used only for display; costs are still recorded in USD. | 保留 |
| usage.display.rateInvalid | 请输入大于 0 的数字 | 0보다 큰 숫자를 입력하세요. | Enter a number greater than 0 | 保留 |
| usage.display.approxNote | 换算后的金额悬停可看美元原值。 | 변환된 금액에 마우스를 올리면 USD 가치를 확인할 수 있습니다. | Hover a converted amount to see the USD value. | 保留 |
| usage.display.sidebarToday | 侧栏「今日」 | 사이드바 "오늘" | Sidebar "Today" | 保留 |
| usage.display.sidebarTodayItems.cost | 金额 | 비용 | Cost | 保留 |
| usage.display.sidebarTodayItems.tokens | Token | 토큰 | Tokens | 保留 |
| usage.display.sidebarTodayItems.requests | 请求数 | 요청 수 | Requests | 已修订 |
| usage.display.sidebarTodayItems.hitRate | 缓存命中率 | 캐시 적중률 | Cache hit rate | 保留 |
| usage.display.sidebarTodayItems.none | 不显示 | 숨김 | Hidden | 已修订 |
| usage.display.sidebarTodayLimit | 最多选 {{count}} 项 | 최대 {{count}}개 선택 | Pick up to {{count}} | 已修订 |
| usage.display.logColumns | 请求日志的列 | 요청 로그 열 | Request log columns | 保留 |
| usage.display.trendChartType | 趋势图样式 | 추세 차트 | Trend chart | 保留 |
| usage.display.trendChartTypes.bar | 柱形图 | 막대 | Bar | 已修订 |
| usage.display.trendChartTypes.area | 曲线面积图 | 영역 그래프 | Area | 已修订 |
| usage.providerFilter.label | 供应商 | 공급자 | Provider | 已修订 |
| usage.providerFilter.all | 全部供应商 | 모든 공급자 | All providers | 已修订 |
| usage.providerFilter.title | 按供应商筛选 | 공급자별로 필터링 | Filter by provider | 已修订 |
| usage.modelFilter.label | 模型 | 모델 | Model | 保留 |
| usage.modelFilter.title | 按模型筛选（随供应商级联） | 모델별 필터링(공급자 필터를 따름) | Filter by model (follows the provider filter) | 已修订 |
| usage.metrics.label | 指标 | 측정항목 | Metrics | 保留 |
| usage.metrics.more | 更多指标 | 더 많은 지표 | More metrics | 保留 |
| usage.metrics.realTotalHelpTitle | 真实消耗 Tokens 怎么算 | 총 토큰 계산 방법 | How total tokens are counted | 保留 |
| usage.metrics.realTotalHelp | 新增输入 + 输出 + 缓存写入 + 缓存命中。新增输入不含缓存；部分协议（如 OpenAI）不上报缓存写入，这一项可能偏低。 | 새로운 입력 + 출력 + 캐시 쓰기 + 캐시 적중. 새로운 입력에는 캐시가 제외됩니다. 일부 프로토콜(예: OpenAI)은 캐시 쓰기를 보고하지 않으므로 해당 부분이 낮을 수 있습니다. | Fresh input + output + cache writes + cache hits. Fresh input excludes cache; some protocols (such as OpenAI) don't report cache writes, so that part may be low. | 保留 |
| usage.metrics.hitRateHelpTitle | 缓存命中率怎么算 | 캐시 적중률 계산 방법 | How the cache hit rate is calculated | 保留 |
| usage.metrics.hitRateHelp | 缓存命中 ÷（新增输入 + 缓存写入 + 缓存命中）。 | 캐시 적중 ÷ (신규 입력 + 캐시 쓰기 + 캐시 적중). | Cache hits ÷ (fresh input + cache writes + cache hits). | 已修订 |
| usage.heatmap.title | 用量热力图 | 사용량 히트맵 | Usage heatmap | 保留 |
| usage.heatmap.subtitle | 最近 53 周的每日用量；展开后每 53 周一段往前排，各段颜色深浅可以直接对比 | 최근 53주간의 일별 사용량입니다. 이전 기록은 53주 단위로 펼쳐 볼 수 있으며 각 구간의 색상 농도를 직접 비교할 수 있습니다. | Daily usage over the last 53 weeks; earlier usage continues in 53-week spans, with shading comparable across spans | 已修订 |
| usage.heatmap.spanSummary | {{tokens}} Token · {{requests}} 次请求 · {{cost}} | {{tokens}} 토큰 · {{requests}} 요청 · {{cost}} | {{tokens}} tokens · {{requests}} requests · {{cost}} | 保留 |
| usage.heatmap.showMore | 显示更多 | 더 보기 | Show more | 保留 |
| usage.heatmap.showLess | 收起 | 간략히 보기 | Show less | 保留 |
| usage.heatmap.less | 少 | 적음 | Less | 已修订 |
| usage.heatmap.more | 多 | 많음 | More | 已修订 |
| usage.trend.title | 使用趋势 · {{range}} | 사용량 추이 · {{range}} | Usage trend · {{range}} | 已修订 |
| usage.trend.metricLabel | 趋势指标 | 추세 지표 | Trend metric | 保留 |
| usage.trend.requests | 请求 | 요청 수 | Requests | 已修订 |
| usage.trend.tokens | Tokens | 토큰 | Tokens | 保留 |
| usage.trend.cost | 成本 | 비용 | Cost | 保留 |
| usage.trend.requestsLegend | 请求数 | 요청 수 | Requests | 已修订 |
| usage.trend.titleMetric | {{metric}} · {{granularity}} | {{metric}} · {{granularity}} | {{metric}} · {{granularity}} | 保留 |
| usage.trend.hourly | 按小时 | 매시간 | hourly | 保留 |
| usage.trend.daily | 按天 | 일일 | daily | 保留 |
| usage.tabs.label | 明细 | 세부 정보 | Details | 保留 |
| usage.tabs.providers | 供应商 | 공급자 | Providers | 已修订 |
| usage.tabs.models | 模型 | 모델 | Models | 保留 |
| usage.tabs.pricing | 定价 | 가격 | Pricing | 保留 |
| usage.app | 应用 | 앱 | App | 保留 |
| usage.speed | 速度 | 속도 | Speed | 保留 |
| usage.speedValue | {{value}} tok/s | {{value}} tok/s | {{value}} tok/s | 已修订 |
| usage.speedEstimatedValue | ≈ {{value}} tok/s | ≈ {{value}} tok/s | ≈ {{value}} tok/s | 已修订 |
| usage.speedHelpTitle | 速度怎么算 | 속도 계산 방법 | How speed is calculated | 保留 |
| usage.speedHelp | 每秒输出多少 token，从首字算到结束。只算经路由服务、输出不少于 100 token 的请求；思考过程不外露的模型是近似值。带 ≈ 的是没开路由时按会话日志的时间戳估算的：等首字的时间也算在内，所以偏低；只估输出不少于 200 token 的请求。 | 첫 토큰부터 출력이 끝날 때까지의 초당 출력 토큰 수입니다. 라우팅 서비스를 거치고 출력 토큰이 100개 이상인 요청만 계산합니다. 추론 과정을 표시하지 않는 모델에서는 근사치입니다. ≈ 표시는 라우팅을 끈 상태에서 세션 로그 타임스탬프로 추정한 값입니다. 첫 토큰 대기 시간도 포함되어 실제보다 낮게 나오며, 출력 토큰이 200개 이상인 요청만 추정합니다. | Output tokens per second, from the first token to the end. Only requests through the routing service with at least 100 output tokens count; for models that hide their reasoning it's an approximation. A value with ≈ is estimated from session-log timestamps when routing is off: the wait for the first token is included, so the number reads low. Only requests with at least 200 output tokens are estimated. | 已修订 |
| usage.speedSumHelpTitle | 汇总速度怎么算 | 전체 속도 계산 방법 | How overall speed is calculated | 保留 |
| usage.speedSumHelp | 输出 token 总数除以生成时间总和，不是逐条平均，免得短请求把数字带歪。只算经路由服务、输出不少于 100 token 的请求。带 ≈ 的是按会话日志估算的（含首字等待，只估输出不少于 200 token 的请求），这一行没有路由数据时才显示。 | 총 출력 토큰 수를 총 생성 시간으로 나눈 값입니다. 요청별 속도의 평균을 사용하지 않으므로 짧은 요청에 의해 왜곡되지 않습니다. 라우팅 서비스를 거치고 출력 토큰이 100개 이상인 요청만 계산합니다. ≈ 표시는 세션 로그 기반 추정치로, 첫 토큰 대기 시간을 포함하며 출력 토큰이 200개 이상인 요청만 계산합니다. 해당 행에 라우팅 데이터가 없을 때만 표시합니다. | Total output tokens divided by total generation time, not an average of per-request speeds, so short requests don't skew it. Only requests through the routing service with at least 100 output tokens count. A value with ≈ is estimated from session logs (it includes the wait for the first token, and only requests with at least 200 output tokens count) and is shown only when the row has no routed data. | 已修订 |
| usage.firstToken | 首字 | 첫 번째 토큰 | First token | 保留 |
| usage.firstTokenHelpTitle | 首字时间 | 첫 번째 토큰 시간 | First-token time | 保留 |
| usage.firstTokenHelp | 从路由服务收到请求，到上游开始输出的时间。带 ≈ 的是没开路由时按会话日志的时间戳推出来的：起点是上一条日志写盘的时刻，含客户端组装请求的时间，所以偏高；Claude Code 只有回复以思考开头时推得出，Codex 只有新版日志、而且回复不是一开头就调工具时推得出。 | 라우팅 서비스가 요청을 받은 시점부터 업스트림이 출력을 시작할 때까지 걸린 시간입니다. ≈ 표시는 라우팅을 끈 상태에서 세션 로그 타임스탬프로 추정한 값입니다. 이전 로그가 기록된 시점부터 계산하므로 클라이언트의 요청 준비 시간까지 포함되어 실제보다 높게 나옵니다. Claude Code는 응답이 추론으로 시작할 때만, Codex는 최신 형식의 로그에서 응답이 도구 호출로 시작하지 않을 때만 추정할 수 있습니다. | Time from the routing service receiving the request to the upstream starting its output. A value with ≈ is derived from session-log timestamps when routing is off: it starts from when the previous log line was written, so it includes the client's own request preparation and reads high. Claude Code only yields one when the reply starts with thinking; Codex only with newer logs, and not when the reply opens with a tool call. | 已修订 |
| usage.firstTokenSumHelpTitle | 首字时间怎么算 | 첫 번째 토큰 시간 계산 방법 | How first-token time is calculated | 保留 |
| usage.firstTokenSumHelp | 从路由服务收到请求，到上游开始输出的时间。取这一行所有请求的中位数，不会被个别排队、冷启动的慢请求拉高。只算经路由服务、成功的流式请求；超过 30 天、已并入日汇总的请求不计。带 ≈ 的是按会话日志推出来的（偏高，只有部分请求推得出），这一行没有路由数据时才显示。 | 라우팅 서비스가 요청을 받은 시점부터 업스트림이 출력을 시작할 때까지의 시간입니다. 이 행에 속한 요청들의 중앙값을 표시하므로 대기열이나 콜드 스타트 때문에 일부 요청이 느려져도 크게 영향을 받지 않습니다. 라우팅 서비스를 거친 성공한 스트리밍 요청만 계산하며, 30일이 지나 일별 집계에 포함된 요청은 제외합니다. ≈ 표시는 세션 로그 기반 추정치로 실제보다 높게 나오며 일부 요청에서만 계산할 수 있습니다. 해당 행에 라우팅 데이터가 없을 때만 표시합니다. | Time from the routing service receiving a request to the upstream starting its output. The row shows the median across its requests, so an occasional slow request (queueing, cold start) doesn't pull it up. Only successful streaming requests through the routing service count; requests older than 30 days, already folded into daily rollups, don't. A value with ≈ is derived from session logs (it reads high, and only some requests yield one) and is shown only when the row has no routed data. | 已修订 |
| usage.timingTip | 耗时 {{duration}}s · 首字 {{ttft}}s | 소요 시간 {{duration}}초 · 첫 토큰 {{ttft}}초 | Duration {{duration}}s · first token {{ttft}}s | 已修订 |
| usage.estimatedTimingTip | 耗时约 {{duration}}s（按会话日志的时间戳估算，含首字等待） | 약 {{duration}}초 (세션 로그 타임스탬프 기반 추정치, 첫 토큰 대기 포함) | About {{duration}}s (estimated from session-log timestamps, including the wait for the first token) | 已修订 |
| usage.estimatedTimingTipWithFirstToken | 耗时约 {{duration}}s · 首字约 {{ttft}}s（按会话日志的时间戳估算） | 약 {{duration}}초 · 첫 토큰 약 {{ttft}}초 (세션 로그 타임스탬프 기반 추정치) | About {{duration}}s · first token about {{ttft}}s (estimated from session-log timestamps) | 已修订 |
| usage.cacheTip | 缓存命中 {{read}} · 缓存写入 {{write}} | 캐시 적중 {{read}} · 캐시 쓰기 {{write}} | Cache hits {{read}} · cache writes {{write}} | 保留 |
| usage.logColumns.reset | 恢复默认 | 기본값으로 재설정 | Reset to default | 保留 |
| usage.logColumns.cacheWrite | 缓存写入 | 캐시 쓰기 | Cache Write | 保留 |
| usage.logColumns.hitRate | 命中率 | 적중률 | Hit Rate | 保留 |
| usage.logColumns.hitRateTip | 缓存命中 {{read}} / 可缓存输入 {{total}} | 캐시 가능한 입력 {{total}} 중 캐시 적중 {{read}} | Cache hits {{read}} of {{total}} cacheable input | 已修订 |
| usage.logColumns.duration | 总耗时 | 총 시간 | Total Time | 保留 |
| usage.openRequestDetail | 查看请求详情：{{time}} {{provider}} | 요청 세부정보 보기: {{time}} {{provider}} | View request details: {{time}} {{provider}} | 保留 |
| usage.prevPage | 上一页 | 이전 페이지 | Previous page | 保留 |
| usage.nextPage | 下一页 | 다음 페이지 | Next page | 保留 |
| usage.statusFilter.all | 全部状态码 | 모든 상태 코드 | All status codes | 保留 |
| usage.detail.tokensTitle | Tokens 用量 | 토큰 사용량 | Token usage | 已修订 |
| usage.detail.costTitle | 成本明细（{{currency}}） | 비용 분석({{currency}}) | Cost breakdown ({{currency}}) | 保留 |
| usage.detail.performance | 性能 | 성능 | Performance | 保留 |
| usage.detail.source | 来源 | 출처 | Source | 保留 |
| usage.detail.sourceProxy | 路由服务 · 状态码 {{code}} | 라우팅 서비스 · 상태 {{code}} | Routing service · status {{code}} | 保留 |
| usage.detail.total | 合计 | 총 | Total | 保留 |
| usage.detail.firstToken | 首字 | 첫 번째 토큰 | First token | 保留 |
| usage.detail.firstTokenEstimated | 首字（估算） | 첫 토큰 (추정) | First token (estimated) | 已修订 |
| usage.detail.duration | 耗时 | 소요 시간 | Duration | 已修订 |
| usage.detail.durationEstimated | 耗时（估算） | 소요 시간 (추정) | Duration (estimated) | 已修订 |
| usage.detail.speedTooFew | 输出不到 100 token，不算速度 | 출력이 100토큰 미만이므로 속도를 계산하지 않습니다. | Under 100 output tokens, so no speed | 已修订 |
| usage.detail.speedEstimateTooFew | 输出不到 200 token，不估速度 | 출력이 200토큰 미만이므로 속도를 추정하지 않습니다. | Under 200 output tokens, so no estimate | 已修订 |
| usage.detail.noTimingSession | 会话日志没有计时数据 | 세션 로그에는 타이밍 데이터가 없습니다. | Session logs have no timing data | 保留 |
| usage.detail.noFirstToken | 没有首字计时，不算速度 | 첫 토큰 시간 데이터가 없어 속도를 계산하지 않습니다. | No first-token timing, so no speed | 已修订 |
| usage.detail.providerId | 供应商 ID | 공급자 ID | Provider ID | 已修订 |
| usage.sources.scanTitle | 自动扫描会话日志 | 세션 로그를 자동으로 스캔 | Scan session logs automatically | 保留 |
| usage.sources.scanHelpTitle | 会话日志是什么 | 세션 로그란? | What are session logs? | 已修订 |
| usage.sources.scanHelp | 各应用写在本机的会话记录。CC Switch 从里面读取用量，不开路由也有数据。 | 각 앱이 이 컴퓨터에 저장하는 대화 기록입니다. CC Switch가 여기에서 사용량을 읽으므로 라우팅을 사용하지 않아도 데이터가 표시됩니다. | The conversation records each app writes on this computer. CC Switch reads usage from them, so you get data even without routing. | 已修订 |
| usage.sources.coverage | 覆盖 7 个应用：{{apps}} | 7개 앱 포함: {{apps}} | Covers 7 apps: {{apps}} | 保留 |
| usage.sources.cadenceOn | 启动时扫描一次，后台每 10 分钟一次；打开用量页时立即扫描，之后按所选间隔扫描 | 시작 시 한 번, 이후 백그라운드에서 10분마다 스캔합니다. 사용량 페이지를 열면 즉시 스캔한 뒤 선택한 간격으로 계속 스캔합니다 | Scans at startup and every 10 minutes in the background; opening the Usage page scans right away, then at the selected interval | 已修订 |
| usage.sources.cadenceOff | 自动扫描已关闭，只在点「立即同步」时扫描 | 자동 스캔이 꺼져 있습니다. 지금 동기화를 클릭한 경우에만 로그가 검사됩니다. | Auto scan is off; logs are scanned only when you click Sync Now | 保留 |
| usage.sources.unsupported | Hermes、OpenClaw 暂不支持用量统计 | Hermes 및 OpenClaw는 아직 사용 통계를 지원하지 않습니다. | Hermes and OpenClaw don't support usage stats yet | 保留 |
| usage.sources.loggingHelpTitle | 记录请求用量是什么 | 요청 사용량 기록이란? | What does recording request usage do? | 已修订 |
| usage.sources.loggingHelp | 经路由服务的请求逐条记录，带状态码、耗时和首字时间。 | 라우팅 서비스를 통한 각 요청은 상태 코드, 기간 및 첫 번째 토큰까지의 시간과 함께 기록됩니다. | Each request through the routing service is recorded with its status code, duration and time to first token. | 保留 |
| usage.sources.on | 已开启 | 켜짐 | On | 保留 |
| usage.sources.off | 已关闭 | 꺼짐 | Off | 保留 |
| usage.sources.editLogging | 修改「记录请求用量」 | ‘요청 사용량 기록’ 변경 | Change “Record request usage” | 已修订 |
| usage.sources.codexHelpTitle | Codex 用量维护做什么 | Codex 사용량 유지관리란? | What does Codex usage maintenance do? | 已修订 |
| usage.sources.lastSynced | 上次同步：{{time}} | 마지막 동기화: {{time}} | last synced: {{time}} | 保留 |
| usage.empty.title | 还没有用量数据 | 아직 사용량 데이터가 없습니다. | No usage data yet | 保留 |
| usage.empty.body | 会话日志和经路由服务的请求都会记在这里。 | 세션 로그 및 라우팅 서비스를 통한 요청의 사용량이 여기에 표시됩니다. | Usage from session logs and from requests through the routing service shows up here. | 保留 |
| usage.empty.configurePricing | 配置模型定价 | 모델 가격 설정 | Configure model pricing | 已修订 |
| usage.pricing.modelsDevTitle | models.dev 同步 · {{status}} | models.dev 동기화 · {{status}} | models.dev sync · {{status}} | 保留 |
| usage.pricing.modelsDevHelpTitle | models.dev 同步怎么工作 | models.dev 동기화 작동 방식 | How models.dev sync works | 保留 |
| usage.pricing.modelsDevHelp | 启动时拉取所选模型的最新价格，最多每 6 小时一次；可以自动包含常用模型。 | 시작 시 최대 6시간마다 선택한 모델의 최신 가격을 가져옵니다. 공통 모델이 자동으로 포함될 수 있습니다. | Fetches the latest prices for the selected models at startup, at most every 6 hours; common models can be included automatically. | 保留 |
| usage.pricing.lastSync | 上次同步 {{time}} | 마지막 동기화 {{time}} | Last synced {{time}} | 保留 |
| usage.pricing.commonIncluded | 含常用模型 | 자주 사용하는 모델 포함 | includes common models | 已修订 |
| usage.pricing.moreActions | 更多定价操作 | 추가 가격 조치 | More pricing actions | 保留 |
| usage.pricing.billingHelpTitle | 计费默认配置管什么 | 청구 기본값에 따라 제어되는 사항 | What the billing defaults control | 保留 |
| usage.pricing.billingHelp | 只对经路由服务的请求生效。会话日志导入的用量按日志里的模型计价。 | 라우팅 서비스를 통한 요청에만 적용됩니다. 세션 로그에서 가져온 사용량은 로그에 기록된 모델에 따라 가격이 책정됩니다. | Applies only to requests through the routing service. Usage imported from session logs is priced by the model recorded in the log. | 保留 |
| usage.pricing.byResponse | 按返回模型计价 | 응답 모델에 따라 가격 책정 | Priced by response model | 保留 |
| usage.pricing.byRequest | 按请求模型计价 | 요청 모델에 따라 가격 책정 | Priced by request model | 保留 |
| usage.pricing.edit | 修改 | 변경 | Change | 已修订 |
| usage.pricing.tableTitle | 模型定价 · {{count}} | 모델 가격 · {{count}} | Model pricing · {{count}} | 保留 |
| usage.pricing.costHelpTitle | 成本怎么算 | 비용 계산 방법 | How cost is calculated | 保留 |
| usage.pricing.costHelp | 每条请求按模型定价算成本：新增输入、输出、缓存命中、缓存写入各乘对应单价，再相加。 | 각 요청의 가격은 해당 모델에 따라 책정됩니다. 새로운 입력, 출력, 캐시 적중 및 캐시 쓰기에 각각 해당 단가를 곱하고 합산됩니다. | Each request is priced by its model: fresh input, output, cache hits and cache writes are each multiplied by their unit price and added up. | 保留 |
| usage.pricing.unit | USD / 每百万 Tokens | USD / 100만 토큰 | USD / 1M tokens | 保留 |
| usage.pricing.editAria | 编辑 {{name}} 的定价 | {{name}} 가격 편집 | Edit pricing for {{name}} | 保留 |
| usage.pricing.deleteAria | 删除 {{name}} 的定价 | {{name}} 가격 삭제 | Delete pricing for {{name}} | 保留 |
| usage.pricing.cacheWrite | 缓存写入 | 캐시 쓰기 | Cache write | 保留 |
| usage.prevMonth | 上个月 | 지난달 | Previous month | 保留 |
| usage.nextMonth | 下个月 | 다음 달 | Next month | 保留 |
| usage.settings.title | 用量设置 | 사용량 설정 | Usage settings | 已修订 |
| usage.settings.pricingSummary | 按模型设置每百万 Tokens 的价格，可从 models.dev 同步 | 백만 개 토큰당 모델별 가격을 설정하거나 models.dev에서 동기화하세요. | Set per-model prices per million tokens, or sync them from models.dev | 保留 |
| usage.settings.managePricing | 管理定价… | 가격 관리… | Manage pricing… | 保留 |
| usageScript.title | 配置用量查询 | 사용량 조회 설정 | Configure Usage Query | 已修订 |
| usageScript.enableUsageQuery | 启用用量查询 | 사용량 조회 활성화 | Enable usage query | 已修订 |
| usageScript.presetTemplate | 预设模板 | 프리셋 템플릿 | Preset template | 已修订 |
| usageScript.requestUrl | 请求地址 | 요청 URL | Request URL | 保留 |
| usageScript.requestUrlPlaceholder | 例如：https://api.example.com | 예를 들어 https://api.example.com | e.g. https://api.example.com | 保留 |
| usageScript.method | HTTP 方法 | HTTP 방식 | HTTP method | 保留 |
| usageScript.templateCustom | 自定义 | 사용자 지정 | Custom | 保留 |
| usageScript.templateGeneral | 通用模板 | 일반 | General | 保留 |
| usageScript.templateNewAPI | NewAPI | NewAPI | NewAPI | 已修订 |
| usageScript.templateSub2API | Sub2API | Sub2API | Sub2API | 保留 |
| usageScript.templateCopilot | GitHub Copilot | GitHub Copilot | GitHub Copilot | 已修订 |
| usageScript.templateTokenPlan | Token Plan | Token Plan | Token Plan | 已修订 |
| usageScript.templateBalance | 官方 | 공식 | Official | 已修订 |
| usageScript.templateOfficialSubscription | 官方订阅 | 공식 구독 | Official Subscription | 保留 |
| usageScript.copilotAutoAuth | 自动使用 OAuth 认证，无需手动配置凭证 | 자동 OAuth 인증, 수동 자격 증명 필요 없음 | Auto OAuth authentication, no manual credentials needed | 保留 |
| usageScript.tokenPlanHint | 自动使用供应商的 API Key 和 Base URL 查询 Token Plan 额度 | 공급자의 API 키와 기본 URL을 자동으로 사용하여 Token Plan 할당량을 조회합니다 | Automatically uses the provider's API Key and Base URL to query Token Plan quota | 已修订 |
| usageScript.balanceHint | 自动使用供应商的 API Key 查询账户余额 | 공급자의 API 키를 자동으로 사용하여 계정 잔액을 조회합니다. | Automatically uses the provider's API Key to query account balance | 已修订 |
| usageScript.officialSubscriptionHint | 读取本机 CLI 的 OAuth 凭据，并调用官方接口查询订阅额度。默认关闭，只有启用后才会请求。 | 로컬 CLI OAuth 자격 증명을 읽고 공식 API를 호출하여 구독 할당량을 조회합니다. 기본적으로 비활성화되어 있으며 활성화한 후에만 요청합니다. | Reads the local CLI OAuth credentials and calls the official API to query subscription quota. Disabled by default and only requests after you enable it. | 已修订 |
| usageScript.officialSubscriptionHintAgy | 运行 agy 自带的 /usage 命令查询登录账号的额度，不读取登录凭据，每次查询约需 10 秒。默认关闭，只有启用后才会请求。 | agy의 기본 제공 /usage 명령을 실행하여 로그인된 계정의 할당량을 확인합니다. 로그인 자격 증명은 읽혀지지 않습니다. 각 확인에는 약 10초가 소요됩니다. 기본적으로 비활성화되어 있으며 활성화한 후에만 실행됩니다. | Runs agy's built-in /usage command to check the signed-in account's quota. Sign-in credentials are not read; each check takes about 10 seconds. Disabled by default and only runs after you enable it. | 保留 |
| usageScript.resetDate | 重置日期 | 초기화 날짜 | Reset date | 已修订 |
| usageScript.premiumRequests | Premium 请求 | 프리미엄 요청 | Premium Requests | 保留 |
| usageScript.credentialsConfig | 凭证配置 | 자격 증명 | Credentials | 已修订 |
| usageScript.credentialsHint | 留空则自动使用供应商配置 | 공급자 설정을 사용하려면 비워 두세요. | Leave empty to use provider config | 已修订 |
| usageScript.optional | 可选 | 선택 사항 | optional | 已修订 |
| usageScript.apiKeyPlaceholder | 留空则使用供应商的 API Key | 공급자의 API 키를 사용하려면 비워 두세요. | Leave empty to use provider's API Key | 已修订 |
| usageScript.baseUrlPlaceholder | 留空则使用供应商的请求地址 | 공급자의 기본 URL을 사용하려면 비워두세요. | Leave empty to use provider's base URL | 已修订 |
| usageScript.baseUrl | 请求地址 | 기본 URL | Base URL | 保留 |
| usageScript.accessToken | 访问令牌（在个人安全设置里获取） | 액세스 토큰(개인 보안 설정에서 발급) | Access Token | 已修订 |
| usageScript.accessTokenPlaceholder | 在'安全设置'里生成 | '보안 설정'에서 생성 | Generate in 'Security Settings' | 保留 |
| usageScript.userId | 用户 ID | 사용자 ID | User ID | 保留 |
| usageScript.userIdPlaceholder | 例如：114514 | 예: 114514 | e.g., 114514 | 保留 |
| usageScript.accessKeyId | AccessKey ID | AccessKey ID | AccessKey ID | 已修订 |
| usageScript.secretAccessKey | SecretAccessKey | SecretAccessKey | SecretAccessKey | 已修订 |
| usageScript.volcengineAkSkHint | 火山用量查询需账号级 AccessKey ID / Secret（与推理 API Key 不同）。请在火山引擎控制台右上角账号菜单 →「API访问密钥」中创建。 | Volcengine 사용 조회에는 계정 수준 AccessKey ID/Secret(추론 API 키와 다름)이 필요합니다. 오른쪽 상단 계정 메뉴 → 'API 액세스 키'를 통해 Volcengine 콘솔에서 생성하세요. | Volcengine usage query needs an account-level AccessKey ID / Secret (different from the inference API key). Create them in the Volcengine console via the top-right account menu → 'API Access Keys'. | 已修订 |
| usageScript.volcengineKeyConsoleLink | 密钥创建地址： | 다음 위치에서 키를 생성하세요. | Create keys at: | 保留 |
| usageScript.zhipuTeamHint | 智谱团队套餐用量查询需团队 API Key（沿用本供应商凭据）+ 组织 ID + 项目 ID（作为请求头 bigmodel-organization / bigmodel-project）。组织与项目 ID 可在团队管理后台用量页的 URL 中找到。 | Zhipu 팀 계획 사용 조회에는 팀 API 키(이 공급자의 자격 증명 재사용) + 조직 ID + 프로젝트 ID(bigmodel-organization / bigmodel-project 요청 헤더로 전송됨)가 필요합니다. 팀 관리 콘솔의 사용 페이지 URL에서 조직 및 프로젝트 ID를 찾으세요. | Zhipu team plan usage query needs the team API key (reuses this provider's credentials) + organization ID + project ID (sent as bigmodel-organization / bigmodel-project request headers). Find the organization and project IDs in the team admin console's usage page URL. | 已修订 |
| usageScript.zhipuTeamConsoleLink | 团队用量页： | 팀 사용 페이지: | Team usage page: | 保留 |
| usageScript.organizationId | 组织 ID | 조직 ID | Organization ID | 保留 |
| usageScript.organizationIdPlaceholder | 例如：org-xxxxxx | 예: org-xxxxxx | e.g. org-xxxxxx | 已修订 |
| usageScript.projectId | 项目 ID | 프로젝트 ID | Project ID | 保留 |
| usageScript.projectIdPlaceholder | 例如：proj-xxxxxx | 예: proj-xxxxxx | e.g. proj-xxxxxx | 已修订 |
| usageScript.defaultPlan | 默认套餐 | 기본 요금제 | Default Plan | 已修订 |
| usageScript.queryFailedMessage | 查询失败 | 조회 실패 | Query failed | 已修订 |
| usageScript.queryScript | 查询脚本（JavaScript） | 조회 스크립트(JavaScript) | Query script (JavaScript) | 已修订 |
| usageScript.timeoutSeconds | 超时时间（秒） | 시간 초과(초) | Timeout (seconds) | 保留 |
| usageScript.headers | 请求头 | 헤더 | Headers | 保留 |
| usageScript.body | 请求 Body | 본문 | Body | 已修订 |
| usageScript.timeoutHint | 范围: 2-30 秒 | 범위: 2~30초 | Range: 2-30 seconds | 保留 |
| usageScript.timeoutMustBeInteger | 超时时间必须为整数，小数部分已忽略 | 시간 초과는 정수여야 하며 소수 부분은 무시됩니다. | Timeout must be an integer, decimal part ignored | 保留 |
| usageScript.timeoutCannotBeNegative | 超时时间不能为负数 | 시간 초과는 음수일 수 없습니다. | Timeout cannot be negative | 保留 |
| usageScript.autoIntervalMinutes | 自动查询间隔（分钟，0 表示不自动查询） | 자동 조회 간격 (분, 0이면 사용 안 함) | Auto query interval (minutes, 0 to disable) | 已修订 |
| usageScript.autoQueryInterval | 自动查询间隔（分钟） | 자동 조회 간격 (분) | Auto Query Interval (minutes) | 已修订 |
| usageScript.autoQueryIntervalHint | 0 表示不自动查询，建议 5-60 分钟 | 0은 비활성화합니다. 5~60분 권장 | 0 to disable; recommend 5-60 minutes | 保留 |
| usageScript.intervalMustBeInteger | 自动查询间隔必须为整数，小数部分已忽略 | 간격은 정수여야 하며 소수 부분은 무시됩니다. | Interval must be an integer, decimal part ignored | 保留 |
| usageScript.intervalCannotBeNegative | 自动查询间隔不能为负数 | 간격은 음수일 수 없습니다. | Interval cannot be negative | 保留 |
| usageScript.intervalAdjusted | 自动查询间隔已调整为 {{value}} 分钟 | 간격이 {{value}}분으로 조정되었습니다. | Interval adjusted to {{value}} minutes | 保留 |
| usageScript.scriptHelp | 脚本编写说明： | 스크립트 작성 지침: | Script writing instructions: | 保留 |
| usageScript.configFormat | 配置格式： | 설정 형식: | Configuration format: | 已修订 |
| usageScript.commentOptional | 可选 | 선택 사항 | optional | 已修订 |
| usageScript.commentResponseIsJson | response 是 API 返回的 JSON 数据 | response는 API가 반환하는 JSON 데이터입니다 | response is the JSON data returned by the API | 已修订 |
| usageScript.extractorFormat | extractor 返回格式（所有字段均为可选）： | extractor 반환 형식 (모든 필드 선택 사항): | Extractor return format (all fields optional): | 已修订 |
| usageScript.tips | 💡 提示： | 💡 팁: | 💡 Tips: | 保留 |
| usageScript.testing | 测试中... | 테스트 중... | Testing... | 保留 |
| usageScript.testScript | 测试脚本 | 테스트 스크립트 | Test script | 保留 |
| usageScript.format | 格式化 | 포맷팅 | Format | 已修订 |
| usageScript.saveConfig | 保存配置 | 설정 저장 | Save config | 已修订 |
| usageScript.scriptEmpty | 脚本配置不能为空 | 스크립트 설정은 비워둘 수 없습니다. | Script configuration cannot be empty | 已修订 |
| usageScript.mustHaveReturn | 脚本必须包含 return 语句 | 스크립트에는 return 문이 포함되어야 합니다. | Script must contain return statement | 保留 |
| usageScript.testSuccess | 测试成功！ | 테스트 성공! | Test successful! | 保留 |
| usageScript.testFailed | 测试失败 | 테스트 실패 | Test failed | 保留 |
| usageScript.formatSuccess | 格式化成功 | 포맷팅이 완료되었습니다 | Format successful | 已修订 |
| usageScript.formatFailed | 格式化失败 | 포맷팅 실패 | Format failed | 已修订 |
| usageScript.supportedVariables | 支持的变量 | 지원되는 변수 | Supported Variables | 保留 |
| usageScript.variablesHint | 支持变量: {{apiKey}}, {{baseUrl}} \| extractor 函数接收 API 响应的 JSON 对象 | 지원 변수: {{apiKey}}, {{baseUrl}} \| extractor 함수는 API 응답 JSON 객체를 받습니다 | Supported variables: {{apiKey}}, {{baseUrl}} \| extractor function receives API response JSON object | 已修订 |
| usageScript.scriptConfig | 请求配置 | 요청 설정 | Request configuration | 已修订 |
| usageScript.extractorCode | 提取器代码 | 추출기 코드 | Extractor code | 保留 |
| usageScript.extractorHint | 返回对象需包含剩余额度等字段 | 반환 객체에는 남은 할당량 등의 필드가 포함되어야 합니다. | Return object should include remaining quota fields | 已修订 |
| usageScript.fieldIsValid | • isValid: 布尔值，套餐是否有效 | • isValid: 불리언, 요금제의 유효 여부 | • isValid: Boolean, whether plan is valid | 已修订 |
| usageScript.fieldInvalidMessage | • invalidMessage: 字符串，失效原因说明（当 isValid 为 false 时显示） | • invalidMessage: 문자열, 만료 사유 (isValid가 false일 때 표시됨) | • invalidMessage: String, reason for expiration (shown when isValid is false) | 保留 |
| usageScript.fieldRemaining | • remaining: 数字，剩余额度 | • remaining: 숫자, 남은 할당량 | • remaining: Number, remaining quota | 已修订 |
| usageScript.fieldUnit | • unit: 字符串，单位（如 "USD"） | • unit: 문자열, 단위(예: "USD") | • unit: String, unit (e.g., "USD") | 保留 |
| usageScript.fieldPlanName | • planName: 字符串，套餐名称 | • planName: 문자열, 요금제 이름 | • planName: String, plan name | 已修订 |
| usageScript.fieldTotal | • total: 数字，总额度 | • total: 숫자, 총 할당량 | • total: Number, total quota | 已修订 |
| usageScript.fieldUsed | • used: 数字，已用额度 | • used: 숫자, 사용된 할당량 | • used: Number, used quota | 保留 |
| usageScript.fieldExtra | • extra: 字符串，扩展字段，可自由补充需要展示的文本 | • extra: 문자열, 사용자 정의 표시 텍스트 | • extra: String, custom display text | 保留 |
| usageScript.tip1 | • 变量 {{apiKey}} 和 {{baseUrl}} 会自动替换 | • 변수 {{apiKey}} 및 {{baseUrl}}는 자동으로 대체됩니다. | • Variables {{apiKey}} and {{baseUrl}} are automatically replaced | 保留 |
| usageScript.tip2 | • extractor 函数在沙箱环境中执行，支持 ES2020+ 语法 | • extractor 함수는 샌드박스 환경에서 실행되며 ES2020+ 문법을 지원합니다 | • Extractor function runs in sandbox environment, supports ES2020+ syntax | 已修订 |
| usageScript.tip3 | • 整个配置必须用 () 包裹，形成对象字面量表达式 | • 객체 리터럴 표현식을 형성하려면 전체 설정을 ()로 묶어야 합니다. | • Entire config must be wrapped in () to form object literal expression | 已修订 |
| dbUpgrade.title | 数据库版本过新 | 데이터베이스 버전이 너무 최신입니다. | Database version is too new | 保留 |
| dbUpgrade.description | 当前数据库由更新版本的 CC Switch 创建，需要升级应用后才能继续使用。升级不会删除你的数据。 | 이 데이터베이스는 최신 버전의 CC Switch에 의해 생성되었습니다. 계속하려면 앱을 업그레이드하세요. 업그레이드해도 데이터는 삭제되지 않습니다. | This database was created by a newer version of CC Switch. Upgrade the app to continue. Upgrading will not delete your data. | 保留 |
| dbUpgrade.versionInfo | 数据库版本 v{{db}} · 应用支持 v{{supported}} | 데이터베이스 v{{db}} · 앱은 v{{supported}}을(를) 지원합니다 | Database v{{db}} · App supports v{{supported}} | 已修订 |
| dbUpgrade.dbPath | 数据库文件 | 데이터베이스 파일 | Database file | 保留 |
| dbUpgrade.checking | 正在检查可用更新… | 사용 가능한 업데이트를 확인하는 중… | Checking for available updates… | 保留 |
| dbUpgrade.updateAvailable | 发现新版本 v{{version}}，升级后即可继续使用。 | 버전 v{{version}}을(를) 사용할 수 있습니다. 업그레이드하면 계속할 수 있습니다. | Version v{{version}} is available; upgrading will let you continue. | 已修订 |
| dbUpgrade.incompatibleTitle | 升级也无法解决 | 업그레이드해도 이 문제가 해결되지 않습니다 | Upgrading won't fix this | 保留 |
| dbUpgrade.incompatibleDescription | 你已是最新版本，但数据库版本（v{{db}}）仍高于本应用支持的版本（v{{supported}}）。该数据库可能由第三方客户端或更高版本创建，升级当前官方应用也无法兼容。 | 이미 최신 버전을 사용하고 있지만 데이터베이스(v{{db}})는 이 앱이 지원하는 것(v{{supported}})보다 여전히 최신 버전입니다. 타사 클라이언트나 최신 빌드에서 생성되었을 가능성이 높으므로 공식 앱을 업그레이드해도 호환되지 않습니다. | You are already on the latest version, but the database (v{{db}}) is still newer than this app supports (v{{supported}}). It was likely created by a third-party client or a newer build, so upgrading the official app cannot make it compatible. | 保留 |
| dbUpgrade.preparing | 正在准备更新… | 업데이트 준비 중… | Preparing update… | 保留 |
| dbUpgrade.downloading | 正在下载更新… | 업데이트 다운로드 중… | Downloading update… | 保留 |
| dbUpgrade.upgradeNow | 升级应用 | 앱 업그레이드 | Upgrade app | 保留 |
| dbUpgrade.retry | 重试升级 | 업그레이드 재시도 | Retry upgrade | 保留 |
| dbUpgrade.openReleases | 打开发布页 | 릴리스 페이지 열기 | Open releases page | 保留 |
| dbUpgrade.openConfigDir | 打开配置目录 | 설정 폴더 열기 | Open config folder | 已修订 |
| dbUpgrade.quit | 退出 | 종료 | Quit | 已修订 |
| errors.usage_query_failed | 用量查询失败 | 사용량 조회 실패 | Usage query failed | 已修订 |
| errors.configLoadFailedTitle | 配置加载失败 | 설정 로드 실패 | Configuration Load Failed | 已修订 |
| errors.configLoadFailedMessage | 无法读取配置文件：<br>{{path}}<br><br>错误详情：<br>{{detail}}<br><br>请手动检查 JSON 是否有效，或从同目录的备份文件（如 config.json.bak）恢复。<br><br>应用将退出以便您进行修复。 | 설정 파일을 읽을 수 없습니다:<br>{{path}}<br><br>오류 세부정보:<br>{{detail}}<br><br>JSON이 유효한지 직접 확인하거나 같은 디렉터리의 백업 파일(예: config.json.bak)에서 복원하세요.<br><br>문제를 수정할 수 있도록 앱이 종료됩니다. | Unable to read configuration file:<br>{{path}}<br><br>Error details:<br>{{detail}}<br><br>Please check if the JSON is valid, or restore from a backup file (e.g., config.json.bak) in the same directory.<br><br>The app will exit so you can fix this. | 已修订 |
| errors.frontendCrashTitle | 界面遇到了问题 | 인터페이스에 문제가 발생했습니다. | Something went wrong in the interface | 保留 |
| errors.frontendCrashMessage | 已尝试将错误信息写入应用诊断日志。请重新加载界面；如果问题持续，请在提交 Issue 时附上日志。 | 오류를 앱 진단 로그에 기록하려고 시도했습니다. 인터페이스를 다시 불러오세요. 문제가 계속되면 Issue를 제출할 때 로그를 첨부하세요. | An attempt was made to write the error to the application diagnostic log. Reload the interface, and attach the log when opening an issue if the problem continues. | 已修订 |
| errors.reloadInterface | 重新加载界面 | 인터페이스 새로고침 | Reload interface | 保留 |
| presetSelector.title | 选择配置类型 | 설정 유형 선택 | Select Configuration Type | 已修订 |
| presetSelector.custom | 自定义 | 사용자 지정 | Custom | 保留 |
| presetSelector.customDescription | 手动配置供应商，需要填写完整的配置信息 | 공급자를 수동으로 설정하고 전체 설정이 필요함 | Manually configure provider, requires complete configuration | 已修订 |
| presetSelector.officialDescription | 官方登录，不需要填写 API Key | 공식 로그인, API 키 필요 없음 | Official login, no API Key required | 保留 |
| presetSelector.presetDescription | 使用预设配置，只需填写 API Key | 프리셋 설정 사용, API 키만 필요 | Use preset configuration, only API Key required | 已修订 |
| mcp.title | MCP 管理 | MCP 관리 | MCP Management | 保留 |
| mcp.import | 导入 | 가져오기 | Import | 保留 |
| mcp.importExisting | 导入已有 | 기존 가져오기 | Import Existing | 保留 |
| mcp.addMcp | 添加MCP | MCP 추가 | Add MCP | 保留 |
| mcp.claudeTitle | Claude Code MCP 管理 | Claude Code MCP 관리 | Claude Code MCP Management | 保留 |
| mcp.codexTitle | Codex MCP 管理 | Codex MCP 관리 | Codex MCP Management | 保留 |
| mcp.geminiTitle | Gemini MCP 管理 | Gemini MCP 관리 | Gemini MCP Management | 保留 |
| mcp.unifiedPanel.title | MCP 服务器管理 | MCP 서버 관리 | MCP Server Management | 保留 |
| mcp.unifiedPanel.addServer | 添加服务器 | 서버 추가 | Add Server | 保留 |
| mcp.unifiedPanel.editServer | 编辑服务器 | 서버 편집 | Edit Server | 保留 |
| mcp.unifiedPanel.deleteServer | 删除服务器 | 서버 삭제 | Delete Server | 保留 |
| mcp.unifiedPanel.deleteConfirm | 确定要删除服务器 "{{id}}" 吗？此操作无法撤销。 | 정말로 "{{id}}" 서버를 삭제하시겠습니까? 이 작업은 취소할 수 없습니다. | Are you sure you want to delete server "{{id}}"? This action cannot be undone. | 保留 |
| mcp.unifiedPanel.noServers | 暂无服务器 | 아직 서버가 없습니다 | No servers yet | 保留 |
| mcp.unifiedPanel.enabledApps | 启用的应用 | 활성화된 앱 | Enabled Apps | 保留 |
| mcp.unifiedPanel.noImportFound | 未发现需要导入的 MCP 服务器。所有服务器已在 CC Switch 统一管理中。 | 가져올 MCP 서버를 찾을 수 없습니다. 모든 서버는 이미 CC Switch에 의해 관리됩니다. | No MCP servers to import found. All servers are already managed by CC Switch. | 保留 |
| mcp.unifiedPanel.importSuccess | 成功导入 {{count}} 个 MCP 服务器 | {{count}} MCP 서버를 성공적으로 가져왔습니다. | Successfully imported {{count}} MCP servers | 保留 |
| mcp.unifiedPanel.searchPlaceholder | 搜索 MCP 名称、描述、标签或命令... | MCP 이름, 설명, 태그 또는 명령 검색... | Search MCP name, description, tag, or command... | 保留 |
| mcp.unifiedPanel.searchAriaLabel | 搜索已管理的 MCP 服务器 | 관리형 MCP 서버 검색 | Search managed MCP servers | 保留 |
| mcp.unifiedPanel.noSearchResults | 未找到匹配的 MCP 服务器 | 검색과 일치하는 MCP 서버가 없습니다. | No MCP servers match your search | 保留 |
| mcp.unifiedPanel.apps.claude | Claude | Claude | Claude | 已修订 |
| mcp.unifiedPanel.apps.codex | Codex | Codex | Codex | 保留 |
| mcp.unifiedPanel.apps.gemini | Gemini | Gemini | Gemini | 已修订 |
| mcp.unifiedPanel.apps.grokbuild | Grok Build | Grok Build | Grok Build | 保留 |
| mcp.unifiedPanel.apps.opencode | OpenCode | OpenCode | OpenCode | 保留 |
| mcp.unifiedPanel.apps.openclaw | OpenClaw | OpenClaw | OpenClaw | 保留 |
| mcp.unifiedPanel.apps.hermes | Hermes | Hermes | Hermes | 保留 |
| mcp.unifiedPanel.apps.mcode | MiniMax Code | MiniMax Code | MiniMax Code | 保留 |
| mcp.userLevelPath | 用户级 MCP 配置路径 | 사용자 수준 MCP 경로 | User-level MCP path | 保留 |
| mcp.serverList | 服务器列表 | 서버 | Servers | 保留 |
| mcp.loading | 加载中... | 로드 중... | Loading... | 保留 |
| mcp.empty | 暂无 MCP 服务器 | MCP 서버 없음 | No MCP servers | 保留 |
| mcp.emptyDescription | 点击右上角按钮添加第一个 MCP 服务器 | 첫 번째 MCP 서버를 추가하려면 오른쪽 상단에 있는 버튼을 클릭하세요. | Click the button in the top right to add your first MCP server | 保留 |
| mcp.add | 添加 MCP | MCP 추가 | Add MCP | 保留 |
| mcp.addServer | 新增 MCP | MCP 추가 | Add MCP | 保留 |
| mcp.editServer | 编辑 MCP | MCP 편집 | Edit MCP | 保留 |
| mcp.addClaudeServer | 新增 Claude Code MCP | Claude Code MCP 추가 | Add Claude Code MCP | 保留 |
| mcp.editClaudeServer | 编辑 Claude Code MCP | Claude Code MCP 편집 | Edit Claude Code MCP | 保留 |
| mcp.addCodexServer | 新增 Codex MCP | Codex MCP 추가 | Add Codex MCP | 保留 |
| mcp.editCodexServer | 编辑 Codex MCP | Codex MCP 편집 | Edit Codex MCP | 保留 |
| mcp.configPath | 配置路径 | 설정 경로 | Config Path | 已修订 |
| mcp.serverCount | 已配置 {{count}} 个 MCP 服务器 | {{count}} MCP 서버 설정됨 | {{count}} MCP server(s) configured | 已修订 |
| mcp.enabledCount | 已启用 {{count}} 个 | {{count}} 활성화됨 | {{count}} enabled | 保留 |
| mcp.template.fetch | 快速模板：mcp-fetch | 빠른 템플릿: mcp-fetch | Quick Template: mcp-fetch | 保留 |
| mcp.form.title | MCP 标题（唯一） | MCP 제목(고유) | MCP Title (Unique) | 保留 |
| mcp.form.titlePlaceholder | my-mcp-server | my-mcp-server | my-mcp-server | 已修订 |
| mcp.form.name | 显示名称 | 표시 이름 | Display Name | 保留 |
| mcp.form.namePlaceholder | 例如 mcp-server-time | 예: mcp-server-time | e.g. mcp-server-time | 已修订 |
| mcp.form.enabledApps | 启用到应用 | 앱에 활성화 | Enable to Apps | 保留 |
| mcp.form.noAppsWarning | 至少选择一个应用 | 앱을 하나 이상 선택해야 합니다. | At least one app must be selected | 保留 |
| mcp.form.description | 描述 | 설명 | Description | 保留 |
| mcp.form.descriptionPlaceholder | 可选的描述信息 | 선택적 설명 | Optional description | 保留 |
| mcp.form.tags | 标签（逗号分隔） | 태그(쉼표로 구분) | Tags (comma separated) | 保留 |
| mcp.form.tagsPlaceholder | stdio, time, utility | stdio, time, utility | stdio, time, utility | 已修订 |
| mcp.form.homepage | 主页链接 | 홈페이지 | Homepage | 保留 |
| mcp.form.homepagePlaceholder | https://example.com | https://example.com | https://example.com | 保留 |
| mcp.form.docs | 文档链接 | 문서 | Docs | 保留 |
| mcp.form.docsPlaceholder | https://example.com/docs | https://example.com/docs | https://example.com/docs | 保留 |
| mcp.form.additionalInfo | 附加信息 | 추가 정보 | Additional Info | 保留 |
| mcp.form.jsonConfig | 完整的 JSON 配置 | 전체 JSON 설정 | Full JSON Configuration | 已修订 |
| mcp.form.jsonConfigOrPrefix | 完整的 JSON 配置或者使用 | 전체 JSON 설정 또는 사용 | Full JSON configuration or use | 已修订 |
| mcp.form.tomlConfigOrPrefix | 完整的 TOML 配置或者使用 | 전체 TOML 설정 또는 사용 | Full TOML configuration or use | 已修订 |
| mcp.form.jsonPlaceholder | {<br>  "type": "stdio",<br>  "command": "uvx",<br>  "args": ["mcp-server-fetch"]<br>} | {<br>  "type": "stdio",<br>  "command": "uvx",<br>  "args": ["mcp-server-fetch"]<br>} | {<br>  "type": "stdio",<br>  "command": "uvx",<br>  "args": ["mcp-server-fetch"]<br>} | 已修订 |
| mcp.form.tomlConfig | 完整的 TOML 配置 | 전체 TOML 설정 | Full TOML Configuration | 已修订 |
| mcp.form.tomlPlaceholder | type = "stdio"<br>command = "uvx"<br>args = ["mcp-server-fetch"] | type = "stdio"<br>command = "uvx"<br>args = ["mcp-server-fetch"] | type = "stdio"<br>command = "uvx"<br>args = ["mcp-server-fetch"] | 已修订 |
| mcp.form.useWizard | 配置向导 | 설정 마법사 | Config Wizard | 已修订 |
| mcp.form.syncOtherSide | 同步到 {{target}} | {{target}}에 동기화 | Mirror to {{target}} | 已修订 |
| mcp.form.syncOtherSideHint | 勾选后会把当前配置同时写入 {{target}}，若存在同名配置将被覆盖 | {{target}}에도 동일한 설정을 적용합니다. 동일한 ID를 가진 기존 항목을 덮어씁니다. | Apply the same settings to {{target}}; existing entries with the same id will be overwritten. | 保留 |
| mcp.form.willOverwriteWarning | 将覆盖 {{target}} 中的同名配置 | {{target}}에 있는 같은 이름의 설정을 덮어씁니다. | Will overwrite existing config in {{target}} | 已修订 |
| mcp.wizard.title | MCP 配置向导 | MCP 설정 마법사 | MCP Configuration Wizard | 已修订 |
| mcp.wizard.hint | 快速配置 MCP 服务器，自动生成 JSON 配置 | MCP 서버를 빠르게 설정하고 JSON 설정을 자동 생성합니다. | Quickly configure MCP server and auto-generate JSON configuration | 已修订 |
| mcp.wizard.type | 类型 | 유형 | Type | 保留 |
| mcp.wizard.typeStdio | stdio | stdio | stdio | 已修订 |
| mcp.wizard.typeHttp | http | http | http | 保留 |
| mcp.wizard.typeSse | sse | sse | sse | 已修订 |
| mcp.wizard.command | 命令 | 명령 | Command | 保留 |
| mcp.wizard.commandPlaceholder | npx 或 uvx | npx 또는 uvx | npx or uvx | 保留 |
| mcp.wizard.args | 参数 | 인수 | Arguments | 保留 |
| mcp.wizard.argsPlaceholder | arg1<br>arg2 | arg1<br>arg2 | arg1<br>arg2 | 已修订 |
| mcp.wizard.env | 环境变量 | 환경 변수 | Environment Variables | 保留 |
| mcp.wizard.envPlaceholder | KEY1=value1<br>KEY2=value2 | KEY1=value1<br>KEY2=value2 | KEY1=value1<br>KEY2=value2 | 保留 |
| mcp.wizard.url | URL | URL | URL | 保留 |
| mcp.wizard.urlPlaceholder | https://api.example.com/mcp | https://api.example.com/mcp | https://api.example.com/mcp | 保留 |
| mcp.wizard.urlRequired | 请输入 URL | URL을 입력하세요 | Please enter URL | 保留 |
| mcp.wizard.headers | 请求头（可选） | 헤더(선택사항) | Headers (optional) | 保留 |
| mcp.wizard.headersPlaceholder | Authorization: Bearer your_token_here<br>Content-Type: application/json | Authorization: Bearer your_token_here<br>Content-Type: application/json | Authorization: Bearer your_token_here<br>Content-Type: application/json | 已修订 |
| mcp.wizard.preview | 配置预览 | 설정 미리보기 | Configuration Preview | 已修订 |
| mcp.wizard.apply | 应用配置 | 설정 적용 | Apply Configuration | 已修订 |
| mcp.id | 标识 (唯一) | 식별자(고유) | Identifier (unique) | 保留 |
| mcp.type | 类型 | 유형 | Type | 保留 |
| mcp.command | 命令 | 명령 | Command | 保留 |
| mcp.validateCommand | 校验命令 | 명령 검증 | Validate Command | 保留 |
| mcp.args | 参数 | 인수 | Args | 保留 |
| mcp.argsPlaceholder | 例如：mcp-server-fetch --help | 예: mcp-server-fetch --help | e.g., mcp-server-fetch --help | 保留 |
| mcp.env | 环境变量 (一行一个，KEY=VALUE) | 환경 변수(한 줄에 하나씩, KEY=VALUE) | Environment (one per line, KEY=VALUE) | 已修订 |
| mcp.envPlaceholder | FOO=bar<br>HELLO=world | FOO=bar<br>HELLO=world | FOO=bar<br>HELLO=world | 保留 |
| mcp.reset | 重置 | 초기화 | Reset | 保留 |
| mcp.msg.saved | 已保存 | 저장됨 | Saved | 保留 |
| mcp.msg.deleted | 已删除 | 삭제됨 | Deleted | 保留 |
| mcp.msg.enabled | 已启用 | 활성화됨 | Enabled | 保留 |
| mcp.msg.disabled | 已禁用 | 비활성화됨 | Disabled | 保留 |
| mcp.msg.templateAdded | 已添加模板 | 템플릿이 추가됨 | Template added | 保留 |
| mcp.error.idRequired | 请填写标识 | 식별자를 입력하세요 | Please enter identifier | 保留 |
| mcp.error.idExists | 该标识已存在，请更换 | 식별자가 이미 존재합니다. 다른 것을 선택하세요. | Identifier already exists. Please choose another. | 保留 |
| mcp.error.jsonInvalid | JSON 格式错误，请检查 | 잘못된 JSON 형식 | Invalid JSON format | 保留 |
| mcp.error.tomlInvalid | TOML 格式错误，请检查 | 잘못된 TOML 형식 | Invalid TOML format | 保留 |
| mcp.error.commandRequired | 请填写命令 | 명령어를 입력해주세요 | Please enter command | 保留 |
| mcp.error.singleServerObjectRequired | 此处只需单个服务器对象，请不要粘贴包含 mcpServers 的整份配置 | 단일 MCP 서버 개체를 붙여넣으십시오(최상위 mcpServers는 포함하지 않음). | Please paste a single MCP server object (do not include top-level mcpServers) | 保留 |
| mcp.error.saveFailed | 保存失败 | 저장 실패 | Save failed | 保留 |
| mcp.error.deleteFailed | 删除失败 | 삭제 실패 | Delete failed | 保留 |
| mcp.validation.ok | 命令可用 | 사용 가능한 명령 | Command available | 保留 |
| mcp.validation.fail | 命令不可用 | 명령을 사용할 수 없습니다 | Command not found | 已修订 |
| mcp.confirm.deleteTitle | 删除 MCP 服务器 | MCP 서버 삭제 | Delete MCP Server | 保留 |
| mcp.confirm.deleteMessage | 确定要删除 MCP 服务器 "{{id}}" 吗？此操作无法撤销。 | MCP 서버 "{{id}}"을(를) 삭제하시겠습니까? 이 작업은 취소할 수 없습니다. | Are you sure you want to delete MCP server "{{id}}"? This action cannot be undone. | 保留 |
| mcp.presets.title | 选择 MCP 类型 | MCP 유형 선택 | Select MCP Type | 保留 |
| mcp.presets.enable | 启用 | 활성화 | Enable | 保留 |
| mcp.presets.enabled | 已启用 | 활성화됨 | Enabled | 保留 |
| mcp.presets.installed | 已安装 | 설치됨 | Installed | 保留 |
| mcp.presets.docs | 文档 | 문서 | Docs | 保留 |
| mcp.presets.requiresEnv | 需要环境变量 | 환경 변수 필요 | Requires env | 已修订 |
| mcp.presets.fetch.name | mcp-server-fetch | mcp-server-fetch | mcp-server-fetch | 已修订 |
| mcp.presets.fetch.description | 通用 HTTP 请求工具，支持 GET/POST 等 HTTP 方法，适合快速请求接口/抓取网页数据 | 범용 HTTP 요청 도구는 GET/POST 및 기타 HTTP 방법을 지원하며 빠른 API 요청 및 웹 데이터 스크래핑에 적합합니다. | Universal HTTP request tool, supports GET/POST and other HTTP methods, suitable for quick API requests and web data scraping | 保留 |
| mcp.presets.time.name | mcp-server-time | mcp-server-time | mcp-server-time | 已修订 |
| mcp.presets.time.description | 时间查询工具，提供当前时间、时区转换、日期计算等功能 | 현재 시간, 시간대 변환, 날짜 계산 기능을 제공하는 시간 조회 도구 | Time query tool providing current time, timezone conversion, and date calculation features | 已修订 |
| mcp.presets.memory.name | @modelcontextprotocol/server-memory | @modelcontextprotocol/server-memory | @modelcontextprotocol/server-memory | 已修订 |
| mcp.presets.memory.description | 知识图谱记忆系统，支持存储实体、关系和观察，让 AI 记住对话中的重要信息 | AI가 대화에서 중요한 정보를 기억할 수 있도록 엔터티, 관계 및 관찰을 지원하는 지식 그래프 메모리 시스템 | Knowledge graph memory system supporting entities, relations, and observations to help AI remember important information from conversations | 保留 |
| mcp.presets.sequential-thinking.name | @modelcontextprotocol/server-sequential-thinking | @modelcontextprotocol/server-sequential-thinking | @modelcontextprotocol/server-sequential-thinking | 已修订 |
| mcp.presets.sequential-thinking.description | 顺序思考工具，帮助 AI 将复杂问题分解为多个步骤，逐步深入思考 | AI가 더 깊은 사고를 위해 복잡한 문제를 여러 단계로 분류하는 데 도움이 되는 순차적 사고 도구 | Sequential thinking tool helping AI break down complex problems into multiple steps for deeper thinking | 保留 |
| mcp.presets.context7.name | @upstash/context7-mcp | @upstash/context7-mcp | @upstash/context7-mcp | 保留 |
| mcp.presets.context7.description | Context7 文档搜索工具，提供最新的库文档和代码示例，配置 key 会有更高限额 | 최신 라이브러리 문서 및 코드 예제를 제공하는 Context7 문서 검색 도구(키로 설정 시 제한이 더 높음) | Context7 documentation search tool providing latest library docs and code examples, with higher limits when configured with a key | 已修订 |
| prompts.add | 添加提示词 | 프롬프트 추가 | Add Prompt | 保留 |
| prompts.addTitle | 添加提示词 · {{appName}} | 프롬프트 추가 · {{appName}} | Add prompt · {{appName}} | 保留 |
| prompts.editTitle | 编辑提示词 | 프롬프트 편집 | Edit prompt | 保留 |
| prompts.enabled | 已启用 | 활성화됨 | Enabled | 保留 |
| prompts.enable | 启用 | 활성화 | Enable | 保留 |
| prompts.loading | 加载中... | 로드 중... | Loading... | 保留 |
| prompts.searchPlaceholder | 搜索名称、说明或正文 | 이름, 설명 또는 본문 검색 | Search name, note or text | 已修订 |
| prompts.searchAriaLabel | 搜索提示词 | 프롬프트 검색 | Search prompts | 已修订 |
| prompts.noSearchResults | 没有名称、说明或正文匹配“{{query}}”的提示词 | 이름, 설명 또는 본문이 “{{query}}”와 일치하는 프롬프트가 없습니다. | No prompt name, note or text matches "{{query}}" | 已修订 |
| prompts.name | 名称 | 이름 | Name | 保留 |
| prompts.namePlaceholder | 例如 团队编码规范 | 예를 들어 팀 코딩 규칙 | e.g. Team coding rules | 保留 |
| prompts.description | 说明 | 설명 | Note | 已修订 |
| prompts.descriptionPlaceholder | 可选，只在 CC Switch 里显示 | 선택 사항, CC Switch에만 표시됨 | Optional, shown only in CC Switch | 保留 |
| prompts.content | 正文 | 텍스트 | Text | 保留 |
| prompts.contentPlaceholder | # {{filename}}<br><br>用 Markdown 写给 {{appName}} 的长期说明… | # {{filename}}<br><br>{{appName}}에 적용할 지속적인 지침을 Markdown으로 작성하세요… | # {{filename}}<br><br>Standing instructions for {{appName}}, in Markdown… | 已修订 |
| prompts.loadFailed | 加载提示词失败 | 프롬프트를 로드하지 못했습니다. | Failed to load prompts | 保留 |
| prompts.saveSuccess | 保存成功 | 성공적으로 저장되었습니다 | Saved successfully | 保留 |
| prompts.saveFailed | 保存失败 | 저장하지 못했습니다. | Failed to save | 保留 |
| prompts.deleteSuccess | 删除成功 | 삭제되었습니다. | Deleted successfully | 保留 |
| prompts.deleteFailed | 删除失败 | 삭제하지 못했습니다. | Failed to delete | 保留 |
| prompts.enableSuccess | 启用成功 | 성공적으로 활성화되었습니다 | Enabled successfully | 保留 |
| prompts.enableFailed | 启用失败 | 활성화하지 못했습니다. | Failed to enable | 保留 |
| prompts.disableSuccess | 禁用成功 | 성공적으로 비활성화되었습니다 | Disabled successfully | 保留 |
| prompts.disableFailed | 禁用失败 | 비활성화하지 못했습니다. | Failed to disable | 保留 |
| prompts.importSuccess | 导入成功 | 성공적으로 가져왔습니다 | Imported successfully | 保留 |
| prompts.importFailed | 导入失败 | 가져오지 못했습니다. | Failed to import | 保留 |
| prompts.appSelect | 选择应用 | 앱 선택 | Choose app | 保留 |
| prompts.helpTitle | 提示词怎么生效 | 프롬프트가 적용되는 방식 | How prompts take effect | 保留 |
| prompts.helpText | 每个应用同时只启用一条，它就是目标文件的内容。在别处改了文件，下次打开本页时会收进启用中的那条；文件里有本页没有的内容，启用前先存成「原始提示词」。 | 각 앱에는 한 번에 하나의 활성화된 프롬프트가 있으며 이는 대상 파일이 됩니다. 다른 곳에서 편집한 내용은 다음에 이 페이지를 열 때 활성화된 프롬프트로 가져옵니다. 아직 여기에 없는 파일 콘텐츠는 다른 콘텐츠가 활성화되기 전에 "원본 프롬프트"로 저장됩니다. | Each app has one enabled prompt at a time, and it becomes the target file. Edits made elsewhere are pulled into the enabled prompt the next time you open this page; file content that isn't here yet is saved as an "Original prompt" before another one is enabled. | 保留 |
| prompts.helpHermesTitle | SOUL.md 怎么生效 | SOUL.md의 효과 | How SOUL.md takes effect | 保留 |
| prompts.helpHermesText | SOUL.md 是 Hermes 的人设，同时只启用一条。在别处改了文件，下次打开本页时会收进启用中的那条；文件里有本页没有的内容，启用前先存成「原始提示词」。 | SOUL.md는 Hermes의 페르소나입니다. 한 번에 하나씩 활성화됩니다. 다른 곳에서 편집한 내용은 다음에 이 페이지를 열 때 활성화된 항목으로 가져옵니다. 아직 여기에 없는 파일 콘텐츠는 다른 콘텐츠가 활성화되기 전에 "원본 프롬프트"로 저장됩니다. | SOUL.md is Hermes's persona; one is enabled at a time. Edits made elsewhere are pulled into the enabled one the next time you open this page; file content that isn't here yet is saved as an "Original prompt" before another one is enabled. | 保留 |
| prompts.helpPiTitle | Pi 的提示词怎么生效 | Pi 프롬프트가 적용되는 방법 | How Pi prompts take effect | 保留 |
| prompts.helpPiText | 提示库同时只启用一条，它就是 AGENTS.md 的内容。系统提示文件存在就生效，模板在 Pi 里输入 /命令名 调用，这两类都不用启用。 | 프롬프트 라이브러리에서는 한 번에 하나만 활성화되며, 그 내용이 AGENTS.md에 저장됩니다. 시스템 프롬프트 파일은 존재하면 적용되고 템플릿은 Pi에서 /명령어이름을 입력하여 호출합니다. 이 두 유형은 별도로 활성화할 필요가 없습니다. | One library prompt is enabled at a time and becomes AGENTS.md. System prompt files take effect whenever they exist, and templates are run in Pi by typing /command — neither needs enabling. | 已修订 |
| prompts.moreActions | 提示词的更多操作 | 프롬프트 추가 작업 | More prompt actions | 已修订 |
| prompts.importCurrent | 导入当前的 {{file}} | 현재 {{file}} 가져오기 | Import current {{file}} | 保留 |
| prompts.importReason.missing | {{file}} 不存在，没有可导入的内容 | {{file}}가 존재하지 않으므로 가져올 것이 없습니다. | {{file}} doesn't exist, so there's nothing to import | 保留 |
| prompts.importReason.empty | {{file}} 是空的，没有可导入的内容 | {{file}}가 비어 있으므로 가져올 항목이 없습니다. | {{file}} is empty, so there's nothing to import | 保留 |
| prompts.importReason.duplicate | 文件内容已经在列表里：「{{name}}」 | 파일 콘텐츠가 이미 목록에 있습니다: "{{name}}" | The file content is already in the list: "{{name}}" | 保留 |
| prompts.openFolder | 打开所在文件夹 | 포함된 폴더 열기 | Open containing folder | 保留 |
| prompts.openFolderFailed | 没能打开文件夹 | 폴더를 열 수 없습니다. | Couldn't open the folder | 保留 |
| prompts.copyFilePath | 复制文件路径 | 파일 경로 복사 | Copy file path | 保留 |
| prompts.copyFolderPath | 复制文件夹路径 | 폴더 경로 복사 | Copy folder path | 保留 |
| prompts.copiedPath | 已复制 {{path}} | {{path}}을(를) 복사했습니다. | Copied {{path}} | 已修订 |
| prompts.copyFailed | 没能复制到剪贴板 | 클립보드에 복사할 수 없습니다. | Couldn't copy to the clipboard | 保留 |
| prompts.appLabel | 应用： | 앱: | App: | 保留 |
| prompts.appNoteDesktop | Claude Desktop 用的是 Claude Code 的提示词。 | Claude Desktop는 Claude Code의 프롬프트를 사용합니다. | Claude Desktop uses Claude Code's prompts. | 保留 |
| prompts.appNoteOpenclaw | OpenClaw 在它自己页面的「工作区」里管理。 | OpenClaw는 해당 앱 페이지의 작업 공간에서 관리합니다. | OpenClaw is managed under Workspace on its own page. | 已修订 |
| prompts.targetFile | 目标文件 | 대상 파일 | Target file | 保留 |
| prompts.targetDir | 目录 | 폴더 | Folder | 保留 |
| prompts.fileMissing | 文件不存在 | 파일이 존재하지 않습니다 | file doesn't exist | 保留 |
| prompts.fileEmpty | 空文件 | 빈 파일 | empty file | 保留 |
| prompts.searchPiLibrary | 搜索提示库 | 프롬프트 라이브러리 검색 | Search library | 已修订 |
| prompts.searchFound | 找到 {{count}} 个 | {{count}}을(를) 찾았습니다 | {{count}} found | 已修订 |
| prompts.clearSearch | 清除搜索 | 검색 지우기 | Clear search | 保留 |
| prompts.listLabel | {{app}} 的提示词 | {{app}} 프롬프트 | {{app}} prompts | 保留 |
| prompts.disable | 停用 | 비활성화 | Disable | 保留 |
| prompts.enableAria | 启用 {{name}} | {{name}} 활성화 | Enable {{name}} | 保留 |
| prompts.disableAria | 停用 {{name}} | {{name}} 비활성화 | Disable {{name}} | 保留 |
| prompts.editAria | 编辑 {{name}} | {{name}} 편집 | Edit {{name}} | 保留 |
| prompts.rowMoreActions | {{name}} 的更多操作 | {{name}}에 대한 추가 작업 | More actions for {{name}} | 保留 |
| prompts.updatedToday | 今天 {{time}} 更新 | 오늘 업데이트됨 {{time}} | Updated today {{time}} | 保留 |
| prompts.updatedOn | {{month}} 月 {{day}} 日更新 | {{date}}에 업데이트됨 | Updated {{date}} | 已修订 |
| prompts.emptyContent | （空） | (비어 있는) | (empty) | 保留 |
| prompts.copyToApps | 复制到其他应用 | 다른 앱에 복사 | Copy to other apps | 保留 |
| prompts.copyContent | 复制正文 | 텍스트 복사 | Copy text | 保留 |
| prompts.copiedContent | 已复制「{{name}}」的正文 | "{{name}}" 텍스트를 복사했습니다. | Copied the text of "{{name}}" | 保留 |
| prompts.deleteBlocked | 启用中的不能删除，先停用 | 삭제하기 전에 비활성화하세요. | Disable it before deleting | 保留 |
| prompts.emptyTitle | {{app}} 还没有提示词 | 아직 {{app}} 프롬프트가 없습니다 | No {{app}} prompts yet | 保留 |
| prompts.emptyTarget | 启用的那条会写进 {{path}}。 | 활성화된 프롬프트는 {{path}}에 기록됩니다. | The enabled prompt is written to {{path}}. | 保留 |
| prompts.emptyFile | {{path}} 里已有 {{size}} 内容，还不在 CC Switch 里 | {{path}}에 CC Switch에 아직 등록되지 않은 내용 {{size}}가 있습니다 | {{path}} already has {{size}} of content that isn't in CC Switch yet | 已修订 |
| prompts.importExisting | 导入现有内容 | 기존 콘텐츠 가져오기 | Import existing content | 保留 |
| prompts.formDescription | 名称、说明和写进 {{file}} 的正文 | 이름, 설명 및 {{file}}에 저장할 본문 | Name, note and the text written to {{file}} | 已修订 |
| prompts.requiredMark | （必填） | (필수) | (required) | 已修订 |
| prompts.namePlaceholderHermes | 例如 中文搭档 | 예: 친절한 파트너 | e.g. Friendly partner | 已修订 |
| prompts.nameRequired | 填写名称，例如 团队编码规范 | 이름을 입력하세요. 예: 팀 코딩 규칙 | Enter a name, e.g. Team coding rules | 已修订 |
| prompts.nameRequiredHermes | 填写名称，例如 中文搭档 | 이름을 입력하세요. 예: 친절한 파트너 | Enter a name, e.g. Friendly partner | 已修订 |
| prompts.contentPlaceholderHermes | # SOUL.md<br><br>用 Markdown 写 Hermes 的人设：语气、说话方式、要避免什么… | # SOUL.md<br><br>Markdown의 Hermes 페르소나: 어조, 말하는 방식, 피해야 할 것… | # SOUL.md<br><br>Hermes's persona in Markdown: tone, way of speaking, what to avoid… | 保留 |
| prompts.charCount | {{chars}} 个字符 · {{size}} | {{chars}} 문자 · {{size}} | {{chars}} characters · {{size}} | 保留 |
| prompts.mcodeTooLarge | MiniMax Code 的提示词最多 32 KB（按 UTF-8 字节算），现在是 {{size}}，删掉一些再保存 | MiniMax Code 프롬프트는 최대 32KB(UTF-8바이트)일 수 있습니다. 이것은 {{size}}입니다. 저장하기 전에 다듬어주세요 | MiniMax Code prompts can be at most 32 KB (UTF-8 bytes). This one is {{size}}; trim it before saving | 保留 |
| prompts.addSubmit | 添加 | 추가 | Add | 已修订 |
| prompts.saveAndOverwrite | 保存并覆盖 {{file}} | {{file}} 저장하고 덮어쓰기 | Save and overwrite {{file}} | 保留 |
| prompts.saveAndWritePi | 保存并写入 AGENTS.md | 저장 후 AGENTS.md에 반영 | Save and write AGENTS.md | 已修订 |
| prompts.copyDialog.title | 把「{{name}}」复制到其他应用 | "{{name}}"을(를) 다른 앱에 복사 | Copy "{{name}}" to other apps | 已修订 |
| prompts.copyDialog.lead | 各自复制成独立的一条，不自动启用；之后改动互不影响。 | 각 앱은 활성화되지 않은 자체 복사본을 갖습니다. 이후의 편집 내용은 서로 영향을 미치지 않습니다. | Each app gets its own copy, not enabled. Later edits don't affect each other. | 保留 |
| prompts.copyDialog.legend | 复制到哪些应用 | 복사할 앱 | Apps to copy to | 保留 |
| prompts.copyDialog.sameName | 已有同名的一条 | 같은 이름의 항목이 있습니다 | Has one with this name | 已修订 |
| prompts.copyDialog.hermesNote | SOUL.md 是人设 | SOUL.md는 페르소나입니다 | SOUL.md is a persona | 保留 |
| prompts.copyDialog.pickOne | 至少勾选一个应用 | 앱을 하나 이상 선택하세요. | Select at least one app | 保留 |
| prompts.copyDialog.go | 复制到 {{count}} 个应用 | {{count}} 앱에 복사 | Copy to {{count}} apps | 保留 |
| prompts.copyDialog.goNone | 复制 | 복사 | Copy | 保留 |
| prompts.copyDialog.failed | 没能复制到 {{apps}} | {{apps}}에 복사할 수 없습니다. | Couldn't copy to {{apps}} | 保留 |
| prompts.listSeparator | 、 | ,  | ,  | 保留 |
| prompts.undo | 撤销 | 실행 취소 | Undo | 已修订 |
| prompts.undoFailed | 没能撤销：{{reason}} | 실행취소할 수 없음: {{reason}} | Couldn't undo: {{reason}} | 保留 |
| prompts.toast.joiner | 。 | .  | .  | 保留 |
| prompts.toast.enabled | 已启用「{{name}}」，已覆盖 {{path}} | "{{name}}"을(를) 활성화하고 {{path}}을(를) 덮어썼습니다. | Enabled "{{name}}" and overwrote {{path}} | 已修订 |
| prompts.toast.enabledPi | 已启用「{{name}}」，已写入 AGENTS.md | “{{name}}”을(를) 활성화하고 AGENTS.md에 저장했습니다. | Enabled "{{name}}" and wrote AGENTS.md | 已修订 |
| prompts.toast.disabled | 已停用「{{name}}」，{{path}} 已清空 | "{{name}}" 비활성화; {{path}}는 이제 비어 있습니다 | Disabled "{{name}}"; {{path}} is now empty | 保留 |
| prompts.toast.disabledPi | 已停用「{{name}}」，已删除 AGENTS.md | "{{name}}"을(를) 비활성화하고 AGENTS.md를 삭제했습니다. | Disabled "{{name}}" and deleted AGENTS.md | 已修订 |
| prompts.toast.backup | 文件里原有的内容已存成「{{name}}」 | 파일의 이전 내용이 "{{name}}"로 저장되었습니다. | The file's previous content was saved as "{{name}}" | 保留 |
| prompts.toast.hermesOn | 新开的 Hermes 会话生效 | 새로운 Hermes 세션에 적용됩니다. | Takes effect in new Hermes sessions | 保留 |
| prompts.toast.hermesOff | 新开的 Hermes 会话改用内置的默认人设 | 새로운 Hermes 세션은 내장된 기본 페르소나를 사용합니다. | New Hermes sessions use the built-in default persona | 保留 |
| prompts.toast.added | 已添加「{{name}}」 | "{{name}}"을(를) 추가했습니다. | Added "{{name}}" | 已修订 |
| prompts.toast.saved | 已保存「{{name}}」 | "{{name}}"을(를) 저장했습니다. | Saved "{{name}}" | 已修订 |
| prompts.toast.savedActive | 已保存「{{name}}」，已覆盖 {{path}} | "{{name}}"을(를) 저장하고 {{path}}을(를) 덮어썼습니다. | Saved "{{name}}" and overwrote {{path}} | 已修订 |
| prompts.toast.savedActivePi | 已保存「{{name}}」，已写入 AGENTS.md | “{{name}}”을(를) 저장하고 AGENTS.md에 반영했습니다. | Saved "{{name}}" and wrote AGENTS.md | 已修订 |
| prompts.toast.deleted | 已删除「{{name}}」 | "{{name}}"을(를) 삭제했습니다. | Deleted "{{name}}" | 已修订 |
| prompts.toast.deletedSub | 只从 CC Switch 里删除，{{path}} 没有改动 | CC Switch에서만 제거되었습니다. {{path}}는 변경되지 않았습니다. | Removed from CC Switch only; {{path}} is unchanged | 保留 |
| prompts.toast.deletedPiSub | 只从提示库删除，AGENTS.md 没有改动 | 라이브러리에서만 제거됩니다. AGENTS.md는 변경되지 않았습니다. | Removed from the library only; AGENTS.md is unchanged | 保留 |
| prompts.toast.restored | 已恢复「{{name}}」 | "{{name}}"을(를) 복원했습니다. | Restored "{{name}}" | 已修订 |
| prompts.toast.imported | 已导入 {{path}} 的内容，文件没有改动 | {{path}}의 콘텐츠를 가져왔습니다. 파일은 변경되지 않았습니다 | Imported the content of {{path}}; the file is unchanged | 保留 |
| prompts.toast.importedPi | 已把 AGENTS.md 存进提示库，文件没有改动 | AGENTS.md를 라이브러리에 저장했습니다. 파일은 변경되지 않았습니다 | Saved AGENTS.md to the library; the file is unchanged | 保留 |
| prompts.toast.copied | 已把「{{name}}」复制到 {{apps}} | "{{name}}"을(를) {{apps}}에 복사했습니다. | Copied "{{name}}" to {{apps}} | 已修订 |
| profiles.switcherAriaLabel | 项目：{{name}} | 프로젝트: {{name}} | Project: {{name}} | 保留 |
| profiles.switcherTooltip.claude | 项目：一键切换 Claude Code 的供应商 / MCP / Skills / 记忆文件 | 프로젝트: 한 번의 클릭으로 Claude Code 공급자 / MCP / Skills / 메모리 파일 전환 | Projects: switch the Claude Code provider / MCP / Skills / memory files in one click | 已修订 |
| profiles.switcherTooltip.claude-desktop | 项目：一键切换 Claude Desktop 的供应商 | 프로젝트: 한 번의 클릭으로 Claude Desktop 공급자 전환 | Projects: switch the Claude Desktop provider in one click | 已修订 |
| profiles.switcherTooltip.codex | 项目：一键切换 Codex 的供应商 / MCP / Skills / 记忆文件 | 프로젝트: 한 번의 클릭으로 Codex 공급자 / MCP / Skills / 메모리 파일 전환 | Projects: switch the Codex provider / MCP / Skills / memory files in one click | 已修订 |
| profiles.none | 不使用项目 | 프로젝트 없음 | No project | 保留 |
| profiles.searchPlaceholder | 搜索项目 | 프로젝트 검색 | Search projects | 保留 |
| profiles.empty | 暂无项目 | 아직 프로젝트가 없습니다. | No projects yet | 保留 |
| profiles.createFromCurrent | 新建项目 | 새 프로젝트 | New project | 保留 |
| profiles.createDescription.claude | 把 Claude Code 当前的供应商、MCP、Skills、记忆文件保存为一个项目，之后可一键切换。 | 현재 Claude Code 공급자, MCP, Skills 및 메모리 파일을 나중에 전환할 수 있는 프로젝트로 저장합니다. | Save the current Claude Code provider, MCP, Skills and memory file as a project you can switch to later. | 已修订 |
| profiles.createDescription.claude-desktop | 把 Claude Desktop 当前的供应商保存为一个项目，之后可一键切换。 | 현재 Claude Desktop 공급자를 나중에 전환할 수 있는 프로젝트로 저장하세요. | Save the current Claude Desktop provider as a project you can switch to later. | 已修订 |
| profiles.createDescription.codex | 把 Codex 当前的供应商、MCP、Skills 和记忆文件配置保存为一个项目，之后可一键切换。 | 현재 Codex 공급자, MCP, Skills 및 메모리 파일 설정을 나중에 전환할 수 있는 프로젝트로 저장합니다. | Save the current Codex provider, MCP, Skills and memory file configuration as a project you can switch to later. | 已修订 |
| profiles.manage | 管理项目 | 프로젝트 관리 | Manage projects | 保留 |
| profiles.manageTitle | 管理项目 | 프로젝트 관리 | Manage Projects | 保留 |
| profiles.manageDescription | 项目是配置快照。切换项目时，当前配置会自动保存回原项目。 | 프로젝트는 설정 스냅샷입니다. 프로젝트를 전환하면 현재 설정을 이전 프로젝트에 자동으로 다시 저장합니다. | Projects are configuration snapshots. When you switch projects, the current configuration is automatically saved back to the project you are leaving. | 已修订 |
| profiles.namePlaceholder | 例如：开发、绘图 | 예를 들어 개발, 드로잉 | e.g. Development, Drawing | 保留 |
| profiles.rename | 重命名 | 이름 바꾸기 | Rename | 保留 |
| profiles.noSnapshotForScope | 本侧未保存 | 아직 이 앱에 저장되지 않았습니다. | Not saved for this app yet | 保留 |
| profiles.delete | 删除 | 삭제 | Delete | 保留 |
| profiles.deleteConfirmTitle | 确认删除 | 삭제 확인 | Confirm Delete | 保留 |
| profiles.deleteConfirmMessage | 确定要删除项目 "{{name}}" 吗？不会改动任何现有配置。 | "{{name}}" 프로젝트를 삭제하시겠습니까? 현재 설정은 변경되지 않습니다. | Are you sure you want to delete project "{{name}}"? Your current configuration will not be changed. | 已修订 |
| profiles.createSuccess | 项目已创建 | 프로젝트가 생성되었습니다. | Project created | 保留 |
| profiles.createFailed | 创建项目失败: {{detail}} | 프로젝트 생성 실패: {{detail}} | Failed to create project: {{detail}} | 保留 |
| profiles.updateSuccess | 项目已更新 | 프로젝트가 업데이트되었습니다. | Project updated | 保留 |
| profiles.updateFailed | 更新项目失败: {{detail}} | 프로젝트 업데이트 실패: {{detail}} | Failed to update project: {{detail}} | 保留 |
| profiles.deleteSuccess | 项目已删除 | 프로젝트가 삭제되었습니다. | Project deleted | 保留 |
| profiles.deleteFailed | 删除项目失败: {{detail}} | 프로젝트 삭제 실패: {{detail}} | Failed to delete project: {{detail}} | 保留 |
| profiles.applySuccess | 项目已应用 | 프로젝트 적용 | Project applied | 保留 |
| profiles.applyFailed | 应用项目失败: {{detail}} | 프로젝트 적용 실패: {{detail}} | Failed to apply project: {{detail}} | 保留 |
| profiles.applyWarnings | 项目已应用，{{warningCount}} 条警告：<br>{{details}} | 프로젝트를 적용했으며 경고가 {{warningCount}}개 있습니다:<br>{{details}} | Project applied with {{warningCount}} warning(s):<br>{{details}} | 已修订 |
| profiles.clearSuccess | 已切换为不使用项目 | 프로젝트 없음으로 전환됨 | Switched to no project | 保留 |
| workspace.title | Workspace 文件管理 | 작업 공간 파일 | Workspace Files | 已修订 |
| workspace.manage | Workspace | 작업 공간 | Workspace | 已修订 |
| workspace.files.agents | Agent 操作指令和规则 | 에이전트 지침 및 규칙 | Agent instructions and rules | 已修订 |
| workspace.files.soul | Agent 人格和沟通风格 | 에이전트 성격 및 대화 방식 | Agent personality and communication style | 已修订 |
| workspace.files.user | 用户档案和偏好 | 사용자 프로필 및 기본 설정 | User profile and preferences | 保留 |
| workspace.files.identity | Agent 名称和头像 | 에이전트 이름 및 아바타 | Agent name and avatar | 保留 |
| workspace.files.tools | 本地工具文档 | 로컬 도구 문서 | Local tool documentation | 保留 |
| workspace.files.memory | 长期记忆和决策记录 | 장기 기억 및 결정 기록 | Long-term memory and decisions | 已修订 |
| workspace.files.heartbeat | 心跳运行清单 | 하트비트 실행 체크리스트 | Heartbeat run checklist | 保留 |
| workspace.files.bootstrap | 首次运行仪式 | 첫 번째 실행 부트스트랩 의식 | First-run bootstrap ritual | 保留 |
| workspace.files.boot | 网关重启清单 | 게이트웨이 재부팅 체크리스트 | Gateway reboot checklist | 保留 |
| workspace.editing | 编辑 {{filename}} | {{filename}} 편집 | Edit {{filename}} | 保留 |
| workspace.saveSuccess | 保存成功 | 성공적으로 저장되었습니다 | Saved successfully | 保留 |
| workspace.saveFailed | 保存失败 | 저장하지 못했습니다. | Failed to save | 保留 |
| workspace.loadFailed | 读取失败 | 로드하지 못했습니다. | Failed to load | 保留 |
| workspace.openDirectory | 在文件管理器中打开 | 파일 관리자에서 열기 | Open in file manager | 保留 |
| workspace.dailyMemory.title | 每日记忆 | 일일 메모리 | Daily Memory | 已修订 |
| workspace.dailyMemory.sectionTitle | 每日记忆 | 일일 메모리 | Daily Memory | 已修订 |
| workspace.dailyMemory.cardTitle | 每日记忆文件 | 일일 메모리 파일 | Daily Memory Files | 保留 |
| workspace.dailyMemory.createToday | 添加记忆 | 메모리 추가 | Add Memory | 保留 |
| workspace.dailyMemory.empty | 暂无每日记忆文件 | 아직 일일 메모리 파일이 없습니다. | No daily memory files yet | 保留 |
| workspace.dailyMemory.loadFailed | 加载每日记忆文件失败 | 일일 메모리 파일을 로드하지 못했습니다. | Failed to load daily memory files | 保留 |
| workspace.dailyMemory.createFailed | 创建每日记忆文件失败 | 일일 메모리 파일을 생성하지 못했습니다. | Failed to create daily memory file | 保留 |
| workspace.dailyMemory.deleteSuccess | 每日记忆文件已删除 | 일일 메모리 파일이 삭제되었습니다. | Daily memory file deleted | 保留 |
| workspace.dailyMemory.deleteFailed | 删除每日记忆文件失败 | 일일 메모리 파일 삭제에 실패했습니다. | Failed to delete daily memory file | 保留 |
| workspace.dailyMemory.confirmDeleteTitle | 删除每日记忆 | 일일 메모리 삭제 | Delete Daily Memory | 已修订 |
| workspace.dailyMemory.confirmDeleteMessage | 确定删除 {{date}} 的每日记忆吗？此操作不可撤销。 | {{date}}의 일일 메모리를 삭제하시겠습니까? 이 작업은 취소할 수 없습니다. | Delete the daily memory for {{date}}? This cannot be undone. | 保留 |
| workspace.dailyMemory.searchPlaceholder | 搜索全文内容... | 전체 콘텐츠 검색... | Search full content... | 保留 |
| workspace.dailyMemory.searchScopeHint | 全文搜索所有每日记忆 ⌘F | 모든 일일 메모리에서 전체 텍스트를 검색합니다. ⌘F | Full-text search across all daily memories. ⌘F | 已修订 |
| workspace.dailyMemory.searchCloseHint | Esc 关闭 | 닫으려면 Esc를 누르세요. | Esc to close | 保留 |
| workspace.dailyMemory.noSearchResults | 没有找到匹配的每日记忆。 | 검색어와 일치하는 일일 메모리가 없습니다 | No daily memories match your search. | 已修订 |
| workspace.dailyMemory.searching | 搜索中... | 검색 중... | Searching... | 已修订 |
| workspace.dailyMemory.searchFailed | 搜索失败 | 검색 실패 | Search failed | 保留 |
| workspace.dailyMemory.matchCount | {{count}} 处匹配 | 일치 항목 {{count}}개 | {{count}} match(es) | 已修订 |
| openclaw.backupCreated | 已创建备份：{{path}} | 백업 생성됨: {{path}} | Backup created: {{path}} | 保留 |
| openclaw.providerKey | 供应商标识 | 공급자 키 | Provider Key | 已修订 |
| openclaw.providerKeyPlaceholder | my-provider | my-provider | my-provider | 保留 |
| openclaw.providerKeyHint | 配置文件中的唯一标识符，只能使用小写字母、数字和连字符 | 설정 파일의 고유 식별자입니다. 소문자, 숫자, 하이픈만 사용하세요. | Unique identifier in config file. Use lowercase letters, numbers, and hyphens only. | 已修订 |
| openclaw.providerKeyLockedHint | 该供应商已添加到应用配置中，供应商标识不可修改 | 이 공급자는 이미 앱 설정에 추가되었으므로 해당 키를 더 이상 변경할 수 없습니다. | This provider has already been added to the app config, so its key can no longer be changed. | 已修订 |
| openclaw.providerKeyRequired | 请填写供应商标识 | 공급자 키가 필요합니다. | Provider key is required | 已修订 |
| openclaw.providerKeyDuplicate | 此标识已被使用，请更换 | 이 키는 이미 사용 중입니다. | This key is already in use | 保留 |
| openclaw.providerKeyInvalid | 标识格式无效，只能使用小写字母、数字和连字符 | 형식이 잘못되었습니다. 소문자, 숫자, 하이픈만 사용하세요. | Invalid format. Use lowercase letters, numbers, and hyphens only. | 保留 |
| openclaw.apiProtocol | API 协议 | API 프로토콜 | API Protocol | 保留 |
| openclaw.selectProtocol | 选择 API 协议 | API 프로토콜 선택 | Select API Protocol | 保留 |
| openclaw.apiProtocolHint | 选择与供应商 API 兼容的协议类型。大多数供应商使用 OpenAI Completions 格式。 | 공급자 API와 호환되는 프로토콜을 선택하세요. 대부분의 공급자는 OpenAI Completions 형식을 사용합니다. | Select the protocol type compatible with the provider's API. Most providers use OpenAI Completions format. | 已修订 |
| openclaw.baseUrl | API 端点 | API 엔드포인트 | API Endpoint | 保留 |
| openclaw.models | 模型配置 | 모델 설정 | Model Configuration | 已修订 |
| openclaw.addModel | 添加模型 | 모델 추가 | Add Model | 保留 |
| openclaw.selectDefaultModel | 选择默认模型 | 기본 모델 선택 | Select Default Model | 保留 |
| openclaw.noModels | 暂无模型配置 | 설정된 모델이 없습니다. | No models configured | 已修订 |
| openclaw.modelId | 模型 ID | 모델 ID | Model ID | 保留 |
| openclaw.modelIdPlaceholder | claude-3-sonnet | claude-3-sonnet | claude-3-sonnet | 已修订 |
| openclaw.modelName | 显示名称 | 표시 이름 | Display Name | 保留 |
| openclaw.modelNamePlaceholder | Claude 3 Sonnet | Claude 3 Sonnet | Claude 3 Sonnet | 已修订 |
| openclaw.toggleModelDetails | 展开或收起模型详情 | 모델 세부 정보 펼치기/접기 | Expand or collapse model details | 已修订 |
| openclaw.removeModel | 移除模型 | 모델 제거 | Remove model | 已修订 |
| openclaw.contextWindow | 上下文长度 | 컨텍스트 길이 | Context Length | 保留 |
| openclaw.maxTokens | 最大输出 Token 数 | 최대 출력 토큰 | Max Output Tokens | 保留 |
| openclaw.reasoning | 支持扩展思考 | 확장 추론 지원 | Supports Extended Thinking | 已修订 |
| openclaw.inputTypes | 输入类型 | 입력 유형 | Input Types | 保留 |
| openclaw.modelCost | 成本（$/百万 Token） | 비용($/백만 토큰) | Cost ($/million tokens) | 保留 |
| openclaw.inputCost | 输入 | 입력 | Input | 保留 |
| openclaw.outputCost | 输出 | 출력 | Output | 已修订 |
| openclaw.cacheReadCost | 缓存读取 | 캐시 읽기 | Cache Read | 保留 |
| openclaw.cacheWriteCost | 缓存写入 | 캐시 쓰기 | Cache Write | 保留 |
| openclaw.userAgent | 发送 User-Agent | User-Agent 전송 | Send User-Agent | 已修订 |
| openclaw.userAgentHint | 部分供应商需要浏览器 User-Agent 才能正常访问。 | 일부 공급자는 브라우저 User-Agent 헤더가 있어야 정상적으로 작동합니다. | Some providers require a browser User-Agent header to work properly. | 已修订 |
| openclaw.env.title | 环境变量 | 환경 변수 | Environment Variables | 保留 |
| openclaw.env.editorHint | 以 JSON 形式编辑整个 env 节点。支持 env.vars、env.shellEnv 等嵌套对象。 | env 전체를 JSON으로 편집합니다. env.vars, env.shellEnv 같은 중첩 객체도 지원합니다. | Edit the full env section as JSON. Nested objects such as env.vars and env.shellEnv are supported. | 已修订 |
| openclaw.env.objectRequired | OpenClaw 的 env 必须是 JSON 对象。 | OpenClaw의 env는 JSON 객체여야 합니다. | OpenClaw env must be a JSON object. | 已修订 |
| openclaw.env.invalidJson | OpenClaw 的 env 必须是合法 JSON。 | OpenClaw의 env는 유효한 JSON이어야 합니다. | OpenClaw env must be valid JSON. | 已修订 |
| openclaw.env.empty | OpenClaw 的 env 不能为空。空对象请使用 {}。 | OpenClaw의 env는 비워 둘 수 없습니다. 빈 객체는 {}를 사용하세요. | OpenClaw env cannot be empty. Use {} for an empty object. | 已修订 |
| openclaw.env.keyPlaceholder | 变量名 | 변수 이름 | Variable name | 保留 |
| openclaw.env.valuePlaceholder | 值 | 값 | Value | 保留 |
| openclaw.env.add | 添加变量 | 변수 추가 | Add Variable | 保留 |
| openclaw.env.saveSuccess | 环境变量已保存 | 환경 변수가 저장되었습니다. | Environment variables saved | 保留 |
| openclaw.env.saveFailed | 保存环境变量失败 | 환경 변수를 저장하지 못했습니다. | Failed to save environment variables | 保留 |
| openclaw.env.loadFailed | 读取环境变量失败 | 환경 변수를 로드하지 못했습니다. | Failed to load environment variables | 保留 |
| openclaw.env.duplicateKey | 检测到重复的变量名: {{key}} | 중복된 변수 이름이 감지되었습니다: {{key}} | Duplicate variable name detected: {{key}} | 保留 |
| openclaw.tools.title | 工具权限 | 도구 권한 | Tool Permissions | 保留 |
| openclaw.tools.profile | 权限模式 | 권한 프로필 | Permission Profile | 保留 |
| openclaw.tools.profileMinimal | 最小权限 | 최소 권한 | Minimal | 已修订 |
| openclaw.tools.profileCoding | 编码 | 코딩 | Coding | 保留 |
| openclaw.tools.profileMessaging | 对话 | 메시징 | Messaging | 保留 |
| openclaw.tools.profileFull | 完全访问 | 전체 접근 | Full | 已修订 |
| openclaw.tools.profileUnset | 未设置 | 설정되지 않음 | Not set | 保留 |
| openclaw.tools.unsupportedProfileTitle | 检测到不受支持的工具配置 | 지원되지 않는 도구 프로필이 감지되었습니다. | Unsupported tools profile detected | 保留 |
| openclaw.tools.unsupportedProfileDescription | 当前 tools.profile 的值“{{value}}”不在 OpenClaw 支持列表内。在你手动选择新值之前，它会被保留。 | 현재 tools.profile 값 '{{value}}'는 지원되는 OpenClaw 목록에 없습니다. 새 값을 선택할 때까지 보존됩니다. | The current tools.profile value '{{value}}' is not in the supported OpenClaw list. It will be preserved until you choose a new value. | 保留 |
| openclaw.tools.unsupportedProfileLabel | 不受支持 | 지원되지 않음 | unsupported | 已修订 |
| openclaw.tools.allowList | 允许列表 | 허용 목록 | Allow List | 保留 |
| openclaw.tools.denyList | 拒绝列表 | 거부 목록 | Deny List | 保留 |
| openclaw.tools.patternPlaceholder | 工具名称或模式 | 도구 이름 또는 패턴 | Tool name or pattern | 保留 |
| openclaw.tools.addAllow | 添加允许 | 허용 추가 | Add Allow | 保留 |
| openclaw.tools.addDeny | 添加拒绝 | 거부 추가 | Add Deny | 保留 |
| openclaw.tools.saveSuccess | 工具权限已保存 | 도구 권한이 저장되었습니다. | Tool permissions saved | 保留 |
| openclaw.tools.saveFailed | 保存工具权限失败 | 도구 권한을 저장하지 못했습니다. | Failed to save tool permissions | 保留 |
| openclaw.tools.loadFailed | 读取工具权限失败 | 도구 권한을 로드하지 못했습니다. | Failed to load tool permissions | 保留 |
| openclaw.agents.title | Agents 配置 | 에이전트 설정 | Agents Config | 已修订 |
| openclaw.agents.description | 管理 openclaw.json 中的 agents.defaults 配置（默认模型、运行参数等） | openclaw.json의 agents.defaults 설정(기본 모델, 실행 매개변수 등)을 관리합니다 | Manage agents.defaults in openclaw.json (default model, runtime parameters, etc.) | 已修订 |
| openclaw.agents.modelSection | 模型配置 | 모델 설정 | Model Configuration | 已修订 |
| openclaw.agents.primaryModel | 默认模型 | 기본 모델 | Default Model | 保留 |
| openclaw.agents.primaryModelHint | 从已配置供应商的模型中选择默认模型 | 설정된 공급자의 모델 중에서 기본 모델 선택 | Select from models of configured providers | 已修订 |
| openclaw.agents.notSet | 未设置 | 설정되지 않음 | Not set | 保留 |
| openclaw.agents.fallbackModels | 回退模型 | 대체 모델 | Fallback Models | 保留 |
| openclaw.agents.fallbackModelsHint | 当主模型不可用时，按优先级依次尝试以下回退模型 | 기본 모델을 사용할 수 없는 경우 순서대로 대체가 시도됩니다. | When the primary model is unavailable, fallbacks are tried in order | 保留 |
| openclaw.agents.addFallback | 添加回退模型 | 대체 모델 추가 | Add fallback model | 保留 |
| openclaw.agents.noModels | 暂无已配置的供应商模型。请先添加 OpenClaw 供应商。 | 설정된 공급자 모델이 없습니다. 먼저 OpenClaw 공급자를 추가하세요. | No configured provider models. Please add an OpenClaw provider first. | 已修订 |
| openclaw.agents.notInList | {{value}} (供应商未配置) | {{value}}(공급자 미설정) | {{value}} (not configured) | 已修订 |
| openclaw.agents.runtimeSection | 运行参数 | 런타임 매개변수 | Runtime Parameters | 保留 |
| openclaw.agents.workspace | 工作区路径 | 작업 공간 경로 | Workspace Path | 已修订 |
| openclaw.agents.timeout | 超时时间（秒） | 시간 초과(초) | Timeout (seconds) | 保留 |
| openclaw.agents.contextTokens | 上下文 Token 数 | 컨텍스트 토큰 | Context Tokens | 保留 |
| openclaw.agents.maxConcurrent | 最大并发数 | 최대 동시 실행 수 | Max Concurrent | 已修订 |
| openclaw.agents.legacyTimeoutTitle | 检测到旧版超时字段 | 레거시 시간 초과가 감지되었습니다. | Legacy timeout detected | 保留 |
| openclaw.agents.legacyTimeoutDescription | 当前配置仍在使用 agents.defaults.timeout。保存本页面时会迁移为 timeoutSeconds。 | 현재 설정은 여전히 agents.defaults.timeout을 사용합니다. 이 페이지에서 저장하면 timeoutSeconds로 이전합니다. | This config still uses agents.defaults.timeout. Saving here will migrate it to timeoutSeconds. | 已修订 |
| openclaw.agents.saveSuccess | Agents 配置已保存 | 에이전트 설정이 저장되었습니다. | Agents config saved | 已修订 |
| openclaw.agents.saveFailed | 保存 Agents 配置失败 | 에이전트 설정을 저장하지 못했습니다. | Failed to save agents config | 已修订 |
| openclaw.agents.loadFailed | 读取 Agents 配置失败 | 에이전트 설정을 로드하지 못했습니다. | Failed to load agents config | 已修订 |
| openclaw.health.title | 检测到 OpenClaw 配置警告 | OpenClaw 설정 경고가 감지되었습니다. | OpenClaw config warnings detected | 已修订 |
| openclaw.health.invalidToolsProfile | tools.profile 使用了不受支持的值。OpenClaw 当前只支持 minimal、coding、messaging、full。 | tools.profile에 지원되지 않는 값이 있습니다. OpenClaw는 현재 minimal, coding, messaging, full만 지원합니다. | tools.profile contains an unsupported value. OpenClaw currently expects minimal, coding, messaging, or full. | 已修订 |
| openclaw.health.legacyTimeout | agents.defaults.timeout 已废弃。打开并保存 Agents 面板即可迁移到 timeoutSeconds。 | agents.defaults.timeout은 더 이상 사용하지 않는 필드입니다. 에이전트 패널을 열고 저장하면 timeoutSeconds로 이전합니다. | agents.defaults.timeout is deprecated. Save the Agents panel to migrate it to timeoutSeconds. | 已修订 |
| openclaw.health.stringifiedEnvVars | env.vars 应为对象，但当前值看起来像被字符串化或已损坏。 | env.vars는 객체여야 하지만 현재 값이 문자열이거나 잘못된 형식으로 보입니다. | env.vars should be an object, but the current value looks stringified or malformed. | 保留 |
| openclaw.health.stringifiedShellEnv | env.shellEnv 应为对象，但当前值看起来像被字符串化或已损坏。 | env.shellEnv는 객체여야 하지만 현재 값이 문자열이거나 잘못된 형식으로 보입니다. | env.shellEnv should be an object, but the current value looks stringified or malformed. | 保留 |
| openclaw.health.parseFailed | openclaw.json 不是合法 JSON5。请先修复文件，再通过这里编辑。 | openclaw.json을 유효한 JSON5로 구문 분석할 수 없습니다. 여기에서 파일을 편집하기 전에 수정하세요. | openclaw.json could not be parsed as valid JSON5. Fix the file before editing it here. | 保留 |
| hermes.form.baseUrl | API 端点 | API 엔드포인트 | API Endpoint | 保留 |
| hermes.form.providerKey | 供应商标识 | 공급자 키 | Provider Key | 已修订 |
| hermes.form.providerKeyPlaceholder | my-provider | my-provider | my-provider | 保留 |
| hermes.form.providerKeyHint | 只能使用小写字母、数字和连字符。用作 config.yaml 中的供应商名称。 | 소문자, 숫자, 하이픈만 가능합니다. config.yaml에서 공급자 이름으로 사용됩니다. | Lowercase letters, numbers, and hyphens only. Used as the provider name in config.yaml. | 已修订 |
| hermes.form.providerKeyLockedHint | 该供应商已添加到 Hermes 配置中，标识不可修改。 | 이미 Hermes 설정에 추가된 공급자이므로 식별자를 변경할 수 없습니다. | This provider is in Hermes config; key is locked. | 已修订 |
| hermes.form.providerKeyRequired | 供应商标识不能为空 | 공급자 키가 필요합니다. | Provider key is required | 已修订 |
| hermes.form.providerKeyInvalid | 供应商标识只能包含小写字母、数字和连字符 | 공급자 키에는 소문자, 숫자, 하이픈만 포함할 수 있습니다. | Provider key can only contain lowercase letters, numbers, and hyphens | 已修订 |
| hermes.form.providerKeyDuplicate | 该供应商标识已存在 | 이 공급자 키가 이미 존재합니다. | This provider key already exists | 已修订 |
| hermes.form.providerKeyBuiltin | 「{{key}}」是 Hermes 内置供应商的标识。Hermes 会改用内置供应商（要它自己的环境变量 Key），这张卡的地址和 Key 不会生效。请换一个标识，例如 cc-switch-{{key}}。 | ‘{{key}}’는 Hermes 내장 공급자의 ID입니다. Hermes는 자체 API 키 환경 변수가 필요한 내장 공급자를 사용하며 이 카드의 엔드포인트와 키를 무시합니다. cc-switch-{{key}} 같은 다른 식별자를 사용하세요. | "{{key}}" is the ID of a Hermes built-in provider. Hermes will use the built-in provider (which needs its own API key environment variable) and ignore this card's endpoint and key. Use a different key, e.g. cc-switch-{{key}}. | 已修订 |
| hermes.form.providerKeyBuiltinLocked | 「{{key}}」是 Hermes 内置供应商的标识。Hermes 会改用内置供应商，这张卡的地址和 Key 不会生效。标识已锁定无法修改，请用其他标识（例如 cc-switch-{{key}}）重新添加这个供应商，再删除这张卡。 | "{{key}}"는 Hermes 내장 공급자의 ID입니다. Hermes는 내장 공급자를 사용하고 이 카드의 엔드포인트와 키를 무시합니다. 키가 잠겨 있습니다. 이 공급자를 다른 키(예: cc-switch-{{key}}) 아래에 다시 추가한 다음 이 카드를 삭제하세요. | "{{key}}" is the ID of a Hermes built-in provider. Hermes will use the built-in provider and ignore this card's endpoint and key. The key is locked: add this provider again under another key (e.g. cc-switch-{{key}}), then delete this card. | 已修订 |
| hermes.form.apiMode | API 模式 | API 모드 | API Mode | 保留 |
| hermes.form.apiModeChatCompletions | OpenAI Chat Completions | OpenAI Chat Completions | OpenAI Chat Completions | 已修订 |
| hermes.form.apiModeAnthropicMessages | Anthropic Messages | Anthropic Messages | Anthropic Messages | 已修订 |
| hermes.form.apiModeCodexResponses | OpenAI Responses | OpenAI Responses | OpenAI Responses | 已修订 |
| hermes.form.apiModeBedrockConverse | AWS Bedrock Converse | AWS Bedrock Converse | AWS Bedrock Converse | 已修订 |
| hermes.form.baseUrlRequired | API 端点不能为空 | API 엔드포인트가 필요합니다. | API endpoint is required | 保留 |
| hermes.form.baseUrlScheme | 请使用 http:// 或 https:// 开头的地址 | http:// 또는 https:// 주소를 사용하세요. | Use an http:// or https:// address | 保留 |
| hermes.form.baseUrlInvalid | API 端点不是有效的 URL | API 엔드포인트는 유효한 URL이 아닙니다. | API endpoint is not a valid URL | 保留 |
| hermes.form.models | 模型列表 | 모델 목록 | Models | 已修订 |
| hermes.form.addModel | 添加模型 | 모델 추가 | Add model | 保留 |
| hermes.form.noModels | 暂无模型配置。切换到此供应商时将不会更新默认模型。 | 설정된 모델이 없습니다. 이 공급자로 전환해도 기본 모델은 변경되지 않습니다. | No models configured. Switching to this provider won't change the default model. | 已修订 |
| hermes.form.modelId | 模型 ID | 모델 ID | Model ID | 保留 |
| hermes.form.modelIdPlaceholder | anthropic/claude-opus-5 | anthropic/claude-opus-5 | anthropic/claude-opus-5 | 已修订 |
| hermes.form.modelName | 显示名称 | 표시 이름 | Display name | 保留 |
| hermes.form.modelNamePlaceholder | Claude Opus 5 | Claude Opus 5 | Claude Opus 5 | 已修订 |
| hermes.form.contextLength | 上下文长度 | 컨텍스트 길이 | Context length | 保留 |
| hermes.form.supportsVision | 支持图片输入 | 이미지 입력 지원 | Supports image input | 已修订 |
| hermes.form.toggleModelDetails | 展开或收起模型详情 | 모델 세부 정보 펼치기/접기 | Expand or collapse model details | 已修订 |
| hermes.form.removeModel | 移除模型 | 모델 제거 | Remove model | 已修订 |
| hermes.form.modelsHint | 启用为当前供应商时，第一个模型会设为 Hermes 默认模型。 | 활성화되면 첫 번째 모델이 Hermes 기본값이 됩니다. | When activated, the first model becomes the Hermes default. | 保留 |
| hermes.form.rateLimitDelay | 请求间隔（秒） | 요청 간격 (초) | Rate limit delay (seconds) | 已修订 |
| hermes.form.rateLimitDelayHint | 连续请求间的最小间隔秒数（可选）。留空表示无限制。 | 연속 요청 간의 최소 지연 시간(초)입니다(선택 사항). 제한이 없으면 비워 두세요. | Minimum delay in seconds between consecutive requests (optional). Leave empty for no limit. | 保留 |
| hermes.webui.open | 打开 Hermes Web UI | Hermes 웹 UI 열기 | Open Hermes Web UI | 保留 |
| hermes.webui.offline | Hermes Web UI 未启动，请先运行 `hermes dashboard` 启动服务。 | Hermes 웹 UI가 실행되고 있지 않습니다. 먼저 `hermes dashboard`로 시작하세요. | Hermes Web UI is not running. Start it with `hermes dashboard` first. | 保留 |
| hermes.webui.openFailed | 打开 Hermes Web UI 失败 | Hermes 웹 UI를 열지 못했습니다. | Failed to open Hermes Web UI | 保留 |
| hermes.webui.launchConfirmTitle | Hermes Dashboard 未启动 | Hermes 대시보드가 ​​실행되지 않습니다. | Hermes Dashboard is not running | 保留 |
| hermes.webui.launchConfirmMessage | 是否打开终端并运行 `hermes dashboard` 启动服务？<br><br>启动完成后会自动打开浏览器。<br><br>若终端提示找不到 hermes 或缺少 web 依赖，请先运行：<br>pip install hermes-agent[web] | 터미널을 열고 `hermes dashboard`로 서비스를 시작하시겠습니까?<br><br>시작이 완료되면 브라우저가 자동으로 열립니다.<br><br>터미널에 `hermes`를 찾을 수 없거나 웹 의존성이 없다는 메시지가 나오면 먼저 다음 명령을 실행하세요:<br>pip install hermes-agent[web] | Open a terminal and start it now with `hermes dashboard`?<br><br>The browser will open automatically once startup completes.<br><br>If the terminal reports that `hermes` cannot be found or the web extras are missing, run first:<br>pip install hermes-agent[web] | 已修订 |
| hermes.webui.launchConfirmAction | 打开终端并启动 | 터미널 열기 및 실행 | Open terminal & launch | 保留 |
| hermes.webui.launching | 已在终端启动 hermes dashboard | 터미널에서 `hermes dashboard`를 시작했습니다. | Started `hermes dashboard` in a terminal. | 保留 |
| hermes.webui.launchFailed | 打开终端失败 | 터미널을 열지 못했습니다. | Failed to open terminal | 保留 |
| hermes.memory.disabledHint | 在重新启用前 Hermes 会跳过此记忆 | Hermes는 다시 활성화될 때까지 이 메모리를 건너뜁니다. | Hermes will skip this memory until re-enabled | 保留 |
| hermes.memory.toggleFailed | 切换记忆状态失败 | 메모리를 전환하지 못했습니다. | Failed to toggle memory | 保留 |
| hermes.memory.saveSuccess | 记忆已保存，Hermes 下次启动或新建会话时生效。 | 메모리를 저장했습니다. Hermes를 다시 시작하거나 새 세션을 만들면 적용됩니다. | Memory saved. Takes effect when Hermes restarts or starts a new session. | 已修订 |
| hermes.memory.saveFailed | 保存记忆失败 | 메모리를 저장하지 못했습니다. | Failed to save memory | 保留 |
| hermes.memory.loadFailed | 读取记忆文件失败 | 메모리 파일을 읽지 못했습니다. | Failed to read memory file | 保留 |
| hermes.memory.openConfig | 在 Hermes Web UI 调整上限 | Hermes 웹 UI에서 제한 조정 | Adjust limits in Hermes Web UI | 保留 |
| hermes.memory.fileTabs | 记忆文件 | 메모리 파일 | Memory files | 保留 |
| hermes.memory.agentName | Agent 记忆 | 에이전트 메모리 | Agent Memory | 保留 |
| hermes.memory.userName | 用户画像 | 사용자 프로필 | User Profile | 保留 |
| hermes.memory.agentDesc | Hermes 自己记下的笔记，会带进它的系统提示 | Hermes가 자신을 위해 보관하는 메모로, 시스템 프롬프트에 포함됩니다 | Notes Hermes keeps for itself; they go into its system prompt | 已修订 |
| hermes.memory.userDesc | 关于你的信息，会带进 Hermes 的系统提示 | 사용자에 관한 정보로, Hermes의 시스템 프롬프트에 포함됩니다 | What Hermes knows about you; it goes into Hermes' system prompt | 已修订 |
| hermes.memory.separatorRule | 每条之间用单独一行的 § 分隔 | §만 포함하는 줄로 항목을 구분하세요. | Separate entries with a line containing only § | 保留 |
| hermes.memory.helpTitle | {{name}}是什么 | {{name}}는 무엇입니까? | What is {{name}}? | 保留 |
| hermes.memory.helpBody | {{desc}}。{{rule}}。 | {{desc}}. {{rule}}. | {{desc}}. {{rule}}. | 保留 |
| hermes.memory.enableLabel | 启用 {{name}} | {{name}} 활성화 | Enable {{name}} | 保留 |
| hermes.memory.agentPlaceholder | 项目 acme-web 用 pnpm 和 Node 22。<br>§<br>部署走 GitHub Actions。 | 프로젝트 acme-web은 pnpm과 Node 22를 사용합니다.<br>§<br>배포는 GitHub Actions로 진행합니다. | Project acme-web uses pnpm and Node 22.<br>§<br>Deploys go through GitHub Actions. | 已修订 |
| hermes.memory.userPlaceholder | 称呼：octocat。<br>§<br>用中文交流，代码注释用英文。 | 호칭: octocat.<br>§<br>중국어로 대화하고 코드 주석은 영어로 작성합니다. | Name: octocat.<br>§<br>Prefers short answers: conclusion first. | 已修订 |
| hermes.memory.editorLabel | {{name}}（{{file}}）内容 | {{name}}({{file}}) 내용 | {{name}} ({{file}}) content | 保留 |
| hermes.memory.unsaved | 有未保存的修改 | 저장되지 않은 변경사항 | Unsaved changes | 保留 |
| hermes.memory.noChanges | 没有未保存的修改 | 저장되지 않은 변경사항 없음 | No unsaved changes | 保留 |
| hermes.memory.meterLabel | 剩余字符 | 남은 문자 수 | Characters remaining | 保留 |
| hermes.memory.remaining | 剩余 {{remaining}} / {{limit}} 字符 | {{limit}} 자 중 {{remaining}} 자 남음 | {{remaining}} of {{limit}} characters remaining | 保留 |
| hermes.memory.overLimitBy | 超出上限 {{over}} 字符，Hermes 下次加载时会截断 | 한도를 {{over}}자 초과했습니다. Hermes가 다음에 불러올 때 내용을 잘라냅니다 | {{over}} characters over the limit — Hermes will truncate on next load | 已修订 |
| hermes.memory.toggledOn | 已启用 {{name}}，Hermes 下次启动或新建会话时生效。 | {{name}}가 활성화되었습니다. Hermes가 다시 시작되거나 새 세션을 시작할 때 적용됩니다. | {{name}} enabled. Takes effect when Hermes restarts or starts a new session. | 保留 |
| hermes.memory.toggledOff | 已停用 {{name}}，Hermes 下次启动或新建会话时生效。 | {{name}}가 비활성화되었습니다. Hermes가 다시 시작되거나 새 세션을 시작할 때 적용됩니다. | {{name}} disabled. Takes effect when Hermes restarts or starts a new session. | 保留 |
| env.warning.title | 检测到系统环境变量冲突 | 환경 변수 충돌이 감지되었습니다. | Environment Variable Conflicts Detected | 保留 |
| env.warning.description | 发现 {{count}} 个环境变量可能会覆盖您的配置 | 설정을 재정의할 수 있는 {{count}} 환경 변수가 발견되었습니다. | Found {{count}} environment variables that may override your configuration | 已修订 |
| env.actions.expand | 查看详情 | 세부정보 보기 | View Details | 保留 |
| env.actions.collapse | 收起 | 접기 | Collapse | 保留 |
| env.actions.selectAll | 全选 | 모두 선택 | Select All | 保留 |
| env.actions.clearSelection | 取消选择 | 선택 지우기 | Clear Selection | 保留 |
| env.actions.deleteSelected | 删除选中 ({{count}}) | 선택 항목 삭제({{count}}) | Delete Selected ({{count}}) | 保留 |
| env.actions.deleting | 删除中... | 삭제 중... | Deleting... | 保留 |
| env.field.value | 值 | 값 | Value | 保留 |
| env.field.source | 来源 | 출처 | Source | 保留 |
| env.source.userRegistry | 用户环境变量 (注册表) | 사용자 환경변수(레지스트리) | User Environment Variable (Registry) | 保留 |
| env.source.systemRegistry | 系统环境变量 (注册表) | 시스템 환경변수(레지스트리) | System Environment Variable (Registry) | 保留 |
| env.source.systemEnv | 系统环境变量 | 시스템 환경 변수 | System Environment Variable | 保留 |
| env.delete.success | 环境变量已成功删除 | 환경 변수가 삭제되었습니다. | Environment variables deleted successfully | 保留 |
| env.delete.error | 删除环境变量失败 | 환경 변수를 삭제하지 못했습니다. | Failed to delete environment variables | 保留 |
| env.backup.location | 备份位置: {{path}} | 백업 위치: {{path}} | Backup location: {{path}} | 保留 |
| env.confirm.title | 确认删除环境变量 | 환경 변수 삭제 확인 | Confirm Delete Environment Variables | 保留 |
| env.confirm.message | 确定要删除 {{count}} 个环境变量吗？ | {{count}} 환경 변수를 삭제하시겠습니까? | Are you sure you want to delete {{count}} environment variable(s)? | 保留 |
| env.confirm.backupNotice | 删除前将自动备份,您可以稍后恢复。删除后需要重启应用或终端才能生效。 | 삭제하기 전에 백업이 자동으로 생성됩니다. 나중에 복원할 수 있습니다. 변경 사항은 애플리케이션이나 터미널을 다시 시작한 후에 적용됩니다. | A backup will be created automatically before deletion. You can restore it later. Changes take effect after restarting the application or terminal. | 保留 |
| env.confirm.confirm | 确认删除 | 삭제 확인 | Confirm Delete | 保留 |
| env.error.noSelection | 请选择要删除的环境变量 | 삭제할 환경 변수를 선택하세요. | Please select environment variables to delete | 保留 |
| skills.manage | Skills | Skills | Skills | 保留 |
| skills.title | Skills 管理 | Skills 관리 | Skills Management | 保留 |
| skills.description | 从流行的仓库发现并安装技能，扩展 Claude Code/Codex/Gemini 的能力 | 인기 저장소에서 스킬을 찾아 설치하여 Claude Code/Codex/Gemini의 기능을 확장합니다 | Discover and install skills from popular repositories to extend Claude Code/Codex/Gemini capabilities | 已修订 |
| skills.refresh | 刷新 | 새로 고침 | Refresh | 保留 |
| skills.refreshing | 刷新中... | 새로 고치는 중... | Refreshing... | 保留 |
| skills.repoManager | 仓库管理 | 저장소 관리 | Repository Management | 保留 |
| skills.count | 共 {{count}} 个技能 | {{count}} 스킬 | {{count}} skills | 保留 |
| skills.empty | 暂无可用技能 | 사용 가능한 스킬이 없습니다 | No skills available | 已修订 |
| skills.emptyDescription | 添加技能仓库以发现可用的技能 | 스킬 저장소를 추가하여 설치 가능한 스킬을 찾아보세요 | Add skill repositories to discover available skills | 已修订 |
| skills.addRepo | 添加技能仓库 | 스킬 저장소 추가 | Add Skill Repository | 保留 |
| skills.loading | 加载中... | 로드 중... | Loading... | 保留 |
| skills.installed | 已安装 | 설치됨 | Installed | 保留 |
| skills.install | 安装 | 설치 | Install | 保留 |
| skills.installing | 安装中... | 설치 중... | Installing... | 保留 |
| skills.uninstall | 卸载 | 제거 | Uninstall | 保留 |
| skills.uninstalling | 卸载中... | 제거 중... | Uninstalling... | 保留 |
| skills.view | 查看 | 보기 | View | 保留 |
| skills.noDescription | 暂无描述 | 설명 없음 | No description | 保留 |
| skills.loadFailed | 加载失败 | 로드하지 못했습니다. | Failed to load | 保留 |
| skills.installSuccess | 技能 {{name}} 已安装 | 스킬 {{name}} 설치됨 | Skill {{name}} installed | 保留 |
| skills.installFailed | 安装失败 | 설치하지 못했습니다. | Failed to install | 保留 |
| skills.uninstallSuccess | 技能 {{name}} 已卸载 | 스킬 {{name}}가 제거되었습니다. | Skill {{name}} uninstalled | 保留 |
| skills.uninstallPiPreserved | 无法确认该 Pi 副本由 CC Switch 管理，已保留：{{path}} | Pi의 사본은 CC Switch 관리로 확인될 수 없으며 그대로 남아 있습니다: {{path}} | Pi's copy could not be verified as CC Switch-managed and was left in place: {{path}} | 保留 |
| skills.uninstallPiCleanupIncomplete | Pi 清理未能完成，请手动检查 Pi Skills 目录中是否有残留副本。 | Pi 정리를 완료할 수 없습니다. 남은 사본이 있는지 Pi Skills 디렉토리를 수동으로 확인하십시오. | Pi cleanup could not be completed. Check the Pi Skills directory manually for a leftover copy. | 保留 |
| skills.uninstallFailed | 卸载失败 | 제거하지 못했습니다. | Failed to uninstall | 保留 |
| skills.update | 更新 | 업데이트 | Update | 保留 |
| skills.updating | 更新中... | 업데이트 중... | Updating... | 保留 |
| skills.updateAvailable | 可更新 | 업데이트 | Update | 保留 |
| skills.updateSuccess | 技能 {{name}} 已更新到最新版本 | 스킬 {{name}}가 최신 버전으로 업데이트되었습니다. | Skill {{name}} updated to latest version | 保留 |
| skills.updateFailed | 更新失败 | 업데이트하지 못했습니다. | Failed to update | 保留 |
| skills.checkUpdates | 检查更新 | 업데이트 확인 | Check Updates | 保留 |
| skills.checkingUpdates | 检查中... | 확인 중... | Checking... | 保留 |
| skills.noUpdates | 所有技能已是最新版本 | 모든 스킬이 최신 상태입니다. | All skills are up to date | 保留 |
| skills.updateAll | 全部更新 ({{count}}) | 모두 업데이트({{count}}) | Update All ({{count}}) | 保留 |
| skills.updatingAll | 更新中... | 업데이트 중... | Updating... | 保留 |
| skills.updateAllSuccess | 已成功更新 {{count}} 个技能 | {{count}} 스킬을 성공적으로 업데이트했습니다. | Successfully updated {{count}} skill(s) | 保留 |
| skills.error.skillNotFound | 技能不存在：{{directory}} | 스킬을 찾을 수 없음: {{directory}} | Skill not found: {{directory}} | 保留 |
| skills.error.missingRepoInfo | 缺少仓库信息（owner 或 name） | 저장소 정보(owner 또는 name)가 없습니다 | Missing repository info (owner or name) | 已修订 |
| skills.error.downloadTimeout | 下载仓库 {{owner}}/{{name}} 超时（{{timeout}}秒） | 저장소 {{owner}}/{{name}} 다운로드 시간 초과 ({{timeout}}초) | Download repository {{owner}}/{{name}} timeout ({{timeout}}s) | 已修订 |
| skills.error.downloadTimeoutHint | 请检查网络连接或稍后重试 | 네트워크 연결을 확인하거나 나중에 다시 시도하세요. | Please check network connection or retry later | 保留 |
| skills.error.skillPathNotFound | 仓库 {{owner}}/{{name}} 中未找到技能路径 '{{path}}' | {{owner}}/{{name}} 저장소에서 스킬 경로 '{{path}}'을(를) 찾을 수 없습니다. | Skill path '{{path}}' not found in repository {{owner}}/{{name}} | 已修订 |
| skills.error.skillDirNotFound | 技能目录不存在：{{path}} | 스킬 디렉터리를 찾을 수 없습니다: {{path}} | Skill directory not found: {{path}} | 保留 |
| skills.error.directoryConflict | 技能目录 '{{directory}}' 已被 {{existing_repo}} 占用，无法从 {{new_repo}} 安装 | 스킬 디렉터리 '{{directory}}'는 이미 {{existing_repo}}에 의해 사용 중이므로 {{new_repo}}에서 설치할 수 없습니다. | Skill directory '{{directory}}' is already occupied by {{existing_repo}}, cannot install from {{new_repo}} | 保留 |
| skills.error.emptyArchive | 下载的压缩包为空 | 다운로드한 아카이브가 비어 있습니다. | Downloaded archive is empty | 保留 |
| skills.error.invalidRepoRef | 仓库地址不合法：{{owner}}/{{name}} | 잘못된 저장소 참조: {{owner}}/{{name}} | Invalid repository reference: {{owner}}/{{name}} | 保留 |
| skills.error.archiveTooLarge | 压缩包解压后超过 {{limit_mb}} MB 上限，已中止 | 아카이브가 {{limit_mb}} MB 추출 제한을 초과합니다. 중단됨 | Archive exceeds the {{limit_mb}} MB extraction limit; aborted | 保留 |
| skills.error.archiveDownloadTooLarge | 仓库压缩包下载超过 {{limit_mb}} MB 上限，已中止 | 저장소 아카이브 다운로드가 {{limit_mb}} MB 제한을 초과했습니다. 중단됨 | Repository archive download exceeds the {{limit_mb}} MB limit; aborted | 保留 |
| skills.error.archiveTooManyEntries | 压缩包条目过多（{{count}}），上限 {{limit}} | 아카이브에 항목이 너무 많습니다({{count}}). 한계는 {{limit}}입니다 | Archive has too many entries ({{count}}); the limit is {{limit}} | 保留 |
| skills.error.downloadFailed | 下载失败：HTTP {{status}} | 다운로드 실패: HTTP {{status}} | Download failed: HTTP {{status}} | 保留 |
| skills.error.allBranchesFailed | 所有分支下载失败，尝试了：{{branches}} | 모든 브랜치 다운로드에 실패했습니다. 시도한 브랜치: {{branches}} | All branches failed, tried: {{branches}} | 已修订 |
| skills.error.httpError | HTTP 错误 {{status}} | HTTP 오류 {{status}} | HTTP error {{status}} | 保留 |
| skills.error.http403 | GitHub 访问受限，可能是请求频率过高 | GitHub 접근이 제한되었습니다. 요청 빈도 제한일 수 있습니다 | GitHub access restricted, possibly rate limited | 已修订 |
| skills.error.http404 | 仓库或分支不存在，请检查地址 | 저장소 또는 분기를 찾을 수 없습니다. URL을 확인하세요. | Repository or branch not found, please check URL | 保留 |
| skills.error.http429 | 请求过于频繁，请等待后重试 | 요청이 너무 많습니다. 잠시 기다렸다가 다시 시도해 주세요. | Too many requests, please wait and retry | 保留 |
| skills.error.parseMetadataFailed | 解析技能元数据失败 | 스킬 메타데이터를 해석하지 못했습니다 | Failed to parse skill metadata | 已修订 |
| skills.error.getHomeDirFailed | 无法获取用户主目录 | 사용자 홈 디렉터리를 가져올 수 없습니다. | Unable to get user home directory | 保留 |
| skills.error.noSkillsInZip | ZIP 文件中未找到技能（需包含 SKILL.md 文件） | ZIP 파일에 스킬이 없습니다 (SKILL.md 파일 필요) | No skills found in ZIP file (requires SKILL.md file) | 已修订 |
| skills.error.networkError | 网络错误 | 네트워크 오류 | Network error | 保留 |
| skills.error.fsError | 文件系统错误 | 파일 시스템 오류 | File system error | 保留 |
| skills.error.unknownError | 未知错误 | 알 수 없는 오류 | Unknown error | 保留 |
| skills.error.suggestion.checkNetwork | 请检查网络连接 | 네트워크 연결을 확인해주세요 | Please check network connection | 保留 |
| skills.error.suggestion.checkProxy | 建议配置 HTTP 代理 | HTTP 프록시 설정을 고려하세요. | Consider configuring HTTP proxy | 已修订 |
| skills.error.suggestion.retryLater | 请稍后重试 | 나중에 다시 시도해 주세요. | Please retry later | 保留 |
| skills.error.suggestion.checkRepoUrl | 请检查仓库地址和分支名称 | 저장소 URL과 브랜치 이름을 확인하세요 | Please check repository URL and branch name | 已修订 |
| skills.error.suggestion.checkDiskSpace | 请检查磁盘空间 | 디스크 공간을 확인하세요 | Please check disk space | 保留 |
| skills.error.suggestion.checkPermission | 请检查目录权限 | 디렉터리 권한을 확인하세요. | Please check directory permissions | 保留 |
| skills.error.suggestion.uninstallFirst | 请先卸载已安装的同名技能 | 먼저 동일한 이름을 가진 기존 스킬을 제거하십시오. | Please uninstall the existing skill with the same name first | 保留 |
| skills.error.suggestion.checkZipContent | 请确认 ZIP 文件包含有效的技能目录（含 SKILL.md 文件） | ZIP 파일에 SKILL.md를 포함하는 유효한 스킬 디렉터리가 있는지 확인하세요 | Please verify the ZIP file contains valid skill directories (with SKILL.md files) | 已修订 |
| skills.repo.title | 管理技能仓库 | 스킬 저장소 관리 | Manage Skill Repositories | 已修订 |
| skills.repo.description | 添加或删除 GitHub 技能仓库源 | GitHub 스킬 저장소 추가 또는 제거 | Add or remove GitHub skill repository sources | 已修订 |
| skills.repo.url | 仓库 URL | 저장소 URL | Repository URL | 保留 |
| skills.repo.urlPlaceholder | owner/name 或 https://github.com/owner/name | owner/name 또는 https://github.com/owner/name | owner/name or https://github.com/owner/name | 已修订 |
| skills.repo.branch | 分支 | 브랜치 | Branch | 已修订 |
| skills.repo.branchPlaceholder | main | main | main | 已修订 |
| skills.repo.path | 技能路径 | Skills 경로 | Skills Path | 保留 |
| skills.repo.pathPlaceholder | skills (可选，留空扫描根目录) | skills (선택 사항, 비워 두면 루트 디렉터리 스캔) | skills (optional, leave empty for root) | 已修订 |
| skills.repo.add | 添加仓库 | 저장소 추가 | Add Repository | 保留 |
| skills.repo.list | 已添加的仓库 | 추가된 저장소 | Added Repositories | 保留 |
| skills.repo.empty | 暂无仓库 | 저장소 없음 | No repositories | 保留 |
| skills.repo.invalidUrl | 无效的仓库 URL 格式 | 잘못된 저장소 URL 형식 | Invalid repository URL format | 保留 |
| skills.repo.addSuccess | 仓库 {{owner}}/{{name}} 已添加，识别到 {{count}} 个技能 | 저장소 {{owner}}/{{name}}을(를) 추가하고 스킬 {{count}}개를 찾았습니다 | Repository {{owner}}/{{name}} added, detected {{count}} skills | 已修订 |
| skills.repo.addFailed | 添加失败 | 추가하지 못했습니다. | Failed to add | 保留 |
| skills.repo.removeSuccess | 仓库 {{owner}}/{{name}} 已删除 | 저장소 {{owner}}/{{name}}가 제거되었습니다. | Repository {{owner}}/{{name}} removed | 保留 |
| skills.repo.removeFailed | 删除失败 | 제거하지 못했습니다. | Failed to remove | 保留 |
| skills.repo.skillCount | 识别到 {{count}} 个技能 | {{count}} 스킬 감지됨 | {{count}} skills detected | 保留 |
| skills.search | 搜索技能 | Skills 검색 | Search Skills | 保留 |
| skills.searchPlaceholder | 搜索技能名称或仓库名称... | 스킬 이름 또는 저장소 검색... | Search skill name or repo... | 保留 |
| skills.installedSearchPlaceholder | 搜索已安装技能的名称、描述或仓库... | 설치된 스킬 이름, 설명, 저장소 검색... | Search installed skill name, description, or repo... | 保留 |
| skills.installedSearchAriaLabel | 搜索已安装技能 | 설치된 스킬 검색 | Search installed skills | 保留 |
| skills.noInstalledSearchResults | 未找到匹配的已安装技能 | 검색어와 일치하는 설치된 스킬이 없습니다 | No installed skills match your search | 已修订 |
| skills.searchSource.repos | 仓库 | 저장소 | Repos | 已修订 |
| skills.searchSource.skillssh | skills.sh | skills.sh | skills.sh | 保留 |
| skills.skillssh.searchPlaceholder | 搜索 skills.sh（至少 2 个字符）... | skills.sh 검색 (최소 2자)... | Search skills.sh (min 2 chars)... | 已修订 |
| skills.skillssh.installs | {{count}} 次安装 | {{count}} 설치 | {{count}} installs | 保留 |
| skills.skillssh.loadMore | 加载更多 | 더 로드하기 | Load More | 保留 |
| skills.skillssh.loading | 正在搜索 skills.sh... | skills.sh 검색 중... | Searching skills.sh... | 已修订 |
| skills.skillssh.noResults | 未找到 "{{query}}" 相关技能 | ‘{{query}}’ 관련 스킬이 없습니다 | No skills found for "{{query}}" | 已修订 |
| skills.skillssh.error | 搜索 skills.sh 失败 | skills.sh 검색 실패 | Failed to search skills.sh | 已修订 |
| skills.skillssh.poweredBy | 由 skills.sh 提供 | skills.sh 제공 | Powered by skills.sh | 已修订 |
| skills.filter.placeholder | 状态筛选 | 상태별로 필터링 | Filter by status | 保留 |
| skills.filter.all | 全部 | 모두 | All | 保留 |
| skills.filter.installed | 已安装 | 설치됨 | Installed | 保留 |
| skills.filter.uninstalled | 未安装 | 설치되지 않음 | Not installed | 保留 |
| skills.filter.repo | 仓库筛选 | 저장소로 필터링 | Filter by repo | 保留 |
| skills.filter.allRepos | 全部仓库 | 모든 저장소 | All repos | 保留 |
| skills.noResults | 未找到匹配的技能 | 일치하는 스킬이 없습니다 | No matching skills found | 已修订 |
| skills.noInstalled | 暂无已安装的技能 | 설치된 스킬 없음 | No skills installed | 保留 |
| skills.noInstalledDescription | 从仓库发现并安装技能，或导入已有的技能 | 저장소에서 스킬을 찾아 설치하거나 기존 스킬을 가져오세요 | Discover and install skills from repositories, or import existing skills | 已修订 |
| skills.discover | 发现技能 | Skills 살펴보기 | Discover Skills | 保留 |
| skills.import | 导入已有 | 기존 항목 가져오기 | Import Existing | 已修订 |
| skills.importDescription | 选择要导入到 CC Switch 统一管理的技能 | CC Switch에서 통합 관리할 스킬을 선택하세요 | Select skills to import into CC Switch unified management | 已修订 |
| skills.importSuccess | 成功导入 {{count}} 个技能 | 스킬 {{count}}개를 가져왔습니다 | Successfully imported {{count}} skills | 已修订 |
| skills.importSelected | 导入已选 ({{count}}) | 선택 항목 가져오기({{count}}) | Import Selected ({{count}}) | 保留 |
| skills.noUnmanagedFound | 未发现需要导入的技能。所有技能已在 CC Switch 统一管理中。 | 가져올 스킬이 없습니다. 모든 스킬은 이미 CC Switch에서 관리 중입니다. | No skills to import found. All skills are already managed by CC Switch. | 已修订 |
| skills.unmanagedAvailable | 发现可导入的技能 | Skills 가져오기 가능 | Skills available to import | 保留 |
| skills.foundIn | 发现于 | 다음에서 발견됨 | Found in | 保留 |
| skills.local | 本地 | 로컬 | Local | 已修订 |
| skills.uninstallConfirm | 确定要卸载技能 "{{name}}" 吗？这将从所有应用中移除该技能，并在删除前自动创建本地备份。 | 정말로 "{{name}}"을(를) 제거하시겠습니까? 이렇게 하면 모든 앱에서 스킬이 제거되고 먼저 로컬 백업이 생성됩니다. | Are you sure you want to uninstall "{{name}}"? This will remove the skill from all apps and create a local backup first. | 已修订 |
| skills.uninstallInMainPanel | 请在主面板中卸载技能 | 메인 패널에서 스킬을 제거하세요 | Please uninstall skills from the main panel | 保留 |
| skills.notFound | 未找到技能 | 스킬을 찾을 수 없습니다 | Skill not found | 已修订 |
| skills.backup.location | 备份位置: {{path}} | 백업 위치: {{path}} | Backup location: {{path}} | 保留 |
| skills.restoreFromBackup.button | 从备份中恢复 | 백업 복원 | Restore Backup | 保留 |
| skills.restoreFromBackup.title | 从备份中恢复 | 백업에서 복원 | Restore From Backup | 保留 |
| skills.restoreFromBackup.description | 选择一个 Skills 备份，将文件恢复到本地并重新加入当前列表。 | Skills 백업을 선택하여 파일을 로컬로 복원하고 현재 목록에 다시 추가하세요. | Choose a Skills backup to restore its files locally and add it back to the current list. | 保留 |
| skills.restoreFromBackup.empty | 暂无可恢复的 Skills 备份 | 복원할 수 있는 Skills 백업이 없습니다. | No Skills backups available to restore | 保留 |
| skills.restoreFromBackup.createdAt | 备份时间 | 백업 시간: | Backed up at | 保留 |
| skills.restoreFromBackup.path | 备份路径 | 백업 경로 | Backup path | 保留 |
| skills.restoreFromBackup.restore | 恢复 | 복원 | Restore | 已修订 |
| skills.restoreFromBackup.restoring | 恢复中... | 복원 중... | Restoring... | 保留 |
| skills.restoreFromBackup.delete | 删除 | 삭제 | Delete | 保留 |
| skills.restoreFromBackup.deleting | 删除中... | 삭제 중... | Deleting... | 保留 |
| skills.restoreFromBackup.deleteSuccess | 技能备份 {{name}} 已删除 | {{name}}에 대한 백업이 삭제되었습니다. | Deleted backup for {{name}} | 保留 |
| skills.restoreFromBackup.deleteFailed | 删除技能备份失败 | 스킬 백업 삭제 실패 | Failed to delete skill backup | 保留 |
| skills.restoreFromBackup.deleteConfirmTitle | 确认删除备份 | 백업 삭제 | Delete Backup | 保留 |
| skills.restoreFromBackup.deleteConfirmMessage | 确定要删除技能备份 "{{name}}" 吗？此操作无法撤销。 | "{{name}}"에 대한 백업을 삭제하시겠습니까? 이 작업은 취소할 수 없습니다. | Are you sure you want to delete the backup for "{{name}}"? This action cannot be undone. | 保留 |
| skills.restoreFromBackup.success | 技能 {{name}} 已从备份恢复 | 백업에서 복원된 스킬 {{name}} | Skill {{name}} restored from backup | 保留 |
| skills.restoreFromBackup.failed | 从备份恢复失败 | 백업에서 복원하지 못했습니다. | Failed to restore from backup | 保留 |
| skills.apps.claude | Claude | Claude | Claude | 已修订 |
| skills.apps.codex | Codex | Codex | Codex | 保留 |
| skills.apps.gemini | Gemini | Gemini | Gemini | 已修订 |
| skills.apps.opencode | OpenCode | OpenCode | OpenCode | 保留 |
| skills.apps.openclaw | OpenClaw | OpenClaw | OpenClaw | 保留 |
| skills.installFromZip.button | 从 ZIP 安装 | ZIP에서 설치 | Install from ZIP | 保留 |
| skills.installFromZip.installing | 安装中... | 설치 중... | Installing... | 保留 |
| skills.installFromZip.successSingle | 技能 {{name}} 已安装 | 스킬 {{name}} 설치됨 | Skill {{name}} installed | 保留 |
| skills.installFromZip.successMultiple | 成功安装 {{count}} 个技能 | {{count}} 스킬을 성공적으로 설치했습니다. | Successfully installed {{count}} skills | 保留 |
| skills.installFromZip.noSkillsFound | ZIP 文件中未找到技能（需包含 SKILL.md 文件） | ZIP 파일에 스킬이 없습니다 (SKILL.md 파일 필요) | No skills found in ZIP file (requires SKILL.md file) | 已修订 |
| skills.installFromZip.skippedTitle | 跳过了 {{count}} 个 Skill：目录名已被占用 | 건너뛴 {{count}} Skills: 폴더 이름이 이미 사용 중입니다. | Skipped {{count}} Skills: folder name already in use | 保留 |
| skills.installFromZip.allSkipped | 没有安装：ZIP 里的 {{count}} 个 Skill 目录名都已被占用 | 아무것도 설치되지 않음: ZIP의 모든 {{count}} Skills는 이미 사용된 폴더 이름을 사용합니다. | Nothing installed: all {{count}} Skills in the ZIP use folder names that are already taken | 保留 |
| skills.installFromZip.skippedItem | {{directory}}（已被 {{name}} 使用） | {{directory}}({{name}}에서 사용) | {{directory}} (used by {{name}}) | 保留 |
| skills.installFromZip.skippedBody | {{list}}。要换成 ZIP 里的版本，先卸载同名的 Skill 再安装。 | {{list}}. ZIP 버전을 사용하려면 먼저 같은 이름의 스킬을 제거하세요. | {{list}}. To use the version in the ZIP, uninstall the Skill with the same name first. | 保留 |
| skills.backToInstalled | 返回已安装 | 설치된 스킬로 돌아가기 | Back to installed | 已修订 |
| skills.moreActions | Skills 的更多操作 | 더 많은 Skills 작업 | More Skills actions | 保留 |
| skills.storageSheet.title | 存储与同步 | 저장 및 동기화 | Storage and sync | 保留 |
| skills.storageSheet.open | 存储与同步 | 저장 및 동기화 | Storage and sync | 保留 |
| skills.storageSheet.resync | 立即重新同步 | 지금 다시 동기화 | Resync now | 保留 |
| skills.storageSheet.resyncing | 正在重新同步… | 재동기화 중… | Resyncing… | 保留 |
| skills.storageSheet.resyncHint | 修改只对之后启用或更新的 Skill 生效。要让已启用的 Skill 也换成当前方式，点「立即重新同步」。 | 변경 사항은 나중에 활성화하거나 업데이트하는 Skills에만 적용됩니다. 이미 활성화된 Skills를 전환하려면 지금 다시 동기화하세요. | Changes only apply to Skills you enable or update afterwards. To switch Skills that are already enabled, resync now. | 保留 |
| skills.storageSheet.resyncDone | 已按当前方式把 Skill 重新同步到各应用 | 현재 방법을 사용하여 모든 앱에 Skills를 다시 동기화했습니다. | Resynced Skills to every app using the current method | 保留 |
| skills.storageSheet.resyncPartial | {{count}} 个应用没有同步完整：{{apps}} | {{count}} 앱이 완전히 동기화되지 않았습니다: {{apps}} | {{count}} apps didn't fully sync: {{apps}} | 保留 |
| skills.storageSheet.resyncSkillItem | {{directory}}：{{error}} | {{directory}}: {{error}} | {{directory}}: {{error}} | 保留 |
| skills.storageSheet.locationTitle | 主副本放在 | 원본 보관 위치 | Keep the master copies in | 已修订 |
| skills.storageSheet.locationCcSwitch | CC Switch 目录 | CC Switch 폴더 | CC Switch folder | 保留 |
| skills.storageSheet.locationUnified | 通用目录 | 공유 폴더 | Shared folder | 保留 |
| skills.storageSheet.openFolder | 打开 | 열기 | Open | 保留 |
| skills.storageSheet.openFolderAria | 打开 {{path}} | {{path}} 열기 | Open {{path}} | 保留 |
| skills.storageSheet.unifiedWarning | Codex、Gemini CLI、OpenCode 等会直接读这个目录，各应用的开关对它们不再完全生效。 | Codex, Gemini CLI, OpenCode 등은 이 폴더를 직접 읽으므로 앱별 스위치가 더 이상 완전히 적용되지 않습니다. | Codex, Gemini CLI, OpenCode and others read this folder directly, so the per-app switches no longer fully apply to them. | 保留 |
| skills.storageSheet.move | 移动并切换 | 이동 및 전환 | Move and switch | 保留 |
| skills.storageSheet.moving | 正在移动… | 이동 중… | Moving… | 已修订 |
| skills.storageSheet.moveConfirmTitle | 把 {{count}} 个 Skill 移到 {{path}}？ | {{count}} Skills를 {{path}}로 이동하시겠습니까? | Move {{count}} Skills to {{path}}? | 保留 |
| skills.storageSheet.moveConfirmBody | 会逐个移动主副本，再让各应用里的链接指向新位置。移动完成前请不要退出 CC Switch。 | 각 마스터 복사본이 이동된 다음 모든 앱의 링크가 새 위치를 가리킵니다. 이동이 완료될 때까지 CC Switch를 종료하지 마십시오. | Each master copy is moved, then the links in every app are pointed at the new location. Don't quit CC Switch until the move finishes. | 保留 |
| skills.storageSheet.moveConfirmButton | 移动并切换 | 이동 및 전환 | Move and switch | 保留 |
| skills.storageSheet.moveDone | 已把 {{count}} 个 Skill 移到 {{path}} | {{count}} Skills를 {{path}}로 이동했습니다. | Moved {{count}} Skills to {{path}} | 保留 |
| skills.storageSheet.movePartial | 移动了 {{migrated}} 个 Skill，{{errors}} 个失败，请查看日志 | 스킬 {{migrated}}개 이동, {{errors}}개 실패. 자세한 내용은 로그를 확인하세요. | Moved {{migrated}} Skills, {{errors}} failed. Check the logs for details. | 已修订 |
| skills.storageSheet.syncTitle | 同步到各应用的方式 | 앱별 스킬 동기화 방식 | How Skills reach each app | 已修订 |
| skills.storageSheet.syncAuto | 自动：优先用软链接，失败时复制（推荐） | 자동: 먼저 심볼릭 링크를 연결하고, 실패하면 복사합니다(권장) | Automatic: symlink first, copy if that fails (recommended) | 保留 |
| skills.storageSheet.syncSymlink | 只用软链接 | 심볼릭 링크만 | Symlink only | 保留 |
| skills.storageSheet.syncSymlinkDesc | Windows 需要开启开发者模式 | Windows에서는 개발자 모드가 필요합니다. | Requires Developer Mode on Windows | 保留 |
| skills.storageSheet.syncCopy | 只用复制 | 복사만 사용 | Copy only | 已修订 |
| skills.storageSheet.syncCopyDesc | 占用更多空间，更新后会重新复制 | 더 많은 디스크 공간을 사용합니다. 업데이트할 때마다 다시 복사됨 | Uses more disk space; copied again after each update | 保留 |
| skills.storageSheet.moveHint | 切换位置会把 {{count}} 个 Skill 移动过去。 | 전환하면 {{count}} Skills가 새 위치로 이동됩니다. | Switching moves {{count}} Skills to the new location. | 保留 |
| skills.updatesIncomplete | 没有发现更新，但有 {{count}} 个仓库没有读到 | 업데이트를 찾을 수 없지만 {{count}} 저장소를 읽을 수 없습니다. | No updates found, but {{count}} repositories couldn't be read | 保留 |
| deeplink.confirmImport | 确认导入供应商配置 | 공급자 가져오기 확인 | Confirm Import Provider | 已修订 |
| deeplink.confirmImportDescription | 以下配置将导入到 CC Switch | 다음 설정은 딥 링크에서 CC Switch로 가져옵니다. | The following configuration will be imported from deep link into CC Switch | 已修订 |
| deeplink.importPrompt | 导入提示词 | 프롬프트 가져오기 | Import Prompt | 已修订 |
| deeplink.importPromptDescription | 请确认是否导入此系统提示词 | 이 시스템 프롬프트를 가져올지 확인하세요 | Please confirm whether to import this system prompt | 已修订 |
| deeplink.importMcp | 导入 MCP Servers | MCP 서버 가져오기 | Import MCP Servers | 保留 |
| deeplink.importMcpDescription | 请确认是否导入这些 MCP Servers | 이 MCP 서버를 가져올지 여부를 확인하세요. | Please confirm whether to import these MCP Servers | 保留 |
| deeplink.importSkill | 添加 Skill 仓库 | 스킬 저장소 추가 | Add Skill Repository | 保留 |
| deeplink.importSkillDescription | 请确认是否添加此 Skill 仓库 | 이 스킬 저장소를 추가할지 확인하세요 | Please confirm whether to add this Skill repository | 已修订 |
| deeplink.promptImportSuccess | 提示词导入成功 | 프롬프트를 성공적으로 가져왔습니다. | Prompt imported successfully | 保留 |
| deeplink.promptImportSuccessDescription | 已导入提示词: {{name}} | 가져온 프롬프트: {{name}} | Imported prompt: {{name}} | 保留 |
| deeplink.mcpImportSuccess | MCP Servers 导入成功 | MCP 서버를 성공적으로 가져왔습니다. | MCP Servers imported successfully | 保留 |
| deeplink.mcpImportSuccessDescription | 成功导入 {{count}} 个服务器 | {{count}} 서버를 성공적으로 가져왔습니다. | Successfully imported {{count}} server(s) | 保留 |
| deeplink.mcpPartialSuccess | 部分导入成功 | 부분 가져오기 성공 | Partial import success | 保留 |
| deeplink.mcpPartialSuccessDescription | 成功: {{success}}, 失败: {{failed}} | 성공: {{success}}, 실패: {{failed}} | Success: {{success}}, Failed: {{failed}} | 保留 |
| deeplink.skillImportSuccess | Skill 仓库添加成功 | 스킬 저장소가 성공적으로 추가되었습니다. | Skill repository added successfully | 保留 |
| deeplink.skillImportSuccessDescription | 已添加仓库: {{repo}} | 추가된 저장소: {{repo}} | Added repository: {{repo}} | 保留 |
| deeplink.app | 应用类型 | 앱 유형 | App Type | 保留 |
| deeplink.providerName | 供应商名称 | 공급자 이름 | Provider Name | 已修订 |
| deeplink.homepage | 官网地址 | 홈페이지 | Homepage | 保留 |
| deeplink.endpoint | API 端点 | API 엔드포인트 | API Endpoint | 保留 |
| deeplink.apiKey | API 密钥 | API 키 | API Key | 保留 |
| deeplink.icon | 图标 | 아이콘 | Icon | 已修订 |
| deeplink.model | 模型 | 모델 | Model | 保留 |
| deeplink.haikuModel | Haiku 模型 | Haiku 모델 | Haiku Model | 已修订 |
| deeplink.sonnetModel | Sonnet 模型 | Sonnet 모델 | Sonnet Model | 已修订 |
| deeplink.opusModel | Opus 模型 | Opus 모델 | Opus Model | 已修订 |
| deeplink.multiModel | 多模态模型 | 멀티모달 모델 | Multi-Modal Model | 已修订 |
| deeplink.notes | 备注 | 메모 | Notes | 保留 |
| deeplink.import | 导入 | 가져오기 | Import | 保留 |
| deeplink.importing | 导入中... | 가져오는 중... | Importing... | 保留 |
| deeplink.warning | 请确认以上信息准确无误后再导入。导入后可在供应商列表中编辑或删除。 | 가져오기 전에 위의 정보가 올바른지 확인하세요. 나중에 공급자 목록에서 편집하거나 삭제할 수 있습니다. | Please confirm the information above is correct before importing. You can edit or delete it later in the provider list. | 已修订 |
| deeplink.providerEnabledWarning | 导入后将立即切换到此供应商，客户端请求会改发到上面的地址 | 가져온 후 CC Switch는 즉시 이 공급자로 전환하고 클라이언트 요청은 위의 끝점으로 이동합니다. | After import, CC Switch will switch to this provider immediately, and client requests will go to the endpoint above | 已修订 |
| deeplink.apiFormat | 接口格式 | API 형식 | API format | 保留 |
| deeplink.switchAfterImport | 导入后立即切换到这个供应商 | 가져온 후 이 공급자로 전환 | Switch to this provider after import | 已修订 |
| deeplink.addToAppAfterImport | 导入后立即添加到 {{app}} 配置 | 가져온 후 {{app}} 설정에 추가 | Add to the {{app}} config after import | 已修订 |
| deeplink.enableInPiAfterImport | 导入后立即在 Pi 中启用 | 가져온 후 Pi에서 활성화 | Enable in Pi after import | 保留 |
| deeplink.parseError | 深链接解析失败 | 딥링크를 파싱하지 못했습니다. | Failed to parse deep link | 保留 |
| deeplink.importSuccess | 导入成功 | 가져오기 성공 | Import successful | 保留 |
| deeplink.importSuccessDescription | 供应商 "{{name}}" 已成功导入 | 공급자 "{{name}}"을(를) 성공적으로 가져왔습니다. | Provider "{{name}}" has been successfully imported | 已修订 |
| deeplink.importError | 导入失败 | 가져오지 못했습니다. | Failed to import | 保留 |
| deeplink.configSource | 配置来源 | 설정 소스 | Config Source | 已修订 |
| deeplink.codexConfigScopeHint | 只导入其中属于这个供应商的设置（地址、鉴权、模型、推理强度等）；[features]、MCP、权限这类全局设置不会导入。 | 이 공급자에 속한 설정(엔드포인트, 인증, 모델, 추론 수준 등)만 가져옵니다. [features], MCP, 권한 같은 전역 설정은 가져오지 않습니다. | Only the settings that belong to this provider (endpoint, auth, model, reasoning effort, etc.) are imported; global settings such as [features], MCP and permissions are skipped. | 已修订 |
| deeplink.grokConfigScopeHint | 只导入 [models] default 指向的那张模型表（显示名、说明、接口类型、窗口等）；地址和 Key 用链接参数，其他模型表不导入。 | [models]의 default가 가리키는 모델 테이블(표시 이름, 설명, API 유형, 컨텍스트 창 등)만 가져옵니다. 엔드포인트와 API 키는 링크 매개변수를 사용하며 다른 모델 테이블은 가져오지 않습니다. | Only the model table named by [models] default is imported (display name, description, API backend, context window, etc.); the endpoint and key come from the link parameters, and other model tables are skipped. | 已修订 |
| deeplink.configEmbedded | 内嵌配置 | 내장된 설정 | Embedded Config | 已修订 |
| deeplink.configRemote | 远程配置 | 원격 설정 | Remote Config | 已修订 |
| deeplink.configDetails | 配置详情 | 설정 세부정보 | Config Details | 已修订 |
| deeplink.configUrl | 配置文件 URL | 설정 파일 URL | Config File URL | 已修订 |
| deeplink.configMergeError | 合并配置文件失败 | 설정 파일을 병합하지 못했습니다. | Failed to merge configuration file | 已修订 |
| deeplink.primaryEndpoint | 主 | 주 엔드포인트 | Primary | 已修订 |
| deeplink.mcp.title | 批量导入 MCP Servers | MCP 서버 일괄 가져오기 | Batch Import MCP Servers | 保留 |
| deeplink.mcp.targetApps | 目标应用 | 대상 앱 | Target Apps | 保留 |
| deeplink.mcp.serverCount | MCP Servers ({{count}} 个) | MCP 서버({{count}}) | MCP Servers ({{count}}) | 保留 |
| deeplink.mcp.enabledWarning | 导入后将立即写入所有指定应用的配置文件 | 가져오면 지정한 모든 앱의 설정 파일에 즉시 저장됩니다. | After import, configurations will be written to all specified apps immediately | 已修订 |
| deeplink.mcp.command | 命令 | 명령 | Command | 保留 |
| deeplink.mcp.args | 参数 | 인수 | Args | 保留 |
| deeplink.mcp.env | 环境 | 환경 | Env | 保留 |
| deeplink.mcp.url | 地址 | URL | URL | 保留 |
| deeplink.prompt.title | 导入系统提示词 | 시스템 프롬프트 가져오기 | Import System Prompt | 保留 |
| deeplink.prompt.app | 应用 | 앱 | App | 保留 |
| deeplink.prompt.name | 名称 | 이름 | Name | 保留 |
| deeplink.prompt.description | 描述 | 설명 | Description | 保留 |
| deeplink.prompt.contentPreview | 内容预览 | 콘텐츠 미리보기 | Content Preview | 保留 |
| deeplink.prompt.enabledWarning | 导入后将立即启用此提示词，其他提示词将被禁用 | 가져온 후에는 이 프롬프트가 즉시 활성화되고 다른 프롬프트는 비활성화됩니다. | After import, this prompt will be enabled immediately and other prompts will be disabled | 保留 |
| deeplink.prompt.enableAfterImport | 导入后立即启用 | 가져온 후 활성화 | Enable after import | 保留 |
| deeplink.skill.title | 添加 Claude Skill 仓库 | Claude 스킬 저장소 추가 | Add Claude Skill Repository | 已修订 |
| deeplink.skill.repo | GitHub 仓库 | GitHub 저장소 | GitHub Repository | 保留 |
| deeplink.skill.directory | 目标目录 | 대상 디렉터리 | Target Directory | 保留 |
| deeplink.skill.branch | 分支 | 브랜치 | Branch | 已修订 |
| deeplink.skill.skillsPath | Skills 路径 | Skills 경로 | Skills Path | 保留 |
| deeplink.skill.hint | 此操作将添加 Skill 仓库到列表。 | 그러면 스킬 저장소가 목록에 추가됩니다. | This will add the Skill repository to the list. | 保留 |
| deeplink.skill.hintDetail | 添加后，您可以在 Skills 管理界面中选择安装具体的 Skill。 | 추가 후 Skills 관리 페이지에서 특정 Skills를 설치할 수 있습니다. | After adding, you can install specific Skills from the Skills management page. | 保留 |
| deeplink.usageScript | 用量查询 | 사용량 조회 | Usage Query | 保留 |
| deeplink.usageScriptEnabled | 已启用 | 활성화됨 | Enabled | 保留 |
| deeplink.usageScriptDisabled | 未启用 | 비활성화됨 | Disabled | 保留 |
| deeplink.usageCodingPlan | 套餐额度：{{name}} | 요금제 할당량: {{name}} | Plan quota: {{name}} | 已修订 |
| deeplink.usageScriptCode | 脚本代码 | 스크립트 코드 | Script code | 保留 |
| deeplink.usageScriptWarning | 这是一段 JavaScript 代码，启用后会在查询用量时执行。请确认来源可信后再导入。 | 활성화하면 사용량을 조회할 때 실행되는 JavaScript 코드입니다. 출처를 신뢰할 수 있을 때만 가져오세요. | This is JavaScript that runs when usage is queried, once enabled. Import it only if you trust the source. | 已修订 |
| deeplink.usageApiKey | 用量 API Key | 사용량 API 키 | Usage API Key | 已修订 |
| deeplink.usageBaseUrl | 用量查询地址 | 사용량 조회 URL | Usage Query URL | 已修订 |
| deeplink.usageAccessToken | 用量访问令牌 | 사용량 조회 액세스 토큰 | Usage Access Token | 已修订 |
| deeplink.usageUserId | 用量用户 ID | 사용량 조회 사용자 ID | Usage User ID | 已修订 |
| deeplink.usageAutoInterval | 自动查询 | 자동 조회 | Auto Query | 已修订 |
| deeplink.usageAutoIntervalValue | 每 {{minutes}} 分钟 | {{minutes}}분마다 | Every {{minutes}} minutes | 保留 |
| deeplink.risk.envHijack | 该配置包含可改变进程加载行为的环境变量（如注入动态库、替换 CA 证书），请确认来源可信。 | 이 설정에는 프로세스의 로드 동작을 변경할 수 있는 환경 변수(예: 동적 라이브러리 주입, CA 인증서 교체)가 포함되어 있습니다. 출처를 신뢰할 수 있는지 확인하세요. | This config sets environment variables that change how processes load code (e.g. injecting libraries or replacing CA certificates). Import only from a source you trust. | 已修订 |
| deeplink.risk.privateEndpoint | 该地址指向本机或内网。若非你自建的本地服务，请勿导入。 | 이 주소는 localhost 또는 개인 네트워크를 가리킵니다. 자체 로컬 서비스가 아닌 이상 가져오지 마세요. | This address points at localhost or a private network. Do not import unless it is your own local service. | 保留 |
| deeplink.risk.shellCommand | 该配置通过 shell 执行一整段命令，实际运行的内容在参数里，请逐行核对。 | 이 설정은 셸을 통해 전체 명령줄을 실행합니다. 실제로 실행되는 것은 인수에 있습니다. 각 줄을 검토하세요. | This config runs a full command line through a shell — what actually executes is in the arguments. Review each line. | 已修订 |
| iconPicker.search | 搜索图标 | 아이콘 검색 | Search Icons | 已修订 |
| iconPicker.searchPlaceholder | 输入图标名称... | 아이콘 이름을 입력하세요... | Enter icon name... | 保留 |
| iconPicker.noResults | 未找到匹配的图标 | 일치하는 아이콘이 없습니다. | No matching icons found | 保留 |
| iconPicker.clear | 清除图标 | 아이콘 지우기 | Clear icon | 保留 |
| iconPicker.myIcons | 我的图标 | 내 아이콘 | My Icons | 保留 |
| iconPicker.builtinIcons | 内置图标 | 내장 아이콘 | Built-in Icons | 保留 |
| iconPicker.myIconsEmpty | 上传的图片起好名字后存在这里，其他供应商也能直接选用。 | 귀하가 업로드하고 이름을 지정한 이미지는 여기에 보관되므로 다른 공급자도 해당 이미지를 사용할 수 있습니다. | Images you upload and name are kept here, so other providers can use them too. | 已修订 |
| iconPicker.currentIcon | 当前图标 | 현재 아이콘 | Current icon | 保留 |
| iconPicker.saveToLibrary | 存入我的图标 | 내 아이콘에 저장 | Save to My Icons | 保留 |
| iconPicker.saveCurrentTitle | 把当前图标存入「我的图标」 | 현재 아이콘을 내 아이콘에 저장 | Save the current icon to My Icons | 保留 |
| iconPicker.uploadTitle | 给图标起个名字 | 이 아이콘의 이름을 지정하세요. | Name this icon | 保留 |
| iconPicker.uploadDescription | 存进「我的图标」后，其他供应商也能直接选用。 | 내 아이콘에 있으면 다른 공급자도 사용할 수 있습니다. | Once it is in My Icons, other providers can use it too. | 已修订 |
| iconPicker.saveAndUse | 保存并使用 | 저장 및 사용 | Save and Use | 保留 |
| iconPicker.renameTitle | 重命名图标 | 아이콘 이름 바꾸기 | Rename Icon | 保留 |
| iconPicker.rename | 重命名 | 이름 바꾸기 | Rename | 保留 |
| iconPicker.delete | 删除 | 삭제 | Delete | 保留 |
| iconPicker.deleteTitle | 删除图标 | 아이콘 삭제 | Delete Icon | 保留 |
| iconPicker.deleteMessage | 从「我的图标」中删除「{{name}}」？已经在用它的供应商不受影响。 | 내 아이콘에서 "{{name}}"을(를) 삭제하시겠습니까? 이미 이를 사용하고 있는 공급자는 영향을 받지 않습니다. | Delete "{{name}}" from My Icons? Providers already using it are not affected. | 已修订 |
| iconPicker.alreadySaved | 这张图片已经在「我的图标」里了，名为「{{name}}」 | 이 이미지는 이미 내 아이콘에 "{{name}}"로 있습니다. | This image is already in My Icons as "{{name}}" | 保留 |
| iconPicker.nameLabel | 名称 | 이름 | Name | 保留 |
| iconPicker.namePlaceholder | 例如：我的中转站 | 예를 들어 나의 릴레이 | e.g. My relay | 保留 |
| iconPicker.upload | 上传 | 업로드 | Upload | 保留 |
| iconPicker.uploadHint | 支持 PNG、JPG、WebP、SVG，不超过 2 MB。图片会缩成小尺寸 PNG 存进「我的图标」，随云同步一起带走。 | PNG, JPG, WebP 또는 SVG(최대 2MB) 이미지는 작은 PNG로 축소되어 내 아이콘에 저장되고 클라우드 동기화를 통해 전달됩니다. | PNG, JPG, WebP or SVG, up to 2 MB. The image is shrunk to a small PNG, saved to My Icons and carried along by cloud sync. | 保留 |
| iconPicker.uploadError.unsupported | 不支持这种图片格式，请选择 PNG、JPG、WebP 或 SVG | 지원되지 않는 이미지 형식입니다. PNG, JPG, WebP 또는 SVG 파일을 선택하세요 | Unsupported image format. Choose a PNG, JPG, WebP or SVG file | 保留 |
| iconPicker.uploadError.tooLarge | 图片超过 2 MB | 이미지가 2MB보다 큽니다. | The image is larger than 2 MB | 保留 |
| iconPicker.uploadError.decodeFailed | 无法读取这张图片，请换一张试试 | 이 이미지를 읽을 수 없습니다. 다른 이미지를 시도해 보세요. | Couldn't read this image, please try another one | 保留 |
| iconPicker.uploadError.dimensions | 图片尺寸太大（宽高不能超过 4096 像素） | 이미지가 너무 큽니다(너비와 높이는 4096픽셀을 초과할 수 없음). | The image is too large (width and height must not exceed 4096 px) | 保留 |
| iconPicker.category.aiProvider | AI 服务商 | AI 공급자 | AI Providers | 已修订 |
| iconPicker.category.cloud | 云平台 | 클라우드 플랫폼 | Cloud Platforms | 保留 |
| iconPicker.category.tool | 开发工具 | 개발 도구 | Dev Tools | 保留 |
| iconPicker.category.other | 其他 | 기타 | Other | 已修订 |
| providerIcon.label | 图标 | 아이콘 | Icon | 已修订 |
| providerIcon.colorLabel | 图标颜色 | 아이콘 색상 | Icon Color | 保留 |
| providerIcon.selectIcon | 选择图标 | 아이콘 선택 | Select Icon | 保留 |
| providerIcon.preview | 预览 | 미리보기 | Preview | 已修订 |
| providerIcon.clickToChange | 点击更换图标 | 아이콘을 변경하려면 클릭하세요. | Click to change icon | 保留 |
| providerIcon.clickToSelect | 点击选择图标 | 아이콘을 선택하려면 클릭하세요. | Click to select icon | 保留 |
| providerIcon.change | 更换图标 | 아이콘 변경 | Change icon | 保留 |
| migration.success | 配置迁移成功 | 설정이 성공적으로 마이그레이션되었습니다. | Configuration migrated successfully | 已修订 |
| migration.skillsSuccess | 已自动导入 {{count}} 个技能到统一管理 | 스킬 {{count}}개를 통합 관리에 자동으로 가져왔습니다 | Automatically imported {{count}} skill(s) into unified management | 已修订 |
| migration.skillsFailed | 自动导入技能失败 | 스킬 자동 가져오기 실패 | Failed to auto import skills | 保留 |
| migration.skillsFailedDescription | 请打开 Skills 页面点击“导入已有”手动导入（或重启后再试）。 | Skills 페이지를 열고 "기존 항목 가져오기"를 클릭하여 수동으로 가져오거나 다시 시작한 후 다시 시도하세요. | Open the Skills page and click "Import Existing" to import manually (or restart and try again). | 保留 |
| health.operational | 正常 | 정상 | Operational | 已修订 |
| health.degraded | 降级 | 성능 저하 | Degraded | 已修订 |
| health.failed | 失败 | 실패 | Failed | 已修订 |
| health.circuitOpen | 熔断 | 서킷 브레이커 열림 | Circuit Open | 已修订 |
| health.consecutiveFailures | 连续失败 {{count}} 次 | {{count}} 연속 실패 | {{count}} consecutive failures | 保留 |
| failover.enabled | {{app}} 故障转移已启用 | {{app}} 장애 조치 활성화됨 | {{app}} failover enabled | 保留 |
| failover.disabled | {{app}} 故障转移已关闭 | {{app}} 장애 조치가 비활성화되었습니다. | {{app}} failover disabled | 保留 |
| failover.toggleFailed | 操作失败: {{detail}} | 작업 실패: {{detail}} | Operation failed: {{detail}} | 保留 |
| failover.queueAddFailed | 加入队列失败：{{detail}} | 대기열에 추가하지 못했습니다: {{detail}} | Failed to add to the queue: {{detail}} | 保留 |
| failover.queueRemoveFailed | 移出队列失败：{{detail}} | 대기열에서 제거하지 못했습니다: {{detail}} | Failed to remove from the queue: {{detail}} | 保留 |
| failover.inQueue | 已加入 | 대기열에 있음 | In queue | 保留 |
| failover.addQueue | 加入 | 추가 | Add | 已修订 |
| failover.priority.tooltip | 故障转移优先级 {{priority}} | 장애 조치 우선 순위 {{priority}} | Failover priority {{priority}} | 保留 |
| failover.tooltip.enabled | {{app}} 故障转移已启用<br>按队列优先级（P1→P2→...）选择供应商 | {{app}} 장애 조치 활성화됨<br>요청은 대기열 우선순위를 따릅니다(P1→P2→...) | {{app}} failover enabled<br>Requests follow queue priority (P1→P2→...) | 保留 |
| failover.tooltip.disabled | 启用 {{app}} 故障转移<br>将立即切换到队列 P1，并在失败时自动切换到下一个 | {{app}} 장애 조치 활성화<br>즉시 대기열 P1로 전환한 다음 오류 발생 시 폴백합니다. | Enable {{app}} failover<br>Switches to queue P1 immediately, then falls back on failures | 保留 |
| failover.tooltip.takeoverRequired | 请先接管 {{app}}，再启用故障转移 | 먼저 {{app}}의 요청을 라우팅 서비스에서 관리하도록 설정한 뒤 장애 조치를 켜세요 | Take over {{app}} first, then enable failover | 已修订 |
| proxy.panel.serviceAddress | 服务地址 | 서비스 주소 | Service Address | 保留 |
| proxy.panel.addressCopied | 地址已复制 | 주소가 복사되었습니다 | Address copied | 保留 |
| proxy.panel.currentProvider | 当前 Provider： | 현재 공급자: | Current Provider: | 已修订 |
| proxy.panel.waitingFirstRequest | 当前 Provider：等待首次请求… | 현재 공급자: 첫 요청 대기 중... | Current Provider: Waiting for first request... | 已修订 |
| proxy.panel.stoppedTitle | 路由服务已停止 | 라우팅 서비스가 중지되었습니다. | Routing Service Stopped | 保留 |
| proxy.panel.stoppedDescription | 使用上方开关即可启动服务 | 위의 토글을 사용하여 서비스를 시작하세요. | Use the toggle above to start the service | 保留 |
| proxy.panel.openSettings | 配置路由服务 | 라우팅 서비스 설정 | Configure Routing Service | 已修订 |
| proxy.panel.stats.activeConnections | 活跃连接 | 활성 연결 | Active Connections | 保留 |
| proxy.panel.stats.totalRequests | 总请求数 | 총 요청 | Total Requests | 保留 |
| proxy.panel.stats.successRate | 成功率 | 성공률 | Success Rate | 保留 |
| proxy.panel.stats.uptime | 运行时间 | 가동 시간 | Uptime | 保留 |
| proxy.settings.title | 路由服务设置 | 라우팅 서비스 설정 | Routing Service Settings | 保留 |
| proxy.settings.description | 配置本地路由服务器的监听地址、端口和运行参数，保存后立即生效。 | 로컬 라우팅 서버 수신 주소, 포트 및 런타임 매개변수를 설정합니다. 변경사항은 저장 후 즉시 적용됩니다. | Configure local routing server listening address, port and runtime parameters. Changes take effect immediately after saving. | 已修订 |
| proxy.settings.alert.autoApply | 保存后将自动同步到正在运行的路由服务，无需手动重启。 | 변경 사항은 수동으로 다시 시작하지 않고도 실행 중인 라우팅 서비스에 자동으로 동기화됩니다. | Changes will be automatically synced to the running routing service without manual restart. | 保留 |
| proxy.settings.basic.title | 基础设置 | 기본 설정 | Basic Settings | 保留 |
| proxy.settings.basic.description | 配置路由服务监听的地址与端口。 | 라우팅 서비스 수신 주소 및 포트를 설정합니다. | Configure routing service listening address and port. | 已修订 |
| proxy.settings.advanced.title | 高级参数 | 고급 매개변수 | Advanced Parameters | 保留 |
| proxy.settings.advanced.description | 控制请求的稳定性和日志记录。 | 요청 안정성 및 로깅을 제어합니다. | Control request stability and logging. | 保留 |
| proxy.settings.timeout.title | 超时设置 | 시간 초과 설정 | Timeout Settings | 保留 |
| proxy.settings.timeout.description | 配置流式和非流式请求的超时时间。 | 스트리밍 및 비스트리밍 요청에 대한 시간 제한을 설정합니다. | Configure timeout for streaming and non-streaming requests. | 已修订 |
| proxy.settings.fields.listenAddress.label | 监听地址 | 수신 주소 | Listen Address | 已修订 |
| proxy.settings.fields.listenAddress.placeholder | 127.0.0.1 | 127.0.0.1 | 127.0.0.1 | 保留 |
| proxy.settings.fields.listenAddress.description | 路由服务器监听的 IP 地址（推荐 127.0.0.1） | 라우팅 서버가 수신하는 IP 주소(권장: 127.0.0.1) | IP address the routing server listens on (recommended: 127.0.0.1) | 保留 |
| proxy.settings.fields.listenPort.label | 监听端口 | 수신 포트 | Listen Port | 已修订 |
| proxy.settings.fields.listenPort.placeholder | 15721 | 15721 | 15721 | 保留 |
| proxy.settings.fields.listenPort.description | 路由服务器监听的端口号（1024 ~ 65535） | 라우팅 서버가 수신하는 포트 번호 (1024 ~ 65535) | Port number the routing server listens on (1024 ~ 65535) | 保留 |
| proxy.settings.fields.maxRetries.label | 最大重试次数 | 최대 재시도 횟수 | Max Retries | 保留 |
| proxy.settings.fields.maxRetries.placeholder | 3 | 3 | 3 | 保留 |
| proxy.settings.fields.maxRetries.description | 请求失败时的重试次数（0 ~ 10） | 요청 실패 시 재시도 횟수 (0 ~ 10) | Number of retries on request failure (0 ~ 10) | 保留 |
| proxy.settings.fields.requestTimeout.label | 请求超时（秒） | 요청 시간 초과(초) | Request Timeout (sec) | 保留 |
| proxy.settings.fields.requestTimeout.placeholder | 0（不限）或 300 | 0(무제한) 또는 300 | 0 (unlimited) or 300 | 保留 |
| proxy.settings.fields.requestTimeout.description | 单个请求的最大等待时间（0 表示不限制，或设置 10 ~ 600 秒） | 단일 요청에 대한 최대 대기 시간(0 = 무제한 또는 10~600초) | Maximum wait time for a single request (0 = unlimited, or 10 ~ 600 seconds) | 保留 |
| proxy.settings.fields.enableLogging.label | 记录请求用量 | 요청 사용량 기록 | Record Request Usage | 已修订 |
| proxy.settings.fields.enableLogging.description | 将路由请求的用量与状态写入本地统计数据库 | 라우팅 요청 사용 및 상태를 로컬 통계 데이터베이스에 기록합니다. | Write routing request usage and status to the local statistics database | 保留 |
| proxy.settings.fields.streamingFirstByteTimeout.label | 流式首字超时（秒） | 스트리밍 첫 번째 바이트 시간 초과(초) | Streaming First Byte Timeout (sec) | 保留 |
| proxy.settings.fields.streamingFirstByteTimeout.description | 等待首个数据块的最大时间 | 첫 번째 데이터 청크를 기다리는 최대 시간 | Maximum time to wait for the first data chunk | 保留 |
| proxy.settings.fields.streamingIdleTimeout.label | 流式静默超时（秒） | 스트리밍 유휴 시간 초과(초) | Streaming Idle Timeout (sec) | 保留 |
| proxy.settings.fields.streamingIdleTimeout.description | 数据块之间的最大间隔 | 데이터 청크 사이의 최대 간격 | Maximum interval between data chunks | 保留 |
| proxy.settings.fields.nonStreamingTimeout.label | 非流式超时（秒） | 비스트리밍 시간 초과(초) | Non-Streaming Timeout (sec) | 保留 |
| proxy.settings.fields.nonStreamingTimeout.description | 非流式请求的总超时时间 | 스트리밍되지 않는 요청의 총 시간 초과 | Total timeout for non-streaming requests | 保留 |
| proxy.settings.validation.addressInvalid | 请输入有效的IP地址 | 유효한 IP 주소를 입력하세요. | Please enter a valid IP address | 保留 |
| proxy.settings.validation.portMin | 端口必须大于1024 | 포트는 1024보다 커야 합니다. | Port must be greater than 1024 | 保留 |
| proxy.settings.validation.portMax | 端口必须小于65535 | 포트는 65535보다 작아야 합니다. | Port must be less than 65535 | 保留 |
| proxy.settings.validation.retryMin | 重试次数不能为负 | 재시도 횟수는 음수일 수 없습니다. | Retry count cannot be negative | 保留 |
| proxy.settings.validation.retryMax | 重试次数不能超过10 | 재시도 횟수는 10을 초과할 수 없습니다. | Retry count cannot exceed 10 | 保留 |
| proxy.settings.validation.timeoutNonNegative | 超时时间不能为负数 | 시간 초과는 음수일 수 없습니다. | Timeout cannot be negative | 保留 |
| proxy.settings.validation.timeoutMax | 超时时间最多600秒 | 시간 초과는 600초를 초과할 수 없습니다. | Timeout cannot exceed 600 seconds | 保留 |
| proxy.settings.validation.timeoutRange | 请输入 0 或 10-600 之间的数值 | 0 또는 10~600 사이의 값을 입력하세요. | Please enter 0 or a value between 10-600 | 保留 |
| proxy.settings.validation.streamingTimeoutMin | 超时时间至少5秒 | 시간 초과는 5초 이상이어야 합니다. | Timeout must be at least 5 seconds | 保留 |
| proxy.settings.validation.streamingTimeoutMax | 超时时间最多300秒 | 시간 초과는 300초를 초과할 수 없습니다. | Timeout cannot exceed 300 seconds | 保留 |
| proxy.settings.actions.save | 保存配置 | 설정 저장 | Save Configuration | 已修订 |
| proxy.settings.toast.saved | 路由配置已保存 | 라우팅 설정이 저장되었습니다. | Routing configuration saved | 已修订 |
| proxy.settings.toast.saveFailed | 保存失败: {{error}} | 저장 실패: {{error}} | Save failed: {{error}} | 保留 |
| proxy.settings.invalidPort | 端口无效，请输入 1024-65535 之间的数字 | 포트가 잘못되었습니다. 1024~65535 사이의 숫자를 입력하세요. | Invalid port, please enter a number between 1024-65535 | 保留 |
| proxy.settings.invalidAddress | 地址无效，请输入 IPv4（如 127.0.0.1）、IPv6（如 ::1）或 localhost | 주소가 잘못되었습니다. IPv4(예: 127.0.0.1), IPv6(예: ::1) 또는 localhost를 입력하세요. | Invalid address. Enter an IPv4 (e.g. 127.0.0.1), IPv6 (e.g. ::1), or localhost | 保留 |
| proxy.settings.configSaved | 路由配置已保存 | 라우팅 설정이 저장되었습니다. | Routing configuration saved | 已修订 |
| proxy.settings.configSaveFailed | 保存配置失败 | 설정을 저장하지 못했습니다. | Failed to save configuration | 已修订 |
| proxy.settings.restartRequired | 修改地址或端口后需要重启路由服务才能生效 | 주소 또는 포트 변경사항을 적용하려면 라우팅 서비스를 다시 시작하세요. | Restart routing service for address or port changes to take effect | 保留 |
| proxy.switchFailed | 切换失败: {{error}} | 전환 실패: {{error}} | Switch failed: {{error}} | 已修订 |
| proxy.takeover.ariaLabel | {{appLabel}} 本地路由 | {{appLabel}} 로컬 라우팅 | {{appLabel}} local routing | 保留 |
| proxy.takeover.hint | 选择要路由的应用，启用后该应用的请求将通过本地路由转发 | 라우팅할 앱 선택 - 활성화되면 해당 앱의 요청이 로컬 라우팅을 통해 전달됩니다. | Select apps to route — once enabled, requests from that app will go through local routing | 保留 |
| proxy.takeover.enabled | {{app}} 路由已启用 | {{app}} 라우팅 활성화됨 | {{app}} routing enabled | 保留 |
| proxy.takeover.disabled | {{app}} 路由已关闭 | {{app}} 라우팅이 비활성화되었습니다. | {{app}} routing disabled | 保留 |
| proxy.takeover.failed | 切换路由状态失败: {{detail}} | 라우팅 전환 실패: {{detail}} | Failed to toggle routing: {{detail}} | 保留 |
| proxy.takeover.tooltip.active | {{appLabel}} 路由中 - {{address}}:{{port}}<br>切换供应商只改路由，直连供应商不变 | {{appLabel}} 라우팅 중 - {{address}}:{{port}}<br>공급자를 전환해도 라우팅 대상만 바뀌며 직접 연결 공급자는 유지됩니다 | {{appLabel}} is routing - {{address}}:{{port}}<br>Switching providers changes the route only; the direct provider stays | 已修订 |
| proxy.takeover.tooltip.broken | {{appLabel}} 路由中，但路由服务未运行 | {{appLabel}}가 라우팅 중이지만 라우팅 서비스가 실행되고 있지 않습니다. | {{appLabel}} is routing, but routing service is not running | 保留 |
| proxy.takeover.tooltip.inactive | 路由 {{appLabel}} 的请求，让该应用请求走本地路由 | 로컬 라우팅을 통해 {{appLabel}}의 요청 라우팅 | Route {{appLabel}}'s requests through local routing | 保留 |
| proxy.stackMode.enabled | {{app}} 已进入聚合模式 | {{app}}이(가) 통합 모드로 전환되었습니다 | {{app}} is now in Aggregation mode | 已修订 |
| proxy.stackMode.exitedToDirect | {{apps}} 已退回直连 | {{apps}}을(를) 직접 연결로 되돌렸습니다 | {{apps}} switched back to direct | 已修订 |
| proxy.stackMode.ariaLabel | {{appLabel}} 聚合模式 | {{appLabel}} 통합 모드 | {{appLabel}} Aggregation mode | 已修订 |
| proxy.stackMode.failoverUnavailable | {{appLabel}} 在聚合模式下不做故障转移。队列和设置保留，回到路由模式后恢复 | {{appLabel}}은(는) 통합 모드이므로 장애 조치를 사용하지 않습니다. 대기열과 설정은 유지되며 라우팅 모드로 돌아가면 다시 적용됩니다 | {{appLabel}} is in Aggregation mode, which has no failover. The queue and settings are kept and apply again in routing mode | 已修订 |
| proxy.stackMode.codexStale.authTitle | Codex 可能仍缓存着切换前的账号；重启后台服务才能载入新登录 | Codex는 여전히 이전 계정을 캐시할 수 있습니다. 새 로그인을 로드하려면 백그라운드 서버를 다시 시작하세요. | Codex may still cache the previous account; restart its background server to load the new login | 保留 |
| proxy.stackMode.codexStale.title | Codex 还在用旧的模型列表，切换后的模型不会出现 | Codex는 여전히 이전 모델 목록을 사용하고 있으므로 현재 모델은 표시되지 않습니다. | Codex is still using an old model list, so the current models won't show | 保留 |
| proxy.stackMode.codexStale.unverifiedTitle | 切换前就开着的 Codex 可能还在用之前的账号或模型列表 | 전환 전에 열려 있던 Codex 앱은 이전 계정 또는 모델 목록을 계속 사용할 수 있습니다. | Codex apps that were open before the switch may still use the previous account or model list | 保留 |
| proxy.stackMode.codexStale.unverifiedHint | CC Switch 看不到桌面版和编辑器插件是否在运行；没开着的话直接关掉这条提示即可。 | CC Switch는 데스크톱 앱이나 편집기 확장이 실행 중인지 알 수 없습니다. 열려 있지 않으면 이 공지를 닫으시면 됩니다. | CC Switch can't tell whether the desktop app or editor extensions are running. If they aren't open, just close this notice. | 保留 |
| proxy.stackMode.codexStale.daemon | 命令行：重开 codex 不够，要重启后台的守护进程。 | CLI: codex를 다시 여는 것만으로는 부족합니다. 백그라운드 데몬을 다시 시작해야 합니다. | CLI: reopening codex isn't enough; its background daemon needs a restart. | 已修订 |
| proxy.stackMode.codexStale.others | 桌面版：要彻底退出再重开（macOS 上按 ⌘Q，只关窗口不行）；编辑器插件要重开编辑器窗口。 | 데스크톱 앱: 완전히 종료하고 다시 엽니다(macOS에서는 ⌘Q, 창을 닫는 것만으로는 충분하지 않음). 편집기 확장: 편집기 창을 다시 엽니다. | Desktop app: quit it completely and reopen it (⌘Q on macOS; closing the window isn't enough). Editor extensions: reopen the editor window. | 保留 |
| proxy.stackMode.codexStale.restart | 重启 Codex 守护进程 | Codex 데몬 다시 시작 | Restart Codex daemon | 保留 |
| proxy.stackMode.codexStale.confirmTitle | 重启 Codex 守护进程？ | Codex 데몬을 다시 시작하시겠습니까? | Restart the Codex daemon? | 保留 |
| proxy.stackMode.codexStale.confirmMessage | 所有终端里的 codex 共用这个守护进程，正在运行的任务会被中断。重启之后重新打开 codex，载入最新的账号和模型列表。 | 모든 터미널의 codex 세션이 이 데몬을 공유하므로 실행 중인 작업이 중단됩니다. 이후 codex를 다시 열어 현재 계정과 모델 목록을 불러오세요. | Every codex session in your terminals shares this daemon, so running tasks will be interrupted. Reopen codex afterwards to load the current account and model list. | 已修订 |
| proxy.stackMode.codexStale.confirm | 重启 | 다시 시작 | Restart | 保留 |
| proxy.stackMode.codexStale.restarted | Codex 守护进程已重启，重新打开 codex 以载入最新账号和模型列表 | Codex 데몬을 다시 시작했습니다. codex를 다시 열어 현재 계정과 모델 목록을 불러오세요 | Codex daemon restarted. Reopen codex to load the current account and model list | 已修订 |
| proxy.stackMode.codexStale.notRunning | Codex 守护进程没有在运行，下次启动时会载入当前登录和模型列表 | Codex 데몬이 실행되고 있지 않습니다. 다음에 시작할 때 현재 로그인 및 모델 목록을 로드합니다. | The Codex daemon isn't running. It will load the current login and model list the next time it starts | 保留 |
| proxy.stackMode.codexStale.failed | 重启 Codex 守护进程失败：{{error}} | Codex 데몬을 다시 시작하지 못했습니다: {{error}} | Failed to restart the Codex daemon: {{error}} | 保留 |
| proxy.failover.proxyRequired | 需要先启动路由服务才能配置故障转移 | 장애 조치를 설정하려면 라우팅 서비스를 시작해야 합니다. | Routing service must be started to configure failover | 已修订 |
| proxy.failover.autoSwitch | 自动故障转移 | 자동 장애 조치 | Auto Failover | 保留 |
| proxy.failover.autoSwitchDescription | 开启后将立即切换到队列 P1，并在请求失败时自动切换到队列中的下一个供应商 | 활성화되면 즉시 대기열 P1로 전환하고 실패 시 자동으로 대기열의 다음 공급자를 시도합니다. | When enabled, switches to queue P1 immediately and automatically tries the next provider in the queue on failures | 已修订 |
| proxy.failoverQueue.title | 故障转移队列 | 장애 조치 대기열 | Failover Queue | 保留 |
| proxy.failoverQueue.description | 管理各应用的供应商故障转移顺序 | 각 앱 공급자의 장애 조치 순서 관리 | Manage failover order for each app's providers | 已修订 |
| proxy.failoverQueue.info | 启用自动故障转移后，将按队列优先级选择供应商（P1 优先）。当请求失败时，系统会按队列顺序依次尝试下一个供应商。 | 자동 장애 조치(failover)가 활성화되면 요청은 큐 우선 순위(P1 우선)를 따릅니다. 오류가 발생하면 시스템은 대기열의 다음 공급자를 시도합니다. | When auto failover is enabled, requests follow the queue priority order (P1 first). On failures, the system will try the next provider in the queue. | 已修订 |
| proxy.failoverQueue.selectProvider | 选择供应商添加到队列 | 대기열에 추가할 공급자를 선택하세요. | Select a provider to add to queue | 已修订 |
| proxy.failoverQueue.noAvailableProviders | 没有可添加的供应商 | 추가할 수 있는 공급자가 없습니다. | No providers available to add | 已修订 |
| proxy.failoverQueue.empty | 故障转移队列为空。添加供应商以启用自动故障转移。 | 장애 조치 대기열이 비어 있습니다. 자동 장애 조치를 활성화하려면 공급자를 추가하세요. | Failover queue is empty. Add providers to enable automatic failover. | 已修订 |
| proxy.failoverQueue.orderHint | 队列顺序与首页供应商列表顺序一致，可在首页拖拽调整顺序。 | 대기열 순서는 홈 페이지의 공급자 목록 순서와 일치합니다. 우선순위를 변경하려면 홈 페이지에서 공급자 순서를 변경하세요. | Queue order matches the provider list order on the Home page. Reorder providers on the Home page to change priority. | 已修订 |
| proxy.failoverQueue.dragHint | 拖拽供应商可调整故障转移顺序，序号越小优先级越高。 | 장애 조치 순서를 조정하려면 공급자를 드래그하세요. 숫자가 낮을수록 우선순위가 높습니다. | Drag providers to adjust failover order. Lower numbers have higher priority. | 已修订 |
| proxy.failoverQueue.toggleEnabled | 启用/禁用 | 활성화/비활성화 | Enable/Disable | 保留 |
| proxy.failoverQueue.addSuccess | 已添加到故障转移队列 | 장애 조치 대기열에 추가됨 | Added to failover queue | 保留 |
| proxy.failoverQueue.addFailed | 添加失败 | 추가하지 못했습니다. | Failed to add | 保留 |
| proxy.failoverQueue.removeSuccess | 已从故障转移队列移除 | 장애 조치 대기열에서 제거됨 | Removed from failover queue | 保留 |
| proxy.failoverQueue.removeFailed | 移除失败 | 제거하지 못했습니다. | Failed to remove | 保留 |
| proxy.failoverQueue.reorderSuccess | 队列顺序已更新 | 대기열 순서가 업데이트되었습니다. | Queue order updated | 保留 |
| proxy.failoverQueue.reorderFailed | 更新顺序失败 | 순서 변경 실패 | Failed to update order | 已修订 |
| proxy.failoverQueue.toggleFailed | 状态更新失败 | 상태를 업데이트하지 못했습니다. | Failed to update status | 保留 |
| proxy.autoFailover.info | 当故障转移队列中配置了多个供应商时，系统会在请求失败时按优先级顺序依次尝试。当某个供应商连续失败达到阈值时，熔断器会打开并在一段时间内跳过该供应商。 | 장애 조치 대기열에 공급자가 여러 개 있으면 요청 실패 시 우선순위에 따라 순서대로 시도합니다. 연속 실패 횟수가 임계값에 도달하면 서킷 브레이커가 열리고 해당 공급자를 일시적으로 건너뜁니다. | When the failover queue has multiple providers, the system will try them in priority order when requests fail. When a provider reaches the consecutive failure threshold, the circuit breaker will open and skip it temporarily. | 已修订 |
| proxy.autoFailover.configSaved | 自动故障转移配置已保存 | 자동 장애 조치 설정이 저장되었습니다. | Auto failover config saved | 已修订 |
| proxy.autoFailover.configSaveFailed | 保存失败 | 저장하지 못했습니다. | Failed to save | 保留 |
| proxy.autoFailover.validationFailed | 以下字段超出有效范围: {{fields}} | 다음 필드는 유효한 범위를 벗어났습니다: {{fields}} | The following fields are out of valid range: {{fields}} | 保留 |
| proxy.autoFailover.retrySettings | 重试与超时设置 | 재시도 및 시간 초과 설정 | Retry & Timeout Settings | 保留 |
| proxy.autoFailover.failureThreshold | 失败阈值 | 실패 임계값 | Failure Threshold | 保留 |
| proxy.autoFailover.failureThresholdHint | 连续失败多少次后打开熔断器（建议: 3-10） | 연속 실패 횟수가 이 값에 도달하면 서킷 브레이커를 엽니다 (권장: 3~10) | Open circuit breaker after this many consecutive failures (recommended: 3-10) | 已修订 |
| proxy.autoFailover.timeout | 恢复等待时间（秒） | 복구 대기 시간(초) | Recovery Wait Time (seconds) | 保留 |
| proxy.autoFailover.timeoutHint | 熔断器打开后，等待多久后尝试恢复（建议: 30-120） | 서킷 브레이커가 열린 후 복구를 시도하기까지 기다릴 시간입니다 (권장: 30~120초) | Wait this long before trying to recover after circuit opens (recommended: 30-120) | 已修订 |
| proxy.autoFailover.circuitBreakerSettings | 熔断器设置 | 서킷 브레이커 설정 | Circuit Breaker Settings | 已修订 |
| proxy.autoFailover.successThreshold | 恢复成功阈值 | 복구 성공 임계값 | Recovery Success Threshold | 保留 |
| proxy.autoFailover.successThresholdHint | 半开状态下成功多少次后关闭熔断器 | 반열림 상태에서 성공 횟수가 이 값에 도달하면 서킷 브레이커를 닫습니다 | Close circuit breaker after this many successes in half-open state | 已修订 |
| proxy.autoFailover.errorRate | 错误率阈值 (%) | 오류율 임계값(%) | Error Rate Threshold (%) | 保留 |
| proxy.autoFailover.errorRateHint | 错误率超过此值时打开熔断器 | 오류율이 이 값을 초과하면 서킷 브레이커를 엽니다 | Open circuit breaker when error rate exceeds this value | 已修订 |
| proxy.autoFailover.minRequests | 最小请求数 | 최소 요청 | Minimum Requests | 保留 |
| proxy.autoFailover.minRequestsHint | 计算错误率前的最小请求数 | 오류율 계산 전 최소 요청 | Minimum requests before calculating error rate | 保留 |
| proxy.autoFailover.explanationTitle | 工作原理 | 작동 방식 | How It Works | 保留 |
| proxy.autoFailover.failureThresholdLabel | 失败阈值 | 실패 임계값 | Failure Threshold | 保留 |
| proxy.autoFailover.failureThresholdExplain | 连续失败达到此次数时，熔断器打开，该供应商暂时不可用 | 연속 실패 횟수가 이 값에 도달하면 서킷 브레이커가 열리고 해당 공급자를 일시적으로 사용할 수 없게 됩니다 | Circuit breaker opens after this many consecutive failures, making the provider temporarily unavailable | 已修订 |
| proxy.autoFailover.timeoutLabel | 恢复等待时间 | 복구 대기 시간 | Recovery Wait Time | 保留 |
| proxy.autoFailover.timeoutExplain | 熔断器打开后，等待此时间后尝试半开状态 | 서킷 브레이커가 열린 후 설정한 시간만큼 기다렸다가 반열림 상태로 전환을 시도합니다 | After circuit opens, wait this long before trying half-open state | 已修订 |
| proxy.autoFailover.successThresholdLabel | 恢复成功阈值 | 복구 성공 임계값 | Recovery Success Threshold | 保留 |
| proxy.autoFailover.successThresholdExplain | 半开状态下，成功达到此次数时关闭熔断器，供应商恢复可用 | 반열림 상태에서 성공 횟수가 이 값에 도달하면 서킷 브레이커를 닫고 해당 공급자를 다시 사용할 수 있게 합니다 | In half-open state, close circuit breaker after this many successes, making provider available again | 已修订 |
| proxy.autoFailover.errorRateLabel | 错误率阈值 | 오류율 임계값 | Error Rate Threshold | 保留 |
| proxy.autoFailover.errorRateExplain | 错误率超过此值时，即使未达到失败阈值也会打开熔断器 | 연속 실패 임계값에 도달하지 않았더라도 오류율이 이 값을 초과하면 서킷 브레이커를 엽니다 | Open circuit breaker when error rate exceeds this value, even if failure threshold not reached | 已修订 |
| proxy.autoFailover.maxRetries | 最大重试次数 | 최대 재시도 횟수 | Max Retries | 保留 |
| proxy.autoFailover.timeoutSettings | 超时配置 | 시간 초과 설정 | Timeout Settings | 保留 |
| proxy.autoFailover.streamingFirstByte | 流式首字节超时 | 스트리밍 첫 번째 바이트 시간 초과 | Streaming First Byte Timeout | 保留 |
| proxy.autoFailover.streamingIdle | 流式静默超时 | 스트리밍 유휴 시간 초과 | Streaming Idle Timeout | 保留 |
| proxy.autoFailover.nonStreaming | 非流式超时 | 비스트리밍 시간 초과 | Non-Streaming Timeout | 保留 |
| proxy.autoFailover.maxRetriesHint | 请求失败时的重试次数（0-10） | 요청 실패 시 재시도 횟수(0-10) | Number of retries on request failure (0-10) | 保留 |
| proxy.autoFailover.streamingFirstByteHint | 等待首个数据块的最大时间，范围 1-120 秒，默认 60 秒 | 첫 번째 데이터 청크를 기다리는 최대 시간, 범위 1-120초, 기본값 60초 | Max time to wait for first data chunk, range 1-120s, default 60s | 保留 |
| proxy.autoFailover.streamingIdleHint | 数据块之间的最大间隔，范围 60-600 秒，填 0 禁用（防止中途卡住） | 데이터 청크 사이의 최대 간격입니다. 범위는 60~600초이며 0이면 사용하지 않습니다 (스트리밍 중 멈춤 방지) | Max interval between data chunks, range 60-600s, 0 to disable (prevents mid-stream stalls) | 已修订 |
| proxy.autoFailover.nonStreamingHint | 非流式请求的总超时时间，范围 60-1200 秒，默认 600 秒（10 分钟） | 비스트리밍 요청에 대한 총 제한 시간, 범위 60~1,200초, 기본값 600초(10분) | Total timeout for non-streaming requests, range 60-1200s, default 600s (10 min) | 保留 |
| proxy.logging.enabled | 日志记录已启用 | 로깅 활성화됨 | Logging enabled | 保留 |
| proxy.logging.disabled | 日志记录已关闭 | 로깅이 비활성화되었습니다. | Logging disabled | 保留 |
| proxy.logging.failed | 切换日志状态失败 | 로깅을 전환하지 못했습니다. | Failed to toggle logging | 保留 |
| proxy.server.started | 路由服务已启动 - {{address}}:{{port}} | 라우팅 서비스 시작 - {{address}}:{{port}} | Routing service started - {{address}}:{{port}} | 保留 |
| proxy.server.startFailed | 启动路由服务失败: {{detail}} | 라우팅 서비스를 시작하지 못했습니다: {{detail}} | Failed to start routing service: {{detail}} | 保留 |
| proxy.server.stopped | 路由服务已停止 | 라우팅 서비스가 중지되었습니다. | Routing service stopped | 保留 |
| proxy.server.stopFailed | 停止路由服务失败：{{detail}} | 라우팅 서비스 중지 실패: {{detail}} | Failed to stop routing service: {{detail}} | 保留 |
| proxy.stoppedWithRestore | 路由服务已关闭，所有应用已退回直连 | 라우팅 서비스가 중지되었습니다. 모든 앱이 다시 직접 연결로 돌아왔습니다 | Routing service stopped; all apps are back on direct connections | 保留 |
| proxy.stopWithRestoreFailed | 停止失败: {{detail}} | 중지 실패: {{detail}} | Stop failed: {{detail}} | 保留 |
| streamCheck.reachable | {{providerName}} 连通正常 ({{responseTimeMs}}ms) | {{providerName}}에 연결할 수 있습니다({{responseTimeMs}}ms). | {{providerName}} is reachable ({{responseTimeMs}}ms) | 保留 |
| streamCheck.reachableSlow | {{providerName}} 连通但较慢 ({{responseTimeMs}}ms) | {{providerName}}에 연결할 수 있지만 느림({{responseTimeMs}}ms) | {{providerName}} reachable but slow ({{responseTimeMs}}ms) | 保留 |
| streamCheck.unreachable | {{providerName}} 无法连通: {{message}} | {{providerName}}에 연결할 수 없음: {{message}} | {{providerName}} unreachable: {{message}} | 保留 |
| streamCheck.unreachableHint | 无法建立连接（DNS / 连接 / TLS / 超时）。请检查 base_url 与网络。 | 연결을 설정할 수 없습니다(DNS/연결/TLS/시간 초과). base_url과 네트워크를 확인하세요. | Could not establish a connection (DNS / connect / TLS / timeout). Check the base_url and your network. | 保留 |
| streamCheck.error | {{providerName}} 检查出错: {{error}} | {{providerName}} 확인 오류: {{error}} | {{providerName}} check error: {{error}} | 保留 |
| proxyConfig.proxyEnabled | 路由总开关 | 라우팅 마스터 스위치 | Routing Master Switch | 保留 |
| proxyConfig.appTakeover | 路由启用 | 라우팅 활성화됨 | Routing Enabled | 保留 |
| proxyConfig.perAppConfig | 应用配置 | 앱별 설정 | Per-App Config | 已修订 |
| proxyConfig.circuitBreaker | 熔断器配置 | 서킷 브레이커 | Circuit Breaker | 已修订 |
| proxyConfig.circuitBreakerSettings | 熔断器设置 | 서킷 브레이커 설정 | Circuit Breaker Settings | 已修订 |
| proxyConfig.failureThreshold | 失败阈值 | 실패 임계값 | Failure Threshold | 保留 |
| proxyConfig.successThreshold | 恢复阈值 | 복구 성공 임계값 | Success Threshold | 已修订 |
| proxyConfig.recoveryTimeout | 恢复等待时间 | 복구 대기 시간 | Recovery Timeout | 已修订 |
| proxyConfig.errorRateThreshold | 错误率阈值 | 오류율 임계값 | Error Rate Threshold | 保留 |
| proxyConfig.minRequests | 最小请求数 | 최소 요청 | Min Requests | 保留 |
| proxyConfig.timeoutConfig | 超时配置 | 시간 초과 설정 | Timeout Config | 已修订 |
| proxyConfig.streamingFirstByte | 流式首字节超时 | 스트리밍 첫 번째 바이트 시간 초과 | Streaming First Byte Timeout | 保留 |
| proxyConfig.streamingIdle | 流式静默超时 | 스트리밍 유휴 시간 초과 | Streaming Idle Timeout | 保留 |
| proxyConfig.nonStreaming | 非流式超时 | 비스트리밍 시간 초과 | Non-Streaming Timeout | 保留 |
| universalProvider.duplicate | 复制 | 복제 | Duplicate | 已修订 |
| universalProvider.duplicatedAndSynced | 统一供应商已复制并同步 | 범용 공급자가 복제되고 동기화되었습니다. | Universal provider duplicated and synced | 已修订 |
| universalProvider.duplicateError | 复制统一供应商失败 | 범용 공급자를 복제하지 못했습니다. | Failed to duplicate universal provider | 已修订 |
| universalProvider.title | 统一供应商 | 범용 공급자 | Universal Provider | 已修订 |
| universalProvider.description | 统一供应商可以同时管理 Claude、Codex 和 Gemini 的配置。修改后会自动同步到所有启用的应用。 | 범용 공급자는 Claude, Codex 및 Gemini 설정을 동시에 관리합니다. 변경 사항은 활성화된 모든 앱에 자동으로 동기화됩니다. | Universal providers manage Claude, Codex, and Gemini configurations simultaneously. Changes are automatically synced to all enabled apps. | 已修订 |
| universalProvider.add | 添加统一供应商 | 범용 공급자 추가 | Add Universal Provider | 已修订 |
| universalProvider.edit | 编辑统一供应商 | 범용 공급자 편집 | Edit Universal Provider | 已修订 |
| universalProvider.empty | 还没有统一供应商 | 아직 범용 공급자가 없습니다. | No universal providers yet | 已修订 |
| universalProvider.emptyHint | 点击下方「添加统一供应商」按钮创建一个 | 범용 공급자를 생성하려면 아래의 "범용 공급자 추가" 버튼을 클릭하세요. | Click the "Add Universal Provider" button below to create one | 已修订 |
| universalProvider.selectPreset | 选择预设类型 | 프리셋 유형 선택 | Select Preset Type | 保留 |
| universalProvider.name | 名称 | 이름 | Name | 保留 |
| universalProvider.namePlaceholder | 例如：我的 NewAPI | 예: 내 NewAPI | e.g., My NewAPI | 保留 |
| universalProvider.baseUrl | API 地址 | API URL | API URL | 保留 |
| universalProvider.apiKey | API Key | API 키 | API Key | 保留 |
| universalProvider.websiteUrl | 官网地址 | 웹사이트 URL | Website URL | 保留 |
| universalProvider.websiteUrlPlaceholder | https://example.com（可选，用于在列表中显示） | https://example.com(선택 사항, 목록에 표시됨) | https://example.com (optional, displayed in the list) | 保留 |
| universalProvider.notes | 备注 | 메모 | Notes | 保留 |
| universalProvider.notesPlaceholder | 可选：添加备注信息 | 선택사항: 메모 추가 | Optional: Add notes | 保留 |
| universalProvider.enabledApps | 启用的应用 | 활성화된 앱 | Enabled Apps | 保留 |
| universalProvider.modelConfig | 模型配置 | 모델 설정 | Model Configuration | 已修订 |
| universalProvider.model | 模型 | 모델 | Model | 保留 |
| universalProvider.sync | 同步到应用 | 앱과 동기화 | Sync to Apps | 保留 |
| universalProvider.synced | 已同步到所有应用 | 모든 앱에 동기화됨 | Synced to all apps | 保留 |
| universalProvider.syncError | 同步失败 | 동기화 실패 | Sync failed | 保留 |
| universalProvider.noAppsEnabled | 未启用任何应用 | 활성화된 앱이 없습니다. | No apps enabled | 保留 |
| universalProvider.added | 统一供应商已添加 | 범용 공급자가 추가됨 | Universal provider added | 已修订 |
| universalProvider.addedAndSynced | 统一供应商已添加并同步 | 범용 공급자가 추가되고 동기화되었습니다. | Universal provider added and synced | 已修订 |
| universalProvider.addedButSyncFailed | 统一供应商已添加，但同步失败 | 범용 공급자가 추가되었지만 동기화에 실패했습니다. | Universal provider added, but sync failed | 已修订 |
| universalProvider.updated | 统一供应商已更新 | 범용 공급자가 업데이트되었습니다. | Universal provider updated | 已修订 |
| universalProvider.deleted | 统一供应商已删除 | 범용 공급자가 삭제되었습니다. | Universal provider deleted | 已修订 |
| universalProvider.addFailed | 统一供应商添加失败 | 범용 공급자를 추가하지 못했습니다. | Failed to add universal provider | 已修订 |
| universalProvider.hint | 跨应用统一配置，自动同步到 Claude/Codex/Gemini | 앱 간 통합 설정, Claude/Codex/Gemini에 자동 동기화 | Cross-app unified config, auto-sync to Claude/Codex/Gemini | 已修订 |
| universalProvider.manage | 管理 | 관리 | Manage | 已修订 |
| universalProvider.loadError | 加载统一供应商失败 | 범용 공급자를 로드하지 못했습니다. | Failed to load universal providers | 已修订 |
| universalProvider.saveError | 保存统一供应商失败 | 범용 공급자를 저장하지 못했습니다. | Failed to save universal provider | 已修订 |
| universalProvider.deleteError | 删除统一供应商失败 | 범용 공급자를 삭제하지 못했습니다. | Failed to delete universal provider | 已修订 |
| universalProvider.deleteConfirmTitle | 删除统一供应商 | 범용 공급자 삭제 | Delete Universal Provider | 已修订 |
| universalProvider.deleteConfirmDescription | 确定要删除 "{{name}}" 吗？这将同时删除它在各应用中生成的供应商配置。 | 정말로 "{{name}}"을(를) 삭제하시겠습니까? 이렇게 하면 각 앱에서 생성된 공급자 설정도 삭제됩니다. | Are you sure you want to delete "{{name}}"? This will also delete its generated provider configurations in each app. | 已修订 |
| universalProvider.syncConfirmTitle | 同步统一供应商 | 범용 공급자 동기화 | Sync Universal Provider | 已修订 |
| universalProvider.syncConfirmDescription | 同步 "{{name}}" 将会覆盖 Claude、Codex 和 Gemini 中关联的供应商配置。确定要继续吗？ | "{{name}}"을(를) 동기화하면 Claude, Codex 및 Gemini의 관련 공급자 설정을 덮어씁니다. 계속하시겠습니까? | Syncing "{{name}}" will overwrite the associated provider configurations in Claude, Codex, and Gemini. Do you want to continue? | 已修订 |
| universalProvider.syncConfirm | 同步 | 동기화 | Sync | 已修订 |
| universalProvider.saveAndSync | 保存并同步 | 저장 및 동기화 | Save & Sync | 保留 |
| universalProvider.savedAndSynced | 已保存并同步到所有应用 | 모든 앱에 저장 및 동기화됨 | Saved and synced to all apps | 保留 |
| universalProvider.saveAndSyncError | 保存并同步失败 | 저장 및 동기화하지 못했습니다. | Failed to save and sync | 保留 |
| universalProvider.configJsonPreview | 配置 JSON 预览 | JSON 설정 미리보기 | Config JSON Preview | 已修订 |
| universalProvider.configJsonPreviewHint | 以下是将要同步到各应用的配置内容（仅覆盖显示的字段，保留其他自定义配置） | 다음 설정이 각 앱에 동기화됩니다(표시된 필드만 덮어쓰고 다른 사용자 정의 설정은 유지됩니다). | The following configurations will be synced to each app (only the displayed fields will be overwritten, other custom settings will be preserved) | 已修订 |
| omo.editProfile | 编辑 OMO 配置 | OMO 설정 편집 | Edit OMO Config | 已修订 |
| omo.newProfile | 新建 OMO 配置 | 새로운 OMO 설정 | New OMO Config | 已修订 |
| omo.profileName | 名称 | 이름 | Name | 保留 |
| omo.mainAgents | 主 Agent | 주 에이전트 | Main Agents | 已修订 |
| omo.subAgents | 子 Agent | 서브에이전트 | Sub Agents | 已修订 |
| omo.categories | 分类 | 카테고리 | Categories | 保留 |
| omo.customAgents | 自定义 Agent | 맞춤형 에이전트 | Custom Agents | 保留 |
| omo.noCustomAgents | 暂无自定义 Agent | 맞춤 에이전트 없음 | No custom agents | 保留 |
| omo.otherFields | 其他配置 | 기타 설정 | Other Config | 已修订 |
| omo.globalConfig | OMO 全局配置 | OMO 전역 설정 | OMO Global Config | 已修订 |
| omo.globalConfigShort | OMO 配置 | OMO 설정 | OMO Config | 已修订 |
| omo.globalConfigSaved | 全局配置已保存 | 전역 설정이 저장되었습니다. | Global config saved | 已修订 |
| omo.addProfile | 添加 OMO 配置 | OMO 설정 추가 | Add OMO Provider | 已修订 |
| omo.disabledItems | 禁用项设置 | 비활성화된 항목 | Disabled Items | 保留 |
| omo.advanced | 高级设置 | 고급 설정 | Advanced Settings | 保留 |
| omo.profileCreated | OMO 配置已创建 | OMO 설정이 생성되었습니다. | OMO config created | 已修订 |
| omo.profileUpdated | OMO 配置已更新 | OMO 설정이 업데이트되었습니다. | OMO config updated | 已修订 |
| omo.invalidJson | 其他字段包含无效 JSON | 기타 필드에 잘못된 JSON가 포함되어 있습니다. | Other Fields contains invalid JSON | 保留 |
| omo.confirmDelete | 删除配置 | 설정 삭제 | Delete Config | 已修订 |
| omo.confirmDeleteMsg | 确定删除 "{{name}}" 吗？ | '{{name}}'을(를) 삭제하시겠습니까? | Delete "{{name}}"? | 已修订 |
| omo.profileDeleted | 配置已删除 | 설정이 삭제되었습니다. | Config deleted | 已修订 |
| omo.imported | 已导入为 "{{name}}" | "{{name}}"로 가져옴 | Imported as "{{name}}" | 保留 |
| omo.import | 导入 | 가져오기 | Import | 保留 |
| omo.global | 全局 | 전역 | Global | 已修订 |
| omo.empty | 暂无配置。点击 + 添加或从本地导入。 | 아직 OMO 설정이 없습니다. + 추가 또는 로컬에서 가져오기를 클릭합니다. | No OMO configs yet. Click + Add or Import from local. | 已修订 |
| omo.applied | 已应用 | 적용됨 | Applied | 已修订 |
| omo.apply | 应用 | 적용 | Apply | 保留 |
| omo.enable | 启用 | 활성화 | Enable | 保留 |
| omo.enabled | 启用中 | 활성화됨 | Enabled | 保留 |
| omo.disabled | OMO 已停用 | OMO 비활성화됨 | OMO disabled | 保留 |
| omo.disableFailed | 停用 OMO 失败: {{error}} | OMO 비활성화 실패: {{error}} | Failed to disable OMO: {{error}} | 保留 |
| omo.selectPlaceholder | 请选择... | 선택... | Select... | 已修订 |
| omo.clear | 清空 | 지우기 | Clear | 保留 |
| omo.clearWrapped | （清空） | (지우기) | (Clear) | 已修订 |
| omo.defaultWrapped | （默认） | (기본) | (Default) | 保留 |
| omo.variantPlaceholder | 思考等级 | 추론 수준 | variant | 已修订 |
| omo.selectEnabledModel | 选择已配置模型 | 설정된 모델 선택 | Select configured model | 已修订 |
| omo.selectModel | 选择已配置模型 | 설정된 모델 선택 | Select configured model | 已修订 |
| omo.recommendedHint | 推荐: {{model}} | 권장: {{model}} | Recommended: {{model}} | 保留 |
| omo.searchModel | 搜索模型... | 모델 검색... | Search model... | 保留 |
| omo.selectModelFirst | 先选择模型 | 모델을 먼저 선택하세요 | Select model first | 保留 |
| omo.noEnabledModels | 暂无已配置模型 | 설정된 모델 없음 | No configured models | 已修订 |
| omo.noVariantsForModel | 该模型无思考等级 | 이 모델에는 추론 수준이 없습니다 | No variants for model | 已修订 |
| omo.currentValueNotEnabled | {{value}}（当前值，未配置） | {{value}}(현재 값, 설정되지 않음) | {{value}} (current value, not configured) | 已修订 |
| omo.currentValueUnavailable | {{value}}（当前值，不可用） | {{value}}(현재 값, 사용 불가) | {{value}} (current value, unavailable) | 保留 |
| omo.advancedLabel | 高级参数 | 고급 매개변수 | Advanced | 已修订 |
| omo.advancedJsonInvalid | 高级参数 JSON 无效 | 고급 매개변수 JSON이 유효하지 않습니다. | Advanced JSON is invalid | 已修订 |
| omo.advancedJsonHint | temperature, top_p, budgetTokens, prompt_append, permission 等，留空使用默认值 | temperature, top_p, budgetTokens, prompt_append, permission 등. 기본값을 사용하려면 비워 두세요 | temperature, top_p, budgetTokens, prompt_append, permission, etc. Leave empty for defaults | 保留 |
| omo.noEnabledModelsWarning | 当前没有可用的已配置模型，请先配置 OpenCode 模型 | 설정된 모델이 없습니다. 먼저 OpenCode 모델을 설정하세요. | No configured models available. Configure OpenCode models first. | 已修订 |
| omo.modelSourcePartialWarning | 部分供应商模型配置无效，已自动跳过。 | 일부 공급자 모델 설정이 잘못되어 건너뛰었습니다. | Some provider model configs are invalid and were skipped. | 已修订 |
| omo.modelSourceFallbackWarning | 读取 live 供应商状态失败，已回退到已配置供应商列表。 | 실시간 공급자 상태를 로드하지 못했습니다. 설정된 공급자로 대체됩니다. | Failed to load live provider state. Falling back to configured providers. | 已修订 |
| omo.runtimeModelsFailedWarning | 读取 OpenCode 运行时模型失败，已仅展示已配置供应商模型。 | OpenCode 런타임 모델을 읽지 못해 설정된 공급자의 모델만 표시합니다. | Failed to load OpenCode runtime models. Showing configured providers only. | 已修订 |
| omo.importLocalReplaceSuccess | 已从本地文件导入并覆盖 Agent/Category/Other Fields | 로컬 파일을 가져오고 에이전트/범주/기타 필드를 대체했습니다. | Imported local file and replaced Agents/Categories/Other Fields | 保留 |
| omo.importLocalFailed | 读取本地文件失败: {{error}} | 로컬 파일을 읽지 못했습니다: {{error}} | Failed to read local file: {{error}} | 保留 |
| omo.agentKeyPlaceholder | agent 键名 | 에이전트 키 | agent key | 保留 |
| omo.categoryKeyPlaceholder | 分类键名 | 카테고리 키 | category key | 保留 |
| omo.modelNamePlaceholder | 模型名 | 모델명 | model-name | 保留 |
| omo.custom | 自定义 | 사용자 지정 | Custom | 保留 |
| omo.customCategories | 自定义分类 | 맞춤 카테고리 | Custom Categories | 保留 |
| omo.modelConfiguration | 模型配置 | 모델 설정 | Model Configuration | 已修订 |
| omo.fillRecommended | 填充推荐 | 권장 모델 채우기 | Fill Recommended | 已修订 |
| omo.fillRecommendedSuccess | 已填充 {{count}} 个推荐模型 | 권장 모델 {{count}}개를 채웠습니다 | Filled {{count}} recommended models | 已修订 |
| omo.fillRecommendedPartial | 已填充 {{filled}} 个推荐模型，{{unmatched}} 个未匹配 | 권장 모델 {{filled}}개를 채웠으며 {{unmatched}}개는 일치하지 않습니다 | Filled {{filled}} recommended models, {{unmatched}} unmatched | 已修订 |
| omo.fillRecommendedMostlyUnmatched | 仅填充了 {{filled}} 个，{{unmatched}} 个未匹配（如 {{examples}}）。请配置提供这些模型的供应商，或手动选择替代项。 | {{filled}}개만 채웠으며 {{unmatched}}개는 일치하지 않습니다 (예: {{examples}}). 해당 모델을 제공하는 공급자를 설정하거나 대체 모델을 직접 선택하세요. | Filled only {{filled}}, {{unmatched}} unmatched (e.g. {{examples}}). Configure providers offering these models or pick a substitute. | 已修订 |
| omo.fillRecommendedAllSet | 所有槽位已有模型配置 | 모든 슬롯에 이미 모델이 설정되어 있습니다. | All slots already have models configured | 已修订 |
| omo.fillRecommendedNoMatch | 推荐模型在已配置的供应商中未找到匹配（如 {{examples}}） | 설정된 공급자에서 권장 모델과 일치하는 모델을 찾지 못했습니다(예: {{examples}}). | Recommended models not found in configured providers (e.g. {{examples}}) | 已修订 |
| omo.configSummary | 已配置 {{agents}} 个 Agent，{{categories}} 个 Category · 点击 ⚙ 展开高级参数 | {{agents}} 에이전트, {{categories}} 카테고리 설정됨 · 고급 매개변수를 보려면 ⚙를 클릭하세요. | {{agents}} agents, {{categories}} categories configured · Click ⚙ for advanced params | 已修订 |
| omo.enabledModelsCount | 可选已配置模型 {{count}} 个 | {{count}} 설정 모델 사용 가능 | {{count}} configured models available | 已修订 |
| omo.source | 来源: | 출처: | from: | 已修订 |
| omo.otherFieldsJson | 其他字段 (JSON) | 기타 필드(JSON) | Other Fields (JSON) | 保留 |
| omo.slimOtherFieldsHint | OMO Slim 的 council、fallback、multiplexer、disabled_mcps、todoContinuation 等顶层配置请写在这里。 | council, fallback, multiplexer, disabled_mcps, todoContinuation 등 최상위 OMO Slim 설정을 입력하세요. | Use this area for top-level OMO Slim config such as council, fallback, multiplexer, disabled_mcps, and todoContinuation. | 保留 |
| omo.searchOrType | 搜索或输入自定义值... | 맞춤 값을 검색하거나 입력하세요... | Search or type custom value... | 保留 |
| omo.noMatches | 无匹配项 | 일치하는 항목 없음 | No matches | 保留 |
| omo.jsonMustBeObject | {{field}} 必须是 JSON 对象 | {{field}}는 JSON 객체여야 합니다. | {{field}} must be a JSON object | 保留 |
| omo.jsonInvalid | {{field}} 包含无效 JSON | {{field}}에 잘못된 JSON가 포함되어 있습니다. | {{field}} contains invalid JSON | 保留 |
| omo.importGlobalSuccess | 已从本地文件导入全局配置（未保存） | 로컬 파일에서 가져온 전역 설정(저장되지 않음) | Imported global config from local file (unsaved) | 已修订 |
| omo.importGlobalFailed | 读取本地文件失败: {{error}} | 로컬 파일을 읽지 못했습니다: {{error}} | Failed to read local file: {{error}} | 保留 |
| omo.importLocal | 从本地导入 | 로컬 가져오기 | Import Local | 保留 |
| omo.saveGlobalConfig | 保存全局配置 | 전역 설정 저장 | Save Global Config | 已修订 |
| omo.schemaUrl | $schema | $schema | $schema | 已修订 |
| omo.resetDefault | 重置默认 | 기본값으로 재설정 | Reset | 已修订 |
| omo.sisyphusAgentConfig | Sisyphus Agent 设置 | Sisyphus 에이전트 설정 | Sisyphus Agent Config | 已修订 |
| omo.disabledAgents | Agents | 에이전트 | Agents | 已修订 |
| omo.disabledAgentsPlaceholder | 禁用的 Agents | 비활성화된 에이전트 | Disabled Agents | 保留 |
| omo.disabledMcps | MCPs | MCP | MCPs | 保留 |
| omo.disabledMcpsPlaceholder | 禁用的 MCPs | 비활성화된 MCP | Disabled MCPs | 保留 |
| omo.disabledHooks | Hooks | 후크 | Hooks | 保留 |
| omo.disabledHooksPlaceholder | 禁用的 Hooks | 비활성화된 후크 | Disabled Hooks | 保留 |
| omo.disabledSkills | Skills | Skills | Skills | 保留 |
| omo.disabledSkillsPlaceholder | 禁用的 Skills | 비활성화된 Skills | Disabled Skills | 保留 |
| omo.advancedLsp | LSP 配置 | LSP 설정 | LSP Config | 已修订 |
| omo.advancedExperimental | 实验性功能 | 실험적 기능 | Experimental Features | 保留 |
| omo.advancedBackgroundTask | 后台任务 | 백그라운드 작업 | Background Tasks | 保留 |
| omo.advancedBrowserAutomation | 浏览器自动化 | 브라우저 자동화 | Browser Automation | 保留 |
| omo.advancedClaudeCode | Claude Code | Claude Code | Claude Code | 保留 |
| omo.agentDesc.sisyphus | 主编排者 | 메인 오케스트레이터 | Main orchestrator | 保留 |
| omo.agentDesc.hephaestus | 自主深度工作者 | 자율적인 심층 작업자 | Autonomous deep worker | 保留 |
| omo.agentDesc.prometheus | 战略规划者 | 전략 기획자 | Strategic planner | 保留 |
| omo.agentDesc.atlas | 任务管理者 | 작업 관리자 | Task manager | 保留 |
| omo.agentDesc.oracle | 战略顾问 | 전략 고문 | Strategic advisor | 保留 |
| omo.agentDesc.librarian | 多仓库研究员 | 다중 저장소 연구원 | Multi-repo researcher | 保留 |
| omo.agentDesc.explore | 快速代码搜索 | 빠른 코드 검색 | Fast code search | 保留 |
| omo.agentDesc.multimodalLooker | 媒体分析器 | 미디어 분석기 | Media analyzer | 保留 |
| omo.agentDesc.metis | 规划前分析顾问 | 사전 계획 분석 고문 | Pre-plan analysis advisor | 保留 |
| omo.agentDesc.momus | 计划审查者 | 계획 검토자 | Plan reviewer | 保留 |
| omo.agentDesc.sisyphusJunior | 委托任务执行器 | 위임된 작업 실행자 | Delegated task executor | 保留 |
| omo.agentTooltip.sisyphus | 主编排器，负责任务规划、委派与并行执行，使用扩展思考（32k 预算），通过 TODO 驱动工作流确保任务完成。 | 작업 계획, 위임 및 병렬 실행을 담당하는 주 조정자입니다. 확장 추론(32k 예산)과 TODO 목록 기반 워크플로로 작업을 완료합니다. | Main orchestrator responsible for task planning, delegation and parallel execution. Uses extended thinking (32k budget) and drives workflows through TODO lists to ensure task completion. | 已修订 |
| omo.agentTooltip.atlas | 主编排器（持有 TODO 列表），负责执行阶段的任务分发与协调，不直接完成所有工作而是委派给专业代理。 | 실행 단계에서 작업 분배 및 조정을 담당하는 메인 오케스트레이터(TODO 목록 보유)입니다. 모든 업무를 직접 완료하기 보다는 전문 에이전트에게 위임합니다. | Main orchestrator (holds TODO list) responsible for task distribution and coordination during execution phase. Delegates to specialized agents rather than completing all work directly. | 保留 |
| omo.agentTooltip.prometheus | 战略规划师，通过访谈模式收集需求并制定详细工作计划，仅能在 .sisyphus/ 目录读写 Markdown 文件，从不直接写代码。 | 인터뷰 모드를 통해 요구사항을 수집하고 세부적인 업무 계획을 수립하는 전략 기획자입니다. .sisyphus/ 디렉터리에 있는 Markdown 파일을 읽고 쓸 수만 있고 코드를 직접 작성할 수는 없습니다. | Strategic planner that collects requirements through interview mode and creates detailed work plans. Can only read/write Markdown files in .sisyphus/ directory, never writes code directly. | 保留 |
| omo.agentTooltip.hephaestus | 自主深度工作者（「合法工匠」），受 AmpCode 深度模式启发，目标导向执行，行动前会并行启动 2-5 个探索/图书管理员代理进行研究。 | AmpCode의 심층 모드에서 영감을 받은 자율 심층 작업자(‘정당한 장인’)입니다. 목표 중심으로 실행하며, 행동하기 전에 explore/librarian 에이전트 2~5개를 병렬로 실행하여 조사합니다. | Autonomous deep worker ("legitimate craftsman") inspired by AmpCode deep mode. Goal-oriented execution that launches 2-5 explore/librarian agents in parallel for research before taking action. | 已修订 |
| omo.agentTooltip.oracle | 架构决策与调试顾问，只读咨询代理，提供出色的逻辑推理和深度分析，不能写文件或委派任务。 | 아키텍처 결정 및 디버깅 고문. 탁월한 논리적 추론과 심층 분석을 제공하는 읽기 전용 컨설팅 에이전트입니다. 파일을 쓰거나 작업을 위임할 수 없습니다. | Architecture decision and debugging advisor. Read-only consulting agent providing excellent logical reasoning and deep analysis. Cannot write files or delegate tasks. | 保留 |
| omo.agentTooltip.librarian | 多仓库分析与文档检索专家，深度理解代码库并提供基于证据的答案，擅长查找官方文档和开源实现示例。 | 다중 저장소 분석 및 문서 검색 전문가. 코드베이스를 깊이 이해하고 증거 기반 답변을 제공합니다. 공식 문서와 오픈 소스 구현 예제를 찾는 데 탁월합니다. | Multi-repository analysis and documentation retrieval expert. Deeply understands codebases and provides evidence-based answers. Excels at finding official documentation and open-source implementation examples. | 保留 |
| omo.agentTooltip.explore | 快速代码库探索与上下文 grep 专家，使用轻量级模型进行高速搜索，是理解代码结构的先锋。 | 빠른 코드베이스 탐색 및 컨텍스트 파악 전문가. 고속 검색을 위해 경량 모델을 사용합니다. 코드 구조를 이해하기 위한 스카우트입니다. | Fast codebase exploration and context grep expert. Uses lightweight models for high-speed search. The scout for understanding code structure. | 保留 |
| omo.agentTooltip.multimodalLooker | 视觉内容专家，分析 PDF、图片、图表等非文本媒体，提取其中的信息与洞察。 | PDF, 이미지, 차트 및 기타 텍스트가 아닌 미디어를 분석하여 정보와 통찰력을 추출하는 시각적 콘텐츠 전문가입니다. | Visual content expert that analyzes PDFs, images, charts and other non-text media, extracting information and insights from them. | 保留 |
| omo.agentTooltip.metis | 计划顾问，在规划前进行预分析，识别隐藏意图、模糊点和 AI 失败点，防止过度工程化。 | 기획 전 사전 분석을 수행하는 기획 컨설턴트입니다. 과도한 엔지니어링을 방지하기 위해 숨겨진 의도, 모호성 및 AI 실패 지점을 식별합니다. | Plan consultant that performs pre-analysis before planning. Identifies hidden intents, ambiguities and AI failure points to prevent over-engineering. | 保留 |
| omo.agentTooltip.momus | 计划评审员，高精度验证计划的清晰度、可验证性和完整性，拒绝并要求修订直到计划完美。 | 높은 정밀도로 계획의 명확성, 검증 가능성 및 완전성을 검증하는 계획 검토자입니다. 계획이 완벽해질 때까지 거부하고 수정을 요청합니다. | Plan reviewer that validates plan clarity, verifiability and completeness with high precision. Rejects and requests revisions until plans are perfect. | 保留 |
| omo.agentTooltip.sisyphusJunior | 类别生成的执行器，由 category 参数自动生成，专注于执行分配的任务且不能再委派，防止无限委派循环。 | 카테고리 매개변수를 통해 자동으로 생성되는 카테고리 생성 실행자입니다. 할당된 작업 실행에 중점을 두고 재위임할 수 없으므로 무한 위임 루프가 방지됩니다. | Category-generated executor, automatically created via category parameters. Focuses on executing assigned tasks and cannot re-delegate, preventing infinite delegation loops. | 保留 |
| omo.categoryDesc.visualEngineering | 视觉/前端工程 | 비주얼/프론트엔드 엔지니어링 | Visual/frontend engineering | 保留 |
| omo.categoryDesc.ultrabrain | 超级思考 | 고강도 추론 | Ultra thinking | 已修订 |
| omo.categoryDesc.deep | 深度工作 | 심층 작업 | Deep work | 保留 |
| omo.categoryDesc.artistry | 创意/文艺 | 창의적/예술적 | Creative/artistic | 保留 |
| omo.categoryDesc.quick | 快速响应 | 빠른 응답 | Quick response | 保留 |
| omo.categoryDesc.unspecifiedLow | 通用低配 | 일반 저사양 작업 | General low tier | 已修订 |
| omo.categoryDesc.unspecifiedHigh | 通用高配 | 일반 고사양 작업 | General high tier | 已修订 |
| omo.categoryDesc.writing | 写作 | 글쓰기 | Writing | 保留 |
| omo.categoryTooltip.visualEngineering | 前端与视觉工程类别，专注于 UI/UX 设计、样式、动画和界面实现，默认使用 Gemini 3.6 Flash 模型。 | UI/UX 디자인, 스타일링, 애니메이션 및 인터페이스 구현을 위한 프런트엔드 및 비주얼 엔지니어링 카테고리입니다. 기본값은 Gemini 3.6 Flash 모델입니다. | Frontend and visual engineering category for UI/UX design, styling, animation and interface implementation. Defaults to Gemini 3.6 Flash model. | 保留 |
| omo.categoryTooltip.ultrabrain | 深度逻辑推理类别，用于需要广泛分析的复杂架构决策，默认使用 GPT-5.3 Codex 的超高推理变体。 | 광범위한 분석이 필요한 복잡한 아키텍처 결정을 위한 심도 있는 논리적 추론 카테고리입니다. 기본값은 GPT-5.3 Codex 초고 추론 변형입니다. | Deep logical reasoning category for complex architectural decisions requiring extensive analysis. Defaults to GPT-5.3 Codex ultra-high reasoning variant. | 保留 |
| omo.categoryTooltip.deep | 深度自主问题解决类别，目标导向执行，行动前进行彻底研究，适用于需要深度理解的棘手问题。 | 목표 지향적 실행을 통한 심층적인 자율적 문제 해결 카테고리입니다. 행동하기 전에 철저한 조사를 수행하므로 깊은 이해가 필요한 어려운 문제에 적합합니다. | Deep autonomous problem-solving category with goal-oriented execution. Conducts thorough research before action, suitable for difficult problems requiring deep understanding. | 保留 |
| omo.categoryTooltip.artistry | 高度创意与艺术性任务类别，激发新颖想法和创造性解决方案，默认使用 Gemini 3.6 Flash 的高推理变体。 | 참신한 아이디어와 창의적인 솔루션에 영감을 주는 매우 창의적이고 예술적인 작업 카테고리입니다. 기본값은 Gemini 3.6 Flash high 변형입니다. | Highly creative and artistic task category that inspires novel ideas and creative solutions. Defaults to Gemini 3.6 Flash high variant. | 保留 |
| omo.categoryTooltip.quick | 轻量任务类别，用于单文件修改、错别字修复、简单调整等琐碎工作，默认使用 Claude Haiku 4.5 快速模型。 | 단일 파일 수정, 오타 수정, 간단한 조정을 위한 경량 작업 카테고리입니다. 기본값은 Claude Haiku 4.5 고속 모델입니다. | Lightweight task category for single-file modifications, typo fixes, and simple adjustments. Defaults to Claude Haiku 4.5 fast model. | 保留 |
| omo.categoryTooltip.unspecifiedLow | 未归类低工作量任务类别，适用于不适合其他类别且工作量较小的任务，默认使用 Claude Sonnet 4.5。 | 다른 범주에 속하지 않으며 작업량이 적은 작업을 위한 범주입니다. 기본 모델은 Claude Sonnet 4.5입니다. | Uncategorized low-effort task category for tasks that don't fit other categories with small workload. Defaults to Claude Sonnet 4.5. | 已修订 |
| omo.categoryTooltip.unspecifiedHigh | 未归类高工作量任务类别，适用于不适合其他类别且工作量较大的任务，默认使用 Claude Opus 5 的最大变体。 | 다른 범주에 속하지 않으며 작업량이 많은 작업을 위한 범주입니다. 기본 모델은 Claude Opus 5의 max 설정입니다. | Uncategorized high-effort task category for tasks that don't fit other categories with large workload. Defaults to Claude Opus 5 max variant. | 已修订 |
| omo.categoryTooltip.writing | 写作类别，专注于文档、散文和技术写作，默认使用 Kimi K2.5 模型。 | 문서, 산문 및 기술 문서 작성 카테고리입니다. 기본값은 Kimi K2.5 모델입니다. | Writing category for documentation, prose and technical writing. Defaults to Kimi K2.5 model. | 保留 |
| omo.slimAgentDesc.orchestrator | 编排者 | 오케스트레이터 | Orchestrator | 保留 |
| omo.slimAgentDesc.oracle | 神谕者 | Oracle | Oracle | 已修订 |
| omo.slimAgentDesc.librarian | 图书管理员 | 사서 | Librarian | 保留 |
| omo.slimAgentDesc.explorer | 探索者 | 탐색자 | Explorer | 已修订 |
| omo.slimAgentDesc.designer | 设计师 | 디자이너 | Designer | 保留 |
| omo.slimAgentDesc.fixer | 修复者 | 수정 담당 | Fixer | 已修订 |
| omo.slimAgentDesc.council | 议会 | 이사회 | Council | 保留 |
| omo.slimAgentTooltip.orchestrator | 编写执行代码，编排多代理工作流，召唤专家 | 실행 가능한 코드 작성, 다중 에이전트 워크플로 조정, 전문가 소환 | Writes executable code, orchestrates multi-agent workflow, summons experts | 保留 |
| omo.slimAgentTooltip.oracle | 根本原因分析、架构审查、调试指导（只读） | 근본 원인 분석, 아키텍처 검토, 디버깅 지침(읽기 전용) | Root cause analysis, architecture review, debugging guidance (read-only) | 保留 |
| omo.slimAgentTooltip.librarian | 文档查询、GitHub 代码搜索（只读） | 문서 조회, GitHub 코드 검색(읽기 전용) | Documentation lookup, GitHub code search (read-only) | 保留 |
| omo.slimAgentTooltip.explorer | 正则搜索、AST 模式匹配、文件发现（只读） | 정규식 검색, AST 패턴 일치, 파일 검색(읽기 전용) | Regex search, AST pattern matching, file discovery (read-only) | 保留 |
| omo.slimAgentTooltip.designer | 现代响应式设计、CSS/Tailwind 精通 | 현대적인 반응형 디자인, CSS/Tailwind 전문 지식 | Modern responsive design, CSS/Tailwind expertise | 保留 |
| omo.slimAgentTooltip.fixer | 代码实现、重构、测试、验证 | 코드 구현, 리팩토링, 테스트, 검증 | Code implementation, refactoring, testing, verification | 保留 |
| omo.slimAgentTooltip.council | 多模型共识代理，并行运行多个只读 councillor，再由 master 汇总最终答案。 | 다중 모델 합의 에이전트. 여러 읽기 전용 의원을 병렬로 실행한 다음 마스터가 최종 답변을 종합하도록 합니다. | Multi-model consensus agent. Runs multiple read-only councillors in parallel, then lets the master synthesize the final answer. | 保留 |
| openclawConfig.defaultModel.title | 默认模型 | 기본 모델 | Default Model | 保留 |
| openclawConfig.defaultModel.description | 配置 OpenClaw 的默认主模型和回退模型 | OpenClaw의 기본 주 모델과 대체 모델을 설정합니다 | Configure the default primary model and fallback models for OpenClaw | 已修订 |
| openclawConfig.defaultModel.primary | 主模型 | 기본 모델 | Primary Model | 保留 |
| openclawConfig.defaultModel.primaryPlaceholder | 例如: deepseek/deepseek-chat | 예: deepseek/deepseek-chat | e.g., deepseek/deepseek-chat | 保留 |
| openclawConfig.defaultModel.fallbacks | 回退模型 | 대체 모델 | Fallback Models | 保留 |
| openclawConfig.defaultModel.fallbacksPlaceholder | 例如: openrouter/anthropic/claude-sonnet-4.5 | 예: openrouter/anthropic/claude-sonnet-4.5 | e.g., openrouter/anthropic/claude-sonnet-4.5 | 保留 |
| openclawConfig.defaultModel.addFallback | 添加回退模型 | 대체 모델 추가 | Add Fallback Model | 保留 |
| openclawConfig.defaultModel.saved | 默认模型配置已保存 | 기본 모델 설정이 저장되었습니다. | Default model configuration saved | 已修订 |
| openclawConfig.defaultModel.saveFailed | 保存默认模型失败 | 기본 모델을 저장하지 못했습니다. | Failed to save default model | 保留 |
| openclawConfig.modelCatalog.title | 模型目录 | 모델 카탈로그 | Model Catalog | 保留 |
| openclawConfig.modelCatalog.description | 配置可用模型的别名和允许列表 | 모델 별칭 및 허용 목록 설정 | Configure model aliases and allowlist | 已修订 |
| openclawConfig.modelCatalog.modelId | 模型 ID | 모델 ID | Model ID | 保留 |
| openclawConfig.modelCatalog.modelIdPlaceholder | 例如: deepseek/deepseek-chat | 예: deepseek/deepseek-chat | e.g., deepseek/deepseek-chat | 保留 |
| openclawConfig.modelCatalog.alias | 别名 | 별칭 | Alias | 已修订 |
| openclawConfig.modelCatalog.aliasPlaceholder | 例如: DeepSeek | 예: DeepSeek | e.g., DeepSeek | 保留 |
| openclawConfig.modelCatalog.addEntry | 添加模型 | 모델 추가 | Add Model | 保留 |
| openclawConfig.modelCatalog.removeEntry | 移除 | 제거 | Remove | 保留 |
| openclawConfig.modelCatalog.saved | 模型目录已保存 | 모델 카탈로그가 저장되었습니다. | Model catalog saved | 保留 |
| openclawConfig.modelCatalog.saveFailed | 保存模型目录失败 | 모델 카탈로그를 저장하지 못했습니다. | Failed to save model catalog | 保留 |
| openclawConfig.modelCatalog.empty | 暂无模型目录配置 | 모델 카탈로그 항목이 없습니다. | No model catalog entries | 保留 |
| openclawConfig.modelCatalog.emptyHint | 添加模型到目录以配置别名 | 별칭을 설정하려면 카탈로그에 모델을 추가하세요. | Add models to the catalog to configure aliases | 已修订 |
| openclawConfig.suggestedDefaults | 应用建议默认配置 | 제안된 기본값 적용 | Apply Suggested Defaults | 保留 |
| openclawConfig.suggestedDefaultsHint | 使用此预设推荐的默认模型配置 | 이 프리셋의 권장 기본 모델 설정을 사용하세요. | Use this preset's recommended default model configuration | 已修订 |
| subscription.title | 订阅额度 | 구독 할당량 | Subscription Quota | 保留 |
| subscription.short.fiveHour | 5 小时 | 5시간 | 5h | 保留 |
| subscription.short.sevenDay | 每周 | 주 | Wk | 保留 |
| subscription.short.sevenDayFable | Fable | Fable | Fable | 已修订 |
| subscription.short.sevenDayOpus | Opus | Opus | Opus | 已修订 |
| subscription.short.sevenDaySonnet | Sonnet | Sonnet | Sonnet | 已修订 |
| subscription.short.thirtyDay | 30 天 | 30일 | 30d | 保留 |
| subscription.short.geminiPro | Pro | Pro | Pro | 已修订 |
| subscription.short.geminiFlash | Flash | Flash | Flash | 已修订 |
| subscription.short.geminiFlashLite | Lite | Lite | Lite | 已修订 |
| subscription.short.agyGeminiFiveHour | Gemini 5 小时 | Gemini 5시간 | Gemini 5h | 已修订 |
| subscription.short.agyGeminiWeekly | Gemini 每周 | Gemini 주간 | Gemini Wk | 已修订 |
| subscription.short.agyThirdPartyFiveHour | Claude 5 小时 | Claude 5시간 | Claude 5h | 已修订 |
| subscription.short.agyThirdPartyWeekly | Claude 每周 | Claude 주간 | Claude Wk | 已修订 |
| subscription.short.monthly | 每月 | 월 | Mo | 已修订 |
| subscription.short.credits | 额度 | 크레딧 | Credits | 保留 |
| subscription.short.copilotPremium | 高级请求 | 프리미엄 요청 | Premium | 已修订 |
| subscription.fiveHour | 5 小时 | 5시간 | 5-hour | 保留 |
| subscription.sevenDay | 每周 | 주간 | Weekly | 保留 |
| subscription.sevenDayFable | Fable | Fable | Fable | 已修订 |
| subscription.sevenDayOpus | 每周 Opus | 주간 Opus | Weekly Opus | 已修订 |
| subscription.sevenDaySonnet | 每周 Sonnet | 주간 Sonnet | Weekly Sonnet | 已修订 |
| subscription.thirtyDay | 30 天 | 30일 | 30-day | 保留 |
| subscription.geminiPro | Pro | Pro | Pro | 已修订 |
| subscription.geminiFlash | Flash | Flash | Flash | 已修订 |
| subscription.geminiFlashLite | Flash Lite | Flash Lite | Flash Lite | 已修订 |
| subscription.agyGemini | Gemini | Gemini | Gemini | 已修订 |
| subscription.agyThirdParty | Claude/GPT | Claude/GPT | Claude/GPT | 已修订 |
| subscription.agyGeminiFiveHour | Gemini 5 小时 | Gemini 5시간 | Gemini 5-hour | 已修订 |
| subscription.agyGeminiWeekly | Gemini 每周 | Gemini 주간 | Gemini weekly | 已修订 |
| subscription.agyThirdPartyFiveHour | Claude/GPT 5 小时 | Claude/GPT 5시간 | Claude/GPT 5-hour | 已修订 |
| subscription.agyThirdPartyWeekly | Claude/GPT 每周 | Claude/GPT 주간 | Claude/GPT weekly | 已修订 |
| subscription.weeklyLimit | 每周 | 주간 | Weekly | 保留 |
| subscription.monthly | 每月 | 월간 | Monthly | 已修订 |
| subscription.credits | 额度 | 크레딧 | Credits | 保留 |
| subscription.copilotPremium | 高级请求 | 프리미엄 요청 | Premium | 已修订 |
| subscription.utilization | {{value}}% | {{value}}% | {{value}}% | 保留 |
| subscription.resetsIn | {{time}}后重置 | {{time}} 후 초기화 | Resets in {{time}} | 已修订 |
| subscription.extraUsage | 超额用量 | 추가 사용량 | Extra Usage | 保留 |
| subscription.expired | 会话已过期 | 세션이 만료되었습니다. | Session expired | 保留 |
| subscription.expiredHint | 请运行 {{tool}} 命令刷新登录 | {{tool}} 명령을 실행하여 로그인을 새로 고치세요. | Run the {{tool}} command to refresh your login | 保留 |
| subscription.queryFailed | 查询失败 | 조회 실패 | Query failed | 已修订 |
| subscription.refresh | 刷新 | 새로 고침 | Refresh | 保留 |
| nav.mainLabel | 主导航 | 메인 네비게이션 | Main navigation | 保留 |
| nav.skipToContent | 跳到主要内容 | 주요 콘텐츠로 건너뛰기 | Skip to main content | 保留 |
| nav.expandSidebar | 展开侧栏 | 사이드바 확장 | Expand sidebar | 保留 |
| nav.collapseSidebar | 收起侧栏 | 사이드바 접기 | Collapse sidebar | 保留 |
| nav.appsGroup | 应用 | 앱 | Apps | 保留 |
| nav.today | 今日 {{value}} | 오늘 {{value}} | Today {{value}} | 保留 |
| nav.todayRequests | {{value}} 次 | {{value}} 요청 | {{value}} req | 保留 |
| nav.todayHitRate | 命中 {{value}} | 적중률 {{value}} | Hit {{value}} | 已修订 |
| nav.usage | 用量统计 | 사용량 | Usage | 保留 |
| nav.auth | 授权中心 | 인증 센터 | Accounts | 已修订 |
| nav.authNeedsReauth | 有账号需要重新登录 | 계정에 다시 로그인해야 합니다. | An account needs to sign in again | 保留 |
| nav.prompts | 提示词 | 프롬프트 | Prompts | 保留 |
| nav.sessions | 会话 | 세션 | Sessions | 保留 |
| nav.apps | 应用 | 앱 | Apps | 保留 |
| nav.appsTitle | 应用：安装、升级、在侧栏显示哪些 | 앱: 설치, 업그레이드, 사이드바에서 표시할 항목 선택 | Apps: install, upgrade, choose which show in the sidebar | 保留 |
| nav.appsHasUpdate | 应用 · 有可用更新 | 앱 · 업데이트 사용 가능 | Apps · updates available | 保留 |
| nav.settings | 设置 | 설정 | Settings | 保留 |
| nav.settingsHasUpdate | 设置 · CC Switch 有新版本 | 설정 · 새로운 CC Switch 버전을 사용할 수 있습니다 | Settings · a new CC Switch version is available | 保留 |
| nav.mode.route | 路由 | 라우팅 | Routing | 保留 |
| nav.mode.stack | 聚合 | 통합 | Aggregation | 保留 |
| nav.needsAttention | 需要处理 | 주의가 필요함 | Needs attention | 保留 |
| nav.back | 返回 | 뒤로 | Back | 保留 |
| appsPage.showInSidebar | 在侧栏显示 {{name}} | 사이드바에 {{name}} 표시 | Show {{name}} in the sidebar | 保留 |
| appsPage.lastChecked | 上次检查 {{time}} | 마지막 확인 {{time}} | Last checked {{time}} | 保留 |
| appsPage.neverChecked | 还没检查过更新 | 아직 업데이트를 확인하지 않았습니다. | Not checked for updates yet | 保留 |
| appsPage.helpTitle | 应用 | 앱 | Apps | 保留 |
| appsPage.helpBody | 在这里安装、升级命令行应用，并选择在侧栏显示哪些。 | 여기에서 명령줄 앱을 설치 및 업그레이드하고 사이드바에 표시할 앱을 선택하세요. | Install and upgrade command-line apps here, and choose which ones show in the sidebar. | 保留 |
| appsPage.checking | 检查中… | 확인 중… | Checking… | 保留 |
| appsPage.checkUpdates | 检查更新 | 업데이트 확인 | Check for updates | 保留 |
| appsPage.moreActions | 更多操作 | 추가 작업 | More actions | 保留 |
| appsPage.manualCommands | 手动安装命令 | 수동 설치 명령 | Manual install commands | 保留 |
| appsPage.columnApp | 应用 | 앱 | App | 保留 |
| appsPage.columnVersion | 版本 | 버전 | Version | 保留 |
| appsPage.columnVisible | 显示 | 표시 | Show | 已修订 |
| appsPage.visibleHelp | 关掉后，这个应用不再出现在侧栏、托盘菜单、MCP / Skills 的应用列，以及提示词和会话的应用下拉里。只是不显示：它的供应商、MCP 等配置都还在，它自己的配置文件也不会被改动。 | 끄면 앱이 더 이상 사이드바, 트레이 메뉴, MCP/Skills 앱 열 또는 프롬프트 및 세션의 앱 선택기에 표시되지 않습니다. 숨겨져 있을 뿐입니다. 공급자, MCP 서버 및 기타 설정은 그대로 유지되며 자체 설정 파일은 그대로 유지됩니다. | When off, the app no longer appears in the sidebar, the tray menu, the MCP / Skills app columns, or the app pickers on Prompts and Sessions. It is only hidden: its providers, MCP servers and other settings stay, and its own config files are left untouched. | 已修订 |
| appsPage.desktopHelp | Claude Desktop 是桌面应用，不能在这里安装或升级；CC Switch 通过它的配置文件接入。 | Claude Desktop는 데스크톱 앱이므로 여기에서 설치하거나 업그레이드할 수 없습니다. CC Switch는 설정 파일을 통해 연결됩니다. | Claude Desktop is a desktop app and can't be installed or upgraded here; CC Switch connects to it through its config file. | 已修订 |
| appsPage.desktopUnsupported | 当前系统不支持 | 이 시스템에서는 지원되지 않습니다 | Not supported on this system | 保留 |
| appsPage.desktopConnected | 已接入 | 연결됨 | Connected | 保留 |
| appsPage.desktopNotConnected | 未接入 | 연결되지 않음 | Not connected | 保留 |
| appsPage.newVersion | 有新版本 {{version}} | {{version}} 사용 가능 | {{version}} available | 保留 |
| appsPage.notRunnable | 无法运行 | 실행할 수 없습니다 | Can't run | 保留 |
| appsPage.updateNeedsNode | 新版本 {{version}} 要求 Node {{required}}，这处安装用的是 Node {{current}}，需要先升级 Node。 | 새 버전 {{version}}에는 Node {{required}}가 필요하지만 이 설치는 Node {{current}}을(를) 사용합니다. 먼저 Node를 업그레이드하세요. | {{version}} requires Node {{required}}, but this installation runs on Node {{current}}. Upgrade Node first. | 已修订 |
| appsPage.otherInstalls | 另有 {{count}} 处安装 | {{count}} 추가 설치 | {{count}} more install(s) | 保留 |
| appsPage.installsFound | 检测到 {{count}} 处安装 | {{count}} 설치를 찾았습니다. | {{count}} installs found | 保留 |
| appsPage.wslFlag | 标志 | 플래그 | Flag | 已修订 |
| appsPage.installHint.claude | 安装时运行官方安装脚本，失败时改用 npm | 공식 스크립트로 설치하며, 실패하면 npm을 사용합니다 | Installs with the official script, falls back to npm | 保留 |
| appsPage.installHint.codex | 通过 npm 安装 | npm으로 설치 | Installs with npm | 保留 |
| appsPage.installHint.gemini | 通过 npm 安装 | npm으로 설치 | Installs with npm | 保留 |
| appsPage.installHint.grok | 通过 npm 安装 | npm으로 설치 | Installs with npm | 保留 |
| appsPage.installHint.opencode | 安装时运行官方安装脚本，失败时改用 npm | 공식 스크립트로 설치하며, 실패하면 npm을 사용합니다 | Installs with the official script, falls back to npm | 保留 |
| appsPage.installHint.openclaw | 通过 npm 安装 | npm으로 설치 | Installs with npm | 保留 |
| appsPage.installHint.hermes | 安装时运行官方安装脚本 | 공식 스크립트로 설치 | Installs with the official script | 保留 |
| appsPage.installHint.pi | 通过 npm 安装 | npm으로 설치 | Installs with npm | 保留 |
| appsPage.installHint.mcode | 安装时运行官方安装脚本，失败时改用 npm | 공식 스크립트로 설치하며, 실패하면 npm을 사용합니다 | Installs with the official script, falls back to npm | 保留 |
| appsPage.installHint.agy | 安装时运行官方安装脚本 | 공식 스크립트로 설치 | Installs with the official script | 保留 |
| appPage.moreActions | {{name}} 的更多操作 | {{name}}에 대한 추가 작업 | More actions for {{name}} | 保留 |
| appPage.viewSessions | 查看会话 | 세션 보기 | View sessions | 保留 |
| appPage.configDirectory | 配置目录 | 설정 디렉토리 | Config directory | 已修订 |
| appPage.installAndUpgrade | 安装与升级 | 설치 및 업그레이드 | Install and upgrade | 保留 |
| appPage.hideFromSidebar | 在侧栏隐藏 | 사이드바에서 숨기기 | Hide from sidebar | 保留 |
| appPage.providers | 供应商 | 공급자 | Providers | 已修订 |
| appPage.workspace | 工作区 | 작업 공간 | Workspace | 已修订 |
| appPage.openclawConfig | 配置 | 설정 | Config | 已修订 |
| appPage.memory | 记忆 | 메모리 | Memory | 保留 |
| appPage.webUi | Web UI | 웹 UI | Web UI | 保留 |
| appPage.viewUsage | 查看此应用的用量 | 이 앱의 사용량 보기 | View usage for this app | 保留 |
| mode.tabsLabel | 连接模式 | 연결 모드 | Connection mode | 保留 |
| mode.names.direct | 直连 | 직접 연결 | Direct | 保留 |
| mode.names.route | 路由 | 라우팅 | Routing | 保留 |
| mode.names.stack | 聚合 | 통합 | Aggregation | 保留 |
| mode.active | 生效中 | 적용 중 | active | 已修订 |
| mode.activeTitle | {{mode}}生效中 | {{mode}}가 활성화되었습니다 | {{mode}} is active | 保留 |
| mode.noProvider | 未选择 | 없음 | none | 保留 |
| mode.failover | 故障转移 | 장애 조치 | Failover | 保留 |
| mode.routeSettings | 路由设置 | 라우팅 설정 | Routing settings | 保留 |
| mode.routeSettingsTitle | 路由设置 | 라우팅 설정 | Routing settings | 保留 |
| mode.moreRouteSettings | 更多路由设置 | 라우팅 설정 더보기 | More routing settings | 保留 |
| mode.stackSettings.title | 聚合设置 | 통합 설정 | Aggregation settings | 已修订 |
| mode.stackSettings.subagentDescription | 子代理默认跟随主模型。选一个聚合里的模型后，主代理派出的子代理默认用它（主代理派单时自己指定了模型的除外）。不用重启 Codex，新开的对话就会用上；已经开着的对话仍按原来的设置。 | 서브에이전트는 기본으로 주 모델을 따릅니다. 통합된 모델을 선택하면 주 에이전트가 생성하는 서브에이전트가 기본으로 해당 모델을 사용합니다. 단, 생성할 때 주 에이전트가 모델을 직접 지정한 경우는 제외합니다. Codex를 다시 시작할 필요 없이 새 대화부터 적용되며, 이미 열린 대화는 이전 설정을 유지합니다. | Sub-agents follow the main model by default. Pick an aggregated model and the sub-agents the main agent spawns use it by default (unless the main agent names a model when spawning). No Codex restart needed: new conversations pick it up, conversations already open keep the previous setting. | 已修订 |
| mode.stackSettings.subagentModel | 子代理模型 | 서브에이전트 모델 | Sub-agent model | 已修订 |
| mode.stackSettings.followMain | 跟随主模型 | 주 모델 따르기 | Follow the main model | 已修订 |
| mode.stackSettings.subagentEffort | 子代理推理强度 | 서브에이전트 추론 수준 | Sub-agent reasoning effort | 已修订 |
| mode.stackSettings.effortModelDefault | 模型默认 | 모델 기본값 | Model default | 保留 |
| mode.stackSettings.effortModelDefaultNamed | 模型默认（{{effort}}） | 모델 기본값({{effort}}) | Model default ({{effort}}) | 保留 |
| mode.stackSettings.unavailableOption | {{model}}（已不在聚合里） | {{model}} (통합 목록에서 제외됨) | {{model}} (no longer aggregated) | 已修订 |
| mode.stackSettings.unavailable | 所选模型已不在聚合名单里（成员被移除或模型不再发布），子代理暂时跟随主模型；加回来后自动恢复。 | 선택한 모델이 통합 목록에서 제외되었습니다. 공급자가 제거되었거나 모델 제공을 중단했으므로 서브에이전트는 일시적으로 주 모델을 따릅니다. 다시 추가하면 기존 설정이 복원됩니다. | The selected model is no longer in the aggregation (the provider was removed or stopped publishing it), so sub-agents follow the main model for now. It comes back once you add it again. | 已修订 |
| mode.stackSettings.noModels | 聚合名单里还没有发布的模型，先把供应商加入聚合。 | 통합 목록에 제공되는 모델이 없습니다. 먼저 공급자를 통합에 추가하세요. | No aggregated models are published yet. Add providers to the aggregation first. | 已修订 |
| mode.stackSettings.classicOff | 子代理和主代理不在同一家，Codex 新版的子 agent 工具会把任务加密，只有主代理那家解得开，子代理会收不到任务。必须打开下面的「聚合模式下子 agent 用经典工具」。 | 서브에이전트와 주 에이전트의 공급자가 다릅니다. Codex의 새 서브에이전트 도구는 주 에이전트의 공급자만 해독할 수 있게 작업을 암호화하므로 서브에이전트가 작업을 받지 못합니다. 아래의 ‘통합 모드에서 기존 서브에이전트 도구 사용’을 반드시 켜세요. | The sub-agent runs on a different provider from the main agent, so Codex's new sub-agent tools encrypt its task where only the main agent's provider can read it, and the sub-agent receives nothing. You must turn on "Classic sub-agent tools in aggregation" below. | 已修订 |
| mode.stackSettings.autoReviewModel | 自动审批模型 | 자동 승인 모델 | Auto Review model | 已修订 |
| mode.stackSettings.autoReviewDescription | Codex 开了自动审批（Approve for me）时，判断操作能不能放行用的模型，可以选聚合里别家的模型。改完需要重启 Codex。 | 자동 승인(Approve for me)이 켜져 있을 때 Codex가 작업 허용 여부를 판단하는 데 사용할 모델입니다. 통합 목록에 있는 다른 공급자의 모델도 선택할 수 있습니다. 변경 후 Codex를 다시 시작하세요. | The model Codex uses to decide whether an action may go ahead when automatic approval (Approve for me) is on. It can be another provider's aggregated model. Restart Codex after changes. | 已修订 |
| mode.stackSettings.autoReviewDefaultOfficial | 官方 Auto Review（默认） | 공식 Auto Review (기본값) | Official Auto Review (default) | 已修订 |
| mode.stackSettings.autoReviewDefaultMain | 主模型自己审批（默认） | 주 모델이 직접 승인 (기본값) | Main model reviews itself (default) | 已修订 |
| mode.stackSettings.autoReviewUnavailable | 所选模型已不在聚合名单里（成员被移除或模型不再发布），审批暂时用默认模型；加回来后自动恢复。 | 선택한 모델이 통합 목록에서 제외되었습니다. 공급자가 제거되었거나 모델 제공을 중단했으므로 일시적으로 기본 승인 모델을 사용합니다. 다시 추가하면 기존 설정이 복원됩니다. | The selected model is no longer in the aggregation (the provider was removed or stopped publishing it), so approvals use the default reviewer for now. It comes back once you add it again. | 已修订 |
| mode.stackSettings.saveFailed | 保存失败：{{error}} | 저장 실패: {{error}} | Failed to save: {{error}} | 保留 |
| mode.queueMoved | {{name}} 移到第 {{position}} 位。 | {{name}}가 {{position}} 위치로 이동되었습니다. | {{name}} moved to position {{position}}. | 保留 |
| mode.status.directLead | 直连生效中 · 直接连接 | 직접 연결 적용 중 · 연결 대상 | Direct is active · connected to | 已修订 |
| mode.status.routeLead | 路由生效中 | 라우팅이 활성화되었습니다. | Routing is active | 保留 |
| mode.status.byQueue | 按队列 | 대기열별 | by queue | 保留 |
| mode.status.stackLead | 聚合生效中 · 默认 | 통합 적용 중 · 기본값 | Aggregation is active · default | 已修订 |
| mode.status.stackValue | {{name}} · 另有 {{count}} 家共 {{models}} 个模型 | {{name}} · 그 외 공급자 {{count}}곳, 총 모델 {{models}}개 | {{name}} · {{count}} more with {{models}} models | 已修订 |
| mode.activate.viewing | 你在查看「{{view}}」，{{app}} 目前是{{active}}。 | 당신은 "{{view}}"을(를) 보고 있습니다. {{app}}는 현재 {{active}}에 있습니다. | You're viewing “{{view}}”. {{app}} is currently on {{active}}. | 已修订 |
| mode.activate.route | 开始路由 | 라우팅 시작 | Start routing | 保留 |
| mode.activate.stack | 切换到聚合模式 | 통합 모드로 전환 | Switch to Aggregation | 已修订 |
| mode.activate.direct | 回到直连 | 직접 연결로 돌아가기 | Back to direct | 已修订 |
| mode.notice.serviceDown | {{app}} 处于{{mode}}模式，但路由服务没有运行，请求会失败。 | {{app}}는 {{mode}} 모드에 있지만 라우팅 서비스가 실행되고 있지 않으므로 요청이 실패합니다. | {{app}} is in {{mode}} mode but the routing service isn't running, so requests will fail. | 保留 |
| mode.notice.startService | 启动服务 | 서비스 시작 | Start service | 保留 |
| mode.notice.backToDirect | 回到直连 | 직접 연결로 돌아가기 | Back to direct | 已修订 |
| mode.notice.attachFailed | 上次的{{mode}}模式没能接上，{{app}} 已回到直连。 | 이전에 {{mode}} 모드에 다시 연결하지 못하여 {{app}}을(를) 직접 연결로 되돌렸습니다. | {{mode}} couldn't reconnect last time, so {{app}} went back to direct. | 已修订 |
| mode.toast.enteredRoute | {{app}} 已开始路由 → {{provider}}。 | 이제 {{app}}가 → {{provider}}로 라우팅됩니다. | {{app}} is now routing → {{provider}}. | 保留 |
| mode.toast.enteredStack | {{app}} 已切换到聚合模式。重启 {{app}} 后，聚合的模型出现在 /model 里。 | {{app}}을(를) 통합 모드로 전환했습니다. {{app}}을(를) 다시 시작하면 /model에 통합된 모델이 표시됩니다. | {{app}} switched to Aggregation. Restart {{app}} to see the aggregated models in /model. | 已修订 |
| mode.toast.enteredStackLive | {{app}} 已切换到聚合模式，聚合的模型已出现在 /model 里。 | {{app}}을(를) 통합 모드로 전환했습니다. /model에 통합된 모델이 표시됩니다. | {{app}} switched to Aggregation. The aggregated models are now in /model. | 已修订 |
| mode.toast.enteredStackDesktop | {{app}} 已切换到聚合模式。重启 {{app}} 后，聚合的模型出现在模型列表里。 | {{app}}을(를) 통합 모드로 전환했습니다. {{app}}을(를) 다시 시작하면 모델 목록에 통합된 모델이 표시됩니다. | {{app}} switched to Aggregation. Restart {{app}} to see the aggregated models in its model list. | 已修订 |
| mode.toast.exited | 已回到直连：{{app}} 现在直接连接 {{provider}}。 | 직접 연결로 돌아왔습니다. 이제 {{app}}이(가) {{provider}}에 직접 연결됩니다. | Back to direct: {{app}} now connects to {{provider}} directly. | 已修订 |
| mode.toast.routeRemembered | 已记住供应商 {{provider}}，客户端接入路由或聚合后使用。 | 클라이언트가 라우팅 또는 통합 모드에 연결될 때 사용할 공급자 {{provider}}을(를) 저장했습니다. | Provider {{provider}} saved for when the client connects through routing or aggregation. | 已修订 |
| mode.toast.routeTargetChanged | 路由目标已设为 {{provider}}。 | 라우팅 대상을 {{provider}}(으)로 설정했습니다. | Route target set to {{provider}}. | 已修订 |
| mode.toast.routeSwitched | 路由已切换至 {{provider}}，后续新请求将使用该供应商。 | 라우팅 대상을 {{provider}}(으)로 전환했습니다. 이후 새 요청은 이 공급자를 사용합니다. | Route switched to {{provider}}. New requests will use this provider. | 已修订 |
| mode.toast.stackDefaultChanged | 聚合默认供应商已设为 {{provider}}；已选聚合模型仍使用各自的供应商。 | 통합 기본 공급자를 {{provider}}(으)로 설정했습니다. 이미 선택한 통합 모델은 각자의 공급자를 계속 사용합니다. | Aggregation default set to {{provider}}. Selected aggregated models still use their respective providers. | 已修订 |
| mode.toast.clientConfigChanged | 客户端配置也已更新；重启 {{app}} 以加载更新后的配置。 | 클라이언트 설정도 변경되었습니다. 업데이트된 설정을 로드하려면 {{app}}을(를) 다시 시작하세요. |  Client configuration also changed. Restart {{app}} to load the updated configuration. | 已修订 |
| mode.toast.defaultRemembered | 切换到聚合模式后，默认供应商是 {{provider}}。 | 통합 모드로 전환하면 {{provider}}이(가) 기본 공급자가 됩니다. | {{provider}} will be the default provider once you switch to Aggregation. | 已修订 |
| mode.toast.restartHint | 重启 {{app}} 后生效。 | 적용하려면 {{app}}을(를) 다시 시작하세요. |  Restart {{app}} to apply. | 已修订 |
| mode.toast.failed | 切换失败：{{detail}} | 전환할 수 없음: {{detail}} | Couldn't switch: {{detail}} | 保留 |
| mode.dialog.routeTitle | 让 {{app}} 使用路由模式？ | {{app}}에 라우팅을 사용하시겠습니까? | Use routing for {{app}}? | 保留 |
| mode.dialog.stackTitle | 让 {{app}} 使用聚合模式？ | {{app}}에 통합 모드를 사용하시겠습니까? | Use Aggregation for {{app}}? | 已修订 |
| mode.dialog.switchTitle | 把 {{app}} 从「{{from}}」切换到「{{to}}」？ | {{app}}을(를) "{{from}}"에서 "{{to}}"로 전환하시겠습니까? | Switch {{app}} from “{{from}}” to “{{to}}”? | 已修订 |
| mode.dialog.routeLead | 请求会先经过本机的 CC Switch，再转给你选的供应商。 | 요청은 먼저 이 시스템의 CC Switch를 거쳐 선택한 공급자에게 전달됩니다. | Requests go through CC Switch on this machine first, then to the provider you pick. | 已修订 |
| mode.dialog.stackLead | 默认供应商承接不带前缀的请求。 | 접두사가 없는 요청은 기본 공급자가 처리합니다. | The default provider takes requests without a prefix. | 已修订 |
| mode.dialog.routeTo | 路由到 | 라우팅 대상 | Route to | 保留 |
| mode.dialog.stackDefault | 默认供应商 | 기본 공급자 | Default provider | 已修订 |
| mode.dialog.officialOption | {{name}}（官方） | {{name}} (공식) | {{name}} (official) | 保留 |
| mode.dialog.stackOfficialNote | 如果你在用官方订阅，请把官方账号设为默认供应商。 | 공식 구독을 사용하는 경우 공식 계정을 기본 공급자로 설정하세요. | If you use an official subscription, set the official account as the default provider. | 已修订 |
| mode.dialog.routeNoteFile | 会改写 {{file}} 里的地址和密钥；真实密钥留在 CC Switch 里，其他设置不动。 | {{file}}의 주소와 API 키를 변경하여 저장합니다. 실제 API 키는 CC Switch에 보관하며 다른 설정은 변경하지 않습니다. | Rewrites the address and key in {{file}}. The real key stays in CC Switch; other settings are untouched. | 已修订 |
| mode.dialog.routeNoteSwitch | 之后在「路由」页签里换供应商，不再改写配置文件。 | 이후 ‘라우팅’ 탭에서 공급자를 바꿀 때는 설정 파일을 다시 저장하지 않습니다. | Changing providers later on the Routing tab won't rewrite the config file. | 已修订 |
| mode.dialog.routeNoteKeepRunning | CC Switch 需要保持运行；退出时自动写回直连，下次启动再接上。 | CC Switch를 실행 상태로 유지하세요. 종료하면 직접 연결 설정이 복원되며, 다음 실행 시 다시 연결됩니다. | Keep CC Switch running. Quitting writes the direct config back; it reconnects on the next start. | 保留 |
| mode.dialog.desktopRouteNoteModels | Claude Desktop 的模型列表换成路由那家的模型；之后换路由那家会改写配置文件。 | Claude Desktop의 모델 목록을 라우팅 대상 공급자의 모델로 바꿉니다. 이후 라우팅 대상 공급자를 전환하면 설정 파일을 다시 저장합니다. | Claude Desktop's model list becomes the routed provider's models; switching the routed provider later rewrites the config file. | 已修订 |
| mode.dialog.desktopRouteNoteRestart | {{app}} 只在启动时读配置，确认后要重启 {{app}} 才生效。 | {{app}}은(는) 시작할 때만 설정을 읽으므로 확인 후 {{app}}을(를) 다시 시작해야 적용됩니다. | {{app}} only reads its config at launch: restart {{app}} after confirming. | 已修订 |
| mode.dialog.desktopRouteNoteKeepRunning | CC Switch 需要保持运行，{{app}} 的请求才能转出去。 | {{app}}의 요청을 전달할 수 있도록 CC Switch를 계속 실행하세요. | Keep CC Switch running so {{app}}'s requests can go out. | 已修订 |
| mode.dialog.stackNoteMembers | 另有 {{names}} 共 {{count}} 个模型，会以 ccs- 前缀出现在 /model 里。 | {{names}}의 모델 {{count}}개를 추가하며 /model에 ccs- 접두사와 함께 표시합니다. | {{names}} add {{count}} models, shown in /model with the ccs- prefix. | 已修订 |
| mode.dialog.desktopStackNoteMembers | 另有 {{names}} 共 {{count}} 个模型，会加进 Claude Desktop 的模型列表，显示为「供应商 / 模型」。 | {{names}}는 "공급자/모델"로 표시된 Claude Desktop 모델 목록에 {{count}} 모델을 추가합니다. | {{names}} add {{count}} models to the Claude Desktop model list, shown as "Provider / model". | 已修订 |
| mode.dialog.stackNoteEmpty | 还没有添加其他供应商，切换后只有默认供应商；可以之后在「聚合」页签里添加。 | 다른 공급자를 아직 추가하지 않아 기본 공급자만 사용할 수 있습니다. 나중에 통합 탭에서 추가할 수 있습니다. | No other providers added yet, so only the default is available. You can add more on the Aggregation tab later. | 已修订 |
| mode.dialog.stackNoteNoFailover | 聚合模式不做故障转移；队列和设置会保留，回到路由模式后恢复。 | 통합 모드에서는 장애 조치를 사용하지 않습니다. 대기열과 설정은 유지되며 라우팅 모드로 돌아가면 다시 적용됩니다. | Aggregation has no failover. The queue and its settings are kept and come back with routing. | 已修订 |
| mode.dialog.stackNoteRestartCodex | 需要重启 {{app}} 才能看到聚合的模型；桌面版要彻底退出后重新打开。 | 통합된 모델을 보려면 {{app}}을(를) 다시 시작하세요. 데스크톱 앱은 완전히 종료한 후 다시 열어야 합니다. | Restart {{app}} to see the aggregated models; quit the desktop app completely and reopen it. | 已修订 |
| mode.dialog.stackSubagentLead | 子代理默认跟随主模型，也可以选聚合里的一个模型（之后在「聚合设置」里随时能改）。 | 서브에이전트는 기본으로 주 모델을 따릅니다. 통합된 모델을 따로 선택할 수도 있으며 나중에 통합 설정에서 언제든지 바꿀 수 있습니다. | Sub-agents follow the main model by default; you can also pick an aggregated model (change it any time later in Aggregation settings). | 已修订 |
| mode.dialog.leaveStackNote | 以 ccs- 开头的聚合模型会从 /model 里消失；聚合名单不会删，切回聚合模式就回来。正在用其中某个的话，要在 /model 里换回普通模型。 | ccs- 접두사로 시작하는 통합 모델이 /model에서 사라집니다. 통합 목록은 유지되며 통합 모드로 돌아가면 다시 표시됩니다. 해당 모델을 사용 중이라면 /model에서 일반 모델로 바꾸세요. | The ccs- aggregated models disappear from /model. The aggregation list is kept and they come back when you switch to aggregation again. If you're using one of them, pick a regular model in /model. | 已修订 |
| mode.dialog.desktopLeaveStackNote | 聚合的模型会从 Claude Desktop 的模型列表撤下，重启后生效；聚合名单不会删，切回聚合模式就回来。正在用其中某个的话，要换回普通模型。 | 다시 시작하면 Claude Desktop 모델 목록에서 통합 모델이 제거됩니다. 통합 목록은 유지되며 통합 모드로 돌아가면 다시 표시됩니다. 해당 모델을 사용 중이라면 일반 모델로 바꾸세요. | Aggregated models are withdrawn from the Claude Desktop model list after a restart. The aggregation list is kept and they come back when you switch to aggregation again. If you're using one of them, pick a regular model. | 已修订 |
| mode.dialog.exitTitle | 把 {{app}} 从「{{from}}」切回直连？ | {{app}}을(를) ‘{{from}}’에서 직접 연결로 되돌리시겠습니까? | Switch {{app}} from “{{from}}” back to direct? | 已修订 |
| mode.dialog.exitLead | {{app}} 会直接连接 {{provider}}，请求不再经过 CC Switch。 | {{app}}는 {{provider}}에 직접 연결됩니다. 요청은 더 이상 CC Switch를 거치지 않습니다. | {{app}} will connect to {{provider}} directly; requests no longer go through CC Switch. | 保留 |
| mode.dialog.exitNoteFile | 会把 {{file}} 里的地址和密钥改回 {{provider}} 的，其他设置不动。 | {{file}}의 주소와 키를 다시 {{provider}}의 주소와 키로 다시 씁니다. 다른 설정은 그대로 유지됩니다. | Rewrites the address and key in {{file}} back to {{provider}}'s; other settings are untouched. | 保留 |
| mode.dialog.exitNoteRouteKept | 路由目标、故障转移队列和设置都会保留，下次开始路由时恢复。 | 라우팅 대상, 장애 조치 대기열 및 설정은 유지되며 다음에 라우팅을 시작할 때 다시 나타납니다. | The routing target, failover queue and settings are kept and come back the next time you start routing. | 保留 |
| mode.dialog.desktopExitNoteRouteKept | 路由目标会保留，下次开始路由时恢复。 | 라우팅 대상은 유지되며 다음에 라우팅을 시작할 때 다시 나타납니다. | The routing target is kept and comes back the next time you start routing. | 保留 |
| mode.dialog.confirmDirect | 回到直连 | 직접 연결로 돌아가기 | Back to direct | 已修订 |
| mode.dialog.confirmRoute | 开始路由 | 라우팅 시작 | Start routing | 保留 |
| mode.dialog.confirmStack | 切换到聚合模式 | 통합 모드로 전환 | Switch to Aggregation | 已修订 |
| mode.dialog.needsRouteTitle | {{provider}} 需要路由 | {{provider}}에는 라우팅이 필요합니다 | {{provider}} needs routing | 保留 |
| mode.dialog.needsRouteLead | {{provider}}：{{reason}}。直连切换过去，{{app}} 会无法使用它。 | {{provider}}: {{reason}}. 직접 연결로 전환하면 {{app}}에서 이 공급자를 사용할 수 없습니다. | {{provider}}: {{reason}}. If you switch to it directly, {{app}} won't be able to use it. | 已修订 |
| mode.dialog.switchAnyway | 仍然直连切换 | 그래도 직접 연결로 전환 | Switch directly anyway | 已修订 |
| mode.dialog.routeAndUse | 开始路由并使用它 | 라우팅을 시작하고 사용 | Start routing and use it | 已修订 |
| mode.help.title | 连接模式的区别 | 연결 모드의 차이점 | How the connection modes differ | 保留 |
| mode.help.direct | 直连：CC Switch 不经手任何请求，客户端直接连所选供应商，体验最原生。 | 직접 연결: 요청을 CC Switch를 거치지 않고 클라이언트에서 선택한 공급자로 바로 보냅니다. 클라이언트 본연의 동작을 그대로 사용할 수 있습니다. | Direct: CC Switch never touches your requests; the client talks to the chosen provider itself for the most native experience. | 已修订 |
| mode.help.route | 路由：请求经本机 CC Switch 转发，可热切换供应商，并支持故障转移、格式转换等高级功能。 | 라우팅: 이 컴퓨터의 CC Switch가 요청을 전달합니다. 공급자 실시간 전환, 장애 조치, 형식 변환 등 고급 기능을 사용할 수 있습니다. | Routing: requests go through CC Switch on this machine, unlocking hot-switching providers, failover, format conversion, and other advanced features. | 已修订 |
| mode.help.stack | 聚合：多家供应商的模型同列在 /model，在客户端内即可无感切换。 | 통합: 여러 공급자의 모델을 /model에 함께 표시하여 클라이언트 안에서 간편하게 전환할 수 있습니다. | Aggregation: models from several providers sit together in /model, so you can switch between them seamlessly inside the client. | 已修订 |
| providerCard.status.inUse | 使用中 | 사용 중 | In use | 保留 |
| providerCard.status.routing | 路由中 | 라우팅 | Routing | 保留 |
| providerCard.status.currentDefault | 当前默认 | 현재 기본값 | Current default | 保留 |
| providerCard.status.defaultAfterSwitch | 切换后默认 | 전환 후 기본값 | Default after switching | 保留 |
| providerCard.status.current | 当前 | 현재 | Current | 已修订 |
| providerCard.status.default | 默认 | 기본값 | Default | 保留 |
| providerCard.action.switch | 切换 | 전환 | Switch | 已修订 |
| providerCard.action.routeHere | 路由到此 | 여기로 라우팅 | Route here | 保留 |
| providerCard.action.backToDirectAndUse | 回到直连并使用 | 직접 연결로 돌아가서 사용 | Back to direct and use | 已修订 |
| providerCard.action.addToQueue | 加入队列 | 대기열에 추가 | Add to queue | 保留 |
| providerCard.action.removeFromQueue | 移出队列 | 대기열에서 제거 | Remove from queue | 保留 |
| providerCard.action.setDefault | 设为默认 | 기본값으로 설정 | Set as default | 保留 |
| providerCard.action.add | 添加 | 추가 | Add | 已修订 |
| providerCard.action.remove | 移除 | 제거 | Remove | 保留 |
| providerCard.action.enable | 启用 | 활성화 | Enable | 保留 |
| providerCard.action.disable | 停用 | 비활성화 | Disable | 保留 |
| providerCard.action.edit | 编辑 {{name}} | {{name}} 편집 | Edit {{name}} | 保留 |
| providerCard.action.more | {{name}} 的更多操作 | {{name}}에 대한 추가 작업 | More actions for {{name}} | 保留 |
| providerCard.action.moveUp | {{name}} 上移一位 | {{name}}을(를) 위로 이동 | Move {{name}} up | 已修订 |
| providerCard.action.moveDown | {{name}} 下移一位 | {{name}}을(를) 아래로 이동 | Move {{name}} down | 已修订 |
| providerCard.chip.official | 官方 | 공식 | Official | 已修订 |
| providerCard.chip.needsRoute | 需要路由 | 라우팅 필요 | Needs routing | 保留 |
| providerCard.chip.directWhenDirect | 直连时使用 | 직접 연결 시 사용 | Used when direct | 已修订 |
| providerCard.chip.default | 默认 | 기본값 | Default | 保留 |
| providerCard.chip.models | {{count}} 个模型 | {{count}} 모델 | {{count}} models | 保留 |
| providerCard.chip.noModels | 没有模型 | 모델 없음 | No models | 保留 |
| providerCard.chip.direct | 直连 | 직접 연결 | Direct | 保留 |
| providerCard.chip.hermesManaged | Hermes 托管 | Hermes에서 관리함 | Managed by Hermes | 保留 |
| providerCard.chip.defaultModel | 默认模型 {{model}} | 기본 모델 {{model}} | Default model {{model}} | 保留 |
| providerCard.reason.noRoute | 官方订阅不经过路由，回到直连后可用。 | 공식 구독은 라우팅을 거치지 않습니다. 직접 연결 모드로 돌아가면 사용할 수 있습니다. | Official subscriptions don't go through routing; available again in direct mode. | 已修订 |
| providerCard.reason.noStack | 官方订阅不能用于聚合模式。 | 공식 구독은 통합 모드에서 사용할 수 없습니다. | Official subscriptions can't be used in Aggregation. | 已修订 |
| providerCard.reason.officialStack | 官方账号只能做默认，不能加入聚合。 | 공식 계정은 기본 공급자로만 사용할 수 있으며 통합 목록에는 추가할 수 없습니다. | Official accounts can only be the default; they can't join the aggregation. | 已修订 |
| providerCard.reason.defaultWhileRouting | 正在路由时，默认就是路由到的那家；切换到聚合模式时可以另选。 | 라우팅 중에는 라우팅 대상이 기본 공급자입니다. 통합 모드로 전환할 때 다른 공급자를 선택할 수 있습니다. | While routing, the default is the provider you route to. You can pick another one when switching to Aggregation. | 已修订 |
| providerCard.reason.needsRoute | 需要路由：{{reason}}，不能直连。 | 라우팅 필요: {{reason}}; 직접 연결할 수 없습니다. | Needs routing: {{reason}}; can't connect directly. | 保留 |
| providerCard.reason.defaultCannotRemove | 默认那家不能移除，先把别家设为默认。 | 기본값은 제거할 수 없습니다. 먼저 다른 공급자를 기본값으로 설정하세요. | The default can't be removed. Make another provider the default first. | 已修订 |
| providerCard.reason.currentCannotRemove | 正在用的这家不能移除，先启用别家。 | 사용 중인 공급자는 제거할 수 없습니다. 먼저 다른 공급자를 활성화하세요. | The provider in use can't be removed. Enable another one first. | 已修订 |
| providerCard.reason.inUseCannotDelete | 正在用的这家不能删除，先切到别家。 | 사용 중인 공급자는 삭제할 수 없습니다. 먼저 다른 것으로 전환하십시오. | The provider in use can't be deleted. Switch to another one first. | 已修订 |
| providerCard.reason.directDefaultCannotDelete | 退出路由后会回到这家，所以不能删除。先在直连页对别家点「回到直连并使用」，再删除。 | 라우팅을 종료하면 이 공급자로 돌아오므로 삭제할 수 없습니다. 먼저 직접 연결 페이지에서 다른 공급자의 ‘직접 연결로 돌아가서 사용’을 선택하세요. | Leaving routing switches back to this provider, so it can't be deleted. On the direct page, choose "Back to direct and use" on another provider first. | 已修订 |
| providerCard.reason.noFailover | 官方账号不进故障转移队列：它用客户端自己的登录，不能和别家轮换。 | 공식 계정은 장애 조치 대기열에 참여할 수 없습니다. 클라이언트 자체 로그인을 사용하고 다른 공급자와 순환할 수 없습니다. | Official accounts can't join the failover queue: they use the client's own login and can't rotate with other providers. | 已修订 |
| providerCard.section.queue | 队列 · 按优先级（{{count}}） | 대기열 · 우선순위별({{count}}) | Queue · by priority ({{count}}) | 保留 |
| providerCard.section.queueHelpTitle | 故障转移队列 | 장애 조치 대기열 | Failover queue | 保留 |
| providerCard.section.queueHelp | 请求先发给第一位；它连续失败时自动换到下一位。用上移、下移或拖动调整顺序。 | 첫 번째 공급자에 요청을 보내며 연속 실패하면 다음 공급자로 전환합니다. 위로/아래로 이동하거나 드래그하여 순서를 바꾸세요. | Requests go to the first provider; after repeated failures they move to the next. Reorder with move up / down or by dragging. | 已修订 |
| providerCard.section.queueEmpty | 队列是空的，从下面加入供应商。 | 대기열이 비어 있습니다. 아래에서 공급자를 추가하세요. | The queue is empty. Add providers from below. | 已修订 |
| providerCard.section.notInQueue | 不在队列（{{count}}） | 대기열에 없음({{count}}) | Not in queue ({{count}}) | 保留 |
| providerCard.section.stackDefault | 默认供应商 | 기본 공급자 | Default provider | 已修订 |
| providerCard.section.stackDefaultAfterSwitch | 切换到聚合模式后的默认供应商 | 통합 모드 전환 후 기본 공급자 | Default provider after switching to Aggregation | 已修订 |
| providerCard.section.stackDefaultHelp | 不带前缀的请求都发给它；其他已添加的供应商以 ccs- 前缀出现在 /model 里。 | 접두사가 없는 요청은 이 공급자로 보냅니다. 추가된 다른 공급자의 모델은 /model에 ccs- 접두사와 함께 표시됩니다. | Requests without a prefix go to it; other added providers appear in /model with the ccs- prefix. | 已修订 |
| providerCard.section.stackDefaultHelpDesktop | Claude Desktop 的默认模型和映射表里的模型都发给它；其他已添加的供应商以「供应商 / 模型」出现在模型列表里。 | 기본 모델과 매핑된 모델의 요청은 이 공급자로 보냅니다. 추가된 다른 공급자의 모델은 모델 목록에 ‘공급자 / 모델’로 표시됩니다. | Requests for the default model and the mapped models go to it; other added providers appear in the model list as "Provider / model". | 已修订 |
| providerCard.section.stackEmpty | 还没有添加其他供应商。 | 아직 추가된 다른 공급자가 없습니다. | No other providers added yet. | 已修订 |
| providerCard.section.added | 已添加 · {{count}} | 추가됨 · {{count}} | Added · {{count}} | 保留 |
| providerCard.section.addedHelpTitle | 已添加 | 추가됨 | Added | 保留 |
| providerCard.section.addedHelp | 已添加的供应商会同时写进 {{app}} 的配置，在 {{app}} 里选模型即可。 | 추가된 공급자는 모두 {{app}}의 설정에 함께 저장됩니다. {{app}}에서 모델을 선택하면 됩니다. | Added providers are all written into {{app}}'s config; pick the model inside {{app}}. | 已修订 |
| providerCard.section.addedEmpty | 还没有添加供应商。 | 아직 추가된 공급자가 없습니다. | No providers added yet. | 已修订 |
| providerCard.section.available | 可添加 · {{count}} | 사용 가능 · {{count}} | Available · {{count}} | 保留 |
| providerCard.section.stackNoDefault | 还没有默认供应商；切换到聚合模式时选一家。 | 기본 공급자가 없습니다. 통합 모드로 전환할 때 선택하세요. | No default provider yet. You pick one when switching to Aggregation. | 已修订 |
| routingSettings.service | 服务 | 서비스 | Service | 保留 |
| routingSettings.serviceName | 路由服务 | 라우팅 서비스 | Routing service | 保留 |
| routingSettings.serviceHelp | 路由模式和聚合模式下，请求先经过本机的路由服务再转给供应商。进入这两种模式时会自动启动。 | 라우팅 및 통합 모드에서는 요청이 이 컴퓨터의 라우팅 서비스를 거쳐 공급자로 전달됩니다. 앱이 두 모드 중 하나로 전환되면 서비스가 자동으로 시작됩니다. | In routing and Aggregation modes, requests go through the routing service on this machine before reaching the provider. It starts automatically when an app enters either mode. | 已修订 |
| routingSettings.runningFor | 运行中 · 已运行 {{uptime}} | 실행 중 · 가동 시간 {{uptime}} | Running · up {{uptime}} | 已修订 |
| routingSettings.uptimeHours | {{hours}} 小时 {{minutes}} 分 | {{hours}} h {{minutes}} 분 | {{hours}} h {{minutes}} min | 保留 |
| routingSettings.uptimeMinutes | {{minutes}} 分钟 | {{minutes}} 분 | {{minutes}} min | 保留 |
| routingSettings.stopped | 已停止 | 중지됨 | Stopped | 保留 |
| routingSettings.totalRequests | 总请求数 | 요청 수 | Requests | 已修订 |
| routingSettings.successRate | 成功率 | 성공률 | Success rate | 保留 |
| routingSettings.activeConnections | 活跃连接 | 활성 연결 | Active connections | 保留 |
| routingSettings.start | 启动 | 시작 | Start | 保留 |
| routingSettings.stop | 停止 | 중지 | Stop | 已修订 |
| routingSettings.stopBlocked | 还有应用在用路由服务，先让它们回到直连。 | 일부 앱이 아직 라우팅 서비스를 사용 중입니다. 먼저 직접 연결로 전환하세요. | Some apps still use the routing service. Switch them back to direct first. | 已修订 |
| routingSettings.listen | 监听地址与端口 | 수신 주소 및 포트 | Listen address and port | 保留 |
| routingSettings.address | 监听地址 | 수신 주소 | Listen address | 已修订 |
| routingSettings.addressHint | 推荐 127.0.0.1 | 권장: 127.0.0.1 | Recommended: 127.0.0.1 | 保留 |
| routingSettings.port | 监听端口 | 수신 포트 | Listen port | 已修订 |
| routingSettings.saveAndRestart | 保存并重启服务 | 저장 후 서비스 다시 시작 | Save and restart service | 已修订 |
| routingSettings.clientHost | 连接地址 | 연결 주소 | Connection address | 保留 |
| routingSettings.clientHostHint | 客户端连路由用的地址；留空按监听地址 | 클라이언트가 연결할 주소입니다. 비워 두면 수신 주소를 사용합니다 | Where clients connect. Empty: the listen address | 已修订 |
| routingSettings.clientHostInvalid | 请输入客户端能访问到的 IP 地址或主机名 | 클라이언트가 연결할 수 있는 IP 주소 또는 호스트 이름을 입력하세요. | Enter an IP address or hostname that clients can reach | 保留 |
| routingSettings.clientHostHelp | CC Switch 写进客户端配置的代理主机（含 Claude Desktop 的网关地址）。留空时按监听地址推导。客户端无法通过本机回环访问时填写，例如 WSL2（NAT 模式）里的 Claude Desktop 会话：把监听地址设为 0.0.0.0，在这里填 WSL 能访问到的 Windows IP（如 vEthernet (WSL) 网卡的地址），并在防火墙中放行端口。 | CC Switch가 클라이언트 설정에 저장하는 프록시 호스트 주소입니다(Claude Desktop의 게이트웨이 주소 포함). 비워 두면 수신 주소를 기준으로 결정합니다. 클라이언트가 이 컴퓨터의 루프백 주소로 연결할 수 없을 때 입력하세요. 예를 들어 WSL2(NAT 모드)의 Claude Desktop 세션에서는 수신 주소를 0.0.0.0으로 설정하고 여기에 WSL에서 접근할 수 있는 Windows IP(예: vEthernet (WSL) 어댑터 주소)를 입력한 뒤 방화벽에서 해당 포트를 허용하세요. | The host CC Switch writes into client configs (including Claude Desktop's gateway URL). Leave it empty to derive it from the listen address. Set it when clients can't reach this machine through loopback, e.g. Claude Desktop sessions inside WSL2 (NAT mode): set the listen address to 0.0.0.0 and enter a Windows IP that WSL can reach (such as the vEthernet (WSL) adapter address), and allow the port through the firewall. | 已修订 |
| routingSettings.logging | 记录请求用量 | 요청 사용량 기록 | Record request usage | 已修订 |
| routingSettings.loggingHelp | 关闭后，用量统计里没有经路由的请求明细。 | 끄면 사용량에 라우팅된 요청에 대한 요청별 세부 정보가 없습니다. | When off, Usage has no per-request details for routed requests. | 保留 |
| routingSettings.usingApps | 正在使用路由的应用 · {{count}} | 라우팅을 사용하는 앱 · {{count}} | Apps using routing · {{count}} | 保留 |
| routingSettings.noApps | 没有应用在用路由。在应用页的「路由」或「聚合」页签里进入。 | 라우팅을 사용하는 앱이 없습니다. 앱 페이지의 라우팅 또는 통합 탭에서 시작하세요. | No app is using routing. Enter it from the Routing or Aggregation tab on an app's page. | 已修订 |
| routingSettings.routeDetail | 路由到 {{name}} | {{name}}로 라우팅 | Routing to {{name}} | 保留 |
| routingSettings.stackDetail | 默认 {{name}} | 기본 {{name}} | Default {{name}} | 保留 |
| routingSettings.goTo | 前往 | 열기 | Open | 保留 |
| routingSettings.exitAll | 全部回到直连 | 모두 직접 연결로 되돌리기 | Switch all back to direct | 已修订 |
| routingSettings.exitAllTitle | 让所有应用回到直连？ | 모든 앱을 직접 연결로 되돌리시겠습니까? | Switch every app back to direct? | 已修订 |
| routingSettings.exitAllMessage | 在路由和聚合模式下的应用都会写回直连配置，然后停止路由服务。路由目标、队列和聚合名单会保留。 | 라우팅 또는 통합 모드인 모든 앱에 직접 연결 설정을 복원한 후 라우팅 서비스를 중지합니다. 라우팅 대상, 대기열 및 통합 목록은 유지됩니다. | Apps in routing or Aggregation mode get their direct config written back, then the routing service stops. Route targets, queues and aggregation lists are kept. | 已修订 |
| routingSettings.exitAllConfirm | 全部回到直连 | 모두 직접 연결로 되돌리기 | Switch all back to direct | 已修订 |
| routingSettings.failoverHelp | 这里调各应用的超时、重试和熔断。队列在各应用页的「路由」页签里管理。 | 각 앱의 시간 초과, 재시도 및 서킷 브레이커를 설정합니다. 대기열은 각 앱의 라우팅 탭에서 관리합니다. | Tune each app's timeouts, retries and circuit breaker here. Queues are managed on each app's Routing tab. | 已修订 |
| quota.tierShort | {{label}} {{value}}% | {{label}} {{value}}% | {{label}} {{value}}% | 保留 |
| quota.tierLeft | {{labelSp}}剩余 {{value}}% | {{label}} {{value}}% 남음 | {{label}} {{value}}% left | 保留 |
| quota.tierUsedUp | {{labelSp}}已用完 | {{label}}을(를) 모두 사용했습니다. | {{label}} used up | 已修订 |
| quota.tierUsed | {{labelSp}}已用 {{value}}% | {{label}} {{value}}% 사용됨 | {{label}} {{value}}% used | 保留 |
| quota.left | 剩余 {{value}}% | {{value}}% 남음 | {{value}}% left | 保留 |
| quota.used | 已用 {{value}}% | {{value}}% 사용됨 | {{value}}% used | 保留 |
| quota.usedUp | 已用完 | 소진됨 | Used up | 已修订 |
| quota.balance | 余额 {{value}} | 잔액 {{value}} | Balance {{value}} | 已修订 |
| quota.balanceUsedUp | 余额已用完 | 잔액이 소진되었습니다. | Balance used up | 保留 |
| quota.planExpired | 套餐已过期 | 요금제 만료됨 | Plan expired | 已修订 |
| quota.failed | 额度没查到 | 할당량을 확인할 수 없음 | Quota unavailable | 保留 |
| quota.reason.loginExpired | 登录已过期 | 로그인이 만료되었습니다 | Sign-in expired | 保留 |
| quota.reason.tokenRefreshPending | 令牌待刷新 | 토큰 새로고침 보류 중 | Token refresh pending | 保留 |
| quota.updatedAt | {{time}}更新 | {{time}}에 업데이트됨 | Updated {{time}} | 已修订 |
| quota.clickToRefresh | 点击重新查询 | 다시 확인하려면 클릭하세요 | Click to check again | 保留 |
| quota.resetCredits.label | 重置 | 재설정 | Resets | 保留 |
| quota.resetCredits.left | 重置剩余 {{count}} 次 | 남은 초기화 횟수: {{count}}회 | Resets left: {{count}} | 已修订 |
| quota.resetCredits.short | 重置 {{count}} 次 | 초기화 {{count}}회 | Resets {{count}} | 已修订 |
| quota.resetCredits.value | 剩余 {{count}} 次 | {{count}}회 남음 | {{count}} left | 已修订 |
| quota.resetCredits.expiresOn | {{date}}到期 | {{date}} 만료 | Expires {{date}} | 保留 |
| quota.resetCredits.noExpiry | 不会过期 | 만료 없음 | No expiry | 保留 |
| quota.resetCredits.detail | 存下的限额重置剩余 {{count}} 次 · 最早 {{date}}到期 | 저장된 한도 초기화 {{count}}회 남음 · 가장 빠른 만료일 {{date}} | Saved limit resets left: {{count}} · next expires {{date}} | 已修订 |
| quota.resetCredits.detailNoExpiry | 存下的限额重置剩余 {{count}} 次 · 不会过期 | 저장된 한도 초기화 {{count}}회 남음 · 만료 없음 | Saved limit resets left: {{count}} · no expiry | 已修订 |
| quota.resetCredits.title | 存下的限额重置 | 저장된 한도 재설정 | Saved limit resets | 保留 |
| quota.resetCredits.times | {{count}} 次 | ×{{count}} | ×{{count}} | 保留 |
| quota.resetCredits.inTime | {{time}}后 | {{time}} 후 | in {{time}} | 已修订 |
| quota.resetCredits.showAll | 查看 {{count}} 次重置各自的到期时间 | 초기화 {{count}}회의 개별 만료일 보기 | Show when each of the {{count}} resets expires | 已修订 |
| quota.credits.label | Credits | 크레딧 | Credits | 保留 |
| quota.credits.text | Credits 约 {{usd}} | 크레딧 ≒ {{usd}} | Credits ≈ {{usd}} | 保留 |
| quota.credits.usd | 约 {{usd}} | ≒ {{usd}} | ≈ {{usd}} | 保留 |
| quota.credits.detail | Credits 余额 {{balance}} · 按 API 价折算约 {{usd}} · 额度用完后才扣 | 크레딧 잔액 {{balance}} · API 요금 기준 약 {{usd}} · 할당량 소진 후에만 차감 | Credits balance {{balance}} · ≈ {{usd}} at API prices · used only after your limits run out | 已修订 |
| quota.windows.title | 各档额度 | 모든 한도 | All limits | 保留 |
| quota.windows.showAll | 查看各档额度 | 모든 한도 표시 | Show all limits | 保留 |
| appMatrix.clearSearch | 清空搜索 | 검색 지우기 | Clear search | 保留 |
| appMatrix.found | 找到 {{count}} 个 | {{count}}을(를) 찾았습니다 | {{count}} found | 已修订 |
| appMatrix.columnAria | {{app}}：已在 {{on}} / {{total}} 个 {{noun}} 上启用，批量操作 | {{app}}: {{noun}} {{total}}개 중 {{on}}개 활성화됨, 일괄 작업 | {{app}}: enabled for {{on}} of {{total}} {{noun}}, bulk actions | 已修订 |
| appMatrix.pop.count | 已在 {{on}} / {{total}} 个 {{noun}} 上启用 | {{noun}} {{total}}개 중 {{on}}개 활성화됨 | Enabled for {{on}} of {{total}} {{noun}} | 已修订 |
| appMatrix.pop.failCount | 其中 {{count}} 个写入失败 | 그중 {{count}}개 저장 실패 | {{count}} failed to write | 已修订 |
| appMatrix.pop.enableRest | 启用其余 {{count}} 个 | 다른 {{count}} 활성화 | Enable the other {{count}} | 保留 |
| appMatrix.pop.enableAll | 全部启用 | 모두 활성화 | Enable all | 保留 |
| appMatrix.pop.disableAll | 全部关闭 | 모두 끄기 | Turn all off | 保留 |
| appMatrix.pop.scopeAll | 只作用于当前列表里的 {{count}} 个 | 이 목록의 {{count}}에 적용됩니다. | Applies to the {{count}} in this list | 保留 |
| appMatrix.pop.scopeSearch | 只作用于搜索出的 {{count}} 个 | {{count}} 검색 결과에만 적용됩니다. | Applies only to the {{count}} search results | 保留 |
| appMatrix.pop.scopeFilter | 只作用于筛选出的 {{count}} 个 | 필터링된 {{count}}개 항목에만 적용됩니다 | Applies only to the {{count}} filtered items | 保留 |
| appMatrix.toast.enabled | 已在 {{app}} 启用 {{count}} 个 {{noun}} | {{app}}에서 {{count}} {{noun}}을(를) 활성화했습니다. | Enabled {{count}} {{noun}} in {{app}} | 已修订 |
| appMatrix.toast.disabled | 已在 {{app}} 关闭 {{count}} 个 {{noun}} | {{app}}에서 {{count}} {{noun}}을(를) 껐습니다. | Turned off {{count}} {{noun}} in {{app}} | 已修订 |
| appMatrix.toast.partialFail | ，其中 {{count}} 个没有写入，已在列表里标出 |  · 그중 {{count}}개를 저장하지 못해 목록에 표시했습니다. | ; {{count}} could not be written and are marked in the list | 已修订 |
| appMatrix.toast.undone | 已撤销 | 실행 취소됨 | Undone | 已修订 |
| appMatrix.undo | 撤销 | 실행 취소 | Undo | 已修订 |
| appMatrix.cell.on | {{name}} · {{app}}：已启用 | {{name}} · {{app}}: 활성화됨 | {{name}} · {{app}}: enabled | 保留 |
| appMatrix.cell.off | {{name}} · {{app}}：未启用 | {{name}} · {{app}}: 꺼짐 | {{name}} · {{app}}: off | 保留 |
| appMatrix.cell.fail | {{name}} · {{app}}：写入失败，点按重试 | {{name}} · {{app}}: 저장 실패, 클릭하여 다시 시도 | {{name}} · {{app}}: write failed, click to retry | 已修订 |
| mcpPage.noun | MCP | MCP 서버 | MCP servers | 保留 |
| mcpPage.listSeparator | 、 | ,  | ,  | 保留 |
| mcpPage.helpTitle | MCP 怎么同步 | MCP의 동기화 방법 | How MCP syncs | 保留 |
| mcpPage.help | 以这里为准：写进你勾选的应用的配置文件，切换供应商时按这里重写。Claude Desktop、OpenClaw 不支持，所以表格里没有这两列；Pi 需要 1.0 及以上，且不支持 SSE。 | 여기의 설정을 기준으로 선택한 앱의 설정 파일에 저장하며, 공급자를 전환할 때도 이 설정에 따라 다시 저장합니다. Claude Desktop과 OpenClaw는 지원되지 않아 해당 열이 없습니다. Pi는 1.0 이상이 필요하며 SSE를 지원하지 않습니다. | This list is the source of truth: it is written into the config files of the apps you tick, and rewritten from here when you switch providers. Claude Desktop and OpenClaw are not supported, so they have no column; Pi needs 1.0 or later and does not support SSE. | 已修订 |
| mcpPage.importFromApps | 从应用导入 | 앱에서 가져오기 | Import from apps | 保留 |
| mcpPage.add | 添加 MCP | MCP 추가 | Add MCP | 保留 |
| mcpPage.moreActions | MCP 的更多操作 | 더 많은 MCP 작업 | More MCP actions | 保留 |
| mcpPage.copyAll | 复制全部为 mcpServers JSON | 모두 mcpServers JSON로 복사 | Copy all as mcpServers JSON | 保留 |
| mcpPage.searchPlaceholder | 搜索名称、命令或地址 | 이름, 명령 또는 URL 검색 | Search name, command or URL | 保留 |
| mcpPage.count | {{count}} 个 MCP | {{count}} MCP 서버 | {{count}} MCP servers | 保留 |
| mcpPage.countFiltered | {{shown}} / {{count}} 个 MCP | {{count}} MCP 서버의 {{shown}} | {{shown}} of {{count}} MCP servers | 保留 |
| mcpPage.overwriteNote | 直接改应用配置里的同名项会被覆盖 | 동일한 항목에 대해 앱 설정에서 직접 수정한 내용을 덮어씁니다. | Edits made directly in app configs to the same entries get overwritten | 已修订 |
| mcpPage.failNoticeTitle | 无法写入 {{app}} 的配置 | {{app}}의 설정을 저장할 수 없습니다. | Couldn't write {{app}}'s config | 已修订 |
| mcpPage.failNoticeBody | {{error}}。修好文件后点「重试」。 | {{error}}. 파일을 수정한 후 재시도를 클릭하세요. | {{error}}. Fix the file, then click Retry. | 保留 |
| mcpPage.loadFailed | 读取 MCP 列表失败 | MCP 목록을 로드할 수 없습니다. | Couldn't load the MCP list | 保留 |
| mcpPage.noFilesChanged | CC Switch 没有改动任何文件。 | CC Switch는 파일을 변경하지 않았습니다. | CC Switch didn't change any files. | 保留 |
| mcpPage.emptyTitle | 还没有 MCP 服务器 | 아직 MCP 서버가 없습니다 | No MCP servers yet | 保留 |
| mcpPage.emptyBody | 已经在应用里配过的 MCP，可以直接导入 | 앱에 이미 설정된 MCP 서버를 가져올 수 있습니다 | MCP servers already set up in your apps can be imported | 保留 |
| mcpPage.importHelpTitle | 导入会读哪些配置 | 가져오기에서 읽는 내용 | What import reads | 保留 |
| mcpPage.importHelp | 只读用户级配置。用 claude mcp add 默认加到项目里的 MCP、插件自带的 MCP 不会导入。 | 사용자 수준 설정만 읽습니다. claude mcp add가 기본으로 프로젝트에 추가한 MCP 서버와 플러그인에 포함된 서버는 가져오지 않습니다. | Only user-level configs are read. MCP servers that claude mcp add puts in a project by default, and ones bundled with plugins, are not imported. | 保留 |
| mcpPage.columnName | 名称 | 이름 | Name | 保留 |
| mcpPage.noMatch | 没有名称、命令或地址匹配“{{query}}”的 MCP | MCP 서버의 이름, 명령 또는 URL이 "{{query}}"와 일치하지 않습니다. | No MCP server's name, command or URL matches “{{query}}” | 保留 |
| mcpPage.clearSearch | 清除搜索 | 검색 지우기 | Clear search | 保留 |
| mcpPage.listLabel | MCP 列表 | MCP 서버 | MCP servers | 保留 |
| mcpPage.notEnabled | 未启用 | 꺼짐 | Off | 保留 |
| mcpPage.rowFail | 写入 {{apps}} 失败 | {{apps}}에 저장 실패 | Writing to {{apps}} failed | 已修订 |
| mcpPage.rowRetryAria | 重新写入 {{id}} 到 {{apps}} | {{id}}을(를) {{apps}}에 다시 저장 | Write {{id}} to {{apps}} again | 已修订 |
| mcpPage.editAria | 编辑 {{id}} | {{id}} 편집 | Edit {{id}} | 保留 |
| mcpPage.rowMoreAria | {{id}} 的更多操作 | {{id}}에 대한 추가 작업 | More actions for {{id}} | 保留 |
| mcpPage.copyJson | 复制为 JSON | JSON로 복사 | Copy as JSON | 保留 |
| mcpPage.openDocs | 打开文档 | 문서 열기 | Open docs | 保留 |
| mcpPage.enableEverywhere | 在所有应用启用 | 모든 앱에서 활성화 | Enable in all apps | 保留 |
| mcpPage.disableEverywhere | 全部关闭 | 모든 앱에서 끄기 | Turn off everywhere | 已修订 |
| mcpPage.deleteEllipsis | 删除 | 삭제 | Delete | 保留 |
| mcpPage.deleteTitle | 删除 {{id}}？ | {{id}}을(를) 삭제하시겠습니까? | Delete {{id}}? | 保留 |
| mcpPage.deleteBodyApps | 会从 CC Switch 以及 {{apps}} 的配置文件里删除这一项，无法撤销。 | 이렇게 하면 CC Switch 및 {{apps}}의 설정 파일에서 제거됩니다. 이 작업은 취소할 수 없습니다. | This removes it from CC Switch and from the config files of {{apps}}. This can't be undone. | 已修订 |
| mcpPage.deleteBody | 会从 CC Switch 里删除这一项，无法撤销。 | 이렇게 하면 CC Switch에서 제거됩니다. 이 작업은 취소할 수 없습니다. | This removes it from CC Switch. This can't be undone. | 保留 |
| mcpPage.toast.written | 已写入 {{app}} | {{app}}에 저장했습니다 | Written to {{app}} | 已修订 |
| mcpPage.toast.rowAllOn | {{id}} 已在全部 {{count}} 个应用启用 | {{id}}는 모든 {{count}} 앱에서 활성화됩니다. | {{id}} is enabled in all {{count}} apps | 保留 |
| mcpPage.toast.rowAllOff | {{id}} 已在所有应用关闭 | 모든 앱에서 {{id}}가 꺼졌습니다 | {{id}} is turned off in all apps | 保留 |
| mcpPage.toast.copiedAll | 已复制 {{count}} 个 MCP 的 mcpServers JSON（含环境变量和请求头的值） | MCP 서버 {{count}}개의 mcpServers JSON을 복사했습니다 (환경 변수 및 헤더 값 포함) | Copied mcpServers JSON for {{count}} MCP servers (including env and header values) | 保留 |
| mcpPage.toast.copiedOne | 已复制 {{id}} 的 JSON（含环境变量和请求头的值） | {{id}}을(를) JSON로 복사했습니다(env 및 헤더 값 포함). | Copied {{id}} as JSON (including env and header values) | 已修订 |
| mcpPage.toast.deleted | 已删除 {{id}} | {{id}}을(를) 삭제했습니다. | Deleted {{id}} | 已修订 |
| mcpPage.toast.added | 已添加 {{id}} | {{id}}을(를) 추가했습니다. | Added {{id}} | 已修订 |
| mcpPage.toast.saved | 已保存 {{id}} | {{id}}을(를) 저장했습니다 | Saved {{id}} | 已修订 |
| mcpPage.toast.batchAdded | 已添加 {{count}} 个 MCP | {{count}} MCP 서버 추가 | Added {{count}} MCP servers | 保留 |
| mcpPage.toast.batchAddedReplaced | 已添加 {{count}} 个 MCP，覆盖 {{replaced}} 个 | {{count}} MCP 서버 추가, {{replaced}} 교체 | Added {{count}} MCP servers, replaced {{replaced}} | 保留 |
| mcpPage.toast.resynced | 已按这里的开关重新写入 {{count}} 个应用的配置 | 여기의 스위치 상태에 따라 앱 {{count}}개의 설정을 다시 저장했습니다. | Rewrote the config of {{count}} apps from these switches | 已修订 |
| mcpPage.toast.resyncPartial | {{count}} 个应用写入失败：{{apps}} | 앱 {{count}}개에 설정을 저장하지 못했습니다: {{apps}} | Couldn't write {{count}} apps: {{apps}} | 已修订 |
| mcpPage.import.title | 导入完成 | 가져오기 완료 | Import finished | 保留 |
| mcpPage.import.added | 新增 {{count}} 个 MCP：{{names}}。 | {{count}} MCP 서버 추가: {{names}}. | Added {{count}} MCP servers: {{names}}. | 保留 |
| mcpPage.import.none | 没有发现新的 MCP。 | 새로운 MCP 서버를 찾을 수 없습니다. | No new MCP servers found. | 保留 |
| mcpPage.import.sameName | 已有的同名 MCP 只打开了对应应用的开关，配置仍以 CC Switch 里的为准。 | 목록에 이미 있는 서버는 해당 앱의 스위치만 켰으며, 설정은 CC Switch에 저장된 내용을 유지합니다. | For servers already in the list, only the matching app switches were turned on; the config in CC Switch still wins. | 已修订 |
| mcpPage.import.failedTitle | 有应用没有读到 | 일부 앱을 읽을 수 없습니다 | Some apps couldn't be read | 保留 |
| mcpPage.import.filesTitle | 读取了哪些文件 | 읽은 파일 | Which files were read | 保留 |
| mcpPage.import.claudeNote | （顶层 mcpServers） |  (최상위 mcpServers) |  (top-level mcpServers) | 保留 |
| mcpPage.import.ok | 知道了 | 확인했습니다 | Got it | 已修订 |
| mcpPage.templateLabels.sequential-thinking | 顺序思考 | 순차적 사고 | sequential-thinking | 保留 |
| mcpPage.drawer.addTitle | 添加 MCP | MCP 추가 | Add MCP | 保留 |
| mcpPage.drawer.editTitle | 编辑 MCP | MCP 편집 | Edit MCP | 保留 |
| mcpPage.drawer.templates | 从模板开始 | 템플릿에서 시작 | Start from a template | 保留 |
| mcpPage.drawer.paste | 粘贴配置 | 설정 붙여넣기 | Paste a config | 已修订 |
| mcpPage.drawer.pastePlaceholder | 粘贴 JSON 或 TOML，自动识别 mcpServers、Codex、OpenCode 的写法 | JSON 또는 TOML를 붙여넣으세요. mcpServers, Codex 및 OpenCode 형식이 인식됩니다. | Paste JSON or TOML; mcpServers, Codex and OpenCode formats are recognized | 保留 |
| mcpPage.drawer.pasteOneOk | 识别为 {{format}}：{{name}}，已填入下面的表单 | 인식된 {{format}}: {{name}}, 아래 양식에 작성됨 | Recognized {{format}}: {{name}}, filled into the form below | 保留 |
| mcpPage.drawer.pasteOneNoName | 识别为{{format}}，已填入下面的表单；名称要自己填 | 아래 양식에 작성된 {{format}}가 인식되었습니다. 이름을 직접 추가하세요 | Recognized {{format}}, filled into the form below; add a name yourself | 保留 |
| mcpPage.drawer.pasteManyOk | 已识别，见下面的列表 | 인식됨; 아래 목록을 참조하세요 | Recognized; see the list below | 保留 |
| mcpPage.drawer.pasteHelp | 无法识别。支持：单个服务器对象、"名称": {…}、{"mcpServers": {…}}、Codex 的 [mcp_servers.名称]、OpenCode 的 local / remote 写法。 | 형식을 인식하지 못했습니다. 단일 서버 객체, "name": {…}, {"mcpServers": {…}}, Codex의 [mcp_servers.name], OpenCode의 local / remote 형식을 지원합니다. | Couldn't recognize this. Supported: a single server object, "name": {…}, {"mcpServers": {…}}, Codex's [mcp_servers.name], and OpenCode's local / remote format. | 已修订 |
| mcpPage.drawer.pasteFormats.mcpServers | mcpServers 格式 | mcpServers 형식 | mcpServers format | 保留 |
| mcpPage.drawer.pasteFormats.opencode | OpenCode 的写法 | OpenCode 형식 | OpenCode format | 保留 |
| mcpPage.drawer.pasteFormats.codex | Codex 的写法 | Codex 형식 | Codex format | 保留 |
| mcpPage.drawer.pasteFormats.codexToml | Codex 的 TOML 写法 | Codex TOML 형식 | Codex TOML format | 保留 |
| mcpPage.drawer.pasteFormats.single | 单个服务器配置 | 단일 서버 설정 | a single server config | 已修订 |
| mcpPage.drawer.pasteFormats.named | "名称": {…} 写法 | "name": {…} 형식 | "name": {…} format | 保留 |
| mcpPage.drawer.batchTitle | 识别到 {{count}} 个服务器（{{format}}） | 서버 {{count}}개 발견 ({{format}}) | Found {{count}} servers ({{format}}) | 保留 |
| mcpPage.drawer.batchClear | 清空，改为逐个添加 | 비우고 하나씩 추가 | Clear and add one at a time | 已修订 |
| mcpPage.drawer.batchNew | 新的 | 신규 | New | 已修订 |
| mcpPage.drawer.batchExists | 已存在同名 | 이름이 이미 존재합니다. | Name already exists | 保留 |
| mcpPage.drawer.batchExistsGroup | {{name}} 已存在同名：跳过还是覆盖 | {{name}}가 이미 존재합니다. 건너뛰거나 교체하세요. | {{name}} already exists: skip or replace | 保留 |
| mcpPage.drawer.batchSkip | 跳过 | 건너뛰기 | Skip | 已修订 |
| mcpPage.drawer.batchOverwrite | 覆盖 | 덮어쓰기 | Replace | 已修订 |
| mcpPage.drawer.batchNone | 至少勾选一个服务器 | 서버를 하나 이상 선택하세요. | Select at least one server | 保留 |
| mcpPage.drawer.addMany | 添加 {{count}} 个 | {{count}} 추가 | Add {{count}} | 保留 |
| mcpPage.drawer.addManyReplace | 添加 {{count}} 个，覆盖 {{replaced}} 个 | {{count}} 추가, {{replaced}} 교체 | Add {{count}}, replace {{replaced}} | 保留 |
| mcpPage.drawer.name | 名称 | 이름 | Name | 保留 |
| mcpPage.drawer.required | （必填） | (필수) | (required) | 已修订 |
| mcpPage.drawer.namePlaceholder | 例如 context7 | 예: context7 | e.g. context7 | 已修订 |
| mcpPage.drawer.nameHelpTitle | 名称是什么 | 이름이 뭐예요? | What the name is | 保留 |
| mcpPage.drawer.nameHelp | 写进各应用配置文件里的键名。 | 각 앱의 설정 파일에 저장되는 키 이름입니다. | The key written into each app's config file. | 已修订 |
| mcpPage.drawer.nameHelpEditTitle | 为什么不能改名 | 이름을 변경할 수 없는 이유 | Why the name can't change | 保留 |
| mcpPage.drawer.nameHelpEdit | 名称是各应用配置里的键。要改名，新建一个再删除旧的。 | 이름은 각 앱 설정의 키로 사용됩니다. 이름을 바꾸려면 새 항목을 만들고 기존 항목을 삭제하세요. | The name is the key in each app's config. To rename, create a new one and delete the old one. | 保留 |
| mcpPage.drawer.errors.nameRequired | 填写名称，例如 context7 | 이름을 입력하세요 (예: context7) | Enter a name, e.g. context7 | 已修订 |
| mcpPage.drawer.errors.nameSpaces | 名称里不能有空格，可以用 - 或 _ 连接 | 이름에는 공백을 사용할 수 없습니다. - 또는 _를 사용하세요 | Names can't contain spaces; use - or _ | 已修订 |
| mcpPage.drawer.errors.nameExists | 已经有一个叫 {{name}} 的 MCP | {{name}}라는 MCP 서버가 이미 존재합니다. | An MCP server named {{name}} already exists | 保留 |
| mcpPage.drawer.errors.commandRequired | 填写要运行的命令，例如 npx 或 uvx | 실행할 명령을 입력하세요 (예: npx 또는 uvx) | Enter the command to run, e.g. npx or uvx | 保留 |
| mcpPage.drawer.errors.urlRequired | 填写服务器地址，例如 https://mcp.example.com/mcp | 서버 URL을 입력하세요. https://mcp.example.com/mcp | Enter the server URL, e.g. https://mcp.example.com/mcp | 保留 |
| mcpPage.drawer.errors.urlScheme | 地址要以 http:// 或 https:// 开头 | URL은 http:// 또는 https://로 시작해야 합니다. | The URL must start with http:// or https:// | 保留 |
| mcpPage.drawer.connection | 连接配置 | 연결 | Connection | 保留 |
| mcpPage.drawer.editMode | 编辑方式 | 편집 방식 | Edit as | 保留 |
| mcpPage.drawer.tabForm | 表单 | 양식 | Form | 保留 |
| mcpPage.drawer.transport | 连接方式 | 전송 방식 | Transport | 保留 |
| mcpPage.drawer.transportStdio | 本地命令（stdio） | 로컬 명령(stdio) | Local command (stdio) | 保留 |
| mcpPage.drawer.command | 命令 | 명령 | Command | 保留 |
| mcpPage.drawer.commandPlaceholder | 只写程序，例如 npx 或 uvx；参数写在下面 | 프로그램 이름만 입력하세요 (예: npx 또는 uvx). 인수는 아래에 입력합니다 | Just the program, e.g. npx or uvx; arguments go below | 保留 |
| mcpPage.drawer.args | 参数 | 인수 | Arguments | 保留 |
| mcpPage.drawer.argAria | 参数 {{index}} | 인수 {{index}} | Argument {{index}} | 保留 |
| mcpPage.drawer.removeArg | 删除参数 {{index}} | 인수 {{index}} 제거 | Remove argument {{index}} | 保留 |
| mcpPage.drawer.addArg | 添加参数 | 인수 추가 | Add argument | 保留 |
| mcpPage.drawer.env | 环境变量 | 환경 변수 | Environment variables | 保留 |
| mcpPage.drawer.headers | 请求头 | 헤더 | Headers | 保留 |
| mcpPage.drawer.addEnv | 添加环境变量 | 변수 추가 | Add variable | 保留 |
| mcpPage.drawer.addHeader | 添加请求头 | 헤더 추가 | Add header | 保留 |
| mcpPage.drawer.kvKeyPlaceholder | 名称 | 이름 | Name | 保留 |
| mcpPage.drawer.kvValuePlaceholder | 值 | 값 | Value | 保留 |
| mcpPage.drawer.kvKeyAria | {{label}} {{index}} 的名称 | {{label}} {{index}} 이름 | {{label}} {{index}} name | 保留 |
| mcpPage.drawer.kvValueAria | {{label}} {{index}} 的值 | {{label}} {{index}} 값 | {{label}} {{index}} value | 保留 |
| mcpPage.drawer.revealValue | 显示 {{name}} 的值 | {{name}}의 값을 표시합니다. | Show the value of {{name}} | 保留 |
| mcpPage.drawer.showValueTip | 显示值 | 값 표시 | Show value | 保留 |
| mcpPage.drawer.hideValueTip | 隐藏值 | 값 숨기기 | Hide value | 保留 |
| mcpPage.drawer.removeRow | 删除{{label}} {{name}} | {{label}} {{name}} 제거 | Remove {{label}} {{name}} | 保留 |
| mcpPage.drawer.cwd | 工作目录 | 작업 디렉토리 | Working directory | 保留 |
| mcpPage.drawer.optional | 可选 | 선택 사항 | Optional | 保留 |
| mcpPage.drawer.cwdPlaceholder | 留空时由应用决定 | 앱이 결정하도록 하려면 비워두세요. | Leave empty to let the app decide | 保留 |
| mcpPage.drawer.extraFields | 原样保留的字段（{{count}}） | 필드를 그대로 유지함({{count}}) | Fields kept as-is ({{count}}) | 保留 |
| mcpPage.drawer.editInJson | 在 JSON 中编辑 | JSON에서 편집 | Edit in JSON | 保留 |
| mcpPage.drawer.jsonLabel | 服务器配置 | 서버 설정 | Server config | 已修订 |
| mcpPage.drawer.jsonHelpTitle | JSON 和表单的关系 | JSON과 양식 | JSON and the form | 保留 |
| mcpPage.drawer.jsonHelp | 两边是同一份配置，切换时自动同步。环境变量和请求头的值显示为 ••••••••，保存时保留原值。 | 둘 다 동일한 설정을 편집하고 동기화를 유지합니다. Env 및 헤더 값은 다음과 같이 표시됩니다. ••••••••; 저장하면 실제 값이 유지됩니다. | Both edit the same config and stay in sync. Env and header values show as ••••••••; the real values are kept when you save. | 已修订 |
| mcpPage.drawer.showValues | 显示值 | 값 표시 | Show values | 保留 |
| mcpPage.drawer.jsonSyntax | 有语法错误 | 구문 오류가 있습니다 | There is a syntax error | 保留 |
| mcpPage.drawer.jsonSyntaxLine | 第 {{line}} 行附近有语法错误 | {{line}}줄 근처에 구문 오류가 있습니다 | Syntax error near line {{line}} | 保留 |
| mcpPage.drawer.jsonNotObject | 最外层要是一个对象，例如 {"command": "npx"} | 최상위 값은 객체여야 합니다. 예: {"command": "npx"} | The top level must be an object, e.g. {"command": "npx"} | 已修订 |
| mcpPage.drawer.jsonBlocksForm | 修好后才能切回表单。 | 오류를 수정하면 양식으로 돌아갈 수 있습니다. | Fix it to switch back to the form. | 保留 |
| mcpPage.drawer.jsonMaskedUnknown | 「{{key}}」的值还是占位符，但草稿里没有这个键的原值：填入真实值，或先点「显示值」再改键名。 | "{{key}}"에 자리표시자가 남아 있지만 초안에 해당 키의 원래 값이 없습니다. 실제 값을 입력하거나 키 이름을 변경하기 전에 "값 표시"를 켜세요. | "{{key}}" still holds the placeholder, but the draft has no original value for that key. Enter the real value, or turn on "Show values" before renaming keys. | 保留 |
| mcpPage.drawer.writeTo | 写入到 | 저장 대상 | Write to | 已修订 |
| mcpPage.drawer.writeToHelpTitle | 怎么写进各应用 | 각 앱에 저장되는 방식 | How it's written to apps | 已修订 |
| mcpPage.drawer.writeToHelp | 同一份配置原样写进勾选的每个应用；某个应用要不同参数时，另建一条只勾它。MiniMax Code 只替换连接字段，mcp.json 里的其他字段保留。 | 같은 설정을 선택한 모든 앱에 그대로 저장합니다. 특정 앱에 다른 매개변수가 필요하면 별도 항목을 만들고 해당 앱만 선택하세요. MiniMax Code에서는 연결 필드만 교체하며 mcp.json의 나머지 필드는 유지합니다. | The same config is written as-is to every ticked app; if one app needs different arguments, create a separate entry for it. MiniMax Code only replaces the connection fields; other fields in mcp.json are kept. | 已修订 |
| mcpPage.drawer.meta | 说明与链接 | 설명 및 링크 | Description & links | 保留 |
| mcpPage.drawer.metaHint | 显示名、描述、标签、主页、文档 | 표시 이름, 설명, 태그, 홈페이지, 문서 | Display name, description, tags, homepage, docs | 保留 |
| mcpPage.drawer.displayName | 显示名 | 표시 이름 | Display name | 保留 |
| mcpPage.drawer.displayNameHelpTitle | 显示名用在哪 | 표시 이름이 표시되는 위치 | Where the display name shows | 保留 |
| mcpPage.drawer.displayNameHelp | 只在 CC Switch 里显示，不写进应用的配置。 | CC Switch에만 표시되며 앱 설정에는 저장하지 않습니다. | Only shown in CC Switch; not written to app configs. | 已修订 |
| mcpPage.drawer.description | 描述 | 설명 | Description | 保留 |
| mcpPage.drawer.tags | 标签 | 태그 | Tags | 保留 |
| mcpPage.drawer.tagsPlaceholder | 用逗号分隔，例如 docs, web | 쉼표로 구분 (예: docs, web) | Comma-separated, e.g. docs, web | 已修订 |
| mcpPage.drawer.homepage | 主页 | 홈페이지 | Homepage | 保留 |
| mcpPage.drawer.docs | 文档 | 문서 | Docs | 保留 |
| mcpPage.resync | 按这里的开关重写各应用配置 | 이 스위치 상태에 따라 모든 앱의 설정 다시 쓰기 | Rewrite every app's config from these switches | 保留 |
| skillsPage.noun | Skill | Skills | Skills | 保留 |
| skillsPage.helpTitle | Skills 怎么同步 | Skills 동기화 방식 | How Skills sync | 保留 |
| skillsPage.help | 主副本放在 CC Switch 的目录里，再同步到你勾选的应用。Claude Desktop、OpenClaw 不支持 Skills，所以表格里没有这两列。 | 원본은 CC Switch 폴더에 저장되며 선택한 앱에 동기화됩니다. Claude Desktop과 OpenClaw는 Skills를 지원하지 않아 해당 열이 없습니다. | The main copy lives in CC Switch's folder and is synced to the apps you tick. Claude Desktop and OpenClaw don't support Skills, so they have no column. | 保留 |
| skillsPage.add | 添加 Skill | Skill 추가 | Add Skill | 保留 |
| skillsPage.addMenu.discover | 在发现里浏览 | 탐색에서 찾아보기 | Browse in Discover | 已修订 |
| skillsPage.addMenu.zip | 从 ZIP 安装 | ZIP에서 설치 | Install from ZIP | 保留 |
| skillsPage.addMenu.import | 导入本机已有 | 이 컴퓨터에서 가져오기 | Import from this computer | 保留 |
| skillsPage.moreMenu.restore | 从备份恢复 | 백업에서 복원 | Restore from backup | 保留 |
| skillsPage.moreMenu.repos | 仓库管理 | 저장소 관리 | Manage repositories | 保留 |
| skillsPage.viewAria | Skills 视图 | Skills 보기 | Skills view | 保留 |
| skillsPage.viewInstalled | 已安装 | 설치됨 | Installed | 保留 |
| skillsPage.viewInstalledCount | 已安装 {{count}} | {{count}}개 설치됨 | Installed {{count}} | 保留 |
| skillsPage.viewDiscover | 发现 | 탐색 | Discover | 保留 |
| skillsPage.searchPlaceholder | 搜索名称、目录、描述或仓库 | 이름, 폴더, 설명 또는 저장소 검색 | Search name, folder, description or repo | 保留 |
| skillsPage.lastChecked | 上次检查：{{when}} | 마지막 확인: {{when}} | Last checked: {{when}} | 保留 |
| skillsPage.justNow | 刚刚 | 방금 | just now | 保留 |
| skillsPage.banner.unmanaged | 本机有 {{count}} 个 Skill 不在 CC Switch 管理中。 | 이 컴퓨터의 Skills {{count}}개는 CC Switch에서 관리하지 않습니다. | {{count}} Skills on this computer aren't managed by CC Switch. | 保留 |
| skillsPage.banner.reviewImport | 查看并导入 | 검토 후 가져오기 | Review and import | 保留 |
| skillsPage.banner.ignore | 忽略 | 무시 | Ignore | 保留 |
| skillsPage.banner.close | 关闭提示 | 닫기 | Dismiss | 保留 |
| skillsPage.filter.all | 全部 | 모두 | All | 保留 |
| skillsPage.filter.updates | 可更新 | 업데이트 있음 | Has updates | 保留 |
| skillsPage.filter.none | 未在任何应用启用 | 활성화된 앱 없음 | Not enabled anywhere | 保留 |
| skillsPage.filter.inApp | 在 {{app}} 启用 | {{app}}에서 활성화됨 | Enabled in {{app}} | 保留 |
| skillsPage.filter.sourceButton | 来源：{{source}} | 출처: {{source}} | Source: {{source}} | 保留 |
| skillsPage.source.local | 本地 | 로컬 | Local | 已修订 |
| skillsPage.bulk.selected | 已选 {{count}} | {{count}}개 선택됨 | {{count}} selected | 保留 |
| skillsPage.bulk.enableTo | 启用到 | 활성화할 앱 | Enable in | 保留 |
| skillsPage.bulk.enableToAria | 把选中的 {{count}} 个 Skill 启用到 | 선택한 Skills {{count}}개를 활성화할 앱 | Enable the {{count}} selected Skills in | 保留 |
| skillsPage.bulk.disable | 停用 | 비활성화할 앱 | Turn off in | 保留 |
| skillsPage.bulk.disableAria | 在这个应用里停用选中的 {{count}} 个 Skill | 선택한 Skills {{count}}개를 비활성화할 앱 | Turn off the {{count}} selected Skills in | 保留 |
| skillsPage.bulk.uninstall | 卸载 | 제거 | Uninstall | 保留 |
| skillsPage.piColumnTitle | Pi 按 ~/.pi/agent/skills 里有没有这个目录来判断 | Pi는 ~/.pi/agent/skills에 폴더가 있으면 해당 Skill이 활성화된 것으로 간주합니다 | Pi counts a Skill as enabled when its folder exists in ~/.pi/agent/skills | 保留 |
| skillsPage.piHelpTitle | Pi 怎么算启用 | Pi의 활성화 판단 기준 | How Pi counts as enabled | 保留 |
| skillsPage.piHelp | 看 ~/.pi/agent/skills 里有没有这个目录。 | ~/.pi/agent/skills에 폴더가 있는지 여부입니다. | Whether the folder exists in ~/.pi/agent/skills. | 保留 |
| skillsPage.pop.onlyApp | 只看在 {{app}} 启用的 | {{app}}에서 활성화된 항목만 표시 | Show only ones enabled in {{app}} | 保留 |
| skillsPage.pop.showAll | 显示全部 Skill | 모든 Skills 표시 | Show all Skills | 保留 |
| skillsPage.selectAria | 选择 {{name}} | {{name}} 선택 | Select {{name}} | 保留 |
| skillsPage.selectAllAria | 全选当前列表 | 표시된 항목 모두 선택 | Select all shown | 保留 |
| skillsPage.rowFail | 在 {{app}} 启用失败：{{error}} | {{app}}에서 활성화 실패: {{error}} | Enabling in {{app}} failed: {{error}} | 保留 |
| skillsPage.fixSync | 改同步方式 | 동기화 방식 변경 | Change sync method | 保留 |
| skillsPage.rowMoreAria | {{name}} 的更多操作 | {{name}}에 대한 추가 작업 | More actions for {{name}} | 保留 |
| skillsPage.copyDir | 复制目录名 | 폴더 이름 복사 | Copy folder name | 保留 |
| skillsPage.uninstallEllipsis | 卸载 | 제거 | Uninstall | 保留 |
| skillsPage.listLabel | 已安装的 Skill | 설치된 Skills | Installed Skills | 保留 |
| skillsPage.noMatch | 没有匹配“{{query}}”的 Skill | “{{query}}”와 일치하는 Skills가 없습니다 | No Skills match “{{query}}” | 保留 |
| skillsPage.noFilterMatch | 没有符合筛选条件的 Skill | 필터에 맞는 Skills가 없습니다 | No Skills match the filters | 保留 |
| skillsPage.searchInDiscover | 在发现里搜索“{{query}}” | 탐색에서 “{{query}}” 검색 | Search Discover for “{{query}}” | 保留 |
| skillsPage.clearFilters | 清除筛选 | 필터 초기화 | Clear filters | 保留 |
| skillsPage.loadFailed | 读取已安装的 Skill 失败 | 설치된 Skills를 불러올 수 없습니다 | Couldn't load installed Skills | 保留 |
| skillsPage.emptyTitle | 还没有 Skill | 아직 Skills가 없습니다 | No Skills yet | 保留 |
| skillsPage.emptyBody | 从发现里安装，或者导入本机已有的 Skill。 | 탐색에서 설치하거나 이 컴퓨터에 이미 있는 Skills를 가져오세요. | Install one from Discover, or import Skills already on this computer. | 保留 |
| skillsPage.goDiscover | 去发现 | 탐색으로 이동 | Go to Discover | 保留 |
| skillsPage.importCount | 导入本机已有（{{count}}） | 이 컴퓨터에서 가져오기 ({{count}}개) | Import from this computer ({{count}}) | 保留 |
| skillsPage.confirm.uninstallOne | 卸载 {{name}}？ | {{name}}을(를) 제거하시겠습니까? | Uninstall {{name}}? | 保留 |
| skillsPage.confirm.uninstallMany | 卸载 {{count}} 个 Skill？ | Skills {{count}}개를 제거하시겠습니까? | Uninstall {{count}} Skills? | 保留 |
| skillsPage.confirm.uninstallBody | 会从所有应用中移除，并删除 CC Switch 里的主副本。卸载前会自动备份到 {{path}}。 | 모든 앱에서 제거되고 CC Switch의 원본도 삭제됩니다. 먼저 {{path}}에 백업을 저장합니다. | It's removed from every app and the main copy in CC Switch is deleted. A backup is saved to {{path}} first. | 保留 |
| skillsPage.confirm.uninstallManyButton | 卸载 {{count}} 个 | {{count}}개 제거 | Uninstall {{count}} | 保留 |
| skillsPage.confirm.updateAll | 更新 {{count}} 个 Skill？ | Skills {{count}}개를 업데이트하시겠습니까? | Update {{count}} Skills? | 保留 |
| skillsPage.confirm.updateBody | 更新会用仓库里的内容替换本地目录。本地改过的地方只保留在备份里（{{path}}）。 | 업데이트하면 로컬 폴더가 저장소의 내용으로 교체됩니다. 로컬 수정 사항은 백업({{path}})에만 보관됩니다. | Updating replaces the local folder with the repository's content. Local edits are kept only in the backup ({{path}}). | 保留 |
| skillsPage.confirm.updateAllButton | 更新 {{count}} 个 | {{count}}개 업데이트 | Update {{count}} | 保留 |
| skillsPage.confirm.updateListAria | 将要更新的 Skill | 업데이트할 Skills | Skills to update | 保留 |
| skillsPage.toast.installed | 已安装 {{name}}，并在 {{apps}} 启用 | {{name}}을(를) 설치하고 {{apps}}에서 활성화했습니다 | Installed {{name}} and enabled it in {{apps}} | 保留 |
| skillsPage.toast.installedMany | 已安装 {{count}} 个 Skill，并在 {{apps}} 启用 | Skills {{count}}개를 설치하고 {{apps}}에서 활성화했습니다 | Installed {{count}} Skills and enabled them in {{apps}} | 保留 |
| skillsPage.toast.enableFailed | 没能在 {{apps}} 启用，已在列表里标出 | {{apps}}에서 활성화하지 못했습니다. 목록에 표시했습니다 | Couldn't enable in {{apps}}; marked in the list | 保留 |
| skillsPage.toast.uninstalledMany | 已卸载 {{count}} 个 Skill | Skills {{count}}개를 제거했습니다 | Uninstalled {{count}} Skills | 保留 |
| skillsPage.toast.backupAt | 备份在 {{path}} | {{path}}에 백업했습니다 | Backed up to {{path}} | 保留 |
| skillsPage.toast.copiedDir | 已复制目录名 {{dir}} | 폴더 이름 {{dir}}을(를) 복사했습니다 | Copied folder name {{dir}} | 保留 |
| skillsPage.toast.noUpdatesInSelection | 选中的 Skill 没有可用的更新 | 선택한 Skills에 업데이트가 없습니다 | None of the selected Skills have updates | 保留 |
| skillsPage.toast.selectionAlreadyOn | 选中的 {{count}} 个 Skill 已经在 {{app}} 启用 | 선택한 Skills {{count}}개가 이미 {{app}}에서 활성화되어 있습니다 | The {{count}} selected Skills are already enabled in {{app}} | 保留 |
| skillsPage.toast.selectionAlreadyOff | 选中的 {{count}} 个 Skill 都没有在 {{app}} 启用 | 선택한 Skills {{count}}개 중 {{app}}에서 활성화된 항목이 없습니다 | None of the {{count}} selected Skills are enabled in {{app}} | 保留 |
| skillsPage.toast.disabledSelection | 已在 {{app}} 停用 {{count}} 个 {{noun}} | {{app}}에서 {{count}} {{noun}}을(를) 껐습니다. | Turned off {{count}} {{noun}} in {{app}} | 已修订 |
| skillsPage.installTo.prefix | 安装到： | 설치 대상:  | Install to:  | 保留 |
| skillsPage.installTo.button | 安装到：{{apps}} | 설치 대상: {{apps}} | Install to: {{apps}} | 保留 |
| skillsPage.installTo.many | {{first}} 等 {{count}} 个 | {{first}} 등 {{count}}개 | {{first}} and {{count}} more | 已修订 |
| skillsPage.installTo.title | 安装后在这些应用里启用 | 설치 후 다음 앱에서 활성화 | Enable in these apps after installing | 保留 |
| skillsPage.installTo.helpTitle | 选好的应用会记住吗 | 이 선택이 저장되나요? | Is this remembered? | 保留 |
| skillsPage.installTo.help | 会，默认用你上次的选择。装好后也能在「已安装」里随时调整。从 ZIP 安装和从备份恢复也用这里的选择。 | 예. 마지막 선택이 기본값으로 저장됩니다. 설치됨 화면에서 언제든지 바꿀 수 있습니다. ZIP에서 설치하거나 백업에서 복원할 때도 이 선택을 사용합니다. | Yes, your last choice is the default. You can change it any time under Installed. Installing from ZIP and restoring from backup use this choice too. | 保留 |
| skillsPage.discover.searchPlaceholder | 搜索 Skill 或仓库 | Skills 또는 저장소 검색 | Search Skills or repos | 保留 |
| skillsPage.discover.searchAria | 搜索发现里的 Skill | 탐색 검색 | Search Discover | 保留 |
| skillsPage.discover.skillsShPlaceholder | 至少 2 个字，回车搜索 | 2자 이상 입력한 후 Enter를 누르세요 | At least 2 characters, press Enter | 保留 |
| skillsPage.discover.skillsShAria | 在 skills.sh 搜索 | skills.sh 검색 | Search skills.sh | 保留 |
| skillsPage.discover.skillsShHint | 在上面输入至少 2 个字，按回车搜索 skills.sh。 | 위에 2자 이상 입력하고 Enter를 눌러 skills.sh를 검색하세요. | Type at least 2 characters above and press Enter to search skills.sh. | 保留 |
| skillsPage.discover.skillsShNone | skills.sh 上没有找到“{{query}}” | skills.sh에서 “{{query}}”에 대한 결과가 없습니다 | Nothing found on skills.sh for “{{query}}” | 保留 |
| skillsPage.discover.sourceAria | 发现来源 | 탐색 출처 | Discover source | 保留 |
| skillsPage.discover.sourceRepos | 仓库 · {{count}} | 저장소 · {{count}}개 | Repos · {{count}} | 保留 |
| skillsPage.discover.reload | 重新读取仓库 | 저장소 다시 불러오기 | Reload repositories | 保留 |
| skillsPage.discover.listLabel | 可安装的 Skill | 설치 가능한 Skills | Skills you can install | 保留 |
| skillsPage.discover.installed | 已安装 · {{count}} 个应用 | 설치됨 · 앱 {{count}}개 | Installed · {{count}} apps | 保留 |
| skillsPage.discover.installedAria | {{name}} 已安装在 {{count}} 个应用，在「已安装」里查看 | {{name}}이(가) 앱 {{count}}개에 설치되어 있습니다. 설치됨 화면에서 확인하세요 | {{name}} is installed in {{count}} apps; view it under Installed | 保留 |
| skillsPage.discover.dirTaken | 目录名已被 {{name}}（{{source}}）使用 | {{name}}({{source}})에서 이 폴더 이름을 사용 중입니다 | Folder name is used by {{name}} ({{source}}) | 保留 |
| skillsPage.discover.installing | 安装中 | 설치 중 | Installing | 保留 |
| skillsPage.discover.installingAria | 正在安装 {{name}} | {{name}} 설치 중 | Installing {{name}} | 保留 |
| skillsPage.discover.installAria | 安装 {{name}} | {{name}} 설치 | Install {{name}} | 保留 |
| skillsPage.discover.retryAria | 重新安装 {{name}} | {{name}} 다시 설치 | Install {{name}} again | 保留 |
| skillsPage.discover.installFailed | 安装失败：{{reason}} | 설치 실패: {{reason}} | Install failed: {{reason}} | 保留 |
| skillsPage.discover.loadFailed | 仓库读取失败 | 저장소를 읽을 수 없습니다 | Couldn't read repositories | 保留 |
| skillsPage.discover.noneRead | 这些仓库里没有读到 Skill | 이 저장소에서 읽어 온 Skills가 없습니다 | No Skills were read from these repositories | 保留 |
| skillsPage.discover.noneReadBody | {{count}} 个仓库都没有读到 Skill，可能是网络问题或 GitHub 限制了访问。 | 저장소 {{count}}개 모두에서 Skills를 가져오지 못했습니다. 네트워크 문제 또는 GitHub 요청 제한일 수 있습니다. | None of the {{count}} repositories returned Skills. It may be a network problem or GitHub rate limiting. | 保留 |
| skillsPage.discover.manageRepos | 管理仓库 | 저장소 관리 | Manage repositories | 保留 |
| skillsPage.discover.allInstalled | 这些仓库里的 Skill 都已安装 | 이 저장소의 모든 Skill이 설치되어 있습니다 | Every Skill in these repositories is installed | 保留 |
| skillsPage.discover.showAll | 显示全部 | 모두 표시 | Show all | 保留 |
| skillsPage.discover.onlyUninstalled | 只看未安装 | 미설치 항목만 | Not installed only | 保留 |
| skillsPage.repos.buttonAll | 仓库：全部 | 저장소: 전체 | Repos: all | 保留 |
| skillsPage.repos.buttonSome | 仓库：{{count}} / {{total}} | 저장소: {{total}}개 중 {{count}}개 | Repos: {{count}} of {{total}} | 保留 |
| skillsPage.repos.popoverAria | 参与发现的仓库 | 탐색에 사용하는 저장소 | Repositories used by Discover | 保留 |
| skillsPage.repos.enableAria | 在发现里使用 {{repo}} | 탐색에서 {{repo}} 사용 | Use {{repo}} in Discover | 保留 |
| skillsPage.repos.disabledShort | 停用 | 꺼짐 | Off | 保留 |
| skillsPage.repos.disabled | 已停用，不参与发现 | 꺼짐, 탐색에 사용하지 않음 | Turned off, not used by Discover | 保留 |
| skillsPage.repos.manage | 添加或管理仓库 | 저장소 추가 또는 관리 | Add or manage repositories | 保留 |
| skillsPage.repos.openAria | 在 GitHub 打开 {{repo}} | GitHub에서 {{repo}} 열기 | Open {{repo}} on GitHub | 保留 |
| skillsPage.repos.removeAria | 删除仓库 {{repo}} | 저장소 {{repo}} 제거 | Remove repository {{repo}} | 保留 |
| skillsPage.repos.readFailed | 读取失败 | 읽기 실패 | Read failed | 保留 |
| skillsPage.import.title | 导入本机已有的 Skill | 이 컴퓨터에서 Skills 가져오기 | Import Skills from this computer | 保留 |
| skillsPage.import.helpTitle | 哪些算本机已有 | 이 컴퓨터에 이미 있는 항목의 기준 | What counts as already on this computer | 保留 |
| skillsPage.import.help | 有 SKILL.md、但还不归 CC Switch 管理的目录。 | SKILL.md가 있지만 아직 CC Switch에서 관리하지 않는 폴더입니다. | Folders that contain a SKILL.md but aren't managed by CC Switch yet. | 保留 |
| skillsPage.import.lead | 导入会复制一份到 CC Switch 的目录，原来的文件不动。 | 가져오면 CC Switch 폴더에 복사되며 원래 파일은 그대로 유지됩니다. | Importing copies them into CC Switch's folder; the original files stay as they are. | 保留 |
| skillsPage.import.searchPlaceholder | 搜索名称或位置 | 이름 또는 위치 검색 | Search name or location | 保留 |
| skillsPage.import.searchAria | 搜索要导入的 Skill | 가져올 Skills 검색 | Search Skills to import | 保留 |
| skillsPage.import.selectAll | 全选 | 모두 선택 | Select all | 保留 |
| skillsPage.import.selectNone | 全不选 | 모두 선택 해제 | Select none | 已修订 |
| skillsPage.import.foundIn | 发现于：{{places}} | 발견 위치: {{places}} | Found in: {{places}} | 保留 |
| skillsPage.import.foundCcSwitch | CC Switch 目录 | CC Switch 폴더 | CC Switch folder | 保留 |
| skillsPage.import.appsTitle | 导入后在这些应用里启用 | 가져온 후 다음 앱에서 활성화 | Enable in these apps after importing | 保留 |
| skillsPage.import.appsHelpTitle | 默认勾选哪些应用 | 기본으로 선택되는 앱 | Which apps are ticked by default | 保留 |
| skillsPage.import.appsHelp | 默认勾选「发现于」里的应用，只在发现它的应用里启用；另外勾选的应用，所有导入的 Skill 都会启用。Pi 按目录判断，不在这里选。 | “발견 위치”에 있는 앱은 기본으로 선택되며 그 위치에서 발견한 Skills만 활성화합니다. 추가로 선택한 앱에서는 가져온 모든 Skill을 활성화합니다. Pi는 폴더로 판단하므로 목록에 표시되지 않습니다. | Apps listed under “Found in” are ticked and only enable the Skills found there; any other app you tick enables every imported Skill. Pi is decided by its folder, so it isn't listed. | 保留 |
| skillsPage.import.submit | 导入 {{count}} 个 | {{count}}개 가져오기 | Import {{count}} | 保留 |
| skillsPage.restore.lead | 选一个备份，把文件恢复到本地并重新加入列表，并在 {{apps}} 启用（「发现」里的「安装到」决定）。 | 복원할 백업을 선택하면 파일을 복원하고 목록에 다시 추가하며 {{apps}}에서 활성화합니다 (탐색의 “설치 대상” 설정 사용). | Pick a backup to restore its files and add it back to the list, enabled in {{apps}} (set by “Install to” in Discover). | 保留 |
| skillsPage.repoFail.title | {{count}} 个仓库没有读到：{{repos}} | 저장소 {{count}}개를 읽지 못했습니다: {{repos}} | Couldn't read {{count}} repositories: {{repos}} | 保留 |
| skillsPage.repoFail.item | {{repo}}（{{reason}}） | {{repo}} ({{reason}}) | {{repo}} ({{reason}}) | 保留 |
| skillsPage.repoFail.discoverBody | 列表可能不完整。 | 목록이 완전하지 않을 수 있습니다. | The list may be incomplete. | 保留 |
| skillsPage.repoFail.updatesBody | 这些仓库里的 Skill 没有检查，更新结果可能不完整。 | 이 저장소의 Skills는 확인하지 못했으므로 결과가 완전하지 않을 수 있습니다. | Skills from these repositories weren't checked, so the results may be incomplete. | 保留 |
| skillsPage.headerUpdates | {{count}} 个可更新 | 업데이트 {{count}}개 | {{count}} updates | 保留 |
| skillsPage.headerUpdatesShow | 只看可更新的 Skill | 업데이트가 있는 Skills만 표시 | Show only Skills with updates | 保留 |
| skillsPage.headerUpdatesClear | 显示全部 Skill | 모든 Skills 표시 | Show all Skills | 保留 |
| skillsPage.updateAllCount | 全部更新（{{count}} 个） | 모두 업데이트 ({{count}}개) | Update all ({{count}}) | 保留 |
| skillsPage.updatingProgress | 正在更新 {{done}}/{{total}}… | 업데이트 중 {{done}}/{{total}}… | Updating {{done}}/{{total}}… | 保留 |
| newLayoutNotice.title | 界面改版了 | CC Switch의 디자인이 새로워졌습니다 | CC Switch has a new look | 保留 |
| newLayoutNotice.body | CC Switch 这一版重新设计了界面，常用功能的位置有变化：<br>• 模式移到了每个应用页的顶部<br>• 用量统计和授权中心移到了左侧边栏<br>想了解全部变化，可以看看这一版的更新说明。 | 이번 버전에서 CC Switch의 인터페이스를 새롭게 디자인하여 자주 사용하는 기능의 위치가 바뀌었습니다:<br>• 연결 모드는 각 앱 페이지 상단으로 이동했습니다<br>• 사용량 통계와 인증 센터는 왼쪽 사이드바로 이동했습니다<br>전체 변경 사항은 이번 버전의 릴리스 노트를 확인하세요. | This version redesigns the interface, so a few things have moved:<br>• Modes now sit at the top of each app page<br>• Usage and Accounts are in the sidebar<br>See the release notes for everything that changed. | 已修订 |
| newLayoutNotice.viewReleaseNotes | 查看更新说明 | 릴리스 노트 보기 | View release notes | 保留 |
| newLayoutNotice.confirm | 我知道了 | 확인했습니다 | Got it | 已修订 |
| whatsNew.updatedTo | 已更新到 v{{version}} | v{{version}}(으)로 업데이트됨 | Updated to v{{version}} | 保留 |
| whatsNew.recentTitle | 近期更新 | 최근 업데이트 | Recent updates | 保留 |
| whatsNew.since | 自 v{{version}} 以来的更新 | v{{version}} 이후 변경 사항 | What changed since v{{version}} | 保留 |
| whatsNew.types.new | 新增 | 신규 | New | 已修订 |
| whatsNew.types.fix | 修复 | 수정 | Fix | 保留 |
| whatsNew.types.improve | 改进 | 개선 | Improved | 保留 |
| whatsNew.versionDetails | 详情 | 세부 정보 | Details | 保留 |
| whatsNew.showEarlier | 还有 {{count}} 个更早的版本 | 이전 버전 {{count}}개 | {{count}} earlier version(s) | 保留 |
| whatsNew.viewFull | 查看完整更新内容 | 전체 변경 기록 보기 | View full changelog | 保留 |
| whatsNew.confirm | 知道了 | 확인했습니다 | Got it | 已修订 |
| authCenter.helpTitle | 授权中心是什么 | 인증 센터란? | What is Accounts? | 已修订 |
| authCenter.group.helpTitle | {{service}} 账号怎么用 | {{service}} 계정의 사용 방식 | How {{service}} accounts are used | 保留 |
| authCenter.group.copilotHelp | 用于 Claude Code、Claude Desktop 的 GitHub Copilot 预设。没指定账号的供应商用「默认」账号。 | Claude Code와 Claude Desktop의 GitHub Copilot 프리셋에서 사용합니다. 계정을 선택하지 않은 공급자는 기본 계정을 사용합니다. | Used by GitHub Copilot presets in Claude Code and Claude Desktop. Providers without a chosen account use the Default one. | 已修订 |
| authCenter.group.chatgptHelp | 用于 Claude Code、Claude Desktop 的 ChatGPT 预设，以及 Codex 官方登录绑定。没指定账号的供应商用「默认」账号。 | Claude Code와 Claude Desktop의 ChatGPT 프리셋 및 Codex의 공식 로그인 연결에 사용합니다. 계정을 선택하지 않은 공급자는 기본 계정을 사용합니다. | Used by ChatGPT presets in Claude Code and Claude Desktop, and by Codex's official-login binding. Providers without a chosen account use the Default one. | 已修订 |
| authCenter.group.xaiHelp | 用于 Claude Code、Claude Desktop、Codex 的 xAI 预设。没指定账号的供应商用「默认」账号。 | Claude Code, Claude Desktop 및 Codex의 xAI 프리셋에서 사용합니다. 계정을 선택하지 않은 공급자는 기본 계정을 사용합니다. | Used by xAI presets in Claude Code, Claude Desktop and Codex. Providers without a chosen account use the Default one. | 已修订 |
| authCenter.group.agyHelp | Antigravity CLI（agy）的官方登录。agy 同时只能登录一个号，「切换」会把 agy 的登录换成选中的账号，之后新开的 agy 都用它。agy 里原来登着的号会自动收进这里，切走也不会丢。 | Antigravity CLI(agy)의 공식 로그인입니다. agy는 한 번에 하나의 계정에만 로그인할 수 있습니다. 전환하면 agy의 로그인이 선택한 계정으로 교체되며 이후 시작한 agy 세션에서 사용됩니다. 기존에 agy에 로그인된 계정은 자동으로 여기에 추가되므로 다른 계정으로 전환해도 사라지지 않습니다. | The official sign-in for Antigravity CLI (agy). agy can only be signed in to one account at a time; Switch replaces agy's sign-in with the selected account, and agy sessions started afterwards use it. The account agy was already signed in with is added here automatically, so switching away never loses it. | 保留 |
| authCenter.addAccount | 添加账号 | 계정 추가 | Add account | 保留 |
| authCenter.groupMenu | {{service}} 的更多操作 | {{service}}의 추가 작업 | More actions for {{service}} | 保留 |
| authCenter.accountMenu | {{login}} 的更多操作 | {{login}}의 추가 작업 | More actions for {{login}} | 保留 |
| authCenter.removeAll | 删除全部账号 | 모든 계정 삭제 | Delete all accounts | 保留 |
| authCenter.removeAccount | 删除账号 | 계정 삭제 | Delete account | 保留 |
| authCenter.setDefault | 设为默认 | 기본값으로 설정 | Set as default | 保留 |
| authCenter.reauth | 重新登录 | 다시 로그인 | Sign in again | 保留 |
| authCenter.busyHint | 先完成或取消正在进行的登录 | 먼저 진행 중인 로그인을 완료하거나 취소하세요 | Finish or cancel the sign-in in progress first | 保留 |
| authCenter.default | 默认 | 기본값 | Default | 保留 |
| authCenter.needsReauth | 需要重新登录 | 다시 로그인 필요 | Sign-in needed | 已修订 |
| authCenter.empty | 还没有登录 {{service}} 账号。 | 아직 로그인된 {{service}} 계정이 없습니다. | No {{service}} account signed in yet. | 保留 |
| authCenter.signedInOn | {{date}}登录 | {{date}}에 로그인함 | Signed in {{date}} | 保留 |
| authCenter.enterpriseServer | Enterprise Server | Enterprise Server | Enterprise Server | 保留 |
| authCenter.enterpriseDomain | 企业域名 | 기업 도메인 | Enterprise domain | 保留 |
| authCenter.enterpriseDomainRequired | 先填企业域名，例如 company.ghe.com | 먼저 기업 도메인을 입력하세요 (예: company.ghe.com) | Enter the enterprise domain first, e.g. company.ghe.com | 保留 |
| authCenter.codexReauthNote | 缺少登录凭据（id_token），不能用于 Codex 托管绑定 | 로그인 자격 증명(id_token)이 없어 Codex 관리형 연결에 사용할 수 없습니다 | Missing a sign-in credential (id_token), so it can't be used for Codex managed binding | 保留 |
| authCenter.xaiReauthNote | 登录凭据已失效，用到它的供应商无法使用 | 로그인 자격 증명이 만료되어 이를 사용하는 공급자가 작동하지 않습니다 | Sign-in credential expired; providers using it won't work | 已修订 |
| authCenter.statusLoading | 正在加载账号… | 계정 불러오는 중… | Loading accounts… | 保留 |
| authCenter.xaiStatusLoadFailed | 无法加载 xAI 账号状态，请重试。 | xAI 계정을 불러올 수 없습니다. 다시 시도하세요. | Couldn't load xAI accounts. Try again. | 保留 |
| authCenter.retry | 重试 | 다시 시도 | Retry | 保留 |
| authCenter.loginFailed | 登录没有完成 | 로그인이 완료되지 않았습니다 | Sign-in didn't finish | 保留 |
| authCenter.pending.add | 添加 {{service}} 账号 · 等待授权中… | {{service}} 계정 추가 중 · 인증 대기 중… | Adding a {{service}} account · Waiting for authorization… | 保留 |
| authCenter.pending.login | 登录 {{service}} · 等待授权中… | {{service}}에 로그인 중 · 인증 대기 중… | Signing in to {{service}} · Waiting for authorization… | 保留 |
| authCenter.pending.reauth | 重新登录 {{login}} · 等待授权中… | {{login}}(으)로 다시 로그인 중 · 인증 대기 중… | Signing in again as {{login}} · Waiting for authorization… | 保留 |
| authCenter.pending.enterCode | 在浏览器中输入验证码： | 브라우저에 다음 코드를 입력하세요: | Enter this code in the browser: | 保留 |
| authCenter.pending.copy | 复制验证码 | 코드 복사 | Copy code | 保留 |
| authCenter.pending.copied | 验证码已复制。 | 코드를 복사했습니다. | Code copied. | 保留 |
| authCenter.pending.open | 打开授权页面 | 인증 페이지 열기 | Open the authorization page | 保留 |
| authCenter.pending.note | 已在浏览器打开授权页面，完成后这里会自动更新。注意 {{service}} 的使用条款。 | 브라우저에 인증 페이지가 열렸습니다. 완료하면 자동으로 업데이트됩니다. {{service}}의 이용 약관을 확인하세요. | The authorization page is open in your browser; this updates on its own when you finish. Mind {{service}}'s terms of use. | 保留 |
| authCenter.pending.browserNote | 已在浏览器打开 {{service}} 的登录页，登录并同意授权后这里会自动更新。 | 브라우저에 {{service}} 로그인 페이지가 열렸습니다. 로그인 후 접근을 허용하면 자동으로 업데이트됩니다. | The {{service}} sign-in page is open in your browser. Sign in and grant access, and this updates automatically. | 保留 |
| authCenter.pending.reopen | 重新打开登录页 | 로그인 페이지 다시 열기 | Reopen sign-in page | 保留 |
| authCenter.toast.added | 已添加 {{service}} 账号。 | {{service}} 계정을 추가했습니다. | {{service}} account added. | 保留 |
| authCenter.toast.reauthed | {{login}} 已重新登录。 | {{login}}(으)로 다시 로그인했습니다. | Signed in again as {{login}}. | 保留 |
| authCenter.quota.updating | 更新中… | 업데이트 중… | Updating… | 保留 |
| authCenter.quota.loading | 正在查询额度… | 할당량 확인 중… | Checking quota… | 保留 |
| authCenter.quota.refresh | 刷新额度 | 할당량 새로 고침 | Refresh quota | 保留 |
| authCenter.quota.refreshAria | 刷新 {{login}} 的额度 | {{login}}의 할당량 새로 고침 | Refresh quota for {{login}} | 保留 |
| authCenter.agy.reauthNote | 登录凭据已失效，切不过去 | 로그인이 만료되어 전환할 수 없습니다 | Sign-in expired, can't switch to it | 保留 |
| authCenter.agy.addedOn | {{date}}添加 | {{date}}에 추가됨 | Added {{date}} | 保留 |
| authCenter.agy.statusLoadFailed | 无法读取 Antigravity 账号，请重试。 | Antigravity 계정을 읽을 수 없습니다. 다시 시도하세요. | Couldn't read Antigravity accounts. Try again. | 保留 |
| authCenter.agy.empty | 还没有 Antigravity 账号。agy 里已登录的号会自动出现在这里。 | 아직 Antigravity 계정이 없습니다. agy에 로그인된 계정이 자동으로 여기에 표시됩니다. | No Antigravity accounts yet. The account agy is signed in with appears here automatically. | 保留 |
| authCenter.agy.login | 用 Google 登录 | Google로 로그인 | Sign in with Google | 保留 |
| authCenter.agy.current | agy 在用 | agy에서 사용 중 | In use by agy | 保留 |
| authCenter.agy.switchTo | 切换 agy 到这个账号 | agy를 이 계정으로 전환 | Switch agy to this account | 保留 |
| authCenter.agy.removeNote | 不会让 agy 退出登录：agy 现在登着的号删掉后仍然可用。 | agy의 로그인은 유지됩니다. 이 계정을 사용 중인 경우 여기서 제거해도 계속 작동합니다. | agy stays signed in: if agy is using this account, it keeps working after removal. | 保留 |
| authCenter.agy.switched | 已切换，新开的 agy 会使用这个账号。 | 전환했습니다. 새 agy 세션은 이 계정을 사용합니다. | Switched. New agy sessions will use this account. | 保留 |
| authCenter.agy.switchedWhileRunning | 已切换。检测到 agy 正在运行：已打开的 agy 仍用原账号，还可能把原账号写回去，请退出后重新打开。 | 전환했습니다. 실행 중인 agy가 감지되었습니다. 이미 실행 중인 agy는 기존 계정을 계속 사용하며 기존 계정 정보를 로그인 설정에 다시 저장할 수도 있습니다. agy를 모두 종료한 뒤 다시 실행하세요. | Switched. agy is running: open agy sessions keep using the previous account and may write it back. Quit agy and open it again. | 已修订 |
| kimi.oauth.useAccount | 使用此账号 | 이 계정 사용 | Use this account | 保留 |
| kimi.oauth.title | Kimi Code 官方登录 | Kimi Code 공식 로그인 | Kimi Code official sign-in | 保留 |
| kimi.oauth.description | 可添加多个 Kimi 编程套餐账号，各自保存凭据和供应商。在此管理登录，再选择账号使用其官方模型。 | Kimi 코딩 요금제 계정을 여러 개 추가하고 각 계정의 자격 증명과 공급자를 별도로 저장할 수 있습니다. 여기에서 로그인을 관리한 다음 계정을 선택하여 해당 계정의 공식 모델을 사용하세요. | Add Kimi coding plan accounts with separate credentials and providers. Manage sign-in here, then select an account to use its official models. | 已修订 |
| kimi.oauth.region | 登录区域 | 로그인 지역 | Sign-in region | 保留 |
| kimi.oauth.mainland-cn | 国内版 | 중국 본토 | Mainland China | 保留 |
| kimi.oauth.global | 海外版 | 글로벌 | Global | 保留 |
| kimi.oauth.signIn | 登录 Kimi | Kimi에 로그인 | Sign in to Kimi | 保留 |
| kimi.oauth.removeAccount | 删除账号 | 계정 삭제 | Remove account | 保留 |
| kimi.oauth.dismissAccount | 移出列表 | 목록에서 제거 | Hide from list | 已修订 |
| kimi.oauth.signedOut | 未登录 | 로그아웃됨 | Signed out | 保留 |
| kimi.oauth.statusFailed | 无法读取登录状态 | 로그인 상태를 읽을 수 없음 | Cannot read sign-in status | 保留 |
| kimi.oauth.expired | 授权码已过期，请重新登录。 | 인증 코드가 만료되었습니다. 다시 로그인하세요. | The authorization code expired. Please sign in again. | 保留 |
| kimi.oauth.denied | 授权已被拒绝，请重新登录。 | 인증이 거부되었습니다. 다시 로그인하세요. | Authorization was denied. Please sign in again. | 保留 |
| kimi.oauth.cancelled | 登录已取消或被其他登录替代，请重新登录。 | 이 로그인은 취소되거나 다른 로그인으로 교체되었습니다. 다시 로그인하세요. | This sign-in was cancelled or replaced. Please sign in again. | 保留 |
| kimi.oauth.success | Kimi Code 登录成功，已添加官方模型。 | Kimi Code에 로그인하고 공식 모델을 추가했습니다. | Signed in to Kimi Code and added the official models. | 保留 |
| kimi.oauth.removeConfirm | 删除 {{name}}？会从 Kimi Code 里删掉这个账号的供应商和模型，并删除它的本机登录凭据和卡片。其他账号不受影响。 | {{name}}을(를) 제거하시겠습니까? Kimi Code의 해당 공급자와 모델, 로컬 자격 증명 및 카드가 제거됩니다. 다른 계정에는 영향을 주지 않습니다. | Remove {{name}}? Its provider and models are removed from Kimi Code, along with its local credentials and card. Other accounts are not affected. | 已修订 |
| kimi.oauth.dismissConfirm | 把 {{name}} 移出列表？这是 Kimi Code 自己的登录，CC Switch 不会替它退出登录，凭据和模型都会保留；如需退出，请在 Kimi Code 里运行 /logout。之后重新登录会让它回到列表。 | {{name}}을(를) 목록에서 제거하시겠습니까? Kimi Code 자체 로그인 계정이므로 CC Switch에서 대신 로그아웃하지 않으며 자격 증명과 모델도 유지됩니다. 로그아웃하려면 Kimi Code에서 /logout을 실행하세요. 이후 다시 로그인하면 목록에 다시 표시됩니다. | Hide {{name}} from the list? This is Kimi Code's own login; CC Switch will not sign it out and keeps its credentials and models. To sign out, run /logout in Kimi Code. Signing in again brings it back to the list. | 已修订 |
| kimi.oauth.primaryHidden | Kimi Code 自己的登录已移出列表，重新登录同一账号即可找回 | Kimi Code 자체 로그인 계정을 목록에서 제거했습니다. 같은 계정으로 다시 로그인하면 되찾을 수 있습니다. | Kimi Code's own login was removed from the list; sign in to the same account to bring it back | 已修订 |
| kimi.oauth.removeCurrentHint | 这个账号正在使用，请先切换到其他账号再删除 | 사용 중인 계정입니다. 제거하기 전에 다른 계정으로 전환하세요. | This account is in use. Switch to another account before removing it. | 保留 |
| kimi.oauth.manageAccounts | 管理 Kimi 账号 | Kimi 계정 관리 | Manage Kimi accounts | 保留 |
| kimi.oauth.managedHint | 请在授权中心管理 Kimi 官方账号。 | 인증 센터에서 Kimi 공식 계정을 관리합니다. | Manage official Kimi accounts in the Authorization Center. | 保留 |
| kimi.oauth.current | Kimi 在用 | Kimi에서 사용 중 | In use by Kimi | 保留 |
| kimi.oauth.primaryShort | Kimi Code 自己的登录 | Kimi Code 자체 로그인 | Kimi Code's own login | 保留 |
| kimi.oauth.empty | 还没有 Kimi 账号。Kimi Code 里已登录的号会自动出现在这里。 | 아직 Kimi 계정이 없습니다. Kimi Code에 로그인된 계정이 자동으로 여기에 표시됩니다. | No Kimi accounts yet. The account signed in to Kimi Code shows up here automatically. | 保留 |
| kimi.oauth.help | 可添加多个 Kimi 编程套餐账号，每个号在 Kimi Code 里有自己的供应商和模型。「使用此账号」会把 Kimi Code 的默认模型换成这个号的，之后新开的会话都用它。Kimi Code 自己登着的号会自动出现在这里，联网搜索和网页抓取始终用它；在这里删掉它只会移出列表，不会让 Kimi Code 退出登录。 | Kimi 코딩 요금제 계정을 여러 개 추가할 수 있습니다. 각 계정에는 Kimi Code의 개별 공급자와 모델이 생깁니다. “이 계정 사용”을 누르면 Kimi Code의 기본 모델이 해당 계정으로 전환되며 이후 새 세션에서 사용됩니다. Kimi Code 자체 로그인 계정은 자동으로 표시되며 웹 검색과 가져오기에 항상 사용됩니다. 여기에서 제거해도 목록에서만 숨겨지며 Kimi Code에서 로그아웃되지 않습니다. | Add several Kimi coding plan accounts; each gets its own provider and models in Kimi Code. "Use this account" switches Kimi Code's default model to that account, and new sessions use it from then on. The account Kimi Code itself is signed in with shows up here automatically and is always used for web search and fetch; removing it here only hides it from the list and never signs Kimi Code out. | 已修订 |
| kimi.modelSelectionHint | 点击供应商卡片的切换按钮选择默认供应商；需要指定其他模型时，在 Kimi Code 中使用 /model。 | 공급자 카드의 전환 버튼을 눌러 기본 공급자를 선택하세요. 다른 모델을 지정하려면 Kimi Code에서 /model을 사용하세요. | Use the switch button on a provider card to select it. To choose another model, use /model in Kimi Code. | 已修订 |
| kimi.contextSize | 上下文长度 | 컨텍스트 크기 | Context size | 保留 |
| kimi.capabilities.image_in | 图片输入 | 이미지 입력 | Image input | 保留 |
| kimi.capabilities.thinking | 思考 | 추론 | Thinking | 已修订 |
| kimi.capabilities.always_thinking | 始终思考 | 항상 추론 | Always thinking | 保留 |
| kimi.capabilities.tool_use | 工具调用 | 도구 사용 | Tool use | 保留 |
| kimi.capabilities.dynamically_loaded_tools | 按需加载工具 | 필요할 때 도구 불러오기 | Load tools on demand | 保留 |
| kimi.capabilityHints.always_thinking | 模型的思考无法关闭时勾选：选中该模型时自动开启思考，且不提供关闭选项 | 모델의 추론을 끌 수 없는 경우 선택하세요. Kimi는 이 모델 선택 시 추론을 켜고 끄기 옵션을 숨깁니다 | Check when the model's thinking can't be turned off: Kimi turns thinking on when this model is selected and hides the off option | 保留 |
| kimi.capabilityHints.dynamically_loaded_tools | 让模型按需加载工具说明，缩短请求。仅 Kimi 自家模型支持，第三方模型请勿勾选；还需开启 KIMI_CODE_EXPERIMENTAL_TOOL_SELECT | 요청 길이를 줄이기 위해 필요할 때 도구 설명을 불러옵니다. Kimi 자체 모델만 지원하므로 타사 모델에서는 꺼 두세요. KIMI_CODE_EXPERIMENTAL_TOOL_SELECT도 켜야 합니다 | Lets the model load tool descriptions on demand to keep requests short. Only Kimi's own models support it; leave it off for third-party models. Also requires KIMI_CODE_EXPERIMENTAL_TOOL_SELECT | 已修订 |
| kimi.empty.title | 添加 Kimi Code 供应商 | Kimi Code 공급자 추가 | Add a Kimi Code provider | 已修订 |
| kimi.empty.description | 配置请求地址、API Key 和模型；已有 Kimi 配置会自动导入。 | 엔드포인트, API 키 및 모델을 설정합니다. 기존 Kimi 설정은 자동으로 가져옵니다. | Configure an endpoint, API key and models. Existing Kimi configuration is imported automatically. | 保留 |
| kimi.deleteSessionHint | 请在 Kimi Code 中删除，以同时更新会话索引和历史记录。 | 색인과 기록을 함께 업데이트하려면 Kimi Code에서 이 세션을 삭제하세요. | Delete this session in Kimi Code to update its index and history together. | 保留 |
| kimi.error.defaultModelInUse | Kimi Code 正在使用该供应商的模型，请先在 Kimi Code 中用 /model 切换到其他模型 | Kimi Code가 이 공급자의 모델을 사용 중입니다. 먼저 Kimi Code에서 /model로 다른 모델로 전환하세요. | Kimi Code is using a model from this provider. Switch to another model with /model in Kimi Code first. | 已修订 |
| kimi.error.secondaryModelInUse | Kimi Code 的子代理模型正在使用该供应商的模型，请先在 Kimi Code 中用 /secondary-model 更换 | Kimi Code의 서브에이전트가 이 공급자의 모델을 사용 중입니다. 먼저 Kimi Code에서 /secondary-model로 변경하세요. | Kimi Code's subagent model uses a model from this provider. Change it with /secondary-model in Kimi Code first. | 已修订 |
| native.tray.rs.show_main | 打开 CC Switch | CC Switch 열기 | Open CC Switch | 保留 |
| native.tray.rs.open_website | 打开官方网站 | 공식 웹사이트 열기 | Open official website | 保留 |
| native.tray.rs.lightweight_mode | 轻量模式 | 경량 모드 | Lightweight mode | 保留 |
| native.tray.rs.quit | 退出 CC Switch | CC Switch 종료 | Quit CC Switch | 保留 |
| native.tray.rs.quit_stops_routing | 退出 CC Switch（路由服务会停止） | CC Switch 종료 (라우팅 서비스 중지) | Quit CC Switch (stops the routing service) | 保留 |
| native.tray.rs.projects_label | 项目 | 프로젝트 | Projects | 保留 |
| native.tray.rs.no_project_label | 不使用项目 | 프로젝트 없음 | No project | 保留 |
| native.tray.rs.header_direct | 直连 | 직접 연결 | Direct | 保留 |
| native.tray.rs.header_route | 路由 | 라우팅 | Routing | 保留 |
| native.tray.rs.header_failover | 路由 · 故障转移开启中 | 라우팅 · 장애 조치 켜짐 | Routing · Failover on | 保留 |
| native.tray.rs.header_stack | 聚合 · 默认供应商 | 통합 · 기본 공급자 | Aggregation · Default provider | 已修订 |
| native.tray.rs.header_stack_default | 聚合 · 默认 {name} | 통합 · 기본값: {name} | Aggregation · Default: {name} | 保留 |
| native.tray.rs.failover_note | 按队列自动选择，要调整请到应用页 | 대기열에서 자동으로 선택됩니다. 앱 페이지에서 변경하세요 | Picked from the queue automatically; change it on the app page | 保留 |
| native.tray.rs.mode_route | 路由 | 라우팅 | Routing | 保留 |
| native.tray.rs.mode_stack | 聚合 | 통합 | Aggregation | 保留 |
| native.tray.rs.needs_routing_suffix | （需要路由）… |  (라우팅 필요)… |  (needs routing)… | 保留 |
| native.tray.rs.official_blocked_suffix | （官方订阅不经过路由） |  (공식 요금제는 라우팅을 사용하지 않음) |  (official plans don't go through routing) | 保留 |
| native.tray.rs.open_app_page | 打开 {app} 页面 | {app} 페이지 열기 | Open {app} page | 保留 |
| native.tray.rs.add_provider | 添加供应商… | 공급자 추가… | Add provider… | 已修订 |
| native.tray.rs.almost_out | 快用完 | 거의 소진됨 | almost out | 保留 |
| native.tray.rs.needs_attention | 需要处理 | 확인 필요 | needs attention | 保留 |
| native.tray.rs.problem_service_down | 路由服务没在运行（端口 {port}） | 라우팅 서비스가 실행 중이 아닙니다 (포트 {port}) | The routing service isn't running (port {port}) | 保留 |
| native.tray.rs.problem_attach_failed | {app}：上次的{mode}没能接上，已回到直连 | {app}: 이전 {mode} 연결에 실패하여 직접 연결로 돌아갔습니다 | {app}: {mode} couldn't reconnect at startup; back to direct | 已修订 |
| native.tray.rs.problem_switch_failed | {app} 没切换成功：{reason} | {app} 전환 실패: {reason} | {app} didn't switch: {reason} | 保留 |
| native.tray.rs.problem_more | 还有 {count} 个问题，打开 CC Switch 查看 | 문제 {count}개 더 있음 — CC Switch에서 확인하세요 | {count} more issues — open CC Switch to see them | 保留 |
| native.tray.rs.tooltip_problem | CC Switch · 需要处理：{problem} | CC Switch · 확인 필요: {problem} | CC Switch · Needs attention: {problem} | 保留 |
| native.tray.rs.feedback_switched | {app} 已切换到 {name}，重启 {app} 后生效 | {app}의 공급자가 {name}(으)로 전환되었습니다. 적용하려면 {app}을(를) 다시 시작하세요 | {app} switched to {name}. Restart {app} to apply | 已修订 |
| native.tray.rs.feedback_stack_default | {app} 的默认供应商改为 {name}，重启 {app} 后生效 | {app}의 기본 공급자가 {name}(으)로 변경되었습니다. 적용하려면 {app}을(를) 다시 시작하세요 | {app}'s default provider is now {name}. Restart {app} to apply | 已修订 |
| native.tray.rs.feedback_profile | 已把项目「{name}」用到 {app} | {app}에 {name} 프로젝트를 적용했습니다 | Applied project “{name}” to {app} | 保留 |
| native.tray.rs.tier_five_hour | 5 小时 | 5시간 | 5-hour | 保留 |
| native.tray.rs.tier_weekly | 每周 | 주간 | Weekly | 保留 |
| native.tray.rs.tier_fable | Fable | Fable | Fable | 保留 |
| native.tray.rs.tier_monthly | 每月 | 월간 | Monthly | 保留 |
| native.tray.rs.tier_thirty_day | 30 天 | 30일 | 30-day | 保留 |
| native.tray.rs.tier_credits | 额度 | 크레딧 | Credits | 保留 |
| native.tray.rs.tier_gemini_pro | Pro | Pro | Pro | 保留 |
| native.tray.rs.tier_gemini_flash | Flash | Flash | Flash | 保留 |
| native.tray.rs.tier_gemini_flash_lite | Flash Lite | Flash Lite | Flash Lite | 保留 |
| native.tray.rs.tier_premium | 高级请求 | 프리미엄 요청 | Premium | 已修订 |
| native.tray.rs.tier_left | {labelSp}剩余 {value}% | {label} {value}% 남음 | {label} {value}% left | 保留 |
| native.tray.rs.tier_used | {labelSp}已用 {value}% | {label} {value}% 사용 | {label} {value}% used | 保留 |
| native.tray.rs.tier_used_up | {labelSp}已用完 | {label} 소진됨 | {label} used up | 保留 |
| native.tray.rs.balance | 余额 {value} | 잔액 {value} | Balance {value} | 保留 |
| native.tray.rs.balance_used_up | 余额已用完 | 잔액 소진됨 | Balance used up | 保留 |
| native.tray.rs.plan_expired | 套餐已过期 | 요금제 만료됨 | Plan expired | 保留 |
| native.tray.rs.used_amount | 已使用 {value} | {value} 사용 | Used {value} | 保留 |
| native.tray.rs.quota_failed | 额度没查到 | 할당량을 확인할 수 없음 | Quota unavailable | 保留 |
| native.tray.rs.quota_failed_login_expired | 额度没查到：登录已过期 | 할당량을 확인할 수 없음: 로그인 만료 | Quota unavailable: sign-in expired | 保留 |
| native.tray.rs.quota_failed_token_refresh_pending | 额度没查到：令牌待刷新 | 할당량을 확인할 수 없음: 토큰 갱신 대기 중 | Quota unavailable: token refresh pending | 保留 |
| native.tray.rs.reset_on_date | {labelSp}额度 {when}重置 | {when}에 {label} 할당량 초기화 | {label} quota resets {when} | 保留 |
| native.tray.rs.reset_at_time | {labelSp}额度 {when} 重置 | {when}에 {label} 할당량 초기화 | {label} quota resets at {when} | 保留 |
| native.tray.rs.date_format | %-m 月 %-d 日 | %-m월 %-d일 | %b %-d | 保留 |
| native.tray_panel.rs.switch_provider | 切换供应商 | 공급자 전환 | Switch provider | 已修订 |
| native.tray_panel.rs.search_placeholder | 搜索供应商… | 공급자 검색… | Search providers… | 已修订 |
| native.tray_panel.rs.in_use | 使用中 | 사용 중 | In use | 保留 |
| native.tray_panel.rs.no_match | 没有匹配的供应商 | 일치하는 공급자 없음 | No matching providers | 已修订 |
| native.tray_panel.rs.open_main | 打开主窗口 | 메인 창 열기 | Open main window | 保留 |
| native.tray_panel.rs.quit | 退出 | 종료 | Quit | 保留 |
| native.tray_panel.rs.settings | 设置 | 설정 | Settings | 保留 |
| native.tray_panel.rs.open_panel | 打开快捷面板 | 빠른 패널 열기 | Open quick panel | 保留 |
| native.tray_panel.rs.config_tab | 配置 | 설정 | Configuration | 保留 |
| native.tray_panel.rs.usage_tab | 用量 | 사용량 | Usage | 保留 |
| native.tray_panel.rs.resets_in | {when}后重置 | {when} 후 초기화 | Resets in {when} | 保留 |
| native.tray_panel.rs.duration_days | {n}天 | {n}일 | {n}d | 保留 |
| native.tray_panel.rs.duration_hours | {n}小时 | {n}시간 | {n}h | 保留 |
| native.tray_panel.rs.duration_minutes | {n}分 | {n}분 | {n}m | 保留 |
| native.tray_panel.rs.duration_sep |  |   |   | 保留 |
| native.tray_panel.rs.reset_credits | 可重置 {count} 次 | 초기화 {count}회 가능 | {count} resets available | 保留 |
| native.tray_panel.rs.lightweight_mode | 轻量模式 | 경량 모드 | Lightweight mode | 保留 |
| native.config.invalidJSON | 无效的 JSON 格式: {error} | 잘못된 JSON 형식: {error} | Invalid JSON format: {error} | 保留 |
| native.config.invalidTOML | 无效的 TOML 格式: {error} | 잘못된 TOML 형식: {error} | Invalid TOML format: {error} | 保留 |
