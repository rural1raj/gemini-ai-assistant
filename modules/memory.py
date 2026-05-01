import json
import os
from config import CHAT_HISTORY_FILE, MAX_HISTORY

# ==============================
# 📥 Load Memory
# ==============================
def load_memory():
    """
    Load chat history from JSON file
    """
    if not os.path.exists(CHAT_HISTORY_FILE):
        return []

    try:
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


# ==============================
# 💾 Save Memory
# ==============================
def save_memory(history):
    """
    Save chat history to JSON file
    """

    # 🧠 Keep only last MAX_HISTORY*2 messages (user + model)
    trimmed_history = history[-(MAX_HISTORY * 2):]

    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(trimmed_history, f, indent=4, ensure_ascii=False)


# ==============================
# ➕ Add New Message (FIXED)
# ==============================
def add_message(history, role, message):
    """
    Add new message to history in Gemini format
    """

    history.append({
        "role": role,
        "parts": [{"text": message}]   # ✅ FIXED FORMAT
    })

    return history


# ==============================
# 🗑️ Clear Memory
# ==============================
def clear_memory():
    """
    Reset chat history
    """
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)