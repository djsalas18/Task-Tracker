# 🧪 Group Project Test Plan

This test strategy describes the testing approach established during Sprints 1–4 of the Task Tracker project. It outlines the different levels of testing used to validate the system, including unit testing, API testing, UI testing, and acceptance testing.

The group project begins with this testing framework already implemented and functioning.

Teams will extend the test strategy by adding new test cases, improving coverage, and validating any new features developed during the group project.

Students should follow the existing testing structure and tools when expanding the test suite.

## 📝 Purpose

Sprint 5 expands the Task Tracker system with external API integration and UI enhancements. The following components will be tested:

1. **API Layer:** Ensure `/api/time` returns the current time (mocked or real)
2. **UI Integration:** Display time in the Task Report view
3. **Robot Framework Acceptance Testing** for time display (US039)
4. **Regression Testing:** Validate previously implemented features still function as expected
5. **CI/CD Pipeline:** Run all test layers through GitHub Actions


## 📅 Sprint Information

**Sprint:** 5
**Iteration Dates:** YYYY-MM-DD → YYYY-MM-DD
**Version under test:** `main` branch after merging Sprint 5 PRs
**Prepared by:** \[Your Name]
**Last updated:** YYYY-MM-DD

## 🎯 Test Scope

### ✅ New Features and Stories Covered in Sprint 5:

| User Story | Description                 | Test Focus                       |
| ---------- | --------------------------- | -------------------------------- |
| US031      | View Current Time (API)     | Unit, Integration (requests)     |
| US039      | View Current Time in Web UI | Playwright, Robot, Unit (mocked) |

## 🧪 Test Strategy

### ✅ Testing Layers

| Layer       | Tool/Method        | Scope                                                               |
| ----------- | ------------------ | ------------------------------------------------------------------- |
| Unit Tests  | `pytest`           | Logic in `TimeService`, UI render with mock, `TaskService` fallback |
| Integration | `requests` + Flask | `/api/time` endpoint w/ and w/o mocked service                      |
| UI Tests    | `Playwright`       | Time shown in `/tasks/report`                                       |
| Acceptance  | `Robot Framework`  | End-to-end time display scenario                                    |
| Regression  | `pytest`           | Rerun all prior tests from Sprints 1–4                              |


## 📋 Test Case Summary

### ✅ Time API and UI

| TC ID        | Description                                           | Tool            | Type              |
| ------------ | ----------------------------------------------------- | --------------- | ----------------- |
| TC-US031-001 | GET `/api/time` returns mocked time                   | requests/pytest | Integration (API) |
| TC-US031-002 | GET `/api/time` returns real current time             | requests/pytest | Integration (API) |
| TC-US031-003 | TimeService returns correct datetime string           | pytest          | Unit              |
| TC-US039-001 | Time shown in Task Report UI (mocked)                 | Playwright      | UI                |
| TC-US039-002 | User sees current time in UI summary (mocked)         | Robot Framework | Acceptance        |
| TC-US039-003 | Inject MockTimeService for predictable test rendering | pytest          | Unit              |

### 🔁 Regression Cases (Selected)

| TC ID        | Description                           | Tool            | Type          |
| ------------ | ------------------------------------- | --------------- | ------------- |
| TC-US014-001 | Add Task via Web Form                 | Selenium        | UI            |
| TC-US018-001 | List Tasks in HTML                    | Playwright      | UI            |
| TC-US027-001 | View Task Summary Report              | Robot Framework | Acceptance    |
| TC-RF014-001 | Form validation errors for empty task | Playwright      | UI            |
| TC-RF014-002 | JavaScript errors not shown           | Selenium        | UI (Negative) |

## 🔄 CI Integration

All test layers must pass during CI/CD GitHub Actions pipeline:

```yaml
- name: Run Unit Tests
  run: pytest tests/unit --cov=app --cov-report=term-missing

- name: Run API Integration Tests
  run: pytest tests/api --cov=app --cov-report=term-missing

- name: Run UI Tests (Playwright)
  run: pytest tests/ui/playwright

- name: Run Robot Framework Acceptance Tests
  run: robot tests/robot/
```

## 📊 In-Scope Functionality (Test Targets)


| ID    | Component        | Description                                                         |
| ----- | ---------------- | ------------------------------------------------------------------- |
| API   | Flask API Routes | `GET`, `POST`, `PUT`, `DELETE` endpoints for task and time handling |
| UI    | Web Interface    | Forms, task views, navigation, and report pages                     |
| Tools | Postman & Robot  | Use external tools to test both frontend and backend functionality  |
| Ext   | External API     | World Time API integration through `/api/time` endpoint             |


## 🔍 Acceptance Criteria

