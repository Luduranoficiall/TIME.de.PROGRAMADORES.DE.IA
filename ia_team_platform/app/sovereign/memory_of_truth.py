class MemoryOfTruth:
    def __init__(self):
        self.validated_knowledge = []

    def store(self, content: str, score: int):
        if score >= 9:
            self.validated_knowledge.append(content)

    def recall(self) -> str:
        return "\n".join(self.validated_knowledge[-5:])
