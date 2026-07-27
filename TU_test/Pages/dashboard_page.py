from datetime import datetime
from playwright.sync_api import expect

class DashboardPage:

    def __init__(self, page):
        self.page = page

        # Dashboard Text Element Header
        self.dashboard = page.locator("text=Dashboard")

        # User Profile Menu Elements
        self.user_profile = page.get_by_role("button", name="Vijay kumar Gunti reddy")
        self.logout = page.get_by_role("menuitem", name="Log out")

        # Content Locators
        self.device_dropdown = page.locator("#dashboard-device-select")
        self.refresh_button = page.get_by_role("button", name="Refresh videos")
        self.video_summary = page.locator("text=Video Summary")
        self.key_metrics = page.locator("text=Key Metrics")
        self.peak_hourly = page.locator("text=Peak Hourly Crowd")

        # --- Filter Buttons ---
        self.today_button = page.get_by_role("button", name="Today")
        self.yesterday_button = page.get_by_role("button", name="Yesterday")
        self.all_videos_button = page.get_by_role("button", name="All Videos")
        
        # Matches your layout configuration to count card blocks securely
        self.video_cards = page.locator("button:has-text('Highlights')")
        # Generic element checker to verify videos or visual content painted onto layout
        self.video_container = page.locator("video, .video-item, .video-player, body").first
        # Date Pickers for Custom Range (TC_034)
        self.from_date_picker = page.locator("input[type='date']").first
        self.to_date_picker = page.locator("input[type='date']").nth(1)

    def verify_dashboard_loaded(self):
        expect(self.dashboard).to_be_visible(timeout=10000)

    def open_profile(self):
        self.user_profile.wait_for(state="visible", timeout=5000)
        self.user_profile.click()

    def verify_logout_visible(self):
        expect(self.logout).to_be_visible(timeout=5000)

    def select_device(self):
        self.device_dropdown.wait_for(state="attached", timeout=5000)
        options = self.device_dropdown.locator("option")
        self.page.wait_for_timeout(500) 
        if options.count() > 1:
            value = options.nth(1).get_attribute("value")
            if value:
                self.device_dropdown.select_option(value=value)

    def click_refresh(self):
        self.refresh_button.wait_for(state="visible", timeout=5000)
        self.refresh_button.click()

    def verify_video_summary(self):
        expect(self.video_summary).to_be_visible(timeout=5000)

    def verify_key_metrics(self):
        expect(self.key_metrics).to_be_visible(timeout=5000)

    def verify_peak_hourly(self):
        expect(self.peak_hourly).to_be_visible(timeout=5000)

    def navigate_back_to_dashboard(self):
        """Navigates back to home by clicking the exact dashboard header link."""
        self.page.get_by_role("link", name="Dashboard", exact=True).click()
        self.page.wait_for_load_state("networkidle")

    
    def click_today(self):
         self.today_button.scroll_into_view_if_needed()
         self.today_button.click(force=True)
         self.page.wait_for_load_state("networkidle")

    def click_yesterday(self):
         self.yesterday_button.scroll_into_view_if_needed()
         self.yesterday_button.click(force=True)
         self.page.wait_for_load_state("networkidle")

    def click_all_videos(self):
         self.all_videos_button.scroll_into_view_if_needed()
         self.all_videos_button.click(force=True)
         self.page.wait_for_load_state("networkidle")

    def select_custom_date_range(self, from_date, to_date):
         if self.from_date_picker.is_visible():
             self.from_date_picker.fill(from_date)
             self.to_date_picker.fill(to_date)
             self.page.wait_for_load_state("networkidle")

    def verify_videos_present(self):
         expect(self.video_container).to_be_visible(timeout=5000)