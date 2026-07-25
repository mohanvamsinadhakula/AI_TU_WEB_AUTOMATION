# Utilities/logger.py

import logging
import os
from datetime import datetime

# Create Logs folder if it doesn't exist
LOG_FOLDER = "Reports/Logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

# Log file name
log_file = os.path.join(
    LOG_FOLDER,
    f"Automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

# Configure logger
logging.basicConfig(
    filename=log_file,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

logger = logging.getLogger("ThirdUmpireAutomation")