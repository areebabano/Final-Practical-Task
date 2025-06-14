# Gemini-Powered Async Assistant

This project is an asynchronous AI assistant built using the LiteLLM Agent SDK and Google’s Gemini API.  
It allows you to chat with a helpful AI agent right from your terminal — powered by async Python and modern AI models!

---

## Features

- **Async interaction:** Ask multiple questions one after another without blocking.
- **Gemini API integration:** Uses Google Gemini’s OpenAI-compatible model for responses.
- **Easy environment config:** Manage your API keys securely using a `.env` file.
- **Clean terminal UI:** Type your questions, get answers instantly, exit anytime.

---

## Getting Started

### 1. Clone this repo

```bash
git clone <your-repo-url>
cd hello_agent
2. Initialize your project with uv (if not done yet)

uv init --package hello_agent
uv venv
.venv\Scripts\activate    # Windows
# or
source .venv/bin/activate # macOS/Linux
3. Install dependencies

uv add openai-agents[litellm] python-dotenv
4. Add your Gemini API key
Create a .env file in the root folder:

GEMINI_API_KEY=your_gemini_api_key_here
How to Use
Run the assistant script:

uv run main.py
You’ll see a prompt like:

Welcome to the Gemini-powered Assistant! (Type 'exit' to quit)
Ask your question:
Type any question and hit Enter. The assistant will respond asynchronously.

To exit, just type:

exit