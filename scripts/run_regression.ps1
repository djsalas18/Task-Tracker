<#
Run-regression.ps1

Purpose: Run PR-7 final regression in discrete batches and collect logs.

Usage (PowerShell):
  .\scripts\run_regression.ps1

#>

param()

Write-Host "Starting PR-7 final regression run..."

# Ensure TESTING mode (isolated DB)
$env:TESTING = 'true'

# Activate venv if available
if (Test-Path -Path ".venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..."
    & ".venv\Scripts\Activate.ps1"
}

New-Item -ItemType Directory -Path test-results -Force | Out-Null

function Run-Batch {
    param(
        [string]$Name,
        [string]$Args
    )
    Write-Host "\n== Running: $Name =="
    $outfile = "test-results\$($Name -replace '[^a-zA-Z0-9]', '_').txt"
    pytest $Args 2>&1 | Tee-Object -FilePath $outfile
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Batch '$Name' FAILED (exit $LASTEXITCODE). See $outfile" -ForegroundColor Red
    } else {
        Write-Host "Batch '$Name' passed. Output saved to $outfile" -ForegroundColor Green
    }
    return $LASTEXITCODE
}

# Core regression
$rc = Run-Batch -Name "core_api_unit_integration" -Args "tests/api tests/unit tests/integration -q"
if ($rc -ne 0) { exit $rc }

# UI Playwright
$rc = Run-Batch -Name "ui_playwright" -Args "tests/e2e/ui/playwright/pytest -q"
if ($rc -ne 0) { Write-Host "Playwright failures detected; continue to run Selenium for comparison" -ForegroundColor Yellow }

# UI Selenium
$rc2 = Run-Batch -Name "ui_selenium" -Args "tests/e2e/ui/selenium/pytest -q"
if ($rc2 -ne 0) { Write-Host "Selenium failures detected" -ForegroundColor Yellow }

# Acceptance (BDD / Robot)
$rc3 = Run-Batch -Name "acceptance_bdd_playwright" -Args "tests/e2e/acceptance/bdd_playwright -q"
if ($rc3 -ne 0) { Write-Host "BDD failures detected" -ForegroundColor Yellow }

Write-Host "\nRegression run complete. Check the test-results directory for outputs and failing traces." -ForegroundColor Cyan

if ($rc -eq 0 -and $rc2 -eq 0 -and $rc3 -eq 0) { exit 0 } else { exit 1 }
