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

- 确认遗漏：797
- 待核实：1256
- 无需国际化：2373
- 未审核：0

## 确认遗漏分布

- `src-tauri/src/commands/misc.rs`：51
- `src-tauri/src/database/schema.rs`：48
- `src-tauri/src/usage_script.rs`：41
- `src-tauri/src/services/provider/mod.rs`：34
- `src-tauri/src/services/proxy.rs`：27
- `src-tauri/src/services/session_usage_pi.rs`：27
- `src-tauri/src/services/env_manager.rs`：25
- `src-tauri/src/services/provider/live.rs`：20
- `src-tauri/src/claude_desktop_config.rs`：19
- `src-tauri/src/services/webdav_sync/archive.rs`：17
- `src-tauri/src/services/session_usage_codex.rs`：15
- `src-tauri/src/proxy/providers/xai_oauth_auth.rs`：14
- `src-tauri/src/services/session_usage.rs`：14
- `src-tauri/src/services/webdav.rs`：14
- `src-tauri/src/services/agy_account/keychain.rs`：13
- `src-tauri/src/services/session_usage_opencode.rs`：13
- `src-tauri/src/services/s3.rs`：12
- `src-tauri/src/services/model_pricing.rs`：11
- `src-tauri/src/commands/settings.rs`：10
- `src-tauri/src/database/backup.rs`：10
- `src-tauri/src/grok_config.rs`：10
- `src-tauri/src/session_manager/content.rs`：10
- `src-tauri/src/services/sync_protocol.rs`：9
- `src/lib/schemas/provider.ts`：9
- `src-tauri/src/claude_mcp.rs`：8
- `src-tauri/src/database/dao/settings.rs`：8
- `src-tauri/src/database/mod.rs`：8
- `src-tauri/src/services/claude_account/login.rs`：8
- `src-tauri/src/settings.rs`：8
- `src/lib/requestOverrides.ts`：8
- `src-tauri/src/codex_config.rs`：7
- `src-tauri/src/commands/failover.rs`：7
- `src-tauri/src/mode/controller.rs`：7
- `src-tauri/src/services/claude_account/snapshot/switch.rs`：7
- `src-tauri/src/codex_history_migration.rs`：6
- `src-tauri/src/gemini_config.rs`：6
- `src-tauri/src/mcp/validation.rs`：6
- `src-tauri/src/services/agy_account/mod.rs`：6
- `src-tauri/src/services/provider/codex_official_models.rs`：6
- `src-tauri/src/services/provider/icon.rs`：6

## 结论类型

- 确认遗漏 / `rust_string`：475
- 确认遗漏 / `backend_localized_error`：262
- 确认遗漏 / `string`：40
- 确认遗漏 / `template`：14
- 确认遗漏 / `jsx_text`：5
- 确认遗漏 / `html_text`：1
- 待核实 / `rust_string`：699
- 待核实 / `template`：268
- 待核实 / `dynamic_i18n_key`：162
- 待核实 / `string`：127

## 静态分析限制

- 动态拼接文本、运行时外部数据和间接渲染链仍可能存在静态扫描无法穷尽的文案。
- 动态翻译键已全部保留为待核实，不视为已证明安全。
- 语言质量结论不等同于程序化校验通过。
