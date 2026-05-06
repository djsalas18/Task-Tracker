# Sprint 2 – Feature Development and Architecture Improvements

⚠️ **Pull requests must be created continuously during the sprint.  
Large end-of-sprint code dumps will receive reduced credit because they prevent proper CI validation and team review.**
---

# Sprint Goal

The goal of Sprint 2 is to begin extending the Task Tracker application through the implementation of new functionality while continuing to improve system architecture and test coverage.

During this sprint, teams will:

* select a feature from the group project backlog
* implement the feature using the existing layered architecture
* expand automated test coverage
* continue using GitHub workflow practices
* validate that existing functionality continues to operate correctly

Sprint 2 represents the transition from **system onboarding to active development**.

---

# Project Requirement Alignment (Sprint 2)

Sprint 2 must implement the following Group Project requirements:

| Requirement | Sprint 2 Expectation |
| ----------- | -------------------- |
| PR-1 Documentation | Update Sprint Plan, Test Plan, Test Cases, API reference/diagrams as changes are introduced. |
| PR-2 DevOps / CI | Start CI refactor: keep unit+integration in primary workflow, isolate UI/BDD workflows, add docs-only ignore rules. |
| PR-3 Hybrid Tests | Organize tests by concern and add `unit`, `integration`, `e2e` markers in `pytest.ini`. |
| PR-4 TimeService Testing | Implement automated TimeService tests (UI/API as applicable), execute, and document results. |
| PR-5 Validation Architecture | Centralize task validation in shared schema + service-layer rules. |
| PR-6 Feature Enhancements | Implement the first selected feature enhancement from `group_project_choice.md`. |
| PR-7 QA Coverage | Add unit + integration coverage for all new/changed Sprint 2 behavior. |

---

# Educational Context

In real software projects, development teams extend existing systems by implementing new features while maintaining system stability.

This sprint emphasizes:

* incremental feature development
* architectural consistency
* automated testing
* collaborative development practices

Teams should ensure that **new functionality follows the same architectural patterns established in the existing codebase**.

---

# Sprint 2 Development Activities

Teams should complete the following development tasks.

### Feature Selection

Teams must select the **two required project features** from the available group project options and schedule them across Sprint 2 and Sprint 3.

Sprint 2 must implement **at least the first selected feature**.

Possible feature examples include:

* task editing enhancements
* task filtering or search
* improved task validation
* UI improvements
* additional API endpoints

Refer to:

```text
group_project_choice.md
```

for the assigned feature options provided on Blackboard.

---

### Architecture Consistency

New code must follow the established architecture:

| Layer            | Responsibility       |
| ---------------- | -------------------- |
| Route Layer      | Handle HTTP requests |
| Service Layer    | Business logic       |
| Repository Layer | Data persistence     |
| Model Layer      | Data structure       |

New functionality should be implemented primarily within the **service layer** with minimal logic inside route handlers.

Sprint 2 must also complete architecture requirements from the project brief:

* implement hybrid test organization (concern-based folders + pytest markers)
* centralize task validation in shared schema/service logic

---

### Automated Testing Expansion

For each implemented feature, teams must add automated tests.

Examples include:

| Test Type | Example                   |
| --------- | ------------------------- |
| Unit Test | testing service methods   |
| API Test  | testing REST endpoints    |
| UI Test   | validating user workflows |

Tests should be added to the appropriate testing directories.

Sprint 2 testing must explicitly include:

* TimeService automated test coverage (PR-4)
* marker-based execution support (`pytest -m unit`, `pytest -m integration`, `pytest -m e2e`) (PR-3)
* regression checks for existing TaskService and TimeService behaviors (PR-7)

---

### CI / DevOps Work (Required in Sprint 2)

Sprint 2 must begin PR-2 CI restructuring:

* primary workflow runs only unit + integration tests
* UI and BDD tests run in separate workflows
* workflows ignore documentation-only changes
* workflows support manual run and path-based conditional triggers

---

# Sprint 2 Team Responsibilities

Teams should divide development tasks among members.

Example roles:

| Role              | Responsibility                |
| ----------------- | ----------------------------- |
| Feature Developer | implement application feature |
| Test Developer    | create automated tests        |
| Code Reviewer     | review pull requests          |
| QA Lead           | verify system stability       |

Teams should continue using **GitHub issues and pull requests** to manage development work.

---

# Definition of Done – Sprint 2

Work in Sprint 2 is considered complete when the following conditions are satisfied:

* the first selected project feature has been implemented according to its user story
* the new functionality follows the existing application architecture (route → service → repository)
* PR-3 hybrid testing structure and pytest markers are implemented
* PR-4 TimeService automated tests are implemented and executed
* PR-5 centralized validation architecture has been implemented
* automated tests have been added to validate all Sprint 2 functionality
* existing automated tests continue to pass
* regression testing confirms that previously implemented features still function correctly
* all development work has been completed through GitHub issues and pull requests
* pull requests have been reviewed and approved by at least one team member
* the CI pipeline executes successfully
* documentation has been updated where necessary to reflect architecture, test, and API changes

