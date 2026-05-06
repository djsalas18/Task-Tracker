# Task Tracker Application - Group Project Start

A comprehensive Flask-based task management application demonstrating modern software engineering practices, including Test-Driven Development (TDD), Behavior-Driven Development (BDD), and comprehensive automated testing.

## 🎯 Project Overview

This is a learning project that demonstrates:
- **Flask Web Application** - Full-stack task management system
- **Test-Driven Development (TDD)** - Unit, integration, and API testing
- **Behavior-Driven Development (BDD)** - Acceptance testing with pytest-bdd + Playwright
- **Multiple UI Testing Frameworks** - Selenium and Playwright comparison
- **CI/CD Pipeline** - GitHub Actions with comprehensive test automation
- **Database Integration** - SQLAlchemy with SQLite
- **Professional Code Structure** - Application factory pattern, dependency injection

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ (recommended: 3.13.5)
- Virtual environment (required)

The commands in this guide are IDE-agnostic and work from any terminal (PowerShell, Git Bash, macOS/Linux shell, VS Code terminal, or PyCharm terminal).

### Setup

1. **Clone and navigate to your project:**
   ```bash
   cd your-repo-directory
   ```

2. **Create and activate virtual environment:**
   ```powershell
   # PowerShell (Windows)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   
   ```bash
   # Git Bash / Linux / macOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers (for UI testing):**
   ```bash
   playwright install chromium
   ```

5. **Run the application:**
   ```bash
   python -m app.main
   ```

6. **Access the application:**
   - Web Interface: http://localhost:5000
   - API Health Check: http://localhost:5000/api/health

## 🧪 Testing Strategy

This project demonstrates comprehensive testing at multiple levels with **proper test separation**:

### Test Separation Overview

The project uses **industry standard test separation** to prevent conflicts:

- **Main Test Suite (80+ tests)**: Unit, integration, API, and UI tests using sync fixtures
- **BDD Acceptance Tests**: Separate test suite using async pytest-playwright fixtures
- **pytest.ini Configuration**: Excludes BDD tests from main runs to prevent asyncio conflicts

### Running Tests

#### Main Test Suite (Recommended for Daily Development)
```bash
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate    # Linux/macOS

# Run all main tests (excludes BDD tests via pytest.ini)
pytest -v

# Run specific test categories
pytest tests/api/ -v                    # API tests only
pytest tests/ui/selenium/ -v            # Selenium UI tests
pytest tests/ui/playwright/ -v          # Playwright UI tests (custom fixtures)
pytest tests/storage/ -v                # Database tests
```

#### BDD Acceptance Tests (Separate Test Suite)
```bash
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate    # Linux/macOS

# Start Flask server in separate terminal
python -m app.main

# Run BDD tests separately (requires pytest-playwright)
# Note: -o addopts='' bypasses global pytest.ini ignores for this suite
pytest tests/acceptance/bdd_playwright/ -v -o addopts=''

# BDD tests with advanced features
pytest tests/acceptance/bdd_playwright/ --headed --browser=firefox -v -o addopts=''
pytest tests/acceptance/bdd_playwright/ --html=results/bdd_report.html --self-contained-html -v -o addopts=''
```

#### BDD Acceptance Tests via Helper Scripts (From Repo Root)
```bash
# Confirm you are at repository root first
# Windows PowerShell: pwd
# Git Bash/Linux/macOS: pwd

# PowerShell (from repo root)
.\test_helpers\bdd_pytest.ps1
.\test_helpers\bdd_pytest.ps1 -Headed
.\test_helpers\bdd_pytest.ps1 -JUnit -Html

# Git Bash/Linux/macOS (from repo root)
bash ./test_helpers/bdd_pytest.sh
bash ./test_helpers/bdd_pytest.sh --headed
bash ./test_helpers/bdd_pytest.sh --junit --html
```

