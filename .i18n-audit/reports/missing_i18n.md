# 国际化遗漏审查

- 生产源码纳入：801
- 成功扫描：801
- 扫描失败：0
- 候选总数：4426
- 确认遗漏：0
- 待核实：162
- 无需国际化：4264
- 范围排除文件：1
- 候选类别排除：1891（后端错误 1436；前端单/双语硬编码 455）

> 本报告不展示已确认无需国际化的候选项。候选详情保留在 `.i18n-audit/reviews/hardcoded/`。

## 系统性结论

- 后端错误和前端单/双语硬编码文案按产品决定排除，均不计入韩语遗漏项。
- 多个前端校验器和工具函数直接抛出中文/英文错误，绕过 i18n。
- 多处可见 JSX 标签（如 `Auth:`、`TOML Config:`、`Reasoning Effort`、`API Key`）仍未使用翻译函数。
- 162 个动态翻译键已逐一登记为待核实，不能仅因运行时未崩溃视为安全。

## 确认遗漏明细（0）

## 待核实明细（162）

### 1. `dynamic-i18n:src/App.tsx:handleEnablePiProvider:779cd86c8074aae3:001`

- 状态：待核实
- 文件：`src/App.tsx:362`
- 结构：`handleEnablePiProvider` / `dynamic_i18n_key`
- 原文/表达式：`${app}.provider.enabled`
- 判定原因：翻译键由运行时表达式“`${app}.provider.enabled`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`779cd86c8074aae3ab74e44d7f9a4112386e799d3c4d3602bd8f5d133a9b3797`

### 2. `dynamic-i18n:src/App.tsx:handleEnablePiProvider:4d25811d6f7f74f8:001`

- 状态：待核实
- 文件：`src/App.tsx:370`
- 结构：`handleEnablePiProvider` / `dynamic_i18n_key`
- 原文/表达式：`${app}.provider.enableFailed`
- 判定原因：翻译键由运行时表达式“`${app}.provider.enableFailed`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4d25811d6f7f74f874704e452d4fc963c30ca9736c0fa17effb5e174eddec755`

### 3. `dynamic-i18n:src/App.tsx:handleConfirmAction:9f662d6a31a429e7:001`

- 状态：待核实
- 文件：`src/App.tsx:1049`
- 结构：`handleConfirmAction` / `dynamic_i18n_key`
- 原文/表达式：`${activeApp}.provider.removed`
- 判定原因：翻译键由运行时表达式“`${activeApp}.provider.removed`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`9f662d6a31a429e7abb4e270235f4a3145d221a103f551f9133578be4d227cea`

### 4. `dynamic-i18n:src/App.tsx:handleDuplicateProvider:fe3b12eac8542ca4:001`

- 状态：待核实
- 文件：`src/App.tsx:1103`
- 结构：`handleDuplicateProvider` / `dynamic_i18n_key`
- 原文/表达式：isNative<br>              ? "opencode.duplicateRequiresNativeDefinition"<br>              : "opencode.duplicateRequiresDefinition"
- 判定原因：翻译键由运行时表达式“isNative
              ? "opencode.duplicateRequiresNativeDefinition"
              : "opencode.duplicateRequiresDefinition"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`fe3b12eac8542ca4453864a00732b5936729c25137498b39d884736efaa8313e`

### 5. `dynamic-i18n:src/components/DeepLinkImportDialog.tsx:DeepLinkImportDialog:dfdad65bcce899e6:001`

- 状态：待核实
- 文件：`src/components/DeepLinkImportDialog.tsx:575`
- 结构：`DeepLinkImportDialog` / `dynamic_i18n_key`
- 原文/表达式：riskI18nKey(endpointRisk)
- 判定原因：翻译键由运行时表达式“riskI18nKey(endpointRisk)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`dfdad65bcce899e6341ac9fb04a16b9a165a38c0c0a5341e9df1076f6d4bac0f`

### 6. `dynamic-i18n:src/components/IconPicker.tsx:handleFileChange:16fefef2206f4fc1:001`

- 状态：待核实
- 文件：`src/components/IconPicker.tsx:116`
- 结构：`handleFileChange` / `dynamic_i18n_key`
- 原文/表达式：`iconPicker.uploadError.${code}`
- 判定原因：翻译键由运行时表达式“`iconPicker.uploadError.${code}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`16fefef2206f4fc17164e7f45bdfee2456257b2d9e91e15a66dc0b147119a614`

### 7. `dynamic-i18n:src/components/SubscriptionQuotaFooter.tsx:tierLabel:594c5d7f4330650b:001`

- 状态：待核实
- 文件：`src/components/SubscriptionQuotaFooter.tsx:129`
- 结构：`tierLabel` / `dynamic_i18n_key`
- 原文/表达式：TIER_I18N_KEYS[name]
- 判定原因：翻译键由运行时表达式“TIER_I18N_KEYS[name]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`594c5d7f4330650b8869a1eff51f6e2fe4a277881c240a0a19e4b91e46dac546`

### 8. `dynamic-i18n:src/components/SubscriptionQuotaFooter.tsx:tierShortLabel:cc8832922601ce1f:001`

- 状态：待核实
- 文件：`src/components/SubscriptionQuotaFooter.tsx:135`
- 结构：`tierShortLabel` / `dynamic_i18n_key`
- 原文/表达式：key.replace("subscription.", "subscription.short.")
- 判定原因：翻译键由运行时表达式“key.replace("subscription.", "subscription.short.")”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cc8832922601ce1f1074be0045da3942eed6b0d23f9618bb02fdf597641e861b`

### 9. `dynamic-i18n:src/components/SubscriptionQuotaFooter.tsx:label:ad936fcbed631fa6:001`

- 状态：待核实
- 文件：`src/components/SubscriptionQuotaFooter.tsx:152`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：group
- 判定原因：翻译键由运行时表达式“group”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ad936fcbed631fa67e05c3ea03953905221c9d46af0616b70badf105a966fb11`

### 10. `dynamic-i18n:src/components/UsageScriptModal.tsx:UsageScriptModal:f52cef484535047b:001`

- 状态：待核实
- 文件：`src/components/UsageScriptModal.tsx:988`
- 结构：`UsageScriptModal` / `dynamic_i18n_key`
- 原文/表达式：TEMPLATE_NAME_KEYS[name]
- 判定原因：翻译键由运行时表达式“TEMPLATE_NAME_KEYS[name]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`f52cef484535047b84076cc20d0d6ab8a036bf7c19ac95a1e96bd959dce84ce0`

### 11. `dynamic-i18n:src/components/WhatsNewDialog.tsx:WhatsNewDialog:3f85b3caaa1db65c:001`

- 状态：待核实
- 文件：`src/components/WhatsNewDialog.tsx:123`
- 结构：`WhatsNewDialog` / `dynamic_i18n_key`
- 原文/表达式：`whatsNew.types.${item.type}`
- 判定原因：翻译键由运行时表达式“`whatsNew.types.${item.type}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`3f85b3caaa1db65c266a4b88be6939885791f7c36060642eee5f98ac55453a1d`

### 12. `dynamic-i18n:src/components/apps/AppsPage.tsx:sections:88b10ec29471d286:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:217`
- 结构：`sections` / `dynamic_i18n_key`
- 原文/表达式：installed<br>                ? "appsPage.sectionInstalled"<br>                : "appsPage.sectionNotInstalled"
- 判定原因：翻译键由运行时表达式“installed
                ? "appsPage.sectionInstalled"
                : "appsPage.sectionNotInstalled"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`88b10ec29471d286f568d96fe5a96005b2e44592ebd16daef0c067f09d0b56d8`

### 13. `dynamic-i18n:src/components/apps/AppsPage.tsx:envBadge:cfc322af6c201189:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:749`
- 结构：`envBadge` / `dynamic_i18n_key`
- 原文/表达式：ENV_BADGE_CONFIG.wsl.labelKey
- 判定原因：翻译键由运行时表达式“ENV_BADGE_CONFIG.wsl.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cfc322af6c20118946129fe571601732b788bf744b7587675baf8f51ca169d3f`

### 14. `dynamic-i18n:src/components/apps/AppsPage.tsx:installHint:a7313ac9d3fdc954:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:801`
- 结构：`installHint` / `dynamic_i18n_key`
- 原文/表达式：`appsPage.installHint.${tool}`
- 判定原因：翻译键由运行时表达式“`appsPage.installHint.${tool}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a7313ac9d3fdc95467738f3e8d22bfc93d7f9b14c75fe5c47b7ec556ceb63883`

### 15. `dynamic-i18n:src/components/apps/useToolManagement.ts:executeRun:fa889cec796591ae:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:866`
- 结构：`executeRun` / `dynamic_i18n_key`
- 原文/表达式：action === "uninstall"<br>              ? "settings.toolUninstallFailed"<br>              : "settings.toolActionFailed"
- 判定原因：翻译键由运行时表达式“action === "uninstall"
              ? "settings.toolUninstallFailed"
              : "settings.toolActionFailed"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`fa889cec796591ae640bbcb93cd3e84c8957360cf229a01204a9f6db6f6cce7e`

