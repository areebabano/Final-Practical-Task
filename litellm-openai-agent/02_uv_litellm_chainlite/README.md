# 🤖 SmartBuddy — Your Intelligent AI Assistant

Welcome to **SmartBuddy**, an interactive AI assistant built with **Chainlit**, powered by **LiteLLM** (Gemini model), and enhanced with the ultra-fast **UV** backend! 🚀✨

SmartBuddy is designed to make your study sessions, coding help, and everyday questions smarter, faster, and friendlier.

---

## 🌟 Features

- **Conversational AI** powered by Google’s Gemini model via LiteLLM  
- Built on **Chainlit** for seamless chat UI and session management  
- Real-time responses with typing animation and interactive prompts  
- Secure API key management using `.env` files  
- Personalized assistant name and branding — *created by Areeba Hammad* 💖  
- Maintains chat history for context-aware answers  
- Easy to extend and customize for your own AI assistant projects  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher  
- [Chainlit](https://docs.chainlit.io) installed  
- [LiteLLM](https://github.com/BerriAI/litellm) library installed  
- Your Gemini API key (set in `.env` file as `GEMINI_API_KEY`)

Run This
chainlit run src/smartbuddy_chatbot/main.py