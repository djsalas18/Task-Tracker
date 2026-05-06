# Sprint 4 – Quality Assurance and Project Completion

Sprint 4 is a stabilization sprint. Teams should focus on testing, documentation, and validation rather than introducing major new features.

⚠️ **Pull requests must be created continuously during the sprint.  
Large end-of-sprint code dumps will receive reduced credit because they prevent proper CI validation and team review.**

---

# Sprint Goal

The goal of Sprint 4 is to finalize testing, documentation, and validation of the Task Tracker system.

During this sprint, teams will:

* complete final testing validation
* prepare testing documentation
* verify CI pipelines
* prepare the final project presentation

Sprint 4 focuses on **software quality assurance and project completion**.

---

# Project Requirement Alignment (Sprint 4)

Sprint 4 finalizes the remaining Group Project requirements:

| Requirement | Sprint 4 Expectation |
| ----------- | -------------------- |
| PR-1 Documentation | Finalize all Agile/technical documentation updates (Sprint Plan, Test Plan, Test Cases, API/diagrams/README updates as applicable). |
| PR-7 QA Coverage | Confirm full unit, integration, UI, and acceptance regression coverage for new and existing functionality. |
| PR-8 Testing Documentation | Complete Test Execution Report with ownership, execution summary, regression verification, edge cases, CI validation, and QA sign-off. |
| PR-9 Final Test Report | Produce consolidated Final Test Report (PDF) summarizing full project testing outcomes. |
| PR-10 Presentation | Prepare and deliver professional final team presentation. |

---

# Testing Documentation and Verification

Teams must create documentation describing how the system was tested and validated.

Create the following document:

```text
docs/test_documentation/test_execution_report.md
```

The report content must satisfy PR-8 requirements, including:

* test ownership
* execution summary
* regression verification
* at least two edge case results
* CI validation evidence
* final QA validation sign-off

This document must include:

### Test Ownership

Identify which team members created and reviewed each test category.

| Test Area        | Framework           | Created By | Reviewed By |
| ---------------- | ------------------- | ---------- | ----------- |
| Unit Tests       | pytest              |            |             |
| API Tests        | pytest + requests   |            |             |
| UI Tests         | Playwright/Selenium |            |             |
| Acceptance Tests | Robot Framework     |            |             |

---

### Test Execution Summary

Provide a summary of automated test runs.

| Test Suite       | Command           | Result |
| ---------------- | ----------------- | ------ |
| Unit Tests       | pytest            |        |
| API Tests        | pytest tests/api  |        |
| UI Tests         | pytest tests/ui   |        |
| Acceptance Tests | robot tests/robot |        |

---

### Regression Verification

Teams must confirm that the following features function correctly:

* Add Task
* View Tasks
* Update Task
* Delete Task
* Time API endpoint

---

### CI Validation

Provide evidence that automated tests execute successfully within the CI workflow.

Examples include:

* screenshot of successful GitHub Actions runs
* confirmation that tests run during pull requests

---

# Final Test Report

Teams must produce a **Final Test Report** summarizing testing activities performed during the project.

The completed report should be prepared for PDF submission.

Refer to:

```text
Appendix A – Final Test Report Guidance
```

for the report guidance provided on Blackboard.

The report should summarize:

* testing strategy
* automated testing coverage
* major test results
* identified issues
* validation results

---

# Final Presentation

Teams will present their completed project.

The presentation should include:

* system architecture overview
* implemented features
* testing strategy
* lessons learned during development

Refer to:

```text
Appendix D – Presentation Guidance
```

for the presentation guidance provided on Blackboard.

---

## Sprint 4 Level Acceptance Criteria

Sprint 4 is considered complete when the team has finalized testing, documentation, and validation of the Task Tracker system.

The following conditions must be satisfied:

* all automated tests execute successfully
* Robot Framework acceptance tests run successfully
* regression testing confirms previously implemented features continue to work
* the **Test Execution Report** has been completed
* the **Final Test Report** has been prepared
* CI pipelines run successfully without failures
* the team has prepared their final project presentation
* all remaining PR-1 documentation updates are complete and accurate

No new features should be introduced during this sprint unless they are required to resolve defects discovered during testing.

---

## Definition of Done

Work in Sprint 4 is considered complete when:

* all pull requests have been reviewed and merged
* automated tests pass locally and in CI
* the test execution report document is complete and includes PR-8 required sections
* the Final Test Report PDF has been generated and reviewed by the team
* documentation accurately reflects the current system
* the system runs successfully without errors
* the team presentation materials are ready for a professional 20-30 minute delivery

