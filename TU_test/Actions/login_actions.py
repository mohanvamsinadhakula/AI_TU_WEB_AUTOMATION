import time

from Pages.login_page import LoginPage
from Utilities.config import EMAIL, PASSWORD


class LoginActions:

    def __init__(self, page):

        self.page = page
        self.login = LoginPage(page)

    # ======================================================
    # TC_001
    # Valid Login
    # ======================================================
    def tc_001(self):

        self.login.open()

        self.login.login(
            EMAIL,
            PASSWORD
        )

        assert self.login.is_dashboard_visible()

        return "Dashboard displayed successfully"

    # ======================================================
    # TC_002
    # Invalid Password
    # ======================================================
    def tc_002(self):

        self.login.open()

        self.login.login(
            EMAIL,
            "WrongPassword123"
        )

        assert self.login.is_invalid_login()

        return "Invalid credentials message displayed"

    # ======================================================
    # TC_003
    # Invalid Username
    # ======================================================
    def tc_003(self):

        self.login.open()

        self.login.login(
            "invalid@gmail.com",
            PASSWORD
        )

        assert self.login.is_invalid_login()

        return "Invalid credentials message displayed"

    # ======================================================
    # TC_004
    # Empty Credentials
    # ======================================================
    def tc_004(self):

        self.login.open()

        self.login.click_signin()

        email_validation = self.login.email_validation()

        assert email_validation != ""

        return email_validation

    # ======================================================
    # TC_005
    # Logout
    # ======================================================
    def tc_005(self):

        self.login.open()

        self.login.login(
            EMAIL,
            PASSWORD
        )

        assert self.login.is_dashboard_visible()

        time.sleep(2)

        self.login.logout()

        return "Logout successful"

    # ======================================================
    # Dispatcher
    # ======================================================
    def execute(self, tc_id):

        actions = {

            "TC_001": self.tc_001,
            "TC_002": self.tc_002,
            "TC_003": self.tc_003,
            "TC_004": self.tc_004,
            "TC_005": self.tc_005,

        }

        if tc_id not in actions:

            raise Exception(f"{tc_id} is not implemented.")

        return actions[tc_id]()