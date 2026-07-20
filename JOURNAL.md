## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/72

**Issue title:** Add a bias audit report that runs over a sample of stored reviews

**Tier:** [x] Tier 2

**Problem summary:**
The pathreview app has a bias detector (`safety/bias_detector.py`) that analyzes reviews for demographic bias signals, but there is no tooling to audit its performance at scale. Issue #72 asks for an offline script (`scripts/audit_bias.py`) that samples 100 stored reviews from the database, runs them through the bias detector with detailed logging, and produces a report showing false positive and false negative rates by demographic signal. A successful fix would give maintainers a repeatable way to measure and track the bias detector's accuracy over time.

**Branch name:** feat/72-bias-audit-report

**Setup confirmation:** [x] App runs locally at localhost:5173

**Cohort ledger:** [ ] Issue added to cohort ledger