### Postman Testing

* ✅ Collection includes all task-related and `/api/time` endpoints
* ✅ Valid task creation, retrieval, update, delete return expected payloads and status
* ✅ Time API call returns valid timestamp or error if unavailable
* ✅ Error cases return expected 4xx or 5xx responses

### Robot Framework Testing

* ✅ UI flows: add task, view list, delete, mark complete, see report
* ✅ Input validation scenarios tested (e.g. whitespace-only titles)
* ✅ Time shown via UI (if implemented)
* ✅ Output logs and screenshots saved
* ✅ Robot test scripts are structured and readable

### Regression

* ✅ Tests from Sprint 1–4 re-run using CI
* ✅ pytest, requests, Selenium, and Playwright tests pass
* ✅ Routes refactored for injected services remain compatible


## 🔗 Traceability Matrix


| ID  | Acceptance Criterion                         | Test Case ID Range       |
| --- | -------------------------------------------- | ------------------------ |
| API | All API endpoints tested (incl. `/api/time`) | TC-API-001 to TC-API-010 |
| UI  | Robot Framework verifies all UI features     | TC-UI-Robot-001 to 010   |
| EXT | TimeService mock and real response tests     | TC-TIME-001 to 004       |
| REG | Regression tests from previous sprints       | TC-REG-001+              |


## 🕵️ Test Types and Approach


| Test Type        | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| Postman Tests    | Black-box API testing via request collections (manual and CI-run)         |
| Robot Framework  | Acceptance and UI automation using keyword-driven scripting               |
| Mocked Testing   | Injected mock services to simulate real-time API responses and edge cases |
| Regression Tests | Run pytest/requests/selenium/playwright tests to ensure continuity        |
| CI Verification  | Ensure all test suites run and report under GitHub Actions CI             |
| BDD (Optional)   | Gherkin + Robot acceptance tests (if expanded)                            |


## 🛠️ Testing Tools


| Tool                  | Purpose                                             |
| --------------------- | --------------------------------------------------- |
| Postman               | REST API validation and script-based assertions     |
| Robot Framework       | Automated end-to-end UI flow testing                |
| GitHub Actions        | CI for automated multi-tool validation              |
| pytest / requests     | Unit and integration test support (including mocks) |
| selenium / playwright | UI testing (legacy or optional regression check)    |

## 🔧 Test Environment Setup

* Python 3.11+, Flask application running (`flask run`)
* `create_app()` supports service injection for test modes
* Postman installed with collection file loaded
* Robot Framework with SeleniumLibrary or Browser Library installed
* CI YAML file includes Postman, pytest, and Robot test runs


## 🧪 Test Data & Preconditions


| Scenario                 | Input / Action                                   | Expected Result                        |
| ------------------------ | ------------------------------------------------ | -------------------------------------- |
| Valid API request        | POST `{"title": "Grade papers"}` to `/api/tasks` | `201 Created` with new task object     |
| Invalid task submission  | Empty or whitespace title                        | `400 Bad Request` with error message   |
| External API working     | Call `/api/time`                                 | Returns current UTC timestamp          |
| External API unavailable | Simulate or inject failure                       | Returns error JSON or fallback message |
| UI Form submission       | Fill and submit via Robot                        | Task appears in list or report         |


## 🧾 Test Coverage Goals

* 🔄 All API endpoints (including `/api/time`) tested via Postman and pytest
* ✅ Robot Framework covers all primary user UI workflows
* 🧪 Mocked `TimeService` and `TaskService` tested independently
* 💻 CI executes pytest, Postman, and Robot on every push and PR


## ⚠️ Risks & Mitigations


| Risk                     | Impact             | Mitigation                                      |
| ------------------------ | ------------------ | ----------------------------------------------- |
| API outage / no internet | Test failure       | Use mocks and retry logic in CI                 |
| Tool misconfiguration    | Delayed testing    | CI tested on every push; setup scripts provided |
| Robot test flakiness     | Intermittent fails | Use wait-for or screen capture logs             |


## 📃 Test Artifacts

* `tests/postman/collection.json`: Postman test suite
* `tests/robot/`: Robot test cases and logs
* `docs/test_documentation/s5_test_plan.md`: This document
* `docs/test_documentation/s5_test_cases.md`: Test case breakdown
* `docs/test_documentation/s5_test_report.md`: Results and screenshots

## ✍️ Approvals

> **Note:** Approvals are not required in this course but mirror real-world QA review processes.

| Role                 | Name | Signature / Date |
| -------------------- | ---- | ---------------- |
| Product Owner        |      |                  |
| QA Lead / Instructor |      |                  |
| Developer            |      |                  |