### 16. `dynamic-i18n:src/components/deeplink/McpConfirmation.tsx:McpConfirmation:d7f7b8d4887c79a0:001`

- 状态：待核实
- 文件：`src/components/deeplink/McpConfirmation.tsx:161`
- 结构：`McpConfirmation` / `dynamic_i18n_key`
- 原文/表达式：riskI18nKey(kind)
- 判定原因：翻译键由运行时表达式“riskI18nKey(kind)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d7f7b8d4887c79a0de17ef5158c37ad4cf32609e660350c71f01326dd264af1d`

### 17. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:name:75356b9afb016217:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:119`
- 结构：`name` / `dynamic_i18n_key`
- 原文/表达式：meta.nameKey
- 判定原因：翻译键由运行时表达式“meta.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`75356b9afb01621774bc813d1d21c3f8a9da401b6627205fa24ff6106a671d06`

### 18. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:handleToggle:7663f326f8433d18:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:146`
- 结构：`handleToggle` / `dynamic_i18n_key`
- 原文/表达式：next ? "hermes.memory.toggledOn" : "hermes.memory.toggledOff"
- 判定原因：翻译键由运行时表达式“next ? "hermes.memory.toggledOn" : "hermes.memory.toggledOff"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`7663f326f8433d188375fc655defeac94f6915774b979d2dd3a14cbee2063eb1`

### 19. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:MemoryTabPane:8fb010723006dfa3:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:175`
- 结构：`MemoryTabPane` / `dynamic_i18n_key`
- 原文/表达式：meta.descKey
- 判定原因：翻译键由运行时表达式“meta.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8fb010723006dfa36c05d41cacd6c24d2b8cd98441b1c4cc824670f19b9bf700`

### 20. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:MemoryTabPane:51f6c463686ee31f:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:208`
- 结构：`MemoryTabPane` / `dynamic_i18n_key`
- 原文/表达式：meta.placeholderKey
- 判定原因：翻译键由运行时表达式“meta.placeholderKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`51f6c463686ee31f6081657b2c9e2ed0f07612d1b172800f059acf7475979176`

### 21. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:HermesMemoryPanel:43ecfa8432d123f8:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:300`
- 结构：`HermesMemoryPanel` / `dynamic_i18n_key`
- 原文/表达式：KIND_META[kind].nameKey
- 判定原因：翻译键由运行时表达式“KIND_META[kind].nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`43ecfa8432d123f8c6578042a3deaf5b4ce608d8c09b5f4e9b40bb7217247d31`

### 22. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:fieldErrorText:c2af3397f931d9d7:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:206`
- 结构：`fieldErrorText` / `dynamic_i18n_key`
- 原文/表达式：`mcpPage.drawer.errors.${code}`
- 判定原因：翻译键由运行时表达式“`mcpPage.drawer.errors.${code}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c2af3397f931d9d7d775675a0d91f651bfe460fa4b610fc2f28d156b68e06c23`

### 23. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:formatLabel:365b5da25b0130b9:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:210`
- 结构：`formatLabel` / `dynamic_i18n_key`
- 原文/表达式：`mcpPage.drawer.pasteFormats.${format}`
- 判定原因：翻译键由运行时表达式“`mcpPage.drawer.pasteFormats.${format}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`365b5da25b0130b97d4166f1b4ed9112b3781abb292013a91f5eb9c31b80b853`

### 24. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:McpFormModal:110e6c2fccad7e63:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:659`
- 结构：`McpFormModal` / `dynamic_i18n_key`
- 原文/表达式：`mcp.presets.${preset.id}.description`
- 判定原因：翻译键由运行时表达式“`mcp.presets.${preset.id}.description`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`110e6c2fccad7e63497c8d59fc75f0c8538d7d985c7020f437e6854c17fb8048`

### 25. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:McpFormModal:b38b4246acafdcdc:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:668`
- 结构：`McpFormModal` / `dynamic_i18n_key`
- 原文/表达式：`mcpPage.templateLabels.${preset.id}`
- 判定原因：翻译键由运行时表达式“`mcpPage.templateLabels.${preset.id}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b38b4246acafdcdcbc1a744cfaa372d515996efc14f9eed16a8aeeb457324b42`

### 26. `dynamic-i18n:src/components/mcp/UnifiedMcpPanel.tsx:UnifiedMcpPanel:947324ed6a00ba24:001`

- 状态：待核实
- 文件：`src/components/mcp/UnifiedMcpPanel.tsx:940`
- 结构：`UnifiedMcpPanel` / `dynamic_i18n_key`
- 原文/表达式：`appMatrix.cell.${state}`
- 判定原因：翻译键由运行时表达式“`appMatrix.cell.${state}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`947324ed6a00ba241dcc93e16c9b7022385f2e299608f805663901480e1d6454`

### 27. `dynamic-i18n:src/components/mcp/UnifiedMcpPanel.tsx:UnifiedMcpPanel:d9d6a85445fe9b7e:001`

- 状态：待核实
- 文件：`src/components/mcp/UnifiedMcpPanel.tsx:1143`
- 结构：`UnifiedMcpPanel` / `dynamic_i18n_key`
- 原文/表达式：IMPORT_SOURCE_FILES[app].noteKey as string
- 判定原因：翻译键由运行时表达式“IMPORT_SOURCE_FILES[app].noteKey as string”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d9d6a85445fe9b7e4c33f649bfe9bc029ac989a37e98f491405a5fb4c42718c1`

### 28. `dynamic-i18n:src/components/profiles/ProfileSwitcher.tsx:ProfileSwitcher:bf07f0e194763ea6:001`

- 状态：待核实
- 文件：`src/components/profiles/ProfileSwitcher.tsx:116`
- 结构：`ProfileSwitcher` / `dynamic_i18n_key`
- 原文/表达式：`profiles.switcherTooltip.${scope}`
- 判定原因：翻译键由运行时表达式“`profiles.switcherTooltip.${scope}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`bf07f0e194763ea621ddc1be1a0fa505b153e66da09a849dc06007c5051c8f33`

### 29. `dynamic-i18n:src/components/profiles/ProfileSwitcher.tsx:ProfileSwitcher:bf07f0e194763ea6:002`

- 状态：待核实
- 文件：`src/components/profiles/ProfileSwitcher.tsx:134`
- 结构：`ProfileSwitcher` / `dynamic_i18n_key`
- 原文/表达式：`profiles.switcherTooltip.${scope}`
- 判定原因：翻译键由运行时表达式“`profiles.switcherTooltip.${scope}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`bf07f0e194763ea621ddc1be1a0fa505b153e66da09a849dc06007c5051c8f33`

### 30. `dynamic-i18n:src/components/profiles/ProfileSwitcher.tsx:ProfileSwitcher:1ea05b4ee91472f2:001`

- 状态：待核实
- 文件：`src/components/profiles/ProfileSwitcher.tsx:223`
- 结构：`ProfileSwitcher` / `dynamic_i18n_key`
- 原文/表达式：`profiles.createDescription.${scope}`
- 判定原因：翻译键由运行时表达式“`profiles.createDescription.${scope}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1ea05b4ee91472f2dff58eae1a3185cc82d499fe00c348b089dcb152ba5846d9`

