# import os
# from dotenv import load_dotenv
# from litellm import OpenAI  # sync client

# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set.")

# client = OpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# def main():
#     print("Type 'exit' to quit.")
#     while True:
#         prompt = input("You: ")
#         if prompt.strip().lower() == "exit":
#             print("Goodbye!")
#             break
        
#         response = client.chat.completions.create(
#             model="gemini-2.0-flash",
#             messages=[{"role": "user", "content": prompt}]
#         )
        
#         # Extract the assistant reply text
#         assistant_message = response.choices[0].message.content
#         print("Assistant:", assistant_message)

# if __name__ == "__main__":
#     main()
import os
import time
from dotenv import load_dotenv
from litellm import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

load_dotenv()
console = Console()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def type_out(text, delay=0.03):
    """Simulate typing effect in console."""
    for char in text:
        console.print(char, end="", style="bold cyan")
        time.sleep(delay)
    console.print()  # newline

def main():
    console.print("[bold green]🤖 Welcome to [underline cyan]GeminiSync Chat[/underline cyan]![/bold green]")
    console.print("[bold yellow]❌ Type [bold bright_red]'exit'[/bold bright_red] to quit anytime. See you soon! 👋[/bold yellow]\n")

    while True:
        prompt = Prompt.ask("[bold yellow]You[/bold yellow]").strip()
        if prompt.lower() == "exit":
            console.print("\n[bold magenta]👋 Goodbye! Thanks for chatting.[/bold magenta]")
            break

        try:
            response = client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[{"role": "user", "content": prompt}]
            )
            assistant_message = response.choices[0].message.content
            
            console.print("[bold green]Assistant:[/bold green] ", end="")
            type_out(assistant_message)
            console.print()  # add spacing

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
