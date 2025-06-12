import os
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion
import random

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")

# Unique greeting with signature
greeting = (
        "✨ Welcome! I’m SmartBuddy 🤖, created by *Areeba Hammad* 💖 — "
        "your friendly guide to mastering your studies 📚🚀."
    )

@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])
    await cl.Message(content=greeting).send()

@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})
    cl.user_session.set("chat_history", history)

    thinking_phrases = [
        "Hmm, let me think 🤔",
        "Interesting question...",
        "Just a moment while I get that for you ⏳",
        "Analyzing your input 🔍",
        "Let's figure this out together 💡"
    ]

    thinking_msg = random.choice(thinking_phrases)
    thinking = cl.Message(content=f"{thinking_msg}")
    await thinking.send()

    for _ in range(3):
        thinking.content += "."
        await thinking.update()
        await cl.sleep(0.4)

    response = completion(
        model="gemini/gemini-2.0-flash",
        api_key=GEMINI_API_KEY,
        messages=history
    ).choices[0].message.content

    msg = cl.Message(content="")
    await msg.send()

    for char in response:
        msg.content += char
        await msg.update()
        await cl.sleep(0.015)

    history.append({"role": "assistant", "content": response})
    cl.user_session.set("chat_history", history)

