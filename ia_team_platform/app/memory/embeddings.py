import openai
from app.core.config import settings

def embed(text: str) -> list[float]:
    res = openai.Embedding.create(
        model="text-embedding-3-large",
        input=text
    )
    return res["data"][0]["embedding"]
