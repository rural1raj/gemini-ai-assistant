import os
from dotenv import load_dotenv

# ==============================
# 🔐 LOAD ENV VARIABLES
# ==============================
load_dotenv()

# ==============================
# 🔑 API KEYS
# ==============================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# ==============================
# 📁 PATH CONFIG
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
CHAT_HISTORY_FILE = os.path.join(DATA_FOLDER, "chat_history.json")

# Ensure data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# ==============================
# 🤖 MODEL CONFIG (FIXED)
# ==============================
# ❌ Old (invalid): gemini-2.5-flash
# ✅ Use working model:
MODEL_NAME = "gemini-2.5-flash"
# (optional fallback)
# MODEL_NAME = "gemini-pro"

# ==============================
# ⚙️ APP SETTINGS
# ==============================
MAX_HISTORY = 10   # memory limit

# ⚠️ Google Search API currently broken (403)
# Disable for now to avoid errors
ENABLE_SEARCH = False