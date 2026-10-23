# 韩语翻译审查

本分支包含韩语国际化、逐条审查后的译文和中韩对照页。

## 在其他机器上打开

克隆此分支后，用浏览器打开 `docs/i18n/ko-zh-review.html`：

```sh
git clone --branch codex/korean-localization --single-branch https://github.com/cuiyf5516/cc-switch.git
```

也可以在 GitHub 的此分支页面选择 **Code → Download ZIP**，解压后打开同一文件。请保留同目录的 `ko-review-controls.js`，标记功能需要它。无需安装项目依赖或运行应用。

GitHub 的文件预览不会运行 HTML 中的交互功能。只想阅读文本时，可查看 [Markdown 对照](ko-zh-review.md) 和 [审查说明](ko-review-notes.md)。

## 标记与跨机器转移

在对照页右侧勾选“待复审”并添加备注，审查完成后点击“导出待复审 JSON”，将文件交给助手进行二次审查。

标记保存在各机器的浏览器本地存储中，不随 Git 自动同步。换机器前请导出 JSON，在另一台机器的对照页中点击“导入标记 JSON”恢复。浏览器提示无法本地保存时，请在离开页面前导出。

[逐条审计记录](ko-review-audit.json) 记录的是 LLM 对译文的审查结果，与用户在浏览器中添加的复审标记分别保存。
