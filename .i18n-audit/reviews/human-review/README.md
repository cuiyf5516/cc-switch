# 人工审核工作区

## 两个审核文件

### 1. 韩语翻译问题

`translation_review_decisions.csv`

- 86 条：必改、建议改、待核实。
- 主要列：
  - `中文原文`
  - `当前韩文`
  - `问题说明`
  - `建议韩文`
  - `人工决定`
  - `最终韩文`

`人工决定` 只能填写：

- `采纳`：采用 `建议韩文`
- `修改后采纳`：在 `最终韩文` 填最终版本
- `保留原译`
- `暂不处理`
- 留空：尚未审核

### 2. 国际化遗漏

`missing_i18n_review_decisions.csv`

- 2,053 条：确认遗漏和待核实。
- 主要列：
  - `文件`
  - `位置`
  - `功能上下文`
  - `原文或表达式`
  - `问题说明`
  - `建议处理方式`
  - `建议韩文`
  - `人工决定`
  - `最终韩文/修复要求`
  - `修复范围`

`人工决定` 只能填写：

- `确认修复`
- `误报`
- `无需国际化`
- `暂不处理`
- 留空：尚未审核

`修复范围` 默认是以下之一：

- `translation-only`
- `frontend-i18n`
- `backend-error`
- `dynamic-key`

> `deplink.html` 已按产品决定排除在韩语国际化审查范围之外，不再出现在本 CSV 中。

## 生成修复清单

完成 CSV 后运行：

```powershell
python .i18n-audit/scripts/build_repair_plan.py
```

脚本会：

1. 分别读取两个审核 CSV。
2. 校验所有非空人工结论。
3. 拒绝非法状态。
4. 拒绝缺少最终译文的已批准翻译项。
5. 只把 `采纳`、`修改后采纳`、`确认修复` 写入 `repair_plan.csv`。

交给修复 AI 时，只允许它读取 `repair_plan.csv`，不得处理其他条目。

## 注意

不要直接修改以下自动生成文件：

- `.i18n-audit/reports/translation_issues.md`
- `.i18n-audit/reports/missing_i18n.md`
- `.i18n-audit/manifest/resources.json`
- `.i18n-audit/manifest/hardcoded_candidates.json`
- `.i18n-audit/reviews/translations/`
- `.i18n-audit/reviews/hardcoded/`

人工审核结论只写在本目录的两个审核 CSV 中。
