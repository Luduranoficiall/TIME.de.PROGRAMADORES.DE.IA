class ShortTermMemory:
    def __init__(self):
        self.buffer = []

    def add(self, content: str):
        self.buffer.append(content)

    def context(self) -> str:
        return "\n".join(self.buffer[-10:])
