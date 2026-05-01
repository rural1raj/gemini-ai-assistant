import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME, MAX_HISTORY

# 🔑 Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# 🤖 Load Model
model = genai.GenerativeModel(MODEL_NAME)


# ==============================
# 🧠 Format history for Gemini
# ==============================
def format_history(history):
    """
    Convert stored history into Gemini-compatible format
    """
    formatted = []

    for msg in history[-MAX_HISTORY:]:
        formatted.append({
            "role": msg["role"],
            "parts": msg["parts"]
        })

    return formatted


# ==============================
# 🤖 Get AI Response
# ==============================
def get_response(prompt, history):
    """
    Generate response from Gemini using conversation history
    """

    try:
        # Format history
        formatted_history = format_history(history)

        # Start chat session
        chat = model.start_chat(history=formatted_history)

        # Send message
        response = chat.send_message(prompt)

        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"

