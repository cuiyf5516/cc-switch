import fs from "node:fs";
import path from "node:path";
import ts from "typescript";
import crypto from "node:crypto";

const listPath = process.argv[2];
const outputPath = process.argv[3];
const fileList = JSON.parse(fs.readFileSync(listPath, "utf8"));
const candidates = [];
const translationRefs = [];
const dynamicTranslationRefs = [];
const sourceFiles = [];

const UI_ATTRS = new Set(["placeholder", "title", "aria-label", "aria-description", "alt", "label"]);
const I18N_CALLEES = new Set(["t", "$t", "translate", "formatMessage"]);
const NON_UI_PROPS = new Set([
  "className", "class", "id", "key", "name", "type", "role", "href", "src", "to", "target",
  "rel", "data-testid", "data-test", "aria-hidden", "value", "defaultValue", "style",
  "accept", "method", "action", "autoComplete", "inputMode", "lang", "dir"
]);

function sha(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}

function sourceName(node) {
  let current = node;
  while (current) {
    if (ts.isFunctionDeclaration(current) && current.name) return current.name.text;
    if (ts.isMethodDeclaration(current) && current.name) return current.name.getText();
    if (ts.isVariableDeclaration(current) && ts.isIdentifier(current.name)) return current.name.text;
    if (ts.isPropertyDeclaration(current) && current.name) return current.name.getText();
    if (ts.isClassDeclaration(current) && current.name) return current.name.text;
    current = current.parent;
  }
  return "<module>";
}

function propertyName(node) {
  if (!node) return null;
  if (ts.isPropertyAssignment(node) || ts.isPropertyDeclaration(node) || ts.isPropertySignature(node)) {
    return node.name?.getText() ?? null;
  }
  if (ts.isJsxAttribute(node)) return node.name?.getText() ?? null;
  return null;
}

function contextFor(node) {
  const chain = [];
  let current = node.parent;
  while (current && chain.length < 5) {
    const prop = propertyName(current);
    if (prop) chain.push(prop);
    if (ts.isCallExpression(current) && current.expression) {
      chain.push(`call:${current.expression.getText().slice(0, 100)}`);
    }
    current = current.parent;
  }
  return { function: sourceName(node), properties: chain.reverse(), parent_kind: ts.SyntaxKind[node.parent?.kind ?? 0] };
}

function isTranslationCall(node) {
  if (!ts.isCallExpression(node)) return false;
  const expr = node.expression;
  if (ts.isIdentifier(expr) && I18N_CALLEES.has(expr.text)) return true;
  if (ts.isPropertyAccessExpression(expr) && (expr.name.text === "t" || I18N_CALLEES.has(expr.name.text))) return true;
  return false;
}

function insideTranslationArgument(node) {
  let current = node;
  while (current.parent) {
    const parent = current.parent;
    if (isTranslationCall(parent) && parent.arguments.includes(current)) return true;
    if (ts.isPropertyAssignment(parent) && parent.name?.getText() === "defaultValue") return true;
    if (current !== node && ts.isStatement(parent)) break;
    current = parent;
  }
  return false;
}

function uiAttribute(node) {
  let current = node;
  while (current.parent) {
    const parent = current.parent;
    if (ts.isJsxAttribute(parent) && parent.name && UI_ATTRS.has(parent.name.getText())) return parent.name.getText();
    if (ts.isJsxElement(parent) || ts.isJsxSelfClosingElement(parent)) return null;
    current = parent;
  }
  return null;
}

function candidateKind(node) {
  if (ts.isJsxText(node)) return "jsx_text";
  if (ts.isJsxAttribute(node)) return "jsx_attribute";
  if (ts.isTemplateExpression(node) || ts.isNoSubstitutionTemplateLiteral(node)) return "template";
  return "string";
}

