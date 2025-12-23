class Memory:
    def __init__(self):
        self.short = []
        self.truth = []

    def remember(self, content: str):
        self.short.append(content)

    def store_truth(self, content: str, score: int):
        if score >= 9:
            self.truth.append(content)

    def recall_truth(self) -> str:
        return "\n".join(self.truth[-5:])
