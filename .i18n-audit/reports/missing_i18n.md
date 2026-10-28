# 国际化遗漏审查

- 生产源码纳入：801
- 成功扫描：801
- 扫描失败：0
- 候选总数：4426
- 确认遗漏：60
- 待核实：557
- 无需国际化：3809
- 范围排除文件：1
- 候选类别排除：1436（后端错误：双语 262 + 其他硬编码 1174）

> 本报告不展示已确认无需国际化的候选项。候选详情保留在 `.i18n-audit/reviews/hardcoded/`。

## 系统性结论

- 后端错误按产品决定排除：`AppError::localized` 262 条中英双语错误，以及其他后端硬编码错误 1174 条，均不计入韩语遗漏项。
- 多个前端校验器和工具函数直接抛出中文/英文错误，绕过 i18n。
- 多处可见 JSX 标签（如 `Auth:`、`TOML Config:`、`Reasoning Effort`、`API Key`）仍未使用翻译函数。
- 162 个动态翻译键已逐一登记为待核实，不能仅因运行时未崩溃视为安全。

## 确认遗漏明细（60）

### 1. `hardcoded:src/components/DeepLinkImportDialog.tsx:DeepLinkImportDialog:7de02e7f919bd514:001`

- 状态：确认遗漏
- 文件：`src/components/DeepLinkImportDialog.tsx:732`
- 结构：`DeepLinkImportDialog` / `jsx_text`
- 原文/表达式：Auth:
- 判定原因：对话框中的字段分组标题直接硬编码英文，切换韩语后仍显示英文。
- 处理方向：新增翻译键并在韩语资源中提供对应标签。
- 推荐韩文：인증:
- 严重程度：中
- 指纹：`7de02e7f919bd51427a2a49637b5c42567018fb93282b59b55b2b22702496bf5`

### 2. `hardcoded:src/components/DeepLinkImportDialog.tsx:DeepLinkImportDialog:4922fc9dd3ca2b64:001`

- 状态：确认遗漏
- 文件：`src/components/DeepLinkImportDialog.tsx:750`
- 结构：`DeepLinkImportDialog` / `jsx_text`
- 原文/表达式：TOML Config:
- 判定原因：对话框中的字段分组标题直接硬编码英文，切换韩语后仍显示英文。
- 处理方向：新增翻译键并在韩语资源中提供对应标签。
- 推荐韩文：TOML 설정:
- 严重程度：中
- 指纹：`4922fc9dd3ca2b64dee0e420d7d46927d37f1c7147a0c3aef8b5601ac96eb468`

### 3. `hardcoded:src/components/UsageScriptModal.tsx:UsageScriptModal:23189d55f6973f2c:001`

- 状态：确认遗漏
- 文件：`src/components/UsageScriptModal.tsx:1156`
- 结构：`UsageScriptModal` / `jsx_text`
- 原文/表达式：API Key
- 判定原因：可见字段标签硬编码英文，现有韩语界面统一使用「API 키」。
- 处理方向：使用现有 API Key 标签翻译键。
- 推荐韩文：API 키
- 严重程度：中
- 指纹：`23189d55f6973f2ce5325707ab40ed9a145fd5b71f0f009448f0c15fc22b3d73`

### 4. `hardcoded:src/components/UsageScriptModal.tsx:UsageScriptModal:23189d55f6973f2c:002`

- 状态：确认遗漏
- 文件：`src/components/UsageScriptModal.tsx:1320`
- 结构：`UsageScriptModal` / `jsx_text`
- 原文/表达式：API Key
- 判定原因：可见字段标签硬编码英文，现有韩语界面统一使用「API 키」。
- 处理方向：使用现有 API Key 标签翻译键。
- 推荐韩文：API 키
- 严重程度：中
- 指纹：`23189d55f6973f2ce5325707ab40ed9a145fd5b71f0f009448f0c15fc22b3d73`

### 5. `hardcoded:src/components/providers/forms/hooks/useCodexTomlValidation.ts:errorMessage:dded5e1d24c96e2a:001`

- 状态：确认遗漏
- 文件：`src/components/providers/forms/hooks/useCodexTomlValidation.ts:30`
- 结构：`errorMessage` / `string`
- 原文/表达式：TOML 格式错误
- 判定原因：Codex TOML 校验错误显示在表单内，未接入 i18n。
- 处理方向：按错误类型映射到翻译键。
- 严重程度：中
- 指纹：`dded5e1d24c96e2ab01ae6104d644879cd1342121f14ea2f61f45289423e4636`

### 6. `hardcoded:src/components/universal/UniversalProviderFormModal.tsx:UniversalProviderFormModal:6f71800c93bd916e:001`

- 状态：确认遗漏
- 文件：`src/components/universal/UniversalProviderFormModal.tsx:600`
- 结构：`UniversalProviderFormModal` / `jsx_text`
- 原文/表达式：Reasoning Effort
- 判定原因：表单字段标签直接硬编码英文，未接入 i18n。
- 处理方向：使用字段标签翻译键。
- 推荐韩文：추론 수준
- 严重程度：中
- 指纹：`6f71800c93bd916e601cf078542b5250383633bf18f08a2c6e019db9975abcbb`

### 7. `hardcoded:src/components/usage/providerLabel.ts:SESSION_PROVIDER_APPS:01f4e2433ec4be24:001`

- 状态：确认遗漏
- 文件：`src/components/usage/providerLabel.ts:15`
- 结构：`SESSION_PROVIDER_APPS` / `string`
- 原文/表达式：Grok Build (Session)
- 判定原因：会话来源标签后缀固定为英文，会出现在用量筛选/表格的用户可见名称中。
- 处理方向：将后缀改为 i18n 片段。
- 严重程度：低
- 指纹：`01f4e2433ec4be24aa94ed7466ff73dab3a6273a008a0f9aed4869b5e16e7381`

### 8. `hardcoded:src/components/usage/providerLabel.ts:SESSION_PROVIDER_APPS:8fe6db86f3c11f21:001`

- 状态：确认遗漏
- 文件：`src/components/usage/providerLabel.ts:16`
- 结构：`SESSION_PROVIDER_APPS` / `string`
- 原文/表达式：MiniMax Code (Session)
- 判定原因：会话来源标签后缀固定为英文，会出现在用量筛选/表格的用户可见名称中。
- 处理方向：将后缀改为 i18n 片段。
- 严重程度：低
- 指纹：`8fe6db86f3c11f21652978cdaaf7dc6862ff8027669c667d9b53aba230d8385a`

### 9. `hardcoded:src/components/usage/providerLabel.ts:SESSION_PROVIDER_APPS:0f38be253cd29be7:001`

- 状态：确认遗漏
- 文件：`src/components/usage/providerLabel.ts:17`
- 结构：`SESSION_PROVIDER_APPS` / `string`
- 原文/表达式：Kimi Code (Session)
- 判定原因：会话来源标签后缀固定为英文，会出现在用量筛选/表格的用户可见名称中。
- 处理方向：将后缀改为 i18n 片段。
- 严重程度：低
- 指纹：`0f38be253cd29be755bc5a7ce60ac1f4eac5fb8a9f3f49def9b0b34ff6776911`

### 10. `hardcoded:src/config/codingPlanProviders.ts:CODING_PLAN_PROVIDERS:3db0e7b4fbcf5a89:001`

- 状态：确认遗漏
- 文件：`src/config/codingPlanProviders.ts:36`
- 结构：`CODING_PLAN_PROVIDERS` / `string`
- 原文/表达式：Zhipu GLM (智谱)
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`3db0e7b4fbcf5a8948b03db16bd40f01af615ee9904524b3272508eba3cde421`

### 11. `hardcoded:src/config/codingPlanProviders.ts:CODING_PLAN_PROVIDERS:b1d2aaa46c82135e:001`

- 状态：确认遗漏
- 文件：`src/config/codingPlanProviders.ts:46`
- 结构：`CODING_PLAN_PROVIDERS` / `string`
- 原文/表达式：Zhipu GLM Team (智谱团队)
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`b1d2aaa46c82135e0282e4459e7bfe473670d79814971cdf27774cc7b7ab9bab`

### 12. `hardcoded:src/config/codingPlanProviders.ts:CODING_PLAN_PROVIDERS:63c6e0bb0efb7b2f:001`

- 状态：确认遗漏
- 文件：`src/config/codingPlanProviders.ts:68`
- 结构：`CODING_PLAN_PROVIDERS` / `string`
- 原文/表达式：火山方舟 (Volcengine)
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`63c6e0bb0efb7b2f6f3fda2e0400019812642e4a76f44e02c7e9ab2a74d7d86a`

### 13. `hardcoded:src/config/geminiProviderPresets.ts:geminiProviderPresets:adc217dd32753992:001`

- 状态：确认遗漏
- 文件：`src/config/geminiProviderPresets.ts:44`
- 结构：`geminiProviderPresets` / `string`
- 原文/表达式：Google 官方 Gemini API (OAuth)
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`adc217dd3275399254b3aba37faa7150ec4e752f85dfe37af80fccbe4685bb7f`

### 14. `hardcoded:src/config/opencodeProviderPresets.ts:opencodeProviderPresets:789e7138516546aa:002`

- 状态：确认遗漏
- 文件：`src/config/opencodeProviderPresets.ts:1619`
- 结构：`opencodeProviderPresets` / `string`
- 原文/表达式：火山 Agent Plan
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`789e7138516546aa68ed5ea9c8627110855d29b1508d9ad45c62862229330f09`

### 15. `hardcoded:src/config/opencodeProviderPresets.ts:opencodeProviderPresets:4c8a38aad6ae652f:002`

- 状态：确认遗漏
- 文件：`src/config/opencodeProviderPresets.ts:1654`
- 结构：`opencodeProviderPresets` / `string`
- 原文/表达式：火山 Coding Plan
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`4c8a38aad6ae652f0539951f8b9983f36ffab8ed99199f7648df6aada9753a9c`

### 16. `hardcoded:src/config/opencodeProviderPresets.ts:opencodeProviderPresets:dfc683f1eeccb537:002`

- 状态：确认遗漏
- 文件：`src/config/opencodeProviderPresets.ts:2873`
- 结构：`opencodeProviderPresets` / `string`
- 原文/表达式：千问AI平台
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`dfc683f1eeccb5372dd95a3444222d8c6161c261fdfbe9efc0ad0b086f45e3c1`

### 17. `hardcoded:src/config/opencodeProviderPresets.ts:opencodeProviderPresets:97c44cb45918dcfe:002`

- 状态：确认遗漏
- 文件：`src/config/opencodeProviderPresets.ts:2921`
- 结构：`opencodeProviderPresets` / `string`
- 原文/表达式：千问AI平台 Token Plan
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`97c44cb45918dcfee9ba21647a6c60d52621760b8208176d0d7c6dabfa7fd12b`

### 18. `hardcoded:src/config/opencodeProviderPresets.ts:opencodeProviderPresets:d4c50f95774cffbd:002`

- 状态：确认遗漏
- 文件：`src/config/opencodeProviderPresets.ts:4430`
- 结构：`opencodeProviderPresets` / `string`
- 原文/表达式：模力方舟
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`d4c50f95774cffbdd6d3e0c9322cabbe28c48e1300e327260432b52186917a32`

### 19. `hardcoded:src/config/piProviderPresets.ts:piProviderPresetDefinitions:789e7138516546aa:002`

- 状态：确认遗漏
- 文件：`src/config/piProviderPresets.ts:938`
- 结构：`piProviderPresetDefinitions` / `string`
- 原文/表达式：火山 Agent Plan
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`789e7138516546aa68ed5ea9c8627110855d29b1508d9ad45c62862229330f09`

### 20. `hardcoded:src/config/piProviderPresets.ts:piProviderPresetDefinitions:4c8a38aad6ae652f:002`

- 状态：确认遗漏
- 文件：`src/config/piProviderPresets.ts:964`
- 结构：`piProviderPresetDefinitions` / `string`
- 原文/表达式：火山 Coding Plan
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`4c8a38aad6ae652f0539951f8b9983f36ffab8ed99199f7648df6aada9753a9c`

### 21. `hardcoded:src/config/piProviderPresets.ts:piProviderPresetDefinitions:dfc683f1eeccb537:002`

- 状态：确认遗漏
- 文件：`src/config/piProviderPresets.ts:1507`
- 结构：`piProviderPresetDefinitions` / `string`
- 原文/表达式：千问AI平台
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`dfc683f1eeccb5372dd95a3444222d8c6161c261fdfbe9efc0ad0b086f45e3c1`

### 22. `hardcoded:src/config/piProviderPresets.ts:piProviderPresetDefinitions:97c44cb45918dcfe:002`

- 状态：确认遗漏
- 文件：`src/config/piProviderPresets.ts:1534`
- 结构：`piProviderPresetDefinitions` / `string`
- 原文/表达式：千问AI平台 Token Plan
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`97c44cb45918dcfee9ba21647a6c60d52621760b8208176d0d7c6dabfa7fd12b`

### 23. `hardcoded:src/config/piProviderPresets.ts:piProviderPresetDefinitions:d4c50f95774cffbd:002`

- 状态：确认遗漏
- 文件：`src/config/piProviderPresets.ts:3221`
- 结构：`piProviderPresetDefinitions` / `string`
- 原文/表达式：模力方舟
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`d4c50f95774cffbdd6d3e0c9322cabbe28c48e1300e327260432b52186917a32`

### 24. `hardcoded:src/config/presetFamilies.ts:PRESET_FAMILIES:dfc683f1eeccb537:001`

- 状态：确认遗漏
- 文件：`src/config/presetFamilies.ts:34`
- 结构：`PRESET_FAMILIES` / `string`
- 原文/表达式：千问AI平台
- 判定原因：该预设字段可能展示给用户，但仍是硬编码中文。
- 处理方向：核实展示位置后迁入 i18n 资源。
- 严重程度：中
- 指纹：`dfc683f1eeccb5372dd95a3444222d8c6161c261fdfbe9efc0ad0b086f45e3c1`

### 25. `hardcoded:src/config/universalProviderPresets.ts:universalProviderPresets:664ce053a17de1b3:001`

- 状态：确认遗漏
- 文件：`src/config/universalProviderPresets.ts:75`
- 结构：`universalProviderPresets` / `string`
- 原文/表达式：NewAPI 是一个可自部署的 API 网关，支持 Anthropic、OpenAI、Gemini 等多种协议
- 判定原因：通用供应商预设说明会直接展示给用户，但仍是硬编码中文。
- 处理方向：改为翻译键并在 zh/ko/en 资源中提供说明。
- 推荐韩文：NewAPI는 Anthropic, OpenAI, Gemini 등 여러 프로토콜을 지원하는 자체 호스팅 가능한 API 게이트웨이입니다.
- 严重程度：中
- 指纹：`664ce053a17de1b3e13623a1bc0aff33eaebdcab7c04f81910e6cd9f90f08940`

### 26. `hardcoded:src/config/universalProviderPresets.ts:universalProviderPresets:c0c340c6669b573e:001`

- 状态：确认遗漏
- 文件：`src/config/universalProviderPresets.ts:78`
- 结构：`universalProviderPresets` / `string`
- 原文/表达式：自定义网关
- 判定原因：通用供应商预设说明会直接展示给用户，但仍是硬编码中文。
- 处理方向：改为翻译键并在 zh/ko/en 资源中提供说明。
- 推荐韩文：사용자 지정 구성의 API 게이트웨이
- 严重程度：中
- 指纹：`c0c340c6669b573e18e6d5299a9dd465ccd59f8fbfac855315a8bce686806315`

### 27. `hardcoded:src/config/universalProviderPresets.ts:universalProviderPresets:f21532a893347f92:001`

- 状态：确认遗漏
- 文件：`src/config/universalProviderPresets.ts:88`
- 结构：`universalProviderPresets` / `string`
- 原文/表达式：自定义配置的 API 网关
- 判定原因：通用供应商预设说明会直接展示给用户，但仍是硬编码中文。
- 处理方向：改为翻译键并在 zh/ko/en 资源中提供说明。
- 推荐韩文：사용자 지정 구성의 API 게이트웨이
- 严重程度：中
- 指纹：`f21532a893347f92a196d5fbf7be8002b50452cfc9517c225b38077a2e210d19`

### 28. `hardcoded:src/hooks/usePromptActions.ts:toggleEnabled:7dddff38555ef878:001`

- 状态：确认遗漏
- 文件：`src/hooks/usePromptActions.ts:199`
- 结构：`toggleEnabled` / `template`
- 原文/表达式：`Prompt ${id} does not exist`
- 判定原因：提示词操作异常会向上冒泡到用户通知，但消息固定为英文。
- 处理方向：使用错误码并在通知层翻译。
- 严重程度：中
- 指纹：`7dddff38555ef8787e5d36ce807e6e3c0b4c852ca4c6fd7de592f7e643ac2774`

### 29. `hardcoded:src/index.html:<html>:25446063f4c3bc2c:001`

- 状态：确认遗漏
- 文件：`src/index.html:6`
- 结构：`<html>` / `html_text`
- 原文/表达式：Claude Code 供应商切换器
- 判定原因：HTML 文档标题硬编码中文，窗口首次加载或读取文档标题时不会随语言切换。
- 处理方向：在运行时根据 i18n 设置 document.title，并使用资源键。
- 严重程度：中
- 指纹：`25446063f4c3bc2c4ce81522b40c699107700afcbbd0d794b4a8ec0e13978833`

### 30. `hardcoded:src/lib/requestOverrides.ts:parseRequestOverrideJson:74a1bddc53f46610:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:91`
- 结构：`parseRequestOverrideJson` / `string`
- 原文/表达式：JSON must be an object
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`74a1bddc53f466101dff2904702b8bd0ddaef45642ab91ee157378761979c0ea`

### 31. `hardcoded:src/lib/requestOverrides.ts:parseBodyOverrideJson:813beebde821ec1c:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:107`
- 结构：`parseBodyOverrideJson` / `string`
- 原文/表达式：Body override must not include protocol field "stream"
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`813beebde821ec1cb48962885314f3d031e6a6bd5482e27a4e210a81940131b4`

### 32. `hardcoded:src/lib/requestOverrides.ts:parseHeaderOverrideJson:587ae7c1023150ec:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:124`
- 结构：`parseHeaderOverrideJson` / `string`
- 原文/表达式：Header name must not be empty
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`587ae7c1023150ecebc867c1df143765656e9380c6464a02a190f337ce98627c`

### 33. `hardcoded:src/lib/requestOverrides.ts:parseHeaderOverrideJson:de3ce1024b239d54:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:127`
- 结构：`parseHeaderOverrideJson` / `template`
- 原文/表达式：`Header "${name}" name is not a valid HTTP token`
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`de3ce1024b239d54108c50efa6da9ba8387d822f3bb2da1daff71d060a2822dc`

### 34. `hardcoded:src/lib/requestOverrides.ts:parseHeaderOverrideJson:c77d98caf29bc0fc:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:130`
- 结构：`parseHeaderOverrideJson` / `template`
- 原文/表达式：`Header "${name}" value must be a string`
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`c77d98caf29bc0fc37623658e4524653c937a42ca0d2d204d62c51b94bb13c65`

### 35. `hardcoded:src/lib/requestOverrides.ts:parseHeaderOverrideJson:a45fdb85bfe0af33:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:133`
- 结构：`parseHeaderOverrideJson` / `template`
- 原文/表达式：`Header "${name}" value contains control characters`
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`a45fdb85bfe0af339b8c272992fd8858ba95727f4e09e08409d29f8576cdf9c8`

### 36. `hardcoded:src/lib/requestOverrides.ts:parseHeaderOverrideJson:a639e11e36f4e1ed:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:138`
- 结构：`parseHeaderOverrideJson` / `template`
- 原文/表达式：`Header "${name}" duplicates another header after case normalization`
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`a639e11e36f4e1edef2e3f824bd6feb179f721bbec6e803769cd4775cf4d6774`

### 37. `hardcoded:src/lib/requestOverrides.ts:parseHeaderOverrideJson:cdd5bee05a2f14b7:001`

- 状态：确认遗漏
- 文件：`src/lib/requestOverrides.ts:143`
- 结构：`parseHeaderOverrideJson` / `template`
- 原文/表达式：`Header "${name}" is managed by the local proxy and cannot be overridden`
- 判定原因：请求覆盖字段会将该英文校验错误直接显示在表单中，没有韩语版本。
- 处理方向：返回错误码并在展示层通过 t() 本地化。
- 严重程度：中
- 指纹：`cdd5bee05a2f14b731f62ea59c18ef91aa0461065f2a267a23497f4b9294d0f0`

### 38. `hardcoded:src/lib/schemas/provider.ts:parseJsonError:aecab70fa3eb4483:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:8`
- 结构：`parseJsonError` / `string`
- 原文/表达式：配置 JSON 格式错误
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`aecab70fa3eb4483d59e7135e6cdb65eb399594a53e65c6aeb2db6bc15e2cbd7`

### 39. `hardcoded:src/lib/schemas/provider.ts:parseJsonError:e61d4ec9a0fef58d:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:17`
- 结构：`parseJsonError` / `template`
- 原文/表达式：`JSON 格式错误：${message.split(" in JSON")[0]}（位置：${position}）`
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`e61d4ec9a0fef58db5ff96f63a6a681b09e417d73a3ff70d650a53603efd6076`

### 40. `hardcoded:src/lib/schemas/provider.ts:parseJsonError:d73db14d9074a0c0:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:25`
- 结构：`parseJsonError` / `template`
- 原文/表达式：`JSON 格式错误：第 ${line} 行，第 ${column} 列`
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`d73db14d9074a0c08f89b15b5c974e472b2b555a85a6b94396bb512d6b49dd00`

### 41. `hardcoded:src/lib/schemas/provider.ts:cleanMessage:97077e67b17ede29:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:31`
- 结构：`cleanMessage` / `string`
- 原文/表达式：意外的
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`97077e67b17ede29a35860441bc8000c254533a05720b689f192931234c66f58`

### 42. `hardcoded:src/lib/schemas/provider.ts:cleanMessage:e892654a499d52a7:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:32`
- 结构：`cleanMessage` / `string`
- 原文/表达式：符号
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`e892654a499d52a776c3d245b8800e9d15b1b07e6451fd2fa30d453a2b1a7b82`

### 43. `hardcoded:src/lib/schemas/provider.ts:cleanMessage:c8cdcb6926a83554:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:33`
- 结构：`cleanMessage` / `string`
- 原文/表达式：预期
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`c8cdcb6926a835545691338032924229cd53759990aae97477a7bf21e131e35b`

### 44. `hardcoded:src/lib/schemas/provider.ts:parseJsonError:871e44e90167d743:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:35`
- 结构：`parseJsonError` / `template`
- 原文/表达式：`JSON 格式错误：${cleanMessage}`
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`871e44e90167d7433d1072b39182b1448f83765d0dcde7e9577a2832e8791818`

### 45. `hardcoded:src/lib/schemas/provider.ts:providerSchema:427abb574107ec59:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:40`
- 结构：`providerSchema` / `string`
- 原文/表达式：请输入有效的网址
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`427abb574107ec59a30fde77da8729c8c08073c9fb45ff05b125331a88aa7ec2`

### 46. `hardcoded:src/lib/schemas/provider.ts:providerSchema:e8867867bf2d0227:001`

- 状态：确认遗漏
- 文件：`src/lib/schemas/provider.ts:44`
- 结构：`providerSchema` / `string`
- 原文/表达式：请填写配置内容
- 判定原因：供应商表单 zod 校验消息直接返回中文，字段错误会原样显示。
- 处理方向：错误码化并在表单层本地化。
- 严重程度：高
- 指纹：`e8867867bf2d0227e95f4188c168499c13dfee7249796dc55f4250831fbce7a3`

### 47. `hardcoded:src/utils/grokBuildConfig.ts:validateGrokBuildConfig:635935c049e3abfa:001`

- 状态：确认遗漏
- 文件：`src/utils/grokBuildConfig.ts:134`
- 结构：`validateGrokBuildConfig` / `string`
- 原文/表达式：config.toml must not be empty
- 判定原因：Grok Build 表单直接把该英文校验结果展示给用户，未经过 i18n。
- 处理方向：返回结构化错误码并在表单层本地化。
- 严重程度：中
- 指纹：`635935c049e3abfa7247fbd192cc4eb7265ad18cff7a3165d737ec491e3fab2c`

### 48. `hardcoded:src/utils/grokBuildConfig.ts:validateGrokBuildConfig:968d44e96bbf12f6:001`

- 状态：确认遗漏
- 文件：`src/utils/grokBuildConfig.ts:140`
- 结构：`validateGrokBuildConfig` / `string`
- 原文/表达式：Missing [models] default model table
- 判定原因：Grok Build 表单直接把该英文校验结果展示给用户，未经过 i18n。
- 处理方向：返回结构化错误码并在表单层本地化。
- 严重程度：中
- 指纹：`968d44e96bbf12f608276a5eced6afc50a8f4fef840e5eb40a52e7ad791610df`

### 49. `hardcoded:src/utils/grokBuildConfig.ts:validateGrokBuildConfig:2a3495bd745faa88:001`

- 状态：确认遗漏
- 文件：`src/utils/grokBuildConfig.ts:142`
- 结构：`validateGrokBuildConfig` / `template`
- 原文/表达式：`Missing ${field}`
- 判定原因：Grok Build 表单直接把该英文校验结果展示给用户，未经过 i18n。
- 处理方向：返回结构化错误码并在表单层本地化。
- 严重程度：中
- 指纹：`2a3495bd745faa8885ff841209ab8af13f6a2e3e22c7cf8884f9a67725e148da`

### 50. `hardcoded:src/utils/grokBuildConfig.ts:validateGrokBuildConfig:d431161f73c1ac64:001`

- 状态：确认遗漏
- 文件：`src/utils/grokBuildConfig.ts:148`
- 结构：`validateGrokBuildConfig` / `string`
- 原文/表达式：Missing api_key or env_key
- 判定原因：Grok Build 表单直接把该英文校验结果展示给用户，未经过 i18n。
- 处理方向：返回结构化错误码并在表单层本地化。
- 严重程度：中
- 指纹：`d431161f73c1ac6437b4d0b9a7ffd0c0ea3514cff3ccbae1b61a1958141b009f`

### 51. `hardcoded:src/utils/grokBuildConfig.ts:validateGrokBuildConfig:b7775baf7a5fdce9:001`

- 状态：确认遗漏
- 文件：`src/utils/grokBuildConfig.ts:156`
- 结构：`validateGrokBuildConfig` / `string`
- 原文/表达式：context_window must be a positive integer
- 判定原因：Grok Build 表单直接把该英文校验结果展示给用户，未经过 i18n。
- 处理方向：返回结构化错误码并在表单层本地化。
- 严重程度：中
- 指纹：`b7775baf7a5fdce95f61dff5e19343fc3cbb8e50fcc71cb4f79597e58856db12`

### 52. `hardcoded:src/utils/providerConfigUtils.ts:validateJsonConfig:148d195e21b05db5:001`

- 状态：确认遗漏
- 文件：`src/utils/providerConfigUtils.ts:15`
- 结构：`validateJsonConfig` / `string`
- 原文/表达式：配置
- 判定原因：供应商配置校验错误直接面向表单用户，未国际化。
- 处理方向：改为错误码/翻译键。
- 严重程度：中
- 指纹：`148d195e21b05db59551b5f85b09fed0c9b3b4c7562654815396d4f98af53328`

### 53. `hardcoded:src/utils/providerConfigUtils.ts:validateJsonConfig:639cb148b070e7fe:001`

- 状态：确认遗漏
- 文件：`src/utils/providerConfigUtils.ts:23`
- 结构：`validateJsonConfig` / `template`
- 原文/表达式：`${fieldName}必须是 JSON 对象`
- 判定原因：供应商配置校验错误直接面向表单用户，未国际化。
- 处理方向：改为错误码/翻译键。
- 严重程度：中
- 指纹：`639cb148b070e7fe5226b48b8369e5de2b69d8b08db5c7f3a39a5932a3532645`

### 54. `hardcoded:src/utils/providerConfigUtils.ts:validateJsonConfig:f97bc449d16f097d:001`

- 状态：确认遗漏
- 文件：`src/utils/providerConfigUtils.ts:27`
- 结构：`validateJsonConfig` / `template`
- 原文/表达式：`${fieldName}JSON格式错误，请检查语法`
- 判定原因：供应商配置校验错误直接面向表单用户，未国际化。
- 处理方向：改为错误码/翻译键。
- 严重程度：中
- 指纹：`f97bc449d16f097d3aea6632be3b35c38783c1ba9dd3aa8fa01cefbfd2b5e89a`

### 55. `hardcoded:src/utils/tomlUtils.ts:tomlToMcpServer:240c7ff86f1aecbb:001`

- 状态：确认遗漏
- 文件：`src/utils/tomlUtils.ts:55`
- 结构：`tomlToMcpServer` / `string`
- 原文/表达式：TOML 内容不能为空
- 判定原因：TOML/MCP 解析错误会反馈给用户，当前为硬编码中文。
- 处理方向：改为结构化错误码并通过 i18n 展示。
- 严重程度：中
- 指纹：`240c7ff86f1aecbb227873991becce122d47306bdd8a616c392308747d3657fb`

### 56. `hardcoded:src/utils/tomlUtils.ts:tomlToMcpServer:d98de4c622938e59:001`

- 状态：确认遗漏
- 文件：`src/utils/tomlUtils.ts:93`
- 结构：`tomlToMcpServer` / `string`
- 原文/表达式：无法识别的 TOML 格式。请提供单个 MCP 服务器配置，或使用 [mcp_servers.<id>] 格式
- 判定原因：TOML/MCP 解析错误会反馈给用户，当前为硬编码中文。
- 处理方向：改为结构化错误码并通过 i18n 展示。
- 严重程度：中
- 指纹：`d98de4c622938e596340b98d8fabc8679feda1bb76fd35500647753705bd1270`

### 57. `hardcoded:src/utils/tomlUtils.ts:normalizeServerConfig:b6499972805a260f:001`

- 状态：确认遗漏
- 文件：`src/utils/tomlUtils.ts:103`
- 结构：`normalizeServerConfig` / `string`
- 原文/表达式：服务器配置必须是对象
- 判定原因：TOML/MCP 解析错误会反馈给用户，当前为硬编码中文。
- 处理方向：改为结构化错误码并通过 i18n 展示。
- 严重程度：中
- 指纹：`b6499972805a260fe3f2d54f127303cd8e7adcc8610923b7b7a54968ea5e8888`

### 58. `hardcoded:src/utils/tomlUtils.ts:normalizeServerConfig:7a31ea38d57de345:001`

- 状态：确认遗漏
- 文件：`src/utils/tomlUtils.ts:113`
- 结构：`normalizeServerConfig` / `string`
- 原文/表达式：stdio 类型的 MCP 服务器必须包含 command 字段
- 判定原因：TOML/MCP 解析错误会反馈给用户，当前为硬编码中文。
- 处理方向：改为结构化错误码并通过 i18n 展示。
- 严重程度：中
- 指纹：`7a31ea38d57de345c57f8e5647bb7ad9a84fefa98fb31df5c5a9ef8c17d87da8`

### 59. `hardcoded:src/utils/tomlUtils.ts:normalizeServerConfig:628993c2cd0e3bf1:001`

- 状态：确认遗漏
- 文件：`src/utils/tomlUtils.ts:151`
- 结构：`normalizeServerConfig` / `template`
- 原文/表达式：`${type} 类型的 MCP 服务器必须包含 url 字段`
- 判定原因：TOML/MCP 解析错误会反馈给用户，当前为硬编码中文。
- 处理方向：改为结构化错误码并通过 i18n 展示。
- 严重程度：中
- 指纹：`628993c2cd0e3bf114744cfd3087de772b027995d3d5d1cce9373e6aedf965de`

### 60. `hardcoded:src/utils/tomlUtils.ts:normalizeServerConfig:36486ce84613bdea:001`

- 状态：确认遗漏
- 文件：`src/utils/tomlUtils.ts:180`
- 结构：`normalizeServerConfig` / `template`
- 原文/表达式：`不支持的 MCP 服务器类型: ${type}`
- 判定原因：TOML/MCP 解析错误会反馈给用户，当前为硬编码中文。
- 处理方向：改为结构化错误码并通过 i18n 展示。
- 严重程度：中
- 指纹：`36486ce84613bdeadf0b0958503e153090ca44c6811297bac8c23fb14a19372e`

## 待核实明细（557）

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

### 5. `hardcoded:src/App.tsx:duplicatedProvider:efdc2dc862a451d8:001`

- 状态：待核实
- 文件：`src/App.tsx:1120`
- 结构：`duplicatedProvider` / `template`
- 原文/表达式：`${provider.name} copy`
- 判定原因：该英文字符串“`${provider.name} copy`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`efdc2dc862a451d8d0191b12d29172b2e68bd1e019e3e245497774d15e58971e`

### 6. `hardcoded:src/App.tsx:handleDuplicateProvider:b6d02c61ff9c358e:001`

- 状态：待核实
- 文件：`src/App.tsx:1173`
- 结构：`handleDuplicateProvider` / `template`
- 原文/表达式：`: ${errorMessage}`
- 判定原因：该英文字符串“`: ${errorMessage}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b6d02c61ff9c358e11ab0b11fcbf983c2b65d33e89d407606060bd0be650b418`

### 7. `hardcoded:src/App.tsx:handleDuplicateProvider:fa141baa557cdc46:001`

- 状态：待核实
- 文件：`src/App.tsx:1200`
- 结构：`handleDuplicateProvider` / `template`
- 原文/表达式：`${duplicatedProvider.providerKey}/${key.startsWith(`${provider.id}/`) ? key.slice(provider.id.length + 1) : key}`
- 判定原因：该英文字符串“`${duplicatedProvider.providerKey}/${key.startsWith(`${provider.id}/`) ? key.slice(provider.id.length + 1) : key}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fa141baa557cdc463bcb34459fe1ab3f5830e53e408b85b9257b131f7fdaeb1d`

### 8. `hardcoded:src/components/DatabaseUpgrade.tsx:DatabaseUpgrade:96019d7f543d5d45:001`

