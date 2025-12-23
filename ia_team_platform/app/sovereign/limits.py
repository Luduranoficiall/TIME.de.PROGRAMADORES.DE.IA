class Limits:
    MAX_COST = 10000
    MAX_ITERATIONS = 5

    def validate(self, cost: int, iterations: int) -> bool:
        if cost > self.MAX_COST:
            return False
        if iterations > self.MAX_ITERATIONS:
            return False
        return True
