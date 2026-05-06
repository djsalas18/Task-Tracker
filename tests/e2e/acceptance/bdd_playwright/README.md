# BDD Testing with pytest-bdd + pytest-playwright

This directory contains **industry standard** pytest-bdd implementation with pytest-playwright integration for running Playwright-backed UI acceptance scenarios.

**pytest-playwright** is the official Playwright plugin providing built-in fixtures, video recording, screenshot capture, and zero-configuration browser management.

## 📋 Quick Reference

### Essential Setup Commands

```bash
# 1. Activate virtual environment (CRITICAL - do this first!)
.\.venv\Scripts\Activate.ps1    # Windows PowerShell
# source .venv/bin/activate     # Linux/macOS/Git Bash

# 2. Install BDD dependencies (if not already installed)
pip install pytest-bdd pytest-playwright pytest-html
playwright install chromium firefox

# 3. Start Flask application (separate terminal)
python -m app.main

# 4. Run BDD tests
# Note: -o addopts='' bypasses global pytest.ini ignores for this suite
pytest tests/acceptance/bdd_playwright/ -v -o addopts=''
```

### Most Common Commands

```bash
# Basic BDD test run
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -v -o addopts=''

# Visual debugging (see browser)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --headed -v -o addopts=''

# Generate comprehensive report with videos
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --html=results/bdd_report.html --self-contained-html --video=retain-on-failure -v -o addopts=''

# Test with different browser
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --browser=firefox -v -o addopts=''
```

## 🎯 Why BDD Tests Are Separate

**Important:** BDD tests run **separately** from the main test suite to prevent asyncio conflicts:

- ✅ **Main Test Suite**: `pytest -v` (excludes BDD via pytest.ini)
- ✅ **BDD Tests**: `pytest tests/acceptance/bdd_playwright/ -v -o addopts=''` (separate execution)

**Why This Separation:**
- 🔧 **Different Fixtures**: Main tests use sync fixtures, BDD uses async pytest-playwright fixtures
- ⚡ **Performance**: Main test suite stays fast without BDD overhead
- 🏢 **Industry Standard**: Professional teams separate test types by purpose
- 🚫 **Prevents Conflicts**: Avoids asyncio issues between test types

## 🚀 Getting Started

### 1. Environment Setup

**Virtual Environment (Required):**
```bash
# Navigate to your project root
cd your-project-directory

# Activate virtual environment (ALWAYS do this first!)
.\.venv\Scripts\Activate.ps1    # Windows PowerShell
# source .venv/bin/activate     # Linux/macOS/Git Bash

# Verify activation (should show (.venv) in prompt and correct Python path)
python --version
which python    # Linux/macOS
where python    # Windows
```

**Install BDD Dependencies:**
```bash
# Install pytest-bdd and pytest-playwright
pip install pytest-bdd pytest-playwright pytest-html

# Install browser engines
playwright install chromium firefox
```

### 2. Start Flask Application

**In a separate terminal:**
```bash
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1    # Windows
# source .venv/bin/activate     # Linux/macOS

# Start Flask server
python -m app.main

# Verify server is running
curl http://localhost:5000/api/health
```

### 3. Run BDD Tests

**Basic Execution:**
```bash
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1    # Windows
# source .venv/bin/activate     # Linux/macOS

# Run all BDD scenarios
pytest tests/acceptance/bdd_playwright/ -v -o addopts=''

# Run specific test file
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -v -o addopts=''
```

## 🎭 pytest-playwright Features

### Video Recording
```bash
# Record videos only on test failure (recommended)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --video=retain-on-failure -v -o addopts=''

# Record all test executions
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --video=on -v -o addopts=''
```

### Screenshot Capture
```bash
# Screenshots only on assertion failure (recommended)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --screenshot=only-on-failure -v -o addopts=''

# Screenshots for all tests
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --screenshot=on -v -o addopts=''
```

### Multiple Browser Testing
```bash
# Test with Firefox
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --browser=firefox -v -o addopts=''

# Test with Safari (macOS only)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --browser=webkit -v -o addopts=''

# Test with multiple browsers (sequential)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --browser=chromium --browser=firefox -v -o addopts=''
```

