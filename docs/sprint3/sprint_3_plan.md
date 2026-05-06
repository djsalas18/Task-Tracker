# Sprint 3 – Advanced Feature Development and Test Automation

⚠️ **Pull requests must be created continuously during the sprint.  
Large end-of-sprint code dumps will receive reduced credit because they prevent proper CI validation and team review.**
---

# Sprint Goal

The goal of Sprint 3 is to expand application capabilities while strengthening automated testing and system reliability.

During this sprint, teams will:

* implement an additional feature from the backlog
* introduce acceptance testing using Robot Framework
* expand UI and API test coverage
* validate system stability through regression testing

Sprint 3 completes the project transition from feature delivery to verification-ready quality.

---

# Project Requirement Alignment (Sprint 3)

Sprint 3 must advance and/or complete the following Group Project requirements:

| Requirement | Sprint 3 Expectation |
| ----------- | -------------------- |
| PR-1 Documentation | Continue updating Sprint Plan, Test Plan, Test Cases, API and architecture docs for all Sprint 3 changes. |
| PR-2 DevOps / CI | Complete conditional CI behavior: path-based triggers, manual run support, PR-label override where required. |
| PR-6 Feature Enhancements | Implement the second selected feature enhancement from `group_project_choice.md`. |
| PR-7 QA Coverage | Expand unit/integration/UI/acceptance coverage for all new and existing critical workflows. |
| PR-8 Testing Documentation | Begin/expand test execution documentation including ownership, execution summary, regression verification, and CI validation evidence. |

---

# Educational Context

Professional software teams rely heavily on automated testing to ensure that systems remain stable as new functionality is introduced.

This sprint emphasizes:

* automated acceptance testing
* regression testing
* continuous integration

Students will practice validating complex workflows through automated testing tools.

---

# Sprint 3 Development Activities

### Feature Implementation

Teams must implement the **second required feature enhancement** from the available backlog.

Refer to:

```text
group_project_choice.md
```

for the assigned feature options provided on Blackboard.

This feature should follow the same architecture patterns used in previous development work.

---

### Acceptance Test Implementation

Sprint 3 introduces **Robot Framework acceptance testing**.

Acceptance tests should validate full user workflows such as:

* creating a task
* completing a task
* deleting a task
* viewing task reports
* retrieving time from the external API

These tests simulate real user interactions with the system.

Robot acceptance coverage should support PR-7 regression expectations, including TaskService and TimeService workflows.

---

### Regression Testing

Teams must verify that all previously implemented features continue to function correctly.

Regression tests should cover:

* task creation
* task updates
* task deletion
* database persistence
* UI workflows
* external API integration

Regression scope in Sprint 3 should align with required suite behavior for:

* `/api/tasks` add/list/update/delete + error paths
* `/api/time` success + failure/edge behavior

---

### Testing Documentation Progress (PR-8)

Sprint 3 should produce a draft/working version of the Test Execution Report with:

* test ownership matrix
* execution command summary and current results
* regression verification notes
* CI validation evidence references

---

# Definition of Done – Sprint 3

Work in Sprint 3 is considered complete when the following conditions are satisfied:

* the second selected project feature has been implemented according to its user story
* automated tests have been created for the new functionality
* Robot Framework acceptance tests validate required end-to-end workflows
* existing unit, API, and UI tests continue to pass
* PR-2 CI behavior is completed for conditional workflows, manual run, and override strategy
* PR-8 testing documentation is updated with Sprint 3 evidence
* regression testing confirms that previously implemented features still function correctly
* all code changes have been committed through pull requests
* pull requests have been reviewed and approved by at least one team member
* the CI pipeline executes successfully
* documentation has been updated where necessary to reflect system changes

At the end of Sprint 3, the application should be **feature complete and ready for final quality validation in Sprint 4**.

---

>Sprint 3 represents the final feature development sprint. Sprint 4 should focus on testing, documentation, and final validation rather than introducing major new features.

---

# Sprint 3 GitHub Issue Structure

Sprint 3 work should be organized using **one Epic Issue** and several **sub-issues**.

Recommended structure:

```text
Sprint 3 Epic
 ├─ Sub-Issue 1 – Feature Implementation
 ├─ Sub-Issue 2 – Robot Framework Acceptance Tests
 ├─ Sub-Issue 3 – Automated Test Expansion
 └─ Sub-Issue 4 – Regression Testing
```

