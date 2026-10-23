# 动态名称宾格助词统一

日期：2026-10-24。按用户要求，将动态值（包括闭引号、闭括号）后直接连接的 을／를 统一为 을(를)，共修改 39 条、41 处。已覆盖姓名、路径、版本、字段名、数量等插值；原有 을(를) 保持不变。固定韩语名词（例如 모델을、파일을、설정을）和动态数字后带固定量词的结构（例如 {{count}}개를）按已有正确助词保留。

实际译文、HTML／Markdown 对照和审计已同步；原始 before 和历史轮次记录保留。原生韩语文案未发现直接跟在动态值后、尚未统一的宾格助词。

| 翻译键 | 修改前 | 修改后 |
|---|---|---|
| settings.backupStorage.deleteConfirmTitle | '{{name}}'을 삭제하시겠습니까? | '{{name}}'을(를) 삭제하시겠습니까? |
| settings.backupStorage.deleteSuccess | 삭제하여 {{size}}를 확보했습니다 | 삭제하여 {{size}}을(를) 확보했습니다 |
| settings.codexSessionCompressionUsage | 세션은 현재 {{size}}를 사용합니다. | 세션은 현재 {{size}}을(를) 사용합니다. |
| settings.toolActionVersionUnchanged | 아직 {{version}}(최신: {{latest}})를 사용하고 있습니다. 업데이트 프로그램이 업데이트를 적용하지 않고 성공했다고 보고했을 수 있습니다. | 아직 {{version}}(최신: {{latest}})을(를) 사용하고 있습니다. 업데이트 프로그램이 업데이트를 적용하지 않고 성공했다고 보고했을 수 있습니다. |
| sessionManager.pathCopied | {{path}}를 복사했습니다. | {{path}}을(를) 복사했습니다. |
| sessionManager.reader.event.slashCommand | {{command}}를 실행 | {{command}}을(를) 실행 |
| providerForm.fillParameter | {{label}}를 입력하세요. | {{label}}을(를) 입력하세요. |
| providerForm.fillTemplateValue | {{label}}를 입력하세요. | {{label}}을(를) 입력하세요. |
| dbUpgrade.versionInfo | 데이터베이스 v{{db}} · 앱은 v{{supported}}를 지원합니다 | 데이터베이스 v{{db}} · 앱은 v{{supported}}을(를) 지원합니다 |
| dbUpgrade.updateAvailable | 버전 v{{version}}를 사용할 수 있습니다. 업그레이드하면 계속할 수 있습니다. | 버전 v{{version}}을(를) 사용할 수 있습니다. 업그레이드하면 계속할 수 있습니다. |
| prompts.copiedPath | {{path}}를 복사했습니다. | {{path}}을(를) 복사했습니다. |
| prompts.searchFound | {{count}}를 찾았습니다 | {{count}}을(를) 찾았습니다 |
| prompts.copyDialog.title | "{{name}}"를 다른 앱에 복사 | "{{name}}"을(를) 다른 앱에 복사 |
| prompts.toast.enabled | "{{name}}"를 활성화하고 {{path}}를 덮어썼습니다. | "{{name}}"을(를) 활성화하고 {{path}}을(를) 덮어썼습니다. |
| prompts.toast.disabledPi | "{{name}}"를 비활성화하고 AGENTS.md를 삭제했습니다. | "{{name}}"을(를) 비활성화하고 AGENTS.md를 삭제했습니다. |
| prompts.toast.added | "{{name}}"를 추가했습니다. | "{{name}}"을(를) 추가했습니다. |
| prompts.toast.saved | "{{name}}"를 저장했습니다. | "{{name}}"을(를) 저장했습니다. |
| prompts.toast.savedActive | "{{name}}"를 저장하고 {{path}}를 덮어썼습니다. | "{{name}}"을(를) 저장하고 {{path}}을(를) 덮어썼습니다. |
| prompts.toast.deleted | "{{name}}"를 삭제했습니다. | "{{name}}"을(를) 삭제했습니다. |
| prompts.toast.restored | "{{name}}"를 복원했습니다. | "{{name}}"을(를) 복원했습니다. |
| prompts.toast.copied | "{{name}}"를 {{apps}}에 복사했습니다. | "{{name}}"을(를) {{apps}}에 복사했습니다. |
| skills.error.skillPathNotFound | {{owner}}/{{name}} 저장소에서 스킬 경로 '{{path}}'를 찾을 수 없습니다. | {{owner}}/{{name}} 저장소에서 스킬 경로 '{{path}}'을(를) 찾을 수 없습니다. |
| skills.uninstallConfirm | 정말로 "{{name}}"를 제거하시겠습니까? 이렇게 하면 모든 앱에서 스킬이 제거되고 먼저 로컬 백업이 생성됩니다. | 정말로 "{{name}}"을(를) 제거하시겠습니까? 이렇게 하면 모든 앱에서 스킬이 제거되고 먼저 로컬 백업이 생성됩니다. |
| deeplink.importSuccessDescription | 공급자 "{{name}}"를 성공적으로 가져왔습니다. | 공급자 "{{name}}"을(를) 성공적으로 가져왔습니다. |
| iconPicker.deleteMessage | 내 아이콘에서 "{{name}}"를 삭제하시겠습니까? 이미 이를 사용하고 있는 공급자는 영향을 받지 않습니다. | 내 아이콘에서 "{{name}}"을(를) 삭제하시겠습니까? 이미 이를 사용하고 있는 공급자는 영향을 받지 않습니다. |
| universalProvider.deleteConfirmDescription | 정말로 "{{name}}"을 삭제하시겠습니까? 이렇게 하면 각 앱에서 생성된 공급자 설정도 삭제됩니다. | 정말로 "{{name}}"을(를) 삭제하시겠습니까? 이렇게 하면 각 앱에서 생성된 공급자 설정도 삭제됩니다. |
| universalProvider.syncConfirmDescription | "{{name}}"를 동기화하면 Claude, Codex 및 Gemini의 관련 공급자 설정을 덮어씁니다. 계속하시겠습니까? | "{{name}}"을(를) 동기화하면 Claude, Codex 및 Gemini의 관련 공급자 설정을 덮어씁니다. 계속하시겠습니까? |
| omo.confirmDeleteMsg | '{{name}}'을 삭제하시겠습니까? | '{{name}}'을(를) 삭제하시겠습니까? |
| appsPage.updateNeedsNode | 새 버전 {{version}}에는 Node {{required}}가 필요하지만 이 설치는 Node {{current}}를 사용합니다. 먼저 Node를 업그레이드하세요. | 새 버전 {{version}}에는 Node {{required}}가 필요하지만 이 설치는 Node {{current}}을(를) 사용합니다. 먼저 Node를 업그레이드하세요. |
| mode.activate.viewing | 당신은 "{{view}}"를 보고 있습니다. {{app}}는 현재 {{active}}에 있습니다. | 당신은 "{{view}}"을(를) 보고 있습니다. {{app}}는 현재 {{active}}에 있습니다. |
| quota.tierUsedUp | {{label}}를 모두 사용했습니다. | {{label}}을(를) 모두 사용했습니다. |
| appMatrix.found | {{count}}를 찾았습니다 | {{count}}을(를) 찾았습니다 |
| appMatrix.toast.enabled | {{app}}에서 {{count}} {{noun}}를 활성화했습니다. | {{app}}에서 {{count}} {{noun}}을(를) 활성화했습니다. |
| appMatrix.toast.disabled | {{app}}에서 {{count}} {{noun}}를 껐습니다. | {{app}}에서 {{count}} {{noun}}을(를) 껐습니다. |
| mcpPage.toast.copiedOne | {{id}}를 JSON로 복사했습니다(env 및 헤더 값 포함). | {{id}}을(를) JSON로 복사했습니다(env 및 헤더 값 포함). |
| mcpPage.toast.deleted | {{id}}를 삭제했습니다. | {{id}}을(를) 삭제했습니다. |
| mcpPage.toast.added | {{id}}를 추가했습니다. | {{id}}을(를) 추가했습니다. |
| mcpPage.toast.saved | {{id}}를 저장했습니다 | {{id}}을(를) 저장했습니다 |
| skillsPage.toast.disabledSelection | {{app}}에서 {{count}} {{noun}}를 껐습니다. | {{app}}에서 {{count}} {{noun}}을(를) 껐습니다. |
