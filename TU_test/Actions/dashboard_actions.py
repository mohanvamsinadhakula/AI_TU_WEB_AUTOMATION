from Pages.dashboard_page import DashboardPage


class DashboardActions:

    def __init__(self, page):

        self.dashboard = DashboardPage(page)

    # ==================================================
    # TC_006
    # Verify Dashboard loads
    # ==================================================
    def tc_006(self):

        assert self.dashboard.is_dashboard_loaded()

        return "Dashboard loaded successfully"

    # ==================================================
    # TC_007
    # Verify Device Dropdown
    # ==================================================
    def tc_007(self):

        assert self.dashboard.is_device_dropdown_visible()

        return "Device dropdown displayed"

    # ==================================================
    # TC_008
    # Verify Device Selection
    # ==================================================
    def tc_008(self):

        self.dashboard.select_device("All Devices")

        return "Device selected successfully"

    # ==================================================
    # TC_009
    # Verify Refresh Videos
    # ==================================================
    def tc_009(self):

        self.dashboard.click_refresh_videos()

        return "Videos refreshed successfully"

    # ==================================================
    # TC_010
    # Verify Video Summary
    # ==================================================
    def tc_010(self):

        assert self.dashboard.is_video_summary_visible()

        return "Video Summary displayed"

    # ==================================================
    # TC_011
    # Verify Key Metrics
    # ==================================================
    def tc_011(self):

        assert self.dashboard.is_key_metrics_visible()

        return "Key Metrics displayed"

    # ==================================================
    # TC_012
    # Verify Peak Hourly Crowd
    # ==================================================
    def tc_012(self):

        assert self.dashboard.is_peak_hourly_crowd_visible()

        return "Peak Hourly Crowd displayed"

    # ==================================================
    # Dispatcher
    # ==================================================
    def execute(self, tc_id):

        actions = {

            "TC_006": self.tc_006,
            "TC_007": self.tc_007,
            "TC_008": self.tc_008,
            "TC_009": self.tc_009,
            "TC_010": self.tc_010,
            "TC_011": self.tc_011,
            "TC_012": self.tc_012,

        }

        if tc_id not in actions:
            raise Exception(f"{tc_id} is not implemented.")

        return actions[tc_id]()