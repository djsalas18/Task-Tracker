# PR-7 Final Regression Plan

Sprint 4 — Sub-Issue 1: Final Regression Testing (PR-7)

Goal
- Verify that all implemented features operate correctly before final submission.
- Confirm full unit, integration, UI, and acceptance regression coverage for new and existing functionality.

Scope
- Add Task
- Update Task
- Delete Task
- Task Report
- Time API endpoint
- Sprint 2 feature(s)
- Sprint 3 feature(s)

Validation Criteria
- Automated tests pass (unit, integration, UI, acceptance)
- UI workflows function correctly (manual/automated validation)
- No regressions introduced compared to baseline

How to run (Windows PowerShell)
1. Activate project virtual environment.

```powershell
$env:TESTING='true'
& ".venv\Scripts\Activate.ps1"
```

2. Run core regression (API + unit + integration):

```powershell
pytest tests/api tests/unit tests/integration -q --maxfail=1
```

3. Run UI regression (Playwright + Selenium):

```powershell
pytest tests/e2e/ui/playwright/pytest -q
pytest tests/e2e/ui/selenium/pytest -q
```

4. Run acceptance tests (Robot / BDD):

```powershell
pytest tests/e2e/acceptance/bdd_playwright -q
robot tests/e2e/acceptance/robot/tests/task_workflow.robot
```

Interpreting results
- All suites should exit with code 0 and no FAILED tests.
- If tests fail, capture the failing test file and exact assertion/traceback.
- Classify failures: environment/setup vs functional regression.

Remediation steps (when failures occur)
1. Reproduce failing test locally and capture logs/screenshots (UI).
2. If environment-related (DB schema, TESTING env var), reset DB using `test_helpers/db_reset_helper.py` or remove stale `tasks.db`.
3. If functional regression, create a small failing test branch and open PR with fix + regression tests.

Artifacts to collect
- `test-results/` folder with HTML reports and screenshots
- `htmlcov/` coverage report
- pytest log with `-q` output and failing tracebacks

Notes
- Tests in this repo use `TESTING=true` to select an isolated temp database. Ensure the environment variable is set before running UI tests that start a live server.
- Playwright tests run headless in CI by default; for local debugging, set `HEADLESS=false`.
