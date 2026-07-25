# Tests/test_devicestats.py

import time
import pytest

from Pages.login_page import LoginPage
from Pages.Device_stats_page import DeviceStatsPage

from Utilities.config import Config
from Utilities.excel_utility import ExcelUtility
from Utilities.logger import logger
from Utilities.screenshot import Screenshot

from TestCases.device_stats_testcases import DEVICE_STATS_TEST_CASES


# Setup a shared fixture to handle Excel file reading and saving cleanly
@pytest.fixture(scope="module")
def excel_reporter():
    excel = ExcelUtility()
    yield excel
    excel.save()
    excel.close()


# Shared fixture to handle login once so you don't log in repeatedly for every single test case
@pytest.fixture(scope="module")
def logged_in_page(browser):
    context = browser.new_context()
    page = context.new_page()
    
    logger.info("Opening Login Page")
    login = LoginPage(page)
    login.open()
    login.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
    page.wait_for_load_state("networkidle")
    logger.info("Login Successful")
    
    yield page
    context.close()


@pytest.mark.order(3)
# This dynamic parameterization turns every dictionary item into an independent pytest execution
@pytest.mark.parametrize("tc_id, tc", DEVICE_STATS_TEST_CASES.items())
def test_device_stats(logged_in_page, excel_reporter, tc_id, tc):

    page = logged_in_page
    excel = excel_reporter
    device = DeviceStatsPage(page)

    api_responses = {}

    def capture_response(response):
        try:
            url = response.url
            if any(x in url.lower() for x in ["device", "stats", "cpu", "ram", "temperature", "metrics"]):
                api_responses[url] = {"status": response.status}
        except Exception:
            pass

    page.on("response", capture_response)

    logger.info(f"========== EXECUTING {tc_id} ==========")
    start = time.time()
    status = "FAIL"
    actual_result = ""
    screenshot = ""

    try:
        action = tc["action"]

        # --------------------------------------------
        # TC_017
        # --------------------------------------------
        if action == "device_stats_navigation":
            device.open_device_stats()
            device.is_device_stats_page_loaded()
            device.verify_complete_device_stats_page()
            assert device.verify_api_response(api_responses)
            actual_result = "Device Stats page opened successfully."

        # --------------------------------------------
        # TC_018
        # --------------------------------------------
        elif action == "one_day_filter":
            device.click_one_day()
            device.verify_complete_device_stats_page()
            assert device.verify_api_response(api_responses)
            actual_result = "1 Day statistics displayed correctly."

        # --------------------------------------------
        # TC_019
        # --------------------------------------------
        elif action == "seven_days_filter":
            device.click_seven_days()
            device.verify_complete_device_stats_page()
            assert device.verify_api_response(api_responses)
            actual_result = "7 Days statistics displayed correctly."

        # --------------------------------------------
        # TC_020
        # --------------------------------------------
        elif action == "thirty_days_filter":
            device.click_thirty_days()
            device.verify_complete_device_stats_page()
            assert device.verify_api_response(api_responses)
            actual_result = "30 Days statistics displayed correctly."

        # --------------------------------------------
        # TC_021
        # --------------------------------------------
        elif action == "refresh":
            before = page.locator("text=Updated").inner_text()
            device.click_refresh()
            page.wait_for_load_state("networkidle")
            after = page.locator("text=Updated").inner_text()
            assert after != ""
            device.verify_complete_device_stats_page()
            assert device.verify_api_response(api_responses)
            actual_result = "Refresh executed successfully."

        status = "PASS"

    except Exception as e:
        logger.error(f"{tc_id} Failed : {e}")
        actual_result = str(e)
        screenshot = Screenshot.capture(page, tc_id)
        status = "FAIL"

    execution_time = round(time.time() - start, 2)

    # --------------------------------------------
    # Excel Update Logic
    # --------------------------------------------
    test_cases = excel.get_test_cases()
    for test_case in test_cases:
        if test_case["tc_id"] == tc_id:
            row = test_case["row"]
            excel.update_actual_result(row, actual_result)
            excel.update_status(row, status)
            excel.update_execution_time(row, execution_time)
            excel.update_screenshot(row, screenshot)
            break

    logger.info(f"{tc_id} result: {status}")

    # Remove network listener so it doesn't pile up across different test cases
    page.remove_listener("response", capture_response)

    # Explicitly fail this isolated test step if an exception was caught
    if status == "FAIL":
        pytest.fail(f"Test case {tc_id} failed: {actual_result}")