- 状态：待核实
- 文件：`src/components/DatabaseUpgrade.tsx:235`
- 结构：`DatabaseUpgrade` / `template`
- 原文/表达式：` / ${fmtMB(progress.total)} MB`
- 判定原因：该英文字符串“` / ${fmtMB(progress.total)} MB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`96019d7f543d5d4552d9c21f3e7072b5fa79eb82a8e0e88566d578678dcda9cd`

### 9. `hardcoded:src/components/DeepLinkImportDialog.tsx:maskedApiKey:1f0f80da914365a2:001`

- 状态：待核实
- 文件：`src/components/DeepLinkImportDialog.tsx:386`
- 结构：`maskedApiKey` / `template`
- 原文/表达式：`${request.apiKey.substring(0, 4)}${"*".repeat(20)}`
- 判定原因：该英文字符串“`${request.apiKey.substring(0, 4)}${"*".repeat(20)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1f0f80da914365a220efd3e94eaf0ea65bdd28426fd1cb63e78c441332c25488`

### 10. `dynamic-i18n:src/components/DeepLinkImportDialog.tsx:DeepLinkImportDialog:dfdad65bcce899e6:001`

- 状态：待核实
- 文件：`src/components/DeepLinkImportDialog.tsx:575`
- 结构：`DeepLinkImportDialog` / `dynamic_i18n_key`
- 原文/表达式：riskI18nKey(endpointRisk)
- 判定原因：翻译键由运行时表达式“riskI18nKey(endpointRisk)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`dfdad65bcce899e6341ac9fb04a16b9a165a38c0c0a5341e9df1076f6d4bac0f`

### 11. `hardcoded:src/components/DeepLinkImportDialog.tsx:DeepLinkImportDialog:4689fe1c9f813640:001`

- 状态：待核实
- 文件：`src/components/DeepLinkImportDialog.tsx:905`
- 结构：`DeepLinkImportDialog` / `template`
- 原文/表达式：`${request.usageApiKey.substring(0, 4)}${"*".repeat(12)}`
- 判定原因：该英文字符串“`${request.usageApiKey.substring(0, 4)}${"*".repeat(12)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4689fe1c9f8136400d0496d8ae0148a9839c61a8c3ef8d17e3299e38d4a46943`

### 12. `hardcoded:src/components/DeepLinkImportDialog.tsx:DeepLinkImportDialog:dd1cb78915b1fd59:001`

- 状态：待核实
- 文件：`src/components/DeepLinkImportDialog.tsx:936`
- 结构：`DeepLinkImportDialog` / `template`
- 原文/表达式：`${request.usageAccessToken.substring(0, 4)}${"*".repeat(12)}`
- 判定原因：该英文字符串“`${request.usageAccessToken.substring(0, 4)}${"*".repeat(12)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`dd1cb78915b1fd5934a0a4c6d131e722deed437c4c594b9ec5aefa02d924fdd5`

### 13. `dynamic-i18n:src/components/IconPicker.tsx:handleFileChange:16fefef2206f4fc1:001`

- 状态：待核实
- 文件：`src/components/IconPicker.tsx:116`
- 结构：`handleFileChange` / `dynamic_i18n_key`
- 原文/表达式：`iconPicker.uploadError.${code}`
- 判定原因：翻译键由运行时表达式“`iconPicker.uploadError.${code}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`16fefef2206f4fc17164e7f45bdfee2456257b2d9e91e15a66dc0b147119a614`

### 14. `hardcoded:src/components/JsonEditor.tsx:baseTheme:b526669093ff1ced:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:156`
- 结构：`baseTheme` / `string`
- 原文/表达式：1px solid hsl(var(--border))
- 判定原因：该英文字符串“1px solid hsl(var(--border))”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b526669093ff1cedb320b8b8fa8ac9f3aef7add6d0aff313f8d3bfdb448a6c3f`

### 15. `hardcoded:src/components/JsonEditor.tsx:baseTheme:b526669093ff1ced:002`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:169`
- 结构：`baseTheme` / `string`
- 原文/表达式：1px solid hsl(var(--border))
- 判定原因：该英文字符串“1px solid hsl(var(--border))”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b526669093ff1cedb320b8b8fa8ac9f3aef7add6d0aff313f8d3bfdb448a6c3f`

### 16. `hardcoded:src/components/JsonEditor.tsx:baseTheme:00079d61aabef6cd:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:172`
- 结构：`baseTheme` / `string`
- 原文/表达式：.cm-selectionBackground, .cm-content ::selection
- 判定原因：该英文字符串“.cm-selectionBackground, .cm-content ::selection”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`00079d61aabef6cd94e2d65cfc72d77cdf15e8a73238038391eb96790ad56fa4`

### 17. `hardcoded:src/components/JsonEditor.tsx:baseTheme:f2ce477a87688125:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:173`
- 结构：`baseTheme` / `string`
- 原文/表达式：hsl(var(--primary) / 0.18)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.18)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f2ce477a87688125ce091bdfe93639564f19c6b34c54f66e3fad5664b706c84d`

### 18. `hardcoded:src/components/JsonEditor.tsx:baseTheme:133c9f619bb5ead3:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:176`
- 结构：`baseTheme` / `string`
- 原文/表达式：hsl(var(--primary) / 0.12)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.12)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`133c9f619bb5ead3accccc6dbc85f1c8884f6df2c4268dc114a1abc59b1f352d`

### 19. `hardcoded:src/components/JsonEditor.tsx:baseTheme:c4b4a4d89aa6ed5e:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:179`
- 结构：`baseTheme` / `string`
- 原文/表达式：hsl(var(--primary) / 0.08)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.08)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c4b4a4d89aa6ed5ebc17ea88aa52cdd6228ca467fac99e5bd86627b016822b26`

### 20. `hardcoded:src/components/JsonEditor.tsx:baseTheme:c4b4a4d89aa6ed5e:002`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:182`
- 结构：`baseTheme` / `string`
- 原文/表达式：hsl(var(--primary) / 0.08)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.08)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c4b4a4d89aa6ed5ebc17ea88aa52cdd6228ca467fac99e5bd86627b016822b26`

### 21. `hardcoded:src/components/JsonEditor.tsx:sizingTheme:e32cda8c0d120e75:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:194`
- 结构：`sizingTheme` / `string`
- 原文/表达式：ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace
- 判定原因：该英文字符串“ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e32cda8c0d120e755364c4ebd8c51be48a4a623329d216cdbfb5febe7ad81664`

### 22. `hardcoded:src/components/JsonEditor.tsx:JsonEditor:b526669093ff1ced:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:226`
- 结构：`JsonEditor` / `string`
- 原文/表达式：1px solid hsl(var(--border))
- 判定原因：该英文字符串“1px solid hsl(var(--border))”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b526669093ff1cedb320b8b8fa8ac9f3aef7add6d0aff313f8d3bfdb448a6c3f`

### 23. `hardcoded:src/components/JsonEditor.tsx:JsonEditor:b526669093ff1ced:002`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:239`
- 结构：`JsonEditor` / `string`
- 原文/表达式：1px solid hsl(var(--border))
- 判定原因：该英文字符串“1px solid hsl(var(--border))”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b526669093ff1cedb320b8b8fa8ac9f3aef7add6d0aff313f8d3bfdb448a6c3f`

### 24. `hardcoded:src/components/JsonEditor.tsx:JsonEditor:00079d61aabef6cd:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:242`
- 结构：`JsonEditor` / `string`
- 原文/表达式：.cm-selectionBackground, .cm-content ::selection
- 判定原因：该英文字符串“.cm-selectionBackground, .cm-content ::selection”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`00079d61aabef6cd94e2d65cfc72d77cdf15e8a73238038391eb96790ad56fa4`

### 25. `hardcoded:src/components/JsonEditor.tsx:JsonEditor:f2ce477a87688125:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:243`
- 结构：`JsonEditor` / `string`
- 原文/表达式：hsl(var(--primary) / 0.18)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.18)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f2ce477a87688125ce091bdfe93639564f19c6b34c54f66e3fad5664b706c84d`

### 26. `hardcoded:src/components/JsonEditor.tsx:JsonEditor:133c9f619bb5ead3:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:246`
- 结构：`JsonEditor` / `string`
- 原文/表达式：hsl(var(--primary) / 0.12)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.12)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`133c9f619bb5ead3accccc6dbc85f1c8884f6df2c4268dc114a1abc59b1f352d`

### 27. `hardcoded:src/components/JsonEditor.tsx:JsonEditor:c4b4a4d89aa6ed5e:001`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:249`
- 结构：`JsonEditor` / `string`
- 原文/表达式：hsl(var(--primary) / 0.08)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.08)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c4b4a4d89aa6ed5ebc17ea88aa52cdd6228ca467fac99e5bd86627b016822b26`

### 28. `hardcoded:src/components/JsonEditor.tsx:JsonEditor:c4b4a4d89aa6ed5e:002`

- 状态：待核实
- 文件：`src/components/JsonEditor.tsx:252`
- 结构：`JsonEditor` / `string`
- 原文/表达式：hsl(var(--primary) / 0.08)
- 判定原因：该英文字符串“hsl(var(--primary) / 0.08)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c4b4a4d89aa6ed5ebc17ea88aa52cdd6228ca467fac99e5bd86627b016822b26`

### 29. `hardcoded:src/components/MarkdownEditor.tsx:baseTheme:e32cda8c0d120e75:001`

- 状态：待核实
- 文件：`src/components/MarkdownEditor.tsx:45`
- 结构：`baseTheme` / `string`
- 原文/表达式：ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace
- 判定原因：该英文字符串“ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e32cda8c0d120e755364c4ebd8c51be48a4a623329d216cdbfb5febe7ad81664`

### 30. `hardcoded:src/components/MarkdownEditor.tsx:baseTheme:c05176e6e7136a09:001`

- 状态：待核实
- 文件：`src/components/MarkdownEditor.tsx:48`
- 结构：`baseTheme` / `string`
- 原文/表达式：&light .cm-content, &dark .cm-content
- 判定原因：该英文字符串“&light .cm-content, &dark .cm-content”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c05176e6e7136a092820bc0e067cdbd97345f8b58adb9a733047a3712244c08c`

### 31. `hardcoded:src/components/MarkdownEditor.tsx:baseTheme:cbabaa1ff400c8a9:001`

- 状态：待核实
- 文件：`src/components/MarkdownEditor.tsx:51`
- 结构：`baseTheme` / `string`
- 原文/表达式：&light .cm-editor, &dark .cm-editor
- 判定原因：该英文字符串“&light .cm-editor, &dark .cm-editor”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`cbabaa1ff400c8a95e9e26245a8248e3e4a056ee7376f2123a6cb9d0cd1674a6`

### 32. `hardcoded:src/components/ProviderIcon.tsx:fallbackFontSize:0295b0c36d914862:001`

- 状态：待核实
- 文件：`src/components/ProviderIcon.tsx:121`
- 结构：`fallbackFontSize` / `template`
- 原文/表达式：`${Math.max(size * 0.5, 12)}px`
- 判定原因：该英文字符串“`${Math.max(size * 0.5, 12)}px`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0295b0c36d91486239274f3ce34d8a756ced28b7bbd728d6ac60b506da3fcd0d`

### 33. `dynamic-i18n:src/components/SubscriptionQuotaFooter.tsx:tierLabel:594c5d7f4330650b:001`

- 状态：待核实
- 文件：`src/components/SubscriptionQuotaFooter.tsx:129`
- 结构：`tierLabel` / `dynamic_i18n_key`
- 原文/表达式：TIER_I18N_KEYS[name]
- 判定原因：翻译键由运行时表达式“TIER_I18N_KEYS[name]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`594c5d7f4330650b8869a1eff51f6e2fe4a277881c240a0a19e4b91e46dac546`

### 34. `dynamic-i18n:src/components/SubscriptionQuotaFooter.tsx:tierShortLabel:cc8832922601ce1f:001`

- 状态：待核实
- 文件：`src/components/SubscriptionQuotaFooter.tsx:135`
- 结构：`tierShortLabel` / `dynamic_i18n_key`
- 原文/表达式：key.replace("subscription.", "subscription.short.")
- 判定原因：翻译键由运行时表达式“key.replace("subscription.", "subscription.short.")”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cc8832922601ce1f1074be0045da3942eed6b0d23f9618bb02fdf597641e861b`

### 35. `dynamic-i18n:src/components/SubscriptionQuotaFooter.tsx:label:ad936fcbed631fa6:001`

