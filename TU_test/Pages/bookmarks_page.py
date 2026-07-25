from playwright.sync_api import expect


class BookmarksPage:

    def __init__(self, page):
        self.page = page

        # Navigation
        self.bookmarks_menu = page.get_by_role("link", name="Bookmarks")

        # Page Header
        self.bookmarks_header = page.get_by_role("heading", name="Bookmarks")

        # Search
        self.search_box = page.locator("input[placeholder*='Search']")

        # Refresh
        self.refresh_button = page.locator("button").filter(has_text="Refresh")

        # Camera Filter
        self.camera_dropdown = page.locator("select").first

    #########################################

    def open_bookmarks(self):
        self.bookmarks_menu.click()

    #########################################

    def verify_bookmarks_loaded(self):
        expect(self.bookmarks_header).to_be_visible(timeout=10000)

    #########################################

    def search_bookmark(self, text):
        self.search_box.fill(text)

    #########################################

    def verify_search_results(self):
        expect(self.search_box).to_have_value("Sample Text")

    #########################################

    def click_refresh(self):
        if self.refresh_button.count() > 0:
            self.refresh_button.click()

    #########################################

    def select_camera_filter(self):
        if self.camera_dropdown.count() > 0:
            options = self.camera_dropdown.locator("option")
            if options.count() > 1:
                value = options.nth(1).get_attribute("value")
                self.camera_dropdown.select_option(value=value)

    #########################################

    def verify_camera_filter(self):
        expect(self.camera_dropdown).to_be_visible()