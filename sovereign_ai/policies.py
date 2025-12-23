BLOCKED_WORDS = ["fraud", "illegal", "exploit"]

def allowed(intent: str) -> bool:
    return not any(w in intent.lower() for w in BLOCKED_WORDS)
