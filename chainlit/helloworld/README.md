# 🌦️ Chainlit Weather Chatbot

A fun and interactive weather chatbot built with **Chainlit**, **Python**, and **WeatherAPI**.  
Ask it questions like “What’s the weather in Lahore?” or simply type a city like “Karachi” — and it will respond with real-time weather info.

---

## 🚀 Features

- 🌍 Global city support  
- 🧠 Smart city detection using natural language  
- ☁️ Real-time weather using WeatherAPI  
- 🔐 Secure API key management with `.env`  
- 🤖 Chainlit UI for interactive chat experience  

---

## 🧰 Tech Stack

- `Python`  
- `Chainlit`  
- `httpx`  
- `python-dotenv`  
- `WeatherAPI`  

---

## 🔧 Installation Steps

### 1. Clone the Project

```bash
git clone 
cd weather-chatbot
2. Install Dependencies
If you are using uv (recommended):

uv venv
uv pip install chainlit httpx python-dotenv
Or with pip:

python -m venv venv
venv\Scripts\activate    # On Windows
pip install chainlit httpx python-dotenv
🔑 Add Your API Key
Get a free API key from https://www.weatherapi.com

Create a .env file in the root folder:

OPENWEATHER_API_KEY=your_api_key_here
▶️ Run the App

chainlit run chatbot.py -w