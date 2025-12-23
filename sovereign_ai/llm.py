import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def llm(prompt: str) -> str:
    res = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return res.choices[0].message.content.strip()