- 状态：待核实
- 文件：`src/components/SubscriptionQuotaFooter.tsx:152`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：group
- 判定原因：翻译键由运行时表达式“group”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ad936fcbed631fa67e05c3ea03953905221c9d46af0616b70badf105a966fb11`

### 36. `hardcoded:src/components/UsageFooter.tsx:key:9362b5b84393faf0:001`

- 状态：待核实
- 文件：`src/components/UsageFooter.tsx:64`
- 结构：`key` / `template`
- 原文/表达式：`${index}-${data.planName ?? ""}`
- 判定原因：该英文字符串“`${index}-${data.planName ?? ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9362b5b84393faf07321373fd9ad946ae174ef83bc648088c02d41bf49698fe8`

### 37. `hardcoded:src/components/UsageFooter.tsx:amount:272d40f9ddbe07f5:001`

- 状态：待核实
- 文件：`src/components/UsageFooter.tsx:66`
- 结构：`amount` / `template`
- 原文/表达式：`${value === -1 ? "∞" : value.toFixed(2)}${data.unit ? ` ${data.unit}` : ""}`
- 判定原因：该英文字符串“`${value === -1 ? "∞" : value.toFixed(2)}${data.unit ? ` ${data.unit}` : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`272d40f9ddbe07f503c96770f5bd6f53d274e0c90a9afea654f787400db3dc01`

### 38. `hardcoded:src/components/UsageFooter.tsx:amount:1c0605d00a26c685:001`

- 状态：待核实
- 文件：`src/components/UsageFooter.tsx:66`
- 结构：`amount` / `template`
- 原文/表达式：` ${data.unit}`
- 判定原因：该英文字符串“` ${data.unit}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1c0605d00a26c685620ce3f86006981b212a7a23bef2211d7de973c55ab2e1a3`

### 39. `hardcoded:src/components/UsageFooter.tsx:detail:632b5e14fd752866:001`

- 状态：待核实
- 文件：`src/components/UsageFooter.tsx:69`
- 结构：`detail` / `template`
- 原文/表达式：`${t("usage.total")} ${amount(data.total)}`
- 判定原因：该英文字符串“`${t("usage.total")} ${amount(data.total)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`632b5e14fd7528662e60320a23b31fc8250c1715da919fb697a7ff9a3ada6a49`

### 40. `hardcoded:src/components/UsageFooter.tsx:detail:9836ac80e6765d0a:001`

- 状态：待核实
- 文件：`src/components/UsageFooter.tsx:70`
- 结构：`detail` / `template`
- 原文/表达式：`${t("usage.used")} ${amount(data.used)}`
- 判定原因：该英文字符串“`${t("usage.used")} ${amount(data.used)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9836ac80e6765d0ac80426b2b3aa31802e0e0143849f0071aa3c590a2f1b2b96`

### 41. `hardcoded:src/components/UsageFooter.tsx:planLine:9836ac80e6765d0a:001`

- 状态：待核实
- 文件：`src/components/UsageFooter.tsx:93`
- 结构：`planLine` / `template`
- 原文/表达式：`${t("usage.used")} ${amount(data.used)}`
- 判定原因：该英文字符串“`${t("usage.used")} ${amount(data.used)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9836ac80e6765d0ac80426b2b3aa31802e0e0143849f0071aa3c590a2f1b2b96`

### 42. `dynamic-i18n:src/components/UsageScriptModal.tsx:UsageScriptModal:f52cef484535047b:001`

- 状态：待核实
- 文件：`src/components/UsageScriptModal.tsx:988`
- 结构：`UsageScriptModal` / `dynamic_i18n_key`
- 原文/表达式：TEMPLATE_NAME_KEYS[name]
- 判定原因：翻译键由运行时表达式“TEMPLATE_NAME_KEYS[name]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`f52cef484535047b84076cc20d0d6ab8a036bf7c19ac95a1e96bd959dce84ce0`

### 43. `dynamic-i18n:src/components/WhatsNewDialog.tsx:WhatsNewDialog:3f85b3caaa1db65c:001`

- 状态：待核实
- 文件：`src/components/WhatsNewDialog.tsx:123`
- 结构：`WhatsNewDialog` / `dynamic_i18n_key`
- 原文/表达式：`whatsNew.types.${item.type}`
- 判定原因：翻译键由运行时表达式“`whatsNew.types.${item.type}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`3f85b3caaa1db65c266a4b88be6939885791f7c36060642eee5f98ac55453a1d`

### 44. `hardcoded:src/components/apps/AppsPage.tsx:APP_ROW_GRID:7f012046c274f80a:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:157`
- 结构：`APP_ROW_GRID` / `string`
- 原文/表达式：grid grid-cols-[minmax(0,1fr)_168px_var(--apps-actions-width,0px)_56px_28px] items-center gap-x-4
- 判定原因：该英文字符串“grid grid-cols-[minmax(0,1fr)_168px_var(--apps-actions-width,0px)_56px_28px] items-center gap-x-4”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7f012046c274f80a8894ec7bc2a343a5afae4223b8d358c07a2b7c9df9ad4e11`

### 45. `hardcoded:src/components/apps/AppsPage.tsx:formatCheckedAt:eac4e940aeeff445:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:168`
- 结构：`formatCheckedAt` / `template`
- 原文/表达式：`${date.toLocaleDateString(locale, { month: "numeric", day: "numeric" })} ${time}`
- 判定原因：该英文字符串“`${date.toLocaleDateString(locale, { month: "numeric", day: "numeric" })} ${time}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`eac4e940aeeff4450e7e3cc40432e540f556df39c0f33a06424d98e95dcb4cda`

### 46. `dynamic-i18n:src/components/apps/AppsPage.tsx:sections:88b10ec29471d286:001`

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

### 47. `hardcoded:src/components/apps/AppsPage.tsx:envBadge:2dd110cb1990361d:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:749`
- 结构：`envBadge` / `template`
- 原文/表达式：`${t(ENV_BADGE_CONFIG.wsl.labelKey)}${info.wsl_distro ? ` · ${info.wsl_distro}` : ""}`
- 判定原因：该英文字符串“`${t(ENV_BADGE_CONFIG.wsl.labelKey)}${info.wsl_distro ? ` · ${info.wsl_distro}` : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2dd110cb1990361d6b2dd2db2dc6891012b42fbf449f5c15b2d234ac077c8276`

### 48. `dynamic-i18n:src/components/apps/AppsPage.tsx:envBadge:cfc322af6c201189:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:749`
- 结构：`envBadge` / `dynamic_i18n_key`
- 原文/表达式：ENV_BADGE_CONFIG.wsl.labelKey
- 判定原因：翻译键由运行时表达式“ENV_BADGE_CONFIG.wsl.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cfc322af6c20118946129fe571601732b788bf744b7587675baf8f51ca169d3f`

### 49. `hardcoded:src/components/apps/AppsPage.tsx:envBadge:fe929c298d19df00:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:749`
- 结构：`envBadge` / `template`
- 原文/表达式：` · ${info.wsl_distro}`
- 判定原因：该英文字符串“` · ${info.wsl_distro}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fe929c298d19df002764ac0fcc4bd95d3f96f569c9af11777411f4f0aa026742`

### 50. `dynamic-i18n:src/components/apps/AppsPage.tsx:installHint:a7313ac9d3fdc954:001`

- 状态：待核实
- 文件：`src/components/apps/AppsPage.tsx:801`
- 结构：`installHint` / `dynamic_i18n_key`
- 原文/表达式：`appsPage.installHint.${tool}`
- 判定原因：翻译键由运行时表达式“`appsPage.installHint.${tool}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a7313ac9d3fdc95467738f3e8d22bfc93d7f9b14c75fe5c47b7ec556ceb63883`

### 51. `hardcoded:src/components/apps/ManualUninstallDialog.tsx:environmentLabelForTool:94385bfc2ba7421b:001`

- 状态：待核实
- 文件：`src/components/apps/ManualUninstallDialog.tsx:72`
- 结构：`environmentLabelForTool` / `template`
- 原文/表达式：`WSL · ${info.wsl_distro}`
- 判定原因：该英文字符串“`WSL · ${info.wsl_distro}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`94385bfc2ba7421bead570d98aebcb55e2188e7639d00d856d22ea77de2ea5bc`

### 52. `hardcoded:src/components/apps/ManualUninstallDialog.tsx:ManualUninstallDialog:9a2afcf76256a500:001`

- 状态：待核实
- 文件：`src/components/apps/ManualUninstallDialog.tsx:172`
- 结构：`ManualUninstallDialog` / `template`
- 原文/表达式：` (${variant})`
- 判定原因：该英文字符串“` (${variant})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9a2afcf76256a50095dbe8262463ad8980a29cdc6ab0c9df756bc3630d8faaa3`

### 53. `hardcoded:src/components/apps/useToolManagement.ts:posixScriptInstallCommand:ac5e91f05ec20efe:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:106`
- 结构：`posixScriptInstallCommand` / `template`
- 原文/表达式：`bash -c 'tmp=$(mktemp) && curl -fsSL ${url} -o $tmp && bash $tmp; status=$?; rm -f $tmp; exit $status'`
- 判定原因：该英文字符串“`bash -c 'tmp=$(mktemp) && curl -fsSL ${url} -o $tmp && bash $tmp; status=$?; rm -f $tmp; exit $status'`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ac5e91f05ec20efe85d89714c0f3bde6634f98e55548db73093ad63e593eb56b`

### 54. `hardcoded:src/components/apps/useToolManagement.ts:HERMES_WINDOWS_INSTALL_SCRIPT:036ec285e5e368b4:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:109`
- 结构：`HERMES_WINDOWS_INSTALL_SCRIPT` / `string`
- 原文/表达式：irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 \| iex
- 判定原因：该英文字符串“irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`036ec285e5e368b43375dc25386c36e1e02fce37adcb5996a6a3e2aae72811d8`

### 55. `hardcoded:src/components/apps/useToolManagement.ts:HERMES_WINDOWS_INSTALL_COMMAND:1a14b43a642f417d:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:120`
- 结构：`HERMES_WINDOWS_INSTALL_COMMAND` / `template`
- 原文/表达式：`powershell -NoProfile -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(<br>  HERMES_WINDOWS_INSTALL_SCRIPT,<br>)}`
- 判定原因：该英文字符串“`powershell -NoProfile -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(
  HERMES_WINDOWS_INSTALL_SCRIPT,
)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1a14b43a642f417d35f3640a1bc3af535d050fc27591cd198a2733ff15dc5ab1`

### 56. `hardcoded:src/components/apps/useToolManagement.ts:MCODE_WINDOWS_INSTALL_COMMAND:d75acf25340b91af:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:124`
- 结构：`MCODE_WINDOWS_INSTALL_COMMAND` / `template`
- 原文/表达式：`powershell -NoProfile -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(<br>  "irm https://filecdn.minimax.chat/public/install.ps1 \| iex",<br>)}`
- 判定原因：该英文字符串“`powershell -NoProfile -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(
  "irm https://filecdn.minimax.chat/public/install.ps1 | iex",
)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d75acf25340b91af1db58e92246105b39dcf35cd2c848d5f68744cfa0a1c998f`

### 57. `hardcoded:src/components/apps/useToolManagement.ts:MCODE_WINDOWS_INSTALL_COMMAND:02fdf84a68f89170:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:125`
- 结构：`MCODE_WINDOWS_INSTALL_COMMAND` / `string`
- 原文/表达式：irm https://filecdn.minimax.chat/public/install.ps1 \| iex
- 判定原因：该英文字符串“irm https://filecdn.minimax.chat/public/install.ps1 | iex”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`02fdf84a68f891706db8cc9700fb0986d94f992bd81f9e6ba6a2aa1f3524ba06`

### 58. `hardcoded:src/components/apps/useToolManagement.ts:KIMI_WINDOWS_INSTALL_COMMAND:f56dac5c58fa85df:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:128`
- 结构：`KIMI_WINDOWS_INSTALL_COMMAND` / `template`
- 原文/表达式：`powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(<br>  "irm https://code.kimi.com/kimi-code/install.ps1 \| iex",<br>)}`
- 判定原因：该英文字符串“`powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(
  "irm https://code.kimi.com/kimi-code/install.ps1 | iex",
)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f56dac5c58fa85df3810c6e0718b9bd96c670bac0d019a4067458515beaa64b1`

### 59. `hardcoded:src/components/apps/useToolManagement.ts:KIMI_WINDOWS_INSTALL_COMMAND:e30ca1e94fd4ceef:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:129`
- 结构：`KIMI_WINDOWS_INSTALL_COMMAND` / `string`
- 原文/表达式：irm https://code.kimi.com/kimi-code/install.ps1 \| iex
- 判定原因：该英文字符串“irm https://code.kimi.com/kimi-code/install.ps1 | iex”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e30ca1e94fd4ceefef017b7ff570e74b58041131444f048c814889ad08dacdfc`

### 60. `hardcoded:src/components/apps/useToolManagement.ts:AGY_WINDOWS_INSTALL_COMMAND:2fbd97be8e0b20e9:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:132`
- 结构：`AGY_WINDOWS_INSTALL_COMMAND` / `template`
- 原文/表达式：`powershell -NoProfile -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(<br>  "irm https://antigravity.google/cli/install.ps1 \| iex",<br>)}`
- 判定原因：该英文字符串“`powershell -NoProfile -ExecutionPolicy Bypass -EncodedCommand ${powershellEncodedCommand(
  "irm https://antigravity.google/cli/install.ps1 | iex",
)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2fbd97be8e0b20e97f59eb115764832526ac4f3b1f1ae48725e65bcb8400fa6d`

### 61. `hardcoded:src/components/apps/useToolManagement.ts:AGY_WINDOWS_INSTALL_COMMAND:58690d86ff0bfe2b:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:133`
- 结构：`AGY_WINDOWS_INSTALL_COMMAND` / `string`
- 原文/表达式：irm https://antigravity.google/cli/install.ps1 \| iex
- 判定原因：该英文字符串“irm https://antigravity.google/cli/install.ps1 | iex”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`58690d86ff0bfe2b02f17453244484c47b9f9572c22ad4b99cc5709f49327ca9`

### 62. `hardcoded:src/components/apps/useToolManagement.ts:MCODE_NPM_INSTALL_COMMAND:6f64ecd0cbd433ff:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:144`
- 结构：`MCODE_NPM_INSTALL_COMMAND` / `string`
- 原文/表达式：npm i -g @minimax-ai/code@latest --ignore-scripts=false --include=optional "--allow-scripts=@minimax-ai/code,better-sqlite3"
- 判定原因：该英文字符串“npm i -g @minimax-ai/code@latest --ignore-scripts=false --include=optional "--allow-scripts=@minimax-ai/code,better-sqlite3"”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6f64ecd0cbd433ff3688016a95ef72911eb1c8dab4091b7bf7d03ae7398bb040`

### 63. `hardcoded:src/components/apps/useToolManagement.ts:failureDescription:e82e31794a97d93d:001`

- 状态：待核实
- 文件：`src/components/apps/useToolManagement.ts:840`
- 结构：`failureDescription` / `template`
- 原文/表达式：`${TOOL_DISPLAY_NAMES[f.toolName]}: ${lastLine(f.detail)}`
- 判定原因：该英文字符串“`${TOOL_DISPLAY_NAMES[f.toolName]}: ${lastLine(f.detail)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e82e31794a97d93d0ee868b95dc025b2ae2253fb0672682651200e5516bd23dd`

### 64. `dynamic-i18n:src/components/apps/useToolManagement.ts:executeRun:fa889cec796591ae:001`

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

### 65. `hardcoded:src/components/common/AppToggleGroup.tsx:AppToggleGroup:9082376c2ee7a698:001`

- 状态：待核实
- 文件：`src/components/common/AppToggleGroup.tsx:27`
- 结构：`AppToggleGroup` / `template`
- 原文/表达式：`${label}${enabled ? " ✓" : ""}`
- 判定原因：该英文字符串“`${label}${enabled ? " ✓" : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9082376c2ee7a698eb414ed4c59f91d2af4863761c909f4023e5bd149f86d814`

### 66. `hardcoded:src/components/deeplink/McpConfirmation.tsx:McpConfirmation:35da9ae11afebfb5:001`

- 状态：待核实
- 文件：`src/components/deeplink/McpConfirmation.tsx:142`
- 结构：`McpConfirmation` / `template`
- 原文/表达式：`${key}=${maskValue(key, String(value))}`
- 判定原因：该英文字符串“`${key}=${maskValue(key, String(value))}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`35da9ae11afebfb5323b8f89fd223456af591e09fdced2e0c311353a1b51c09a`

### 67. `dynamic-i18n:src/components/deeplink/McpConfirmation.tsx:McpConfirmation:d7f7b8d4887c79a0:001`

- 状态：待核实
- 文件：`src/components/deeplink/McpConfirmation.tsx:161`
- 结构：`McpConfirmation` / `dynamic_i18n_key`
- 原文/表达式：riskI18nKey(kind)
- 判定原因：翻译键由运行时表达式“riskI18nKey(kind)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d7f7b8d4887c79a0de17ef5158c37ad4cf32609e660350c71f01326dd264af1d`

### 68. `hardcoded:src/components/hermes/HermesMemoryPanel.tsx:memoryFilePath:481b09631c288ecf:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:59`
- 结构：`memoryFilePath` / `template`
- 原文/表达式：`${dir.replace(/[\\/]+$/, "")}${sep}memories${sep}${file}`
- 判定原因：该英文字符串“`${dir.replace(/[\\/]+$/, "")}${sep}memories${sep}${file}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`481b09631c288ecf74a977eea2a130038896a82074717902feeee44356365a06`

### 69. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:name:75356b9afb016217:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:119`
- 结构：`name` / `dynamic_i18n_key`
- 原文/表达式：meta.nameKey
- 判定原因：翻译键由运行时表达式“meta.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`75356b9afb01621774bc813d1d21c3f8a9da401b6627205fa24ff6106a671d06`

### 70. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:handleToggle:7663f326f8433d18:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:146`
- 结构：`handleToggle` / `dynamic_i18n_key`
- 原文/表达式：next ? "hermes.memory.toggledOn" : "hermes.memory.toggledOff"
- 判定原因：翻译键由运行时表达式“next ? "hermes.memory.toggledOn" : "hermes.memory.toggledOff"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`7663f326f8433d188375fc655defeac94f6915774b979d2dd3a14cbee2063eb1`

### 71. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:MemoryTabPane:8fb010723006dfa3:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:175`
- 结构：`MemoryTabPane` / `dynamic_i18n_key`
- 原文/表达式：meta.descKey
- 判定原因：翻译键由运行时表达式“meta.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8fb010723006dfa36c05d41cacd6c24d2b8cd98441b1c4cc824670f19b9bf700`

### 72. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:MemoryTabPane:51f6c463686ee31f:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:208`
- 结构：`MemoryTabPane` / `dynamic_i18n_key`
- 原文/表达式：meta.placeholderKey
- 判定原因：翻译键由运行时表达式“meta.placeholderKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`51f6c463686ee31f6081657b2c9e2ed0f07612d1b172800f059acf7475979176`

### 73. `dynamic-i18n:src/components/hermes/HermesMemoryPanel.tsx:HermesMemoryPanel:43ecfa8432d123f8:001`

- 状态：待核实
- 文件：`src/components/hermes/HermesMemoryPanel.tsx:300`
- 结构：`HermesMemoryPanel` / `dynamic_i18n_key`
- 原文/表达式：KIND_META[kind].nameKey
- 判定原因：翻译键由运行时表达式“KIND_META[kind].nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`43ecfa8432d123f8c6578042a3deaf5b4ce608d8c09b5f4e9b40bb7217247d31`

### 74. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:fieldErrorText:c2af3397f931d9d7:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:206`
- 结构：`fieldErrorText` / `dynamic_i18n_key`
- 原文/表达式：`mcpPage.drawer.errors.${code}`
- 判定原因：翻译键由运行时表达式“`mcpPage.drawer.errors.${code}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c2af3397f931d9d7d775675a0d91f651bfe460fa4b610fc2f28d156b68e06c23`

### 75. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:formatLabel:365b5da25b0130b9:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:210`
- 结构：`formatLabel` / `dynamic_i18n_key`
- 原文/表达式：`mcpPage.drawer.pasteFormats.${format}`
- 判定原因：翻译键由运行时表达式“`mcpPage.drawer.pasteFormats.${format}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`365b5da25b0130b97d4166f1b4ed9112b3781abb292013a91f5eb9c31b80b853`

### 76. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:McpFormModal:110e6c2fccad7e63:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:659`
- 结构：`McpFormModal` / `dynamic_i18n_key`
- 原文/表达式：`mcp.presets.${preset.id}.description`
- 判定原因：翻译键由运行时表达式“`mcp.presets.${preset.id}.description`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`110e6c2fccad7e63497c8d59fc75f0c8538d7d985c7020f437e6854c17fb8048`

### 77. `dynamic-i18n:src/components/mcp/McpFormModal.tsx:McpFormModal:b38b4246acafdcdc:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:668`
- 结构：`McpFormModal` / `dynamic_i18n_key`
- 原文/表达式：`mcpPage.templateLabels.${preset.id}`
- 判定原因：翻译键由运行时表达式“`mcpPage.templateLabels.${preset.id}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b38b4246acafdcdcbc1a744cfaa372d515996efc14f9eed16a8aeeb457324b42`

### 78. `hardcoded:src/components/mcp/McpFormModal.tsx:McpFormModal:c28bf4f117f283bc:001`

- 状态：待核实
- 文件：`src/components/mcp/McpFormModal.tsx:1177`
- 结构：`McpFormModal` / `template`
- 原文/表达式：` ${t("mcpPage.drawer.jsonBlocksForm")}`
- 判定原因：该英文字符串“` ${t("mcpPage.drawer.jsonBlocksForm")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c28bf4f117f283bc46f5f3191dcfb6b042496e5792e0e94ef05c2ccb8bf3d300`

### 79. `dynamic-i18n:src/components/mcp/UnifiedMcpPanel.tsx:UnifiedMcpPanel:947324ed6a00ba24:001`

- 状态：待核实
- 文件：`src/components/mcp/UnifiedMcpPanel.tsx:940`
- 结构：`UnifiedMcpPanel` / `dynamic_i18n_key`
- 原文/表达式：`appMatrix.cell.${state}`
- 判定原因：翻译键由运行时表达式“`appMatrix.cell.${state}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`947324ed6a00ba241dcc93e16c9b7022385f2e299608f805663901480e1d6454`

### 80. `dynamic-i18n:src/components/mcp/UnifiedMcpPanel.tsx:UnifiedMcpPanel:d9d6a85445fe9b7e:001`

- 状态：待核实
- 文件：`src/components/mcp/UnifiedMcpPanel.tsx:1143`
- 结构：`UnifiedMcpPanel` / `dynamic_i18n_key`
- 原文/表达式：IMPORT_SOURCE_FILES[app].noteKey as string
- 判定原因：翻译键由运行时表达式“IMPORT_SOURCE_FILES[app].noteKey as string”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d9d6a85445fe9b7e4c33f649bfe9bc029ac989a37e98f491405a5fb4c42718c1`

### 81. `hardcoded:src/components/mcp/formBits.tsx:FIELD_CLASS:21e107b21a425660:001`

- 状态：待核实
- 文件：`src/components/mcp/formBits.tsx:124`
- 结构：`FIELD_CLASS` / `string`
- 原文/表达式：h-8 min-w-0 read-only:bg-subtle read-only:text-fg-2 dark:[color-scheme:dark]
- 判定原因：该英文字符串“h-8 min-w-0 read-only:bg-subtle read-only:text-fg-2 dark:[color-scheme:dark]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`21e107b21a42566023fb33d9df9d107493980ae700928a8119d3e05fae24d070`

### 82. `hardcoded:src/components/mcp/mcpDraft.ts:recognizePaste:7a24c8c64468bead:001`

- 状态：待核实
- 文件：`src/components/mcp/mcpDraft.ts:290`
- 结构：`recognizePaste` / `template`
- 原文/表达式：`{${trimmed.replace(/,\s*$/, "")}}`
- 判定原因：该英文字符串“`{${trimmed.replace(/,\s*$/, "")}}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7a24c8c64468beadb562f97001f3f5d728260d1f954ef1e10c2125003c2f1e40`

### 83. `hardcoded:src/components/openclaw/OpenClawHealthBanner.tsx:OpenClawHealthBanner:7fadb5dcf32dcf48:001`

- 状态：待核实
- 文件：`src/components/openclaw/OpenClawHealthBanner.tsx:77`
- 结构：`OpenClawHealthBanner` / `template`
- 原文/表达式：`${warning.code}:${warning.path ?? warning.message}`
- 判定原因：该英文字符串“`${warning.code}:${warning.path ?? warning.message}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7fadb5dcf32dcf483481863270a04d0cef2d4406127b52027b6b6c2187dcd845`

### 84. `hardcoded:src/components/openclaw/OpenClawHealthBanner.tsx:OpenClawHealthBanner:2f1ba34341eb3cec:001`

- 状态：待核实
- 文件：`src/components/openclaw/OpenClawHealthBanner.tsx:79`
- 结构：`OpenClawHealthBanner` / `template`
- 原文/表达式：` (${warning.path})`
- 判定原因：该英文字符串“` (${warning.path})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2f1ba34341eb3cec418d42a62736c134b8f8042070758fbe13721a506f691aa3`

### 85. `hardcoded:src/components/openclaw/ToolsPanel.tsx:ToolsPanel:5dc3c4b05218ca74:001`

- 状态：待核实
- 文件：`src/components/openclaw/ToolsPanel.tsx:170`
- 结构：`ToolsPanel` / `template`
- 原文/表达式：`${unsupportedProfile} (${t(<br>                "openclaw.tools.unsupportedProfileLabel",<br>                {<br>                  defaultValue: "unsupported",<br>                },<br>              )})`
- 判定原因：该英文字符串“`${unsupportedProfile} (${t(
                "openclaw.tools.unsupportedProfileLabel",
                {
                  defaultValue: "unsupported",
                },
              )})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5dc3c4b05218ca749896a46cdaa181c20e11672eda331aa5d610b0cf20e793fe`

### 86. `hardcoded:src/components/openclaw/hooks/useOpenClawModelOptions.ts:label:4e413c3de11f55c5:001`

- 状态：待核实
- 文件：`src/components/openclaw/hooks/useOpenClawModelOptions.ts:48`
- 结构：`label` / `template`
- 原文/表达式：`${providerDisplayName} / ${modelDisplayName}`
- 判定原因：该英文字符串“`${providerDisplayName} / ${modelDisplayName}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4e413c3de11f55c5f9254cbbedce7807bd67b6e5b69414f07b28675a4d901c0a`

### 87. `dynamic-i18n:src/components/profiles/ProfileSwitcher.tsx:ProfileSwitcher:bf07f0e194763ea6:001`

- 状态：待核实
- 文件：`src/components/profiles/ProfileSwitcher.tsx:116`
- 结构：`ProfileSwitcher` / `dynamic_i18n_key`
- 原文/表达式：`profiles.switcherTooltip.${scope}`
- 判定原因：翻译键由运行时表达式“`profiles.switcherTooltip.${scope}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`bf07f0e194763ea621ddc1be1a0fa505b153e66da09a849dc06007c5051c8f33`

### 88. `dynamic-i18n:src/components/profiles/ProfileSwitcher.tsx:ProfileSwitcher:bf07f0e194763ea6:002`

- 状态：待核实
- 文件：`src/components/profiles/ProfileSwitcher.tsx:134`
- 结构：`ProfileSwitcher` / `dynamic_i18n_key`
- 原文/表达式：`profiles.switcherTooltip.${scope}`
- 判定原因：翻译键由运行时表达式“`profiles.switcherTooltip.${scope}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`bf07f0e194763ea621ddc1be1a0fa505b153e66da09a849dc06007c5051c8f33`

### 89. `dynamic-i18n:src/components/profiles/ProfileSwitcher.tsx:ProfileSwitcher:1ea05b4ee91472f2:001`

- 状态：待核实
- 文件：`src/components/profiles/ProfileSwitcher.tsx:223`
- 结构：`ProfileSwitcher` / `dynamic_i18n_key`
- 原文/表达式：`profiles.createDescription.${scope}`
- 判定原因：翻译键由运行时表达式“`profiles.createDescription.${scope}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1ea05b4ee91472f2dff58eae1a3185cc82d499fe00c348b089dcb152ba5846d9`

### 90. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiInstructionFileEditor:d1d3865d992378c2:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:211`
- 结构：`PiInstructionFileEditor` / `dynamic_i18n_key`
- 原文/表达式：baseSnapshot.exists ? "pi.prompts.editFile" : "pi.prompts.createFile"
- 判定原因：翻译键由运行时表达式“baseSnapshot.exists ? "pi.prompts.editFile" : "pi.prompts.createFile"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d1d3865d992378c2b2bccf4e7c7e5a7a63e0e9b4c9a15f1f6a3dfb1556b659ad`

### 91. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiInstructionFileEditor:a8bc05c127159b54:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:215`
- 结构：`PiInstructionFileEditor` / `dynamic_i18n_key`
- 原文/表达式：file.descriptionKey
- 判定原因：翻译键由运行时表达式“file.descriptionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a8bc05c127159b54db39e473aad743e323f90addf0132138f3359fdbb38ed938`

### 92. `hardcoded:src/components/prompts/PiNativePromptResources.tsx:PiInstructionFileEditor:03779880d080c39a:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:288`
- 结构：`PiInstructionFileEditor` / `template`
- 原文/表达式：`${errorId} ${countId}`
- 判定原因：该英文字符串“`${errorId} ${countId}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`03779880d080c39a9e085a5ff016ce29b183ac94dd764c0470b59caaa7def789`

### 93. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:remove:2694dcf2980c7a5b:001`

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

### 94. `hardcoded:src/components/prompts/PiNativePromptResources.tsx:remove:defaf7b75a2b6ad8:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:369`
- 结构：`remove` / `template`
- 原文/表达式：`${t(<br>          blank ? "pi.prompts.deletedBlank" : "pi.prompts.deletedUndoable",<br>        )}${t("pi.prompts.reloadAfterDelete")}`
- 判定原因：该英文字符串“`${t(
          blank ? "pi.prompts.deletedBlank" : "pi.prompts.deletedUndoable",
        )}${t("pi.prompts.reloadAfterDelete")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`defaf7b75a2b6ad8315f6fa1c72571097e4ff7d16ff250ee6b2723a4d03114b3`

### 95. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:remove:ccfd4aa37ca34de2:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:369`
- 结构：`remove` / `dynamic_i18n_key`
- 原文/表达式：blank ? "pi.prompts.deletedBlank" : "pi.prompts.deletedUndoable"
- 判定原因：翻译键由运行时表达式“blank ? "pi.prompts.deletedBlank" : "pi.prompts.deletedUndoable"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ccfd4aa37ca34de27182837641d46f3d97b72638cf56508f3b2c0893d2a3f1c7`

### 96. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:d1d85835cac8c3b6:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:426`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：file.titleKey
- 判定原因：翻译键由运行时表达式“file.titleKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d1d85835cac8c3b67f8f2f2788b521e0f56e6f85bb64f0c5165d5a1e0aeb709c`

### 97. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:a8bc05c127159b54:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:438`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：file.descriptionKey
- 判定原因：翻译键由运行时表达式“file.descriptionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a8bc05c127159b54db39e473aad743e323f90addf0132138f3359fdbb38ed938`

### 98. `hardcoded:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:ff2089b4b04347e4:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:478`
- 结构：`PiSystemPromptFiles` / `template`
- 原文/表达式：`${t(data?.exists ? "common.edit" : "pi.prompts.create")} ${file.filename}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${t(data?.exists ? "common.edit" : "pi.prompts.create")} ${file.filename}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ff2089b4b04347e4968255048f278615f309a5cc7366a5a3d26578223877f005`

### 99. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:c2b9bd028b119153:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:478`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：data?.exists ? "common.edit" : "pi.prompts.create"
- 判定原因：翻译键由运行时表达式“data?.exists ? "common.edit" : "pi.prompts.create"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c2b9bd028b119153842868de21081c0165efb2f1275c7679450a3e836ce7acc2`

### 100. `dynamic-i18n:src/components/prompts/PiNativePromptResources.tsx:PiSystemPromptFiles:c2b9bd028b119153:002`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:483`
- 结构：`PiSystemPromptFiles` / `dynamic_i18n_key`
- 原文/表达式：data?.exists ? "common.edit" : "pi.prompts.create"
- 判定原因：翻译键由运行时表达式“data?.exists ? "common.edit" : "pi.prompts.create"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c2b9bd028b119153842868de21081c0165efb2f1275c7679450a3e836ce7acc2`

### 101. `hardcoded:src/components/prompts/PiNativePromptResources.tsx:remove:de1dcddffe745623:001`

- 状态：待核实
- 文件：`src/components/prompts/PiNativePromptResources.tsx:789`
- 结构：`remove` / `template`
- 原文/表达式：`${t("pi.prompts.templateDeletedSub", {<br>          slug: template.slug,<br>        })}${t("pi.prompts.reloadAfterDelete")}`
- 判定原因：该英文字符串“`${t("pi.prompts.templateDeletedSub", {
          slug: template.slug,
        })}${t("pi.prompts.reloadAfterDelete")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`de1dcddffe745623b54ea279f04edcfb1f42f8a588707db7d63f78f10f20e6a3`

### 102. `hardcoded:src/components/prompts/PiPromptPanel.tsx:target:8243b190caa97da7:001`

- 状态：待核实
- 文件：`src/components/prompts/PiPromptPanel.tsx:351`
- 结构：`target` / `template`
- 原文/表达式：` · ${<br>            fileText === null<br>              ? t("prompts.fileMissing")<br>              : !fileText.trim()<br>                ? t("prompts.fileEmpty")<br>                : formatSize(utf8Bytes(fileText))<br>          }`
- 判定原因：该英文字符串“` · ${
            fileText === null
              ? t("prompts.fileMissing")
              : !fileText.trim()
                ? t("prompts.fileEmpty")
                : formatSize(utf8Bytes(fileText))
          }`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8243b190caa97da70640da0df9147fcffd4f0ba9da8123177cbe1a4471cb7789`

### 103. `dynamic-i18n:src/components/prompts/PromptFormPanel.tsx:nameError:faa60122c7dfa55e:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptFormPanel.tsx:88`
- 结构：`nameError` / `dynamic_i18n_key`
- 原文/表达式：isHermes ? "prompts.nameRequiredHermes" : "prompts.nameRequired"
- 判定原因：翻译键由运行时表达式“isHermes ? "prompts.nameRequiredHermes" : "prompts.nameRequired"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`faa60122c7dfa55e3d3a53f6e70596a0f33d1536751571c46698a866921d592a`

### 104. `hardcoded:src/components/prompts/PromptFormPanel.tsx:countText:131f9b3b16d16646:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptFormPanel.tsx:147`
- 结构：`countText` / `template`
- 原文/表达式：`${formatSize(bodyBytes)} / 32 KB`
- 判定原因：该英文字符串“`${formatSize(bodyBytes)} / 32 KB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`131f9b3b16d166467163ec4836c30508d8c2d59359602dab074a506aa3502433`

### 105. `dynamic-i18n:src/components/prompts/PromptFormPanel.tsx:PromptFormPanel:f3ffc31bc1e64a97:001`

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

### 106. `hardcoded:src/components/prompts/PromptFormPanel.tsx:PromptFormPanel:9adc6b50c82cf115:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptFormPanel.tsx:254`
- 结构：`PromptFormPanel` / `template`
- 原文/表达式：`${bodyHintId} ${countId}`
- 判定原因：该英文字符串“`${bodyHintId} ${countId}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9adc6b50c82cf11518e3cba43b1ea6b7f91d3e890ea06179a68ba2bf3c28a59d`

### 107. `hardcoded:src/components/prompts/PromptListItem.tsx:PromptListItem:a11ba0309dc3fa24:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptListItem.tsx:58`
- 结构：`PromptListItem` / `string`
- 原文/表达式：button, a, input, label, [role='menu']
- 判定原因：该英文字符串“button, a, input, label, [role='menu']”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a11ba0309dc3fa2425c0f9dccb29cee7e47ac0d68ad38cec3dd3a5019542579e`

### 108. `dynamic-i18n:src/components/prompts/PromptListItem.tsx:PromptListItem:d12e0500610428ba:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptListItem.tsx:94`
- 结构：`PromptListItem` / `dynamic_i18n_key`
- 原文/表达式：active ? "prompts.disableAria" : "prompts.enableAria"
- 判定原因：翻译键由运行时表达式“active ? "prompts.disableAria" : "prompts.enableAria"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d12e0500610428ba236c01a7b5b70cb4bb9387f9d55be2e6f8336a0a27c8d701`

### 109. `dynamic-i18n:src/components/prompts/PromptListItem.tsx:PromptListItem:cccf9c2fec5053e8:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptListItem.tsx:100`
- 结构：`PromptListItem` / `dynamic_i18n_key`
- 原文/表达式：active ? "prompts.disable" : "prompts.enable"
- 判定原因：翻译键由运行时表达式“active ? "prompts.disable" : "prompts.enable"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cccf9c2fec5053e836d0753b9ded96c4bc796bd449169bb2b71f8b2a7d7563ee`

### 110. `hardcoded:src/components/prompts/PromptPageFrame.tsx:promptMenuContentClass:6045ed9dbb9a76c7:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptPageFrame.tsx:34`
- 结构：`promptMenuContentClass` / `string`
- 原文/表达式：min-w-[200px] rounded-panel border border-border bg-surface p-1 text-fg-1 shadow-v7-md
- 判定原因：该英文字符串“min-w-[200px] rounded-panel border border-border bg-surface p-1 text-fg-1 shadow-v7-md”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6045ed9dbb9a76c73303325c4cffa76a15d02dd5cc33d37f548fef92459fb158`

### 111. `hardcoded:src/components/prompts/PromptPageFrame.tsx:promptMenuItemClass:b39964dd157e3c40:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptPageFrame.tsx:36`
- 结构：`promptMenuItemClass` / `string`
- 原文/表达式：min-h-8 rounded-control px-2.5 py-1.5 text-body text-fg-1 focus:bg-subtle focus:text-fg-1 data-[disabled]:opacity-100
- 判定原因：该英文字符串“min-h-8 rounded-control px-2.5 py-1.5 text-body text-fg-1 focus:bg-subtle focus:text-fg-1 data-[disabled]:opacity-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b39964dd157e3c40c85ff9a6803081e9b42ae40a28d4610d323472ba49147343`

### 112. `hardcoded:src/components/prompts/PromptPageFrame.tsx:PromptPageFrame:fa4a6d2b1ac5667e:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptPageFrame.tsx:165`
- 结构：`PromptPageFrame` / `template`
- 原文/表达式：`${target.label} ${target.path}${target.meta ?? ""}`
- 控件属性：`title`
- 判定原因：该英文字符串“`${target.label} ${target.path}${target.meta ?? ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fa4a6d2b1ac5667ee399963afba8acced883677b202026eae41975f8bca1572b`

### 113. `hardcoded:src/components/prompts/PromptPanel.tsx:StandardPromptPanel:8ebbda4fd11a88ea:001`

- 状态：待核实
- 文件：`src/components/prompts/PromptPanel.tsx:512`
- 结构：`StandardPromptPanel` / `template`
- 原文/表达式：` · ${fileMeta}`
- 判定原因：该英文字符串“` · ${fileMeta}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8ebbda4fd11a88ea0b160bda8d91d99489dc82453f892247254fabb559e56a6f`

### 114. `hardcoded:src/components/prompts/promptUtils.tsx:formatSize:229dd2efa20cfa06:001`

- 状态：待核实
- 文件：`src/components/prompts/promptUtils.tsx:37`
- 结构：`formatSize` / `template`
- 原文/表达式：`${bytes} B`
- 判定原因：该英文字符串“`${bytes} B`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`229dd2efa20cfa06a18005595e089bef78a3ffc5bd33bb73dac85cca195d46c6`

### 115. `hardcoded:src/components/prompts/promptUtils.tsx:formatSize:3774273e5fbf94ef:001`

- 状态：待核实
- 文件：`src/components/prompts/promptUtils.tsx:37`
- 结构：`formatSize` / `template`
- 原文/表达式：`${(bytes / 1024).toFixed(1)} KB`
- 判定原因：该英文字符串“`${(bytes / 1024).toFixed(1)} KB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3774273e5fbf94ef8195350bfd3982824f82e6586e1751e20151e275c30f64df`

### 116. `dynamic-i18n:src/components/prompts/usePromptPageCommon.ts:toggleEffectText:2225c982a3afe1fa:001`

- 状态：待核实
- 文件：`src/components/prompts/usePromptPageCommon.ts:64`
- 结构：`toggleEffectText` / `dynamic_i18n_key`
- 原文/表达式：enabled ? "prompts.toast.hermesOn" : "prompts.toast.hermesOff"
- 判定原因：翻译键由运行时表达式“enabled ? "prompts.toast.hermesOn" : "prompts.toast.hermesOff"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2225c982a3afe1fa729c3e536e1e1a979ce749d11b999cd756c04e76010b864e`

### 117. `dynamic-i18n:src/components/providers/CodexStaleClientsNotice.tsx:CodexStaleClientsNotice:d73fd9997e52d916:001`

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

### 118. `dynamic-i18n:src/components/providers/KimiAccountLogin.tsx:rows:0efcbaf86f008873:001`

- 状态：待核实
- 文件：`src/components/providers/KimiAccountLogin.tsx:57`
- 结构：`rows` / `dynamic_i18n_key`
- 原文/表达式：`kimi.oauth.${account.region}`
- 判定原因：翻译键由运行时表达式“`kimi.oauth.${account.region}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0efcbaf86f008873c4d489f263f1364693f9365f17d54a5affa885bc16d319ce`

### 119. `dynamic-i18n:src/components/providers/KimiAccountLogin.tsx:KimiAccountLogin:60eddd19f0eccda0:001`

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

### 120. `hardcoded:src/components/providers/OpenTerminalDialog.tsx:handleChoose:cfb52b235594b7cc:001`

- 状态：待核实
- 文件：`src/components/providers/OpenTerminalDialog.tsx:169`
- 结构：`handleChoose` / `template`
- 原文/表达式：`: ${message}`
- 判定原因：该英文字符串“`: ${message}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`cfb52b235594b7cc62a3ea8a1b7f717237bcff8afdab648eeb7fa027e4b5535b`

### 121. `dynamic-i18n:src/components/providers/OpenTerminalDialog.tsx:OpenTerminalDialog:2b72580d648a686e:001`

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

### 122. `hardcoded:src/components/providers/ProviderCard.tsx:providerNameIncludesAccountLogin:b5a2f7477415d9ec:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderCard.tsx:226`
- 结构：`providerNameIncludesAccountLogin` / `template`
- 原文/表达式：`OpenAI Official (${managedCodexAccount.login})`
- 判定原因：该英文字符串“`OpenAI Official (${managedCodexAccount.login})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b5a2f7477415d9ec8937a7b46546ae5534e04f4aea40319c4b9da530e597ad42`

### 123. `dynamic-i18n:src/components/providers/ProviderCardActions.tsx:ProviderCardActions:7ac214e2da017a6c:001`

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

### 124. `dynamic-i18n:src/components/providers/ProviderEmptyState.tsx:ProviderEmptyState:4fd05547609ab33c:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderEmptyState.tsx:48`
- 结构：`ProviderEmptyState` / `dynamic_i18n_key`
- 原文/表达式：`${emptyCopyNs}.empty.title`
- 判定原因：翻译键由运行时表达式“`${emptyCopyNs}.empty.title`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4fd05547609ab33c012446250b5baabb5d65423449887ded7798685c2db0ac23`

### 125. `dynamic-i18n:src/components/providers/ProviderEmptyState.tsx:ProviderEmptyState:bc32d0931c886d14:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderEmptyState.tsx:53`
- 结构：`ProviderEmptyState` / `dynamic_i18n_key`
- 原文/表达式：`${emptyCopyNs}.empty.description`
- 判定原因：翻译键由运行时表达式“`${emptyCopyNs}.empty.description`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`bc32d0931c886d1458a2a0bd5842a0a6ad3d9111fcc8f94afb58fce2c34b9cc2`

### 126. `dynamic-i18n:src/components/providers/ProviderList.tsx:piStateErrorNotice:a72c91773a926bd1:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderList.tsx:430`
- 结构：`piStateErrorNotice` / `dynamic_i18n_key`
- 原文/表达式：`${appId}.current.readFailed`
- 判定原因：翻译键由运行时表达式“`${appId}.current.readFailed`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a72c91773a926bd1ce4dfba5624c1fde35704374ba5763f5af939dafeae59e89`

### 127. `dynamic-i18n:src/components/providers/ProviderList.tsx:piStateErrorNotice:cae9391778824b2d:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderList.tsx:434`
- 结构：`piStateErrorNotice` / `dynamic_i18n_key`
- 原文/表达式：`${appId}.current.stateUnavailableHint`
- 判定原因：翻译键由运行时表达式“`${appId}.current.stateUnavailableHint`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cae9391778824b2dd2e838af86052a9d7821c0f2c504040533cfc169215b346f`

### 128. `hardcoded:src/components/providers/ProviderList.tsx:piStateErrorNotice:b9eb9816a06c901b:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderList.tsx:435`
- 结构：`piStateErrorNotice` / `template`
- 原文/表达式：` ${piStateError}`
- 判定原因：该英文字符串“` ${piStateError}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b9eb9816a06c901b830bf7ae5b9855b3c20c076abe1e93fc63f82e3fbe6cb7a6`

### 129. `hardcoded:src/components/providers/ProviderList.tsx:searchField:5fc70c276fa95a5b:001`

- 状态：待核实
- 文件：`src/components/providers/ProviderList.tsx:529`
- 结构：`searchField` / `template`
- 原文/表达式：`${t("provider.searchScopeHint", {<br>              defaultValue:<br>                "Matches provider name, notes, website, and API address.",<br>            })} ${t("provider.searchCloseHint", {<br>              defaultValue: "Press Esc to close",<br>            })}`
- 控件属性：`title`
- 判定原因：该英文字符串“`${t("provider.searchScopeHint", {
              defaultValue:
                "Matches provider name, notes, website, and API address.",
            })} ${t("provider.searchCloseHint", {
              defaultValue: "Press Esc to close",
            })}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5fc70c276fa95a5b6fbaac8e55772555f23438ea42980e169789efd2d3d119f5`

### 130. `hardcoded:src/components/providers/forms/BasicFormFields.tsx:REQUIRED_LABEL:1e3b3fdaf911a12c:001`

- 状态：待核实
- 文件：`src/components/providers/forms/BasicFormFields.tsx:31`
- 结构：`REQUIRED_LABEL` / `string`
- 原文/表达式：after:ms-0.5 after:text-danger-text after:content-['*']
- 判定原因：该英文字符串“after:ms-0.5 after:text-danger-text after:content-['*']”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1e3b3fdaf911a12ce83852cad918332e87be0084ca631fbb239d5c9befac6f5e`

### 131. `dynamic-i18n:src/components/providers/forms/ClaudeDesktopProviderForm.tsx:applyDesktopPreset:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ClaudeDesktopProviderForm.tsx:433`
- 结构：`applyDesktopPreset` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 132. `hardcoded:src/components/providers/forms/ClaudeOfficialSection.tsx:itemClass:f10d787bf085794b:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ClaudeOfficialSection.tsx:382`
- 结构：`itemClass` / `string`
- 原文/表达式：min-w-0 overflow-hidden py-2 pl-6 [&>span:last-child]:min-w-0 [&>span:last-child]:flex-1 [&>span:last-child]:overflow-hidden
- 判定原因：该英文字符串“min-w-0 overflow-hidden py-2 pl-6 [&>span:last-child]:min-w-0 [&>span:last-child]:flex-1 [&>span:last-child]:overflow-hidden”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f10d787bf085794b93a5ceb068b63314f485a4ef8851bc3ae1bd729541affe98`

### 133. `dynamic-i18n:src/components/providers/forms/CodexConfigSections.tsx:CodexAuthSection:b3aada018c964656:001`

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

### 134. `dynamic-i18n:src/components/providers/forms/CodexConfigSections.tsx:CodexConfigSection:75b82bc2e41ebdef:001`

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

### 135. `hardcoded:src/components/providers/forms/CodexFormFields.tsx:formatReasoningLevelsLabel:5fe8ad79d4e63311:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CodexFormFields.tsx:446`
- 结构：`formatReasoningLevelsLabel` / `template`
- 原文/表达式：`${run[0]} → ${run[run.length - 1]}`
- 判定原因：该英文字符串“`${run[0]} → ${run[run.length - 1]}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5fe8ad79d4e6331157ae48f1f2ff5c7c21505d280a58988f29d4da6e429a2ccc`

### 136. `hardcoded:src/components/providers/forms/CodexFormFields.tsx:handleFetchModels:594950879d16b576:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CodexFormFields.tsx:965`
- 结构：`handleFetchModels` / `string`
- 原文/表达式：[Copilot] Failed to fetch models:
- 判定原因：该英文字符串“[Copilot] Failed to fetch models:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`594950879d16b5769bd90068d33dd2839529b5bdb9812b29ffacebc1bc1731df`

### 137. `hardcoded:src/components/providers/forms/CodexFormFields.tsx:handleFetchModels:1fea753f650f5909:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CodexFormFields.tsx:984`
- 结构：`handleFetchModels` / `string`
- 原文/表达式：[XaiOAuth] Failed to fetch models:
- 判定原因：该英文字符串“[XaiOAuth] Failed to fetch models:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1fea753f650f5909614af26b681e7264fed9d1e00c6867ea1d8144b080a1ed28`

### 138. `hardcoded:src/components/providers/forms/CodexFormFields.tsx:handleFetchModels:7880561a9305b3d1:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CodexFormFields.tsx:1009`
- 结构：`handleFetchModels` / `string`
- 原文/表达式：[ModelFetch] Failed:
- 判定原因：该英文字符串“[ModelFetch] Failed:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7880561a9305b3d106d672a4efa91e76dff338c1c2d13949005955b46d976278`

### 139. `dynamic-i18n:src/components/providers/forms/CommonConfigEditor.tsx:CommonConfigEditor:e626f805fbbd0918:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CommonConfigEditor.tsx:226`
- 结构：`CommonConfigEditor` / `dynamic_i18n_key`
- 原文/表达式：`claudeConfig.${key}`
- 判定原因：翻译键由运行时表达式“`claudeConfig.${key}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e626f805fbbd09186fcb572b913402ca4b8698bdec50eec0cd3c29ef2a6c32ef`

### 140. `dynamic-i18n:src/components/providers/forms/CommonConfigEditor.tsx:CommonConfigEditor:e626f805fbbd0918:002`

- 状态：待核实
- 文件：`src/components/providers/forms/CommonConfigEditor.tsx:228`
- 结构：`CommonConfigEditor` / `dynamic_i18n_key`
- 原文/表达式：`claudeConfig.${key}`
- 判定原因：翻译键由运行时表达式“`claudeConfig.${key}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e626f805fbbd09186fcb572b913402ca4b8698bdec50eec0cd3c29ef2a6c32ef`

### 141. `dynamic-i18n:src/components/providers/forms/CommonConfigEditor.tsx:CommonConfigEditor:6441eb22cfc8b522:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CommonConfigEditor.tsx:229`
- 结构：`CommonConfigEditor` / `dynamic_i18n_key`
- 原文/表达式：`claudeConfig.${key}Help`
- 判定原因：翻译键由运行时表达式“`claudeConfig.${key}Help`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`6441eb22cfc8b522bfba7d8d0ed5fc65dfa2d164e6f833b9aa2f50ef602eb05a`

### 142. `hardcoded:src/components/providers/forms/CommonConfigEditor.tsx:CommonConfigEditor:bb3af58fc0f7e590:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CommonConfigEditor.tsx:238`
- 结构：`CommonConfigEditor` / `template`
- 原文/表达式：{<br>  "env": {<br>    "ANTHROPIC_BASE_URL": "https://your-api-endpoint.com",<br>    "ANTHROPIC_AUTH_TOKEN": "your-api-key-here"<br>  }<br>}
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{
  "env": {
    "ANTHROPIC_BASE_URL": "https://your-api-endpoint.com",
    "ANTHROPIC_AUTH_TOKEN": "your-api-key-here"
  }
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`bb3af58fc0f7e590765f6a5bf7e9f8ec16ea646048fcfb7ff26c5c8641ffb7c6`

### 143. `hardcoded:src/components/providers/forms/CustomUserAgentField.tsx:CustomUserAgentField:6c8d142fc3b6f03f:001`

- 状态：待核实
- 文件：`src/components/providers/forms/CustomUserAgentField.tsx:56`
- 结构：`CustomUserAgentField` / `string`
- 原文/表达式：Mozilla/5.0 ...
- 控件属性：`placeholder`
- 判定原因：该英文字符串“Mozilla/5.0 ...”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6c8d142fc3b6f03ffc7157ec103b305a99681f9f19665ea024e9b0750608139f`

### 144. `hardcoded:src/components/providers/forms/EndpointSpeedTest.tsx:randomId:968d33291c0ad246:001`

- 状态：待核实
- 文件：`src/components/providers/forms/EndpointSpeedTest.tsx:58`
- 结构：`randomId` / `template`
- 原文/表达式：`ep_${Math.random().toString(36).slice(2, 9)}`
- 判定原因：该英文字符串“`ep_${Math.random().toString(36).slice(2, 9)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`968d33291c0ad2461561d0c781bd0a031035e333f33c80e266058934ae25f8cd`

### 145. `hardcoded:src/components/providers/forms/EndpointSpeedTest.tsx:message:5f1c5ef1539c39b7:001`

- 状态：待核实
- 文件：`src/components/providers/forms/EndpointSpeedTest.tsx:384`
- 结构：`message` / `template`
- 原文/表达式：`${t("endpointTest.testFailed", { error: String(error) })}`
- 判定原因：该英文字符串“`${t("endpointTest.testFailed", { error: String(error) })}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5f1c5ef1539c39b70137bef1bfed9f12cd4694849de8588f4ef48357c8fe680a`

### 146. `hardcoded:src/components/providers/forms/FetchedModelPicker.tsx:formatContextWindow:d993c0321b9e0507:001`

- 状态：待核实
- 文件：`src/components/providers/forms/FetchedModelPicker.tsx:48`
- 结构：`formatContextWindow` / `template`
- 原文/表达式：`${Number((tokens / (base * base)).toPrecision(3))}M`
- 判定原因：该英文字符串“`${Number((tokens / (base * base)).toPrecision(3))}M`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d993c0321b9e0507d14faf3dbd6689aac8cd4069ebb8a9cc1c3a9913d4c8c3bc`

### 147. `hardcoded:src/components/providers/forms/FetchedModelPicker.tsx:formatContextWindow:28ad0093b916cd9a:001`

- 状态：待核实
- 文件：`src/components/providers/forms/FetchedModelPicker.tsx:50`
- 结构：`formatContextWindow` / `template`
- 原文/表达式：`${Number((tokens / base).toPrecision(3))}K`
- 判定原因：该英文字符串“`${Number((tokens / base).toPrecision(3))}K`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`28ad0093b916cd9a1f37c7aae67682aa2015f63d2c208451d645faba894f3976`

### 148. `hardcoded:src/components/providers/forms/GeminiConfigSections.tsx:GeminiConfigSection:ba7a280e5a49adcb:001`

- 状态：待核实
- 文件：`src/components/providers/forms/GeminiConfigSections.tsx:139`
- 结构：`GeminiConfigSection` / `template`
- 原文/表达式：{<br>  "timeout": 30000,<br>  "maxRetries": 3<br>}
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{
  "timeout": 30000,
  "maxRetries": 3
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ba7a280e5a49adcb445eacb965e760a2465d7774681bfc322198fced5e5bc129`

### 149. `hardcoded:src/components/providers/forms/GeminiFormFields.tsx:GeminiFormFields:2f864ce7fd5a5836:001`

- 状态：待核实
- 文件：`src/components/providers/forms/GeminiFormFields.tsx:216`
- 结构：`GeminiFormFields` / `string`
- 原文/表达式：Gemini 3.8 Flash (High)
- 控件属性：`placeholder`
- 判定原因：该英文字符串“Gemini 3.8 Flash (High)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2f864ce7fd5a58362b08b4b32505753239d1e06282ba2a20441cd6ec287e79e8`

### 150. `dynamic-i18n:src/components/providers/forms/GrokBuildProviderForm.tsx:presetName:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/GrokBuildProviderForm.tsx:280`
- 结构：`presetName` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 151. `dynamic-i18n:src/components/providers/forms/HermesFormFields.tsx:baseUrlErrorMessage:5eb171ca5f27c5ee:001`

- 状态：待核实
- 文件：`src/components/providers/forms/HermesFormFields.tsx:113`
- 结构：`baseUrlErrorMessage` / `dynamic_i18n_key`
- 原文/表达式：BASE_URL_ERROR_I18N_KEY[baseUrlErrorCode]
- 判定原因：翻译键由运行时表达式“BASE_URL_ERROR_I18N_KEY[baseUrlErrorCode]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5eb171ca5f27c5eefd4e8e2757583c5a23cbb1c00f52b6199b1c9b5d91e475ef`

### 152. `dynamic-i18n:src/components/providers/forms/HermesFormFields.tsx:HermesFormFields:ebd78379247b5bd6:001`

- 状态：待核实
- 文件：`src/components/providers/forms/HermesFormFields.tsx:239`
- 结构：`HermesFormFields` / `dynamic_i18n_key`
- 原文/表达式：mode.labelKey
- 判定原因：翻译键由运行时表达式“mode.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ebd78379247b5bd6b2d34410f886a2e98d012497dd589d92dcc1ae28e9ef5f47`

### 153. `hardcoded:src/components/providers/forms/InactiveFieldsPanel.tsx:InactiveFieldsPanel:3beb400f41b46efa:001`

- 状态：待核实
- 文件：`src/components/providers/forms/InactiveFieldsPanel.tsx:49`
- 结构：`InactiveFieldsPanel` / `template`
- 原文/表达式：`+ ${name}`
- 判定原因：该英文字符串“`+ ${name}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3beb400f41b46efa93d541b244b2404292075b8f534e40c2d1e38927479fbf1f`

### 154. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:presetSelector:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:417`
- 结构：`presetSelector` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 155. `hardcoded:src/components/providers/forms/KimiProviderForm.tsx:rename:c42aa22d48bd32f1:001`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:528`
- 结构：`rename` / `template`
- 原文/表达式：`${next \|\| "custom"}/${key.slice(modelKeyPrefix.length + 1)}`
- 判定原因：该英文字符串“`${next || "custom"}/${key.slice(modelKeyPrefix.length + 1)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c42aa22d48bd32f19b5ee9923dccdd99e0f5dcc841b6cf08b7dcd3402b82bd69`

### 156. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:KimiProviderForm:450a277c2780a76f:001`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:766`
- 结构：`KimiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`kimi.capabilities.${capability}`
- 判定原因：翻译键由运行时表达式“`kimi.capabilities.${capability}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`450a277c2780a76f8de37a14ed429c00fd2d7306f903bbdd718ab732baf89402`

### 157. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:KimiProviderForm:450a277c2780a76f:002`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:770`
- 结构：`KimiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`kimi.capabilities.${capability}`
- 判定原因：翻译键由运行时表达式“`kimi.capabilities.${capability}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`450a277c2780a76f8de37a14ed429c00fd2d7306f903bbdd718ab732baf89402`

### 158. `dynamic-i18n:src/components/providers/forms/KimiProviderForm.tsx:KimiProviderForm:c76f11a5e2460403:001`

- 状态：待核实
- 文件：`src/components/providers/forms/KimiProviderForm.tsx:772`
- 结构：`KimiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`kimi.capabilityHints.${capability}`
- 判定原因：翻译键由运行时表达式“`kimi.capabilityHints.${capability}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c76f11a5e24604034bcd0d3ff1a6d6fb8e3802b27e31cd08ef6989f5a8bdfeeb`

### 159. `hardcoded:src/components/providers/forms/LocalProxyRequestOverridesField.tsx:LocalProxyRequestOverridesField:e1e515e7180d7033:001`

- 状态：待核实
- 文件：`src/components/providers/forms/LocalProxyRequestOverridesField.tsx:50`
- 结构：`LocalProxyRequestOverridesField` / `string`
- 原文/表达式：{<br>  "X-Provider": "cc-switch"<br>}
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{
  "X-Provider": "cc-switch"
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e1e515e7180d70334bec74154e391c3b95dc3aeb889ec645b98a9e0afbc221a0`

### 160. `hardcoded:src/components/providers/forms/LocalProxyRequestOverridesField.tsx:LocalProxyRequestOverridesField:cffd62f1796bb566:001`

- 状态：待核实
- 文件：`src/components/providers/forms/LocalProxyRequestOverridesField.tsx:73`
- 结构：`LocalProxyRequestOverridesField` / `string`
- 原文/表达式：{<br>  "temperature": 0.2<br>}
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{
  "temperature": 0.2
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`cffd62f1796bb566d5ad30fc5fbb75465b006ef7a6a9a42b8fd4e138f46c8369`

### 161. `hardcoded:src/components/providers/forms/OmoFormFields.tsx:ADVANCED_PLACEHOLDER:b31ef31350210726:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:53`
- 结构：`ADVANCED_PLACEHOLDER` / `template`
- 原文/表达式：{<br>  "temperature": 0.5,<br>  "top_p": 0.9,<br>  "budgetTokens": 20000,<br>  "prompt_append": "",<br>  "permission": { "edit": "allow", "bash": "ask" }<br>}
- 判定原因：该英文字符串“{
  "temperature": 0.5,
  "top_p": 0.9,
  "budgetTokens": 20000,
  "prompt_append": "",
  "permission": { "edit": "allow", "bash": "ask" }
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b31ef31350210726dd2d8933a21f58a5cb58ebd2490b61d5b5f7cf3ddcce5cb3`

### 162. `hardcoded:src/components/providers/forms/OmoFormFields.tsx:placeholderText:98f19b1023bf1c62:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:152`
- 结构：`placeholderText` / `template`
- 原文/表达式：`${selectModelText} (${t("omo.recommendedHint", { model: recommended, defaultValue: "Recommended: {{model}}" })})`
- 判定原因：该英文字符串“`${selectModelText} (${t("omo.recommendedHint", { model: recommended, defaultValue: "Recommended: {{model}}" })})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`98f19b1023bf1c62b7efb98afbeb74c692ba7cbf6390f13f505e89810f24f94e`

### 163. `hardcoded:src/components/providers/forms/OmoFormFields.tsx:formatExample:817be6d029ab4b0d:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:744`
- 结构：`formatExample` / `template`
- 原文/表达式：`${display}: ${recommended}`
- 判定原因：该英文字符串“`${display}: ${recommended}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`817be6d029ab4b0d6fe73cb0491be70697a69e9444e2b1b1e7f3c1ebc35c7d38`

### 164. `dynamic-i18n:src/components/providers/forms/OmoFormFields.tsx:renderBuiltinModelRow:f19573ea4c8f34d1:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:921`
- 结构：`renderBuiltinModelRow` / `dynamic_i18n_key`
- 原文/表达式：def.tooltipKey
- 判定原因：翻译键由运行时表达式“def.tooltipKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`f19573ea4c8f34d16ed290a159139f8c4f9d8a6b2d57ba15b5a4226f48405124`

### 165. `dynamic-i18n:src/components/providers/forms/OmoFormFields.tsx:renderBuiltinModelRow:2b3d6a81dfe0d684:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:925`
- 结构：`renderBuiltinModelRow` / `dynamic_i18n_key`
- 原文/表达式：def.descKey
- 判定原因：翻译键由运行时表达式“def.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2b3d6a81dfe0d68451cced7796ce01f17ea2304cfb282b8757154b5060f88179`

### 166. `hardcoded:src/components/providers/forms/OmoFormFields.tsx:OmoFormFields:5e20285fe5ad1cfa:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:1257`
- 结构：`OmoFormFields` / `template`
- 原文/表达式：`${subAgents.length + customAgents.length}`
- 判定原因：该英文字符串“`${subAgents.length + customAgents.length}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5e20285fe5ad1cfa2eba554a9000dbe93a77c749f462ba24c066427d157f1c0a`

### 167. `hardcoded:src/components/providers/forms/OmoFormFields.tsx:OmoFormFields:91d0a331812bbb1c:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:1281`
- 结构：`OmoFormFields` / `template`
- 原文/表达式：`${OMO_BUILTIN_CATEGORIES.length + customCategories.length}`
- 判定原因：该英文字符串“`${OMO_BUILTIN_CATEGORIES.length + customCategories.length}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`91d0a331812bbb1c12b109fddf1922f9cebc6d1202c1e51183c752eba8fb1b34`

### 168. `hardcoded:src/components/providers/forms/OmoFormFields.tsx:OmoFormFields:c746ca58ccfa9445:001`

- 状态：待核实
- 文件：`src/components/providers/forms/OmoFormFields.tsx:1324`
- 结构：`OmoFormFields` / `string`
- 原文/表达式：{ "custom_key": "value" }
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{ "custom_key": "value" }”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c746ca58ccfa944537e641c9bc09b1df5b612728499b00176a8ed4d4e0c37e43`

### 169. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:001`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:1997`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 170. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:002`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2005`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 171. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:003`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2048`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 172. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:144d278fd002fc14:004`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2124`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`pi.form.thinkingLevels.${level}`
- 判定原因：翻译键由运行时表达式“`pi.form.thinkingLevels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`144d278fd002fc148183933e93c9e19ec345a4fcb70ba385572841333ee0f982`

### 173. `dynamic-i18n:src/components/providers/forms/PiProviderForm.tsx:PiProviderForm:132a666b0f252c49:001`

- 状态：待核实
- 文件：`src/components/providers/forms/PiProviderForm.tsx:2213`
- 结构：`PiProviderForm` / `dynamic_i18n_key`
- 原文/表达式：`omp.form.discoveryTypes.${labelKey}`
- 判定原因：翻译键由运行时表达式“`omp.form.discoveryTypes.${labelKey}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`132a666b0f252c49eb4a518979481806f7535319d4b1a4cae4bbd0deb0f020f2`

### 174. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handleSubmit:b107d3ee7afe31c4:001`

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

### 175. `hardcoded:src/components/providers/forms/ProviderForm.tsx:performSubmit:458eb3e0d13f515e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:1808`
- 结构：`performSubmit` / `template`
- 原文/表达式：`${prefix}-${crypto.randomUUID().slice(0, 8)}`
- 判定原因：该英文字符串“`${prefix}-${crypto.randomUUID().slice(0, 8)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`458eb3e0d13f515e55c38f81d413a257efdb51200f91d4e8baa72c1a431f350e`

### 176. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:presetName:70b8f41adf91a088:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:1850`
- 结构：`presetName` / `dynamic_i18n_key`
- 原文/表达式：selectedPresetEntry.preset.nameKey
- 判定原因：翻译键由运行时表达式“selectedPresetEntry.preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`70b8f41adf91a088b81d19e95c1b202946fb7b5f85d9dde92ed37cafbf0718b0`

### 177. `hardcoded:src/components/providers/forms/ProviderForm.tsx:performSubmit:ad1ffbaec168e765:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:1854`
- 结构：`performSubmit` / `template`
- 原文/表达式：`${presetName} (${selectedAccountLogin})`
- 判定原因：该英文字符串“`${presetName} (${selectedAccountLogin})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ad1ffbaec168e765637692922ba9c73bfef1023ace633f044f32cee293d7929c`

### 178. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2245`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 179. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:002`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2271`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 180. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:003`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2300`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 181. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:004`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2327`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 182. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:005`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2344`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 183. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:handlePresetChange:e0d3c7fcb27f761e:006`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:2380`
- 结构：`handlePresetChange` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 184. `dynamic-i18n:src/components/providers/forms/ProviderForm.tsx:ProviderFormFull:2929691ef61b6b98:001`

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

### 185. `hardcoded:src/components/providers/forms/ProviderForm.tsx:ProviderFormFull:c279117c636298ec:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:3006`
- 结构：`ProviderFormFull` / `template`
- 原文/表达式：{<br>  "npm": "@ai-sdk/openai-compatible",<br>  "options": {<br>    "baseURL": "https://your-api-endpoint.com",<br>    "apiKey": "your-api-key-here"<br>  },<br>  "models": {}<br>}
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{
  "npm": "@ai-sdk/openai-compatible",
  "options": {
    "baseURL": "https://your-api-endpoint.com",
    "apiKey": "your-api-key-here"
  },
  "models": {}
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c279117c636298ec9d0a9b4ee551430f8b40a5f2e827497e7aa546703e65b6ef`

### 186. `hardcoded:src/components/providers/forms/ProviderForm.tsx:ProviderFormFull:4161eb0049bf4373:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:3039`
- 结构：`ProviderFormFull` / `template`
- 原文/表达式：{<br>  "name": "my-provider",<br>  "base_url": "https://api.example.com/v1",<br>  "api_key": ""<br>}
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{
  "name": "my-provider",
  "base_url": "https://api.example.com/v1",
  "api_key": ""
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4161eb0049bf43738b75b3168099103d4850d43d4104b4e4ecc95c879fecde59`

### 187. `hardcoded:src/components/providers/forms/ProviderForm.tsx:ProviderFormFull:1ae0ca0cfa110297:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:3044`
- 结构：`ProviderFormFull` / `template`
- 原文/表达式：{<br>  "baseUrl": "https://api.example.com/v1",<br>  "apiKey": "your-api-key-here",<br>  "api": "openai-completions",<br>  "models": []<br>}
- 控件属性：`placeholder`
- 判定原因：该英文字符串“{
  "baseUrl": "https://api.example.com/v1",
  "apiKey": "your-api-key-here",
  "api": "openai-completions",
  "models": []
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1ae0ca0cfa1102971706182688606a46b22d1432ea9712ec893740f22eaa37c9`

### 188. `hardcoded:src/components/providers/forms/ProviderForm.tsx:ProviderFormFull:df0d72913440193d:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderForm.tsx:3101`
- 结构：`ProviderFormFull` / `template`
- 原文/表达式：`• ${issue}`
- 判定原因：该英文字符串“`• ${issue}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`df0d72913440193d37dbb8d2b3e9e80054927eff0f1cadb452ae3d96dc51d345`

### 189. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:PresetPicker:2ecf60adfaf48d3d:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:697`
- 结构：`PresetPicker` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.group.${key}`
- 判定原因：翻译键由运行时表达式“`providerPreset.group.${key}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2ecf60adfaf48d3d178598391a5edcfb21b0b69b7e6065cf8e11a0889b2e42c8`

### 190. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:PresetPicker:4449886f332aee87:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:724`
- 结构：`PresetPicker` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.groupHint.${category}`
- 判定原因：翻译键由运行时表达式“`providerPreset.groupHint.${category}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4449886f332aee87414a8ce0440ca4bc27fab6e67a88ccd42680c8db56b7c721`

### 191. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:PresetPicker:d66617847d5d3184:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:788`
- 结构：`PresetPicker` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.group.${section.group}`
- 判定原因：翻译键由运行时表达式“`providerPreset.group.${section.group}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`d66617847d5d31849ee9eda8fb528297c5c5dfb871a7ceabcc81f0f1bd37ce06`

### 192. `dynamic-i18n:src/components/providers/forms/ProviderPresetSelector.tsx:presetRowDetail:1ef66cb0a07d81d7:001`

- 状态：待核实
- 文件：`src/components/providers/forms/ProviderPresetSelector.tsx:830`
- 结构：`presetRowDetail` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.loginWith.${loginAccountKey(appId, first.preset)}`
- 判定原因：翻译键由运行时表达式“`providerPreset.loginWith.${loginAccountKey(appId, first.preset)}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1ef66cb0a07d81d78c015661ad1c310dc8cab09720e08dd47e36ce6c29953f61`

### 193. `hardcoded:src/components/providers/forms/helpers/opencodeFormUtils.ts:OPENCODE_EXTRA_OPTION_DRAFT_PREFIX:01b63fbbc50ec269:001`

- 状态：待核实
- 文件：`src/components/providers/forms/helpers/opencodeFormUtils.ts:57`
- 结构：`OPENCODE_EXTRA_OPTION_DRAFT_PREFIX` / `string`
- 原文/表达式：draft-option:
- 判定原因：该英文字符串“draft-option:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`01b63fbbc50ec26936b3b7fb0f84b5bfce5929320959b1ae6ade126b3c975da1`

### 194. `hardcoded:src/components/providers/forms/helpers/requestHeaders.ts:REQUEST_HEADER_DRAFT_PREFIX:4cfac90d8fd36cb7:001`

- 状态：待核实
- 文件：`src/components/providers/forms/helpers/requestHeaders.ts:1`
- 结构：`REQUEST_HEADER_DRAFT_PREFIX` / `string`
- 原文/表达式：draft-header:
- 判定原因：该英文字符串“draft-header:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4cfac90d8fd36cb7daa7285167fc65ae32bf38c8cf9a55dbe2d3f1ec290cc1c4`

### 195. `dynamic-i18n:src/components/providers/forms/hooks/useKimiOAuth.ts:poll:54e9f1fe2ffcfff0:001`

- 状态：待核实
- 文件：`src/components/providers/forms/hooks/useKimiOAuth.ts:97`
- 结构：`poll` / `dynamic_i18n_key`
- 原文/表达式：`kimi.oauth.${result.ended}`
- 判定原因：翻译键由运行时表达式“`kimi.oauth.${result.ended}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`54e9f1fe2ffcfff049ba8449c17135b0df6090267d74cc0de907ad199e1ffe7e`

### 196. `hardcoded:src/components/providers/forms/hooks/useOmoModelSource.ts:label:0a04523657c2a840:001`

- 状态：待核实
- 文件：`src/components/providers/forms/hooks/useOmoModelSource.ts:187`
- 结构：`label` / `template`
- 原文/表达式：`${providerDisplayName} / ${modelName} (${modelId})`
- 判定原因：该英文字符串“`${providerDisplayName} / ${modelName} (${modelId})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0a04523657c2a840246e549ebdabb9985676efc194e3471a0da2e8e80f8cbcfe`

### 197. `hardcoded:src/components/providers/forms/hooks/useOmoModelSource.ts:omoModelBuild:6dab1f267cdba5c1:001`

- 状态：待核实
- 文件：`src/components/providers/forms/hooks/useOmoModelSource.ts:242`
- 结构：`omoModelBuild` / `template`
- 原文/表达式：`${model.providerId} / ${model.modelId}`
- 判定原因：该英文字符串“`${model.providerId} / ${model.modelId}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6dab1f267cdba5c1dedb6142ba28b795b66f4ae8bfca79b7264b6195602dfe1a`

### 198. `hardcoded:src/components/providers/forms/hooks/useOmoModelSource.ts:signature:24977a93dd4bf0cd:001`

- 状态：待核实
- 文件：`src/components/providers/forms/hooks/useOmoModelSource.ts:270`
- 结构：`signature` / `template`
- 原文/表达式：`${fallback ? "fallback:" : ""}${failed<br>      .slice()<br>      .sort()<br>      .join(",")}`
- 判定原因：该英文字符串“`${fallback ? "fallback:" : ""}${failed
      .slice()
      .sort()
      .join(",")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`24977a93dd4bf0cd6b8fccc709f3f88bcf2330f16b5f5a6df25ea9631e000ab7`

### 199. `hardcoded:src/components/providers/forms/hooks/useOmoModelSource.ts:signature:791e63429b402f3a:001`

- 状态：待核实
- 文件：`src/components/providers/forms/hooks/useOmoModelSource.ts:270`
- 结构：`signature` / `string`
- 原文/表达式：fallback:
- 判定原因：该英文字符串“fallback:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`791e63429b402f3a6f63aa1bd4d37e48e839b2cdd7dc8a619ef99afba2d5a57c`

### 200. `hardcoded:src/components/providers/forms/hooks/useOpenclawFormState.ts:OPENCLAW_DEFAULT_USER_AGENT:b7592e83088dd0ef:001`

- 状态：待核实
- 文件：`src/components/providers/forms/hooks/useOpenclawFormState.ts:18`
- 结构：`OPENCLAW_DEFAULT_USER_AGENT` / `string`
- 原文/表达式：Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
- 判定原因：该英文字符串“Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b7592e83088dd0ef68ba9f3553a9f670b04f658da05ee5953a0bc593977d9fb9`

### 201. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:presetDisplayName:e0d3c7fcb27f761e:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:87`
- 结构：`presetDisplayName` / `dynamic_i18n_key`
- 原文/表达式：preset.nameKey
- 判定原因：翻译键由运行时表达式“preset.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e0d3c7fcb27f761eebb20fc8cf99a5791d148a2af8c0b379684a6db1387b2e6c`

### 202. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:familyDisplayName:68cf4bfef554bafb:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:209`
- 结构：`familyDisplayName` / `dynamic_i18n_key`
- 原文/表达式：info.nameKey
- 判定原因：翻译键由运行时表达式“info.nameKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`68cf4bfef554bafbbd4e399d25b37bd8e3bb6897a13d8ac9002f1a43095def2a`

### 203. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:presetPlanLabel:0e82ff606c3fadd8:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:219`
- 结构：`presetPlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.plan.${plan}`
- 判定原因：翻译键由运行时表达式“`providerPreset.plan.${plan}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0e82ff606c3fadd8ea8cb6573f83fc7fc69e4f4d6bf6f49f625112a4e0dc6fd3`

### 204. `dynamic-i18n:src/components/providers/forms/presetGroups.ts:presetRegionLabel:ad2da87a36c33418:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:226`
- 结构：`presetRegionLabel` / `dynamic_i18n_key`
- 原文/表达式：`providerPreset.region.${region}`
- 判定原因：翻译键由运行时表达式“`providerPreset.region.${region}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`ad2da87a36c334182cc13e04e16921b7c57d3a7ef14cc3ca7bf8141dfb6c050f`

### 205. `hardcoded:src/components/providers/forms/presetGroups.ts:PINYIN_BOUNDARIES:19c5ea98c97ffa7a:001`

- 状态：待核实
- 文件：`src/components/providers/forms/presetGroups.ts:388`
- 结构：`PINYIN_BOUNDARIES` / `string`
- 原文/表达式：阿八嚓哒妸发旮哈讥咔垃痳拏噢妑七呥扨它穵夕丫帀
- 判定原因：该中文自然语言“阿八嚓哒妸发旮哈讥咔垃痳拏噢妑七呥扨它穵夕丫帀”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`19c5ea98c97ffa7aa52ab4045f709a1c5eb96f58a0fe93be20feb03ace0dde78`

### 206. `dynamic-i18n:src/components/providers/forms/shared/ApiKeySection.tsx:promotion:8c26f1886f0b1401:001`

- 状态：待核实
- 文件：`src/components/providers/forms/shared/ApiKeySection.tsx:60`
- 结构：`promotion` / `dynamic_i18n_key`
- 原文/表达式：`providerForm.partnerPromotion.${partnerPromotionKey}`
- 判定原因：翻译键由运行时表达式“`providerForm.partnerPromotion.${partnerPromotionKey}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8c26f1886f0b14011ff0e721dfc8edb5f48c997d1bc53b50eb2204d9dc05337d`

### 207. `hardcoded:src/components/providers/mode/ModeDialog.tsx:MODE_LABEL:b9670c85a4ab939e:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:45`
- 结构：`MODE_LABEL` / `string`
- 原文/表达式：路由
- 判定原因：该中文自然语言“路由”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`b9670c85a4ab939eebef4821f4f6dad33dd7bc541eea594653d1fdd2ba1ee733`

### 208. `hardcoded:src/components/providers/mode/ModeDialog.tsx:MODE_LABEL:a4768faecb385ed9:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:46`
- 结构：`MODE_LABEL` / `string`
- 原文/表达式：聚合
- 判定原因：该中文自然语言“聚合”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`a4768faecb385ed91181804fde350f669981fba1f4ff0f9c2ede2d61d318e9a2`

### 209. `hardcoded:src/components/providers/mode/ModeDialog.tsx:subject:76dbd40504a70a44:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:53`
- 结构：`subject` / `template`
- 原文/表达式：`进入${MODE_LABEL[state.target]}模式确认框`
- 判定原因：该中文自然语言“`进入${MODE_LABEL[state.target]}模式确认框`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`76dbd40504a70a440cc886dcb42836d185db121e831f66c306f9c1661313852b`

### 210. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:EnterBody:fcdbad57bad3a97a:001`

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

### 211. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:targetName:9a6e6056bc68a344:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:249`
- 结构：`targetName` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${target}`
- 判定原因：翻译键由运行时表达式“`mode.names.${target}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`9a6e6056bc68a34442b51307c97d01a3e76078bb220dcf7407babd52712f33fc`

### 212. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:title:63b0f1c3e4f1b584:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:253`
- 结构：`title` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 213. `dynamic-i18n:src/components/providers/mode/ModeDialog.tsx:ExitBody:63b0f1c3e4f1b584:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeDialog.tsx:427`
- 结构：`ExitBody` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 214. `dynamic-i18n:src/components/providers/mode/ModeTabs.tsx:ModeTabs:8594999185d253ca:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeTabs.tsx:117`
- 结构：`ModeTabs` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${mode}`
- 判定原因：翻译键由运行时表达式“`mode.names.${mode}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8594999185d253cac67012cdf03429a7ec6a6ed8cb4300166ad5416582da216c`

### 215. `dynamic-i18n:src/components/providers/mode/ModeTabs.tsx:ModeTabs:37635fc3d0ebe24c:001`

- 状态：待核实
- 文件：`src/components/providers/mode/ModeTabs.tsx:135`
- 结构：`ModeTabs` / `dynamic_i18n_key`
- 原文/表达式：`mode.help.${mode}`
- 判定原因：翻译键由运行时表达式“`mode.help.${mode}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`37635fc3d0ebe24c450c409de557a403a6c39ba395160f060bc6ccec166eb53e`

### 216. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:63b0f1c3e4f1b584:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:384`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 217. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:3ccf2e312468eabd:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:429`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${startupFailure.stack ? "stack" : "route"}`
- 判定原因：翻译键由运行时表达式“`mode.names.${startupFailure.stack ? "stack" : "route"}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`3ccf2e312468eabdf00e60d92ec7776db283fd6d7e87cfc7b634be1f206a230f`

### 218. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:b01ceb686ee7b005:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:467`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`provider.${stack.notice}`
- 判定原因：翻译键由运行时表达式“`provider.${stack.notice}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b01ceb686ee7b00588f9215bbf65e9ac8c98db79940c176eae397729fbabcfda`

### 219. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:814432bf883e93e6:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:484`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`provider.officialModelsReason.${reason}`
- 判定原因：翻译键由运行时表达式“`provider.officialModelsReason.${reason}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`814432bf883e93e6bcf7f75f4854fd3f7eacbd30847844d2868e8d7483ae4975`

### 220. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:5183420e5cea98fb:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:517`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${view}`
- 判定原因：翻译键由运行时表达式“`mode.names.${view}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5183420e5cea98fb0fba783012ad5279a99efc3025b661f1e77f4545e14792a3`

### 221. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:63b0f1c3e4f1b584:002`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:519`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 222. `hardcoded:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:5067328e35b0d0f2:001`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:545`
- 结构：`SwitchModePanel` / `template`
- 原文/表达式：`${status.lead} ${status.value}`
- 判定原因：该英文字符串“`${status.lead} ${status.value}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5067328e35b0d0f2c4e6b6bb68443ffd527482490b048bf281b2e5a11a64138d`

### 223. `hardcoded:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:5067328e35b0d0f2:002`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:548`
- 结构：`SwitchModePanel` / `template`
- 原文/表达式：`${status.lead} ${status.value}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${status.lead} ${status.value}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5067328e35b0d0f2c4e6b6bb68443ffd527482490b048bf281b2e5a11a64138d`

### 224. `dynamic-i18n:src/components/providers/mode/SwitchModePanel.tsx:SwitchModePanel:63b0f1c3e4f1b584:003`

- 状态：待核实
- 文件：`src/components/providers/mode/SwitchModePanel.tsx:570`
- 结构：`SwitchModePanel` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${active}`
- 判定原因：翻译键由运行时表达式“`mode.names.${active}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`63b0f1c3e4f1b5844cf9ab36a0201e715c7fde17d52bc65f3eba1670110d2047`

### 225. `hardcoded:src/components/providers/presentation.ts:queueItems:493b07f1bebf4d7b:001`

- 状态：待核实
- 文件：`src/components/providers/presentation.ts:380`
- 结构：`queueItems` / `template`
- 原文/表达式：`P${index + 1}`
- 判定原因：该英文字符串“`P${index + 1}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`493b07f1bebf4d7b6b3b2d1adcf67ed840954509207f65386d7e06540bb7b9ec`

### 226. `dynamic-i18n:src/components/providers/presentation.ts:buildSwitchSectionsByView:952b41156d70dc1d:001`

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

### 227. `dynamic-i18n:src/components/providers/presentation.ts:piBlocked:770eceac0b7cd3f8:001`

- 状态：待核实
- 文件：`src/components/providers/presentation.ts:717`
- 结构：`piBlocked` / `dynamic_i18n_key`
- 原文/表达式：`${app}.current.stateUnavailableHint`
- 判定原因：翻译键由运行时表达式“`${app}.current.stateUnavailableHint`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`770eceac0b7cd3f834ccbb1e0089fc40822d920a9092c85a9fdb59d52b54946a`

### 228. `dynamic-i18n:src/components/providers/presentation.ts:buildAdditiveSections:2eb4a51baae54d37:001`

- 状态：待核实
- 文件：`src/components/providers/presentation.ts:957`
- 结构：`buildAdditiveSections` / `dynamic_i18n_key`
- 原文/表达式：`apps.${app}`
- 判定原因：翻译键由运行时表达式“`apps.${app}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2eb4a51baae54d37ab7eb80531cacac553f173e0b41fa7516dd5b8ce6e6e5ef3`

### 229. `hardcoded:src/components/proxy/AutoFailoverConfigPanel.tsx:checkRange:4fd9cb179be0fe0c:001`

- 状态：待核实
- 文件：`src/components/proxy/AutoFailoverConfigPanel.tsx:101`
- 结构：`checkRange` / `template`
- 原文/表达式：`${label}: ${range.min}-${range.max}`
- 判定原因：该英文字符串“`${label}: ${range.min}-${range.max}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4fd9cb179be0fe0c51901353edf5b44b314d89730b5a9d74f025ebeb14b29958`

### 230. `hardcoded:src/components/quota/QuotaLines.tsx:className:24ea28558154b40e:001`

- 状态：待核实
- 文件：`src/components/quota/QuotaLines.tsx:273`
- 结构：`className` / `string`
- 原文/表达式：flex shrink-0 flex-col items-end text-caption leading-[18px] tabular-nums whitespace-nowrap
- 判定原因：该英文字符串“flex shrink-0 flex-col items-end text-caption leading-[18px] tabular-nums whitespace-nowrap”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`24ea28558154b40eebecc0d993d465049e3c81f1b518f3aeb2f52e828ab9e14f`

### 231. `hardcoded:src/components/quota/QuotaLines.tsx:SplitQuotaColumn:52887338717ba4d5:001`

- 状态：待核实
- 文件：`src/components/quota/QuotaLines.tsx:577`
- 结构：`SplitQuotaColumn` / `template`
- 原文/表达式：`${refreshText} · ${t("quota.clickToRefresh")}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${refreshText} · ${t("quota.clickToRefresh")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`52887338717ba4d5d47d3d324031970bf8bc73ae19b9881c42d0e4a3ec60b403`

### 232. `hardcoded:src/components/quota/QuotaLines.tsx:BAR_ROW_CLASS:62556b1602c85b7c:001`

- 状态：待核实
- 文件：`src/components/quota/QuotaLines.tsx:619`
- 结构：`BAR_ROW_CLASS` / `string`
- 原文/表达式：flex h-[18px] items-center gap-2 text-caption
- 判定原因：该英文字符串“flex h-[18px] items-center gap-2 text-caption”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`62556b1602c85b7c14259056da7edb6a57b6fa4a279e457e4fb773deab9c6beb`

### 233. `hardcoded:src/components/quota/QuotaLines.tsx:cells:3e2975c92c22ea2e:001`

- 状态：待核实
- 文件：`src/components/quota/QuotaLines.tsx:690`
- 结构：`cells` / `template`
- 原文/表达式：`${label}: ${line.value ?? line.text}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${label}: ${line.value ?? line.text}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3e2975c92c22ea2e7e479100032dc18677413423b103e4b5f25a984eed0c0e59`

### 234. `hardcoded:src/components/quota/quotaRules.ts:labelParams:13794833d43f5449:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:76`
- 结构：`labelParams` / `template`
- 原文/表达式：`${label} `
- 判定原因：该英文字符串“`${label} `”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`13794833d43f54494869cb0831c0586f61dca7983eee4ead645f4bcccf8dcc14`

### 235. `hardcoded:src/components/quota/quotaRules.ts:countdownStr:5d56a877614b75c9:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:90`
- 结构：`countdownStr` / `template`
- 原文/表达式：`${Math.floor(hours / 24)}d${hours % 24}h`
- 判定原因：该英文字符串“`${Math.floor(hours / 24)}d${hours % 24}h`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5d56a877614b75c912cd22348b87c8207d44fa9df7127affa6b4ddcb7b44c844`

### 236. `dynamic-i18n:src/components/quota/quotaRules.ts:tierLine:02df858ef720e28a:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:138`
- 结构：`tierLine` / `dynamic_i18n_key`
- 原文/表达式：used ? "quota.tierUsed" : "quota.tierLeft"
- 判定原因：翻译键由运行时表达式“used ? "quota.tierUsed" : "quota.tierLeft"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`02df858ef720e28a4a4700bfa3a586d2aa0d1d78d213ecaba83e2595ca282025`

### 237. `dynamic-i18n:src/components/quota/quotaRules.ts:tierLine:b5286d080dc232bd:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:145`
- 结构：`tierLine` / `dynamic_i18n_key`
- 原文/表达式：used ? "quota.used" : "quota.left"
- 判定原因：翻译键由运行时表达式“used ? "quota.used" : "quota.left"”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`b5286d080dc232bde98cb700bc4010de3f717b23353e15e6964b735a20805ed0`

### 238. `hardcoded:src/components/quota/quotaRules.ts:lineHint:8c3eea1cee4a76b7:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:176`
- 结构：`lineHint` / `template`
- 原文/表达式：`${line.label} · ${reset}`
- 判定原因：该英文字符串“`${line.label} · ${reset}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8c3eea1cee4a76b742724e7dab4523cdb87de62c299ef93cd1b05e137bdc329a`

### 239. `hardcoded:src/components/quota/quotaRules.ts:value:fb1c80078c42c46d:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:378`
- 结构：`value` / `template`
- 原文/表达式：`${amount.toFixed(2)}${unit ? ` ${unit}` : ""}`
- 判定原因：该英文字符串“`${amount.toFixed(2)}${unit ? ` ${unit}` : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fb1c80078c42c46d0f53a0c6d674bbf3d1278c380c7e450a2756e55ad96480ce`

### 240. `hardcoded:src/components/quota/quotaRules.ts:value:6b28d9e03de17ad9:001`

- 状态：待核实
- 文件：`src/components/quota/quotaRules.ts:378`
- 结构：`value` / `template`
- 原文/表达式：` ${unit}`
- 判定原因：该英文字符串“` ${unit}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6b28d9e03de17ad993e8ca84831770404d1317d2f8e1df0a8467f4159e12f33f`

### 241. `hardcoded:src/components/sessions/SessionDialogs.tsx:dialogClass:17517a6152ad7bb8:001`

- 状态：待核实
- 文件：`src/components/sessions/SessionDialogs.tsx:20`
- 结构：`dialogClass` / `string`
- 原文/表达式：max-w-[480px] gap-4 rounded-dialog border-border bg-surface p-6 shadow-v7-lg sm:rounded-dialog
- 判定原因：该英文字符串“max-w-[480px] gap-4 rounded-dialog border-border bg-surface p-6 shadow-v7-lg sm:rounded-dialog”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`17517a6152ad7bb830594ba040da4d3b12056db7e3e691f0e642c13c5597c27b`

### 242. `dynamic-i18n:src/components/sessions/SessionItem.tsx:deleteReason:26c0854586264f75:001`

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

### 243. `hardcoded:src/components/sessions/SessionManagerPage.tsx:linkButton:2ef5d2d99339f66b:001`

- 状态：待核实
- 文件：`src/components/sessions/SessionManagerPage.tsx:126`
- 结构：`linkButton` / `string`
- 原文/表达式：h-[22px] rounded-[4px] px-0.5 text-caption text-fg-1 underline decoration-border-strong underline-offset-[3px] hover:decoration-fg-2
- 判定原因：该英文字符串“h-[22px] rounded-[4px] px-0.5 text-caption text-fg-1 underline decoration-border-strong underline-offset-[3px] hover:decoration-fg-2”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2ef5d2d99339f66b4236ce13022af1cec63c57491e97f5374e0eb201ba7914fd`

### 244. `dynamic-i18n:src/components/sessions/SessionManagerPage.tsx:label:2c70e12b7a0646f9:001`

- 状态：待核实
- 文件：`src/components/sessions/SessionManagerPage.tsx:312`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：key
- 判定原因：翻译键由运行时表达式“key”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683`

### 245. `hardcoded:src/components/sessions/SessionManagerPage.tsx:deletedKeys:c0d5b9aa0908fba5:001`

- 状态：待核实
- 文件：`src/components/sessions/SessionManagerPage.tsx:508`
- 结构：`deletedKeys` / `template`
- 原文/表达式：`${result.providerId}:${result.sessionId}:${result.sourcePath ?? ""}`
- 判定原因：该英文字符串“`${result.providerId}:${result.sessionId}:${result.sourcePath ?? ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c0d5b9aa0908fba5415d5238be84c4ab5deaa596da710839b1a6f2a984736759`

### 246. `hardcoded:src/components/sessions/SessionManagerPage.tsx:renderProjectHeader:028a891c0bb5fc32:001`

- 状态：待核实
- 文件：`src/components/sessions/SessionManagerPage.tsx:794`
- 结构：`renderProjectHeader` / `template`
- 原文/表达式：`${appName(app)} ${count}`
- 判定原因：该英文字符串“`${appName(app)} ${count}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`028a891c0bb5fc321681ae1f2675b5e971c1550eb01b5094895276b7b99f4523`

### 247. `hardcoded:src/components/sessions/reader/PathChip.tsx:PathChip:63da264f49765c77:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/PathChip.tsx:136`
- 结构：`PathChip` / `template`
- 原文/表达式：`${copyLabel}: ${localPath}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${copyLabel}: ${localPath}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`63da264f49765c771f1ea3df6827e4a50d410ef8198212d25a099dab8636e60a`

### 248. `hardcoded:src/components/sessions/reader/SessionCodeBlock.tsx:SESSION_INLINE_CODE_CLASS:0d586a1523c16900:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionCodeBlock.tsx:15`
- 结构：`SESSION_INLINE_CODE_CLASS` / `string`
- 原文/表达式：rounded-[4px] px-1 py-px font-mono text-[0.92em] text-fg-1
- 判定原因：该英文字符串“rounded-[4px] px-1 py-px font-mono text-[0.92em] text-fg-1”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0d586a1523c169006a8d3690cc9ffe5ee87b84b2b00bb31b04de3455cf2c1867`

### 249. `hardcoded:src/components/sessions/reader/SessionDiff.tsx:parseDiff:d7075d60cad8f0fd:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionDiff.tsx:54`
- 结构：`parseDiff` / `string`
- 原文/表达式：*** Begin Patch
- 判定原因：该英文字符串“*** Begin Patch”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d7075d60cad8f0fd34f43cd2ea6972636ab3ad4b630ac82be7d60402dc049c0a`

### 250. `hardcoded:src/components/sessions/reader/SessionDiff.tsx:parseDiff:7b317d3955797c76:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionDiff.tsx:55`
- 结构：`parseDiff` / `string`
- 原文/表达式：*** End Patch
- 判定原因：该英文字符串“*** End Patch”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7b317d3955797c769e55497ebfb2a0d5198436a71dff16226b6e37158e4261e5`

### 251. `hardcoded:src/components/sessions/reader/SessionDiff.tsx:parseDiff:5a23bd12069f42da:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionDiff.tsx:56`
- 结构：`parseDiff` / `string`
- 原文/表达式：\ No newline
- 判定原因：该英文字符串“\ No newline”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5a23bd12069f42dae648450c687263d063156363660de82e31880b8e5175cc1b`

### 252. `hardcoded:src/components/sessions/reader/SessionDiff.tsx:parseDiff:a3728fd3516d3283:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionDiff.tsx:72`
- 结构：`parseDiff` / `string`
- 原文/表达式：*** Move to:
- 判定原因：该英文字符串“*** Move to:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a3728fd3516d328368de0af27153bb8baea07b8f2302ae317f43966a64af431f`

### 253. `hardcoded:src/components/sessions/reader/SessionDiff.tsx:parseDiff:a3728fd3516d3283:002`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionDiff.tsx:73`
- 结构：`parseDiff` / `string`
- 原文/表达式：*** Move to:
- 判定原因：该英文字符串“*** Move to:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a3728fd3516d328368de0af27153bb8baea07b8f2302ae317f43966a64af431f`

### 254. `hardcoded:src/components/sessions/reader/SessionDiff.tsx:buildInputDiff:3d641177afb7cdf5:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionDiff.tsx:169`
- 结构：`buildInputDiff` / `template`
- 原文/表达式：`@@\n${[<br>          ...splitLines(old).map((line) => `-${line}`),<br>          ...splitLines(next).map((line) => `+${line}`),<br>        ].join("\n")}`
- 判定原因：该英文字符串“`@@\n${[
          ...splitLines(old).map((line) => `-${line}`),
          ...splitLines(next).map((line) => `+${line}`),
        ].join("\n")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3d641177afb7cdf52ed79811d65ad61b2f159c92085bb65ae23842580ae04e09`

### 255. `hardcoded:src/components/sessions/reader/SessionEventRow.tsx:injectedLabel:2682db8890edcb16:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionEventRow.tsx:239`
- 结构：`injectedLabel` / `template`
- 原文/表达式：`${first.slice(0, 32)}…`
- 判定原因：该英文字符串“`${first.slice(0, 32)}…`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2682db8890edcb1692c6197c33a8bdb17171e11e6b07a585f6b85ff014e4fb2d`

### 256. `hardcoded:src/components/sessions/reader/SessionEventRow.tsx:chars:d74d869e0c8c910a:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionEventRow.tsx:256`
- 结构：`chars` / `template`
- 原文/表达式：`${text.length.toLocaleString()}${partial ? "+" : ""}`
- 判定原因：该英文字符串“`${text.length.toLocaleString()}${partial ? "+" : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d74d869e0c8c910ac01a107b85c7621c6720ab7c1d44d4d91ee6d6ead39d7f7f`

### 257. `hardcoded:src/components/sessions/reader/SessionFinalReply.tsx:rawSnippets:80e61a55831fdfdc:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionFinalReply.tsx:38`
- 结构：`rawSnippets` / `template`
- 原文/表达式：`${start > 0 ? "…" : ""}${text.slice(start, end).replace(/\s+/g, " ")}${end < text.length ? "…" : ""}`
- 判定原因：该英文字符串“`${start > 0 ? "…" : ""}${text.slice(start, end).replace(/\s+/g, " ")}${end < text.length ? "…" : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`80e61a55831fdfdc4e7bc8902f2617f04789cd555e44a85714fa782b9dc4651b`

### 258. `hardcoded:src/components/sessions/reader/SessionImage.tsx:SessionImage:32b4440270b89f31:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionImage.tsx:82`
- 结构：`SessionImage` / `template`
- 原文/表达式：`${alt} · ${rt("image.failed")}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${alt} · ${rt("image.failed")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`32b4440270b89f31bf06bf22bfc5938b051c87eb4b2fca2a796a818d2c5d3eda`

### 259. `hardcoded:src/components/sessions/reader/SessionMarkdown.tsx:LINK_CLASS:5fbbf33bcd89737e:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionMarkdown.tsx:609`
- 结构：`LINK_CLASS` / `string`
- 原文/表达式：rounded-[2px] text-action-text underline-offset-[3px] hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring
- 判定原因：该英文字符串“rounded-[2px] text-action-text underline-offset-[3px] hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5fbbf33bcd89737ea17316c48c613b6e5fb5a481f488cf463eafa15821e933c1`

### 260. `hardcoded:src/components/sessions/reader/SessionMarkdown.tsx:RemoteImage:d85e2f66ade87760:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionMarkdown.tsx:724`
- 结构：`RemoteImage` / `template`
- 原文/表达式：`${loadLabel}: ${label}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${loadLabel}: ${label}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d85e2f66ade877607561b4e3cc03eab53d71e5343575610f7a220c6a72049a1e`

### 261. `hardcoded:src/components/sessions/reader/SessionOutline.tsx:SessionOutline:d13d464b5a783f24:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionOutline.tsx:136`
- 结构：`SessionOutline` / `template`
- 原文/表达式：` · ${formatMessageTime(entry.turn.question.ts)}`
- 判定原因：该英文字符串“` · ${formatMessageTime(entry.turn.question.ts)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d13d464b5a783f242c36910f4f4f380a3a4d2e371e322c85440ccc0646f13c87`

### 262. `hardcoded:src/components/sessions/reader/SessionOutline.tsx:SessionOutline:81a7128bd23417af:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionOutline.tsx:144`
- 结构：`SessionOutline` / `string`
- 原文/表达式：color-mix(in srgb, var(--reader-accent) 14%, var(--bg-subtle))
- 判定原因：该英文字符串“color-mix(in srgb, var(--reader-accent) 14%, var(--bg-subtle))”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`81a7128bd23417af05e4a92bfc7c7075f0cc879903a072ea897b2e523ac4a5cc`

### 263. `hardcoded:src/components/sessions/reader/SessionQuestion.tsx:formatCharCount:e160bcaaf07b06d9:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionQuestion.tsx:22`
- 结构：`formatCharCount` / `template`
- 原文/表达式：`${(count / 1000).toFixed(1)}k`
- 判定原因：该英文字符串“`${(count / 1000).toFixed(1)}k`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e160bcaaf07b06d96896ba8dd2b0fe33c4af5e58792c01db5da849287eb90e93`

### 264. `hardcoded:src/components/sessions/reader/SessionQuestion.tsx:rowIconButton:c6cde6d21bf248af:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionQuestion.tsx:25`
- 结构：`rowIconButton` / `string`
- 原文/表达式：inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-control text-fg-3 opacity-0 transition-[opacity,color,background-color] hover:bg-selected hover:text-fg-1 focus-visible:opacity-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring
- 判定原因：该英文字符串“inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-control text-fg-3 opacity-0 transition-[opacity,color,background-color] hover:bg-selected hover:text-fg-1 focus-visible:opacity-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c6cde6d21bf248af2c48d07ff9814fd2d721cd7ec9a75fb06f12d6e482c99c48`

### 265. `hardcoded:src/components/sessions/reader/SessionQuestion.tsx:SessionQuestion:81a7128bd23417af:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionQuestion.tsx:130`
- 结构：`SessionQuestion` / `string`
- 原文/表达式：color-mix(in srgb, var(--reader-accent) 14%, var(--bg-subtle))
- 判定原因：该英文字符串“color-mix(in srgb, var(--reader-accent) 14%, var(--bg-subtle))”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`81a7128bd23417af05e4a92bfc7c7075f0cc879903a072ea897b2e523ac4a5cc`

### 266. `hardcoded:src/components/sessions/reader/SessionReader.tsx:isEditableTarget:3938f91a7b8377f4:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionReader.tsx:126`
- 结构：`isEditableTarget` / `string`
- 原文/表达式：input, textarea, select, [contenteditable="true"], [role="menu"], [role="dialog"], [role="alertdialog"]
- 判定原因：该英文字符串“input, textarea, select, [contenteditable="true"], [role="menu"], [role="dialog"], [role="alertdialog"]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3938f91a7b8377f49f51c19740837fc9d1ec4d89a3bac57800f09f99f895d743`

### 267. `hardcoded:src/components/sessions/reader/SessionReader.tsx:name:7f62c24d65f4c0f3:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionReader.tsx:426`
- 结构：`name` / `template`
- 原文/表达式：`${toFileName(title) \|\| session.sessionId}.md`
- 判定原因：该英文字符串“`${toFileName(title) || session.sessionId}.md`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7f62c24d65f4c0f35c21dd601842b09abecbfe555db752bba9bce657eb9b8675`

### 268. `dynamic-i18n:src/components/sessions/reader/SessionReaderHeader.tsx:moreMenu:d9527cde90f33c89:001`

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

### 269. `hardcoded:src/components/sessions/reader/SessionReaderHeader.tsx:formatRange:f7ed4c2237a8b6f8:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionReaderHeader.tsx:466`
- 结构：`formatRange` / `template`
- 原文/表达式：`${formatShortDateTime(created)} → ${<br>      sameDay ? formatClock(last) : formatShortDateTime(last)<br>    }`
- 判定原因：该英文字符串“`${formatShortDateTime(created)} → ${
      sameDay ? formatClock(last) : formatShortDateTime(last)
    }`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f7ed4c2237a8b6f8ac65df0fdade3231cdcba28c6e3440b5a4b0a1b493a366f0`

### 270. `hardcoded:src/components/sessions/reader/SessionReaderHeader.tsx:SessionReaderToolbar:766c56b193420bcb:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionReaderHeader.tsx:805`
- 结构：`SessionReaderToolbar` / `template`
- 原文/表达式：`${find.current} / ${find.total}`
- 判定原因：该英文字符串“`${find.current} / ${find.total}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`766c56b193420bcb4ca734eaeb2657c26293185bb76155f602a2681548dbef44`

### 271. `hardcoded:src/components/sessions/reader/SessionStep.tsx:ToolRow:949766eca21a6499:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionStep.tsx:117`
- 结构：`ToolRow` / `template`
- 原文/表达式：`${rt("stepCollapse")} ${fullTitle}（${statusText}）`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${rt("stepCollapse")} ${fullTitle}（${statusText}）`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`949766eca21a64999fa739fa4ee6e3e7cb956576c47013c8b222461950dbf53c`

### 272. `hardcoded:src/components/sessions/reader/SessionStepDetails.tsx:linkButton:4cc0319d831cc5cb:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionStepDetails.tsx:19`
- 结构：`linkButton` / `string`
- 原文/表达式：rounded-[2px] text-caption text-fg-2 underline decoration-border-strong underline-offset-[3px] transition-colors hover:text-fg-1 hover:decoration-fg-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring
- 判定原因：该英文字符串“rounded-[2px] text-caption text-fg-2 underline decoration-border-strong underline-offset-[3px] transition-colors hover:text-fg-1 hover:decoration-fg-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4cc0319d831cc5cb2d675d4fae8333ca798280b0a0b1893f913516889752d4a5`

### 273. `hardcoded:src/components/sessions/reader/SessionStepDetails.tsx:VARIANT_CLASS:bce3832d27b7ee18:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionStepDetails.tsx:61`
- 结构：`VARIANT_CLASS` / `string`
- 原文/表达式：whitespace-pre rounded-[8px] bg-subtle px-3 py-2 font-mono text-caption
- 判定原因：该英文字符串“whitespace-pre rounded-[8px] bg-subtle px-3 py-2 font-mono text-caption”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`bce3832d27b7ee18d1189f075c18859776663d7549dcadd07c01c947d7ffd34e`

### 274. `hardcoded:src/components/sessions/reader/SessionStepDetails.tsx:VARIANT_CLASS:bce3832d27b7ee18:002`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionStepDetails.tsx:63`
- 结构：`VARIANT_CLASS` / `string`
- 原文/表达式：whitespace-pre rounded-[8px] bg-subtle px-3 py-2 font-mono text-caption
- 判定原因：该英文字符串“whitespace-pre rounded-[8px] bg-subtle px-3 py-2 font-mono text-caption”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`bce3832d27b7ee18d1189f075c18859776663d7549dcadd07c01c947d7ffd34e`

### 275. `hardcoded:src/components/sessions/reader/SessionThinkingRow.tsx:formatChars:baeb68554b32111c:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionThinkingRow.tsx:13`
- 结构：`formatChars` / `template`
- 原文/表达式：`${Number((count / 1000).toFixed(1))}k`
- 判定原因：该英文字符串“`${Number((count / 1000).toFixed(1))}k`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`baeb68554b32111c0dbfb18126a7eb551edc3d404f557e9190fbc6cff33020ee`

### 276. `hardcoded:src/components/sessions/reader/SessionThinkingRow.tsx:SessionThinkingRow:b18dd8845d6b72e6:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionThinkingRow.tsx:86`
- 结构：`SessionThinkingRow` / `template`
- 原文/表达式：`· ${meta}`
- 判定原因：该英文字符串“`· ${meta}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b18dd8845d6b72e661aec4f88a25eb65c2f96f154466e1fe2df77b75b75bb9e6`

### 277. `hardcoded:src/components/sessions/reader/SessionTimeline.tsx:SessionTimeline:87ffa331925ba44e:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/SessionTimeline.tsx:86`
- 结构：`SessionTimeline` / `template`
- 原文/表达式：`${actionLabel}：${rt("timelineSummary", { steps })}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${actionLabel}：${rt("timelineSummary", { steps })}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`87ffa331925ba44e90aa7fb321d7e2ac275df9da099e9e740c903e210eac7d91`

### 278. `dynamic-i18n:src/components/sessions/reader/exportMarkdown.ts:metaText:05aec9f0cd39e139:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:34`
- 结构：`metaText` / `dynamic_i18n_key`
- 原文/表达式：`status.${meta.status}`
- 判定原因：翻译键由运行时表达式“`status.${meta.status}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`05aec9f0cd39e139e2c75e1ead486816b6f6841d8684ba2eee6364e52bab6605`

### 279. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:metaText:506268935453b63a:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:38`
- 结构：`metaText` / `template`
- 原文/表达式：`+${meta.diff.added} −${meta.diff.removed}`
- 判定原因：该英文字符串“`+${meta.diff.added} −${meta.diff.removed}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`506268935453b63ad4c7bd2bce168bcccb0316f38e2cd8a2fcfb69a7d93df9cb`

### 280. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:metaText:830be889a30feaa5:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:44`
- 结构：`metaText` / `template`
- 原文/表达式：` — ${parts.join(" · ")}`
- 判定原因：该英文字符串“` — ${parts.join(" · ")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`830be889a30feaa58dd3ebdc89711ad8ef4aff8e37819a9b0bb59e8680f526bf`

### 281. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:20beab94303b2b7f:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:66`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}- ${meta.glyph} ${title.text}${metaText(meta, options)}`
- 判定原因：该英文字符串“`${pad}- ${meta.glyph} ${title.text}${metaText(meta, options)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`20beab94303b2b7fd18bc0d6367d27a0f55d4440477ec4a630a22d02077ae228`

### 282. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:20beab94303b2b7f:002`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:72`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}- ${meta.glyph} ${title.text}${metaText(meta, options)}`
- 判定原因：该英文字符串“`${pad}- ${meta.glyph} ${title.text}${metaText(meta, options)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`20beab94303b2b7fd18bc0d6367d27a0f55d4440477ec4a630a22d02077ae228`

### 283. `dynamic-i18n:src/components/sessions/reader/exportMarkdown.ts:label:741390bbafe0c1e5:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:80`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：style.thinkingLabelKey
- 判定原因：翻译键由运行时表达式“style.thinkingLabelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`741390bbafe0c1e585378ac0ca539a88bc64feaaf4716b3d5cfd23aa308d3d3e`

### 284. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:ccd9bd522b294259:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:84`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}- ${glyph}${label}${body ? `: ${indentBody(body, `${pad}  `)}` : ""}`
- 判定原因：该英文字符串“`${pad}- ${glyph}${label}${body ? `: ${indentBody(body, `${pad}  `)}` : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ccd9bd522b29425966ccaf099c650839827b64446cc95c8781156705731f995c`

### 285. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:e2430612ba818134:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:84`
- 结构：`stepLines` / `template`
- 原文/表达式：`: ${indentBody(body, `${pad}  `)}`
- 判定原因：该英文字符串“`: ${indentBody(body, `${pad}  `)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e2430612ba818134201b5cbb87424e6f60c056025a162cc745c712e260d06285`

### 286. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:6305c7889147ff31:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:84`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}  `
- 判定原因：该英文字符串“`${pad}  `”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6305c7889147ff317f0802887094e13b0470d2518fbb522fb8c9cc4674501462`

### 287. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:b66f800f368ea1fc:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:88`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}- ${indentBody(step.text, `${pad}  `)}`
- 判定原因：该英文字符串“`${pad}- ${indentBody(step.text, `${pad}  `)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b66f800f368ea1fc703c898c6f58884966794d7ccee134b792c6ad8aa4185b66`

### 288. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:6305c7889147ff31:002`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:88`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}  `
- 判定原因：该英文字符串“`${pad}  `”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6305c7889147ff317f0802887094e13b0470d2518fbb522fb8c9cc4674501462`

### 289. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:efcdad63f485d596:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:90`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}- [${step.image.alt \|\| t("image.alt", { index: 1 })}]`
- 判定原因：该英文字符串“`${pad}- [${step.image.alt || t("image.alt", { index: 1 })}]`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`efcdad63f485d5969c8906989617067fa34f7f238390eea1d14b1269d5a569f6`

### 290. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:d3986389ae441035:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:93`
- 结构：`stepLines` / `template`
- 原文/表达式：`${pad}- ${label}${detail ? `: ${indentBody(detail)}` : ""}`
- 判定原因：该英文字符串“`${pad}- ${label}${detail ? `: ${indentBody(detail)}` : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d3986389ae441035877ddd5568c5aac0c7736bdce2286f7edf67af53b356c50f`

### 291. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:stepLines:b3f00d540f9f88e1:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:93`
- 结构：`stepLines` / `template`
- 原文/表达式：`: ${indentBody(detail)}`
- 判定原因：该英文字符串“`: ${indentBody(detail)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b3f00d540f9f88e15514d04312958fba78b5e9c43251edf99f130231c9e09eea`

### 292. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:eventLine:8fa44918571a9f48:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:101`
- 结构：`eventLine` / `template`
- 原文/表达式：`> ${label}${url ? ` (${url})` : ""}${detail ? `\n>\n> ${detail.replace(/\n/g, "\n> ")}` : ""}`
- 判定原因：该英文字符串“`> ${label}${url ? ` (${url})` : ""}${detail ? `\n>\n> ${detail.replace(/\n/g, "\n> ")}` : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8fa44918571a9f48853aa9ecf137fc7d2a99839e4a4c60aa399cab12b66aae50`

### 293. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:eventLine:5f2edd44fa27510d:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:101`
- 结构：`eventLine` / `template`
- 原文/表达式：` (${url})`
- 判定原因：该英文字符串“` (${url})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5f2edd44fa27510d0fe90324b8f1800e459887d08a58585645425d428c756a21`

### 294. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:eventLine:e1ec4df27732ef95:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:101`
- 结构：`eventLine` / `template`
- 原文/表达式：`\n>\n> ${detail.replace(/\n/g, "\n> ")}`
- 判定原因：该英文字符串“`\n>\n> ${detail.replace(/\n/g, "\n> ")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e1ec4df27732ef95b252b76374b2eed069bad10537eba691e06aee951ee89f71`

### 295. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:heading:fb66f34c33928674:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:105`
- 结构：`heading` / `template`
- 原文/表达式：`**${label}**${ts ? ` ${formatMessageTime(ts)}` : ""}`
- 判定原因：该英文字符串“`**${label}**${ts ? ` ${formatMessageTime(ts)}` : ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fb66f34c33928674eb5d852269e81ed2042f6e1aa99cfc1b0302302b20d361db`

### 296. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:heading:779821f2e7d76f6b:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:105`
- 结构：`heading` / `template`
- 原文/表达式：` ${formatMessageTime(ts)}`
- 判定原因：该英文字符串“` ${formatMessageTime(ts)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`779821f2e7d76f6bb88180e5593c490ce1e9a0eb981591a27ba6d01dd7bdf003`

### 297. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:images:ae77544f2398add4:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:117`
- 结构：`images` / `template`
- 原文/表达式：`[${image.alt \|\| t("image.alt", { index: index + 1 })}]`
- 判定原因：该英文字符串“`[${image.alt || t("image.alt", { index: index + 1 })}]`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ae77544f2398add4a6b424bd8c377c3441c5a056038ad4b6ace7256c739444af`

### 298. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:turnToMarkdown:67ed7c54a78811f2:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:133`
- 结构：`turnToMarkdown` / `template`
- 原文/表达式：`${heading(options.appName, turn.final.ts)}\n\n${turn.final.text}`
- 判定原因：该英文字符串“`${heading(options.appName, turn.final.ts)}\n\n${turn.final.text}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`67ed7c54a78811f24ddf76fa3cc603873991366d42d9dc989a3a921b592c2414`

### 299. `hardcoded:src/components/sessions/reader/exportMarkdown.ts:transcriptToMarkdown:fdc12f1cc997e8be:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/exportMarkdown.ts:149`
- 结构：`transcriptToMarkdown` / `template`
- 原文/表达式：`# ${title}\n\n${body}\n`
- 判定原因：该英文字符串“`# ${title}\n\n${body}\n`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fdc12f1cc997e8be6f6890a02cc355f5d0bcec3756c13b901a593dcab3e734e9`

### 300. `dynamic-i18n:src/components/sessions/reader/i18n.ts:useReaderT:a18b869b2e81c0c5:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/i18n.ts:140`
- 结构：`useReaderT` / `dynamic_i18n_key`
- 原文/表达式：full
- 判定原因：翻译键由运行时表达式“full”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`a18b869b2e81c0c529552a3c4fa5c92ed08b98a4e146aed778d71d27517f83ac`

### 301. `hardcoded:src/components/sessions/reader/toolSummary.ts:formatTokens:7dbe023cf61c59b6:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:119`
- 结构：`formatTokens` / `template`
- 原文/表达式：`${Number((tokens / 1000).toFixed(1))}k`
- 判定原因：该英文字符串“`${Number((tokens / 1000).toFixed(1))}k`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7dbe023cf61c59b66137318c583778b568aa47469934e3b174c586b7668a4abe`

### 302. `hardcoded:src/components/sessions/reader/toolSummary.ts:formatTokens:7a48cf6e342704df:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:120`
- 结构：`formatTokens` / `template`
- 原文/表达式：`${Number((tokens / 1_000_000).toFixed(1))}M`
- 判定原因：该英文字符串“`${Number((tokens / 1_000_000).toFixed(1))}M`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7a48cf6e342704df1458ec358ecb843ae75d705ec3ed72317ebe6a14a3af2ed2`

### 303. `dynamic-i18n:src/components/sessions/reader/toolSummary.ts:translate:982d9e3eb996f559:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:199`
- 结构：`translate` / `dynamic_i18n_key`
- 原文/表达式：text
- 判定原因：翻译键由运行时表达式“text”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`982d9e3eb996f559e633f4d194def3761d909f5a3b647d1a851fead67c32c9d1`

### 304. `dynamic-i18n:src/components/sessions/reader/toolSummary.ts:verbFor:6806f86a17f0ae04:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:209`
- 结构：`verbFor` / `dynamic_i18n_key`
- 原文/表达式：verb
- 判定原因：翻译键由运行时表达式“verb”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`6806f86a17f0ae04d4ad43168fcdd0651c0fe99108b992f5ac398fd6bf235331`

### 305. `hardcoded:src/components/sessions/reader/toolSummary.ts:codexDiffTitle:f938069fea1084c8:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:221`
- 结构：`codexDiffTitle` / `template`
- 原文/表达式：`${files.length} files`
- 判定原因：该英文字符串“`${files.length} files`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f938069fea1084c8f5d1ec4910f94037e4695985228b8488a0d86a9bf27258f9`

### 306. `dynamic-i18n:src/components/sessions/reader/toolSummary.ts:verb:5c4db77b4c3c9984:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:238`
- 结构：`verb` / `dynamic_i18n_key`
- 原文/表达式：TOOL_OUTPUT_VERB_KEY
- 判定原因：翻译键由运行时表达式“TOOL_OUTPUT_VERB_KEY”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5c4db77b4c3c9984f81b88ec4d1935af79d93dbff11ff45ed52e6b1bad5367cd`

### 307. `hardcoded:src/components/sessions/reader/toolSummary.ts:formatStepTitle:ee224bf2b6d49e47:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:256`
- 结构：`formatStepTitle` / `template`
- 原文/表达式：`${call.title}(${detail ?? ""})`
- 判定原因：该英文字符串“`${call.title}(${detail ?? ""})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ee224bf2b6d49e473d68c78edb37cb26a3a8ebcdf19b188cb29cd1e208d0bd9a`

### 308. `hardcoded:src/components/sessions/reader/toolSummary.ts:formatStepTitle:66b7272067fcf5d1:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:273`
- 结构：`formatStepTitle` / `template`
- 原文/表达式：`${verb} ${target}`
- 判定原因：该英文字符串“`${verb} ${target}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`66b7272067fcf5d1eed3ceeb3d7107329370bf32c6622db7ce5807d2622b1a5a`

### 309. `hardcoded:src/components/sessions/reader/toolSummary.ts:verb:aedfb50ca5b5bf02:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/toolSummary.ts:300`
- 结构：`verb` / `template`
- 原文/表达式：`Called ${step.server} ${count} times`
- 判定原因：该英文字符串“`Called ${step.server} ${count} times`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`aedfb50ca5b5bf02d1c06c8f7a672067708be703acaba210272e016f8d4dd967`

### 310. `hardcoded:src/components/sessions/reader/turns.ts:LEGACY_CALL_PREFIX:fb916ece96f3bc33:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/turns.ts:154`
- 结构：`LEGACY_CALL_PREFIX` / `string`
- 原文/表达式：legacy:
- 判定原因：该英文字符串“legacy:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fb916ece96f3bc33d28795d2ddc4b3049c391f0a3e1c8b2b98164c83757fd223`

### 311. `hardcoded:src/components/sessions/reader/turns.ts:previewText:4943d47188735c57:001`

- 状态：待核实
- 文件：`src/components/sessions/reader/turns.ts:554`
- 结构：`previewText` / `template`
- 原文/表达式：`${flat.slice(0, QUESTION_PREVIEW_CHARS)}…`
- 判定原因：该英文字符串“`${flat.slice(0, QUESTION_PREVIEW_CHARS)}…`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4943d47188735c572d5d75cab4a7f6490ae9f6af9b5f3ef4ba20389f1ca37f99`

### 312. `hardcoded:src/components/sessions/utils.ts:getSessionKey:1a02f51450160eb2:001`

- 状态：待核实
- 文件：`src/components/sessions/utils.ts:70`
- 结构：`getSessionKey` / `template`
- 原文/表达式：`${session.providerId}:${session.sessionId}:${session.sourcePath ?? ""}`
- 判定原因：该英文字符串“`${session.providerId}:${session.sessionId}:${session.sourcePath ?? ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1a02f51450160eb2b2c9a8a9be151240c9938233a9a72035d42a441022f749ad`

### 313. `hardcoded:src/components/sessions/utils.ts:buildCdResumeCommand:8e6824ca5b8aa702:001`

- 状态：待核实
- 文件：`src/components/sessions/utils.ts:268`
- 结构：`buildCdResumeCommand` / `template`
- 原文/表达式：`cd '${projectDir.replace(/'/g, `'\\''`)}' && ${command}`
- 判定原因：该英文字符串“`cd '${projectDir.replace(/'/g, `'\\''`)}' && ${command}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8e6824ca5b8aa702ccfa73564f28f4193d25b2f320eaf38afeece2c821bd2356`

### 314. `hardcoded:src/components/settings/AboutSection.tsx:AboutSection:6ee73cfe9374c014:001`

- 状态：待核实
- 文件：`src/components/settings/AboutSection.tsx:212`
- 结构：`AboutSection` / `template`
- 原文/表达式：`${t("common.version")} v${displayVersion}`
- 判定原因：该英文字符串“`${t("common.version")} v${displayVersion}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6ee73cfe9374c014e7031d27aedf42379f8a5a99044b23a4cad64c2d659cc038`

### 315. `hardcoded:src/components/settings/BackupListSection.tsx:getDisplayName:152c42ca70ccdbd0:001`

- 状态：待核实
- 文件：`src/components/settings/BackupListSection.tsx:57`
- 结构：`getDisplayName` / `template`
- 原文/表达式：`${y}-${m}-${d} ${hh}:${mm}:${ss}`
- 判定原因：该英文字符串“`${y}-${m}-${d} ${hh}:${mm}:${ss}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`152c42ca70ccdbd0de3d08390b8a7b054dc4115619bcdbb6704381cd1adb6829`

### 316. `hardcoded:src/components/settings/BackupListSection.tsx:handleRestore:1f110bdd2e68492a:001`

- 状态：待核实
- 文件：`src/components/settings/BackupListSection.tsx:103`
- 结构：`handleRestore` / `template`
- 原文/表达式：`${t("settings.backupManager.safetyBackupId", { defaultValue: "Safety Backup ID" })}: ${safetyId}`
- 判定原因：该英文字符串“`${t("settings.backupManager.safetyBackupId", { defaultValue: "Safety Backup ID" })}: ${safetyId}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1f110bdd2e68492a6ce51342c9550549e1dcddf8b5ee6db3b5e13da42b1e1a20`

### 317. `hardcoded:src/components/settings/BackupStorageSection.tsx:formatBytes:229dd2efa20cfa06:001`

- 状态：待核实
- 文件：`src/components/settings/BackupStorageSection.tsx:25`
- 结构：`formatBytes` / `template`
- 原文/表达式：`${bytes} B`
- 判定原因：该英文字符串“`${bytes} B`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`229dd2efa20cfa06a18005595e089bef78a3ffc5bd33bb73dac85cca195d46c6`

### 318. `hardcoded:src/components/settings/BackupStorageSection.tsx:formatBytes:3774273e5fbf94ef:001`

- 状态：待核实
- 文件：`src/components/settings/BackupStorageSection.tsx:26`
- 结构：`formatBytes` / `template`
- 原文/表达式：`${(bytes / 1024).toFixed(1)} KB`
- 判定原因：该英文字符串“`${(bytes / 1024).toFixed(1)} KB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3774273e5fbf94ef8195350bfd3982824f82e6586e1751e20151e275c30f64df`

### 319. `hardcoded:src/components/settings/BackupStorageSection.tsx:formatBytes:388be0693bbcaae7:001`

- 状态：待核实
- 文件：`src/components/settings/BackupStorageSection.tsx:28`
- 结构：`formatBytes` / `template`
- 原文/表达式：`${(bytes / (1024 * 1024)).toFixed(1)} MB`
- 判定原因：该英文字符串“`${(bytes / (1024 * 1024)).toFixed(1)} MB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`388be0693bbcaae784829d908026071c6cf9dd99feb7674ab79943d892cab407`

### 320. `hardcoded:src/components/settings/BackupStorageSection.tsx:formatBytes:c0014229fe1b97ec:001`

- 状态：待核实
- 文件：`src/components/settings/BackupStorageSection.tsx:29`
- 结构：`formatBytes` / `template`
- 原文/表达式：`${(bytes / (1024 * 1024 * 1024)).toFixed(2)} GB`
- 判定原因：该英文字符串“`${(bytes / (1024 * 1024 * 1024)).toFixed(2)} GB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c0014229fe1b97ec6a2575c3f224d2a9273a6ae5168711a00f29b925e072aab2`

### 321. `dynamic-i18n:src/components/settings/BackupStorageSection.tsx:itemText:1db9123095e31b5b:001`

- 状态：待核实
- 文件：`src/components/settings/BackupStorageSection.tsx:42`
- 结构：`itemText` / `dynamic_i18n_key`
- 原文/表达式：`settings.backupStorage.items.${id}.${field}`
- 判定原因：翻译键由运行时表达式“`settings.backupStorage.items.${id}.${field}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1db9123095e31b5b30ec9699f3437bc8d9c7d606a90aec7540d6385f5dbc7a4b`

### 322. `dynamic-i18n:src/components/settings/LogConfigPanel.tsx:LogConfigPanel:691fd4ccfbfb6e21:001`

- 状态：待核实
- 文件：`src/components/settings/LogConfigPanel.tsx:77`
- 结构：`LogConfigPanel` / `dynamic_i18n_key`
- 原文/表达式：`settings.advanced.logConfig.levelDesc.${level}`
- 判定原因：翻译键由运行时表达式“`settings.advanced.logConfig.levelDesc.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`691fd4ccfbfb6e213cc678ea12ea362afcd31bfe554a65c2abf797e955ae447f`

### 323. `dynamic-i18n:src/components/settings/LogConfigPanel.tsx:LogConfigPanel:e46dabee057f30b0:001`

- 状态：待核实
- 文件：`src/components/settings/LogConfigPanel.tsx:96`
- 结构：`LogConfigPanel` / `dynamic_i18n_key`
- 原文/表达式：`settings.advanced.logConfig.levels.${level}`
- 判定原因：翻译键由运行时表达式“`settings.advanced.logConfig.levels.${level}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e46dabee057f30b06ec7ba0d6a7aebd30d52cc0534c78db0434225c4a053bacd`

### 324. `hardcoded:src/components/settings/SettingsPage.tsx:flashTarget:b3f59f2522edde1b:001`

- 状态：待核实
- 文件：`src/components/settings/SettingsPage.tsx:225`
- 结构：`flashTarget` / `string`
- 原文/表达式：0 0 0 2px hsl(var(--ring))
- 判定原因：该英文字符串“0 0 0 2px hsl(var(--ring))”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b3f59f2522edde1b146b72a5ab676fbfb3e49ea2d52911bf3f81c6ada2aeb645`

### 325. `dynamic-i18n:src/components/settings/SettingsPage.tsx:SettingsPage:73080ad588a22bcf:001`

- 状态：待核实
- 文件：`src/components/settings/SettingsPage.tsx:533`
- 结构：`SettingsPage` / `dynamic_i18n_key`
- 原文/表达式：`settings.sections.${section}`
- 判定原因：翻译键由运行时表达式“`settings.sections.${section}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`73080ad588a22bcf793b9900af2a25a37aa84db57382a48713b1575b878c240e`

### 326. `dynamic-i18n:src/components/settings/TerminalSettings.tsx:TerminalSelect:79a386948d425aae:001`

- 状态：待核实
- 文件：`src/components/settings/TerminalSettings.tsx:103`
- 结构：`TerminalSelect` / `dynamic_i18n_key`
- 原文/表达式：terminal.labelKey
- 判定原因：翻译键由运行时表达式“terminal.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`79a386948d425aae95f190e7a841c98ef62a40bb6210ae7f2a13d858cdb4ca6b`

### 327. `hardcoded:src/components/settings/WebdavSyncSection.tsx:currentRemotePath:d7bedb8a00ac4d6d:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:944`
- 结构：`currentRemotePath` / `template`
- 原文/表达式：`/${form.remoteRoot.trim() \|\| "cc-switch-sync"}/v2/db-v6/${form.profile.trim() \|\| "default"}`
- 判定原因：该英文字符串“`/${form.remoteRoot.trim() || "cc-switch-sync"}/v2/db-v6/${form.profile.trim() || "default"}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d7bedb8a00ac4d6d7387f81c2fabd997250bc59bee685fc11455378933b77889`

### 328. `hardcoded:src/components/settings/WebdavSyncSection.tsx:currentS3RemotePath:efa86346bc63f22d:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:945`
- 结构：`currentS3RemotePath` / `template`
- 原文/表达式：`${s3Bucket.trim() \|\| "bucket"}/${s3RemoteRoot.trim() \|\| "cc-switch-sync"}/v2/db-v6/${s3Profile.trim() \|\| "default"}`
- 判定原因：该英文字符串“`${s3Bucket.trim() || "bucket"}/${s3RemoteRoot.trim() || "cc-switch-sync"}/v2/db-v6/${s3Profile.trim() || "default"}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`efa86346bc63f22d7e182a9f5c5f670a348a5294e3c2025f84e34296b7ee63ae`

### 329. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:99f59962822de2ac:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1012`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：preset.label
- 判定原因：翻译键由运行时表达式“preset.label”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`99f59962822de2acae82fbe7ea169c844f62fda0939a56cc23ef9c0a456f1a99`

### 330. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:8387eb890b0f99fb:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1068`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：activePreset.hint
- 判定原因：翻译键由运行时表达式“activePreset.hint”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8387eb890b0f99fb9294383e5c3eba6d37367f934184fd146afb75aa4ccefab7`

### 331. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:99f59962822de2ac:002`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1240`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：preset.label
- 判定原因：翻译键由运行时表达式“preset.label”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`99f59962822de2acae82fbe7ea169c844f62fda0939a56cc23ef9c0a456f1a99`

### 332. `dynamic-i18n:src/components/settings/WebdavSyncSection.tsx:WebdavSyncSection:5dd4180e2514c9a4:001`

- 状态：待核实
- 文件：`src/components/settings/WebdavSyncSection.tsx:1251`
- 结构：`WebdavSyncSection` / `dynamic_i18n_key`
- 原文/表达式：activeS3Preset.hint
- 判定原因：翻译键由运行时表达式“activeS3Preset.hint”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`5dd4180e2514c9a49b23541f88caab22c8fc51afb084a05fd1a4e5980b699046`

### 333. `hardcoded:src/components/settings/auth/AccountQuota.tsx:ROW_CLASS:62556b1602c85b7c:001`

- 状态：待核实
- 文件：`src/components/settings/auth/AccountQuota.tsx:184`
- 结构：`ROW_CLASS` / `string`
- 原文/表达式：flex h-[18px] items-center gap-2 text-caption
- 判定原因：该英文字符串“flex h-[18px] items-center gap-2 text-caption”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`62556b1602c85b7c14259056da7edb6a57b6fa4a279e457e4fb773deab9c6beb`

### 334. `hardcoded:src/components/settings/auth/AccountQuota.tsx:QuotaRowCells:f106c106761965c2:001`

- 状态：待核实
- 文件：`src/components/settings/auth/AccountQuota.tsx:216`
- 结构：`QuotaRowCells` / `template`
- 原文/表达式：`${label}: ${value}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${label}: ${value}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f106c106761965c27cb598738bd02dcfb86c14e2eb757b1301383ce3e4de6af9`

### 335. `hardcoded:src/components/settings/auth/ManagedAccountsGroup.tsx:PILL:af87269d0dd50712:001`

- 状态：待核实
- 文件：`src/components/settings/auth/ManagedAccountsGroup.tsx:109`
- 结构：`PILL` / `string`
- 原文/表达式：inline-flex h-[18px] shrink-0 items-center rounded-full px-1.5 text-badge
- 判定原因：该英文字符串“inline-flex h-[18px] shrink-0 items-center rounded-full px-1.5 text-badge”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`af87269d0dd50712773a273d6521825b51be48b52230457a47fd8e3d50e82041`

### 336. `dynamic-i18n:src/components/settings/sections/AppConfigSection.tsx:directoryRow:1743f9d9e477bf5f:001`

- 状态：待核实
- 文件：`src/components/settings/sections/AppConfigSection.tsx:114`
- 结构：`directoryRow` / `dynamic_i18n_key`
- 原文/表达式：DIRECTORY_PLACEHOLDER[app]
- 判定原因：翻译键由运行时表达式“DIRECTORY_PLACEHOLDER[app]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`1743f9d9e477bf5fb1cf8a57c847a3f8240b314cb301099ff34aa70c583b0237`

### 337. `dynamic-i18n:src/components/settings/sections/GeneralSection.tsx:GeneralSection:4b8d2a85ad692265:001`

- 状态：待核实
- 文件：`src/components/settings/sections/GeneralSection.tsx:70`
- 结构：`GeneralSection` / `dynamic_i18n_key`
- 原文/表达式：language.labelKey
- 判定原因：翻译键由运行时表达式“language.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4b8d2a85ad692265da8e642979b40961d600061dda06d269772225e67eff2e4c`

### 338. `hardcoded:src/components/settings/sections/RoutingSection.tsx:RoutingSection:29e265bbbc49a036:001`

- 状态：待核实
- 文件：`src/components/settings/sections/RoutingSection.tsx:234`
- 结构：`RoutingSection` / `template`
- 原文/表达式：`${(status?.success_rate ?? 0).toFixed(1)}%`
- 判定原因：该英文字符串“`${(status?.success_rate ?? 0).toFixed(1)}%`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`29e265bbbc49a036019d9fff257a3f9c3aa085c4303082a8a0d856db2dc1dd11`

### 339. `dynamic-i18n:src/components/settings/sections/RoutingSection.tsx:RoutingSection:8594999185d253ca:001`

- 状态：待核实
- 文件：`src/components/settings/sections/RoutingSection.tsx:402`
- 结构：`RoutingSection` / `dynamic_i18n_key`
- 原文/表达式：`mode.names.${mode}`
- 判定原因：翻译键由运行时表达式“`mode.names.${mode}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8594999185d253cac67012cdf03429a7ec6a6ed8cb4300166ad5416582da216c`

### 340. `hardcoded:src/components/shell/Sidebar.tsx:tip:8cc90a1e7ba29384:001`

- 状态：待核实
- 文件：`src/components/shell/Sidebar.tsx:433`
- 结构：`tip` / `template`
- 原文/表达式：`${name} · ${t("nav.needsAttention")}`
- 判定原因：该英文字符串“`${name} · ${t("nav.needsAttention")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8cc90a1e7ba29384e9d637f838f10bb47f8b7d5eec3f49163e027d0e918ed6f8`

### 341. `hardcoded:src/components/shell/Sidebar.tsx:tip:8c483261e408f811:001`

- 状态：待核实
- 文件：`src/components/shell/Sidebar.tsx:435`
- 结构：`tip` / `template`
- 原文/表达式：`${name} · ${modeName}`
- 判定原因：该英文字符串“`${name} · ${modeName}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8c483261e408f811946bbdc0b5bec75b49ac20e4cdd560a29747f4dc99f1aca4`

### 342. `dynamic-i18n:src/components/shell/Sidebar.tsx:SettingsDirectory:73080ad588a22bcf:001`

- 状态：待核实
- 文件：`src/components/shell/Sidebar.tsx:754`
- 结构：`SettingsDirectory` / `dynamic_i18n_key`
- 原文/表达式：`settings.sections.${section}`
- 判定原因：翻译键由运行时表达式“`settings.sections.${section}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`73080ad588a22bcf793b9900af2a25a37aa84db57382a48713b1575b878c240e`

### 343. `hardcoded:src/components/skills/SkillsPage.tsx:POPOVER_CLASS:b35351a6c3186104:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsPage.tsx:62`
- 结构：`POPOVER_CLASS` / `string`
- 原文/表达式：z-[110] rounded-panel border border-border bg-surface p-1 text-fg-1 shadow-v7-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=top]:slide-in-from-bottom-2
- 判定原因：该英文字符串“z-[110] rounded-panel border border-border bg-surface p-1 text-fg-1 shadow-v7-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=top]:slide-in-from-bottom-2”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b35351a6c3186104ee70b126b0732146d13d881badaa4982720be5c78fa1e932`

### 344. `hardcoded:src/components/skills/SkillsPage.tsx:installedKey:ba2a4878993628e8:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsPage.tsx:140`
- 结构：`installedKey` / `template`
- 原文/表达式：`${dir}:${(owner ?? "").toLowerCase()}:${(name ?? "").toLowerCase()}`
- 判定原因：该英文字符串“`${dir}:${(owner ?? "").toLowerCase()}:${(name ?? "").toLowerCase()}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ba2a4878993628e807782ef3b80058c44ef619e74df4cb72d79e64d8590f979b`

### 345. `hardcoded:src/components/skills/SkillsPage.tsx:SkillsPage:75cc974621739e45:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsPage.tsx:730`
- 结构：`SkillsPage` / `template`
- 原文/表达式：`skills.sh · ${repo}`
- 判定原因：该英文字符串“`skills.sh · ${repo}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`75cc974621739e45e1cda480df9857ef31bda47d688c4c5c9dc407e7fecfdd8d`

### 346. `hardcoded:src/components/skills/SkillsStorageSheet.tsx:RADIO_LABEL_CLASS:28d833901922662e:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsStorageSheet.tsx:56`
- 结构：`RADIO_LABEL_CLASS` / `string`
- 原文/表达式：flex cursor-pointer items-center gap-2.5 text-body text-fg-1 has-[:disabled]:cursor-not-allowed has-[:disabled]:opacity-60
- 判定原因：该英文字符串“flex cursor-pointer items-center gap-2.5 text-body text-fg-1 has-[:disabled]:cursor-not-allowed has-[:disabled]:opacity-60”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`28d833901922662ef0be9cba0276aeca413416dd1f6d76b81e3f9bb142c18e6d`

### 347. `hardcoded:src/components/skills/SkillsStorageSheet.tsx:details:6085e88121d3f034:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsStorageSheet.tsx:158`
- 结构：`details` / `template`
- 原文/表达式：`${appName(outcome.app)}: ${outcome.error}`
- 判定原因：该英文字符串“`${appName(outcome.app)}: ${outcome.error}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6085e88121d3f03488fa26c1c35912826d8495e15504d92ebbd3dd711044827e`

### 348. `hardcoded:src/components/skills/SkillsStorageSheet.tsx:details:156af28af687edc8:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsStorageSheet.tsx:161`
- 结构：`details` / `template`
- 原文/表达式：`${appName(outcome.app)} · ${t(<br>                "skills.storageSheet.resyncSkillItem",<br>                { directory: skill.directory, error: skill.error },<br>              )}`
- 判定原因：该英文字符串“`${appName(outcome.app)} · ${t(
                "skills.storageSheet.resyncSkillItem",
                { directory: skill.directory, error: skill.error },
              )}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`156af28af687edc84bbf4fceb758634628a88eb41391860f313cf08fa9341dd7`

### 349. `dynamic-i18n:src/components/skills/SkillsStorageSheet.tsx:SkillsStorageSheet:0c9f9f16eb7882e5:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsStorageSheet.tsx:306`
- 结构：`SkillsStorageSheet` / `dynamic_i18n_key`
- 原文/表达式：option.labelKey
- 判定原因：翻译键由运行时表达式“option.labelKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0c9f9f16eb7882e54ef00841c2a810356cde523b3b567ad568f426ada1cf34f4`

### 350. `dynamic-i18n:src/components/skills/SkillsStorageSheet.tsx:SkillsStorageSheet:36befa74dfbcc58f:001`

- 状态：待核实
- 文件：`src/components/skills/SkillsStorageSheet.tsx:309`
- 结构：`SkillsStorageSheet` / `dynamic_i18n_key`
- 原文/表达式：option.descKey
- 判定原因：翻译键由运行时表达式“option.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`36befa74dfbcc58f25411157c9597ba984e7e2d0a0815ac516fadfe3689ab2b7`

### 351. `hardcoded:src/components/skills/UnifiedSkillsPanel.tsx:filteredSkills:0c4237f14c86fc54:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:316`
- 结构：`filteredSkills` / `string`
- 原文/表达式：app:
- 判定原因：该英文字符串“app:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0c4237f14c86fc5448cfb2c04917831dd61fb0365d1b1c5542aa631626fba02c`

### 352. `dynamic-i18n:src/components/skills/UnifiedSkillsPanel.tsx:text:dc4eb9bbc03ce6c2:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:458`
- 结构：`text` / `dynamic_i18n_key`
- 原文/表达式：enabled ? toastKey.on : toastKey.off
- 判定原因：翻译键由运行时表达式“enabled ? toastKey.on : toastKey.off”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`dc4eb9bbc03ce6c2f1f6d09396558b5864c5f98fedaa2cb3471f608770e9cb02`

### 353. `hardcoded:src/components/skills/UnifiedSkillsPanel.tsx:uninstallIds:762c11e5b60e3e2c:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:555`
- 结构：`uninstallIds` / `template`
- 原文/表达式：`${skill?.name ?? id}: ${String(error)}`
- 判定原因：该英文字符串“`${skill?.name ?? id}: ${String(error)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`762c11e5b60e3e2cc397567cbc4e9e5ab9ccc8e1c84b4a945e30746bc733ca78`

### 354. `hardcoded:src/components/skills/UnifiedSkillsPanel.tsx:updateIds:2278c54c92be3a89:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:600`
- 结构：`updateIds` / `template`
- 原文/表达式：`${name ?? id}: ${String(error)}`
- 判定原因：该英文字符串“`${name ?? id}: ${String(error)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2278c54c92be3a8963fafe3e8ac87c5aba31e884b46b5ca5f4cbb812540acd21`

### 355. `hardcoded:src/components/skills/UnifiedSkillsPanel.tsx:statusLabel:0c4237f14c86fc54:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:1061`
- 结构：`statusLabel` / `string`
- 原文/表达式：app:
- 判定原因：该英文字符串“app:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0c4237f14c86fc5448cfb2c04917831dd61fb0365d1b1c5542aa631626fba02c`

### 356. `dynamic-i18n:src/components/skills/UnifiedSkillsPanel.tsx:InstalledRow:947324ed6a00ba24:001`

- 状态：待核实
- 文件：`src/components/skills/UnifiedSkillsPanel.tsx:1929`
- 结构：`InstalledRow` / `dynamic_i18n_key`
- 原文/表达式：`appMatrix.cell.${state}`
- 判定原因：翻译键由运行时表达式“`appMatrix.cell.${state}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`947324ed6a00ba241dcc93e16c9b7022385f2e299608f805663901480e1d6454`

### 357. `hardcoded:src/components/ui/alert.tsx:alertVariants:32238c0c8f8360c5:001`

- 状态：待核实
- 文件：`src/components/ui/alert.tsx:7`
- 结构：`alertVariants` / `string`
- 原文/表达式：relative w-full rounded-lg border px-4 py-3 text-sm [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-fg-1 [&>svg~*]:pl-7
- 判定原因：该英文字符串“relative w-full rounded-lg border px-4 py-3 text-sm [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-fg-1 [&>svg~*]:pl-7”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`32238c0c8f8360c5a6d711b155575f9c7f67ccd054fd197791f8d202fa4d53af`

### 358. `hardcoded:src/components/ui/alert.tsx:alertVariants:9bda9129fb7e467a:001`

- 状态：待核实
- 文件：`src/components/ui/alert.tsx:13`
- 结构：`alertVariants` / `string`
- 原文/表达式：border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive
- 判定原因：该英文字符串“border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9bda9129fb7e467aa77eab57eff76a038de399c1829e4902f60fc84d23319f39`

### 359. `hardcoded:src/components/ui/button.tsx:buttonVariants:bfdc6974e9db8551:001`

- 状态：待核实
- 文件：`src/components/ui/button.tsx:44`
- 结构：`buttonVariants` / `string`
- 原文/表达式：h-8 px-3.5 transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100
- 判定原因：该英文字符串“h-8 px-3.5 transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`bfdc6974e9db8551cbe3df0c82b9f017ac6c3b39c5a48df08a947712917c85b5`

### 360. `hardcoded:src/components/ui/button.tsx:buttonVariants:24f220a92a07a1e8:001`

- 状态：待核实
- 文件：`src/components/ui/button.tsx:45`
- 结构：`buttonVariants` / `string`
- 原文/表达式：h-7 px-3 transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100
- 判定原因：该英文字符串“h-7 px-3 transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`24f220a92a07a1e8609f77c6052640e298841ea3258d712008c79de3fe5ff24f`

### 361. `hardcoded:src/components/ui/button.tsx:buttonVariants:6fcba1d07e3bfd28:001`

- 状态：待核实
- 文件：`src/components/ui/button.tsx:46`
- 结构：`buttonVariants` / `string`
- 原文/表达式：h-9 px-4 transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100
- 判定原因：该英文字符串“h-9 px-4 transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6fcba1d07e3bfd28ad83f84361f01aaf97802099fc5aab31ad945e385970ccb8`

### 362. `hardcoded:src/components/ui/button.tsx:buttonVariants:8844441cae94b24d:001`

- 状态：待核实
- 文件：`src/components/ui/button.tsx:47`
- 结构：`buttonVariants` / `string`
- 原文/表达式：h-8 w-8 p-0 transition-[background-color,color,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100
- 判定原因：该英文字符串“h-8 w-8 p-0 transition-[background-color,color,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8844441cae94b24d929aac454fe5f00be1d5dffea1628f4e0ad9b4e51c0aec35`

### 363. `hardcoded:src/components/ui/button.tsx:buttonVariants:0ac0083c15956191:001`

- 状态：待核实
- 文件：`src/components/ui/button.tsx:51`
- 结构：`buttonVariants` / `string`
- 原文/表达式：h-7 rounded-control px-3 text-body font-medium transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100
- 判定原因：该英文字符串“h-7 rounded-control px-3 text-body font-medium transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0ac0083c15956191afa8ae2d180c04c1c9dd24512276bde7f5ba372a964eb30d`

### 364. `hardcoded:src/components/ui/button.tsx:buttonVariants:238154aab83f59c5:001`

- 状态：待核实
- 文件：`src/components/ui/button.tsx:53`
- 结构：`buttonVariants` / `string`
- 原文/表达式：h-8 rounded-control px-3.5 text-body font-medium transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100
- 判定原因：该英文字符串“h-8 rounded-control px-3.5 text-body font-medium transition-[background-color,filter,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`238154aab83f59c595c2e34c10efe35085f16957d27e7542fd8dead49d035cf7`

### 365. `hardcoded:src/components/ui/button.tsx:buttonVariants:cd79be55fb86e3dd:001`

- 状态：待核实
- 文件：`src/components/ui/button.tsx:55`
- 结构：`buttonVariants` / `string`
- 原文/表达式：h-7 w-7 rounded-control p-0 text-fg-2 hover:text-fg-1 transition-[background-color,color,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100
- 判定原因：该英文字符串“h-7 w-7 rounded-control p-0 text-fg-2 hover:text-fg-1 transition-[background-color,color,scale] active:scale-[0.96] [&[aria-haspopup]]:active:scale-100”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`cd79be55fb86e3dd34b69a2fc7f17d73d61003c0e14580b0801b0c0cb2d08c16`

### 366. `hardcoded:src/components/ui/form.tsx:useFormField:b188163e7d8c7b51:001`

- 状态：待核实
- 文件：`src/components/ui/form.tsx:48`
- 结构：`useFormField` / `string`
- 原文/表达式：useFormField should be used within <FormField>
- 判定原因：该英文字符串“useFormField should be used within <FormField>”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b188163e7d8c7b51f1c63d617b916933551d1413a50321827289a1e9d2cb4a1c`

### 367. `hardcoded:src/components/ui/form.tsx:FormControl:21c2e2787be6da34:001`

- 状态：待核实
- 文件：`src/components/ui/form.tsx:108`
- 结构：`FormControl` / `template`
- 原文/表达式：`${formDescriptionId} ${formMessageId}`
- 判定原因：该英文字符串“`${formDescriptionId} ${formMessageId}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`21c2e2787be6da34f7c8a1083d72bed51655a0728b1974abf209a3cc40cd8f9c`

### 368. `hardcoded:src/components/ui/input.tsx:fieldClass:d46d0a8729156a34:001`

- 状态：待核实
- 文件：`src/components/ui/input.tsx:9`
- 结构：`fieldClass` / `string`
- 原文/表达式：w-full rounded-control border border-border-strong bg-surface px-2.5 text-body text-fg-1 transition-[border-color,box-shadow] placeholder:text-fg-3 focus:border-ring focus:outline-none focus:ring-[3px] focus:ring-ring/20 dark:focus:ring-ring/15 focus-visible:outline-none aria-[invalid=true]:border-danger disabled:cursor-not-allowed disabled:opacity-50
- 判定原因：该英文字符串“w-full rounded-control border border-border-strong bg-surface px-2.5 text-body text-fg-1 transition-[border-color,box-shadow] placeholder:text-fg-3 focus:border-ring focus:outline-none focus:ring-[3px] focus:ring-ring/20 dark:focus:ring-ring/15 focus-visible:outline-none aria-[invalid=true]:border-danger disabled:cursor-not-allowed disabled:opacity-50”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d46d0a8729156a3481c59a7f9d17748b0dbbb2aff7079e73b902be27e2af9c3a`

### 369. `hardcoded:src/components/ui/sliding-indicator.tsx:MOTION:dbb755b646cec532:001`

- 状态：待核实
- 文件：`src/components/ui/sliding-indicator.tsx:67`
- 结构：`MOTION` / `string`
- 原文/表达式：transition-[transform,width,height] duration-200 ease-out motion-reduce:transition-none
- 判定原因：该英文字符串“transition-[transform,width,height] duration-200 ease-out motion-reduce:transition-none”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`dbb755b646cec532cb01eae3acb4be1063c9588fc6de1e0aaada664ecdaabe6b`

### 370. `hardcoded:src/components/ui/sliding-indicator.tsx:THUMB_MOTION:5cb6665c68c37fc8:001`

- 状态：待核实
- 文件：`src/components/ui/sliding-indicator.tsx:71`
- 结构：`THUMB_MOTION` / `string`
- 原文/表达式：transition-[left,top,width,height] duration-200 ease-out motion-reduce:transition-none
- 判定原因：该英文字符串“transition-[left,top,width,height] duration-200 ease-out motion-reduce:transition-none”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5cb6665c68c37fc8c1cf59a5e3396870c239ccdf935dc50c98e04393836260ad`

### 371. `hardcoded:src/components/universal/UniversalProviderFormModal.tsx:codexBaseUrl:eeb319d869b51907:001`

- 状态：待核实
- 文件：`src/components/universal/UniversalProviderFormModal.tsx:156`
- 结构：`codexBaseUrl` / `template`
- 原文/表达式：`${baseUrl.replace(/\/+$/, "")}/v1`
- 判定原因：该英文字符串“`${baseUrl.replace(/\/+$/, "")}/v1`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`eeb319d869b51907d0010394d8ac3aea68c176679902692f6071dbfffd00b79b`

### 372. `hardcoded:src/components/universal/UniversalProviderFormModal.tsx:configToml:fb9c4d37398e05bc:001`

- 状态：待核实
- 文件：`src/components/universal/UniversalProviderFormModal.tsx:157`
- 结构：`configToml` / `template`
- 原文/表达式：`model_provider = "custom"<br>model = "${model}"<br>model_reasoning_effort = "${reasoningEffort}"<br>disable_response_storage = true<br><br>[model_providers.custom]<br>name = "NewAPI"<br>base_url = "${codexBaseUrl}"<br>wire_api = "responses"<br>requires_openai_auth = true`
- 判定原因：该英文字符串“`model_provider = "custom"
model = "${model}"
model_reasoning_effort = "${reasoningEffort}"
disable_response_storage = true

[model_providers.custom]
name = "NewAPI"
base_url = "${codexBaseUrl}"
wire_api = "responses"
requires_openai_auth = true`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fb9c4d37398e05bce58a239fec1e6a8b9c221bca26d9fa336b7c49c58416a6aa`

### 373. `hardcoded:src/components/universal/UniversalProviderFormModal.tsx:UniversalProviderFormModal:6946d3ffe03d648c:001`

- 状态：待核实
- 文件：`src/components/universal/UniversalProviderFormModal.tsx:432`
- 结构：`UniversalProviderFormModal` / `string`
- 原文/表达式：sk-...
- 控件属性：`placeholder`
- 判定原因：该英文字符串“sk-...”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6946d3ffe03d648cf11d876d5bac1994f673af8cb2beb50a4ca4f53b0f82f704`

### 374. `hardcoded:src/components/universal/UniversalProviderPanel.tsx:duplicated:efdc2dc862a451d8:001`

- 状态：待核实
- 文件：`src/components/universal/UniversalProviderPanel.tsx:175`
- 结构：`duplicated` / `template`
- 原文/表达式：`${provider.name} copy`
- 判定原因：该英文字符串“`${provider.name} copy`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`efdc2dc862a451d8d0191b12d29172b2e68bd1e019e3e245497774d15e58971e`

### 375. `hardcoded:src/components/usage/ChecklistMenu.tsx:ChecklistMenu:51382d6aeb80329e:001`

- 状态：待核实
- 文件：`src/components/usage/ChecklistMenu.tsx:68`
- 结构：`ChecklistMenu` / `template`
- 原文/表达式：`${label}: ${summary}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${label}: ${summary}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`51382d6aeb80329e12cbc6ce3aa85df5cd0a06d57250653acbd86149e9ad0827`

### 376. `hardcoded:src/components/usage/ModelStatsTable.tsx:ModelStatsTable:8a7d061463007731:001`

- 状态：待核实
- 文件：`src/components/usage/ModelStatsTable.tsx:110`
- 结构：`ModelStatsTable` / `template`
- 原文/表达式：`${moneyTitle(stat.totalCost, 6)} · ${t("usage.avgCost")} ${money(stat.avgCostPerRequest, 4)}`
- 控件属性：`title`
- 判定原因：该英文字符串“`${moneyTitle(stat.totalCost, 6)} · ${t("usage.avgCost")} ${money(stat.avgCostPerRequest, 4)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8a7d061463007731205af44903fb96babe7a925f1ca5b745817608921c16a81a`

### 377. `hardcoded:src/components/usage/ModelsDevAutoSyncPanel.tsx:AutoSyncDialog:2be9d28f282c8f61:001`

- 状态：待核实
- 文件：`src/components/usage/ModelsDevAutoSyncPanel.tsx:259`
- 结构：`AutoSyncDialog` / `template`
- 原文/表达式：`${t("usage.modelsDevLoadError")}: ${String(error)}`
- 控件属性：`title`
- 判定原因：该英文字符串“`${t("usage.modelsDevLoadError")}: ${String(error)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2be9d28f282c8f6167e379fe876564b728e26d760159eb0698d7c005d588aeb1`

### 378. `hardcoded:src/components/usage/ModelsDevAutoSyncPanel.tsx:ModelsDevAutoSyncPanel:61cb4d60101029a3:001`

- 状态：待核实
- 文件：`src/components/usage/ModelsDevAutoSyncPanel.tsx:610`
- 结构：`ModelsDevAutoSyncPanel` / `template`
- 原文/表达式：`${lastSync} · ${t("usage.pricing.commonIncluded")}`
- 判定原因：该英文字符串“`${lastSync} · ${t("usage.pricing.commonIncluded")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`61cb4d60101029a38c3ae0adaf25dc7e80f3cbaf2bf65fb2c0698aed069a2c69`

### 379. `hardcoded:src/components/usage/ModelsDevPickerDialog.tsx:ModelsDevPickerDialog:720d1cbcde680fdf:001`

- 状态：待核实
- 文件：`src/components/usage/ModelsDevPickerDialog.tsx:191`
- 结构：`ModelsDevPickerDialog` / `template`
- 原文/表达式：`${t("usage.modelsDevLoadError", "加载 models.dev 数据失败")}: ${<br>                error instanceof Error ? error.message : String(error)<br>              }`
- 控件属性：`title`
- 判定原因：该中文自然语言“`${t("usage.modelsDevLoadError", "加载 models.dev 数据失败")}: ${
                error instanceof Error ? error.message : String(error)
              }`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`720d1cbcde680fdfde4b27326b48b67fd2d1c85f41eb603126a0ba626cddfdb0`

### 380. `hardcoded:src/components/usage/PricingConfigPanel.tsx:formatUnitPrice:5bb5e46c6a0e6279:001`

- 状态：待核实
- 文件：`src/components/usage/PricingConfigPanel.tsx:69`
- 结构：`formatUnitPrice` / `template`
- 原文/表达式：`$${whole}.${frac.padEnd(2, "0")}`
- 判定原因：该英文字符串“`$${whole}.${frac.padEnd(2, "0")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5bb5e46c6a0e6279f8ad1b3d36957581284501a117f8497ca81235c84448b322`

### 381. `hardcoded:src/components/usage/PricingConfigPanel.tsx:BillingDefaultsDialog:1005be4f8336d7e2:001`

- 状态：待核实
- 文件：`src/components/usage/PricingConfigPanel.tsx:200`
- 结构：`BillingDefaultsDialog` / `template`
- 原文/表达式：`${APP_DISPLAY_NAME[app]} · ${t("settings.globalProxy.pricingModelSourceLabel")}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${APP_DISPLAY_NAME[app]} · ${t("settings.globalProxy.pricingModelSourceLabel")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1005be4f8336d7e26b7417c04703375bcf35fbd57be49c31537bf5e4dc4cc2b2`

### 382. `hardcoded:src/components/usage/PricingConfigPanel.tsx:summary:43d0b108901a059b:001`

- 状态：待核实
- 文件：`src/components/usage/PricingConfigPanel.tsx:260`
- 结构：`summary` / `template`
- 原文/表达式：`${<br>          group.source === "response"<br>            ? t("usage.pricing.byResponse")<br>            : t("usage.pricing.byRequest")<br>        } · ${joinNames(group.apps, lang)}`
- 判定原因：该英文字符串“`${
          group.source === "response"
            ? t("usage.pricing.byResponse")
            : t("usage.pricing.byRequest")
        } · ${joinNames(group.apps, lang)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`43d0b108901a059bce9908c5b08a3d27f0204793333d1384cbd73fad17846000`

### 383. `hardcoded:src/components/usage/PricingConfigPanel.tsx:PricingConfigPanel:c60333b79b79c4de:001`

- 状态：待核实
- 文件：`src/components/usage/PricingConfigPanel.tsx:378`
- 结构：`PricingConfigPanel` / `template`
- 原文/表达式：`${t("usage.loadPricingError")}: ${String(error)}`
- 控件属性：`title`
- 判定原因：该英文字符串“`${t("usage.loadPricingError")}: ${String(error)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c60333b79b79c4ded3ba331a1134c444a0f728fd9fc1c5cae2ac197b9a2e5e62`

### 384. `hardcoded:src/components/usage/PricingEditModal.tsx:PricingEditModal:4a0c01b3edb39b34:001`

- 状态：待核实
- 文件：`src/components/usage/PricingEditModal.tsx:96`
- 结构：`PricingEditModal` / `template`
- 原文/表达式：`${t("usage.editPricing", "编辑定价")} - ${model.modelId}`
- 控件属性：`title`
- 判定原因：该中文自然语言“`${t("usage.editPricing", "编辑定价")} - ${model.modelId}`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`4a0c01b3edb39b344cdaefcebf59eae05c148c7835159b60ba46665416d1904f`

### 385. `hardcoded:src/components/usage/RequestDetailPanel.tsx:tokens:395f808a0ae35649:001`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:164`
- 结构：`tokens` / `template`
- 原文/表达式：`${fmtInt(freshInput, locale)} (${t("usage.rawInputLabel")}: ${fmtInt(request.inputTokens, locale)})`
- 判定原因：该英文字符串“`${fmtInt(freshInput, locale)} (${t("usage.rawInputLabel")}: ${fmtInt(request.inputTokens, locale)})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`395f808a0ae356498cc6b61ac8e288e980f176e0f9e6a37a275b13da2d3ec147`

### 386. `hardcoded:src/components/usage/RequestDetailPanel.tsx:useDetailSections:fd9f9af498da40a5:001`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:217`
- 结构：`useDetailSections` / `template`
- 原文/表达式：`${t("usage.detail.total")} (${t("usage.withMultiplier")})`
- 判定原因：该英文字符串“`${t("usage.detail.total")} (${t("usage.withMultiplier")})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fd9f9af498da40a590e5ebedf21b5edcbf811b02d7e2c368925859b4fc1fbc00`

### 387. `hardcoded:src/components/usage/RequestDetailPanel.tsx:useDetailSections:91f6f29954d1fd4d:001`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:257`
- 结构：`useDetailSections` / `template`
- 原文/表达式：`${(latency / 1000).toFixed(1)}s`
- 判定原因：该英文字符串“`${(latency / 1000).toFixed(1)}s`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`91f6f29954d1fd4d940c973610605d2f17284f9462e3ebf1a540864c5cb4abb7`

### 388. `hardcoded:src/components/usage/RequestDetailPanel.tsx:useDetailSections:83701575d787c29f:001`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:258`
- 结构：`useDetailSections` / `template`
- 原文/表达式：`${fmtInt(latency, locale)} ms`
- 判定原因：该英文字符串“`${fmtInt(latency, locale)} ms`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`83701575d787c29f04e235dbdfc18c231d8d07750495b88087373dd4aa966b0d`

### 389. `hardcoded:src/components/usage/RequestDetailPanel.tsx:useDetailSections:40c2b1dbf3ff18e6:001`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:266`
- 结构：`useDetailSections` / `template`
- 原文/表达式：`${(firstToken / 1000).toFixed(1)}s`
- 判定原因：该英文字符串“`${(firstToken / 1000).toFixed(1)}s`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`40c2b1dbf3ff18e6e9384d5ae9cafe817280274e9d2715586e54105d1dee9b6b`

### 390. `hardcoded:src/components/usage/RequestDetailPanel.tsx:useDetailSections:40c2b1dbf3ff18e6:002`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:303`
- 结构：`useDetailSections` / `template`
- 原文/表达式：`${(firstToken / 1000).toFixed(1)}s`
- 判定原因：该英文字符串“`${(firstToken / 1000).toFixed(1)}s`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`40c2b1dbf3ff18e6e9384d5ae9cafe817280274e9d2715586e54105d1dee9b6b`

### 391. `hardcoded:src/components/usage/RequestDetailPanel.tsx:useDetailSections:91f6f29954d1fd4d:002`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:310`
- 结构：`useDetailSections` / `template`
- 原文/表达式：`${(latency / 1000).toFixed(1)}s`
- 判定原因：该英文字符串“`${(latency / 1000).toFixed(1)}s`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`91f6f29954d1fd4d940c973610605d2f17284f9462e3ebf1a540864c5cb4abb7`

### 392. `hardcoded:src/components/usage/RequestDetailPanel.tsx:useDetailSections:83701575d787c29f:002`

- 状态：待核实
- 文件：`src/components/usage/RequestDetailPanel.tsx:311`
- 结构：`useDetailSections` / `template`
- 原文/表达式：`${fmtInt(latency, locale)} ms`
- 判定原因：该英文字符串“`${fmtInt(latency, locale)} ms`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`83701575d787c29f04e235dbdfc18c231d8d07750495b88087373dd4aa966b0d`

### 393. `dynamic-i18n:src/components/usage/RequestLogColumnsMenu.tsx:RequestLogColumnsMenu:4c6b716150f3dad4:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogColumnsMenu.tsx:59`
- 结构：`RequestLogColumnsMenu` / `dynamic_i18n_key`
- 原文/表达式：REQUEST_LOG_COLUMN_LABEL_KEYS[id]
- 判定原因：翻译键由运行时表达式“REQUEST_LOG_COLUMN_LABEL_KEYS[id]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4c6b716150f3dad49920b06ba95bb0f52bc634dcdf0f07106200b1cdae9a6d38`

### 394. `hardcoded:src/components/usage/RequestLogTable.tsx:formatLogTime:2e11b75fd2a6490c:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:88`
- 结构：`formatLogTime` / `template`
- 原文/表达式：`${pad2(date.getMonth() + 1)}-${pad2(date.getDate())} ${clock}`
- 判定原因：该英文字符串“`${pad2(date.getMonth() + 1)}-${pad2(date.getDate())} ${clock}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`2e11b75fd2a6490c8d5a2bb5b898301fc0e435e0922f4f0774b2e5d93d06a43e`

### 395. `hardcoded:src/components/usage/RequestLogTable.tsx:formatLogFullTime:48307ba69a16a608:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:94`
- 结构：`formatLogFullTime` / `template`
- 原文/表达式：`${date.getFullYear()}-${pad2(date.getMonth() + 1)}-${pad2(<br>    date.getDate(),<br>  )} ${pad2(date.getHours())}:${pad2(date.getMinutes())}:${pad2(<br>    date.getSeconds(),<br>  )}`
- 判定原因：该英文字符串“`${date.getFullYear()}-${pad2(date.getMonth() + 1)}-${pad2(
    date.getDate(),
  )} ${pad2(date.getHours())}:${pad2(date.getMinutes())}:${pad2(
    date.getSeconds(),
  )}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`48307ba69a16a6087bb8c1f301250d144a50866abc903c3266a819dc39f6a5db`

### 396. `hardcoded:src/components/usage/RequestLogTable.tsx:formatHitPercent:e6c2bb7838daaccd:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:155`
- 结构：`formatHitPercent` / `template`
- 原文/表达式：`${(Math.floor(percent * 10) / 10).toFixed(1)}%`
- 判定原因：该英文字符串“`${(Math.floor(percent * 10) / 10).toFixed(1)}%`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e6c2bb7838daaccddfd737c495df07098d0e60bbe87b2679383e17b4c17e50ea`

### 397. `hardcoded:src/components/usage/RequestLogTable.tsx:keep:e62d9358bc6d42e1:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:283`
- 结构：`keep` / `template`
- 原文/表达式：`, ${own}`
- 判定原因：该英文字符串“`, ${own}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e62d9358bc6d42e165048a5d110e1634b47b6d4a44a19ba6cfc2d1b7acede24f`

### 398. `hardcoded:src/components/usage/RequestLogTable.tsx:RequestLogTable:e4276c3a92725002:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:286`
- 结构：`RequestLogTable` / `template`
- 原文/表达式：`inset 0 0 0 100vmax ${highlight}${keep}`
- 判定原因：该英文字符串“`inset 0 0 0 100vmax ${highlight}${keep}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e4276c3a92725002339b80b6b4f57accfee1b1f6f55ce6dbaca0dc24d229053d`

### 399. `hardcoded:src/components/usage/RequestLogTable.tsx:RequestLogTable:f395ad305248a9de:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:287`
- 结构：`RequestLogTable` / `template`
- 原文/表达式：`inset 0 0 0 100vmax transparent${keep}`
- 判定原因：该英文字符串“`inset 0 0 0 100vmax transparent${keep}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f395ad305248a9de831d8225bf862bbb3f4cfdd5c66d95b195668f891b8949e6`

### 400. `hardcoded:src/components/usage/RequestLogTable.tsx:RequestLogTable:34a29e3c8b32e81a:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:309`
- 结构：`RequestLogTable` / `template`
- 原文/表达式：`translateY(${(from - index) * 100}%)`
- 判定原因：该英文字符串“`translateY(${(from - index) * 100}%)`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`34a29e3c8b32e81af7cd50a996fd679369a605c8c071343315eb826fe8063349`

### 401. `hardcoded:src/components/usage/RequestLogTable.tsx:RequestLogTable:7e5b5efabcadf337:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:312`
- 结构：`RequestLogTable` / `string`
- 原文/表达式：cubic-bezier(0.2, 0, 0, 1)
- 判定原因：该英文字符串“cubic-bezier(0.2, 0, 0, 1)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7e5b5efabcadf33752740db0db30c35155426df370322b475716b13b44d015b5`

### 402. `dynamic-i18n:src/components/usage/RequestLogTable.tsx:label:4c6b716150f3dad4:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:354`
- 结构：`label` / `dynamic_i18n_key`
- 原文/表达式：REQUEST_LOG_COLUMN_LABEL_KEYS[id]
- 判定原因：翻译键由运行时表达式“REQUEST_LOG_COLUMN_LABEL_KEYS[id]”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`4c6b716150f3dad49920b06ba95bb0f52bc634dcdf0f07106200b1cdae9a6d38`

### 403. `hardcoded:src/components/usage/RequestLogTable.tsx:modelTitle:4c0642344d4e2dfb:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:409`
- 结构：`modelTitle` / `template`
- 原文/表达式：`${log.requestModel} → ${log.model}`
- 判定原因：该英文字符串“`${log.requestModel} → ${log.model}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4c0642344d4e2dfb327344f4a906def9c78fb32f53eba907efb3575c560c45dd`

### 404. `hardcoded:src/components/usage/RequestLogTable.tsx:cells:56de1109b9681a57:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:482`
- 结构：`cells` / `template`
- 原文/表达式：`${fmtInt(freshInput, locale)} (${t("usage.rawInputLabel")}: ${fmtInt(log.inputTokens, locale)})`
- 控件属性：`title`
- 判定原因：该英文字符串“`${fmtInt(freshInput, locale)} (${t("usage.rawInputLabel")}: ${fmtInt(log.inputTokens, locale)})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`56de1109b9681a57ddd5a8e95a3727a4f0c56948bdff2acb04459bb1193ec97a`

### 405. `hardcoded:src/components/usage/RequestLogTable.tsx:cells:c977ca4b41b28224:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:549`
- 结构：`cells` / `template`
- 原文/表达式：`${t("usage.costMultiplier")} ×${multiplier.toFixed(2)}`
- 控件属性：`title`
- 判定原因：该英文字符串“`${t("usage.costMultiplier")} ×${multiplier.toFixed(2)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c977ca4b41b28224bf957e50e6308cce91c076f46ee1c6d4f5d5be5ac95bb353`

### 406. `hardcoded:src/components/usage/RequestLogTable.tsx:cells:1937e128a2aa541e:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:595`
- 结构：`cells` / `template`
- 原文/表达式：`${isSession ? "≈" : ""}${fmtInt(latency, locale)} ms`
- 控件属性：`title`
- 判定原因：该英文字符串“`${isSession ? "≈" : ""}${fmtInt(latency, locale)} ms`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1937e128a2aa541e6bfa501910e61b90d8599a32bc611996b69e484d86b8b0e5`

### 407. `hardcoded:src/components/usage/RequestLogTable.tsx:cells:08cc71e15555e2f6:001`

- 状态：待核实
- 文件：`src/components/usage/RequestLogTable.tsx:598`
- 结构：`cells` / `template`
- 原文/表达式：`${isSession ? "≈" : ""}${timing.duration}s`
- 判定原因：该英文字符串“`${isSession ? "≈" : ""}${timing.duration}s`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`08cc71e15555e2f6ba6ba49bbc7cd42f2441cc4b3a63e4d62a85f8b9bcad2dee`

### 408. `hardcoded:src/components/usage/UsageDashboard.tsx:menuContentClass:4b584ccc0509b919:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:137`
- 结构：`menuContentClass` / `string`
- 原文/表达式：min-w-[200px] max-w-[320px] rounded-panel border-border bg-surface p-1 shadow-v7-md
- 判定原因：该英文字符串“min-w-[200px] max-w-[320px] rounded-panel border-border bg-surface p-1 shadow-v7-md”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4b584ccc0509b919d7a5c65964ddb3e5bbc53a687aedcf4ac1b23a644b4897eb`

### 409. `hardcoded:src/components/usage/UsageDashboard.tsx:menuItemClass:e3394c35b6be4a65:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:138`
- 结构：`menuItemClass` / `string`
- 原文/表达式：h-[30px] gap-2 rounded-control px-2 text-body
- 判定原因：该英文字符串“h-[30px] gap-2 rounded-control px-2 text-body”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e3394c35b6be4a65916a4a3ede99356c9360ca7cc8a213e44bcbe77b142de07c`

### 410. `hardcoded:src/components/usage/UsageDashboard.tsx:rangeLabel:0716d895d8892441:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:445`
- 结构：`rangeLabel` / `template`
- 原文/表达式：`${startStr} → ${t("usage.liveEndTimeNow", "现在")}`
- 判定原因：该中文自然语言“`${startStr} → ${t("usage.liveEndTimeNow", "现在")}`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`0716d895d88924413a6332e4e9400539c5f606a2f485b9e12624a505d5e1e643`

### 411. `hardcoded:src/components/usage/UsageDashboard.tsx:rangeLabel:499627258b1a34d9:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:450`
- 结构：`rangeLabel` / `template`
- 原文/表达式：`${startStr} - ${endStr}`
- 判定原因：该英文字符串“`${startStr} - ${endStr}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`499627258b1a34d92018f3f3b9f8d677949e2582b8da3646f4e8c9080d74d6fd`

### 412. `hardcoded:src/components/usage/UsageDashboard.tsx:scopeLabel:72d723c09b75c783:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:492`
- 结构：`scopeLabel` / `template`
- 原文/表达式：`${providerText} / ${model ?? t("usage.modelFilter.label")}`
- 判定原因：该英文字符串“`${providerText} / ${model ?? t("usage.modelFilter.label")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`72d723c09b75c7833b783854c258879661bff00453cc5e46fea5a92b1fb95076`

### 413. `hardcoded:src/components/usage/UsageDashboard.tsx:scopeTitle:5cb9663d32896aed:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:493`
- 结构：`scopeTitle` / `template`
- 原文/表达式：`${<br>    providerName<br>      ? usageProviderTitle(getUsageProviderLabel(providerName, t))<br>      : t("usage.providerFilter.all")<br>  } / ${model ?? t("usage.allModels")}`
- 判定原因：该英文字符串“`${
    providerName
      ? usageProviderTitle(getUsageProviderLabel(providerName, t))
      : t("usage.providerFilter.all")
  } / ${model ?? t("usage.allModels")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5cb9663d32896aede94931e0ba14836c041c77bbda7c6477178c04071a10dc8b`

### 414. `hardcoded:src/components/usage/UsageDashboard.tsx:chipClass:542d0fcb22648b8b:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:577`
- 结构：`chipClass` / `string`
- 原文/表达式：relative inline-flex h-[26px] shrink-0 items-center gap-1.5 whitespace-nowrap rounded-[5px] px-2 text-body transition-colors duration-150
- 判定原因：该英文字符串“relative inline-flex h-[26px] shrink-0 items-center gap-1.5 whitespace-nowrap rounded-[5px] px-2 text-body transition-colors duration-150”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`542d0fcb22648b8bd335b620056aa12f02984044266492ee6ad13b5dea2c2649`

### 415. `hardcoded:src/components/usage/UsageDashboard.tsx:statusLabel:8e1e5c98d5ad132f:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:750`
- 结构：`statusLabel` / `template`
- 原文/表达式：`${t("usage.statusCode")} ${statusCode}`
- 判定原因：该英文字符串“`${t("usage.statusCode")} ${statusCode}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8e1e5c98d5ad132fff7b7ea0bd4dcd6cb19a697998a5117ac5cc680c41e7afe6`

### 416. `hardcoded:src/components/usage/UsageDashboard.tsx:tabTrailing:5bc0be3bb557a00a:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:769`
- 结构：`tabTrailing` / `template`
- 原文/表达式：`${t("usage.statusCode")}: ${statusLabel}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${t("usage.statusCode")}: ${statusLabel}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5bc0be3bb557a00a740a7a562c6a1ee06a7165bed7f853987ad6f03b5e5623f2`

### 417. `hardcoded:src/components/usage/UsageDashboard.tsx:tabTrailing:54a4ec11e9fff92b:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDashboard.tsx:774`
- 结构：`tabTrailing` / `template`
- 原文/表达式：`${t("usage.statusCode")} · ${statusCode}`
- 判定原因：该英文字符串“`${t("usage.statusCode")} · ${statusCode}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`54a4ec11e9fff92b08ca310a1bbb412f593fed224e07172d8e2a8c2d9f40fedc`

### 418. `hardcoded:src/components/usage/UsageDateRangePicker.tsx:fmtDate:fdd7d36ce6361378:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDateRangePicker.tsx:57`
- 结构：`fmtDate` / `template`
- 原文/表达式：`${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`
- 判定原因：该英文字符串“`${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fdd7d36ce6361378ce9533c0b63fe26d5e5150e33f240d1ed3deb733f9dd4061`

### 419. `hardcoded:src/components/usage/UsageDateRangePicker.tsx:fmtTime:9ec707dbf089d1d9:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDateRangePicker.tsx:62`
- 结构：`fmtTime` / `template`
- 原文/表达式：`${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`
- 判定原因：该英文字符串“`${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9ec707dbf089d1d9841d6631bd7113f1f78e3935e3d9d044530753ed2085a9c2`

### 420. `hardcoded:src/components/usage/UsageDateRangePicker.tsx:UsageDateRangePicker:6033976d541c7f64:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDateRangePicker.tsx:337`
- 结构：`UsageDateRangePicker` / `template`
- 原文/表达式：`${t("usage.timeRange")}: ${triggerLabel}`
- 控件属性：`title`
- 判定原因：该英文字符串“`${t("usage.timeRange")}: ${triggerLabel}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6033976d541c7f64408a3d7d4d026e197b3f67f5faaffcc5f7d5ea8c952f2fda`

### 421. `dynamic-i18n:src/components/usage/UsageDisplaySection.tsx:todayLabel:9c965868dda12772:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDisplaySection.tsx:93`
- 结构：`todayLabel` / `dynamic_i18n_key`
- 原文/表达式：`usage.display.sidebarTodayItems.${item}`
- 判定原因：翻译键由运行时表达式“`usage.display.sidebarTodayItems.${item}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`9c965868dda12772b73d7958875846e84e79a30b5a00c878d6a75c0f72e2639a`

### 422. `hardcoded:src/components/usage/UsageDisplaySection.tsx:optionLabel:c3dfb4461375f848:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDisplaySection.tsx:132`
- 结构：`optionLabel` / `template`
- 原文/表达式：`${code} · ${name}`
- 判定原因：该英文字符串“`${code} · ${name}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c3dfb4461375f84869831c84b0f56441bb454554ca512e062ed19c0985590611`

### 423. `dynamic-i18n:src/components/usage/UsageDisplaySection.tsx:UsageDisplaySection:74fefa25328abc5c:001`

- 状态：待核实
- 文件：`src/components/usage/UsageDisplaySection.tsx:196`
- 结构：`UsageDisplaySection` / `dynamic_i18n_key`
- 原文/表达式：`usage.display.trendChartTypes.${type}`
- 判定原因：翻译键由运行时表达式“`usage.display.trendChartTypes.${type}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`74fefa25328abc5cd636335aba766326037e74a4da2150435f5b885939fd630c`

### 424. `hardcoded:src/components/usage/UsageHeatmap.tsx:dayKey:05714fc0c04ea9bc:001`

- 状态：待核实
- 文件：`src/components/usage/UsageHeatmap.tsx:67`
- 结构：`dayKey` / `template`
- 原文/表达式：`${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
- 判定原因：该英文字符串“`${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`05714fc0c04ea9bcfd0f81fab211969a947c1e84c0dc7bb43ec014113ea9d3bd`

### 425. `hardcoded:src/components/usage/UsageHeatmap.tsx:UsageHeatmap:23e345142b3ca51f:001`

- 状态：待核实
- 文件：`src/components/usage/UsageHeatmap.tsx:347`
- 结构：`UsageHeatmap` / `template`
- 原文/表达式：`${formatDay(span.start)} – ${formatDay(span.end)}`
- 判定原因：该英文字符串“`${formatDay(span.start)} – ${formatDay(span.end)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`23e345142b3ca51f6259f8daa8d812be6212b19ebd2c4889dd86eb178917c419`

### 426. `hardcoded:src/components/usage/UsageHeatmap.tsx:UsageHeatmap:d2f6cd8d02b2368e:001`

- 状态：待核实
- 文件：`src/components/usage/UsageHeatmap.tsx:360`
- 结构：`UsageHeatmap` / `template`
- 原文/表达式：`max-content repeat(${WEEKS}, minmax(0, 1fr))`
- 判定原因：该英文字符串“`max-content repeat(${WEEKS}, minmax(0, 1fr))`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d2f6cd8d02b2368e0673e5d3e85509aea3c5a81605dfc024960f4b6cc2594958`

### 427. `hardcoded:src/components/usage/UsageHeatmap.tsx:UsageHeatmap:56fbde541cda9392:001`

- 状态：待核实
- 文件：`src/components/usage/UsageHeatmap.tsx:418`
- 结构：`UsageHeatmap` / `template`
- 原文/表达式：`translate(${<br>              hover.x < 110<br>                ? "-15%"<br>                : hover.x > (sectionRef.current?.clientWidth ?? 0) - 110<br>                  ? "-85%"<br>                  : "-50%"<br>            }, -100%)`
- 判定原因：该英文字符串“`translate(${
              hover.x < 110
                ? "-15%"
                : hover.x > (sectionRef.current?.clientWidth ?? 0) - 110
                  ? "-85%"
                  : "-50%"
            }, -100%)`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`56fbde541cda939239c820886cefa0c3772a0534548413e45dd12c806aa8bb4f`

### 428. `hardcoded:src/components/usage/UsageHero.tsx:MetricCell:ec3537f0ae32e2cd:001`

- 状态：待核实
- 文件：`src/components/usage/UsageHero.tsx:114`
- 结构：`MetricCell` / `template`
- 原文/表达式：`${label} ${value}`
- 控件属性：`aria-label`
- 判定原因：该英文字符串“`${label} ${value}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ec3537f0ae32e2cd271994955ea19538cdb473336444fe2b78d882dcd14450e2`

### 429. `hardcoded:src/components/usage/UsageSettingsSheet.tsx:UsageSettingsSheet:af87a121cdc72f85:001`

- 状态：待核实
- 文件：`src/components/usage/UsageSettingsSheet.tsx:204`
- 结构：`UsageSettingsSheet` / `template`
- 原文/表达式：`${cadence} · ${syncedLabel}`
- 判定原因：该英文字符串“`${cadence} · ${syncedLabel}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`af87a121cdc72f85e0044fb14192a4c657fbaf1dea1844a7abb6e282141f7c9e`

### 430. `hardcoded:src/components/usage/UsageTrendChart.tsx:cjkThousandUnits:8cb898c3a50a87f7:001`

- 状态：待核实
- 文件：`src/components/usage/UsageTrendChart.tsx:202`
- 结构：`cjkThousandUnits` / `string`
- 原文/表达式：千億
- 判定原因：该中文自然语言“千億”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`8cb898c3a50a87f736756b5070e4b7acf56391d69d2ef3277af6e601a50e3737`

### 431. `hardcoded:src/components/usage/UsageTrendChart.tsx:cjkThousandUnits:8ab9459f89997207:001`

- 状态：待核实
- 文件：`src/components/usage/UsageTrendChart.tsx:203`
- 结构：`cjkThousandUnits` / `string`
- 原文/表达式：千萬
- 判定原因：该中文自然语言“千萬”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`8ab9459f89997207a295a31c41adc85f6f606f7a2fcd9423f1c11d1f08ef14cb`

### 432. `hardcoded:src/components/usage/UsageTrendChart.tsx:cjkThousandUnits:4e8ee85b3668ef16:001`

- 状态：待核实
- 文件：`src/components/usage/UsageTrendChart.tsx:208`
- 结构：`cjkThousandUnits` / `string`
- 原文/表达式：千亿
- 判定原因：该中文自然语言“千亿”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`4e8ee85b3668ef1656bfa750123479be1f4940c12bea113ea3d24ce2e4af2272`

### 433. `hardcoded:src/components/usage/UsageTrendChart.tsx:cjkThousandUnits:1a7f74b68f2f3fa1:001`

- 状态：待核实
- 文件：`src/components/usage/UsageTrendChart.tsx:209`
- 结构：`cjkThousandUnits` / `string`
- 原文/表达式：千万
- 判定原因：该中文自然语言“千万”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`1a7f74b68f2f3fa12d8a5bfcdef98e9d9f4be7d9e712ed496669f1fd9e83c0fc`

### 434. `hardcoded:src/components/usage/UsageTrendChart.tsx:cjkThousandUnits:8cb898c3a50a87f7:002`

- 状态：待核实
- 文件：`src/components/usage/UsageTrendChart.tsx:214`
- 结构：`cjkThousandUnits` / `string`
- 原文/表达式：千億
- 判定原因：该中文自然语言“千億”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`8cb898c3a50a87f736756b5070e4b7acf56391d69d2ef3277af6e601a50e3737`

### 435. `hardcoded:src/components/usage/UsageTrendChart.tsx:cjkThousandUnits:1a7f74b68f2f3fa1:002`

- 状态：待核实
- 文件：`src/components/usage/UsageTrendChart.tsx:215`
- 结构：`cjkThousandUnits` / `string`
- 原文/表达式：千万
- 判定原因：该中文自然语言“千万”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`1a7f74b68f2f3fa12d8a5bfcdef98e9d9f4be7d9e712ed496669f1fd9e83c0fc`

### 436. `hardcoded:src/components/usage/UsageTrendChart.tsx:formatYTick:9b4c832c895ad013:001`

- 状态：待核实
- 文件：`src/components/usage/UsageTrendChart.tsx:342`
- 结构：`formatYTick` / `template`
- 原文/表达式：`${+((Number(value) \|\| 0) * 100).toFixed(1)}%`
- 判定原因：该英文字符串“`${+((Number(value) || 0) * 100).toFixed(1)}%`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9b4c832c895ad01389aecf13a5bfcf9a249a260ae24a06238b40653850f67d82`

### 437. `hardcoded:src/components/usage/format.ts:formatHitRatePercent:a56b80ab4481f505:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:93`
- 结构：`formatHitRatePercent` / `template`
- 原文/表达式：`${percent.toFixed(percent >= 99.95 ? 0 : 1)}%`
- 判定原因：该英文字符串“`${percent.toFixed(percent >= 99.95 ? 0 : 1)}%`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a56b80ab4481f5056079d84ed14b5a7848afee0a1260e6d70b3ff679a89f1630`

### 438. `hardcoded:src/components/usage/format.ts:formatFirstTokenSeconds:f0b85f0f527f92a4:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:342`
- 结构：`formatFirstTokenSeconds` / `template`
- 原文/表达式：`${(value / 1000).toFixed(1)}s`
- 判定原因：该英文字符串“`${(value / 1000).toFixed(1)}s`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f0b85f0f527f92a451706703e8bc3a01a80df1e11b00e514eae79d8e0c950139`

### 439. `hardcoded:src/components/usage/format.ts:formatTokensCompact:d7c29eea2a59877c:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:380`
- 结构：`formatTokensCompact` / `template`
- 原文/表达式：`${Number((num / biggerSize).toPrecision(3))}${biggerSuffix}`
- 判定原因：该英文字符串“`${Number((num / biggerSize).toPrecision(3))}${biggerSuffix}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d7c29eea2a59877cc80f9ea801040876351e37fafcd83ea35e31450e3cb50939`

### 440. `hardcoded:src/components/usage/format.ts:formatTokensShort:8e76c146d0b98bd4:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:464`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e8).toFixed(2)} 億`
- 判定原因：该中文自然语言“`${(value / 1e8).toFixed(2)} 億`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`8e76c146d0b98bd4d9f25361fed0ce80568cf2a0770aaa3f8006ca684b5185d5`

### 441. `hardcoded:src/components/usage/format.ts:formatTokensShort:ca5d2c30904e904b:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:465`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e4).toFixed(decimals)} 萬`
- 判定原因：该中文自然语言“`${(value / 1e4).toFixed(decimals)} 萬`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`ca5d2c30904e904b73b7b0d0c48816937e1d5746b18ec7dfbbbb6fc7dee6503b`

### 442. `hardcoded:src/components/usage/format.ts:formatTokensShort:4acbf115cc24262b:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:474`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e8).toFixed(2)} 亿`
- 判定原因：该中文自然语言“`${(value / 1e8).toFixed(2)} 亿`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`4acbf115cc24262b8bc2c7f219b9e114101a2de4c6fcd4963cb69b84b516b278`

### 443. `hardcoded:src/components/usage/format.ts:formatTokensShort:fc92e239e95de9c7:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:475`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e4).toFixed(decimals)} 万`
- 判定原因：该中文自然语言“`${(value / 1e4).toFixed(decimals)} 万`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`fc92e239e95de9c73c6693549bf624862b3af1b952325090ec4fac31e70be7e0`

### 444. `hardcoded:src/components/usage/format.ts:formatTokensShort:0fc5ea62db4a7e4b:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:479`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e8).toFixed(2)}억`
- 判定原因：该中文自然语言“`${(value / 1e8).toFixed(2)}억`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`0fc5ea62db4a7e4b781d537004cf4e8953e7ebd02a70d17232cf582504cef475`

### 445. `hardcoded:src/components/usage/format.ts:formatTokensShort:adb86911aab86ed5:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:480`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e4).toFixed(decimals)}만`
- 判定原因：该中文自然语言“`${(value / 1e4).toFixed(decimals)}만`”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`adb86911aab86ed524a952611adac622cdef3072e07af93a9359eedccb359689`

### 446. `hardcoded:src/components/usage/format.ts:formatTokensShort:83b780cbce7a6b71:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:483`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e9).toFixed(2)}B`
- 判定原因：该英文字符串“`${(value / 1e9).toFixed(2)}B`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`83b780cbce7a6b710750e5f9b08765f2e113cfe9f7cc51a1158d4ba3c44adcfc`

### 447. `hardcoded:src/components/usage/format.ts:formatTokensShort:6d2024a86c35bb0d:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:484`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e6).toFixed(2)}M`
- 判定原因：该英文字符串“`${(value / 1e6).toFixed(2)}M`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6d2024a86c35bb0d337b63d535aa45a27f5bf98db2c5c2e6c28845c705032116`

### 448. `hardcoded:src/components/usage/format.ts:formatTokensShort:943d3fd712684a3e:001`

- 状态：待核实
- 文件：`src/components/usage/format.ts:485`
- 结构：`formatTokensShort` / `template`
- 原文/表达式：`${(value / 1e3).toFixed(decimals)}K`
- 判定原因：该英文字符串“`${(value / 1e3).toFixed(decimals)}K`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`943d3fd712684a3e5afb7c462b749bf88b335ef48d6a86f874608d15245dc427`

### 449. `hardcoded:src/components/usage/usageTable.ts:usageTable:82fd35680446c652:001`

- 状态：待核实
- 文件：`src/components/usage/usageTable.ts:17`
- 结构：`usageTable` / `string`
- 原文/表达式：h-9 bg-subtle text-caption text-fg-2 [&>th]:border-b [&>th]:border-border
- 判定原因：该英文字符串“h-9 bg-subtle text-caption text-fg-2 [&>th]:border-b [&>th]:border-border”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`82fd35680446c652a41e7156bde56cefca7054557357517591adfb291185b8fe`

### 450. `hardcoded:src/components/usage/usageTable.ts:usageTable:7b50091269eb5e92:001`

- 状态：待核实
- 文件：`src/components/usage/usageTable.ts:20`
- 结构：`usageTable` / `string`
- 原文/表达式：h-10 [&:not(:last-child)>td]:border-b [&>td]:border-border
- 判定原因：该英文字符串“h-10 [&:not(:last-child)>td]:border-b [&>td]:border-border”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7b50091269eb5e92ce9bcbc1f77081315d190346c0a8f9cdf0fca1ed57080749`

### 451. `hardcoded:src/components/usage/usageTable.ts:usageTable:bbd2127178da5347:001`

- 状态：待核实
- 文件：`src/components/usage/usageTable.ts:22`
- 结构：`usageTable` / `string`
- 原文/表达式：group h-10 cursor-pointer transition-colors hover:bg-subtle [&:not(:last-child)>td]:border-b [&>td]:border-border
- 判定原因：该英文字符串“group h-10 cursor-pointer transition-colors hover:bg-subtle [&:not(:last-child)>td]:border-b [&>td]:border-border”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`bbd2127178da5347e0803054c8374f347558b941dfb0932266645f341092cfae`

### 452. `hardcoded:src/components/usage/usageTable.ts:usageTable:727c40ceae5a552b:001`

- 状态：待核实
- 文件：`src/components/usage/usageTable.ts:32`
- 结构：`usageTable` / `string`
- 原文/表达式：h-[240px] animate-pulse rounded-panel bg-subtle
- 判定原因：该英文字符串“h-[240px] animate-pulse rounded-panel bg-subtle”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`727c40ceae5a552b56c697a17a5a92fbac1f7a97d7f85818a50fdc16c2b5d8e4`

### 453. `hardcoded:src/components/workspace/DailyMemoryPanel.tsx:formatFileSize:229dd2efa20cfa06:001`

- 状态：待核实
- 文件：`src/components/workspace/DailyMemoryPanel.tsx:38`
- 结构：`formatFileSize` / `template`
- 原文/表达式：`${bytes} B`
- 判定原因：该英文字符串“`${bytes} B`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`229dd2efa20cfa06a18005595e089bef78a3ffc5bd33bb73dac85cca195d46c6`

### 454. `hardcoded:src/components/workspace/DailyMemoryPanel.tsx:formatFileSize:3774273e5fbf94ef:001`

- 状态：待核实
- 文件：`src/components/workspace/DailyMemoryPanel.tsx:39`
- 结构：`formatFileSize` / `template`
- 原文/表达式：`${(bytes / 1024).toFixed(1)} KB`
- 判定原因：该英文字符串“`${(bytes / 1024).toFixed(1)} KB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3774273e5fbf94ef8195350bfd3982824f82e6586e1751e20151e275c30f64df`

### 455. `hardcoded:src/components/workspace/DailyMemoryPanel.tsx:formatFileSize:388be0693bbcaae7:001`

- 状态：待核实
- 文件：`src/components/workspace/DailyMemoryPanel.tsx:40`
- 结构：`formatFileSize` / `template`
- 原文/表达式：`${(bytes / (1024 * 1024)).toFixed(1)} MB`
- 判定原因：该英文字符串“`${(bytes / (1024 * 1024)).toFixed(1)} MB`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`388be0693bbcaae784829d908026071c6cf9dd99feb7674ab79943d892cab407`

### 456. `hardcoded:src/components/workspace/DailyMemoryPanel.tsx:DailyMemoryPanel:a62f9585aac4983d:001`

- 状态：待核实
- 文件：`src/components/workspace/DailyMemoryPanel.tsx:331`
- 结构：`DailyMemoryPanel` / `template`
- 原文/表达式：`# ${editingFile}\n\n...`
- 控件属性：`placeholder`
- 判定原因：该英文字符串“`# ${editingFile}\n\n...`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a62f9585aac4983d7a49633de145969a7f92fe17b1b501de64e1a84f0e8fa075`

### 457. `hardcoded:src/components/workspace/DailyMemoryPanel.tsx:DailyMemoryPanel:3a7a1f5342930d80:001`

- 状态：待核实
- 文件：`src/components/workspace/DailyMemoryPanel.tsx:332`
- 结构：`DailyMemoryPanel` / `string`
- 原文/表达式：calc(100vh - 240px)
- 判定原因：该英文字符串“calc(100vh - 240px)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3a7a1f5342930d8032b686c8e4efdf236973e0713e5d4c9452b396b41cb61e5e`

### 458. `hardcoded:src/components/workspace/WorkspaceFileEditor.tsx:WorkspaceFileEditor:4e3cefaa77f57680:001`

- 状态：待核实
- 文件：`src/components/workspace/WorkspaceFileEditor.tsx:92`
- 结构：`WorkspaceFileEditor` / `template`
- 原文/表达式：`# ${filename}\n\n...`
- 控件属性：`placeholder`
- 判定原因：该英文字符串“`# ${filename}\n\n...`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4e3cefaa77f57680818b0a333b1f1de750be8300312e3ca0ae2d591afb1d4f5c`

### 459. `hardcoded:src/components/workspace/WorkspaceFileEditor.tsx:WorkspaceFileEditor:3a7a1f5342930d80:001`

- 状态：待核实
- 文件：`src/components/workspace/WorkspaceFileEditor.tsx:93`
- 结构：`WorkspaceFileEditor` / `string`
- 原文/表达式：calc(100vh - 240px)
- 判定原因：该英文字符串“calc(100vh - 240px)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`3a7a1f5342930d8032b686c8e4efdf236973e0713e5d4c9452b396b41cb61e5e`

### 460. `dynamic-i18n:src/components/workspace/WorkspaceFilesPanel.tsx:WorkspaceFilesPanel:347a6a525595a8b6:001`

- 状态：待核实
- 文件：`src/components/workspace/WorkspaceFilesPanel.tsx:123`
- 结构：`WorkspaceFilesPanel` / `dynamic_i18n_key`
- 原文/表达式：file.descKey
- 判定原因：翻译键由运行时表达式“file.descKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`347a6a525595a8b6f3f5f07623bb8c87dd641019052c4c36c8d856c7dc75560f`

### 461. `dynamic-i18n:src/config/mcpPresets.ts:getMcpPresetWithDescription:0c1d1c92eda0e772:001`

- 状态：待核实
- 文件：`src/config/mcpPresets.ts:102`
- 结构：`getMcpPresetWithDescription` / `dynamic_i18n_key`
- 原文/表达式：descriptionKey
- 判定原因：翻译键由运行时表达式“descriptionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0c1d1c92eda0e772769c808027e639ef98b15ace47087dabe50c20f4036b633e`

### 462. `hardcoded:src/hooks/useImportExport.ts:stamp:f2dcb0ff05d4bf4f:001`

- 状态：待核实
- 文件：`src/hooks/useImportExport.ts:146`
- 结构：`stamp` / `template`
- 原文/表达式：`${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, "0")}${String(now.getDate()).padStart(2, "0")}_${String(now.getHours()).padStart(2, "0")}${String(now.getMinutes()).padStart(2, "0")}${String(now.getSeconds()).padStart(2, "0")}`
- 判定原因：该英文字符串“`${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, "0")}${String(now.getDate()).padStart(2, "0")}_${String(now.getHours()).padStart(2, "0")}${String(now.getMinutes()).padStart(2, "0")}${String(now.getSeconds()).padStart(2, "0")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f2dcb0ff05d4bf4ff55658e4a4408dbf8a578527420ab0e807c16154a91260f8`

### 463. `hardcoded:src/hooks/useImportExport.ts:exportConfig:f13be88aac6f5c9e:001`

- 状态：待核实
- 文件：`src/hooks/useImportExport.ts:171`
- 结构：`exportConfig` / `template`
- 原文/表达式：`: ${result.message}`
- 判定原因：该英文字符串“`: ${result.message}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f13be88aac6f5c9e477a9411113ec7f1b55bb7d6fba9ff1ef1820b4694a66b3a`

### 464. `dynamic-i18n:src/hooks/useModeActions.ts:enter:883829e896b1bc8a:001`

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

### 465. `hardcoded:src/hooks/useMoneyFormat.ts:useMoneyFormat:59a5fc6fd4cd053a:001`

- 状态：待核实
- 文件：`src/hooks/useMoneyFormat.ts:38`
- 结构：`useMoneyFormat` / `template`
- 原文/表达式：`${formatMoney(usd, digits, display)} (${formatMoney(usd, digits, USD_DISPLAY)})`
- 判定原因：该英文字符串“`${formatMoney(usd, digits, display)} (${formatMoney(usd, digits, USD_DISPLAY)})`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`59a5fc6fd4cd053ad8359ed8da1b2799b65d66a5ae4c473f3cf4d200f7d68f4f`

### 466. `dynamic-i18n:src/hooks/usePromptActions.ts:toggleEnabled:0a592ddbd2de0f49:001`

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

### 467. `hardcoded:src/hooks/useProviderActions.ts:defaultMessage:c5dcde6ac770eac5:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:254`
- 结构：`defaultMessage` / `string`
- 原文/表达式：切换成功！
- 判定原因：该中文自然语言“切换成功！”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`c5dcde6ac770eac5cc5df65d657a8034dee4bc81fb7c1ffdd8bd4f8c26f0a09d`

### 468. `hardcoded:src/hooks/useProviderActions.ts:switchProvider:116dbbe928c6714b:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:257`
- 结构：`switchProvider` / `string`
- 原文/表达式：切换成功，请重启客户端以生效
- 判定原因：该中文自然语言“切换成功，请重启客户端以生效”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`116dbbe928c6714b42133a86d5af4dab8604be9184e71313bbe4ea79fd98bdc6`

### 469. `hardcoded:src/hooks/useProviderActions.ts:switchProvider:126efddcad591bbf:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:260`
- 结构：`switchProvider` / `string`
- 原文/表达式：切换成功，请重启 Gemini CLI 以生效
- 判定原因：该中文自然语言“切换成功，请重启 Gemini CLI 以生效”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`126efddcad591bbffaecbd9241d65a7b95423333103a0493fb3d5252fae769fc`

### 470. `hardcoded:src/hooks/useProviderActions.ts:switchProvider:33e50759e61e9304:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:263`
- 结构：`switchProvider` / `string`
- 原文/表达式：切换成功，请重启 Grok Build 以生效
- 判定原因：该中文自然语言“切换成功，请重启 Grok Build 以生效”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`33e50759e61e93049bf3838a3af6511d0d8899937d417cff91c637bbb0e21059`

### 471. `hardcoded:src/hooks/useProviderActions.ts:switchProvider:85c07603d29beae6:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:267`
- 结构：`switchProvider` / `string`
- 原文/表达式：切换成功，重启 Claude Desktop 后生效
- 判定原因：该中文自然语言“切换成功，重启 Claude Desktop 后生效”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`85c07603d29beae604f31f3ce4310bcb50fc86fc3fb22bd5a686fe1f90e0ba3d`

### 472. `hardcoded:src/hooks/useProviderActions.ts:switchProvider:cf2a766696e724f9:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:274`
- 结构：`switchProvider` / `string`
- 原文/表达式：已添加到配置
- 判定原因：该中文自然语言“已添加到配置”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`cf2a766696e724f946d8c1303c6e2a06a35688db2ae5a8d1eeb7739f3850f0f1`

### 473. `dynamic-i18n:src/hooks/useProviderActions.ts:message:957b5b6d4c6b0d30:001`

- 状态：待核实
- 文件：`src/hooks/useProviderActions.ts:278`
- 结构：`message` / `dynamic_i18n_key`
- 原文/表达式：messageKey
- 判定原因：翻译键由运行时表达式“messageKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`957b5b6d4c6b0d309df52a69490ab3731b3e639d324d8b29bf10dc914b793946`

### 474. `hardcoded:src/hooks/useSidebarCollapsed.ts:TOGGLE_EASING:7e5b5efabcadf337:001`

- 状态：待核实
- 文件：`src/hooks/useSidebarCollapsed.ts:21`
- 结构：`TOGGLE_EASING` / `string`
- 原文/表达式：cubic-bezier(0.2, 0, 0, 1)
- 判定原因：该英文字符串“cubic-bezier(0.2, 0, 0, 1)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`7e5b5efabcadf33752740db0db30c35155426df370322b475716b13b44d015b5`

### 475. `hardcoded:src/hooks/useSidebarCollapsed.ts:animateToggle:5e55e877e79ae833:001`

- 状态：待核实
- 文件：`src/hooks/useSidebarCollapsed.ts:69`
- 结构：`animateToggle` / `template`
- 原文/表达式：`-1px 0 0 0 ${line}`
- 判定原因：该英文字符串“`-1px 0 0 0 ${line}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`5e55e877e79ae833609e3666a0de0fbc82478623eceb1aa56a8853ecbb7811a5`

### 476. `hardcoded:src/hooks/useSidebarCollapsed.ts:animateToggle:1f988455b2ef4d24:001`

- 状态：待核实
- 文件：`src/hooks/useSidebarCollapsed.ts:69`
- 结构：`animateToggle` / `template`
- 原文/表达式：`1px 0 0 0 ${line}`
- 判定原因：该英文字符串“`1px 0 0 0 ${line}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`1f988455b2ef4d24dae3219df974c105cda2e94177054ccca515a1bfc8824d7d`

### 477. `hardcoded:src/hooks/useSidebarCollapsed.ts:animation:b4bf486120a6db3d:001`

- 状态：待核实
- 文件：`src/hooks/useSidebarCollapsed.ts:79`
- 结构：`animation` / `template`
- 原文/表达式：`translateX(${expanding ? width : -width}px)`
- 判定原因：该英文字符串“`translateX(${expanding ? width : -width}px)`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b4bf486120a6db3d708699857a3c78fd64eee65bb03fb73358c9012d2af71e28`

### 478. `hardcoded:src/lib/api/model-fetch.ts:showFetchModelsError:ce8bfd4f9ef161e2:001`

- 状态：待核实
- 文件：`src/lib/api/model-fetch.ts:140`
- 结构：`showFetchModelsError` / `string`
- 原文/表达式：All candidates failed
- 判定原因：该英文错误可能经 API 调用方展示给用户，需结合实际 toast/error boundary 链路确认。
- 处理方向：核实展示链路；如需展示则改为结构化错误并本地化。
- 严重程度：中
- 指纹：`ce8bfd4f9ef161e262ceb59684fe403fdd0249879f7c0a69f33032bf45f74237`

### 479. `hardcoded:src/lib/api/model-fetch.ts:showFetchModelsError:4db7fea974ed743a:001`

- 状态：待核实
- 文件：`src/lib/api/model-fetch.ts:152`
- 结构：`showFetchModelsError` / `string`
- 原文/表达式：Failed to parse
- 判定原因：该英文错误可能经 API 调用方展示给用户，需结合实际 toast/error boundary 链路确认。
- 处理方向：核实展示链路；如需展示则改为结构化错误并本地化。
- 严重程度：中
- 指纹：`4db7fea974ed743affebe73b108266d38f2d7db1a1abd1a3f7d0a6b17e230c11`

### 480. `hardcoded:src/lib/api/settings.ts:syncCurrentProvidersLive:55d960fe732358ec:001`

- 状态：待核实
- 文件：`src/lib/api/settings.ts:239`
- 结构：`syncCurrentProvidersLive` / `string`
- 原文/表达式：Sync current providers failed
- 判定原因：该英文错误可能经 API 调用方展示给用户，需结合实际 toast/error boundary 链路确认。
- 处理方向：核实展示链路；如需展示则改为结构化错误并本地化。
- 严重程度：中
- 指纹：`55d960fe732358ecca0ccaf9a6d24dbf84c91be44a233645e5a5971b680709ee`

### 481. `hardcoded:src/lib/api/settings.ts:openExternal:69e1efdb433faf0f:001`

- 状态：待核实
- 文件：`src/lib/api/settings.ts:248`
- 结构：`openExternal` / `string`
- 原文/表达式：Unsupported URL scheme
- 判定原因：该英文错误可能经 API 调用方展示给用户，需结合实际 toast/error boundary 链路确认。
- 处理方向：核实展示链路；如需展示则改为结构化错误并本地化。
- 严重程度：中
- 指纹：`69e1efdb433faf0fa6423096c721cdeea8e30610464632dae292a329094086fe`

### 482. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:c948ad90dbb56786:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:17`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.pro`
- 判定原因：翻译键由运行时表达式“`${key}.pro`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`c948ad90dbb5678610291538a968108d48de158c5a0ba0bfaf4fb81008c9cd5d`

### 483. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:e6d34e9dad987f63:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:20`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.max20x`
- 判定原因：翻译键由运行时表达式“`${key}.max20x`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`e6d34e9dad987f632f3f18e36e88b55211d1613b8fa4845a48fffe4d566c56b8`

### 484. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:526dea196aee52d7:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:23`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.max5x`
- 判定原因：翻译键由运行时表达式“`${key}.max5x`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`526dea196aee52d7886ac3e4c476eb29cc3bb3a25181468cf00307c80191f65c`

### 485. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:0643f8d5c2a7a4d6:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:25`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.max`
- 判定原因：翻译键由运行时表达式“`${key}.max`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`0643f8d5c2a7a4d6214d2d38a0b43faa32e0f8f264ca47dead55542c58d107ad`

### 486. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:73cc9395a6dcb325:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:29`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.teamPremium`
- 判定原因：翻译键由运行时表达式“`${key}.teamPremium`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`73cc9395a6dcb325d82f735d1a042fff223dcd0e026575f29309f5f69f8f9fa6`

### 487. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:8047060929970a87:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:30`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.team`
- 判定原因：翻译键由运行时表达式“`${key}.team`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`8047060929970a871fcf63d1f23b79fa556b232ba7cb693a0b36dd5c81f00dbc`

### 488. `dynamic-i18n:src/lib/claudePlan.ts:claudePlanLabel:906c5699182dee61:001`

- 状态：待核实
- 文件：`src/lib/claudePlan.ts:32`
- 结构：`claudePlanLabel` / `dynamic_i18n_key`
- 原文/表达式：`${key}.enterprise`
- 判定原因：翻译键由运行时表达式“`${key}.enterprise`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`906c5699182dee610ce1f9488363070fe1520ee83a2604834b454a9a83774070`

### 489. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:formatSkillError:70769166fc12d162:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:88`
- 结构：`formatSkillError` / `dynamic_i18n_key`
- 原文/表达式：defaultTitle
- 判定原因：翻译键由运行时表达式“defaultTitle”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`70769166fc12d1627fb5ece5b0a1c29e89411cde5da0673db299484321d4dd27`

### 490. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:description:f55554c3a3e38660:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:99`
- 结构：`description` / `dynamic_i18n_key`
- 原文/表达式：errorKey
- 判定原因：翻译键由运行时表达式“errorKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`f55554c3a3e386604c41ab7912c05ed79a2c10029c66f618bbe46841de3de024`

### 491. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:suggestionText:74e698c28bf062c8:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:104`
- 结构：`suggestionText` / `dynamic_i18n_key`
- 原文/表达式：suggestionKey
- 判定原因：翻译键由运行时表达式“suggestionKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`74e698c28bf062c806a22962230d15a0ee29463a2cc768d0cf94524888d5a38f`

### 492. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:formatSkillError:70769166fc12d162:002`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:109`
- 结构：`formatSkillError` / `dynamic_i18n_key`
- 原文/表达式：defaultTitle
- 判定原因：翻译键由运行时表达式“defaultTitle”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`70769166fc12d1627fb5ece5b0a1c29e89411cde5da0673db299484321d4dd27`

### 493. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:skillErrorReason:cc40d5267afefbf0:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:126`
- 结构：`skillErrorReason` / `dynamic_i18n_key`
- 原文/表达式：getSuggestionI18nKey(suggestion)
- 判定原因：翻译键由运行时表达式“getSuggestionI18nKey(suggestion)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`cc40d5267afefbf037b85e766c90145120db9f19a3bbdb13a9e69779732037a0`

### 494. `dynamic-i18n:src/lib/errors/skillErrorParser.ts:skillErrorReason:37f93e4d82bbafa0:001`

- 状态：待核实
- 文件：`src/lib/errors/skillErrorParser.ts:128`
- 结构：`skillErrorReason` / `dynamic_i18n_key`
- 原文/表达式：getErrorI18nKey(code)
- 判定原因：翻译键由运行时表达式“getErrorI18nKey(code)”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`37f93e4d82bbafa004c28b0304a43a96a0e1d1f97a588c17fcfa0c7fe241da41`

### 495. `hardcoded:src/lib/frontendLogger.ts:truncateForProcessing:cbfda67ba8d01c49:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:36`
- 结构：`truncateForProcessing` / `template`
- 原文/表达式：`${input.slice(0, limit)}\n[input truncated]`
- 判定原因：该英文字符串“`${input.slice(0, limit)}\n[input truncated]`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`cbfda67ba8d01c499bb2cb5edc43e9452cbff6fdeb27bacf0bd13a98aba339d3`

### 496. `hardcoded:src/lib/frontendLogger.ts:normalizeForSerialization:aec169c0ab82b403:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:113`
- 结构：`normalizeForSerialization` / `string`
- 原文/表达式：[Serialization budget exhausted]
- 判定原因：该英文字符串“[Serialization budget exhausted]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`aec169c0ab82b4036db425e3384a7eb47721ba289734da8a93dc6caaabd8d536`

### 497. `hardcoded:src/lib/frontendLogger.ts:normalizeForSerialization:240a7349df5725a8:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:139`
- 结构：`normalizeForSerialization` / `template`
- 原文/表达式：`[Function ${value.name \|\| "anonymous"}]`
- 判定原因：该英文字符串“`[Function ${value.name || "anonymous"}]`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`240a7349df5725a84188e9201644fa952aff3530b44a4e0a5578412dca4f6bd5`

### 498. `hardcoded:src/lib/frontendLogger.ts:normalizeForSerialization:b61c5f4904ca310d:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:148`
- 结构：`normalizeForSerialization` / `string`
- 原文/表达式：[Object: max depth reached]
- 判定原因：该英文字符串“[Object: max depth reached]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b61c5f4904ca310d8bc805b769dc1e88e78c7a87e98958063993827a7b85b9b3`

### 499. `hardcoded:src/lib/frontendLogger.ts:normalizeForSerialization:ca525422b0710ea8:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:164`
- 结构：`normalizeForSerialization` / `template`
- 原文/表达式：`[${value.length - items.length} more items]`
- 判定原因：该英文字符串“`[${value.length - items.length} more items]`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ca525422b0710ea8979f2f3d7811f511237ee9ab39d89631b3aac5f96a5ced0b`

### 500. `hardcoded:src/lib/frontendLogger.ts:normalizeForSerialization:a6a59f2d7f4301b2:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:194`
- 结构：`normalizeForSerialization` / `string`
- 原文/表达式：[Property access failed]
- 判定原因：该英文字符串“[Property access failed]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a6a59f2d7f4301b2bce74bc9dad8cd3ffba28f5cf30d7d40e087f87f0ae427b8`

### 501. `hardcoded:src/lib/frontendLogger.ts:normalizeForSerialization:320f0288df6f9b9d:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:199`
- 结构：`normalizeForSerialization` / `template`
- 原文/表达式：`${keys.length - MAX_SERIALIZED_ENTRIES} more properties`
- 判定原因：该英文字符串“`${keys.length - MAX_SERIALIZED_ENTRIES} more properties`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`320f0288df6f9b9d36d3c9330043efe075e0f9781f26446293a7fd2f0d0e5007`

### 502. `hardcoded:src/lib/frontendLogger.ts:redactStructuredString:07a7a381e326ec8c:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:231`
- 结构：`redactStructuredString` / `string`
- 原文/表达式：[oversized structured error omitted]
- 判定原因：该英文字符串“[oversized structured error omitted]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`07a7a381e326ec8c19eff2427d09cd352aa475da722401fdcc059a8599381937`

### 503. `hardcoded:src/lib/frontendLogger.ts:redactStructuredString:95fdfbbeae5c2a3e:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:243`
- 结构：`redactStructuredString` / `string`
- 原文/表达式：[Unserializable structured error]
- 判定原因：该英文字符串“[Unserializable structured error]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`95fdfbbeae5c2a3ec622de333fd7579a31949f24c601beafcc79360f8f7abc49`

### 504. `hardcoded:src/lib/frontendLogger.ts:head:bc0589bd3d32ff23:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:252`
- 结构：`head` / `template`
- 原文/表达式：`${error.name}: ${structuredMessage}`
- 判定原因：该英文字符串“`${error.name}: ${structuredMessage}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`bc0589bd3d32ff2338e79997252187f434eec2fdb7cdbbab8f7618ea7e08626e`

### 505. `hardcoded:src/lib/frontendLogger.ts:describeError:0dcceff676974cdc:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:278`
- 结构：`describeError` / `template`
- 原文/表达式：`${error.name}: ${error.message}`
- 判定原因：该英文字符串“`${error.name}: ${error.message}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0dcceff676974cdc68ff6a12ccd011c64acd14bc104aef6995943cccc539cf12`

### 506. `hardcoded:src/lib/frontendLogger.ts:describeError:8a25aa7e91c34786:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:294`
- 结构：`describeError` / `string`
- 原文/表达式：[Unserializable thrown value]
- 判定原因：该英文字符串“[Unserializable thrown value]”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8a25aa7e91c347868a92b6c8c6fc6eae8f700b9e238e5a6602afd940154483df`

### 507. `hardcoded:src/lib/frontendLogger.ts:raw:30f72c0662eb6970:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:307`
- 结构：`raw` / `template`
- 原文/表达式：`[frontend] ${truncateForProcessing(context, MAX_RAW_LOG_INPUT_LENGTH)}`
- 判定原因：该英文字符串“`[frontend] ${truncateForProcessing(context, MAX_RAW_LOG_INPUT_LENGTH)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`30f72c0662eb69702357eaad6b65e1554111d1c00dc30f2b43c796c553606f49`

### 508. `hardcoded:src/lib/frontendLogger.ts:message:20b547b100be9460:001`

- 状态：待核实
- 文件：`src/lib/frontendLogger.ts:320`
- 结构：`message` / `template`
- 原文/表达式：`${redacted.slice(0, MAX_LOG_MESSAGE_LENGTH)}\n[truncated]`
- 判定原因：该英文字符串“`${redacted.slice(0, MAX_LOG_MESSAGE_LENGTH)}\n[truncated]`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`20b547b100be94600edfa97432c17fc083c6b7c5e04c619e650b85e3cb7a6300`

### 509. `hardcoded:src/lib/localCache.ts:PREFIX:b59e5db84eabdb1f:001`

- 状态：待核实
- 文件：`src/lib/localCache.ts:5`
- 结构：`PREFIX` / `string`
- 原文/表达式：cc-switch-cache:
- 判定原因：该英文字符串“cc-switch-cache:”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b59e5db84eabdb1fc4eeb0293d00aec2f7173016f96332aa3035af77e8e4b92f`

### 510. `hardcoded:src/lib/modelMetadata.ts:findByVendor:d70070750f69df8e:001`

- 状态：待核实
- 文件：`src/lib/modelMetadata.ts:322`
- 结构：`findByVendor` / `template`
- 原文/表达式：`${providerId}/${model.id ?? normalized}`
- 判定原因：该英文字符串“`${providerId}/${model.id ?? normalized}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d70070750f69df8e493099fcfabc10bb37f271fc0ddb5080893d9ed296d4342b`

### 511. `hardcoded:src/lib/modelsDev.ts:fetchModelsDev:9e4495a2c8af0702:001`

- 状态：待核实
- 文件：`src/lib/modelsDev.ts:68`
- 结构：`fetchModelsDev` / `template`
- 原文/表达式：`HTTP ${response.status}`
- 判定原因：该英文字符串“`HTTP ${response.status}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`9e4495a2c8af0702e919e43187af73e35bcc45fe973b0698149f13bd8f8959f8`

### 512. `hardcoded:src/lib/modelsDevPricing.ts:searchableName:fe216a14478430f2:001`

- 状态：待核实
- 文件：`src/lib/modelsDevPricing.ts:51`
- 结构：`searchableName` / `template`
- 原文/表达式：`${modelId} ${model?.name ?? ""}`
- 判定原因：该英文字符串“`${modelId} ${model?.name ?? ""}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fe216a14478430f220eeaae632b8024ec7013a0c578506e92c41fe5de130bfab`

### 513. `hardcoded:src/lib/piPromptTemplate.ts:truncateSummary:db463380373038b7:001`

- 状态：待核实
- 文件：`src/lib/piPromptTemplate.ts:92`
- 结构：`truncateSummary` / `template`
- 原文/表达式：`${compact.slice(0, MAX_SUMMARY_LENGTH - 1).trimEnd()}…`
- 判定原因：该英文字符串“`${compact.slice(0, MAX_SUMMARY_LENGTH - 1).trimEnd()}…`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`db463380373038b742c7e038aed6bdb9f411005723079438ee96baead242968e`

### 514. `hardcoded:src/lib/piPromptTemplate.ts:descriptionLine:ac32575ae8489a16:001`

- 状态：待核实
- 文件：`src/lib/piPromptTemplate.ts:131`
- 结构：`descriptionLine` / `template`
- 原文/表达式：`description: ${JSON.stringify(normalizedDescription)}`
- 判定原因：该英文字符串“`description: ${JSON.stringify(normalizedDescription)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ac32575ae8489a162b7d449a83b84fbca77e7879583c741616e0d22655a52936`

### 515. `hardcoded:src/lib/query/mutations.ts:useAddProviderMutation:5a99841bd8136920:001`

- 状态：待核实
- 文件：`src/lib/query/mutations.ts:52`
- 结构：`useAddProviderMutation` / `string`
- 原文/表达式：Claude Desktop official provider was not created
- 判定原因：该英文异常可能向上冒泡到通知层，但当前调用链没有本地化包装。
- 处理方向：追踪 toast/error boundary 展示路径并改为错误码。
- 严重程度：中
- 指纹：`5a99841bd8136920932a647a4a455fb02bfbdc17c7b02c1b637bebadac4e0af9`

### 516. `hardcoded:src/lib/query/mutations.ts:useAddProviderMutation:da200209ed0ab32d:001`

- 状态：待核实
- 文件：`src/lib/query/mutations.ts:62`
- 结构：`useAddProviderMutation` / `string`
- 原文/表达式：Grok Build official provider was not created
- 判定原因：该英文异常可能向上冒泡到通知层，但当前调用链没有本地化包装。
- 处理方向：追踪 toast/error boundary 展示路径并改为错误码。
- 严重程度：中
- 指纹：`da200209ed0ab32dc6c33a10977335ca0e18ad0578e9aee789b3d5dd14e7196c`

### 517. `hardcoded:src/lib/query/mutations.ts:useAddProviderMutation:e23d98e6f193147b:001`

- 状态：待核实
- 文件：`src/lib/query/mutations.ts:86`
- 结构：`useAddProviderMutation` / `template`
- 原文/表达式：`Provider key is required for ${appId}`
- 判定原因：该英文异常可能向上冒泡到通知层，但当前调用链没有本地化包装。
- 处理方向：追踪 toast/error boundary 展示路径并改为错误码。
- 严重程度：中
- 指纹：`e23d98e6f193147b60c44089cc7b95589f8a706786239c35a94955fd286c0094`

### 518. `dynamic-i18n:src/lib/query/proxy.ts:useSetProxyStackMember:2e6460788eddf87d:001`

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

### 519. `dynamic-i18n:src/lib/query/proxy.ts:useSetProxyStackMember:7f3542671de62631:001`

- 状态：待核实
- 文件：`src/lib/query/proxy.ts:138`
- 结构：`useSetProxyStackMember` / `dynamic_i18n_key`
- 原文/表达式：`provider.${notice}`
- 判定原因：翻译键由运行时表达式“`provider.${notice}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`7f3542671de626310d5e5b3ed78dc2b8058c2dc915fbbb03ea3861bf9bcbccbc`

### 520. `dynamic-i18n:src/lib/query/proxy.ts:useAdoptCodexStackCatalog:7f3542671de62631:001`

- 状态：待核实
- 文件：`src/lib/query/proxy.ts:174`
- 结构：`useAdoptCodexStackCatalog` / `dynamic_i18n_key`
- 原文/表达式：`provider.${notice}`
- 判定原因：翻译键由运行时表达式“`provider.${notice}`”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`7f3542671de626310d5e5b3ed78dc2b8058c2dc915fbbb03ea3861bf9bcbccbc`

### 521. `hardcoded:src/lib/query/queries.ts:isTransientUsageError:126fbf59cf043830:001`

- 状态：待核实
- 文件：`src/lib/query/queries.ts:152`
- 结构：`isTransientUsageError` / `string`
- 原文/表达式：请求失败
- 判定原因：该中文自然语言“请求失败”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`126fbf59cf04383070ae09bb214f0949a07ab285c4d0f40585c5a5e67251f358`

### 522. `hardcoded:src/lib/query/queries.ts:isTransientUsageError:1fd8511c4d2c6733:001`

- 状态：待核实
- 文件：`src/lib/query/queries.ts:154`
- 结构：`isTransientUsageError` / `string`
- 原文/表达式：读取响应失败
- 判定原因：该中文自然语言“读取响应失败”不在已确认的翻译调用或明确技术上下文中，需结合实际展示位置复核。
- 处理方向：检查组件引用和渲染路径；若用户可见则迁入 i18n。
- 严重程度：中
- 指纹：`1fd8511c4d2c6733b8563200fea46ce0ea1bc3be082f62eb91de4052fec534a3`

### 523. `hardcoded:src/tray-panel/TrayPanel.tsx:QuotaBlock:cc992c496c079a15:001`

- 状态：待核实
- 文件：`src/tray-panel/TrayPanel.tsx:212`
- 结构：`QuotaBlock` / `template`
- 原文/表达式：`${Math.max(line.left, 2)}%`
- 判定原因：该英文字符串“`${Math.max(line.left, 2)}%`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`cc992c496c079a15ea8d0d0a6bbd1c04c3ff985c191aafe6dcccc3ee2fc13b45`

### 524. `hardcoded:src/tray-panel/TrayPanel.tsx:AppRow:e1c87a72a9ca77b9:001`

- 状态：待核实
- 文件：`src/tray-panel/TrayPanel.tsx:304`
- 结构：`AppRow` / `template`
- 原文/表达式：`${app.current} · `
- 判定原因：该英文字符串“`${app.current} · `”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e1c87a72a9ca77b98e633427834b2afe63b956f3179229dc554bbb8436cb1514`

### 525. `hardcoded:src/tray-panel/TrayPanel.tsx:media:f2d5c41a3679336a:001`

- 状态：待核实
- 文件：`src/tray-panel/TrayPanel.tsx:567`
- 结构：`media` / `template`
- 原文/表达式：`(resolution: ${pixelRatio}dppx)`
- 判定原因：该英文字符串“`(resolution: ${pixelRatio}dppx)`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`f2d5c41a3679336a2c990b296f40c737c5f5f00923e4e1da9477b0633b2a6930`

### 526. `hardcoded:src/tray-panel/TrayPanel.tsx:relayout:8bbf300e92d150fa:001`

- 状态：待核实
- 文件：`src/tray-panel/TrayPanel.tsx:707`
- 结构：`relayout` / `template`
- 原文/表达式：`${mainTop - top}px`
- 判定原因：该英文字符串“`${mainTop - top}px`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`8bbf300e92d150fa713c78adffbfb6ad16df8e3b1f16d30511fd2af6333390ff`

### 527. `hardcoded:src/tray-panel/TrayPanel.tsx:relayout:90b2d1e9dbec423a:001`

- 状态：待核实
- 文件：`src/tray-panel/TrayPanel.tsx:713`
- 结构：`relayout` / `template`
- 原文/表达式：`${subTop - top}px`
- 判定原因：该英文字符串“`${subTop - top}px`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`90b2d1e9dbec423af9e275fbf8080ed72db293434229de0fc6a72b33b7023962`

### 528. `hardcoded:src/tray-panel/TrayPanel.tsx:cornerStyle:a5a5e6a44a98b4e4:001`

- 状态：待核实
- 文件：`src/tray-panel/TrayPanel.tsx:945`
- 结构：`cornerStyle` / `template`
- 原文/表达式：`${radius}px 0 0 ${radius}px`
- 判定原因：该英文字符串“`${radius}px 0 0 ${radius}px`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a5a5e6a44a98b4e4a8eb00ecccb441bb2abb4d8aa7d3bbd3a3343cf552385bbb`

### 529. `hardcoded:src/tray-panel/TrayPanel.tsx:cornerStyle:e63ea7d292a5c50c:001`

- 状态：待核实
- 文件：`src/tray-panel/TrayPanel.tsx:946`
- 结构：`cornerStyle` / `template`
- 原文/表达式：`0 ${radius}px ${radius}px 0`
- 判定原因：该英文字符串“`0 ${radius}px ${radius}px 0`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e63ea7d292a5c50c029a54a7a889fcc7f93819e9d042a9cd102666c5655fef9b`

### 530. `hardcoded:src/tray-panel/UsageTab.tsx:bucketize:fcc75ca0e6b68396:001`

- 状态：待核实
- 文件：`src/tray-panel/UsageTab.tsx:111`
- 结构：`bucketize` / `template`
- 原文/表达式：`${first.label} – ${last.label}`
- 判定原因：该英文字符串“`${first.label} – ${last.label}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`fcc75ca0e6b68396e3b9e89e4fe39e4947df72a80c883be1ca3ae5e52fc19925`

### 531. `hardcoded:src/tray-panel/UsageTab.tsx:UsageTab:ff9484a2eb27a630:001`

- 状态：待核实
- 文件：`src/tray-panel/UsageTab.tsx:301`
- 结构：`UsageTab` / `template`
- 原文/表达式：`${t("usage.inputTokens")} ${formatTokensCompact(summary.totalInputTokens, locale)} · ${t("usage.outputTokens")} ${formatTokensCompact(summary.totalOutputTokens, locale)}`
- 判定原因：该英文字符串“`${t("usage.inputTokens")} ${formatTokensCompact(summary.totalInputTokens, locale)} · ${t("usage.outputTokens")} ${formatTokensCompact(summary.totalOutputTokens, locale)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`ff9484a2eb27a630e990957d8c3738d748b78d8c57d71d29eacd43603ee625c6`

### 532. `hardcoded:src/tray-panel/UsageTab.tsx:UsageTab:e616355cec9d85e9:001`

- 状态：待核实
- 文件：`src/tray-panel/UsageTab.tsx:306`
- 结构：`UsageTab` / `template`
- 原文/表达式：`${t("usage.cacheWrite")} ${formatTokensCompact(summary.totalCacheCreationTokens, locale)} · ${t("usage.cacheRead")} ${formatTokensCompact(summary.totalCacheReadTokens, locale)}`
- 判定原因：该英文字符串“`${t("usage.cacheWrite")} ${formatTokensCompact(summary.totalCacheCreationTokens, locale)} · ${t("usage.cacheRead")} ${formatTokensCompact(summary.totalCacheReadTokens, locale)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e616355cec9d85e9ce9c2aa232b8cfc118c04f5d40dcce23169ec5bee2ae2e1e`

### 533. `hardcoded:src/tray-panel/UsageTab.tsx:UsageTab:60f562bafec64a0d:001`

- 状态：待核实
- 文件：`src/tray-panel/UsageTab.tsx:358`
- 结构：`UsageTab` / `template`
- 原文/表达式：`${currencySymbol}${formatUsageTrendTokenTickLabel(value, tickFormatter)}`
- 判定原因：该英文字符串“`${currencySymbol}${formatUsageTrendTokenTickLabel(value, tickFormatter)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`60f562bafec64a0d4a4a9947e9aec7e174c71421804438923597cca982bae7b6`

### 534. `hardcoded:src/types/omo.ts:OMO_DISABLEABLE_AGENTS:94f4223d1647de6a:001`

- 状态：待核实
- 文件：`src/types/omo.ts:186`
- 结构：`OMO_DISABLEABLE_AGENTS` / `string`
- 原文/表达式：Metis (Plan Consultant)
- 判定原因：该英文字符串“Metis (Plan Consultant)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`94f4223d1647de6a95f079c7b14a8decac0026a10317e83dbca148790c5b0542`

### 535. `hardcoded:src/types/omo.ts:OMO_DISABLEABLE_AGENTS:61b1b3dd8e42e1cd:001`

- 状态：待核实
- 文件：`src/types/omo.ts:187`
- 结构：`OMO_DISABLEABLE_AGENTS` / `string`
- 原文/表达式：Momus (Plan Reviewer)
- 判定原因：该英文字符串“Momus (Plan Reviewer)”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`61b1b3dd8e42e1cde68a81bfea6af70640098421dd8fde8f669605251a2f8afe`

### 536. `hardcoded:src/types/omo.ts:OMO_SISYPHUS_AGENT_PLACEHOLDER:dae3717f08e64178:001`

- 状态：待核实
- 文件：`src/types/omo.ts:252`
- 结构：`OMO_SISYPHUS_AGENT_PLACEHOLDER` / `template`
- 原文/表达式：{<br>  "disabled": false,<br>  "default_builder_enabled": false,<br>  "planner_enabled": true,<br>  "replace_plan": true<br>}
- 判定原因：该英文字符串“{
  "disabled": false,
  "default_builder_enabled": false,
  "planner_enabled": true,
  "replace_plan": true
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`dae3717f08e64178d53c3d7bc262e30308f58223894e70fd93cea35bfa4b4344`

### 537. `hardcoded:src/types/omo.ts:OMO_LSP_PLACEHOLDER:c7371b895550fe89:001`

- 状态：待核实
- 文件：`src/types/omo.ts:259`
- 结构：`OMO_LSP_PLACEHOLDER` / `template`
- 原文/表达式：{<br>  "typescript-language-server": {<br>    "command": ["typescript-language-server", "--stdio"],<br>    "extensions": [".ts", ".tsx"],<br>    "priority": 10<br>  },<br>  "pylsp": {<br>    "disabled": true<br>  }<br>}
- 判定原因：该英文字符串“{
  "typescript-language-server": {
    "command": ["typescript-language-server", "--stdio"],
    "extensions": [".ts", ".tsx"],
    "priority": 10
  },
  "pylsp": {
    "disabled": true
  }
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c7371b895550fe89aaa203f1e36cb9c9ef0b80dd65373008b190ac7e860075b1`

### 538. `hardcoded:src/types/omo.ts:OMO_EXPERIMENTAL_PLACEHOLDER:713f419812a3d0af:001`

- 状态：待核实
- 文件：`src/types/omo.ts:270`
- 结构：`OMO_EXPERIMENTAL_PLACEHOLDER` / `template`
- 原文/表达式：{<br>  "truncate_all_tool_outputs": true,<br>  "aggressive_truncation": true,<br>  "auto_resume": true<br>}
- 判定原因：该英文字符串“{
  "truncate_all_tool_outputs": true,
  "aggressive_truncation": true,
  "auto_resume": true
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`713f419812a3d0afdb705a7c8c0fd9e0273fe48d80286d45b490c05b74629ac1`

### 539. `hardcoded:src/types/omo.ts:OMO_BACKGROUND_TASK_PLACEHOLDER:c07e959e3120b626:001`

- 状态：待核实
- 文件：`src/types/omo.ts:276`
- 结构：`OMO_BACKGROUND_TASK_PLACEHOLDER` / `template`
- 原文/表达式：{<br>  "defaultConcurrency": 5,<br>  "providerConcurrency": {<br>    "anthropic": 3,<br>    "openai": 5,<br>    "google": 10<br>  },<br>  "modelConcurrency": {<br>    "anthropic/claude-opus-5": 2,<br>    "google/gemini-3.6-flash": 10<br>  }<br>}
- 判定原因：该英文字符串“{
  "defaultConcurrency": 5,
  "providerConcurrency": {
    "anthropic": 3,
    "openai": 5,
    "google": 10
  },
  "modelConcurrency": {
    "anthropic/claude-opus-5": 2,
    "google/gemini-3.6-flash": 10
  }
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`c07e959e3120b62620e4e3c50954e75dc37977e98a5854c6283bc34329fd4037`

### 540. `hardcoded:src/types/omo.ts:OMO_BROWSER_AUTOMATION_PLACEHOLDER:be8a375e66943bf9:001`

- 状态：待核实
- 文件：`src/types/omo.ts:289`
- 结构：`OMO_BROWSER_AUTOMATION_PLACEHOLDER` / `template`
- 原文/表达式：{<br>  "provider": "playwright"<br>}
- 判定原因：该英文字符串“{
  "provider": "playwright"
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`be8a375e66943bf97a2e5406a0cb60ed2f80753a88f619507e1fb50a3fd7aba7`

### 541. `hardcoded:src/types/omo.ts:OMO_CLAUDE_CODE_PLACEHOLDER:71c2e1fe2c3d7aa1:001`

- 状态：待核实
- 文件：`src/types/omo.ts:293`
- 结构：`OMO_CLAUDE_CODE_PLACEHOLDER` / `template`
- 原文/表达式：{<br>  "mcp": true,<br>  "commands": true,<br>  "skills": true,<br>  "agents": true,<br>  "hooks": true,<br>  "plugins": true<br>}
- 判定原因：该英文字符串“{
  "mcp": true,
  "commands": true,
  "skills": true,
  "agents": true,
  "hooks": true,
  "plugins": true
}”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`71c2e1fe2c3d7aa1b96d812203d54d98c9c5bb536b1d959cdfcf0e2c4b9cc1eb`

### 542. `hardcoded:src/utils/customIcon.ts:PNG_HEADER_PREFIX:14463a37223c3105:001`

- 状态：待核实
- 文件：`src/utils/customIcon.ts:57`
- 结构：`PNG_HEADER_PREFIX` / `string`
- 原文/表达式：PNG<br><br>   IHDR
- 判定原因：该英文字符串“PNG

   IHDR”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`14463a37223c31053d306ff9a17d58d7c3fc742e0b2d4e82b235af44f742256f`

### 543. `hardcoded:src/utils/customIcon.ts:readAsDataUrl:60d9e332f1d677e8:001`

- 状态：待核实
- 文件：`src/utils/customIcon.ts:132`
- 结构：`readAsDataUrl` / `template`
- 原文/表达式：`data:${mimeType};base64,${result.slice(comma + 1)}`
- 判定原因：该英文字符串“`data:${mimeType};base64,${result.slice(comma + 1)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`60d9e332f1d677e856b4c3ac482377dcd668b255f66be4bf2119f9f1725e0443`

### 544. `hardcoded:src/utils/deepLinkConfigPreview.ts:sanitizeTomlForPreview:6e915f849a4a51a6:001`

- 状态：待核实
- 文件：`src/utils/deepLinkConfigPreview.ts:41`
- 结构：`sanitizeTomlForPreview` / `template`
- 原文/表达式：`${stringifyToml(maskStructuredSecrets(parsed) as Record<string, unknown>).trim()}\n`
- 判定原因：该英文字符串“`${stringifyToml(maskStructuredSecrets(parsed) as Record<string, unknown>).trim()}\n`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`6e915f849a4a51a6a9e91f5572064330ce8e9fa3c31c8d7ddb8ef8def9b46e53`

### 545. `hardcoded:src/utils/deeplinkRisk.ts:maskSensitiveValue:a62c2e494eb6da49:001`

- 状态：待核实
- 文件：`src/utils/deeplinkRisk.ts:34`
- 结构：`maskSensitiveValue` / `template`
- 原文/表达式：`${value.substring(0, 4)}${"*".repeat(12)}`
- 判定原因：该英文字符串“`${value.substring(0, 4)}${"*".repeat(12)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`a62c2e494eb6da4980815e65beb0045581a502c55c589806d4c093fb2d50df23`

### 546. `dynamic-i18n:src/utils/errorUtils.ts:translatePiProviderMutationError:87913d866ba16384:001`

- 状态：待核实
- 文件：`src/utils/errorUtils.ts:47`
- 结构：`translatePiProviderMutationError` / `dynamic_i18n_key`
- 原文/表达式：ompKey
- 判定原因：翻译键由运行时表达式“ompKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`87913d866ba16384ba8999764817a4113c4ca7d29f98076db7cc1b4cc2aad7c5`

### 547. `dynamic-i18n:src/utils/errorUtils.ts:translateMcpBackendError:87913d866ba16384:001`

- 状态：待核实
- 文件：`src/utils/errorUtils.ts:95`
- 结构：`translateMcpBackendError` / `dynamic_i18n_key`
- 原文/表达式：ompKey
- 判定原因：翻译键由运行时表达式“ompKey”动态构造，静态检查无法确认所有分支都能命中现有韩语资源。
- 处理方向：核实枚举/映射的所有可能键值，并补充覆盖测试；若存在未约束的外部输入，应改为显式映射。
- 严重程度：中
- 指纹：`87913d866ba16384ba8999764817a4113c4ca7d29f98076db7cc1b4cc2aad7c5`

### 548. `hardcoded:src/utils/usageDisplay.ts:formatValue:b628b45c26dd70c9:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:20`
- 结构：`formatValue` / `template`
- 原文/表达式：`${formatNumber(value)} ${unit}`
- 判定原因：该英文字符串“`${formatNumber(value)} ${unit}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`b628b45c26dd70c9ef0d45f7ed72737ea728ec56e7a84fdbd07375f5eab5674d`

### 549. `hardcoded:src/utils/usageDisplay.ts:formatUsed:982a7b3b5da93ed4:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:39`
- 结构：`formatUsed` / `template`
- 原文/表达式：`${labels.used} ${formatValue(data.used, "%")}`
- 判定原因：该英文字符串“`${labels.used} ${formatValue(data.used, "%")}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`982a7b3b5da93ed41e73e298e4d3580b0095bc6d935e87941a97c346638c37c4`

### 550. `hardcoded:src/utils/usageDisplay.ts:formatUsed:0330f89ad7c5df76:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:42`
- 结构：`formatUsed` / `template`
- 原文/表达式：`${labels.used} ${formatNumber(usedPercent)}%`
- 判定原因：该英文字符串“`${labels.used} ${formatNumber(usedPercent)}%`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`0330f89ad7c5df76078a8d510d30a37f0e2598ffa230d847dd2db1613e811d80`

### 551. `hardcoded:src/utils/usageDisplay.ts:formatUsed:e7ca37fa7de7d20a:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:45`
- 结构：`formatUsed` / `template`
- 原文/表达式：`${labels.used} ${formatValue(data.used, data.unit)}`
- 判定原因：该英文字符串“`${labels.used} ${formatValue(data.used, data.unit)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`e7ca37fa7de7d20a3a126cbd6631911a8997a17c5b63c7827b424fbdb84ac97d`

### 552. `hardcoded:src/utils/usageDisplay.ts:planPrefix:4896130fd53d476b:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:52`
- 结构：`planPrefix` / `template`
- 原文/表达式：`[${data.planName}] `
- 判定原因：该英文字符串“`[${data.planName}] `”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4896130fd53d476b55d3252d57c1aa6bfb6d9ea007992093640940e28aecde6e`

### 553. `hardcoded:src/utils/usageDisplay.ts:formatUsageDataSummary:27f679f4313c4c95:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:55`
- 结构：`formatUsageDataSummary` / `template`
- 原文/表达式：`${planPrefix}${data.invalidMessage \|\| labels.invalid}`
- 判定原因：该英文字符串“`${planPrefix}${data.invalidMessage || labels.invalid}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`27f679f4313c4c9502078c41db8dc9cb114823750ce0c0082c803dd289457d58`

### 554. `hardcoded:src/utils/usageDisplay.ts:parts:4104163cefe6bd2b:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:61`
- 结构：`parts` / `template`
- 原文/表达式：`${labels.remaining} ${formatValue(data.remaining, data.unit)}`
- 判定原因：该英文字符串“`${labels.remaining} ${formatValue(data.remaining, data.unit)}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`4104163cefe6bd2bf675d1c1e9b65e41edf7204b0d627d37d525acc72509eca0`

### 555. `hardcoded:src/utils/usageDisplay.ts:formatUsageDataSummary:d9c1ae1c8ba031a5:001`

- 状态：待核实
- 文件：`src/utils/usageDisplay.ts:66`
- 结构：`formatUsageDataSummary` / `template`
- 原文/表达式：`${planPrefix}${parts.join(" / ") \|\| labels.invalid}`
- 判定原因：该英文字符串“`${planPrefix}${parts.join(" / ") || labels.invalid}`”可能作为提示或错误展示，但静态上下文不足以确认展示链路。
- 处理方向：追踪调用方并确认是否需要本地化。
- 严重程度：低
- 指纹：`d9c1ae1c8ba031a5f254023b660b4cfef793b10e270a85012e0a5299cdd10e19`

### 556. `hardcoded:src/utils/uuid.ts:generateUUID:9a9f4bf4aeae48b2:001`

- 状态：待核实
- 文件：`src/utils/uuid.ts:21`
- 结构：`generateUUID` / `string`
- 原文/表达式：crypto API not available - please update your operating system
- 判定原因：该英文错误可能经 API 调用方展示给用户，需结合实际 toast/error boundary 链路确认。
- 处理方向：核实展示链路；如需展示则改为结构化错误并本地化。
- 严重程度：中
- 指纹：`9a9f4bf4aeae48b2882f4021cac56f9f4350e04fd8c61c89f42fa458a08f0dda`

### 557. `hardcoded:src/utils/uuid.ts:generateUUID:5dc10448349e3c3f:001`

- 状态：待核实
- 文件：`src/utils/uuid.ts:36`
- 结构：`generateUUID` / `template`
- 原文/表达式：`${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`
- 判定原因：该英文错误可能经 API 调用方展示给用户，需结合实际 toast/error boundary 链路确认。
- 处理方向：核实展示链路；如需展示则改为结构化错误并本地化。
- 严重程度：中
- 指纹：`5dc10448349e3c3f2bbf6a1e1bee1f54d086cfe7deb59921a0d97fc9a2a65613`

