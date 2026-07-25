import time
import pytest

from Pages.login_page import LoginPage
from Pages.about_page import AboutPage
from Utilities.config import Config
from Utilities.excel_utility import ExcelUtility
from Utilities.screenshot import Screenshot
from Utilities.logger import logger

@pytest.mark.order(10)
def test_about(page):

    # Initialize frameworks and page object utilities
    login = LoginPage(page)
    about = AboutPage(page)
    excel = ExcelUtility()

    # -------------------------
    # Authentication & Environment Setup
    # -------------------------
    login.open()
    login.enter_email(Config.VALID_EMAIL)
    login.enter_password(Config.VALID_PASSWORD)
    login.click_signin()
    page.wait_for_load_state("networkidle")

    # Fetch targeted test cases from Excel sheet
    test_cases = excel.get_test_cases()

    # FIX: Track if we have already opened the page to prevent repeated destructive clicking
    about_page_opened = False

    for tc in test_cases:
        # Filter execution stream strictly for About module entries
        if tc["module"] != "About":
            continue

        row = tc["row"]
        tc_id = tc["tc_id"]

        logger.info(f"Executing {tc_id}")
        start_time = time.time()
        
        screenshot_path = ""
        status = "FAIL"
        actual_result = "Test step encountered an unexpected processing roadblock."

        try:
            # FIX: Only click the sidebar menu link the very first time!
            if not about_page_opened:
                about.open_about()
                page.wait_for_load_state("networkidle")
                # Add a micro fallback timeout to let animations clear completely
                page.wait_for_timeout(1000) 
                about_page_opened = True

            # ---------------- TC_028 ----------------
            if tc_id == "TC_028":
                about.verify_about_loaded()
                actual_result = "About page opened successfully"
                status = "PASS"

            # ---------------- TC_029 ----------------
            elif tc_id == "TC_029":
                about.verify_web_application_version()
                actual_result = "Application version should be displayed"
                status = "PASS"

            # ---------------- TC_030 ----------------
            elif tc_id == "TC_030":
                about.verify_device_software_version()
                actual_result = "Device software version should be displayed"
                status = "PASS"

            # ---------------- TC_031 ----------------
            elif tc_id == "TC_031":
                about.download_excel()
                about.verify_excel_download()
                page.wait_for_timeout(3000)
                actual_result = "Excel report should be downloaded successfully"
                status = "PASS"

            # Calculate metrics and handle formatting post-processing
            execution_time = round(time.time() - start_time, 2)

            if status == "FAIL":
                screenshot_path = Screenshot.capture(page, tc_id)

            excel.update_actual_result(row, actual_result)
            excel.update_status(row, status)
            excel.update_execution_time(row, f"{execution_time} sec")
            excel.update_screenshot(row, screenshot_path)

            logger.info(f"{tc_id} : {status}")

        except Exception as e:
            # Trap runtime exceptions smoothly to record failures straight to the log sheet
            execution_time = round(time.time() - start_time, 2)
            screenshot_path = Screenshot.capture(page, tc_id)

            excel.update_actual_result(row, str(e))
            excel.update_status(row, "FAIL")
            excel.update_execution_time(row, f"{execution_time} sec")
            excel.update_screenshot(row, screenshot_path)

            logger.error(f"{tc_id} Failed : {e}")

    excel.close()
    