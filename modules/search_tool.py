import requests
from config import SEARCH_API_KEY, SEARCH_ENGINE_ID, ENABLE_SEARCH


# ==============================
# 🔍 Detect real-time queries
# ==============================
def is_real_time_query(query):
    keywords = [
        "price", "weather", "today", "now",
        "current", "latest", "news", "bitcoin",
        "stock", "temperature"
    ]
    return any(word in query.lower() for word in keywords)


# ==============================
# 🌐 Google Search API (SAFE VERSION)
# ==============================
def google_search(query):

    # 🔒 अगर search disabled है
    if not ENABLE_SEARCH:
        return "⚠️ Real-time search is currently disabled."

    # 🔒 अगर API key missing है
    if not SEARCH_API_KEY or not SEARCH_ENGINE_ID:
        return "⚠️ Search API key or Engine ID missing."

    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": SEARCH_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        # 🔍 Debug logs
        print("STATUS:", response.status_code)

        data = response.json()
        print("DEBUG RESPONSE:", data)

        # ❌ Permission / API error
        if response.status_code == 403:
            return "⚠️ Search API permission denied. Enable Custom Search API."

        # ❌ Other API error
        if response.status_code != 200:
            return f"⚠️ API Error: {data.get('error', {}).get('message', 'Unknown error')}"

        # ❌ No results
        if "items" not in data:
            return "⚠️ No search results found."

        # ✅ Extract top results
        results = []
        for item in data["items"][:3]:
            snippet = item.get("snippet", "")
            results.append(snippet)

        return " ".join(results)

    except requests.exceptions.Timeout:
        return "⚠️ Request timed out."

    except Exception as e:
        return f"⚠️ Search Error: {str(e)}"


# ==============================
# 🧠 Prepare context for Gemini (SMART)
# ==============================
def get_search_context(query):

    search_results = google_search(query)

    # ❌ अगर search fail हो गया
    if search_results.startswith("⚠️"):
        return None   # IMPORTANT: Gemini को मत भेजो

    context = f"""
Use the following real-time information to answer clearly:

{search_results}

Question: {query}
"""
    return context