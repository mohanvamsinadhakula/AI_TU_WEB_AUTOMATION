# AI_TU_WEB_AUTOMATION

This repository contains the Python Playwright Automation Framework for testing the **Third Umpire Retail Analytics Web Application**.

---

# Project Structure

```text
TU_test/
│
├── Actions/
│   ├── login_actions.py
│   ├── dashboard_actions.py
│   └── __pycache__/
│
├── Pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── Device_stats_page.py
│   └── __pycache__/
│
├── TestCases/
│   ├── login_testcases.py
│   ├── dashboard_testcases.py
│   ├── device_stats_testcases.py
│   ├── login_validation.py
│   └── __pycache__/
│
├── Tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│   ├── test_devicestats.py
│   └── __pycache__/
│
├── TestData/
│   └── Login_TestCases.xlsx
│
├── Utilities/
│   ├── config.py
│   ├── excel_utility.py
│   ├── logger.py
│   ├── screenshot.py
│   ├── test_data.py
│   └── __pycache__/
│
├── Reports/
│   └── report.html
│
├── Logs/
│   └── log.txt
│
├── Screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Folder Description

## Actions/

Contains reusable business logic for each module.

**Files**

- `login_actions.py`
- `dashboard_actions.py`

---

## Pages/

Contains Page Object Model (POM) classes with locators and page methods.

**Files**

- `login_page.py`
- `dashboard_page.py`
- `Device_stats_page.py`

---

## TestCases/

Stores all automation test case definitions and expected results.

**Files**

- `login_testcases.py`
- `dashboard_testcases.py`
- `device_stats_testcases.py`
- `login_validation.py`

---

## Tests/

Contains all executable Pytest test scripts.

**Files**

- `test_login.py`
- `test_dashboard.py`
- `test_devicestats.py`

---

## TestData/

Contains Excel sheets used for Data-Driven Testing.

**Files**

- `Login_TestCases.xlsx`

---

## Utilities/

Contains reusable helper classes.

**Files**

- `config.py`
- `excel_utility.py`
- `logger.py`
- `screenshot.py`
- `test_data.py`

---

## Reports/

Stores generated HTML execution reports.

Example:

```
report.html
```

---

## Logs/

Stores execution logs.

Example:

```
log.txt
```

---

## Screenshots/

Stores screenshots captured during failed test execution.

---

# Configuration Files

## conftest.py

Contains:

- Pytest Fixtures
- Browser Initialization
- Browser Cleanup
- Shared Test Configuration

---

## pytest.ini

Contains:

- Pytest Configuration
- Report Configuration
- Markers
- Logging Configuration

---

## requirements.txt

Contains all Python dependencies required to execute the framework.

Example:

```text
playwright
pytest
pytest-html
pytest-order
openpyxl
```

---

## README.md

Project documentation describing the framework, folder structure, setup, and execution steps.

---

# Framework Architecture

```text
Tests
   │
   ▼
Actions
   │
   ▼
Pages
   │
   ▼
Third Umpire Web Application
   │
   ▼
Assertions
   │
   ▼
Reports
Logs
Screenshots
```

---

# Technologies Used

- Python 3.x
- Playwright
- Pytest
- Pytest HTML Report
- OpenPyXL
- Page Object Model (POM)
- Data-Driven Testing (Excel)

---

# Features

- Page Object Model (POM)
- Modular Framework
- Reusable Page Methods
- Data-Driven Testing
- HTML Reports
- Screenshot on Failure
- Logging
- Easy Maintenance
- Scalable Project Structure

---

# Execution

Run all test cases:

```bash
pytest
```

Run a specific test file:

```bash
pytest Tests/test_dashboard.py
```

Generate HTML Report:

```bash
pytest --html=Reports/report.html --self-contained-html
```

---

# Author

**AI_TU_WEB_AUTOMATION**
**MOHAN VAMSI NADH AKULA**
