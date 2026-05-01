import requests
from config import WEATHER_API_KEY


# ==============================
# 🧠 Extract City Safely
# ==============================
def extract_city(query: str) -> str:
    query = query.lower()

    keywords = ["weather", "in", "today", "now", "temperature", "show", "tell"]

    words = query.split()
    city_words = [w for w in words if w not in keywords]

    city = " ".join(city_words).strip()

    return city


# ==============================
# 🌤️ WEATHER API
# ==============================
def get_weather(city: str) -> str:

    if not WEATHER_API_KEY:
        return "⚠️ WEATHER_API_KEY missing in .env"

    if not city:
        return "⚠️ City not found. Example: weather mumbai"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return f"⚠️ City '{city}' not found in weather API"

        data = response.json()

        city_name = data.get("name", "Unknown")
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]

        temp = main.get("temp", "N/A")
        feels_like = main.get("feels_like", "N/A")
        humidity = main.get("humidity", "N/A")
        description = weather.get("description", "N/A")

        return (
            f"🌍 City: {city_name}\n"
            f"🌡️ Temperature: {temp}°C\n"
            f"🤒 Feels Like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌥️ Condition: {description}"
        )

    except requests.exceptions.Timeout:
        return "⏳ Weather API timeout"

    except Exception as e:
        return f"⚠️ Weather Error: {str(e)}"