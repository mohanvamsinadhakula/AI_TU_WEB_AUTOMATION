import time
import pytest

from Pages.login_page import LoginPage
from Pages.bookmarks_page import BookmarksPage
from Utilities.config import Config
from Utilities.excel_utility import ExcelUtility
from Utilities.screenshot import Screenshot
from Utilities.logger import logger

@pytest.mark.order(7)
def test_bookmarks(page):

    # Initialize frameworks and utilities
    login = LoginPage(page)
    bookmarks = BookmarksPage(page)
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

    for tc in test_cases:
        # Filter execution stream strictly for Bookmarks module entries
        if tc["module"] != "Bookmarks":
            continue

        row = tc["row"]
        tc_id = tc["tc_id"]

        logger.info(f"Executing {tc_id}")
        start_time = time.time()
        
        screenshot_path = ""
        status = "FAIL"
        actual_result = "Test step encountered an unexpected processing roadblock."

        try:
            # Navigate to the Bookmarks UI space if a sub-test demands clean entry state
            bookmarks.open_bookmarks()

            # ---------------- TC_013 ----------------
            if tc_id == "TC_013":
                bookmarks.verify_bookmarks_loaded()
                actual_result = "Bookmarks landing panel rendered successfully"
                status = "PASS"

            # ---------------- TC_014 ----------------
            elif tc_id == "TC_014":
                bookmarks.search_bookmark("Sample Text")
                bookmarks.verify_search_results()
                actual_result = "Search results localized matching sample filter data text"
                status = "PASS"

            # ---------------- TC_015 ----------------
            elif tc_id == "TC_015":
                bookmarks.click_refresh()
                page.wait_for_timeout(3000)
                actual_result = "Refresh element processed; dataset reloaded cleanly"
                status = "PASS"

            # ---------------- TC_016 ----------------
            elif tc_id == "TC_016":
                bookmarks.select_camera_filter()
                bookmarks.verify_camera_filter()
                page.wait_for_timeout(3000)
                actual_result = "Camera contextual element filter targeted and deployed"
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
            # Trap failures smoothly to record exceptions directly inside Excel logs
            execution_time = round(time.time() - start_time, 2)
            screenshot_path = Screenshot.capture(page, tc_id)

            excel.update_actual_result(row, str(e))
            excel.update_status(row, "FAIL")
            excel.update_execution_time(row, f"{execution_time} sec")
            excel.update_screenshot(row, screenshot_path)

            logger.error(f"{tc_id} Failed : {e}")

    excel.close()