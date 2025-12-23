class CostTracker:
    def __init__(self):
        self.tokens = 0

    def add(self, amount: int):
        self.tokens += amount

    def report(self):
        return {"tokens_used": self.tokens}
