# 覆盖率与校验

## 已有翻译资源

- 资源提取：6/6（100.0%）
- 资源总数：4448
- 批次规划：158
- 已完成批次：158
- 有效逐条审核：4448/4448（100.0%）
- 未审核：0
- 失效记录：0

## 国际化遗漏扫描

- 纳入生产源码：801
- 成功扫描：801（100.0%）
- 排除的非生产/测试及范围外文件：27
- 扫描失败：0
- 候选审核：4426/4426（100.0%）
- 动态翻译键：162/162 已登记判断

## 候选结论

- 确认遗漏：60
- 待核实：557
- 无需国际化：3809
- 未审核：0

## 确认遗漏分布

- `src/lib/schemas/provider.ts`：9
- `src/lib/requestOverrides.ts`：8
- `src/utils/tomlUtils.ts`：6
- `src/config/opencodeProviderPresets.ts`：5
- `src/config/piProviderPresets.ts`：5
- `src/utils/grokBuildConfig.ts`：5
- `src/components/usage/providerLabel.ts`：3
- `src/config/codingPlanProviders.ts`：3
- `src/config/universalProviderPresets.ts`：3
- `src/utils/providerConfigUtils.ts`：3
- `src/components/DeepLinkImportDialog.tsx`：2
- `src/components/UsageScriptModal.tsx`：2
- `src/components/providers/forms/hooks/useCodexTomlValidation.ts`：1
- `src/components/universal/UniversalProviderFormModal.tsx`：1
- `src/config/geminiProviderPresets.ts`：1
- `src/config/presetFamilies.ts`：1
- `src/hooks/usePromptActions.ts`：1
- `src/index.html`：1

## 结论类型

- 确认遗漏 / `string`：40
- 确认遗漏 / `template`：14
- 确认遗漏 / `jsx_text`：5
- 确认遗漏 / `html_text`：1
- 待核实 / `template`：268
- 待核实 / `dynamic_i18n_key`：162
- 待核实 / `string`：127

## 静态分析限制

- 动态拼接文本、运行时外部数据和间接渲染链仍可能存在静态扫描无法穷尽的文案。
- 动态翻译键已全部保留为待核实，不视为已证明安全。
- 语言质量结论不等同于程序化校验通过。
