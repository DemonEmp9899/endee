# llm.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_resolution(user_query: str, matches: list):

    context = ""
    for res in matches:
        context += f"\nPast Resolution:\n{res}\n"

    prompt = f"""
You are an intelligent customer support assistant.

User Issue:
{user_query}

Similar past tickets:
{context}

Generate a professional and helpful resolution.
Keep it concise.
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",   # 🔥 OpenRouter model
        messages=[
            {"role": "system", "content": "You are a professional support AI."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content