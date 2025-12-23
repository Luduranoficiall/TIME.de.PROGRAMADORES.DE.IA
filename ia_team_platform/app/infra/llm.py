import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content
