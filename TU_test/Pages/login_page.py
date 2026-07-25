from playwright.sync_api import Page
from Utilities.config import Config
import re

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.email = page.locator("input[type='email']")
        self.password = page.locator("input[type='password']")
        self.sign_in = page.locator("button[type='submit']")
        self.profile_button = page.get_by_role("button", name="Vijay kumar Gunti reddy")
        self.logout_button = page.get_by_role("menuitem", name="Log out")

        # Messages (Lenient text locators to handle layout variations)
        self.error_message = page.locator("text=Invalid").or_(page.locator(".error-message, .alert-danger"))
        self.dashboard = page.locator("text=Dashboard")

    # -----------------------------
    # Page Actions
    # -----------------------------

    def open(self):
        # Safely determine the URL to prevent double /login nesting
        if "/login" in Config.BASE_URL:
            target_url = Config.BASE_URL
        else:
            target_url = f"{Config.BASE_URL.rstrip('/')}/login"
            
        self.page.goto(target_url)
        self.email.wait_for(state="visible", timeout=7000)

    def enter_email(self, email):
        self.email.click()
        self.email.clear()
        self.email.fill(email)

    def enter_password(self, password):
        self.password.click()
        self.password.clear()
        self.password.fill(password)

    def click_signin(self):
        self.sign_in.wait_for(state="visible", timeout=5000)
        self.sign_in.click()

    def open_profile(self):
        self.profile_button.wait_for(state="visible", timeout=5000)
        self.profile_button.click()

    def login(self, email, password):
        # 1. Fill fields only if values are provided (handles TC_004 empty checks gracefully)
        if email:
            self.enter_email(email)
        else:
            self.email.clear()

        if password:
            self.enter_password(password)
        else:
            self.password.clear()
        
        # 2. Trigger the submission click
        self.click_signin()
        
        # 3. FIXED: Dynamically wait for EITHER success redirect OR failure feedback UI elements
        self.page.wait_for_function(
            """
            () => {
                return window.location.pathname.includes('dashboard') 
                    || window.location.pathname == '/' 
                    || document.body.innerText.includes('Invalid')
                    || document.body.innerText.includes('required')
                    || document.querySelector('.error-message') !== null;
            }
            """,
            timeout=10000
        )
        self.page.wait_for_timeout(1000) # Give animations a moment to settle down

    def logout(self):
        self.open_profile()
        self.logout_button.wait_for(state="visible", timeout=5000)
        self.logout_button.click()

    # -----------------------------
    # Verification Methods
    # -----------------------------

    def is_login_successful(self):
        return "/dashboard" in self.page.url or self.page.url.endswith("/")
    
    def is_logout_successful(self, email, password):
        self.login(email, password)
        self.logout()
        return "/login" in self.page.url or self.page.url == Config.BASE_URL

    def get_error_message(self):
        # Check if element is attached and has visible text properties
        if self.error_message.count() > 0 and self.error_message.first.is_visible():
            return self.error_message.first.text_content().strip()
        
        # Fallback raw UI innerText scanner if explicit classes don't trap it
        body_text = self.page.locator("body").inner_text()
        if "Invalid" in body_text:
            return "Invalid credentials"
        return ""

    def get_current_url(self):
        return self.page.url
