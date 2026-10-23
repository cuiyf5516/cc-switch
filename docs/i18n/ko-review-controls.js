/* Local annotations for the Korean translation review; no network requests. */
(() => {
  const storageKey = "cc-switch:ko-review:annotations:v1";
  const format = "cc-switch-korean-review/v1";
  const search = document.querySelector("#q");
  const changed = document.querySelector("#changed");
  const count = document.querySelector("#count");
  const rows = [...document.querySelectorAll("tbody tr")];
  const text = (cell) => {
    const copy = cell.cloneNode(true);
    copy.querySelectorAll("br").forEach((br) => br.replaceWith("\n"));
    return copy.textContent;
  };
  let annotations = Object.create(null);
  let storageWorks = true;
  let message = "";
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || "{}");
    if (saved && typeof saved === "object" && !Array.isArray(saved)) {
      for (const [key, value] of Object.entries(saved)) {
        if (value && typeof value.pending === "boolean" && typeof value.note === "string") {
          annotations[key] = value;
        }
      }
    }
  } catch {
    storageWorks = false;
  }

  const toolbar = document.createElement("section");
  toolbar.className = "review-toolbar";
  toolbar.setAttribute("aria-label", "复审标记工具");
  toolbar.innerHTML = `<label><input type="checkbox" id="pending-only">只看待复审</label>
    <button type="button" id="export-review">导出待复审 JSON</button>
    <button type="button" id="import-review">导入标记 JSON</button>
    <input type="file" id="import-file" accept=".json,application/json" hidden>
    <span id="review-status" role="status" aria-live="polite"></span>
    <p>勾选右侧“待复审”，可填写原因或建议。填写备注会自动勾选。标记保存在当前浏览器；导出的 JSON 可交给我二次审查，也可导入恢复。导出不受当前筛选影响。</p>`;
  count.before(toolbar);
  const pendingOnly = toolbar.querySelector("#pending-only");
  const exportButton = toolbar.querySelector("#export-review");
  const importButton = toolbar.querySelector("#import-review");
  const fileInput = toolbar.querySelector("#import-file");
  const status = toolbar.querySelector("#review-status");
  const header = document.createElement("th");
  header.textContent = "你的复审标记";
  document.querySelector("thead tr").append(header);
  const entries = rows.map((row) => {
    const [key, zh, ko, en] = [...row.cells].slice(0, 4).map(text);
    const cell = row.insertCell();
    cell.className = "annotation-cell";
    const label = document.createElement("label");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.setAttribute("aria-label", `待复审 ${key}`);
    label.append(checkbox, "待复审");
    const noteButton = document.createElement("button");
    noteButton.type = "button";
    noteButton.textContent = "添加备注";
    noteButton.setAttribute("aria-label", `编辑备注 ${key}`);
    noteButton.setAttribute("aria-expanded", "false");
    cell.append(label, noteButton);
    const entry = { row, key, zh, ko, en, checkbox, cell, noteButton, textarea: null };
    entry.searchText = `${key}\n${zh}\n${ko}\n${en}`.toLowerCase();
    checkbox.addEventListener("change", () => {
      update(entry, checkbox.checked, annotations[key]?.note || "");
    });
    noteButton.addEventListener("click", () => {
      showNote(entry);
      entry.textarea.focus();
    });
    return entry;
  });
  const byKey = new Map(entries.map((entry) => [entry.key, entry]));

  function showNote(entry) {
    if (entry.textarea) return;
    const area = document.createElement("textarea");
    area.rows = 4;
    area.maxLength = 20000;
    area.placeholder = "疑问、使用场景或建议译法…";
    area.setAttribute("aria-label", `复审备注 ${entry.key}`);
    area.value = annotations[entry.key]?.note || "";
    area.addEventListener("input", () => {
      update(entry, area.value.trim() ? true : entry.checkbox.checked, area.value);
    });
    entry.cell.append(area);
    entry.textarea = area;
    entry.noteButton.textContent = "备注";
    entry.noteButton.setAttribute("aria-expanded", "true");
  }

  function renderEntry(entry) {
    const saved = annotations[entry.key];
    entry.checkbox.checked = saved?.pending === true;
    entry.row.classList.toggle("needs-review", entry.checkbox.checked);
    if (saved?.note) showNote(entry);
    if (entry.textarea) entry.textarea.value = saved?.note || "";
  }

  function persist() {
    try {
      localStorage.setItem(storageKey, JSON.stringify(annotations));
      storageWorks = true;
    } catch {
      storageWorks = false;
    }
  }

  function update(entry, pending, note) {
    if (pending || note) {
      annotations[entry.key] = { pending, note, updatedAt: new Date().toISOString() };
    } else {
      delete annotations[entry.key];
    }
    renderEntry(entry);
    persist();
    message = "";
    filter();
  }

  function filter() {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    let pending = 0;
    for (const entry of entries) {
      const saved = annotations[entry.key];
      if (saved?.pending) pending++;
      entry.row.hidden = (query && !`${entry.searchText}\n${saved?.note || ""}`.toLowerCase().includes(query)) ||
        (changed.checked && entry.row.dataset.changed !== "true") ||
        (pendingOnly.checked && !saved?.pending);
      if (!entry.row.hidden) visible++;
    }
    count.textContent = `显示 ${visible} / ${entries.length} 条 · 待复审 ${pending} 条`;
    exportButton.disabled = pending === 0;
    status.textContent = message || (storageWorks ? "标记已自动保存在当前浏览器" : "当前浏览器无法本地保存，请及时导出 JSON，以免标记丢失");
  }

  exportButton.addEventListener("click", () => {
    const selected = entries.filter((entry) => annotations[entry.key]?.pending);
    if (!selected.length) return;
    const payload = {
      format,
      base: "e5b04221",
      locale: "ko",
      exportedAt: new Date().toISOString(),
      entries: selected.map(({ key, zh, ko, en }) => ({
        key, zh, ko, en, note: annotations[key].note,
        pending: true, updatedAt: annotations[key].updatedAt,
      })),
    };
    const url = URL.createObjectURL(new Blob([JSON.stringify(payload, null, 2) + "\n"], { type: "application/json;charset=utf-8" }));
    const link = document.createElement("a");
    link.href = url;
    link.download = `ko-review-requests-${new Date().toISOString().slice(0, 10)}.json`;
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 30000);
    message = `已发起导出 ${selected.length} 条待复审标记，请确认下载已完成`;
    filter();
  });

  importButton.addEventListener("click", () => fileInput.click());
  fileInput.addEventListener("change", async () => {
    const file = fileInput.files?.[0];
    if (!file) return;
    try {
      if (file.size > 10 * 1024 * 1024) throw new Error("文件超过 10 MB");
      const payload = JSON.parse(await file.text());
      if (payload?.format !== format || payload.locale !== "ko" || !Array.isArray(payload.entries)) {
        throw new Error("请选择本页导出的韩语复审 JSON");
      }
      const incoming = [];
      let skipped = 0;
      for (const item of payload.entries) {
        if (!item || typeof item.key !== "string" || typeof item.note !== "string" || item.note.length > 20000) {
          throw new Error("条目缺少翻译键或备注格式不正确");
        }
        if (!byKey.has(item.key)) { skipped++; continue; }
        incoming.push(item);
      }
      for (const item of incoming) {
        annotations[item.key] = { pending: true, note: item.note, updatedAt: new Date().toISOString() };
        renderEntry(byKey.get(item.key));
      }
      persist();
      message = `已合并导入 ${incoming.length} 条标记${skipped ? `；跳过 ${skipped} 个本页不存在的翻译键` : ""}${!storageWorks ? "；本地保存失败，请保留导出文件" : ""}`;
    } catch (error) {
      message = `导入失败：${error.message}`;
    }
    fileInput.value = "";
    filter();
  });

  entries.forEach(renderEntry);
  search.addEventListener("input", filter);
  changed.addEventListener("change", filter);
  pendingOnly.addEventListener("change", filter);
  filter();
})();
