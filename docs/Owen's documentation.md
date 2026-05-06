# Group Project Work Summary - Task Tracker Application

## Overview
Contributions to the Task Tracker application including feature implementation, test automation, and documentation across multiple sprints.

---

## Time Service Integration 

### Implementation
- Added `TimeService` class with external API integration (WorldTimeAPI)
- Implemented fallback to system time when external API unavailable
- Created `/api/time` endpoint and `/time` UI page
- Injected `TimeService` into Flask app using dependency injection

### Tests Added
- **Unit tests** (`tests/unit/time/test_time_unit.py`)
  - Mocked time service testing
- **Integration tests** (`tests/integration/api/test_sprint2_pr7_time_api.py`)
  - Real API endpoint validation
  - Response structure verification
- **UI tests** (`tests/e2e/ui/playwright/pytest/test_time_ui.py`)
  - Page loads correctly
  - Time display validation
  - Navigation to time page

### Documentation
- Created `docs/sprint2/time_service_test_report.md`
- Screenshots of API responses and UI views

---

## Priority Feature Implementation (Sprint 3)

### Implementation
- Added `priority` field to Task model (values: `low`, `medium`, `high`)
- Updated `TaskService.add_task()` to accept priority parameter
- Modified API route to validate priority (required field, no default)
- Added priority display in `task_list.html` with CSS styling

### Tests Added

#### Unit Tests (`tests/unit/test_task_priority.py`)
| Test | Description |
|------|-------------|
| `test_add_task_with_low_priority` | Verify low priority assignment |
| `test_add_task_with_medium_priority` | Verify medium priority assignment |
| `test_add_task_with_high_priority` | Verify high priority assignment |
| `test_add_task_without_description` | Priority works without description |
| `test_add_task_invalid_priority_raises_error` | Invalid values raise ValueError |
| `test_get_tasks_include_priority_field` | GET requests include priority |
| `test_get_tasks_sorted_by_priority_ascending` | Sort order validation |

#### API Tests (`tests/api/test_tasks_priority_api.py`)
| Test | Description |
|------|-------------|
| `test_post_task_with_low_priority` | POST with low priority |
| `test_post_task_with_medium_priority` | POST with medium priority |
| `test_post_task_with_high_priority` | POST with high priority |
| `test_post_task_missing_priority_returns_400` | Missing priority → 400 error |
| `test_post_task_empty_string_priority_returns_400` | Empty priority → 400 error |
| `test_post_task_invalid_priority_returns_error` | Invalid priority → Exception/500 |
| `test_get_tasks_include_priority_field` | GET returns priority field |
| `test_tasks_returned_in_insertion_order` | Order by insertion (not priority) |

## Documentation Created

| File | Content |
|------|---------|
|`docs/sprint3/sprint3_test_expansion.md` | Details expanded test coverage for feature: task priority |
|`docs/sprint3/images/all_api_tests_pass.png` |
|`docs/sprint3/images/all_priorities_api.png` |
|`docs/sprint3/images/high_priority_api_pass.png` |
|`docs/sprint3/images/low_priority_api_pass.png` |
|`docs/sprint3/images/medium_priority_api_pass.png` |
|`docs/sprint3/images/test_task_priority_pass.png` |
|`docs/sprint3/images/ui_priority_pass.png` |


---

## Delete Confirmation Feature (Sprint 2)

### Tests Added (`tests/e2e/ui/playwright/pytest/test_delete_confirmation.py`)
| Test | Description |
|------|-------------|
| `test_delete_confirmation_cancel_keeps_task` | Cancel does NOT delete task |
| `test_delete_confirmation_confirm_deletes_task` | Confirm DOES delete task |
| `test_delete_confirmation_dialog_text` | Dialog shows correct message |

### Key Implementation Note
- Delete confirmation uses `onsubmit="return confirm(...)"` in HTML
- Tests use Playwright's dialog handler (`page.on("dialog")`)

---

## Documentation Created

| File | Content |
|------|---------|
| `docs/sprint2/time_service_test_report.md` | TimeService test results and screenshots |
| `docs/sprint2/images/manual-time-curl.png` | Manual API test screenshot |
| `docs/sprint2/images/api-time-pass.png` | API test results |
| `docs/sprint2/images/ui-time-pass.png` | UI test results |
| `docs/sprint2/images/time-page.png` | View of functional time page| 


---

## CI/CD Contributions

### GitHub Actions
- Updated CI workflow for priority feature testing
- Debugged and resolved failing CI checks
- Handled environment-specific test failures (local vs CI)

### Key Debugging Challenges Resolved
1. **Database schema mismatch** - Added priority column to database
2. **Empty string handling** - Explicit check for `priority == ""`
3. **Error message matching** - Aligned messages with test expectations
4. **Conflicting test requirements** - Team alignment on priority as required field
5. **Windows vs Linux path differences** - Cross-platform compatibility

---

## Pull Requests Created

| PR # | Title | Status |
|------|-------|--------|
| #37 | test: add priority feature test coverage (unit, API, UI) | ✅ Merged |
| #34 | Feature/time tests: add TimeService API and UI tests | ✅ Merged |
| #37 | docs: add priority feature test summary | ✅ Merged |
| #28 | Add delete confirmation feature (PR-6) | ✅ Merged |

---

## Test Execution Summary

| Test Category | Files | Tests | Status |
|---------------|-------|-------|--------|
| Unit Tests | `test_task_priority.py`, `test_time_*.py` | 10+ | ✅ Passing |
| API Tests | `test_tasks_priority_api.py`, `test_sprint2_pr7_time_api.py` | 10+ | ✅ Passing |
| UI Tests | `test_delete_confirmation.py`, `test_time_ui.py` | 7 | ✅ Passing |

---

## Skills Demonstrated

| Skill | Application |
|-------|-------------|
| **Test-Driven Development** | Wrote tests before/alongside implementation |
| **API Testing** | Created endpoint tests with validation |
| **UI Automation** | Playwright tests with dialog handling |
| **CI/CD Debugging** | Resolved environment-specific failures |
| **Git Workflow** | Feature branches, PRs, merging |
| **Documentation** | Test reports, markdown summaries |
| **External API Integration** | TimeService with fallback logic |

---

## Key Takeaways

1. **Empty strings need explicit handling** - `if priority == ""` catches empty strings
2. **Local vs CI differences** - Environment matters for test behavior
3. **Test alignment** - Conflicting tests reveal need for requirement clarity
4. **Documentation matters** - Test summaries help team understand coverage