Notes:
- If you run from repo root, include `test_helpers/` in the script path.
- `bdd_pytest.ps1` or `bdd_pytest.sh` by itself will fail unless that folder is your current directory.

#### Coverage Report
```bash
# Generate coverage report (main test suite)
pytest --cov=app --cov-report=html --cov-report=term-missing
```

### Why Test Separation?

- ✅ **Prevents Conflicts**: Avoids asyncio issues between sync and async test fixtures
- ✅ **Optimizes Performance**: Main test suite runs fast (80+ tests in ~30 seconds)
- ✅ **Professional Practice**: Different test types serve different purposes
- ✅ **Clear Boundaries**: Unit/integration tests vs. end-to-end acceptance tests

## 📁 Project Structure Handover

Use the root README as the source of truth for full repository layout.

This handover section highlights only the directories new team members use first:

```text
app/                    Flask application (routes, services, models, templates)
tests/                  Automated tests (api, ui, acceptance, storage, tasks, health)
docs/handover/          Baseline architecture + setup + API reference + user journey
docs/sprint1..sprint4/  Sprint plans and artifacts
test_helpers/           BDD helper scripts for local execution
requirements.txt        Python dependencies
pytest.ini              Shared pytest configuration
```

Handover quick map:
- Setup and local run instructions: docs/handover/developer_setup.md
- API documentation: docs/handover/group_project_api_reference.md
- Architecture baseline: docs/handover/group_project_start_architecture.md
- Class diagram: docs/handover/group_project_start_class_diagram.md
- ERD: docs/handover/group_project_erd.md
- Test strategy and cases: docs/handover/group_project_test_strategy.md, docs/handover/group_project_start_test_cases.md

## 🔧 Technology Stack

### Core Framework
- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **Jinja2** - Template engine

### Testing Frameworks
- **pytest** - Test runner and framework
- **pytest-bdd** - BDD testing with Gherkin scenarios
- **pytest-playwright** - Industry standard Playwright plugin  
- **Playwright** - Modern browser automation
- **Selenium** - Cross-browser testing (educational comparison)
- **pytest-html** - HTML test reports
- **pytest-cov** - Code coverage

### Development Tools
- **Black** - Code formatting
- **Flake8** - Code linting
- **MyPy** - Type checking

## 🎭 BDD Acceptance Testing

This project includes **Behavior-Driven Development (BDD)** testing for end-to-end acceptance scenarios using pytest-bdd and pytest-playwright.

### BDD Overview
- **Purpose**: End-to-end acceptance testing with business-readable scenarios
- **Tools**: pytest-bdd + pytest-playwright (industry standard)
- **Separation**: Runs independently from main test suite to prevent conflicts
- **Features**: Video recording, screenshots, cross-browser testing, rich reporting

### Quick BDD Usage
```bash
# Start Flask server (separate terminal)
python -m app.main

# Run BDD acceptance tests
pytest tests/acceptance/bdd_playwright/ -v -o addopts=''
```

📚 **[Complete BDD Setup & Usage Guide →](../../tests/acceptance/bdd_playwright/README.md)**

## 🚀 CI/CD Pipeline

GitHub Actions workflow includes:
- **Unit Tests** - Fast, isolated component testing
- **Integration Tests** - API endpoint testing  
- **UI Tests** - Selenium and Playwright browser testing
- **BDD Tests** - End-to-end acceptance testing (separate workflow)
- **Code Coverage** - Coverage reporting with artifacts
- **Cross-Platform** - Linux (Ubuntu) testing environment

## 📊 Test Reports

Generated reports include:
- **HTML Coverage Report** - `htmlcov/index.html`
- **Pytest HTML Report** - `results/report.html`  
- **JUnit XML** - `results/junit.xml`
- **BDD Reports** - Rich media reports (see BDD documentation)

## 🛠️ Development Workflow

1. **Create feature branch:**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Write tests first (TDD):**
   ```bash
   # Write failing test
   pytest tests/test_new_feature.py::test_new_functionality -v
   ```

