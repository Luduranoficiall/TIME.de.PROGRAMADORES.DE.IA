from app.memory.long_term import LongTermMemory

memory = LongTermMemory()

def retrieve_context(question: str) -> str:
    docs = memory.recall(question)
    return "\n".join(docs)
