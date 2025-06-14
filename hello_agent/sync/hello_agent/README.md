# GeminiSync Chat — Synchronous Gemini AI Chat Client

A simple, interactive synchronous chat client for Google Gemini LLM with a rich terminal UI using Python’s [Rich](https://github.com/Textualize/rich) library. Chat live, get colorful responses, and enjoy a smooth experience without async complexity.

---

## Features
- Synchronous Gemini API chat
- Colorful, styled terminal interface
- Typing animation for responses
- Easy setup with `.env` for API keys
- Cross-platform support (Windows/macOS/Linux)

---

## Setup & Run

1. Clone repo & enter folder  
```bash
git clone https://github.com/yourusername/geminisync-chat.git
cd geminisync-chat
Create & activate virtual environment (using uv):

uv init --package geminisync-chat
uv venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
Install dependencies:

uv pip install rich litellm python-dotenv
Add .env with your Gemini API key:

GEMINI_API_KEY=your_api_key_here
Run the chat client:

uv run main.py