# 韩语术语复审记录（第三轮）

审查日期：2026-10-23。处理用户提交的 26 条备注，其中 17 条译文修改、9 条保留。

已将选定译文同步到实际韩语资源、HTML/Markdown 对照表和逐条审计记录。并将全量界面及原生托盘中表示 provider 的 제공업체 统一为 공급자，Tool Search 相关功能名称统一保留英文。原始审计 before 字段保留，审计状态及计数按最终译文重新计算。

本轮实际修改 339 条界面译文、7 条原生译文。导入 [第三轮结果 JSON](ko-review-round3-results.json) 可将提交的 26 条标为已审查并查看备注回复；批量术语替换涉及的其他条目未自动标记为用户已审查。

## 统一用词

| 概念 | 本次采用 | 说明 |
|---|---|---|
| provider | 공급자 | 适用于本工具中的供应者条目；有 Microsoft AI 产品用例，非唯一合法译法 |
| format（代码/JSON 排版） | 포맷팅 | 用户确认采用；通用编辑器与脚本编辑器保持一致 |
| refresh | 새로 고침 | 沿用 Microsoft 风格；Chrome 的不空格版本也存在 |
| import | 가져오기 | 与 Chrome 导入功能一致 |
| global settings | 전역 설정 | 与 Visual Studio 开发工具表达一致 |
| official | 공식 | 首次出现的预设名保留 Official 对照 |
| Tool Search / Artifact Tool | 保留英文名称 | 本项目功能名风格选择；不声称所有上游韩文都这样处理 |
| API Key | API 키 | 统一本文件中指 API 凭据的表述 |

“更常用”需要有代表性的界面语料统计；本次依据官方产品实例和具体界面语义作决定，不把单一实例当作频率结论。

## 官方参考来源

