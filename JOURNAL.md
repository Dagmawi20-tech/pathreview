## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/72

**Issue title:** Add a bias audit report that runs over a sample of stored reviews

**Tier:** [x] Tier 2

**Problem summary:**
The pathreview app has a bias detector (`safety/bias_detector.py`) that analyzes reviews for demographic bias signals, but there is no tooling to audit its performance at scale. Issue #72 asks for an offline script (`scripts/audit_bias.py`) that samples 100 stored reviews from the database, runs them through the bias detector with detailed logging, and produces a report showing false positive and false negative rates by demographic signal. A successful fix would give maintainers a repeatable way to measure and track the bias detector's accuracy over time.

**Branch name:** feat/72-bias-audit-report

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [ ] Issue added to cohort ledger

## Week 8 — Reproduction & solution planning

**Reproduction commit link:** https://github.com/Dagmawi20-tech/pathreview/commit/0ec6c3b

**Reproduction summary:**
Created `scripts/audit_bias.py` as a stub that raises `NotImplementedError`, confirming the script does not exist. Running `python scripts/audit_bias.py` produces the error, proving the gap described in issue #72 — `BiasDetector` is implemented but never called in a batch context.

**PLAN.md link:** https://github.com/Dagmawi20-tech/pathreview/blob/feat/72-bias-audit-report/PLAN.md

**Walkthrough video (recommended):** N/A

**Blockers or open questions:**
The seeded reviews use placeholder content that won't trigger any bias patterns, so verifying the script works correctly will require injecting synthetic reviews with known-biased text. Need to confirm the best approach for this — either add test fixtures in the script itself or insert them via the DB directly.

**Pre-existing test failures noted:**
Running `make test-unit` before starting implementation shows 53 pre-existing
failures across multiple files unrelated to issue #72. Of note: 9 tests in
`test_bias_detector.py` already fail because the existing regex patterns in
`safety/bias_detector.py` are too narrow — phrases like "bootcamp graduates
can't write production code" and "young developers can't handle complex systems"
are not caught. These failures exist before any changes and will be documented
in the PR. My changes will not introduce any new failures.

## Week 9 — Solution building & PR submission

### Check-in 1 (mid-week)

**Current progress:**
Implemented `scripts/audit_bias.py` — samples up to 100 completed reviews from
the database, runs each through `BiasDetector`, categorizes flags by signal type
(dismissive education vs demographic assumption), and prints a structured report.
Added synthetic fixtures for detector validation. 27 unit tests written and passing.

**Next steps:**
Open PR, write PR description, finalize JOURNAL.md.

**Blockers:**
None.

---

### Check-in 2 (end of week)

**PR link:** [paste PR link after opening]

**Branch:** `feat/72-bias-audit-report`

**What you built:**
`scripts/audit_bias.py` — an offline bias audit script that samples up to 100
completed reviews from the database, runs each through `BiasDetector` with detailed
structlog logging, and produces a report showing flag rates broken down by demographic
signal type. Includes synthetic test fixtures to verify the detector is working even
when seeded reviews contain only placeholder content.

**Tests added or updated:**
`tests/unit/test_audit_bias.py` — 27 tests covering `extract_text_from_review`,
`run_synthetic_validation`, `audit_reviews`, and `compute_report`. All pass.

**Self-review confirmation:** [x] make check passes (182 pre-existing errors, 0 new)  [x] make test-unit passes (53 pre-existing failures, 0 new)

**Draft PR feedback received from:** none