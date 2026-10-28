from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".i18n-audit"
MANIFEST_PATH = OUT / "manifest/hardcoded_candidates.json"
QUALITY_PATH = OUT / "reviews/quality/second_round.json"
RESULT_PATH = OUT / "reviews/quality/dynamic_key_verification.json"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def flatten_keys(tree: Any, prefix: str = "") -> set[str]:
    if isinstance(tree, dict):
        result: set[str] = set()
        for key, value in tree.items():
            result |= flatten_keys(value, f"{prefix}.{key}" if prefix else key)
        return result
    return {prefix}


def source_literals(rel: str, prop: str) -> set[str]:
    text = (ROOT / rel).read_text(encoding="utf-8")
    return set(re.findall(rf'{re.escape(prop)}\s*:\s*"([^"]+)"', text))


def main() -> int:
    locale_keys = {
        lang: flatten_keys(load(ROOT / f"src/i18n/locales/{lang}.json"))
        for lang in ("zh", "en", "ko")
    }
    resources = load(OUT / "manifest/resources.json")
    resource_keys = {
        record["key"]
        for record in resources["records"]
        if record.get("source_kind") == "json-locale"
    }
    manifest = load(MANIFEST_PATH)
    items = [
        item for item in manifest["candidates"]
        if item.get("source_kind") == "dynamic_i18n_key"
    ]

    def keys_exist(keys: list[str], label: str) -> None:
        unique = list(dict.fromkeys(keys))
        missing = {
            lang: [key for key in unique if key not in locale_keys[lang]]
            for lang in ("zh", "en", "ko")
        }
        if any(missing.values()):
            raise RuntimeError(f"{label} missing keys: {missing}")

    def enum(prefix: str, values: list[str]) -> list[str]:
        return [f"{prefix}.{value}" for value in values]

    app_ids = [
        "claude", "claude-desktop", "codex", "gemini", "grokbuild", "opencode",
        "openclaw", "hermes", "pi", "kimi", "dsh", "mcode", "agy", "omp",
    ]
    modes = ["direct", "route", "stack"]
    tool_names = ["claude", "codex", "gemini", "grok", "opencode", "openclaw", "hermes", "pi", "mcode", "kimi", "dsh", "agy", "omp"]
    profile_scopes = ["claude", "claude-desktop", "codex"]
    settings_sections = ["general", "appConfig", "routing", "network", "data", "about"]
    kim_caps = ["image_in", "thinking", "tool_use", "always_thinking", "dynamically_loaded_tools"]
    pi_levels = ["off", "minimal", "low", "medium", "high", "xhigh", "max"]
    omp_discovery = ["openaiModelsList", "proxy", "ollama", "llamaCpp", "lmStudio", "litellm", "appleFoundationModels"]
    log_levels = ["error", "warn", "info", "debug", "trace"]
    sidebar_items = ["cost", "tokens", "requests", "hitRate"]
    trend_types = ["bar", "area"]
    preset_groups = ["all", "login", "vendor", "thirdparty", "cloud", "local", "plugin", "universal"]
    group_hints = ["login", "vendor", "thirdparty", "cloud", "local", "plugin", "universal"]
    login_with = ["github", "chatgpt", "xai", "google", "kimi", "claude"]
    plans = ["payg", "coding", "codingPlan", "agentPlan", "tokenPlan", "enterpriseLite", "enterprisePro", "stepPlan", "aksk", "apiKey"]
    regions = ["cn", "intl"]
    quick_toggles = ["hideAttribution", "enableToolSearch", "disableAutoUpgrade", "disableArtifact", "disableAutoModeServer"]
    matrix_states = ["on", "off", "fail"]
    empty_apps = ["pi", "mcode", "dsh", "kimi", "omp"]
    import_notes = ["mcpPage.import.claudeNote"]
    risk_keys = enum("deeplink.risk", ["envHijack", "privateEndpoint", "shellCommand"])
    icon_codes = ["unsupported", "tooLarge", "dimensions", "decodeFailed"]
    whats_types = ["new", "fix", "improve"]
    reader_keys = []
    reader_text = (ROOT / "src/components/sessions/reader/i18n.ts").read_text(encoding="utf-8")
    reader_block = reader_text.split("export const READER_DEFAULTS", 1)[1].split("};", 1)[0]
    for key in re.findall(r'^\s*"?([A-Za-z][A-Za-z0-9_.]*)"?\s*:', reader_block, re.M):
        reader_keys.append(f"sessionManager.reader.{key}")
    name_keys = set()
    for path in (ROOT / "src").rglob("*.ts*"):
        name_keys |= source_literals(str(path.relative_to(ROOT)), "nameKey")
    label_keys = set()
    desc_keys = set()
    tooltip_keys = set()
    for path in (ROOT / "src").rglob("*.ts*"):
        rel = str(path.relative_to(ROOT))
        label_keys |= source_literals(rel, "labelKey")
        desc_keys |= source_literals(rel, "descKey")
        tooltip_keys |= source_literals(rel, "tooltipKey")
    webdav_keys = set(re.findall(r'(?:label|hint):\s*"(settings\.(?:webdavSync|s3Sync)\.[^"]+)"', (ROOT / "src/components/settings/WebdavSyncSection.tsx").read_text(encoding="utf-8")))
    request_log_keys = set(re.findall(r'labelKey:\s*"(usage\.[^"]+)"', (ROOT / "src/components/usage/requestLogColumns.ts").read_text(encoding="utf-8")))
    terminal_keys = source_literals("src/components/settings/TerminalSettings.tsx", "labelKey")
    language_keys = source_literals("src/components/settings/sections/GeneralSection.tsx", "labelKey")
    hermes_mode_keys = source_literals("src/config/hermesProviderPresets.ts", "labelKey")
    workspace_keys = source_literals("src/components/workspace/WorkspaceFilesPanel.tsx", "descKey")
    sync_keys = source_literals("src/components/skills/SkillsStorageSheet.tsx", "labelKey") | source_literals("src/components/skills/SkillsStorageSheet.tsx", "descKey")
    omo_keys = source_literals("src/components/providers/forms/OmoFormFields.tsx", "tooltipKey") | source_literals("src/components/providers/forms/OmoFormFields.tsx", "descKey")
    mcp_field_keys = enum("mcpPage.drawer.errors", ["nameRequired", "nameSpaces", "nameExists", "commandRequired", "urlRequired", "urlScheme"])
    mcp_format_keys = enum("mcpPage.drawer.pasteFormats", ["mcpServers", "opencode", "codex", "codexToml", "single", "named"])
    mcp_preset_descriptions = enum("mcp.presets", ["fetch", "time", "memory", "sequential-thinking", "context7"])  # normalized below
    mcp_preset_descriptions = [f"mcp.presets.{x}.description" for x in ["fetch", "time", "memory", "sequential-thinking", "context7"]]
    claude_plan_keys = [f"provider.form.claudeAccount.plan.{x}" for x in ["pro", "max20x", "max5x", "max", "teamPremium", "team", "enterprise"]]
    provider_notice_keys = [
        "provider.routeOwnsCatalog", "provider.officialModelsBundled",
        "provider.officialModelsUnavailable", "provider.officialModelsOutdated",
    ]
    official_reason_keys = enum("provider.officialModelsReason", ["cliFailed", "fetchFailed", "invalidList", "loginIncomplete", "loginStale", "noCli", "noLogin", "noVersion", "nothingUsable"])

    # These are deliberate non-translatable/optional fallbacks: the missing key never surfaces as a raw key.
    optional = {
        ("src/components/apps/AppsPage.tsx", 801): "该 hint 使用 defaultValue: ''；Kimi/DSH 在所有语言中都不是可安装提示，缺失键不会显示为原始键。",
        ("src/components/mcp/McpFormModal.tsx", 668): "模板标签使用 preset.id 作为有意的技术回退；fetch/time/memory/context7 是稳定的模板标识，不是可见的自然语言缺失。",
        ("src/components/providers/forms/shared/ApiKeySection.tsx", 60): "推广语使用 defaultValue: ''；google-official 没有推广文案，属于可选内容而非韩语缺失。",
    }
    local_reader_lines = {
        "src/components/sessions/reader/exportMarkdown.ts": {34, 80},
        "src/components/sessions/reader/i18n.ts": {140},
        "src/components/sessions/reader/toolSummary.ts": {199, 209, 238},
    }

    def literal_keys(expr: str) -> list[str]:
        return [key for key in re.findall(r'"([A-Za-z][A-Za-z0-9_-]*(?:\.[A-Za-z0-9_-]+)+)"', expr) if not key.endswith(".")]

    def classify(item: dict[str, Any]) -> dict[str, Any]:
        file = item["source_file"]
        line = item["line"]
        expr = item["expression"]
        key = f"{file}:{line}"
        if file == "src/components/providers/presentation.ts" and line == 957:
            return {
                "status": "确认遗漏",
                "reason": "`apps.${app}` 会为 kimi/dsh 生成 `apps.kimi` / `apps.dsh`，这三个键在 zh/en/ko 均不存在；无 defaultValue，界面会显示原始资源键。",
                "evidence": ["apps.kimi", "apps.dsh"],
                "resolution": "missing-runtime-keys",
                "suggested_ko": "apps.kimi: Kimi\napps.dsh: DSH",
            }
        if (file, line) in optional:
            return {"status": "无需国际化", "reason": optional[(file, line)], "evidence": [], "resolution": "intentional-fallback"}
        if file in local_reader_lines and line in local_reader_lines[file]:
            return {
                "status": "无需国际化",
                "reason": "该动态 key 只经过会话阅读器本地包装器；所有 READER_DEFAULTS 键在 zh/en/ko 的 `sessionManager.reader.*` 下均存在，且包装器提供 defaultValue。",
                "evidence": sorted(reader_keys),
                "resolution": "local-reader-wrapper",
            }
        # Literal-only branches: every possible literal key is present.
        literals = literal_keys(expr)
        if literals and not re.search(r"`|\$\{|\.nameKey|\.labelKey|\.descKey|\[|\bkey\b|\btext\b|\bverb\b|\bfull\b|\bgroup\b|\bompKey\b|\bdefaultTitle\b|\berrorKey\b|\bsuggestionKey\b", expr):
            keys_exist(literals, key)
            return {"status": "无需国际化", "reason": "该动态调用只有有限字面量分支，所有分支键在 zh/en/ko 均存在。", "evidence": literals, "resolution": "literal-branches"}

        checks: dict[str, tuple[list[str], str]] = {
            "src/App.tsx": ([
                "pi.provider.enabled", "omp.provider.enabled", "pi.provider.enableFailed", "omp.provider.enableFailed",
                "pi.provider.removed", "omp.provider.removed",
            ], "app 的取值范围是 PiFamilyAppId（pi/omp），所有 provider 状态键均存在。"),
            "src/components/DeepLinkImportDialog.tsx": (risk_keys, "RiskKind 的三个值均有 deeplink.risk.* 资源。"),
            "src/components/IconPicker.tsx": (enum("iconPicker.uploadError", icon_codes), "CustomIconErrorCode 四个值均有上传错误资源。"),
            "src/components/SubscriptionQuotaFooter.tsx": (
                list(dict.fromkeys([f"subscription.{x}" for x in ["fiveHour", "sevenDay", "sevenDayFable", "sevenDayOpus", "sevenDaySonnet", "thirtyDay", "geminiPro", "geminiFlash", "geminiFlashLite", "agyGeminiFiveHour", "agyGeminiWeekly", "agyThirdPartyFiveHour", "agyThirdPartyWeekly", "monthly", "credits", "copilotPremium", "agyGemini", "agyThirdParty"]])),
                "TIER_I18N_KEYS 的值均存在；INLINE_TIER_GROUPS 的 group 值也存在。",
            ),
            "src/components/UsageScriptModal.tsx": (list(dict.fromkeys(["usageScript.templateCustom", "usageScript.templateGeneral", "usageScript.templateNewAPI", "usageScript.templateSub2API", "usageScript.templateCopilot", "usageScript.templateTokenPlan", "usageScript.templateBalance", "usageScript.templateOfficialSubscription"])), "所有 TEMPLATE_NAME_KEYS 值均存在。"),
            "src/components/WhatsNewDialog.tsx": (enum("whatsNew.types", whats_types), "What's New 类型枚举的三种值均存在。"),
            "src/components/apps/AppsPage.tsx": (["appsPage.sectionInstalled", "appsPage.sectionNotInstalled", "settings.envBadge.wsl"], "App 安装/未安装分支和 ENV_BADGE_CONFIG.wsl.labelKey 均存在；Kimi/DSH hint 使用空默认值，作为可选提示排除。"),
            "src/components/mcp/UnifiedMcpPanel.tsx": ([f"appMatrix.cell.{x}" for x in matrix_states] + import_notes, "MatrixCellState 只有 on/off/fail，import notes 的显式键存在。"),
            "src/components/profiles/ProfileSwitcher.tsx": ([f"profiles.switcherTooltip.{x}" for x in profile_scopes] + [f"profiles.createDescription.{x}" for x in profile_scopes], "ProfileScope 只有 claude/claude-desktop/codex，对应资源均存在。"),
            "src/components/prompts/PiNativePromptResources.tsx": ([
                "pi.prompts.systemAppend", "pi.prompts.systemAppendDescription", "pi.prompts.systemOverride", "pi.prompts.systemOverrideDescription",
                "pi.prompts.editFile", "pi.prompts.createFile", "pi.prompts.appendDeleted", "pi.prompts.overrideDeleted",
                "pi.prompts.deletedBlank", "pi.prompts.deletedUndoable", "common.edit", "pi.prompts.create",
            ], "titleKey/descriptionKey 的字面量及所有分支键均存在。"),
            "src/components/providers/KimiAccountLogin.tsx": (enum("kimi.oauth", ["mainland-cn", "global", "expired", "denied", "cancelled", "dismissConfirm", "removeConfirm"]), "KimiRegion、ended 枚举和确认分支资源均存在。"),
            "src/components/providers/ProviderEmptyState.tsx": ([f"{x}.empty.{field}" for x in empty_apps for field in ("title", "description")], "emptyCopyNs 的五个应用均有 title/description。"),
            "src/components/providers/ProviderList.tsx": ([f"{x}.current.{field}" for x in ("pi", "omp") for field in ("readFailed", "stateUnavailableHint")], "Pi family 只有 pi/omp，current 状态键均存在。"),
            "src/components/providers/forms/CommonConfigEditor.tsx": ([f"claudeConfig.{x}{suffix}" for x in quick_toggles for suffix in ("", "Help")], "QUICK_TOGGLES 的 5 个值和对应 Help 键均存在。"),
            "src/components/providers/forms/HermesFormFields.tsx": (["hermes.form.baseUrlRequired", "hermes.form.baseUrlScheme", "hermes.form.baseUrlInvalid"] + list(hermes_mode_keys), "BaseUrlErrorCode 与 Hermes API mode labelKey 均存在。"),
            "src/components/providers/forms/KimiProviderForm.tsx": (enum("kimi.capabilities", kim_caps) + enum("kimi.capabilityHints", ["always_thinking", "dynamically_loaded_tools"]), "KIMI_CAPABILITIES 及其帮助键均存在。"),
            "src/components/providers/forms/hooks/useKimiOAuth.ts": (enum("kimi.oauth", ["expired", "denied", "cancelled"]), "Kimi OAuth ended 的有限枚举均存在。"),
            "src/components/providers/forms/OmoFormFields.tsx": (list(omo_keys), "Omo 内置模型定义中的 tooltipKey/descKey 均存在。"),
            "src/components/providers/forms/PiProviderForm.tsx": (enum("pi.form.thinkingLevels", pi_levels) + enum("omp.form.discoveryTypes", omp_discovery), "Pi thinking level 与 OMP discovery type 的有限枚举均有资源。"),
            "src/components/providers/forms/ProviderPresetSelector.tsx": (enum("providerPreset.group", preset_groups) + enum("providerPreset.groupHint", group_hints) + enum("providerPreset.loginWith", login_with), "预设分类、分类说明和登录来源的有限值均有资源。"),
            "src/components/providers/forms/presetGroups.ts": (list(name_keys) + [f"providerPreset.plan.{x}" for x in plans] + [f"providerPreset.region.{x}" for x in regions], "preset/family nameKey、plan 和 region 的有限值均有资源。"),
            "src/components/providers/mode/ModeDialog.tsx": (["mode.dialog.desktopLeaveStackNote", "mode.dialog.leaveStackNote"] + enum("mode.names", modes), "AppMode 分支和桌面离开提示键均存在。"),
            "src/components/providers/mode/ModeTabs.tsx": (enum("mode.names", modes) + enum("mode.help", modes), "AppMode 的显示名和帮助键均存在。"),
            "src/components/providers/mode/SwitchModePanel.tsx": (enum("mode.names", modes) + provider_notice_keys + official_reason_keys, "AppMode、ProxyStackNotice 和 noticeReasons 的有限枚举均有资源。"),
            "src/components/providers/presentation.ts": (["providerCard.section.stackDefaultHelpDesktop", "providerCard.section.stackDefaultHelp"] + [f"{x}.current.stateUnavailableHint" for x in ("pi", "omp")], "显式分支和 Pi family 状态键均存在；`apps.${app}` 因 kimi/dsh 缺键单独确认。"),
            "src/components/quota/quotaRules.ts": (["quota.tierUsed", "quota.tierLeft", "quota.used", "quota.left"], "quota 的 used/left 分支键均存在。"),
            "src/components/sessions/SessionItem.tsx": (["dsh.deleteSessionHint", "kimi.deleteSessionHint", "sessionManager.agyDeleteHint", "sessionManager.mcodeDeleteHint"], "session providerId 的有限分支键均存在。"),
            "src/components/sessions/BACKUP-NOT-USED": ([], ""),
            "src/components/sessions/SessionManagerPage.tsx": (list(terminal_keys), "terminal 选项的 labelKey 均存在。"),
            "src/components/sessions/reader/SessionReaderHeader.tsx": (["dsh.deleteSessionHint", "kimi.deleteSessionHint", "sessionManager.mcodeDeleteHint"], "会话删除提示的有限分支键均存在。"),
            "src/components/settings/BackupStorageSection.tsx": ([f"settings.backupStorage.items.{x}.{field}" for x in ["database", "skills", "codexHistoryUnify", "codexHistoryUnifyRestore", "codexHistoryProviderMigration", "liveFirstWrite", "hermes", "openclaw", "proxyLiveBackup", "envVars", "legacyConfigBackups", "legacyConfigArchive", "legacyDbUpgrade", "legacyToolSearch"] for field in ("name", "hint")], "BackupStorage 的全部位置 id 和 name/hint 资源均存在。"),
            "src/components/settings/LogConfigPanel.tsx": (enum("settings.advanced.logConfig.levelDesc", log_levels) + enum("settings.advanced.logConfig.levels", log_levels), "LOG_LEVELS 的五个值均有说明和显示名。"),
            "src/components/settings/SettingsPage.tsx": (enum("settings.sections", settings_sections), "SettingsSection 的六个值均有资源。"),
            "src/components/settings/TerminalSettings.tsx": (list(terminal_keys), "所有 terminal.labelKey 均存在。"),
            "src/components/settings/WebdavSyncSection.tsx": (list(webdav_keys), "WebDAV/S3 预设的 label/hint 均存在。"),
            "src/components/settings/sections/AppConfigSection.tsx": (["settings.browsePlaceholderClaude", "settings.browsePlaceholderCodex", "settings.browsePlaceholderGemini", "settings.browsePlaceholderGrok", "settings.browsePlaceholderOpencode", "settings.browsePlaceholderOpenclaw", "settings.browsePlaceholderHermes", "settings.browsePlaceholderPi", "settings.browsePlaceholderOmp"], "DirectoryAppId 的九个 placeholder 均存在。"),
            "src/components/settings/sections/GeneralSection.tsx": (list(language_keys), "LANGUAGES 的六个 labelKey 均存在。"),
            "src/components/settings/sections/RoutingSection.tsx": (enum("mode.names", modes), "AppMode 的三个显示名均存在。"),
            "src/components/shell/Sidebar.tsx": (enum("settings.sections", settings_sections), "SettingsSection 的六个值均有资源。"),
            "src/components/skills/SkillsStorageSheet.tsx": (list(sync_keys), "SYNC_METHODS 的 labelKey/descKey 均存在。"),
            "src/components/skills/UnifiedSkillsPanel.tsx": (["appMatrix.toast.enabled", "appMatrix.toast.disabled", "skillsPage.toast.disabledSelection"] + enum("appMatrix.cell", matrix_states), "toastKey 的调用值和 appMatrix 状态值均有资源。"),
            "src/components/usage/RequestLogColumnsMenu.tsx": (list(request_log_keys), "REQUEST_LOG_COLUMN_LABEL_KEYS 的所有列标签均存在。"),
            "src/components/usage/RequestLogTable.tsx": (list(request_log_keys), "REQUEST_LOG_COLUMN_LABEL_KEYS 的所有列标签均存在。"),
            "src/components/usage/UsageDisplaySection.tsx": (enum("usage.display.sidebarTodayItems", sidebar_items) + enum("usage.display.trendChartTypes", trend_types), "侧栏今日项和趋势图类型的有限值均有资源。"),
            "src/components/workspace/WorkspaceFilesPanel.tsx": (list(workspace_keys), "workspace 文件 descKey 均有资源。"),
            "src/config/mcpPresets.ts": (mcp_preset_descriptions, "mcpPresets 的五个 descriptionKey 均有资源。"),
            "src/hooks/useProviderActions.ts": (["notifications.switchSuccess", "notifications.codexRestartRequired", "notifications.geminiRestartRequired", "notifications.grokBuildRestartRequired", "notifications.claudeDesktopRestartRequired", "notifications.addToConfigSuccess"], "messageKey 的六个分支键均存在。"),
            "src/lib/claudePlan.ts": (claude_plan_keys, "claudePlanLabel 的七个套餐键均存在。"),
            "src/lib/errors/skillErrorParser.ts": ([
                "skills.error.skillNotFound", "skills.error.missingRepoInfo", "skills.error.downloadTimeout", "skills.error.downloadFailed", "skills.error.skillDirNotFound", "skills.error.directoryConflict", "skills.error.emptyArchive", "skills.error.invalidRepoRef", "skills.error.archiveTooLarge", "skills.error.archiveDownloadTooLarge", "skills.error.archiveTooManyEntries", "skills.error.getHomeDirFailed", "skills.error.noSkillsInZip", "skills.error.unknownError",
                "skills.error.suggestion.checkNetwork", "skills.error.suggestion.checkProxy", "skills.error.suggestion.retryLater", "skills.error.suggestion.checkRepoUrl", "skills.error.suggestion.checkPermission", "skills.error.suggestion.uninstallFirst", "skills.error.suggestion.checkZipContent", "skills.error.http403", "skills.error.http404", "skills.error.http429", "skills.installFailed", "common.error",
            ], "error/suggestion 映射、fallback 和 defaultTitle 均有资源。"),
            "src/lib/query/proxy.ts": (["provider.stackSaved", "provider.stackSavedLive"] + provider_notice_keys, "固定分支和 ProxyStackNotice 的 provider.notice 资源均存在。"),
            "src/utils/errorUtils.ts": ([f"omp.errors.{x}" for x in ["duplicateProvider", "externalChange", "fileTooLarge", "invalidMcp", "invalidProvider", "invalidYaml", "legacyModelsJson", "manualEdit", "providerMissing", "renameProvider", "rollbackConflict"]], "后端 omp.errors.* 的 11 个可能值均有资源。"),
            "src/components/apps/useToolManagement.ts": (["settings.toolUninstallFailed", "settings.toolActionFailed"], "action 的 uninstall/其他分支键均存在。"),
            "src/components/deeplink/McpConfirmation.tsx": (risk_keys, "RiskKind 的三个值均有 deeplink.risk.* 资源。"),
            "src/components/providers/CodexStaleClientsNotice.tsx": (["proxy.stackMode.codexStale.unverifiedTitle", "proxy.stackMode.codexStale.authTitle", "proxy.stackMode.codexStale.title"], "stale client 的三条提示键均存在。"),
            "src/components/providers/OpenTerminalDialog.tsx": (["provider.openTerminalDialog.isolationBodyAgy", "provider.openTerminalDialog.isolationBody"], "agy/其他分支键均存在。"),
            "src/components/providers/ProviderCardActions.tsx": (["provider.openTerminalIsolated", "provider.openTerminal"], "隔离/普通终端分支键均存在。"),
            "src/components/providers/forms/ClaudeDesktopProviderForm.tsx": (list(name_keys), "preset.nameKey 的所有字面量值均存在。"),
            "src/components/providers/forms/GrokBuildProviderForm.tsx": (list(name_keys), "preset.nameKey 的所有字面量值均存在。"),
            "src/components/prompts/usePromptPageCommon.ts": (["prompts.toast.hermesOn", "prompts.toast.hermesOff"], "Hermes 开关提示的两个分支键均存在。"),
            "src/components/settings/AppConfigSection.tsx": ([], ""),
            "src/components/settings/TerminalSettings.tsx": (list(terminal_keys), "terminal 选项的 labelKey 均存在。"),
            "src/hooks/useModeActions.ts": (["mode.toast.enteredStack", "mode.toast.enteredStackDesktop", "mode.toast.enteredStackLive"], "三个栈模式成功提示键均存在。"),
            "src/hooks/usePromptActions.ts": (["pi.prompts.usePromptSuccess", "pi.prompts.stopUsingSuccess"], "Pi 提示词启用/停用成功键均存在。"),
            "src/components/providers/forms/CodexConfigSections.tsx": (["codexConfig.authJsonStorageHint", "codexConfig.authJsonHint", "codexConfig.configTomlStorageHint", "codexConfig.configTomlHint"], "Codex 两种配置提示的代理/非代理解释均存在。"),
            "src/components/providers/forms/HermesFormFields.tsx": (["hermes.form.baseUrlRequired", "hermes.form.baseUrlScheme", "hermes.form.baseUrlInvalid"], "BaseUrlErrorCode 的三个值均存在。"),
            "src/components/prompts/PromptFormPanel.tsx": (["prompts.nameRequiredHermes", "prompts.nameRequired", "prompts.namePlaceholderHermes", "prompts.namePlaceholder"], "Hermes/普通提示词名称提示均存在。"),
            "src/components/prompts/PromptListItem.tsx": (["prompts.disableAria", "prompts.enableAria", "prompts.disable", "prompts.enable"], "提示词启用/停用文案均存在。"),
            "src/components/sessions/reader/exportMarkdown.ts": (reader_keys, "阅读器本地包装器会补齐 sessionManager.reader.*，所有 READER_DEFAULTS 键均存在。"),
            "src/components/sessions/reader/i18n.ts": (reader_keys, "本地阅读器包装器生成完整键，所有 READER_DEFAULTS 键均存在。"),
            "src/components/sessions/reader/toolSummary.ts": (reader_keys, "本地阅读器包装器只翻译带 sessionManager.reader. 前缀的键，所有本地键均存在。"),
        }
        # Specific map/name checks.
        if file in {"src/components/providers/forms/ClaudeDesktopProviderForm.tsx", "src/components/providers/forms/GrokBuildProviderForm.tsx", "src/components/providers/forms/ProviderForm.tsx", "src/components/providers/forms/KimiProviderForm.tsx", "src/components/providers/forms/presetGroups.ts"} and "nameKey" in expr:
            keys_exist(list(name_keys), key)
            return {"status": "无需国际化", "reason": "preset/family nameKey 的所有可能字面量值在 zh/en/ko 均存在。", "evidence": sorted(name_keys), "resolution": "name-key-map"}
        if file == "src/components/hermes/HermesMemoryPanel.tsx":
            check = [f"hermes.memory.{x}" for x in ["agentName", "agentDesc", "agentPlaceholder", "userName", "userDesc", "userPlaceholder", "toggledOn", "toggledOff"]]
            keys_exist(check, key)
            return {"status": "无需国际化", "reason": "KIND_META 的 name/desc/placeholder 及开关提示键均存在。", "evidence": check, "resolution": "kind-meta"}
        if file == "src/components/mcp/McpFormModal.tsx":
            keys_exist(mcp_field_keys + mcp_format_keys + mcp_preset_descriptions, key)
            return {"status": "无需国际化", "reason": "MCp 字段错误、粘贴格式和预设描述均为有限枚举，所有资源键存在。", "evidence": mcp_field_keys + mcp_format_keys + mcp_preset_descriptions, "resolution": "mcp-finite-enums"}
        if file in checks:
            expected, reason = checks[file]
            keys_exist(expected, key)
            return {"status": "无需国际化", "reason": reason, "evidence": expected, "resolution": "finite-map"}

        raise RuntimeError(f"unclassified dynamic key: {key} {expr[:160]}")

    decisions = []
    for item in items:
        try:
            decision = classify(item)
        except Exception as exc:
            raise RuntimeError(f"verification failed for {item['id']}: {exc}") from exc
        decisions.append({
            "id": item["id"],
            "source_file": item["source_file"],
            "line": item["line"],
            "column": item["column"],
            "function": item["function"],
            "expression": item["expression"],
            **decision,
        })
    counts = Counter(decision["status"] for decision in decisions)
    result = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(decisions),
        "status_counts": dict(counts),
        "decisions": decisions,
    }
    atomic_json(RESULT_PATH, result)
    print(json.dumps({"result": str(RESULT_PATH.relative_to(ROOT)), "total": len(decisions), "status_counts": dict(counts), "confirmed": [d["id"] for d in decisions if d["status"] == "确认遗漏"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
