# PR-7 Traceability Matrix

This document maps PR-7 features to the automated tests that validate them.

Feature -> Test Coverage
- Add Task:
  - Unit: tests/unit/tasks/test_add_task.py
  - Integration/API: tests/integration/api/test_add_task_api.py
  - UI: tests/e2e/ui/playwright/pytest/test_playwright_pytest.py

- Update Task:
  - Unit: tests/unit/tasks/test_task_service_get.py
  - Integration/API: tests/integration/api/test_tasks_api.py
  - UI: tests/e2e/ui/playwright/pytest/test_priority_ui.py

- Delete Task:
  - Unit: tests/unit/tasks/test_delete_task.py
  - Integration/API: tests/integration/api/test_tasks_api.py
  - UI: tests/e2e/ui/playwright/pytest/test_delete_confirmation.py

- Task Report:
  - Integration: tests/integration/api/test_tasks_api.py
  - UI: templates/report.html (manual/visual verification)

- Time API endpoint:
  - Unit: tests/unit/time/test_time_unit.py
  - Integration: tests/integration/api/test_sprint2_pr7_time_api.py
  - UI: tests/e2e/ui/playwright/pytest/test_time_ui.py

- Sprint 2 feature(s):
  - Integration: tests/integration/api/test_sprint2_pr7_task_api_errors.py

- Sprint 3 feature(s):
  - See: tests/integration/test_sprint2_pr7_five_core_regression.py

Notes
- When a test is failing, assign to the responsible developer with failing test name and traceback.
- Use `docs/sprint4/PR-7_regression_plan.md` to run the full regression locally and on CI.