### 31. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiInstructionFileEditor:d1d3865d992378c2:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:211`
- 结构：`PiInstructionFileEditor` / `dynamic_i18n_key`
- 原文/表达式：baseSnapshot.exists ? "pi.prompts.editFile" : "pi.prompts.createFile"
- 判定原因：翻译键由运行时表达式“baseSnapshot.exists ? "pi.prompts.editFile" : "pi.prompts.createFile"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d1d3865d992378c2b2bccf4e7c7e5a7a63e0e9b4c9a15f1f6a3dfb1556b659ad`

### 32. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiInstructionFileEditor:a8bc05c127159b54:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:215`
- 结构：`PiInstructionFileEditor` / `dynamic_i18n_key`
- 原文/表达式：file.descriptionKey
- 判定原因：翻译键由运行时表达式“file.descriptionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a8bc05c127159b54db39e473aad743e323f90addf0132138f3359fdbb38ed938`

### 33. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:remove:2694dcf2980c7a5b:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:364`
- 结构：`remove` / `dynamic_i18n_key`
- 原文/表达式：kind === "system_append"<br>            ? "pi.prompts.appendDeleted"<br>            : "pi.prompts.overrideDeleted"
- 判定原因：翻译键由运行时表达式“kind === "system_append"
            ? "pi.prompts.appendDeleted"
            : "pi.prompts.overrideDeleted"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2694dcf2980c7a5b68bf9278cc0cc3aa0c18f8df9a8db46941aab0a51f5aaf21`

### 34. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:remove:ccfd4aa37ca34de2:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:369`
- 结构：`remove` / `dynamic_i18n_key`
- 原文/表达式：blank ? "pi.prompts.deletedBlank" : "pi.prompts.deletedUndoable"
- 判定原因：翻译键由运行时表达式“blank ? "pi.prompts.deletedBlank" : "pi.prompts.deletedUndoable"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ccfd4aa37ca34de27182837641d46f3d97b72638cf56508f3b2c0893d2a3f1c7`

### 35. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:d1d85835cac8c3b6:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:426`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：file.titleKey
- 判定原因：翻译键由运行时表达式“file.titleKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d1d85835cac8c3b67f8f2f2788b521e0f56e6f85bb64f0c5165d5a1e0aeb709c`

### 36. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:a8bc05c127159b54:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:438`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：file.descriptionKey
- 判定原因：翻译键由运行时表达式“file.descriptionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a8bc05c127159b54db39e473aad743e323f90addf0132138f3359fdbb38ed938`

### 37. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:c2b9bd028b119153:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:478`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：data?.exists ? "common.edit" : "pi.prompts.create"
- 判定原因：翻译键由运行时表达式“data?.exists ? "common.edit" : "pi.prompts.create"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c2b9bd028b119153842868de21081c0165efb2f1275c7679450a3e836ce7acc2`

### 38. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:c2b9bd028b119153:002`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:483`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：data?.exists ? "common.edit" : "pi.prompts.create"
- 判定原因：翻译键由运行时表达式“data?.exists ? "common.edit" : "pi.prompts.create"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c2b9bd028b119153842868de21081c0165efb2f1275c7679450a3e836ce7acc2`

### 39. `dynamic-i18n:src/components/prompts/PromptFormPanel.tsx:nameError:faa60122c7dfa55e:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptFormPanel.tsx:88`
- 结构：`nameError` / `dynamic_i18n_key`
- 原文/表达式：isHermes ? "prompts.nameRequiredHermes" : "prompts.nameRequired"
- 判定原因：翻译键由运行时表达式“isHermes ? "prompts.nameRequiredHermes" : "prompts.nameRequired"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`faa60122c7dfa55e3d3a53f6e70596a0f33d1536751571c46698a866921d592a`

### 40. `dynamic-i18n:src/components/prompts/PromptFormPanel.tsx:PromptFormPanel:f3ffc31bc1e64a97:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptFormPanel.tsx:195`
- 结构：`PromptFormPanel` / `dynamic_i18n_key`
- 原文/表达式：isHermes<br>                  ? "prompts.namePlaceholderHermes"<br>                  : "prompts.namePlaceholder"
- 判定原因：翻译键由运行时表达式“isHermes
                  ? "prompts.namePlaceholderHermes"
                  : "prompts.namePlaceholder"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`f3ffc31bc1e64a97df4252231320a3fcbf6176b203f6aaa490901d73d22c516b`

### 41. `dynamic-i18n:src/components/prompts/PromptListItem.tsx:PromptListItem:d12e0500610428ba:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptListItem.tsx:94`
- 结构：`PromptListItem` / `dynamic_i18n_key`
- 原文/表达式：active ? "prompts.disableAria" : "prompts.enableAria"
- 判定原因：翻译键由运行时表达式“active ? "prompts.disableAria" : "prompts.enableAria"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d12e0500610428ba236c01a7b5b70cb4bb9387f9d55be2e6f8336a0a27c8d701`

### 42. `dynamic-i18n:src/components/prompts/PromptListItem.tsx:PromptListItem:cccf9c2fec5053e8:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptListItem.tsx:100`
- 结构：`PromptListItem` / `dynamic_i18n_key`
- 原文/表达式：active ? "prompts.disable" : "prompts.enable"
- 判定原因：翻译键由运行时表达式“active ? "prompts.disable" : "prompts.enable"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cccf9c2fec5053e836d0753b9ded96c4bc796bd449169bb2b71f8b2a7d7563ee`

### 43. `dynamic-i18n:src/components/prompts/usePromptPageCommon.ts:toggleEffectText:2225c982a3afe1fa:001`

- 状态：待核实
- 文件：`src/components/prompts/usePromptPageCommon.ts:64`
- 结构：`toggleEffectText` / `dynamic_i18n_key`
- 原文/表达式：enabled ? "prompts.toast.hermesOn" : "prompts.toast.hermesOff"
- 判定原因：翻译键由运行时表达式“enabled ? "prompts.toast.hermesOn" : "prompts.toast.hermesOff"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2225c982a3afe1fa729c3e536e1e1a979ce749d11b999cd756c04e76010b864e`

### 44. `dynamic-i18n:src/components/providers/CodexStaleClientsNotice.tsx:CodexStaleClientsNotice:d73fd9997e52d916:001`

- 状态：待核实
- 文件：`src/components/providers/CodexStaleClientsNotice.tsx:41`
- 结构：`CodexStaleClientsNotice` / `dynamic_i18n_key`
- 原文/表达式：staleClients.unverified<br>            ? "proxy.stackMode.codexStale.unverifiedTitle"<br>            : staleClients.auth<br>              ? "proxy.stackMode.codexStale.authTitle"<br>              : "proxy.stackMode.codexStale.title"
- 判定原因：翻译键由运行时表达式“staleClients.unverified
            ? "proxy.stackMode.codexStale.unverifiedTitle"
            : staleClients.auth
              ? "proxy.stackMode.codexStale.authTitle"
              : "proxy.stackMode.codexStale.title"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d73fd9997e52d9166bc866e5fd9b0b3c1d44ac8984866401a169617dc52a58ba`

### 45. `dynamic-i18n:src/components/providers/KimiAccountLogin.tsx:rows:0efcbaf86f008873:001`

- 状态：待核实
- 文件：`src/components/providers/KimiAccountLogin.tsx:57`
- 结构：`rows` / `dynamic_i18n_key`
- 原文/表达式：`kimi.oauth.${account.region}`
- 判定原因：翻译键由运行时表达式“`kimi.oauth.${account.region}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0efcbaf86f008873c4d489f263f1364693f9365f17d54a5affa885bc16d319ce`

### 46. `dynamic-i18n:src/components/providers/KimiAccountLogin.tsx:KimiAccountLogin:60eddd19f0eccda0:001`

- 状态：待核实
- 文件：`src/components/providers/KimiAccountLogin.tsx:181`
- 结构：`KimiAccountLogin` / `dynamic_i18n_key`
- 原文/表达式：confirmRemove?.primary<br>            ? "kimi.oauth.dismissConfirm"<br>            : "kimi.oauth.removeConfirm"
- 判定原因：翻译键由运行时表达式“confirmRemove?.primary
            ? "kimi.oauth.dismissConfirm"
            : "kimi.oauth.removeConfirm"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`60eddd19f0eccda058adeaa2c3e9a655c911ebeead5456d6d804ab83c09df438`

### 47. `dynamic-i18n:src/components/providers/OpenTerminalDialog.tsx:OpenTerminalDialog:2b72580d648a686e:001`

- 状态：待核实
- 文件：`src/components/providers/OpenTerminalDialog.tsx:229`
- 结构：`OpenTerminalDialog` / `dynamic_i18n_key`
- 原文/表达式：appId === "agy"<br>                  ? "provider.openTerminalDialog.isolationBodyAgy"<br>                  : "provider.openTerminalDialog.isolationBody"
- 判定原因：翻译键由运行时表达式“appId === "agy"
                  ? "provider.openTerminalDialog.isolationBodyAgy"
                  : "provider.openTerminalDialog.isolationBody"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2b72580d648a686e9dc1aec6062a1426f4846e75d1b70575e8367e15cdc80191`

### 48. `dynamic-i18n:src/components/providers/ProviderCardActions.tsx:ProviderCardActions:7ac214e2da017a6c:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderCardActions.tsx:158`
- 结构：`ProviderCardActions` / `dynamic_i18n_key`
- 原文/表达式：openTerminalIsolated<br>              ? "provider.openTerminalIsolated"<br>              : "provider.openTerminal"
- 判定原因：翻译键由运行时表达式“openTerminalIsolated
              ? "provider.openTerminalIsolated"
              : "provider.openTerminal"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`7ac214e2da017a6c1b84811e286de7467d81e7caad956ec541a998c3b9feae32`

### 49. `dynamic-i18n:src/components/providers/ProviderEmptyState.tsx:ProviderEmptyState:4fd05547609ab33c:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderEmptyState.tsx:48`
- 结构：`ProviderEmptyState` / `dynamic_i18n_key`
- 原文/表达式：`${emptyCopyNs}.empty.title`
- 判定原因：翻译键由运行时表达式“`${emptyCopyNs}.empty.title`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4fd05547609ab33c012446250b5baabb5d65423449887ded7798685c2db0ac23`