The goal of Sprint 4 is to ensure the project reaches a **stable and well-documented release state**.

---

## Sprint 4 Deliverables

```text
• Completed automated test suites
• docs/test_documentation/test_execution_report.md
• Final Test Report (PDF)
• CI pipeline verification
• Team presentation
```

---

# Project Timeline Summary

| Sprint   | Duration | Focus                                 |
| -------- | -------- | ------------------------------------- |
| Sprint 1 | 1 week   | Codebase review and onboarding        |
| Sprint 2 | 2 weeks  | Feature development                   |
| Sprint 3 | 2 weeks  | Testing automation and second feature |
| Sprint 4 | 1 week   | QA validation and project completion  |

---

# Sprint 4 GitHub Issue Structure

Sprint 4 work should be organized using **one Epic Issue** and **three sub-issues**.

Recommended structure:

```text
Sprint 4 Epic
 ├─ Sub-Issue 1 – Final Regression Testing
 ├─ Sub-Issue 2 – Test Execution Documentation
 └─ Sub-Issue 3 – Final Presentation Preparation
```

---

# Sprint 4 Epic Issue Template (PR-1, PR-7, PR-8, PR-9, PR-10)

### Title

```text
Sprint 4 – Quality Assurance and Project Completion
```

### Description

```text
Sprint 4 focuses on final system validation, testing documentation, and preparation for the final project presentation.

Objectives:

• verify all implemented features through full regression and acceptance testing (PR-7)
• complete Test Execution Report with required evidence and QA sign-off (PR-8)
• produce and finalize consolidated Final Test Report PDF (PR-9)
• finalize documentation updates across sprint/testing/API/architecture artifacts (PR-1)
• prepare the final professional team presentation (PR-10)
```

### Deliverables

```text
• full regression and automated testing completed with passing results (PR-7)
• docs/testing/test_execution_report.md completed with required sections (PR-8)
• final test report prepared in PDF format (PR-9)
• documentation finalized and consistent with implementation (PR-1)
• presentation prepared for final panel delivery (PR-10)
```

### Definition of Done

```text
• automated tests pass locally and in CI (PR-7)
• regression testing confirms system stability (PR-7)
• test execution report completed with required evidence/sign-off (PR-8)
• final test report submitted in PDF format (PR-9)
• presentation materials prepared for final delivery (PR-10)
• final documentation alignment complete (PR-1)
```

---

# Sprint 4 Sub-Issue 1 – Final Regression Testing (PR-7)

### Title

```text
Run Final Regression Testing
```

### Description

```text
Verify that all implemented features operate correctly before final submission.
```

PR Mapping: Primary requirement PR-7 (final regression and stability validation).

### Regression Coverage

```text
• Add Task
• Update Task
• Delete Task
• Task Report
• Time API endpoint
• Sprint 2 feature
• Sprint 3 feature
```

### Validation

```text
• automated tests pass
• UI workflows function correctly
• no regressions introduced
```

---

# Sprint 4 Sub-Issue 2 – Test Execution Documentation (PR-8)

### Title

```text
Complete Test Execution Report
```

### Description

```text
Create the testing documentation that summarizes how the system was tested during the group project.
```

PR Mapping: Primary requirement PR-8 (test ownership, execution, regression, edge, CI, QA sign-off).

### Document Location

```text
docs/testing/test_execution_report.md
```

### Required Sections

```text
• Test Ownership
• Test Execution Summary
• Regression Verification
• Edge Case Testing
• CI Validation
• QA Validation Sign-Off
```

### Validation

```text
• document accurately reflects testing work performed
• document reviewed by QA Lead
```

---

# Sprint 4 Sub-Issue 3 – Final Presentation Preparation (PR-10)

### Title

```text
Prepare Final Project Presentation
```

### Description

```text
Prepare a short presentation describing the system architecture, implemented features, and testing strategy.
```

PR Mapping: Primary requirement PR-10 (final presentation delivery).

### Presentation Topics

```text
• system architecture overview
• features implemented during group project
• testing strategy
• lessons learned during development
```

### Validation

```text
• presentation slides prepared
• team members assigned speaking roles
```

---

# Recommended Sprint 4 Workflow

```text
1. Create Sprint 4 Epic
2. Create sub-issues
3. Assign responsibilities
4. Run regression testing
5. Complete testing documentation
6. Prepare presentation
7. Verify CI pipeline
```
---

