from app.memory.embeddings import embed

class LongTermMemory:
    def __init__(self):
        self.vectors = []

    def store(self, text: str):
        self.vectors.append({
            "text": text,
            "vector": embed(text)
        })

    def recall(self, query: str) -> list[str]:
        # Similaridade simplificada (substituir por pgvector)
        return [v["text"] for v in self.vectors[:3]]
