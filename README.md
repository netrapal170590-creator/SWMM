# Basic Pytest + Playwright Framework

## Structure

```text
pages/          Page objects
tests/          Test cases
conftest.py     Shared browser fixtures
pytest.ini      Pytest settings
requirements.txt
```

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
```

## Run

```powershell
pytest
```

The default application URL is `http://172.16.40.161/landing`. Override it
before running tests when needed:

```powershell
$env:BASE_URL = "http://localhost:8000"
$env:HEADLESS = "false"
pytest -v
```

Create new page objects in `pages` and test cases in `tests`.
