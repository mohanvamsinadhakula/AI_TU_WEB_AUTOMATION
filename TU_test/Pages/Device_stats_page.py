# Pages/device_stats_page.py

from playwright.sync_api import Page, expect


class DeviceStatsPage:

    def __init__(self, page: Page):
        self.page = page

        # ----------------------------
        # Navigation
        # ----------------------------
        self.device_stats_menu = page.locator("a[href='/device-stats']")

        # ----------------------------
        # Filters
        # ----------------------------
        self.one_day_btn = page.get_by_role("button", name="1 day")
        self.seven_days_btn = page.get_by_role("button", name="7 days")
        self.thirty_days_btn = page.get_by_role("button", name="30 days")

        self.from_date = page.locator("input[type='date']").nth(0)
        self.to_date = page.locator("input[type='date']").nth(1)

        self.refresh_btn = page.get_by_role("button", name="Refresh")

        # ----------------------------
        # Cards
        # ----------------------------
        self.cpu_card = page.get_by_text("CPU", exact=True).first
        self.ram_card = page.get_by_text("RAM", exact=True).first
        self.temperature_card = page.get_by_text("Temperature", exact=True).first

        self.cpu_status = page.locator("text=Healthy").nth(0)
        self.ram_status = page.locator("text=Healthy").nth(1)
        self.temp_status = page.locator("text=Healthy").nth(2)

        # ----------------------------
        # Charts
        # ----------------------------
        self.cpu_ram_chart = page.locator("canvas").nth(0)
        self.temperature_chart = page.locator("canvas").nth(1)

        # ----------------------------
        # Footer (DEFINED HERE CORRECTLY USING self.page)
        # ----------------------------
        self.device_name = self.page.get_by_text("Pawparazzi", exact=False)
        self.updated_time = self.page.locator("text=/^Updated/") 
        self.cpu_footer = self.page.get_by_text("CPU", exact=True).last
        self.ram_footer = self.page.get_by_text("RAM", exact=True).last
        self.temp_footer = self.page.get_by_text("Temp", exact=True).last
        self.disk_footer = self.page.get_by_text("Disk", exact=True)
        self.uptime_footer = self.page.get_by_text("Up", exact=True)

    # ==========================================================
    # Navigation
    # ==========================================================

    def open_device_stats(self):
        self.device_stats_menu.click()
        self.page.wait_for_load_state("networkidle")

    def is_device_stats_page_loaded(self):
        assert "/device-stats" in self.page.url
        expect(self.page.locator("h1")).to_have_text("Device Stats")
        return True
        
    # ==========================================================
    # Filters
    # ==========================================================

    def click_one_day(self):
        self.one_day_btn.click()
        self.page.wait_for_load_state("networkidle")

    def click_seven_days(self):
        self.seven_days_btn.click()
        self.page.wait_for_load_state("networkidle")

    def click_thirty_days(self):
        self.thirty_days_btn.click()
        self.page.wait_for_load_state("networkidle")

    def click_refresh(self):
        self.refresh_btn.click()
        self.page.wait_for_load_state("networkidle")

    # ==========================================================
    # Cards Validation
    # ==========================================================

    def verify_cpu_card(self):
        expect(self.cpu_card).to_be_visible()
        expect(self.cpu_status).to_be_visible()
        return True

    def verify_ram_card(self):
        expect(self.ram_card).to_be_visible()
        expect(self.ram_status).to_be_visible()
        return True

    def verify_temperature_card(self):
        expect(self.temperature_card).to_be_visible()
        expect(self.temp_status).to_be_visible()
        return True

    # ==========================================================
    # Charts Validation
    # ==========================================================

    def verify_cpu_ram_chart(self):
        expect(self.cpu_ram_chart).to_be_visible()
        return True

    def verify_temperature_chart(self):
        expect(self.temperature_chart).to_be_visible()
        return True

    # ==========================================================
    # Footer Validation (EXECUTES ACTIONS ONLY)
    # ==========================================================

    def verify_footer(self):
        expect(self.device_name).to_be_visible()
        expect(self.updated_time).to_be_visible()
        expect(self.cpu_footer).to_be_visible()
        expect(self.ram_footer).to_be_visible()
        expect(self.temp_footer).to_be_visible()
        expect(self.disk_footer).to_be_visible()
        expect(self.uptime_footer).to_be_visible()
        return True

    # ==========================================================
    # Complete Validation
    # ==========================================================

    def verify_complete_device_stats_page(self):
        self.verify_cpu_card()
        self.verify_ram_card()
        self.verify_temperature_card()
        self.verify_cpu_ram_chart()
        self.verify_temperature_chart()
        self.verify_footer()
        return True

    # ==========================================================
    # API Validation
    # ==========================================================

    def verify_api_response(self, api_responses):
        if len(api_responses) == 0:
            return False
        for api, response in api_responses.items():
            if response["status"] != 200:
                return False
        return True