- [S1 Microsoft：Excel Copilot 提示，包含 AI 공급자](https://support.microsoft.com/ko-KR/Excel/copilot/copilot-in-excel-tips)
- [S2 Microsoft：Visual Studio 代码编辑器，命令为 문서 서식 지정](https://learn.microsoft.com/ko-kr/visualstudio/ide/writing-code-in-the-code-and-text-editor?view=visualstudio)
- [S3 Microsoft：Word 共同创作问题，使用 새로 고침](https://support.microsoft.com/ko-kr/word/troubleshoot-common-coauthoring-errors)
- [S4 Google：Chrome 崩溃排查，使用 새로고침](https://support.google.com/chrome/answer/142063?co=GENIE.Platform%3DDesktop&hl=ko)
- [S5 Google：Chrome 导入书签及设置，使用 가져오기](https://support.google.com/chrome/answer/96816?hl=ko)
- [S6 Microsoft：Visual Studio 打开仓库教程，使用 Git 전역 설정](https://learn.microsoft.com/ko-kr/visualstudio/get-started/tutorial-open-project-from-repo?view=visualstudio)
- [S7 Anthropic：工具上下文管理，使用 Tool search / 도구 검색](https://platform.claude.com/docs/ko/agents-and-tools/tool-use/manage-tool-context)
- [S9 Google：Chrome 更新问题，包含 업데이트 실패、업데이트하지 못했습니다、다시 시도](https://support.google.com/chrome/answer/111996?hl=ko-us)

- [S10 Microsoft：Excel 导入文本或 CSV，使用 데이터 가져오기、텍스트 가져오기 마법사](https://support.microsoft.com/ko-kr/excel/get-started/import-or-export-text-txt-or-csv-files)
- [S11 Microsoft：Outlook 基本任务，使用 가져오기/내보내기](https://support.microsoft.com/ko-kr/outlook/basic-tasks-in-outlook)
- [S12 Mozilla：Firefox 书签管理器，使用 가져오기 및 백업](https://www.mozilla.org/ko/firefox/features/bookmarks/)

以上是核查时可访问的韩文官方资料。官方帮助也可能包含机器翻译，因此以实际命令/术语用例为参照，并结合本产品语境判断。未找到直接可核实的同类控件用例时，下文明确标记为编辑或语义判断。

补充格式化用词来源：[FileMaker Pro JSONFormatElements](https://help.claris.com/ko/pro-help/content/jsonformatelements.html)、[CalculKorea JSON 工具](https://calculkorea.com/json-formatter)、[LiveParse](https://liveparse.com/)。这些实例支持 포맷/포맷팅 用法，不代表使用频率统计。

## 逐条结论

### common.unsavedLeaveMessage（保留）

原备注：编辑页这个词是否可以忽略？建议哪种？

结论：保留。「이 페이지」已经明确当前页面，离开确认框中无需再直译“编辑页”；原译没有丢失不保存修改的关键信息。属于界面语境判断。

最终译文：이 페이지를 나가면 변경 사항이 저장되지 않습니다.

### common.unsavedLeaveCancel（保留）

原备注：편집 계속하기好还是这个好？

结论：保留。계속 편집 是简短、自然的按钮写法；편집 계속하기 也可以，并无足够依据把它判为更常用。与当前简洁按钮风格一致。

最终译文：계속 편집

### common.notInstalled（修改）

原备注：설치되지 않음跟미설치哪个在软件里更常用？

结论：修改。미설치 并非错误；选择完整的状态表达 설치되지 않음，与未完成动作的状态提示一致。这是编辑选择，不宣称存在用量统计上的优势。

原译：미설치

最终译文：설치되지 않음

### common.format（修改）

原备注：格式化说成서식还是觉得怪怪的，找一下常用翻译

结论：修改。用户确认 JSON/代码排版统一采用 포맷팅。FileMaker Pro 使用 포맷 描述 JSON 排版，CalculKorea 和 LiveParse 使用 포맷팅；서식 지정 也是已有译法，不因磁盘格式化联想而排除 포맷。

原译：서식 지정

最终译文：포맷팅

### common.formatSuccess（修改）

原备注：格式化说成서식还是觉得怪怪的，找一下常用翻译

结论：修改。用户确认 JSON/代码排版统一采用 포맷팅。FileMaker Pro 使用 포맷 描述 JSON 排版，CalculKorea 和 LiveParse 使用 포맷팅；서식 지정 也是已有译法，不因磁盘格式化联想而排除 포맷。

原译：서식을 지정했습니다

最终译文：포맷팅이 완료되었습니다

### common.formatError（修改）

原备注：格式化说成서식还是觉得怪怪的，找一下常用翻译

结论：修改。用户确认 JSON/代码排版统一采用 포맷팅。FileMaker Pro 使用 포맷 描述 JSON 排版，CalculKorea 和 LiveParse 使用 포맷팅；서식 지정 也是已有译法，不因磁盘格式化联想而排除 포맷。

原译：서식 지정 실패: {{error}}

最终译文：포맷팅 실패: {{error}}

### common.refresh（保留）

原备注：检查一下需不需要空格？

结论：保留空格。Microsoft 产品采用 새로 고침 [S3]，Chrome 也存在不空格的 새로고침 [S4]。这是产品风格差异，当前写法可用，无需为了统一到另一产品而改动。

最终译文：새로 고침

### common.refreshing（保留）

原备注：找一下常用翻译

结论：保留。새로 고치는 중... 是 새로 고침 的自然进行时表达；不必机械写成 새로 고침 중。属于形态和语体判断。

最终译文：새로 고치는 중...

### common.import（保留）

原备注：这个好像不对吧？

结论：保留。Chrome、Excel、Outlook、Firefox 的导入功能均使用 가져오기 [S5][S10][S11][S12]，此处不是误译。

最终译文：가져오기

### common.enableAllForApp（修改）

原备注：再查一下相似用法怎么翻译的

结论：修改。{{app}}에서 모두 활성화 表示在指定应用中全部启用，省去生硬的 에 대해。활성화 与对应停用项保持成对；这里假设 app 是这些条目生效的应用范围，依据中英文原文。

原译：{{app}}에 대해 모두 활성화

最终译文：{{app}}에서 모두 활성화

### common.disableAllForApp（修改）

原备注：再查一下相似用法怎么翻译的

结论：修改。与上一条统一为 {{app}}에서 모두 비활성화；不混用另一套 사용 설정/사용 중지 术语。

原译：{{app}}에 대해 모두 비활성화

最终译文：{{app}}에서 모두 비활성화

### common.bulkToggleFailed（保留）

原备注：用실패是不是更合适？

结论：保留。업데이트하지 못했습니다 是完整、自然的失败提示。Chrome 官方帮助同时使用 업데이트 실패 与 업데이트하지 못했습니다 类表达 [S9]；실패 并不天然优于现有叙述句。

最终译文：항목 {{count}}개를 업데이트하지 못했습니다

### common.retry（保留）

原备注：재시도

结论：保留。다시 시도 为自然的操作表达，재시도 也成立；没有证据表明应强制改成汉字词。Chrome 帮助使用 다시 시도 [S9]。

最终译文：다시 시도

### firstRunNotice.bodyDefault（修改）

原备注：제공업체？这个确认一下

结论：修改。provider 统一为 공급자：Microsoft 的 AI 模型界面说明使用 AI 공급자 [S1]。这是本项目的统一选择，不代表 제공업체 在商业服务商语境中错误。修正多个工具与供应者的语序，补回自动保存，统一 configuration 为 설정。

原译：CC Switch를 사용하면 한 번의 클릭으로 여러 Claude Code / Codex / Gemini CLI 제공업체 간에 전환할 수 있습니다. 이러한 도구를 이미 구성한 경우 CC Switch는 기존 설정을 "default"라는 제공업체로 저장하므로 이전 구성이 손실되지 않습니다.

最终译文：CC Switch를 사용하면 Claude Code / Codex / Gemini CLI의 여러 공급자 간에 클릭 한 번으로 전환할 수 있습니다. 이러한 도구가 이미 설정되어 있다면 CC Switch가 기존 설정을 "default"라는 공급자로 자동 저장하므로 기존 설정이 손실되지 않습니다.

### firstRunNotice.bodyOfficial（修改）

原备注：공식？오피셜?这个确认一下

结论：修改。选用正式软件语体的 공식，保留 Official 便于对应预设名；不选口语感较强的 오피셜。恢复中文所指的供应者条目，写为 공식(Official) 공급자，避免与 provider 命名分裂。该取舍属于本地化判断。

原译：목록에는 ‘공식’ 프리셋도 포함되어 있습니다. 공식 기본 설정으로 돌아가려면 언제든지 선택하세요. CC Switch는 전환 전에 현재 설정을 ‘default’에 자동으로 백업하므로 자유롭게 전환할 수 있습니다. CC Switch는 이렇게 작동합니다 😊

最终译文：목록에는 ‘공식(Official)’ 공급자도 미리 등록되어 있습니다. 언제든지 선택하여 공식 기본 설정으로 돌아갈 수 있습니다. CC Switch는 전환 전에 현재 설정을 ‘default’에 자동으로 백업하므로 안심하고 전환할 수 있습니다. CC Switch는 이렇게 작동합니다 😊

### apiKeyInput.show（保留）

原备注：보기

结论：保留。표시 更明确表达解除遮蔽、显示 API 密钥；보기 更适合打开查看页面。并无将原译判错的理由；这是控件语义判断。

最终译文：API 키 표시

### claudeConfig.fullSettingsHint（修改）

原备注：怪怪的

结论：修改。用 파일의 전체 설정 내용 明确是 settings.json 文件的全部配置，避免 콘텐츠 的内容产品语感，并补回“配置”。

原译：전체 Claude Code settings.json 콘텐츠

最终译文：Claude Code settings.json 파일의 전체 설정 내용

### claudeConfig.hideAttribution（修改）

原备注：작성자?크레딧?

结论：修改。AI 기여 표시 比 AI 작성자 표시 更能覆盖贡献署名，而不暗示 AI 是唯一作者；크레딧 不如这一写法直接。这是结合 Co-Authored-By 和 PR 说明作出的语义判断。

原译：AI 작성자 표시 숨기기

最终译文：AI 기여 표시 숨기기

### claudeConfig.hideAttributionHelp（修改）

原备注：제공업체?

结论：统一 provider 为 공급자；Co-Authored-By、PR 及会话链接的原意保留。전역 설정 是开发软件中的既有表达，Visual Studio 使用 Git 전역 설정 [S6]。

原译：Claude Code가 생성한 커밋과 PR에서 Co-Authored-By 표시와 세션 링크를 제외합니다. 모든 제공업체에 적용되는 전역 설정입니다.

最终译文：Claude Code가 생성한 커밋과 PR에서 Co-Authored-By 표시와 세션 링크를 제외합니다. 모든 공급자에 적용되는 전역 설정입니다.

### claudeConfig.enableToolSearch（修改）

原备注：Tool Search 활성화

结论：修改。把 Tool Search 作为功能名称保留英文，便于对应上游。注意：Anthropic 韩文文档本身也使用 도구 검색 [S7]，因此原译不是错误；这里选择英文是本项目功能名风格。

原译：도구 검색 활성화

最终译文：Tool Search 활성화

### claudeConfig.enableToolSearchHelp（修改）

原备注：제공업체?

结论：统一 provider 为 공급자。MCP、tool_reference 等标识保持原样；端点、上下文等一般技术概念继续采用可读的韩语表达，不因备注而机械把全部术语改成英文。

原译：컨텍스트 사용량을 줄이기 위해 필요할 때 MCP 도구 정의를 불러옵니다. 타사 엔드포인트에서는 기본으로 꺼져 있습니다. 업스트림이 tool_reference를 지원할 때만 켜세요. 제공업체를 전환하면 이 설정도 함께 바뀝니다.

最终译文：컨텍스트 사용량을 줄이기 위해 필요할 때 MCP 도구 정의를 불러옵니다. 타사 엔드포인트에서는 기본으로 꺼져 있습니다. 업스트림이 tool_reference를 지원할 때만 켜세요. 공급자를 전환하면 이 설정도 함께 바뀝니다.

### claudeConfig.disableAutoUpgradeHelp（保留）

原备注：전역? 全局一般用这个单词吗？查一下

结论：保留。전역 설정 是合理且有实际开发工具用例的 global settings 译法 [S6]，claude update 命令保持原样。

最终译文：자동 업데이트를 끄고 Claude Code를 현재 버전으로 유지합니다. 필요할 때 claude update를 직접 실행하세요. 전역 설정입니다.

### claudeConfig.disableArtifact（修改）

原备注：Artifact Tool 비활성화

结论：修改。按本项目功能名风格采用 Artifact Tool，韩语动作 비활성화 保留；与帮助文案统一。此为术语规范选择，未找到足够依据宣称某一种韩译是唯一标准。

原译：아티팩트 도구 비활성화

最终译文：Artifact Tool 비활성화

### claudeConfig.disableArtifactHelp（修改）

原备注：固有名词，专业名词不要翻译，就写英文

结论：修改。与按钮统一写 Artifact Tool，并统一 provider 为 공급자。schema 是一般技术概念，保留韩文常见音译 스키마；备注中的“不翻译专业词”作为审校意见评估，不扩展为所有文字都改英文的全局命令。

原译：요청에서 Artifact 도구를 제외합니다. 일부 타사 게이트웨이는 이 도구의 스키마를 거부하여 모든 요청에 400 오류를 반환합니다. 제공업체를 전환하면 이 설정도 함께 바뀝니다.

最终译文：요청에서 Artifact Tool을 제외합니다. 일부 타사 게이트웨이는 이 도구의 스키마를 거부하여 모든 요청에 400 오류를 반환합니다. 공급자를 전환하면 이 설정도 함께 바뀝니다.

### claudeConfig.keyFieldsHint（修改）

原备注：제공업체？

结论：修改。统一 provider 为 공급자、Key 为 API 키，并明确“切换供应者时一起改变”，比原文的“按供应者设置”更贴近原意。전역 설정 保留 [S6]。

原译：엔드포인트, 키, 모델, 컨텍스트 창 및 호환성 옵션은 제공업체별 설정입니다. 나머지는 전역 Claude Code 설정이며 저장하면 모든 제공업체에 적용됩니다.

最终译文：엔드포인트, API 키, 모델, 컨텍스트 창 및 호환성 옵션은 공급자를 전환하면 함께 바뀝니다. 나머지 필드는 Claude Code 전역 설정이며 저장하면 모든 공급자에 적용됩니다.

### claudeConfig.inactiveFieldsHint（修改）

原备注：제공업체？

结论：统一本条全部 provider 为 공급자，包括未在备注单独标出的重复位置；전역 설정 保留。

原译：이전 버전에서 이 제공업체에 저장한 설정으로, 이제 제공업체를 전환해도 적용되지 않습니다. 항목을 선택하면 위의 전역 설정에 추가됩니다. 저장한 후에는 모든 제공업체에 적용됩니다.

最终译文：이전 버전에서 이 공급자에 저장한 설정으로, 이제 공급자를 전환해도 적용되지 않습니다. 항목을 선택하면 위의 전역 설정에 추가됩니다. 저장한 후에는 모든 공급자에 적용됩니다.

