from modules.gemini_chat import get_response
from modules.memory import load_memory, save_memory, add_message
from modules.search_tool import is_real_time_query, get_search_context
from modules.weather_api import get_weather, extract_city


# ==============================
# 🚀 CHAT ENGINE
# ==============================
def run_chat():

    print("🤖 Gemini AI Assistant (type 'exit' to quit)")
    print("-" * 50)

    history = load_memory()

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("👋 Bye!")
            break

        response = None
        text = user_input.lower()

        try:

            # =========================
            # 🌤️ WEATHER (SAFE)
            # =========================
            if "weather" in text:

                city = extract_city(user_input)

                if not city:
                    response = "⚠️ Please write like: weather mumbai"
                else:
                    response = get_weather(city)

            # =========================
            # 🔍 SEARCH
            # =========================
            elif is_real_time_query(user_input):

                search_context = get_search_context(user_input)

                if search_context:
                    response = get_response(search_context, history)
                else:
                    response = "⚠️ Search API not working or quota exceeded."

            # =========================
            # 🤖 NORMAL CHAT
            # =========================
            else:
                response = get_response(user_input, history)

            # =========================
            # 🧠 MEMORY SAFE UPDATE
            # =========================
            if response is None:
                response = "⚠️ No response generated."

            history = add_message(history, "user", user_input)
            history = add_message(history, "model", response)

            save_memory(history)

            print(f"\nAI: {response}")

        except Exception as e:
            print("❌ Error:", str(e))


# ==============================
# 🚀 RUN
# ==============================
if __name__ == "__main__":
    run_chat()