function naturalText(value) {
  const text = value.trim();
  if (!text) return false;
  if (/[\u3400-\u9fff\uac00-\ud7af]/.test(text)) return true;
  if (!/[A-Za-z]/.test(text)) return false;
  if (text.length < 2) return false;
  if (/^(?:https?:|data:|mailto:|file:|\/|\.\/|\.\.\/|#)/i.test(text)) return false;
  if (/^[A-Za-z0-9_$.-]+$/.test(text) && !/[A-Z].*[A-Z]/.test(text)) return false;
  if (/^[a-z0-9-]+(?:\s+[a-z0-9-]+)*$/.test(text) && text.split(/\s+/).length < 3) return false;
  if (/^(?:[0-9.%+\-*/()\s]+|[a-z][a-z0-9-]*:[a-z0-9.#-]+)$/i.test(text)) return false;
  return /\s/.test(text) || /[.!?:…]$/.test(text) || /[A-Z][a-z]+[A-Z]/.test(text);
}

function addCandidate(node, value, kind) {
  const trimmed = value.trim();
  if (!trimmed || insideTranslationArgument(node)) return false;
  const attr = uiAttribute(node);
  if (!attr && !naturalText(trimmed)) return false;
  const sf = node.getSourceFile();
  const pos = sf.getLineAndCharacterOfPosition(node.getStart(sf));
  const rel = path.relative(process.cwd(), sf.fileName).replaceAll("\\", "/");
  const digest = sha(trimmed).slice(0, 16);
  const context = contextFor(node);
  const chain = context.properties.join(" > ");
  const machineContexts = ["className", "queryKey", "contentType", "mimeType", "data-testid", "href", "src", "model > id", "models > name"];
  if (!attr && machineContexts.some(part => chain.includes(part))) return false;
  const callContext = context.properties.find(value => value.startsWith("call:")) ?? "";
  const userCall = /(?:toast|message|confirm|alert|notify|notification|dialog|modal|warning|error)/i.test(callContext);
  if (!attr && ts.isStringLiteralLike(node) && !/[㐀-鿿가-힯]/.test(trimmed) && !userCall) {
    // Plain English internal identifiers without a UI sink are not candidates.
    if (!/[.!?:…]$/.test(trimmed) && trimmed.split(/\s+/).length < 3) return false;
  }
  candidates.push({
    id: `hardcoded:${rel}:${context.function}:${pos.line + 1}:${digest}`,
    source_file: rel,
    line: pos.line + 1,
    column: pos.character + 1,
    expression: trimmed,
    raw_expression: value,
    content_fingerprint: sha(value),
    source_kind: kind,
    ui_attribute: attr,
    function: context.function,
    property_chain: context.properties,
    parent_kind: context.parent_kind,
    status: "未审核",
  });
  return true;
}

for (const file of fileList) {
  const rel = file.replaceAll("\\", "/");
  const abs = path.resolve(file);
  try {
    const text = fs.readFileSync(abs, "utf8");
    const kind = rel.endsWith(".tsx") ? ts.ScriptKind.TSX : ts.ScriptKind.TS;
    const sf = ts.createSourceFile(rel, text, ts.ScriptTarget.Latest, true, kind);
    const diagnostics = sf.parseDiagnostics.map(d => ts.flattenDiagnosticMessageText(d.messageText, "\n"));
    let fileCandidates = 0;
    function visit(node) {
      if (isTranslationCall(node)) {
        const first = node.arguments[0];
        const pos = sf.getLineAndCharacterOfPosition(node.getStart(sf));
        if (first && (ts.isStringLiteral(first) || ts.isNoSubstitutionTemplateLiteral(first))) {
          const options = node.arguments[1];
          let defaultValue = null;
          if (options && ts.isObjectLiteralExpression(options)) {
            for (const prop of options.properties) {
              if (ts.isPropertyAssignment(prop) && prop.name?.getText() === "defaultValue") {
                const initializer = prop.initializer;
                if (ts.isStringLiteral(initializer) || ts.isNoSubstitutionTemplateLiteral(initializer)) defaultValue = initializer.text;
              }
            }
          }
          translationRefs.push({
            source_file: rel, line: pos.line + 1, column: pos.character + 1,
            key: first.text, default_value: defaultValue,
            function: sourceName(node), expression: node.getText(sf).slice(0, 500),
          });
        } else if (first) {
          dynamicTranslationRefs.push({
            source_file: rel, line: pos.line + 1, column: pos.character + 1,
            expression: first.getText(sf).slice(0, 500), function: sourceName(node),
            reason: "first translation argument is not a string literal",
          });
        }
      }
      if (ts.isJsxText(node)) {
        if (addCandidate(node, node.getText(sf), "jsx_text")) fileCandidates++;
      } else if (ts.isStringLiteral(node) || ts.isNoSubstitutionTemplateLiteral(node)) {
        if (addCandidate(node, node.text, candidateKind(node))) fileCandidates++;
      } else if (ts.isTemplateExpression(node)) {
        if (addCandidate(node, node.getText(sf), "template")) fileCandidates++;
      }
      ts.forEachChild(node, visit);
    }
    visit(sf);
    sourceFiles.push({ path: rel, language: "typescript", status: "scanned", bytes: Buffer.byteLength(text), candidate_count: fileCandidates, parse_errors: diagnostics });
  } catch (error) {
    sourceFiles.push({ path: rel, language: "typescript", status: "failed", bytes: 0, candidate_count: 0, parse_errors: [String(error)] });
  }
}

fs.writeFileSync(outputPath, JSON.stringify({ candidates, translationRefs, dynamicTranslationRefs, sourceFiles }, null, 2));
console.log(JSON.stringify({ files: sourceFiles.length, candidates: candidates.length, translation_refs: translationRefs.length, dynamic_refs: dynamicTranslationRefs.length }));
