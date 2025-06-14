import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

# 1. Load environment variables from .env file (API keys etc.)
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 2. Check if API key exists, warna error dikhayega
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")

# 3. Gemini API ke liye async client banate hain
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 4. Model define karte hain (Gemini ka model)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# 5. Runner config set karte hain (logging/tracing disable kiya hai)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# 6. Agent ko question bhejne wali async function
async def ask_agent(question: str):
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=model,
    )
    result = await Runner.run(agent, question, run_config=config)
    return result.final_output

# 7. Main async function jo user se questions lega aur answer dega
async def main():
    print("Welcome to the Gemini-powered Assistant! (Type 'exit' to quit)")
    while True:
        user_input = input("Ask your question: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("Thinking...")
        answer = await ask_agent(user_input)
        print(f"Answer: {answer}\n")

# 8. Script ko chalane ke liye asyncio event loop start karte hain
if __name__ == "__main__":
    asyncio.run(main())
