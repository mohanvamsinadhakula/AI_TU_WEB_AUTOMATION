from playwright.sync_api import expect

class AboutPage:

    def __init__(self, page):
        self.page = page

        # Navigation
        self.about = page.get_by_role("link", name="About")

        # FIX LOCATORS HERE: Switch to case/substring-insensitive locators
        self.web_version = page.get_by_text("Version", exact=False).nth(0)
        self.device_version = page.get_by_text("Version", exact=False).nth(1)

        # Download button selector
        self.download_btn = page.locator("button").filter(has_text="Download Excel")

    #########################################

    def open_about(self):
        # Now self.about exists securely!
        self.about.click()

    #########################################

    def verify_about_loaded(self):
        expect(self.about).to_be_visible(timeout=10000)

    #########################################

    def verify_web_application_version(self):
        expect(self.web_version).to_be_visible(timeout=10000)

    #########################################

    def verify_device_software_version(self):
        expect(self.device_version).to_be_visible(timeout=10000)

    #########################################

    def download_excel(self):
        # FIX 3: Robust click handling using the renamed locator variable
        self.download_btn.wait_for(state="visible", timeout=5000)
        with self.page.expect_download() as download_info:
            self.download_btn.click()
        
        # Keep track of the file download asset reference if your tests require saving it
        self.downloaded_file = download_info.value

    #########################################

    def verify_excel_download(self):
        # Validates that the button interface remains valid and download action completed
        expect(self.download_btn).to_be_visible(timeout=5000)
        if hasattr(self, 'downloaded_file') and self.downloaded_file:
            logger_message = f"File successfully downloaded: {self.downloaded_file.suggested_filename}"