3. **Implement feature:**
   ```bash
   # Implement code to make test pass
   pytest tests/test_new_feature.py::test_new_functionality -v
   ```

4. **Run full test suite:**
   ```bash
   # Main test suite (excludes BDD)
   pytest -v
   
   # BDD tests separately (if relevant to feature)
   pytest tests/acceptance/bdd_playwright/ -v -o addopts=''
   ```

5. **Create pull request and wait for CI:**
   - All tests must pass
   - Coverage thresholds must be met

## 🎓 Educational Features

This project demonstrates:
- **Test Pyramid** - Unit → Integration → UI → BDD
- **Test Separation** - Appropriate tools for different test types
- **Clean Architecture** - Separation of concerns
- **Dependency Injection** - Testable design patterns
- **Factory Pattern** - Flask application factory
- **Repository Pattern** - Data access abstraction
- **Service Layer** - Business logic separation
- **Continuous Integration** - Automated testing pipeline

## 🔧 Environment Management

### Virtual Environment Best Practices

**Critical for Complex Testing:**
The virtual environment becomes increasingly important as you add testing frameworks:

```bash
# Always activate before any Python commands
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# .\.venv\Scripts\activate.bat  # Windows CMD
# source .venv/bin/activate     # Linux/macOS

# Verify activation (should show .venv path)
which python  # Linux/macOS
where python  # Windows

# Install dependencies in isolated environment
pip install -r requirements.txt
```

**Why Virtual Environment Discipline Matters:**
- 🔒 **Isolation**: Prevents package conflicts between projects
- 🎯 **Consistency**: Ensures same versions across development/CI
- 🛡️ **Protection**: Avoids polluting system Python installation
- 🔄 **Reproducibility**: Enables reliable environment recreation

## 🐛 Troubleshooting

### Common Issues

1. **Flask server not starting:**
   ```bash
   # Check if virtual environment is activated (should show (.venv))
   pip install -r requirements.txt
   ```

2. **Test separation issues:**
   ```bash
   # Run main tests and BDD tests separately
   pytest -v                                    # Main tests only
   pytest tests/acceptance/bdd_playwright/ -v -o addopts=''   # BDD tests only
   ```

3. **Virtual environment issues:**
   ```bash
   # Recreate virtual environment
   python -m venv .venv
   # Activate and reinstall dependencies
   ```

4. **Database issues:**
   ```bash
   # Remove database file to reset
   rm tasks.db        # Linux/macOS
   del tasks.db       # Windows
   ```

### Environment Verification

```bash
# Check Flask application health
curl http://localhost:5000/api/health
```

## 📚 Documentation


### Sprint Documentation
Each sprint includes comprehensive documentation:
- **Sprint Plans** - Sprint objectives and deliverables
- **API References** - Current API endpoint documentation  
- **Architecture Documentation** - System design and patterns
- **Class Diagrams** - UML class relationships (Mermaid)
- **ERD Diagrams** - Entity relationship diagrams (Mermaid)
- **Test Cases** - Detailed test case specifications
- **Test Plans** - Testing strategy and execution plans
- **User Journey Documentation** - User flow and experience mapping

### Technical Guides
- **BDD Testing Guide** - [tests/acceptance/bdd_playwright/README.md](../../tests/acceptance/bdd_playwright/README.md)


## 📝 License

This is an educational project for learning software engineering practices.

## 🙋‍♂️ Support

For issues or questions:
1. Check the **sprint documentation** in `docs/sprint#/` directories
2. Review **lab instructions** in `labs/` directory  
3. Check **test plans and cases** for testing guidance
4. Review test output and error messages
5. Verify virtual environment is activated
6. Ensure Flask server is running for integration tests
7. See **BDD documentation** for acceptance testing issues

---

**Sprint 4 - Complete Test Automation Suite with Professional Test Separation** 🎯