### 50. `dynamic-i18n:src/components/providers/ProviderEmptyState.tsx:ProviderEmptyState:bc32d0931c886d14:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderEmptyState.tsx:53`
- 结构：`ProviderEmptyState` / `dynamic_i18n_key`
- 原文/表达式：`${emptyCopyNs}.empty.description`
- 判定原因：翻译键由运行时表达式“`${emptyCopyNs}.empty.description`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`bc32d0931c886d1458a2a0bd5842a0a6ad3d9111fcc8f94afb58fce2c34b9cc2`

### 51. `dynamic-i18n:src/components/providers/ProviderList.tsx:piStateErrorNotice:a72c91773a926bd1:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderList.tsx:430`
- 结构：`piStateErrorNotice` / `dynamic_i18n_key`
- 原文/表达式：`${appId}.current.readFailed`
- 判定原因：翻译键由运行时表达式“`${appId}.current.readFailed`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a72c91773a926bd1ce4dfba5624c1fde35704374ba5763f5af939dafeae59e89`

### 52. `dynamic-i18n:src/components/providers/ProviderList.tsx:piStateErrorNotice:cae9391778824b2d:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderList.tsx:434`
- 结构：`piStateErrorNotice` / `dynamic_i18n_key`
- 原文/表达式：`${appId}.current.stateUnavailableHint`
- 判定原因：翻译键由运行时表达式“`${appId}.current.stateUnavailableHint`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cae9391778824b2dd2e838af86052a9d7821c0f2c504040533cfc169215b346f`

### 53. `dynamic-i18n:src/components/providers/forms/ClaudeDesktopProviderForm.tsx:applyDesktopPreset:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ClaudeDesktopProviderForm.tsx:433`
- 结构：`applyDesktopPreset` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 54. `dynamic-i18n:src/components/providers/forms/CodexConfigSections.tsx:CodexAuthSection:b3aada018c964656:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CodexConfigSections.tsx:88`
- 结构：`CodexAuthSection` / `dynamic_i18n_key`
- 原文/表达式：isProxyTakeover<br>              ? "codexConfig.authJsonStorageHint"<br>              : "codexConfig.authJsonHint"
- 判定原因：翻译键由运行时表达式“isProxyTakeover
              ? "codexConfig.authJsonStorageHint"
              : "codexConfig.authJsonHint"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b3aada018c9646567d82bd28483431f01c8c1f84ba059e56e31f30ceae8f9526`

### 55. `dynamic-i18n:src/components/providers/forms/CodexConfigSections.tsx:CodexConfigSection:75b82bc2e41ebdef:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CodexConfigSections.tsx:332`
- 结构：`CodexConfigSection` / `dynamic_i18n_key`
- 原文/表达式：isProxyTakeover<br>              ? "codexConfig.configTomlStorageHint"<br>              : "codexConfig.configTomlHint"
- 判定原因：翻译键由运行时表达式“isProxyTakeover
              ? "codexConfig.configTomlStorageHint"
              : "codexConfig.configTomlHint"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`75b82bc2e41ebdefa9c594cf29c7ed0b183d2c95564d04b358fb9f2fc717219d`

### 56. `dynamic-i18n:src/components/providers/forms/CommonConfigEditor.tsx:CommonConfigEditor:e626f805fbbd0918:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CommonConfigEditor.tsx:226`
- 结构：`CommonConfigEditor` / `dynamic_i18n_key`
- 原文/表达式：`claudeConfig.${key}`
- 判定原因：翻译键由运行时表达式“`claudeConfig.${key}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e626f805fbbd09186fcb572b913402ca4b8698bdec50eec0cd3c29ef2a6c32ef`

### 57. `dynamic-i18n:src/components/providers/forms/CommonConfigEditor.tsx:CommonConfigEditor:e626f805fbbd0918:002`

- 状态：待核实
- 文件：`src/components/providers/forms/CommonConfigEditor.tsx:228`
- 结构：`CommonConfigEditor` / `dynamic_i18n_key`
- 原文/表达式：`claudeConfig.${key}`
- 判定原因：翻译键由运行时表达式“`claudeConfig.${key}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e626f805fbbd09186fcb572b913402ca4b8698bdec50eec0cd3c29ef2a6c32ef`

### 58. `dynamic-i18n:src/components/providers/forms/CommonConfigEditor.tsx:CommonConfigEditor:6441eb22cfc8b522:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CommonConfigEditor.tsx:229`
- 结构：`CommonConfigEditor` / `dynamic_i18n_key`
- 原文/表达式：`claudeConfig.${key}Help`
- 判定原因：翻译键由运行时表达式“`claudeConfig.${key}Help`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`6441eb22cfc8b522bfba7d8d0ed5fc65dfa2d164e6f833b9aa2f50ef602eb05a`

### 59. `dynamic-i18n:src/components/providers/forms/GrokBuildProviderForm.tsx:presetName:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/GrokBuildProviderForm.tsx:280`
- 结构：`presetName` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 60. `dynamic-i18n:src/components/providers/forms/HermesFormFields.tsx:baseUrlErrorMessage:5eb171ca5f27c5ee:001`

- 状态：待核实
- 文件：`src/components/providers/forms/HermesFormFields.tsx:113`
- 结构：`baseUrlErrorMessage` / `dynamic_i18n_key`
- 原文/表达式：BASE_URL_ERROR_I18N_KEY[baseUrlErrorCode]
- 判定原因：翻译键由运行时表达式“BASE_URL_ERROR_I18N_KEY[baseUrlErrorCode]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5eb171ca5f27c5eefd4e8e2757583c5a23cbb1c00f52b6199b1c9b5d91e475ef`

### 61. `dynamic-i18n:src/components/providers/forms/HermesFormFields.tsx:HermesFormFields:ebd78379247b5bd6:001`

- 状态：待核实
- 文件：`src/components/providers/forms/HermesFormFields.tsx:239`
- 结构：`HermesFormFields` / `dynamic_i18n_key`
- 原文/表达式：mode.labelKey
- 判定原因：翻译键由运行时表达式“mode.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ebd78379247b5bd6b2d34410f886a2e98d012497dd589d92dcc1ae28e9ef5f47`

### 62. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:presetSelector:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:417`
- 结构：`presetSelector` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 63. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:KimiProviderForm:450a277c2780a76f:001`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:766`
- 结构：`KimiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`kimi.capabilities.${capability}`
- 判定原因：翻译键由运行时表达式“`kimi.capabilities.${capability}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`450a277c2780a76f8de37a14ed429c00fd2d7306f903bbdd718ab732baf89402`

### 64. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:KimiProviderForm:450a277c2780a76f:002`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:770`
- 结构：`KimiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`kimi.capabilities.${capability}`
- 判定原因：翻译键由运行时表达式“`kimi.capabilities.${capability}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`450a277c2780a76f8de37a14ed429c00fd2d7306f903bbdd718ab732baf89402`

### 65. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:KimiProviderForm:c76f11a5e2460403:001`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:772`
- 结构：`KimiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`kimi.capabilityHints.${capability}`
- 判定原因：翻译键由运行时表达式“`kimi.capabilityHints.${capability}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c76f11a5e24604034bcd0d3ff1a6d6fb8e3802b27e31cd08ef6989f5a8bdfeeb`

### 66. `dynamic-i18n:src/components/providers/forms/OmoFormFields.tsx:renderBuiltinModelRow:f19573ea4c8f34d1:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:921`
- 结构：`renderBuiltinModelRow` / `dynamic_i18n_key`
- 原文/表达式：def.tooltipKey
- 判定原因：翻译键由运行时表达式“def.tooltipKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`f19573ea4c8f34d16ed290a159139f8c4f9d8a6b2d57ba15b5a4226f48405124`

### 67. `dynamic-i18n:src/components/providers/forms/OmoFormFields.tsx:renderBuiltinModelRow:2b3d6a81dfe0d684:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:925`
- 结构：`renderBuiltinModelRow` / `dynamic_i18n_key`
- 原文/表达式：def.descKey
- 判定原因：翻译键由运行时表达式“def.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2b3d6a81dfe0d68451cced7796ce01f17ea2304cfb282b8757154b5060f88179`

### 68. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:001`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:1997`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 69. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:002`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2005`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 70. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:003`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2048`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 71. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:004`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2124`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 72. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:132a666b0f252c49:001`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2213`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`omp.form.discoveryTypes.${labelKey}`
- 判定原因：翻译键由运行时表达式“`omp.form.discoveryTypes.${labelKey}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`132a666b0f252c49eb4a518979481806f7535319d4b1a4cae4bbd0deb0f020f2`

### 73. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handleSubmit:b107d3ee7afe31c4:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:1366`
- 结构：`handleSubmit` / `dynamic_i18n_key`
- 原文/表达式：isNativeOpencode<br>                ? "opencode.nativeCustomProviderRequired"<br>                : "opencode.customProviderRequired"
- 判定原因：翻译键由运行时表达式“isNativeOpencode
                ? "opencode.nativeCustomProviderRequired"
                : "opencode.customProviderRequired"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b107d3ee7afe31c4b51579ab7b942989ba2965c7bb37cbbfdc0073bda4d45245`

### 74. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:presetName:70b8f41adf91a088:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:1850`
- 结构：`presetName` / `dynamic_i18n_key`
- 原文/表达式：selectedPresetEntry.preset.nameKey
- 判定原因：翻译键由运行时表达式“selectedPresetEntry.preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`70b8f41adf91a088b81d19e95c1b202946fb7b5f85d9dde92ed37cafbf0718b0`

