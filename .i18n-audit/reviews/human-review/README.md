# 人工审核工作区

## 文件

- `review_decisions.csv`
  - 全部需要人工确认的审核项。
  - 翻译问题：86 条。
  - 国际化遗漏问题：2,416 条，包含“确认遗漏”和“待核实”。
  - 每条都有稳定 `issue_id`，与 `.i18n-audit/reports/` 中的报告对应。
- `repair_plan.csv`
  - 只包含人工明确批准修复的条目。
  - 初始只有表头，审核后由脚本生成。

## 翻译条目

`review_decision` 只能填写：

- `采纳`：采用 `ai_suggestion`
- `修改后采纳`：在 `final_text` 写最终韩文
- `保留原译`：保留当前韩文
- `暂不处理`
- 留空：尚未审核

`采纳` 时如果 `final_text` 为空，会使用 `ai_suggestion`。
`修改后采纳` 必须填写 `final_text`。

## 国际化遗漏条目

`review_decision` 只能填写：

- `确认修复`
- `误报`
- `无需国际化`
- `暂不处理`
- 留空：尚未审核

`final_text` 可在能确定韩文时填写；结构性修复可以留空。
`fix_scope` 可改为：

- `translation-only`
- `frontend-i18n`
- `backend-error`
- `dynamic-key`
- `deplink-page`

## 生成修复清单

完成 CSV 审核后运行：

```powershell
python .i18n-audit/scripts/build_repair_plan.py
```

脚本会：

1. 校验所有非空人工结论。
2. 拒绝非法状态。
3. 拒绝缺少最终译文的已批准翻译项。
4. 只把 `采纳`、`修改后采纳`、`确认修复` 写入 `repair_plan.csv`。

交给修复 AI 时，只允许它读取 `repair_plan.csv`，不得处理其他条目。

## 注意

不要直接修改以下自动生成文件：

- `.i18n-audit/reports/translation_issues.md`
- `.i18n-audit/reports/missing_i18n.md`
- `.i18n-audit/manifest/resources.json`
- `.i18n-audit/manifest/hardcoded_candidates.json`
- `.i18n-audit/reviews/translations/`
- `.i18n-audit/reviews/hardcoded/`

人工结论必须保存在本目录的 CSV 中。
