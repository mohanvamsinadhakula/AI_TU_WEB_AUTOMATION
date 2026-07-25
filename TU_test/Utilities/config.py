# Utilities/config.py

class Config:
    # Application URL
    BASE_URL = "https://www.third-umpire.com/"

    # Login Credentials
    VALID_EMAIL = "vijay.kumar@sclabsglobal.com"
    VALID_PASSWORD = "vijay@2026"

    INVALID_EMAIL = "invalid@gmail.com"
    INVALID_PASSWORD = "Invalid@123"

    # Browser Settings
    BROWSER = "chromium"
    HEADLESS = False
    SLOW_MO = 300

    # Timeouts
    TIMEOUT = 30000

    # Paths
    SCREENSHOT_FOLDER = "Screenshots"
    REPORT_FOLDER = "Reports"
    EXCEL_FILE = "TestData/Login_TestCases.xlsx"