### 75. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2245`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 76. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:002`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2271`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 77. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:003`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2300`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 78. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:004`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2327`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 79. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:005`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2344`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 80. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:006`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2380`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 81. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:ProviderFormFull:2929691ef61b6b98:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2593`
- 结构：`ProviderFormFull` / `dynamic_i18n_key`
- 原文/表达式：isProviderKeyLocked<br>                          ? "hermes.form.providerKeyBuiltinLocked"<br>                          : "hermes.form.providerKeyBuiltin"
- 判定原因：翻译键由运行时表达式“isProviderKeyLocked
                          ? "hermes.form.providerKeyBuiltinLocked"
                          : "hermes.form.providerKeyBuiltin"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2929691ef61b6b98ba7850f932d6ab6ed43068e48450fa0d7e0b9ef50912f295`

### 82. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:PresetPicker:2ecf60adfaf48d3d:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:697`
- 结构：`PresetPicker` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.group.${key}`
- 判定原因：翻译键由运行时表达式“`providerPreset.group.${key}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2ecf60adfaf48d3d178598391a5edcfb21b0b69b7e6065cf8e11a0889b2e42c8`

### 83. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:PresetPicker:4449886f332aee87:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:724`
- 结构：`PresetPicker` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.groupHint.${category}`
- 判定原因：翻译键由运行时表达式“`providerPreset.groupHint.${category}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4449886f332aee87414a8ce0440ca4bc27fab6e67a88ccd42680c8db56b7c721`

### 84. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:PresetPicker:d66617847d5d3184:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:788`
- 结构：`PresetPicker` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.group.${section.group}`
- 判定原因：翻译键由运行时表达式“`providerPreset.group.${section.group}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d66617847d5d31849ee9eda8fb528297c5c5dfb871a7ceabcc81f0f1bd37ce06`

### 85. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:presetRowDetail:1ef66cb0a07d81d7:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:830`
- 结构：`presetRowDetail` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.loginWith.${loginAccountKey(appId, first.preset)}`
- 判定原因：翻译键由运行时表达式“`providerPreset.loginWith.${loginAccountKey(appId, first.preset)}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1ef66cb0a07d81d78c015661ad1c310dc8cab09720e08dd47e36ce6c29953f61`

### 86. `dynamic-i18n:src/components/providers/forms/hooks/useKimiOAuth.ts:poll:54e9f1fe2ffcfff0:001`

- 状态：待核实
- 文件：`src/components/providers/forms/hooks/useKimiOAuth.ts:97`
- 结构：`poll` / `dynamic_i18n_key`
- 原文/表达式：`kimi.oauth.${result.ended}`
- 判定原因：翻译键由运行时表达式“`kimi.oauth.${result.ended}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`54e9f1fe2ffcfff049ba8449c17135b0df6090267d74cc0de907ad199e1ffe7e`

### 87. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:presetDisplayName:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:87`
- 结构：`presetDisplayName` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 88. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:familyDisplayName:68cf4bfef554bafb:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:209`
- 结构：`familyDisplayName` / `dynamic_i18n_key`
- 原文/表达式：info.nameKey
- 判定原因：翻译键由运行时表达式“info.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`68cf4bfef554bafbbd4e399d25b37bd8e3bb6897a13d8ac9002f1a43095def2a`

### 89. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:presetPlanLabel:0e82ff606c3fadd8:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:219`
- 结构：`presetPlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.plan.${plan}`
- 判定原因：翻译键由运行时表达式“`providerPreset.plan.${plan}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0e82ff606c3fadd8ea8cb6573f83fc7fc69e4f4d6bf6f49f625112a4e0dc6fd3`

### 90. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:presetRegionLabel:ad2da87a36c33418:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:226`
- 结构：`presetRegionLabel` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.region.${region}`
- 判定原因：翻译键由运行时表达式“`providerPreset.region.${region}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ad2da87a36c334182cc13e04e16921b7c57d3a7ef14cc3ca7bf8141dfb6c050f`

### 91. `dynamic-i18n:src/components/providers/forms/shared/ApiKeySection.tsx:promotion:8c26f1886f0b1401:001`

- 状态：待核实
- 文件：`src/components/providers/forms/shared/ApiKeySection.tsx:60`
- 结构：`promotion` / `dynamic_i18n_key`
- 原文/表达式：`providerForm.partnerPromotion.${partnerPromotionKey}`
- 判定原因：翻译键由运行时表达式“`providerForm.partnerPromotion.${partnerPromotionKey}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8c26f1886f0b14011ff0e721dfc8edb5f48c997d1bc53b50eb2204d9dc05337d`

### 92. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:EnterBody:fcdbad57bad3a97a:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:226`
- 结构：`EnterBody` / `dynamic_i18n_key`
- 原文/表达式：app === "claude-desktop"<br>          ? "mode.dialog.desktopLeaveStackNote"<br>          : "mode.dialog.leaveStackNote"
- 判定原因：翻译键由运行时表达式“app === "claude-desktop"
          ? "mode.dialog.desktopLeaveStackNote"
          : "mode.dialog.leaveStackNote"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`fcdbad57bad3a97ac6e8007e336743ca8e1a7d6efa7637892d6a308e499ebcc9`

### 93. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:targetName:9a6e6056bc68a344:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:249`
- 结构：`targetName` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${target}`
- 判定原因：翻译键由运行时表达式“`mode.names.${target}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`9a6e6056bc68a34442b51307c97d01a3e76078bb220dcf7407babd52712f33fc`

### 94. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:title:63b0f1c3e4f1b584:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:253`
- 结构：`title` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 95. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:ExitBody:63b0f1c3e4f1b584:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:427`
- 结构：`ExitBody` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 96. `dynamic-i18n:src/components/providers/mode/ModeTabs.tsx:ModeTabs:8594999185d253ca:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeTabs.tsx:117`
- 结构：`ModeTabs` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${mode}`
- 判定原因：翻译键由运行时表达式“`mode.names.${mode}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8594999185d253cac67012cdf03429a7ec6a6ed8cb4300166ad5416582da216c`

### 97. `dynamic-i18n:src/components/providers/mode/ModeTabs.tsx:ModeTabs:37635fc3d0ebe24c:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeTabs.tsx:135`
- 结构：`ModeTabs` / `dynamic_i18n_key`
- 原文/表达式：`mode.help.${mode}`
- 判定原因：翻译键由运行时表达式“`mode.help.${mode}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`37635fc3d0ebe24c450c409de557a403a6c39ba395160f060bc6ccec166eb53e`

### 98. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:63b0f1c3e4f1b584:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:384`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 99. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:3ccf2e312468eabd:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:429`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${startupFailure.stack ? "stack" : "route"}`
- 判定原因：翻译键由运行时表达式“`mode.names.${startupFailure.stack ? "stack" : "route"}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`3ccf2e312468eabdf00e60d92ec7776db283fd6d7e87cfc7b634be1f206a230f`

### 100. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:b01ceb686ee7b005:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:467`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`provider.${stack.notice}`
- 判定原因：翻译键由运行时表达式“`provider.${stack.notice}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b01ceb686ee7b00588f9215bbf65e9ac8c98db79940c176eae397729fbabcfda`

