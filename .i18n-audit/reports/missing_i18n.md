# 国际化遗漏审查

- 生产源码纳入：801
- 成功扫描：801
- 扫描失败：0
- 候选总数：4426
- 确认遗漏：1
- 待核实：0
- 无需国际化：4425
- 范围排除文件：1
- 候选类别排除：1891（后端错误 1436；前端单/双语硬编码 455）

> 本报告不展示已确认无需国际化的候选项。候选详情保留在 `.i18n-audit/reviews/hardcoded/`。

## 系统性结论

- 后端错误和前端单/双语硬编码文案按产品决定排除，均不计入韩语遗漏项。
- 162 个动态翻译键已逐一核实：161 个解析为有限枚举、本地词典或有意回退；1 个确认缺少 `apps.kimi` / `apps.dsh`。

## 确认遗漏明细（1）

### 1. `dynamic-i18n:src/components/providers/presentation.ts:buildAdditiveSections:2eb4a51baae54d37:001`

- 状态：确认遗漏
- 文件：`src/components/providers/presentation.ts:957`
- 结构：`buildAdditiveSections` / `dynamic_i18n_key`
- 原文/表达式：`apps.${app}`
- 判定原因：`apps.${app}` 会为 kimi/dsh 生成 `apps.kimi` / `apps.dsh`，这三个键在 zh/en/ko 均不存在；无 defaultValue，界面会显示原始资源键。
- 处理方向：为 `apps.kimi`、`apps.dsh` 增加 zh/en/ko 资源键，或对不支持的应用不渲染该帮助文案。
- 推荐韩文：apps.kimi: Kimi<br>apps.dsh: DSH
- 严重程度：中
- 指纹：`2eb4a51baae54d37ab7eb80531cacac553f173e0b41fa7516dd5b8ce6e6e5ef3`

## 待核实明细（0）

