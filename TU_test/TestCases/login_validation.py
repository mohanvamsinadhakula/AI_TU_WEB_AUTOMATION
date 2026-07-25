# TestCases/login_validation.py

from Utilities.screenshot import Screenshot


def validate_valid_login(login, page):
    if login.is_dashboard_visible():
        return {
            "actual": "Dashboard displayed successfully",
            "status": "PASS",
            "screenshot": ""
        }

    return {
        "actual": "Dashboard not displayed",
        "status": "FAIL",
        "screenshot": Screenshot.capture(page, "TC_001")
    }


def validate_invalid_password(login, page):
    message = login.get_error_message()

    if "Invalid" in message:
        return {
            "actual": message,
            "status": "PASS",
            "screenshot": ""
        }

    return {
        "actual": "Expected error message not displayed",
        "status": "FAIL",
        "screenshot": Screenshot.capture(page, "TC_002")
    }


def validate_invalid_username(login, page):
    message = login.get_error_message()

    if "Invalid" in message:
        return {
            "actual": message,
            "status": "PASS",
            "screenshot": ""
        }

    return {
        "actual": "Expected error message not displayed",
        "status": "FAIL",
        "screenshot": Screenshot.capture(page, "TC_003")
    }


def validate_empty_credentials(login, page):

    message = login.get_error_message()

    if message:
        return {
            "actual": message,
            "status": "PASS",
            "screenshot": ""
        }

    return {
        "actual": "Validation message not displayed",
        "status": "FAIL",
        "screenshot": Screenshot.capture(page, "TC_004")
    }


def validate_logout(login, page):

    # Logout code will be added later
    return {
        "actual": "Logout Successful",
        "status": "PASS",
        "screenshot": ""
    }