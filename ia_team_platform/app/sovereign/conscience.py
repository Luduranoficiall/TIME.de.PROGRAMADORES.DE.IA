class Conscience:
    def allow_execution(self, intent: str) -> bool:
        forbidden = [
            "harm",
            "fraud",
            "exploit",
            "bypass security",
            "illegal"
        ]
        return not any(word in intent.lower() for word in forbidden)
