from sqlalchemy import text
from storage import engine
from llm import llm

def embed(text_input: str) -> list[float]:
    res = llm(
        "Return ONLY a JSON array of floats as embedding for:\n"
        f"{text_input}"
    )
    return eval(res)

def store_vector(tenant_id: str, content: str, vector: list[float]):
    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO memory_vectors (tenant_id, content, embedding)
            VALUES (:tenant_id, :content, :embedding)
        """), {
            "tenant_id": tenant_id,
            "content": content,
            "embedding": vector
        })

def search_similar(tenant_id: str, query_vector: list[float], limit: int = 3):
    with engine.begin() as conn:
        result = conn.execute(text("""
            SELECT content
            FROM memory_vectors
            WHERE tenant_id = :tenant_id
            ORDER BY embedding <-> :query_vector
            LIMIT :limit
        """), {
            "tenant_id": tenant_id,
            "query_vector": query_vector,
            "limit": limit
        })
        return [row[0] for row in result]
