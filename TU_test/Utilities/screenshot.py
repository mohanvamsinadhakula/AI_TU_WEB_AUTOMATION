# Utilities/screenshot.py

import os
from datetime import datetime
from Utilities.config import Config


class Screenshot:

    @staticmethod
    def capture(page, test_case_id):

        # Create Screenshots folder if it doesn't exist
        os.makedirs(Config.SCREENSHOT_FOLDER, exist_ok=True)

        # Timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Screenshot filename
        file_name = f"{test_case_id}_{timestamp}.png"

        # Full path
        file_path = os.path.join(
            Config.SCREENSHOT_FOLDER,
            file_name
        )

        # Capture screenshot
        page.screenshot(path=file_path, full_page=True)

        return file_path