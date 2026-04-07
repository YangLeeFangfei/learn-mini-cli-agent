import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

client = Anthropic(base_url=os.getenv("ANTHROPIC_BASE_URL"))
MODEL = os.environ["MODEL_ID"]

SYSTEM = "You are a concise CLI assistant. Answer briefly."

def text_from_content(content):
    parts = []
    for block in content:
        if getattr(block,"type",None) == "text":
            parts.append(block.text)
    return "\n".join(parts).strip()

def run_once(messages):
    response = client.messages.create(
        model=MODEL,
        system=SYSTEM,
        messages=messages,
        max_tokens=1000
    )
    messages.append({"role": "assistant", "content": response.content})
    return text_from_content(response.content)
