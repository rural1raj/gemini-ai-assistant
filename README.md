# 🤖 Gemini AI Assistant (Python + Streamlit)

A smart AI-powered chatbot built using **Google Gemini API**, with **real-time Weather**, **Google Search integration**, and a **memory-based conversation system**.  
This project is designed for a **Python Developer Internship portfolio**.

---

## 🚀 Live Features

### 🧠 AI Chat (Gemini)
- Powered by Google Gemini API
- Natural conversation handling
- Context-aware responses

### 💾 Memory System
- Remembers previous chats
- Stores conversation history locally (JSON)
- Improves response continuity

### 🌤️ Weather Integration
- Real-time weather data using OpenWeatherMap API
- City-based weather detection
- Temperature, humidity, condition display

### 🔍 Google Search (Real-Time Data)
- Live search using Google Custom Search API
- Fetches latest information (news, prices, etc.)
- AI uses search context for answers

### 🎨 Streamlit UI
- Clean and interactive web interface
- Gradient UI design
- Chat history viewer
- Sidebar controls

---

## 🏗️ Project Structure


gemini_ai_assistant/
│
├── app.py / main.py
├── config.py
├── .env
│
├── modules/
│ ├── gemini_chat.py
│ ├── memory.py
│ ├── search_tool.py
│ ├── weather_api.py
│
├── utils/
│ ├── formatter.py
│ ├── logger.py
│
├── data/
│ └── chat_history.json
│
├── logs/
├── README.md


---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/gemini-ai-assistant.git
cd gemini-ai-assistant
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Environment Variables

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key
SEARCH_API_KEY=your_google_search_api_key
SEARCH_ENGINE_ID=your_search_engine_id
WEATHER_API_KEY=your_openweather_api_key
4️⃣ Run Project
Streamlit App:
streamlit run app.py
CLI Version:
python main.py
🧪 Example Queries
weather mumbai
weather delhi today
latest news india
bitcoin price
what is AI
🧠 Tech Stack
Python 🐍
Streamlit 🎨
Google Gemini API 🤖
OpenWeatherMap API 🌤️
Google Custom Search API 🔍
JSON (Memory System)
⚠️ Important Notes
Do NOT upload .env file to GitHub
API keys must be kept private
Google search API may require billing/activation
Gemini API has quota limits (free tier)
📊 Project Highlights

✔ AI Chatbot
✔ Real-time Weather
✔ Live Google Search
✔ Memory-based conversations
✔ Professional UI
✔ Internship-ready project

👨‍💻 Developer

Python Developer Internship Project
Built for learning AI integration, APIs, and real-world chatbot systems.
