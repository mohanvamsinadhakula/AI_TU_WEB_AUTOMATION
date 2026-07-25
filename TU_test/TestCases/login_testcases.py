# TestCases/login_testcases.py

from Utilities.config import Config


LOGIN_TEST_CASES = {

    "TC_001": {
        "email": Config.VALID_EMAIL,
        "password": Config.VALID_PASSWORD,
        "expected": "Dashboard"
    },

    "TC_002": {
        "email": Config.VALID_EMAIL,
        "password": Config.INVALID_PASSWORD,
        "expected": "Invalid credentials"
    },

    "TC_003": {
        "email": Config.INVALID_EMAIL,
        "password": Config.VALID_PASSWORD,
        "expected": "Invalid credentials"
    },

    "TC_004": {
        "email": "",
        "password": "",
        "expected": "Validation message"
    },

    "TC_005": {
        "email":Config.VALID_EMAIL,
        "password":Config.VALID_PASSWORD,
        "action": "logout",
        "expected": "Login Page"
    }
}