### 101. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:814432bf883e93e6:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:484`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`provider.officialModelsReason.${reason}`
- 判定原因：翻译键由运行时表达式“`provider.officialModelsReason.${reason}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`814432bf883e93e6bcf7f75f4854fd3f7eacbd30847844d2868e8d7483ae4975`

### 102. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:5183420e5cea98fb:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:517`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${view}`
- 判定原因：翻译键由运行时表达式“`mode.names.${view}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5183420e5cea98fb0fba783012ad5279a99efc3025b661f1e77f4545e14792a3`

### 103. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:63b0f1c3e4f1b584:002`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:519`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 104. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:63b0f1c3e4f1b584:003`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:570`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 105. `dynamic-i18n:src/components/providers/presentation.ts:buildSwitchSectionsByView:952b41156d70dc1d:001`

- 状态：待核实
- 文件：`src/components/providers/presentation.ts:616`
- 结构：`buildSwitchSectionsByView` / `dynamic_i18n_key`
- 原文/表达式：app === "claude-desktop"<br>            ? "providerCard.section.stackDefaultHelpDesktop"<br>            : "providerCard.section.stackDefaultHelp"
- 判定原因：翻译键由运行时表达式“app === "claude-desktop"
            ? "providerCard.section.stackDefaultHelpDesktop"
            : "providerCard.section.stackDefaultHelp"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`952b41156d70dc1d49a2d578ee40bb60dd986a77bde5c2714e92e76f7095b93f`

### 106. `dynamic-i18n:src/components/providers/presentation.ts:piBlocked:770eceac0b7cd3f8:001`

- 状态：待核实
- 文件：`src/components/providers/presentation.ts:717`
- 结构：`piBlocked` / `dynamic_i18n_key`
- 原文/表达式：`${app}.current.stateUnavailableHint`
- 判定原因：翻译键由运行时表达式“`${app}.current.stateUnavailableHint`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`770eceac0b7cd3f834ccbb1e0089fc40822d920a9092c85a9fdb59d52b54946a`

### 107. `dynamic-i18n:src/components/providers/presentation.ts:buildAdditiveSections:2eb4a51baae54d37:001`

- 状态：待核实
- 文件：`src/components/providers/presentation.ts:957`
- 结构：`buildAdditiveSections` / `dynamic_i18n_key`
- 原文/表达式：`apps.${app}`
- 判定原因：翻译键由运行时表达式“`apps.${app}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2eb4a51baae54d37ab7eb80531cacac553f173e0b41fa7516dd5b8ce6e6e5ef3`

### 108. `dynamic-i18n:src/components/quota/quotaRules.ts:tierLine:02df858ef720e28a:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:138`
- 结构：`tierLine` / `dynamic_i18n_key`
- 原文/表达式：used ? "quota.tierUsed" : "quota.tierLeft"
- 判定原因：翻译键由运行时表达式“used ? "quota.tierUsed" : "quota.tierLeft"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`02df858ef720e28a4a4700bfa3a586d2aa0d1d78d213ecaba83e2595ca282025`

### 109. `dynamic-i18n:src/components/quota/quotaRules.ts:tierLine:b5286d080dc232bd:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:145`
- 结构：`tierLine` / `dynamic_i18n_key`
- 原文/表达式：used ? "quota.used" : "quota.left"
- 判定原因：翻译键由运行时表达式“used ? "quota.used" : "quota.left"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b5286d080dc232bde98cb700bc4010de3f717b23353e15e6964b735a20805ed0`

### 110. `dynamic-i18n:src/components/sessions/SessionItem.tsx:deleteReason:26c0854586264f75:001`

- 状态：待核实
- 文件：`src/components/sessions/SessionItem.tsx:108`
- 结构：`deleteReason` / `dynamic_i18n_key`
- 原文/表达式：session.providerId === "dsh"<br>          ? "dsh.deleteSessionHint"<br>          : session.providerId === "kimi"<br>            ? "kimi.deleteSessionHint"<br>            : session.providerId === "agy"<br>              ? "sessionManager.agyDeleteHint"<br>              : "sessionManager.mcodeDeleteHint"
- 判定原因：翻译键由运行时表达式“session.providerId === "dsh"
          ? "dsh.deleteSessionHint"
          : session.providerId === "kimi"
            ? "kimi.deleteSessionHint"
            : session.providerId === "agy"
              ? "sessionManager.agyDeleteHint"
              : "sessionManager.mcodeDeleteHint"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`26c0854586264f752701894181ddf6d23aecb1ec93d6ea585477f07fc2fbe360`

### 111. `dynamic-i18n:src/components/sessions/SessionManagerPage.tsx:label:2c70e12b7a0646f9:001`

- 状态：待核实
- 文件：`src/components/sessions/SessionManagerPage.tsx:312`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：key
- 判定原因：翻译键由运行时表达式“key”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683`

### 112. `dynamic-i18n:src/components/sessions/reader/SessionReaderHeader.tsx:moreMenu:d9527cde90f33c89:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionReaderHeader.tsx:356`
- 结构：`moreMenu` / `dynamic_i18n_key`
- 原文/表达式：session.providerId === "dsh"<br>                  ? "dsh.deleteSessionHint"<br>                  : session.providerId === "kimi"<br>                    ? "kimi.deleteSessionHint"<br>                    : "sessionManager.mcodeDeleteHint"
- 判定原因：翻译键由运行时表达式“session.providerId === "dsh"
                  ? "dsh.deleteSessionHint"
                  : session.providerId === "kimi"
                    ? "kimi.deleteSessionHint"
                    : "sessionManager.mcodeDeleteHint"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d9527cde90f33c89aeeb4eb07036bd5ecbb43b2f6c1101f44481b72606a54dc0`

### 113. `dynamic-i18n:src/components/sessions/reader/exportMarkdown.ts:metaText:05aec9f0cd39e139:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:34`
- 结构：`metaText` / `dynamic_i18n_key`
- 原文/表达式：`status.${meta.status}`
- 判定原因：翻译键由运行时表达式“`status.${meta.status}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`05aec9f0cd39e139e2c75e1ead486816b6f6841d8684ba2eee6364e52bab6605`

### 114. `dynamic-i18n:src/components/sessions/reader/exportMarkdown.ts:label:741390bbafe0c1e5:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:80`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：style.thinkingLabelKey
- 判定原因：翻译键由运行时表达式“style.thinkingLabelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`741390bbafe0c1e585378ac0ca539a88bc64feaaf4716b3d5cfd23aa308d3d3e`

### 115. `dynamic-i18n:src/components/sessions/reader/i18n.ts:useReaderT:a18b869b2e81c0c5:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/i18n.ts:140`
- 结构：`useReaderT` / `dynamic_i18n_key`
- 原文/表达式：full
- 判定原因：翻译键由运行时表达式“full”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a18b869b2e81c0c529552a3c4fa5c92ed08b98a4e146aed778d71d27517f83ac`

### 116. `dynamic-i18n:src/components/sessions/reader/toolSummary.ts:translate:982d9e3eb996f559:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:199`
- 结构：`translate` / `dynamic_i18n_key`
- 原文/表达式：text
- 判定原因：翻译键由运行时表达式“text”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`982d9e3eb996f559e633f4d194def3761d909f5a3b647d1a851fead67c32c9d1`

### 117. `dynamic-i18n:src/components/sessions/reader/toolSummary.ts:verbFor:6806f86a17f0ae04:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:209`
- 结构：`verbFor` / `dynamic_i18n_key`
- 原文/表达式：verb
- 判定原因：翻译键由运行时表达式“verb”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`6806f86a17f0ae04d4ad43168fcdd0651c0fe99108b992f5ac398fd6bf235331`

### 118. `dynamic-i18n:src/components/sessions/reader/toolSummary.ts:verb:5c4db77b4c3c9984:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:238`
- 结构：`verb` / `dynamic_i18n_key`
- 原文/表达式：TOOL_OUTPUT_VERB_KEY
- 判定原因：翻译键由运行时表达式“TOOL_OUTPUT_VERB_KEY”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5c4db77b4c3c9984f81b88ec4d1935af79d93dbff11ff45ed52e6b1bad5367cd`

### 119. `dynamic-i18n:src/components/settings/BackupStorageSection.tsx:itemText:1db9123095e31b5b:001`

- 状态：待核实
- 文件：`src/components/settings/BackupStorageSection.tsx:42`
- 结构：`itemText` / `dynamic_i18n_key`
- 原文/表达式：`settings.backupStorage.items.${id}.${field}`
- 判定原因：翻译键由运行时表达式“`settings.backupStorage.items.${id}.${field}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1db9123095e31b5b30ec9699f3437bc8d9c7d606a90aec7540d6385f5dbc7a4b`

### 120. `dynamic-i18n:src/components/settings/LogConfigPanel.tsx:LogConfigPanel:691fd4ccfbfb6e21:001`

- 状态：待核实
- 文件：`src/components/settings/LogConfigPanel.tsx:77`
- 结构：`LogConfigPanel` / `dynamic_i18n_key`
- 原文/表达式：`settings.advanced.logConfig.levelDesc.${level}`
- 判定原因：翻译键由运行时表达式“`settings.advanced.logConfig.levelDesc.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`691fd4ccfbfb6e213cc678ea12ea362afcd31bfe554a65c2abf797e955ae447f`

### 121. `dynamic-i18n:src/components/settings/LogConfigPanel.tsx:LogConfigPanel:e46dabee057f30b0:001`

- 状态：待核实
- 文件：`src/components/settings/LogConfigPanel.tsx:96`
- 结构：`LogConfigPanel` / `dynamic_i18n_key`
- 原文/表达式：`settings.advanced.logConfig.levels.${level}`
- 判定原因：翻译键由运行时表达式“`settings.advanced.logConfig.levels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e46dabee057f30b06ec7ba0d6a7aebd30d52cc0534c78db0434225c4a053bacd`

