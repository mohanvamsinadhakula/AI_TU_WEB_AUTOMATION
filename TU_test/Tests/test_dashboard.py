import time
import re
import pytest
from datetime import datetime

from Pages.dashboard_page import DashboardPage  # Ensure filename casing matches your file structure
from Pages.login_page import LoginPage
from Utilities.config import Config
from Utilities.excel_utility import ExcelUtility
from Utilities.logger import logger
from Utilities.screenshot import Screenshot

excel_loader = ExcelUtility()
all_cases = excel_loader.get_test_cases()
dashboard_cases = {tc["tc_id"]: tc for tc in all_cases if tc["module"] == "Dashboard"}
excel_loader.close()

def clean_for_excel(text):
    if not isinstance(text, str):
        return str(text)
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
    return ansi_escape.sub('', text)

@pytest.fixture(scope="module")
def logged_in_dashboard(browser):
    context = browser.new_context()
    page = context.new_page()
    
    login = LoginPage(page)
    login.open()
    login.enter_email(Config.VALID_EMAIL)
    login.enter_password(Config.VALID_PASSWORD)
    login.click_signin()
    page.wait_for_load_state("networkidle")
    
    yield page
    context.close()

@pytest.mark.order(2)
@pytest.mark.parametrize("tc_id, tc", dashboard_cases.items())
def test_dashboard(logged_in_dashboard, tc_id, tc):
    page = logged_in_dashboard
    dashboard = DashboardPage(page)
    excel = ExcelUtility()

    row = tc["row"]
    logger.info(f"========== EXECUTING {tc_id} ==========")
    start_time = time.time()
    screenshot_path = ""
    status = "FAIL"
    actual_result = "Execution thread dropped out early."

    try:
        if tc_id == "TC_006":
            dashboard.verify_dashboard_loaded()
            actual_result = "Dashboard loaded successfully"
            status = "PASS"

        elif tc_id == "TC_007":
            dashboard.open_profile()
            dashboard.verify_logout_visible()
            page.keyboard.press("Escape")
            actual_result = "Profile settings container dropdown displayed"
            status = "PASS"

        elif tc_id == "TC_008":
            dashboard.select_device()
            page.wait_for_load_state("networkidle")
            actual_result = "Selected device information loaded completely."
            status = "PASS"

        elif tc_id == "TC_009":
            dashboard.click_refresh()
            page.wait_for_load_state("networkidle")
            actual_result = "Videos refreshed successfully."
            status = "PASS"

        elif tc_id == "TC_010":
            dashboard.verify_video_summary()
            actual_result = "Video metrics rendered successfully."
            status = "PASS"

        elif tc_id == "TC_011":
            dashboard.verify_key_metrics()
            actual_result = "Key Metrics UI visible."
            status = "PASS"

        elif tc_id == "TC_012":
            dashboard.verify_peak_hourly()
            actual_result = "Peak analysis chart visible."
            status = "PASS"
        
        # ---------------- TC_032 ----------------
        elif tc_id == "TC_032":
            dashboard.click_today()
            dashboard.verify_videos_present()
            actual_result = "Today button clicked. Real-time timeline video stream rendered cleanly"
            status = "PASS"

        # ---------------- TC_033 ----------------
        elif tc_id == "TC_033":
            dashboard.click_yesterday()
            dashboard.verify_videos_present()
            actual_result = "Yesterday filter data successfully populated context from 9am to 10pm"
            status = "PASS"

        # ---------------- TC_034 ----------------
        elif tc_id == "TC_034":
            dashboard.click_all_videos()
            # Target an arbitrary past automated execution date window range (e.g., 2026-07-01 to 2026-07-22)
            dashboard.select_custom_date_range("2026-07-17", "2026-07-22")
            dashboard.verify_videos_present()
            actual_result = "Custom date window range confirmed; multi-date payload populated completely"
            status = "PASS"

        assert status == "PASS", actual_result

    except AssertionError as ae:
        status = "FAIL"
        actual_result = clean_for_excel(str(ae))
        screenshot_path = Screenshot.capture(page, tc_id)
        raise ae
    except Exception as e:
        status = "FAIL"
        actual_result = clean_for_excel(f"Runtime Crash: {str(e)}")
        screenshot_path = Screenshot.capture(page, tc_id)
        pytest.fail(f"Step Exception: {e}")
    finally:
        execution_time = round(time.time() - start_time, 2)
        try:
            excel.update_actual_result(row, clean_for_excel(actual_result))
            excel.update_status(row, status)
            excel.update_execution_time(row, f"{execution_time} sec")
            excel.update_screenshot(row, screenshot_path)
        except PermissionError:
            logger.error(f"Workbook locking conflict handled for tracking row: {tc_id}")
        finally:
            excel.close()