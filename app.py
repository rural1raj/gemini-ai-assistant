import streamlit as st

from modules.gemini_chat import get_response
from modules.memory import load_memory, save_memory, add_message
from modules.search_tool import is_real_time_query, get_search_context
from modules.weather_api import get_weather, extract_city
from utils.formatter import format_response, enhance_prompt
from utils.logger import log_user_input, log_ai_response, log_error


# ==============================
# 🎨 PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Gemini AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Gemini AI Assistant")
st.write("Smart AI + Weather + Search + Memory")


# ==============================
# 🧠 SESSION MEMORY
# ==============================
if "history" not in st.session_state:
    st.session_state.history = load_memory()


# ==============================
# 💬 INPUT
# ==============================
user_input = st.text_input("Ask anything (e.g. weather mumbai)")

send_btn = st.button("🚀 Send")


# ==============================
# 🤖 MAIN LOGIC
# ==============================
if send_btn and user_input:

    log_user_input(user_input)

    try:
        response = None
        text = user_input.lower()

        # =========================
        # 🌤️ WEATHER (TOP PRIORITY)
        # =========================
        if "weather" in text:
            city = extract_city(user_input)

            print("DEBUG CITY:", city)  # 🔥 debug line

            if city:
                response = get_weather(city)
            else:
                response = "⚠️ Please type like: weather mumbai"

        # =========================
        # 🔍 SEARCH
        # =========================
        elif is_real_time_query(user_input):
            search_context = get_search_context(user_input)

            if search_context:
                response = get_response(search_context, st.session_state.history)
            else:
                response = "⚠️ Real-time data unavailable"

        # =========================
        # 🤖 NORMAL CHAT
        # =========================
        else:
            prompt = enhance_prompt(user_input)
            response = get_response(prompt, st.session_state.history)

        # =========================
        # ✨ FORMAT SAFE
        # =========================
        if response:
            response = format_response(response)

        # =========================
        # 🧠 MEMORY UPDATE
        # =========================
        st.session_state.history = add_message(st.session_state.history, "user", user_input)
        st.session_state.history = add_message(st.session_state.history, "model", response)

        save_memory(st.session_state.history)

        log_ai_response(response)

        # =========================
        # 🖥️ OUTPUT
        # =========================
        st.success(response)

    except Exception as e:
        log_error(str(e))
        st.error("❌ Something went wrong!")


# ==============================
# 📜 HISTORY
# ==============================
with st.expander("📜 Chat History"):
    for msg in st.session_state.history:

        role = msg.get("role", "")
        parts = msg.get("parts", [])

        text = ""
        if isinstance(parts, list) and len(parts) > 0:
            if isinstance(parts[0], dict):
                text = parts[0].get("text", "")
            else:
                text = str(parts[0])

        if role == "user":
            st.markdown(f"🧑 **You:** {text}")
        else:
            st.markdown(f"🤖 **AI:** {text}")