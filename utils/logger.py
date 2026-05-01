import logging
import os
from datetime import datetime

# ==============================
# 📁 Create logs directory
# ==============================
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# ==============================
# 📄 Log file (date-wise)
# ==============================
log_file = os.path.join(
    LOG_DIR,
    f"app_{datetime.now().strftime('%Y-%m-%d')}.log"
)

# ==============================
# ⚙️ Logger Setup
# ==============================
logger = logging.getLogger("GeminiApp")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers (important for Streamlit)
if not logger.handlers:

    # 📁 File handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # 🖥️ Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 🧾 Format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# ==============================
# 🧠 Safe Logging Functions
# ==============================

def log_info(message):
    logger.info(str(message))


def log_warning(message):
    logger.warning(str(message))


def log_error(message):
    logger.error(str(message))


def log_user_input(user_input):
    if user_input:
        logger.info(f"USER: {str(user_input)}")


def log_ai_response(response):
    if response:
        logger.info(f"AI: {str(response)}")