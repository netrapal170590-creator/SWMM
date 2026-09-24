# Basic Pytest + Playwright Project

## Structure

```text
pages/          Page objects and page actions
tests/          Test cases
report/         Test report output folder
config/         URL and runtime settings
conftest.py     Shared Playwright fixtures
pytest.ini      Pytest settings
requirements.txt
```

## First-time setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
```

If PowerShell blocks activation, run this first in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
```

## Run tests

```powershell
pytest
```

The default URL is `http://172.16.40.161/landing`.

For the login test, set the password only in the terminal:

```powershell
$env:APP_USERNAME = "ADMIN"
$env:APP_PASSWORD = "your-password"
pytest tests/test_login.py -v
```

Do not save passwords in Python files or commit them to GitHub.

## Add a new test

1. Add a page class in `pages`.
2. Add a test file in `tests`.
3. Run the test with `pytest tests/test_name.py -v`.

Use Playwright Codegen to find selectors:

```powershell
playwright codegen http://172.16.40.161/landing
```