### Visual Debugging
```bash
# Headed mode (see browser during test execution)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --headed -v -o addopts=''

# Full debugging mode with all features
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --headed --video=on --screenshot=on -v -s -o addopts=''
```

## 📊 Test Reports

### HTML Reports with Embedded Media
```bash
# Generate comprehensive HTML report (recommended)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py \
  -o addopts='' \
  --html=results/bdd_report.html \
  --self-contained-html \
  --video=retain-on-failure \
  --screenshot=only-on-failure -v

# View report in browser
# Windows: Invoke-Item results/bdd_report.html
# Linux/macOS: open results/bdd_report.html
```

### CI/CD Integration
```bash
# Generate JUnit XML for CI systems
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py \
  -o addopts='' \
  --junitxml=results/junit.xml -v

# Combined reporting for CI
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py \
  -o addopts='' \
  --junitxml=results/junit.xml \
  --html=results/bdd_report.html \
  --self-contained-html -v
```

### Generated Files
- **HTML Report**: `results/bdd_report.html` (interactive with embedded videos/screenshots)
- **JUnit XML**: `results/junit.xml` (CI/CD integration)
- **Videos**: `test-results/` directory (MP4 files for failed tests)
- **Screenshots**: `test-results/` directory (PNG files for assertion failures)

## 🔍 Running Specific Scenarios

### By Scenario Name
```bash
# Run scenarios containing specific keywords
pytest -k "Complete task workflow" tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -v -o addopts=''

# Run scenarios with task creation
pytest -k "task creation" tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -v -o addopts=''
```

### By Exact Test Name
```bash
# Run specific scenario by exact name (use quotes for spaces)
pytest "tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py::test_complete_task_workflow_with_playwright___create__complete__and_view_report" -v -o addopts=''
```

### Development Workflow
```bash
# Quick test during development (minimal output)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -q -o addopts=''

# Verbose output for debugging
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -v -s -o addopts=''

# Stop on first failure
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -x -v -o addopts=''
```

## 🏗️ Project Structure

```
tests/acceptance/bdd_playwright/
├── README.md                           # This documentation
├── conftest.py                         # pytest fixtures and configuration
├── test_playwright_pytestbdd.py        # pytest-bdd step definitions
└── features/
    └── task_workflow_playwright.feature # Gherkin scenarios
```

### File Descriptions

