from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "openai/gpt-oss-120b"
MAX_HISTORY_MESSAGES = 20  # mémoire : on garde les 20 derniers messages


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


SYSTEM_PROMPT = read_file(file_path="./context.txt")
client = Groq(api_key=os.environ["GROQ_KEY"])


def ask_llm(history):
    """history = liste des messages [{"role": ..., "content": ...}]"""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history[-MAX_HISTORY_MESSAGES:]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=MODEL_NAME,
        include_reasoning=False,
    )
    return chat_completion.choices[0].message.content