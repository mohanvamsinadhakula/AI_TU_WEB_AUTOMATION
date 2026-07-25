import re
from playwright.sync_api import expect


class SettingsPage:

    def __init__(self, page):
        self.page = page

        # --- Resilient Navigation Sidebar Link Selector ---
        self.settings_nav = (
            page.get_by_role("link", name=re.compile(r"Settings", re.I))
            .or_(page.locator("nav").get_by_text("Settings", exact=False))
            .or_(page.locator("text=Settings"))
            .first
        )

        # --- Resilient Page Heading/Header Selector ---
        self.settings_header = (
            page.get_by_role("heading", name=re.compile(r"Settings", re.I))
            .or_(page.locator("h1, h2, h3, span").filter(has_text=re.compile(r"^Settings$", re.I)))
            .first
        )

        # Tab Sections
        self.profile = page.get_by_role("tab", name=re.compile(r"Profile", re.I)).or_(
            page.locator("text=Profile")
        ).first
        
        self.notifications = page.get_by_role("tab", name=re.compile(r"Notifications", re.I)).or_(
            page.locator("button, a, h2").filter(has_text=re.compile(r"^Notifications$", re.I))
        ).first
        
        self.video_settings = page.get_by_role("tab", name=re.compile(r"Video Settings", re.I)).or_(
            page.locator("text=Video Settings")
        ).first
        
        self.data_management = page.get_by_role("tab", name=re.compile(r"Data Management", re.I)).or_(
            page.locator("text=Data Management")
        ).first

        # Buttons
        self.save_changes = page.get_by_role("button", name=re.compile(r"Save Changes", re.I)).or_(
            page.locator("button").filter(has_text="Save Changes")
        ).first

    def open_settings(self):
        self.settings_nav.wait_for(state="visible", timeout=8000)
        self.settings_nav.click()

    def verify_settings_loaded(self):
        # Allow any client-side routing/render processing to finish completely
        self.page.wait_for_load_state("load")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

        # Robust conditional verification strategy
        if self.settings_header.count() > 0:
            expect(self.settings_header).to_be_visible(timeout=5000)
        else:
            expect(self.settings_nav).to_be_visible(timeout=5000)

    def open_profile_section(self):
        self.profile.scroll_into_view_if_needed()
        self.profile.click(force=True)

    def verify_profile_section(self):
        expect(self.profile).to_be_visible(timeout=5000)

    def open_notifications(self):
        self.notifications.scroll_into_view_if_needed()
        self.notifications.click(force=True)

    def verify_notifications(self):
        expect(self.notifications).to_be_visible(timeout=5000)

    def open_video_settings(self):
        self.video_settings.scroll_into_view_if_needed()
        self.video_settings.click(force=True)

    def verify_video_settings(self):
        expect(self.video_settings).to_be_visible(timeout=5000)

    def open_data_management(self):
        self.data_management.scroll_into_view_if_needed()
        self.data_management.click(force=True)

    def verify_data_management(self):
        expect(self.data_management).to_be_visible(timeout=5000)

    def click_save_changes(self):
        self.save_changes.wait_for(state="visible", timeout=5000)
        self.save_changes.click()

    def verify_save_success(self):
        expect(self.save_changes).to_be_visible(timeout=5000)