- **conftest.py**: pytest fixtures using pytest-playwright built-in fixtures
- **test_playwright_pytestbdd.py**: Step definitions that map Gherkin steps to Python code
- **features/**: Gherkin feature files with business-readable scenarios
- **README.md**: This comprehensive documentation

## 🧪 Available BDD Scenarios

### Current Feature: Task Tracker Manual Workflow (US033)

1. **Complete task workflow** - Create, complete, and view task in report
2. **Simple task creation** - Basic task creation and verification
3. **Task creation and verification** - Enhanced task workflow validation

### Scenario Example

```gherkin
Scenario: Complete task workflow with Playwright - Create, Complete, and View Report
  Given I am on the home page
  When I click "Add Task" in the navigation menu
  Then I should be on the task creation page
  When I fill out the task form with:
    | Field       | Value                           |
    | Title       | Playwright BDD Integration Task |
    | Description | Created using Playwright BDD   |
  And I submit the task form
  Then I should be redirected to the task list page
  And I should see "Playwright BDD Integration Task" in the task list
  # ... additional steps for completion and reporting
```

## 🔧 Configuration

### pytest Configuration

The BDD tests are **excluded** from the main test suite via `pytest.ini`:

```ini
# pytest.ini
addopts = 
    # ... other options ...
    --ignore=tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py
```

This ensures:
- Main test suite runs fast: `pytest -v`
- BDD tests run separately: `pytest tests/acceptance/bdd_playwright/ -v -o addopts=''`

### Environment Variables

```bash
# Optional: Control headless mode
export HEADLESS=false  # Linux/macOS
$env:HEADLESS="false"  # Windows PowerShell

# CI environment detection (automatic)
export CI=true         # Automatically sets headless mode
```

## 🐛 Troubleshooting

### Common Issues and Solutions

1. **Virtual Environment Not Activated**
   ```bash
   # Symptom: "pytest not found" or wrong Python version
   # Solution: Always activate virtual environment first
   .\.venv\Scripts\Activate.ps1    # Windows
   # source .venv/bin/activate     # Linux/macOS
   ```

2. **Flask Server Not Running**
   ```bash
   # Symptom: Connection refused errors
   # Solution: Start Flask in separate terminal
   python -m app.main
   # Verify: curl http://localhost:5000/api/health
   ```

3. **Playwright Browsers Not Installed**
   ```bash
   # Symptom: Browser download errors
   # Solution: Install browsers
   playwright install chromium firefox
   ```

4. **pytest-playwright Not Installed**
   ```bash
   # Symptom: Missing fixtures (browser, page, context)
   # Solution: Install pytest-playwright
   pip install pytest-playwright
   ```

5. **BDD Tests Running with Main Suite**
   ```bash
   # Symptom: Asyncio conflicts when running pytest -v
   # Solution: Verify pytest.ini excludes BDD tests
  # BDD tests should only run with: pytest tests/acceptance/bdd_playwright/ -v -o addopts=''
   ```

### Advanced Debugging

```bash
# Debug with full browser automation visibility
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py \
  -o addopts='' \
  --headed \
  --video=on \
  --screenshot=on \
  --slowmo=500 \
  -v -s

# Debug specific scenario with minimal noise
pytest -k "Simple task creation" \
  tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py \
  --headed -v -s -o addopts=''
```

### Performance Optimization

```bash
# Faster execution for CI
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py \
  -o addopts='' \
  --browser=chromium \
  -x \
  --maxfail=1 \
  -q

# Parallel execution (if supported)
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py \
  -o addopts='' \
  --numprocesses=2 \
  -v
```

## 📚 Learning Resources

### Understanding BDD
- **Gherkin Syntax**: Feature files use Given/When/Then structure
- **Step Definitions**: Python functions that implement Gherkin steps
- **pytest-bdd**: Framework that connects Gherkin scenarios to pytest

### Understanding pytest-playwright
- **Built-in Fixtures**: `browser`, `page`, `context` provided automatically
- **Configuration**: Command-line options for browsers, videos, screenshots
- **Best Practices**: Industry standard patterns for browser automation

### Educational Comparison
- **Custom Fixtures** (`tests/ui/playwright/pytest/`): Learn how browser automation works
- **pytest-playwright** (`tests/acceptance/bdd_playwright/`): Industry standard professional tools
- **Same Concepts**: Both use Playwright API, but different fixture management

## 🎯 Development Workflow

### Adding New BDD Scenarios

1. **Write Gherkin scenario** in `features/task_workflow_playwright.feature`
2. **Run test** to see missing step definitions
3. **Implement step definitions** in `test_playwright_pytestbdd.py`
4. **Test scenario** with `pytest -k "scenario name" tests/acceptance/bdd_playwright/ -v -o addopts=''`

### Example Development Cycle

```bash
# 1. Add new scenario to feature file
# 2. Run to see missing steps
pytest tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py -v -o addopts=''

# 3. Implement missing step definitions
# 4. Test new scenario specifically
pytest -k "new scenario name" tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py --headed -v -o addopts=''

# 5. Run full BDD suite to ensure no regressions
pytest tests/acceptance/bdd_playwright/ -v -o addopts=''
```

## 🚀 Best Practices

### Development
- ✅ Always activate virtual environment before running tests
- ✅ Start Flask server in separate terminal
- ✅ Use `--headed` mode for debugging new scenarios
- ✅ Use `--video=retain-on-failure` for failure analysis
- ✅ Run BDD tests separately from main test suite

### CI/CD
- ✅ Use direct pytest commands (not wrapper scripts)
- ✅ Generate both JUnit XML and HTML reports
- ✅ Set appropriate timeouts for browser operations
- ✅ Use headless mode for faster execution

### Maintenance
- ✅ Keep feature files focused and readable
- ✅ Use descriptive scenario names
- ✅ Implement reusable step definitions
- ✅ Document complex step implementations

---

**Professional BDD Testing with Industry Standard Tools** 🎭

📚 For more information, see the main project README and lab documentation.
