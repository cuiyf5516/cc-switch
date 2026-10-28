# Korean i18n audit workspace

This directory contains a reproducible, resumable audit of:

- Existing Korean translations in JSON, native tray/panel code, and backend inline messages.
- User-visible production strings that bypass the i18n system.

No project-owned source, locale, dependency, or configuration file is modified by these tools.

## Commands

```powershell
python .i18n-audit/scripts/extract.py
python .i18n-audit/scripts/plan_batches.py
python .i18n-audit/scripts/scan_hardcoded.py
python .i18n-audit/scripts/plan_hardcoded_batches.py
python .i18n-audit/scripts/apply_scope_exclusions.py
python .i18n-audit/scripts/apply_candidate_exclusions.py
python .i18n-audit/scripts/apply_reviews.py .i18n-audit/reviews/decisions-EXAMPLE.json
python .i18n-audit/scripts/review_hardcoded.py
python .i18n-audit/scripts/verify.py
python .i18n-audit/scripts/generate_report.py
```

All generated state is under `.i18n-audit/`. `verify.py` exits non-zero while required records are incomplete or stale.

## Latest audit state

- Existing translation resources: 4,448 / 4,448 reviewed.
- Translation batches: 158 / 158 complete.
- Translation outcomes: 3 must-fix, 79 suggested changes, 4 pending verification, 4,362 keep.
- Production source files: 801 scanned, 0 failed, 27 excluded (26 test/non-production files plus the Chinese-only `deplink.html` scope exclusion).
- Hardcoded candidates: 4,426 reviewed; 535 confirmed omissions, 1,256 pending verification, 2,635 no-i18n.
- Dynamic translation keys: 162 registered and reviewed as pending runtime-key risks.
- Second round: 655 keep samples plus all 86 translation issues; 535 confirmed and 1,256 pending hardcoded candidates rechecked; 396 no-i18n samples checked.
- Scope exclusion: `deplink.html` is intentionally excluded from Korean i18n review because it is a standalone Simplified-Chinese-only page by product decision.
- Candidate-category exclusion: 262 `backend_localized_error` items are deliberately treated as no-i18n because they already implement Chinese/English bilingual errors.

## Human review and repair handoff

- Translation decisions: `.i18n-audit/reviews/human-review/translation_review_decisions.csv`
- Internationalization-gap decisions: `.i18n-audit/reviews/human-review/missing_i18n_review_decisions.csv`
- Approved repair plan: `.i18n-audit/reviews/human-review/repair_plan.csv`
- Review instructions: `.i18n-audit/reviews/human-review/README.md`

After filling the human decisions, run:

```powershell
python .i18n-audit/scripts/build_repair_plan.py
```

Only rows marked `采纳`, `修改后采纳`, or `确认修复` are exported to the repair plan.