At the end of Sprint 2, the system should include **one new feature with corresponding automated tests while maintaining system stability**.

---

>Sprint 2 focuses on implementing the first new feature while maintaining the architecture and testing practices established earlier in the project.

## Sprint 2 GitHub Issue Structure

Sprint 2 work should be organized using **one Epic Issue** and several **sub-issues**.

Recommended structure:

```text
Sprint 2 Epic
 ├─ Sub-Issue 1 – Feature Implementation
 ├─ Sub-Issue 2 – Automated Testing
 ├─ Sub-Issue 3 – UI / API Integration
 └─ Sub-Issue 4 – Regression Testing
```

Each issue should be assigned to a team member and completed through a pull request.

---

# Sprint 2 Epic Issue Template (PR-1, PR-2, PR-3, PR-4, PR-5, PR-6, PR-7)

### Title

```text
Sprint 2 – Feature Development
```

### Description

```text
Sprint 2 focuses on implementing the first new feature for the Task Tracker application while maintaining architectural consistency and automated testing coverage.

Objectives:

• select and implement the first required feature enhancement (PR-6)
• implement hybrid test organization and marker strategy (PR-3)
• centralize task validation rules in shared schema/service layer (PR-5)
• implement and execute TimeService automated tests (PR-4)
• expand unit/integration regression coverage and preserve system behavior (PR-7)
• begin CI restructuring for conditional workflows and docs-ignore rules (PR-2)
• update sprint/testing/API documentation as changes are introduced (PR-1)
```

### Deliverables

```text
• first selected feature implemented (PR-6)
• hybrid test structure + pytest markers implemented (PR-3)
• centralized validation refactor implemented (PR-5)
• TimeService automated tests executed with results captured (PR-4)
• regression and new-feature automated tests added (PR-7)
• CI updates committed and validated in workflow runs (PR-2)
• pull requests reviewed and merged; docs updated (PR-1)
```

### Definition of Done

```text
• feature implemented according to user story (PR-6)
• hybrid/validation/TimeService requirements completed (PR-3, PR-4, PR-5)
• tests added and passing for new + regression scope (PR-7)
• pull requests reviewed and approved
• CI pipeline successful with required workflow behavior (PR-2)
• required sprint/testing/API documentation updated (PR-1)
```

---

# Sprint 2 Sub-Issue 1 – Feature Implementation (PR-6)

### Title

```text
Implement Feature: [Feature Name]
```

Example:

```text
Implement Feature: Task Filtering
```

### Description

```text
Implement the selected feature for Sprint 2.

The implementation should follow the layered architecture:

Route Layer
Service Layer
Repository Layer
Database Model
```

PR Mapping: Primary requirement PR-6 (Feature Enhancement Selection).

### Implementation Tasks

```text
• update or create route handler
• implement service logic
• update repository logic if required
• update UI templates if necessary
```

### Validation

```text
• feature functions correctly through API
• feature works through the UI
```

---

# Sprint 2 Sub-Issue 2 – Automated Testing (PR-4, PR-7)

### Title

```text
Add Automated Tests for Sprint 2 Feature
```

### Description

```text
Create automated tests validating the functionality of the Sprint 2 feature.
```

PR Mapping: Primary requirements PR-4 (TimeService testing) and PR-7 (test coverage).

### Required Tests

```text
• unit tests for service layer logic
• API tests validating endpoint behavior
• UI test validating workflow (if applicable)
```

### Validation

```text
• tests execute successfully
• tests pass in CI pipeline
```

---

# Sprint 2 Sub-Issue 3 – Integration Verification (PR-5, PR-6)

### Title

```text
Verify Feature Integration with Existing System
```

### Description

```text
Ensure the new feature integrates correctly with existing application components.
```

PR Mapping: Primary requirements PR-5 (centralized validation architecture) and PR-6 (feature integration).

### Tasks

```text
• verify database interactions
• verify UI behavior
• verify API responses
```

### Validation

```text
• no regression issues observed
• system functions normally
```

---

# Sprint 2 Sub-Issue 4 – Regression Testing (PR-7)

### Title

```text
Run Regression Tests
```

### Description

```text
Verify that previously implemented features continue to work correctly after the new feature implementation.
```

PR Mapping: Primary requirement PR-7 (regression verification across existing functionality).

### Regression Coverage

```text
• Add Task
• Update Task
• Delete Task
• Task Report
• Time API
```

### Validation

```text
• automated tests pass
• UI workflows function correctly
```

---

# Recommended Sprint 2 Workflow

Teams should follow this development workflow:

```text
1. Create Sprint 2 Epic
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

```
Closes #12
```

This automatically closes the issue when the PR is merged and makes the project board easier to manage.

