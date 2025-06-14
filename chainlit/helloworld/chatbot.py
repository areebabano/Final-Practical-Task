# import chainlit as cl

# @cl.on_message
# async def main(message: cl.Message):
#     await cl.Message(content=f"Received: {message.content}").send()

import chainlit as cl
import httpx
import re
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def extract_city(text: str):
    # Try to extract after "in [city]"
    match = re.search(r"in\s+([a-zA-Z\s]+)", text.lower())
    if match:
        return match.group(1).strip().title()

    # If no "in", assume entire message is a city name
    if len(text.strip().split()) <= 3:  # "Lahore", "Karachi weather", etc.
        return re.sub(r'weather', '', text, flags=re.IGNORECASE).strip().title()

    return None

async def get_weather(city: str):
    if not API_KEY:
        return "API key missing. Please check your .env file."

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
    except httpx.RequestError as e:
        return f"Network error: {e}"

    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"The weather in {city} is {temp}°C with {condition}."
    elif response.status_code == 401:
        return "Invalid API key."
    else:
        return f"Sorry, weather info for '{city}' not found. (Error {response.status_code})"

@cl.on_message
async def main(message: cl.Message):
    text = message.content.strip()
    city = extract_city(text)

    if city:
        reply = await get_weather(city)
    else:
        reply = "Please specify a city like: 'What's the weather in Lahore?'"

    await cl.Message(content=reply).send()
