# import pytest
# from playwright.sync_api import sync_playwright

# from Pages.login_page import LoginPage  #in login_page.py LoginPage class
# from Utilities.config import Config


# @pytest.fixture(scope="session")  #built in feature in the pytest library
# def browser():

#     playwright = sync_playwright().start()

#     browser = playwright.chromium.launch(
#         headless=False,
#         slow_mo=300
#     )

#     yield browser  #yield is used instead of return, before yeild runs before the test and after the yeild runs the after the test completes 

#     browser.close()
#     playwright.stop()


# @pytest.fixture(scope="session") 
# def context(browser):

#     context = browser.new_context()

#     yield context

#     context.close()


# @pytest.fixture(scope="session")
# def page(context):

#     page = context.new_page()

#     yield page

#     page.close()

#     # Logout can be added here later if needed
import pytest
from playwright.sync_api import sync_playwright
from Pages.login_page import LoginPage
from Utilities.config import Config

@pytest.fixture(scope="session")
def browser():
    """
    Launches a single browser process shared across the entire test session.
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=300
    )
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")  # FIXED: Changed from session to function
def context(browser):
    """
    Creates a fresh browser context jar for each individual test to isolate cookies.
    """
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True
    )
    yield context
    context.close()


@pytest.fixture(scope="function")  # FIXED: Changed from session to function
def page(context):
    """
    Yields an isolated browser tab page for each individual test run.
    """
    page = context.new_page()
    yield page
    page.close()