Each issue should be assigned to a team member and completed through a pull request.

---

# Sprint 3 Epic Issue Template (PR-1, PR-2, PR-6, PR-7, PR-8)

### Title

```text
Sprint 3 – Advanced Feature Development and Test Automation
```

### Description

```text
Sprint 3 focuses on expanding application functionality and strengthening automated testing.

Objectives:

• implement the second required feature enhancement (PR-6)
• complete CI conditional/manual/override behavior as required (PR-2)
• introduce and expand Robot acceptance coverage with supporting UI/API tests (PR-7)
• perform full regression testing to verify system stability (PR-7)
• update Test Execution Report with ownership/results/evidence (PR-8)
• continue updating sprint/testing/API documentation (PR-1)
```

### Deliverables

```text
• second selected feature implemented (PR-6)
• Robot acceptance tests and expanded automated suites completed (PR-7)
• regression testing completed for required task/time workflows (PR-7)
• CI workflow behavior verified in pipeline runs (PR-2)
• Test Execution Report updated with Sprint 3 evidence (PR-8)
• pull requests reviewed/merged and sprint documentation updated (PR-1)
```

### Definition of Done

```text
• Sprint 3 feature implemented and verified (PR-6)
• Robot Framework tests created/executed successfully (PR-7)
• automated tests pass locally and in CI (PR-7)
• CI behavior aligned with required trigger strategy (PR-2)
• Test Execution Report updated with Sprint 3 verification evidence (PR-8)
• pull requests reviewed and approved; docs updated (PR-1)
```

---

# Sprint 3 Sub-Issue 1 – Feature Implementation (PR-6)

### Title

```text
Implement Feature: [Feature Name]
```

Example:

```text
Implement Feature: Task Search
```

### Description

```text
Implement the selected Sprint 3 feature using the established layered architecture.

All business logic should be implemented in the service layer while route handlers remain lightweight.
```

PR Mapping: Primary requirement PR-6 (second feature enhancement).

### Implementation Tasks

```text
• update route handler
• implement service layer logic
• update repository layer if necessary
• update UI templates if required
```

### Validation

```text
• feature functions correctly through API
• feature works through the web UI
```

---

# Sprint 3 Sub-Issue 2 – Robot Framework Acceptance Tests (PR-7)

### Title

```text
Add Robot Framework Acceptance Tests
```

### Description

```text
Create Robot Framework tests that validate end-to-end user workflows within the Task Tracker application.
```

PR Mapping: Primary requirement PR-7 (acceptance/end-to-end coverage).

### Example Workflows

```text
• create a task
• mark a task complete
• delete a task
• retrieve time from the external API
```

### Validation

```text
• tests execute successfully
• tests simulate realistic user workflows
```

---

# Sprint 3 Sub-Issue 3 – Automated Test Expansion (PR-7)

### Title

```text
Expand Automated Test Coverage
```

### Description

```text
Expand the automated test suite to ensure the Sprint 3 feature and related functionality are fully tested.
```

PR Mapping: Primary requirement PR-7 (expanded unit/integration/UI coverage).

### Tasks

```text
• add unit tests for new service logic
• add API tests validating endpoints
• add UI automation tests if applicable
```

### Validation

```text
• tests execute successfully
• tests pass in CI pipeline
```

---

# Sprint 3 Sub-Issue 4 – Regression Testing (PR-7, PR-8)

### Title

```text
Run Full Regression Testing
```

### Description

```text
Verify that all previously implemented features continue to operate correctly after the Sprint 3 development work.
```

PR Mapping: Primary requirements PR-7 (regression suite) and PR-8 (documented verification evidence).

### Regression Coverage

```text
• Add Task
• Update Task
• Delete Task
• Task Report
• Time API endpoint
```

### Validation

```text
• automated tests pass
• UI workflows function correctly
• no regressions introduced
```

---

# Recommended Sprint 3 Workflow

Teams should follow the same development workflow used in Sprint 2.

```text
1. Create Sprint 3 Epic
2. Create sub-issues
3. Assign team members
4. Create feature branches
5. Implement changes
6. Submit pull requests
7. Conduct peer code review
8. Merge to main branch
```

---

Remember to **link pull requests to issues**.

Example:

```text
Closes #24
```

When the PR merges, the issue closes automatically and the project board updates.

---