### 122. `dynamic-i18n:src/components/settings/SettingsPage.tsx:SettingsPage:73080ad588a22bcf:001`

- 状态：待核实
- 文件：`src/components/settings/SettingsPage.tsx:533`
- 结构：`SettingsPage` / `dynamic_i18n_key`
- 原文/表达式：`settings.sections.${section}`
- 判定原因：翻译键由运行时表达式“`settings.sections.${section}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`73080ad588a22bcf793b9900af2a25a37aa84db57382a48713b1575b878c240e`

### 123. `dynamic-i18n:src/components/settings/TerminalSettings.tsx:TerminalSelect:79a386948d425aae:001`

- 状态：待核实
- 文件：`src/components/settings/TerminalSettings.tsx:103`
- 结构：`TerminalSelect` / `dynamic_i18n_key`
- 原文/表达式：terminal.labelKey
- 判定原因：翻译键由运行时表达式“terminal.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`79a386948d425aae95f190e7a841c98ef62a40bb6210ae7f2a13d858cdb4ca6b`

### 124. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:99f59962822de2ac:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1012`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：preset.label
- 判定原因：翻译键由运行时表达式“preset.label”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`99f59962822de2acae82fbe7ea169c844f62fda0939a56cc23ef9c0a456f1a99`

### 125. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:8387eb890b0f99fb:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1068`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：activePreset.hint
- 判定原因：翻译键由运行时表达式“activePreset.hint”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8387eb890b0f99fb9294383e5c3eba6d37367f934184fd146afb75aa4ccefab7`

### 126. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:99f59962822de2ac:002`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1240`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：preset.label
- 判定原因：翻译键由运行时表达式“preset.label”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`99f59962822de2acae82fbe7ea169c844f62fda0939a56cc23ef9c0a456f1a99`

### 127. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:5dd4180e2514c9a4:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1251`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：activeS3Preset.hint
- 判定原因：翻译键由运行时表达式“activeS3Preset.hint”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5dd4180e2514c9a49b23541f88caab22c8fc51afb084a05fd1a4e5980b699046`

### 128. `dynamic-i18n:src/components/settings/sections/AppConfigSection.tsx:directoryRow:1743f9d9e477bf5f:001`

- 状态：待核实
- 文件：`src/components/settings/sections/AppConfigSection.tsx:114`
- 结构：`directoryRow` / `dynamic_i18n_key`
- 原文/表达式：DIRECTORY_PLACEHOLDER[app]
- 判定原因：翻译键由运行时表达式“DIRECTORY_PLACEHOLDER[app]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1743f9d9e477bf5fb1cf8a57c847a3f8240b314cb301099ff34aa70c583b0237`

### 129. `dynamic-i18n:src/components/settings/sections/GeneralSection.tsx:GeneralSection:4b8d2a85ad692265:001`

- 状态：待核实
- 文件：`src/components/settings/sections/GeneralSection.tsx:70`
- 结构：`GeneralSection` / `dynamic_i18n_key`
- 原文/表达式：language.labelKey
- 判定原因：翻译键由运行时表达式“language.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4b8d2a85ad692265da8e642979b40961d600061dda06d269772225e67eff2e4c`

### 130. `dynamic-i18n:src/components/settings/sections/RoutingSection.tsx:RoutingSection:8594999185d253ca:001`

- 状态：待核实
- 文件：`src/components/settings/sections/RoutingSection.tsx:402`
- 结构：`RoutingSection` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${mode}`
- 判定原因：翻译键由运行时表达式“`mode.names.${mode}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8594999185d253cac67012cdf03429a7ec6a6ed8cb4300166ad5416582da216c`

### 131. `dynamic-i18n:src/components/shell/Sidebar.tsx:SettingsDirectory:73080ad588a22bcf:001`

- 状态：待核实
- 文件：`src/components/shell/Sidebar.tsx:754`
- 结构：`SettingsDirectory` / `dynamic_i18n_key`
- 原文/表达式：`settings.sections.${section}`
- 判定原因：翻译键由运行时表达式“`settings.sections.${section}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`73080ad588a22bcf793b9900af2a25a37aa84db57382a48713b1575b878c240e`

### 132. `dynamic-i18n:src/components/skills/SkillsStorageSheet.tsx:SkillsStorageSheet:0c9f9f16eb7882e5:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsStorageSheet.tsx:306`
- 结构：`SkillsStorageSheet` / `dynamic_i18n_key`
- 原文/表达式：option.labelKey
- 判定原因：翻译键由运行时表达式“option.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0c9f9f16eb7882e54ef00841c2a810356cde523b3b567ad568f426ada1cf34f4`

### 133. `dynamic-i18n:src/components/skills/SkillsStorageSheet.tsx:SkillsStorageSheet:36befa74dfbcc58f:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsStorageSheet.tsx:309`
- 结构：`SkillsStorageSheet` / `dynamic_i18n_key`
- 原文/表达式：option.descKey
- 判定原因：翻译键由运行时表达式“option.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`36befa74dfbcc58f25411157c9597ba984e7e2d0a0815ac516fadfe3689ab2b7`

### 134. `dynamic-i18n:src/components/skills/UnifiedSkillsPanel.tsx:text:dc4eb9bbc03ce6c2:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:458`
- 结构：`text` / `dynamic_i18n_key`
- 原文/表达式：enabled ? toastKey.on : toastKey.off
- 判定原因：翻译键由运行时表达式“enabled ? toastKey.on : toastKey.off”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`dc4eb9bbc03ce6c2f1f6d09396558b5864c5f98fedaa2cb3471f608770e9cb02`

### 135. `dynamic-i18n:src/components/skills/UnifiedSkillsPanel.tsx:InstalledRow:947324ed6a00ba24:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:1929`
- 结构：`InstalledRow` / `dynamic_i18n_key`
- 原文/表达式：`appMatrix.cell.${state}`
- 判定原因：翻译键由运行时表达式“`appMatrix.cell.${state}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`947324ed6a00ba241dcc93e16c9b7022385f2e299608f805663901480e1d6454`

### 136. `dynamic-i18n:src/components/usage/RequestLogColumnsMenu.tsx:RequestLogColumnsMenu:4c6b716150f3dad4:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogColumnsMenu.tsx:59`
- 结构：`RequestLogColumnsMenu` / `dynamic_i18n_key`
- 原文/表达式：REQUEST_LOG_COLUMN_LABEL_KEYS[id]
- 判定原因：翻译键由运行时表达式“REQUEST_LOG_COLUMN_LABEL_KEYS[id]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4c6b716150f3dad49920b06ba95bb0f52bc634dcdf0f07106200b1cdae9a6d38`

### 137. `dynamic-i18n:src/components/usage/RequestLogTable.tsx:label:4c6b716150f3dad4:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:354`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：REQUEST_LOG_COLUMN_LABEL_KEYS[id]
- 判定原因：翻译键由运行时表达式“REQUEST_LOG_COLUMN_LABEL_KEYS[id]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4c6b716150f3dad49920b06ba95bb0f52bc634dcdf0f07106200b1cdae9a6d38`

### 138. `dynamic-i18n:src/components/usage/UsageDisplaySection.tsx:todayLabel:9c965868dda12772:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDisplaySection.tsx:93`
- 结构：`todayLabel` / `dynamic_i18n_key`
- 原文/表达式：`usage.display.sidebarTodayItems.${item}`
- 判定原因：翻译键由运行时表达式“`usage.display.sidebarTodayItems.${item}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`9c965868dda12772b73d7958875846e84e79a30b5a00c878d6a75c0f72e2639a`

### 139. `dynamic-i18n:src/components/usage/UsageDisplaySection.tsx:UsageDisplaySection:74fefa25328abc5c:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDisplaySection.tsx:196`
- 结构：`UsageDisplaySection` / `dynamic_i18n_key`
- 原文/表达式：`usage.display.trendChartTypes.${type}`
- 判定原因：翻译键由运行时表达式“`usage.display.trendChartTypes.${type}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`74fefa25328abc5cd636335aba766326037e74a4da2150435f5b885939fd630c`

### 140. `dynamic-i18n:src/components/workspace/WorkspaceFilesPanel.tsx:WorkspaceFilesPanel:347a6a525595a8b6:001`

- 状态：待核实
- 文件：`src/components/workspace/WorkspaceFilesPanel.tsx:123`
- 结构：`WorkspaceFilesPanel` / `dynamic_i18n_key`
- 原文/表达式：file.descKey
- 判定原因：翻译键由运行时表达式“file.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`347a6a525595a8b6f3f5f07623bb8c87dd641019052c4c36c8d856c7dc75560f`

### 141. `dynamic-i18n:src/config/mcpPresets.ts:getMcpPresetWithDescription:0c1d1c92eda0e772:001`

- 状态：待核实
- 文件：`src/config/mcpPresets.ts:102`
- 结构：`getMcpPresetWithDescription` / `dynamic_i18n_key`
- 原文/表达式：descriptionKey
- 判定原因：翻译键由运行时表达式“descriptionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0c1d1c92eda0e772769c808027e639ef98b15ace47087dabe50c20f4036b633e`

