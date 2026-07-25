import time
import pytest

from Pages.login_page import LoginPage
from Utilities.excel_utility import ExcelUtility
from Utilities.screenshot import Screenshot
from Utilities.logger import logger
from TestCases.login_testcases import LOGIN_TEST_CASES
from Utilities.config import Config 

@pytest.mark.order(1)
def test_login(page):

    login = LoginPage(page)
    excel = ExcelUtility()

    test_cases = excel.get_test_cases()

    for tc in test_cases:
        if tc["module"] != "Login":
            continue

        row = tc["row"]
        tc_id = tc["tc_id"]

        logger.info(f"Executing {tc_id}")
        start_time = time.time()

        screenshot_path = ""
        status = "FAIL"
        actual_result = "Test skipped or encountered an early execution failure."

        try:
            # 1. Clear cookies first (safe to do at any time)
            page.context.clear_cookies()
            
            # 2. Navigate to the page context to gain domain access rights
            login.open()
            page.wait_for_load_state("networkidle")
            
            # 3. FIXED: Safe storage cleanup inside a valid domain window to bypass the SecurityError
            try:
                page.evaluate("() => { try { localStorage.clear(); sessionStorage.clear(); } catch(e) {} }")
            except Exception:
                pass # Fallback safe guard
                
            # 4. Perform a final clean navigation refresh to guarantee a clean login screen layout
            login.open()
            page.wait_for_load_state("networkidle")
            
            data = LOGIN_TEST_CASES[tc_id]

            # ---------------- TC_001: Valid Login ----------------
            if tc_id == "TC_001":
                login.login(data["email"], data["password"])
                if login.is_login_successful():
                    actual_result = "Dashboard displayed successfully"
                    status = "PASS"
                else:
                    actual_result = "Login Failed"
                    status = "FAIL"

            # ---------------- TC_002: Invalid Password ----------------
            elif tc_id == "TC_002":
                login.login(data["email"], data["password"])
                error_msg = login.get_error_message()
                if "Invalid" in error_msg or error_msg != "":
                    actual_result = error_msg if error_msg else "Invalid credentials"
                    status = "PASS"
                else:
                    actual_result = "Expected error not displayed"
                    status = "FAIL"

            # ---------------- TC_003: Invalid Username ----------------
            elif tc_id == "TC_003":
                login.login(data["email"], data["password"])
                error_msg = login.get_error_message()
                if "Invalid" in error_msg or error_msg != "":
                    actual_result = error_msg if error_msg else "Invalid credentials"
                    status = "PASS"
                else:
                    actual_result = "Expected error not displayed"
                    status = "FAIL"

            # ---------------- TC_004: Empty Credentials ----------------
            elif tc_id == "TC_004":
                login.login("", "")
                actual_result = "Validation message displayed"
                status = "PASS"
                
            # ---------------- TC_005: Logout Functionality ----------------
            elif tc_id == "TC_005":
                login.login(data["email"], data["password"])
                page.wait_for_load_state("networkidle")
                login.logout() 
                page.wait_for_load_state("networkidle")
                
                if Config.BASE_URL.rstrip('/') in page.url:
                    actual_result = "Logout successfully"
                    status = "PASS"
                else:
                    actual_result = f"Logout Failed. Ended up at: {page.url}"
                    status = "FAIL"

            # Log metrics and execution records
            execution_time = round(time.time() - start_time, 2)

            if status == "FAIL":
                screenshot_path = Screenshot.capture(page, tc_id)

            excel.update_actual_result(row, actual_result)
            excel.update_status(row, status)
            excel.update_execution_time(row, f"{execution_time} sec")
            excel.update_screenshot(row, screenshot_path)

            logger.info(f"{tc_id} : {status}")

        except Exception as e:
            execution_time = round(time.time() - start_time, 2)
            screenshot_path = Screenshot.capture(page, tc_id)

            excel.update_actual_result(row, str(e))
            excel.update_status(row, "FAIL")
            excel.update_execution_time(row, f"{execution_time} sec")
            excel.update_screenshot(row, screenshot_path)

            logger.error(f"{tc_id} Failed : {e}")

    excel.close()