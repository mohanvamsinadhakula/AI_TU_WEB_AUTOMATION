import time
import pytest

from Pages.login_page import LoginPage
from Pages.settings_page import SettingsPage
from Utilities.config import Config
from Utilities.excel_utility import ExcelUtility
from Utilities.screenshot import Screenshot
from Utilities.logger import logger

# Helper initialization to extract test parameters before fixtures initialize
excel_loader = ExcelUtility()
all_cases = excel_loader.get_test_cases()
settings_cases = {tc["tc_id"]: tc for tc in all_cases if tc["module"] == "Settings"}
excel_loader.close()


@pytest.fixture(scope="module")
def excel_reporter():
    excel = ExcelUtility()
    yield excel
    excel.save()
    excel.close()


@pytest.fixture(scope="module")
def logged_in_page(browser):
    context = browser.new_context()
    page = context.new_page()
    
    logger.info("Opening Login Page for Settings Context")
    login = LoginPage(page)
    login.open()
    login.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
    page.wait_for_load_state("networkidle")
    
    yield page
    context.close()


@pytest.mark.order(4)
@pytest.mark.parametrize("tc_id, tc", settings_cases.items())
def test_settings(logged_in_page, excel_reporter, tc_id, tc):
    page = logged_in_page
    excel = excel_reporter
    settings = SettingsPage(page)

    logger.info(f"========== EXECUTING {tc_id} ==========")
    start_time = time.time()
    status = "FAIL"
    actual_result = "Test pipeline drop-out."
    screenshot_path = ""

    try:
        # Route to settings workspace context cleanly if not already initialized
        if "settings" not in page.url.lower():
            settings.open_settings()
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1000)

        # ---------------- TC_022 ----------------
        if tc_id == "TC_022":
            settings.verify_settings_loaded()
            actual_result = "Settings page opened and verified successfully"
            status = "PASS"

        # ---------------- TC_023 ----------------
        elif tc_id == "TC_023":
            settings.open_profile_section()
            settings.verify_profile_section()
            actual_result = "Profile section expanded and verified successfully"
            status = "PASS"

        # ---------------- TC_024 ----------------
        elif tc_id == "TC_024":
            settings.open_notifications()
            settings.verify_notifications()
            actual_result = "Notifications section opened and options verified cleanly"
            status = "PASS"

        # ---------------- TC_025 ----------------
        elif tc_id == "TC_025":
            settings.open_video_settings()
            settings.verify_video_settings()
            actual_result = "Video settings panel expanded and checked completely"
            status = "PASS"

        # ---------------- TC_026 ----------------
        elif tc_id == "TC_026":
            settings.open_data_management()
            settings.verify_data_management()
            actual_result = "Data management configuration tools verified successfully"
            status = "PASS"

        # ---------------- TC_027 ----------------
        elif tc_id == "TC_027":
            settings.click_save_changes()
            settings.verify_save_success()
            page.wait_for_timeout(2000)
            actual_result = "Changes successfully saved and system alert validated"
            status = "PASS"

    except Exception as e:
        logger.error(f"{tc_id} Failed : {e}")
        actual_result = str(e)
        screenshot_path = Screenshot.capture(page, tc_id)
        status = "FAIL"

    execution_time = round(time.time() - start_time, 2)

    # --------------------------------------------
    # Centralized Tracker Syncing
    # --------------------------------------------
    row = tc["row"]
    excel.update_actual_result(row, actual_result)
    excel.update_status(row, status)
    excel.update_execution_time(row, f"{execution_time} sec")
    excel.update_screenshot(row, screenshot_path)

    logger.info(f"{tc_id} result: {status}")

    if status == "FAIL":
        pytest.fail(f"Test step failed: {actual_result}")