### 142. `dynamic-i18n:src/hooks/useModeActions.ts:enter:883829e896b1bc8a:001`

- 状态：待核实
- 文件：`src/hooks/useModeActions.ts:62`
- 结构：`enter` / `dynamic_i18n_key`
- 原文/表达式：app === "codex"<br>                  ? "mode.toast.enteredStack"<br>                  : app === "claude-desktop"<br>                    ? "mode.toast.enteredStackDesktop"<br>                    : "mode.toast.enteredStackLive"
- 判定原因：翻译键由运行时表达式“app === "codex"
                  ? "mode.toast.enteredStack"
                  : app === "claude-desktop"
                    ? "mode.toast.enteredStackDesktop"
                    : "mode.toast.enteredStackLive"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`883829e896b1bc8aef277f4a21d15d6836060d521592f467337d15a69965bd90`

### 143. `dynamic-i18n:src/hooks/usePromptActions.ts:toggleEnabled:0a592ddbd2de0f49:001`

- 状态：待核实
- 文件：`src/hooks/usePromptActions.ts:210`
- 结构：`toggleEnabled` / `dynamic_i18n_key`
- 原文/表达式：enabled<br>                  ? "pi.prompts.usePromptSuccess"<br>                  : "pi.prompts.stopUsingSuccess"
- 判定原因：翻译键由运行时表达式“enabled
                  ? "pi.prompts.usePromptSuccess"
                  : "pi.prompts.stopUsingSuccess"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0a592ddbd2de0f4975252f9cdbe2dbe113aabd4c0d6efee015027c3922676cc9`

### 144. `dynamic-i18n:src/hooks/useProviderActions.ts:message:957b5b6d4c6b0d30:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:278`
- 结构：`message` / `dynamic_i18n_key`
- 原文/表达式：messageKey
- 判定原因：翻译键由运行时表达式“messageKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`957b5b6d4c6b0d309df52a69490ab3731b3e639d324d8b29bf10dc914b793946`

### 145. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:c948ad90dbb56786:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:17`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.pro`
- 判定原因：翻译键由运行时表达式“`${key}.pro`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c948ad90dbb5678610291538a968108d48de158c5a0ba0bfaf4fb81008c9cd5d`

### 146. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:e6d34e9dad987f63:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:20`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.max20x`
- 判定原因：翻译键由运行时表达式“`${key}.max20x`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e6d34e9dad987f632f3f18e36e88b55211d1613b8fa4845a48fffe4d566c56b8`

### 147. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:526dea196aee52d7:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:23`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.max5x`
- 判定原因：翻译键由运行时表达式“`${key}.max5x`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`526dea196aee52d7886ac3e4c476eb29cc3bb3a25181468cf00307c80191f65c`

### 148. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:0643f8d5c2a7a4d6:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:25`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.max`
- 判定原因：翻译键由运行时表达式“`${key}.max`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0643f8d5c2a7a4d6214d2d38a0b43faa32e0f8f264ca47dead55542c58d107ad`

### 149. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:73cc9395a6dcb325:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:29`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.teamPremium`
- 判定原因：翻译键由运行时表达式“`${key}.teamPremium`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`73cc9395a6dcb325d82f735d1a042fff223dcd0e026575f29309f5f69f8f9fa6`

### 150. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:8047060929970a87:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:30`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.team`
- 判定原因：翻译键由运行时表达式“`${key}.team`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8047060929970a871fcf63d1f23b79fa556b232ba7cb693a0b36dd5c81f00dbc`

### 151. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:906c5699182dee61:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:32`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.enterprise`
- 判定原因：翻译键由运行时表达式“`${key}.enterprise`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`906c5699182dee610ce1f9488363070fe1520ee83a2604834b454a9a83774070`

### 152. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:formatSkillError:70769166fc12d162:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:88`
- 结构：`formatSkillError` / `dynamic_i18n_key`
- 原文/表达式：defaultTitle
- 判定原因：翻译键由运行时表达式“defaultTitle”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`70769166fc12d1627fb5ece5b0a1c29e89411cde5da0673db299484321d4dd27`

### 153. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:description:f55554c3a3e38660:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:99`
- 结构：`description` / `dynamic_i18n_key`
- 原文/表达式：errorKey
- 判定原因：翻译键由运行时表达式“errorKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`f55554c3a3e386604c41ab7912c05ed79a2c10029c66f618bbe46841de3de024`

### 154. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:suggestionText:74e698c28bf062c8:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:104`
- 结构：`suggestionText` / `dynamic_i18n_key`
- 原文/表达式：suggestionKey
- 判定原因：翻译键由运行时表达式“suggestionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`74e698c28bf062c806a22962230d15a0ee29463a2cc768d0cf94524888d5a38f`

### 155. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:formatSkillError:70769166fc12d162:002`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:109`
- 结构：`formatSkillError` / `dynamic_i18n_key`
- 原文/表达式：defaultTitle
- 判定原因：翻译键由运行时表达式“defaultTitle”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`70769166fc12d1627fb5ece5b0a1c29e89411cde5da0673db299484321d4dd27`

### 156. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:skillErrorReason:cc40d5267afefbf0:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:126`
- 结构：`skillErrorReason` / `dynamic_i18n_key`
- 原文/表达式：getSuggestionI18nKey(suggestion)
- 判定原因：翻译键由运行时表达式“getSuggestionI18nKey(suggestion)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cc40d5267afefbf037b85e766c90145120db9f19a3bbdb13a9e69779732037a0`

### 157. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:skillErrorReason:37f93e4d82bbafa0:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:128`
- 结构：`skillErrorReason` / `dynamic_i18n_key`
- 原文/表达式：getErrorI18nKey(code)
- 判定原因：翻译键由运行时表达式“getErrorI18nKey(code)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`37f93e4d82bbafa004c28b0304a43a96a0e1d1f97a588c17fcfa0c7fe241da41`

### 158. `dynamic-i18n:src/lib/query/proxy.ts:useSetProxyStackMember:2e6460788eddf87d:001`

- 状态：待核实
- 文件：`src/lib/query/proxy.ts:122`
- 结构：`useSetProxyStackMember` / `dynamic_i18n_key`
- 原文/表达式：variables.appType === "codex" \|\|<br>            variables.appType === "claude-desktop"<br>            ? "provider.stackSaved"<br>            : "provider.stackSavedLive"
- 判定原因：翻译键由运行时表达式“variables.appType === "codex" ||
            variables.appType === "claude-desktop"
            ? "provider.stackSaved"
            : "provider.stackSavedLive"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2e6460788eddf87d8e986c08763e3355caabd19c042657a388010e0c4ab5592a`

### 159. `dynamic-i18n:src/lib/query/proxy.ts:useSetProxyStackMember:7f3542671de62631:001`

- 状态：待核实
- 文件：`src/lib/query/proxy.ts:138`
- 结构：`useSetProxyStackMember` / `dynamic_i18n_key`
- 原文/表达式：`provider.${notice}`
- 判定原因：翻译键由运行时表达式“`provider.${notice}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`7f3542671de626310d5e5b3ed78dc2b8058c2dc915fbbb03ea3861bf9bcbccbc`

### 160. `dynamic-i18n:src/lib/query/proxy.ts:useAdoptCodexStackCatalog:7f3542671de62631:001`

- 状态：待核实
- 文件：`src/lib/query/proxy.ts:174`
- 结构：`useAdoptCodexStackCatalog` / `dynamic_i18n_key`
- 原文/表达式：`provider.${notice}`
- 判定原因：翻译键由运行时表达式“`provider.${notice}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`7f3542671de626310d5e5b3ed78dc2b8058c2dc915fbbb03ea3861bf9bcbccbc`

### 161. `dynamic-i18n:src/utils/errorUtils.ts:translatePiProviderMutationError:87913d866ba16384:001`

- 状态：待核实
- 文件：`src/utils/errorUtils.ts:47`
- 结构：`translatePiProviderMutationError` / `dynamic_i18n_key`
- 原文/表达式：ompKey
- 判定原因：翻译键由运行时表达式“ompKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`87913d866ba16384ba8999764817a4113c4ca7d29f98076db7cc1b4cc2aad7c5`

### 162. `dynamic-i18n:src/utils/errorUtils.ts:translateMcpBackendError:87913d866ba16384:001`

- 状态：待核实
- 文件：`src/utils/errorUtils.ts:95`
- 结构：`translateMcpBackendError` / `dynamic_i18n_key`
- 原文/表达式：ompKey
- 判定原因：翻译键由运行时表达式“ompKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`87913d866ba16384ba8999764817a4113c4ca7d29f98076db7cc1b4cc2aad7c5`

