def calculate_cost(tokens_used: int, price_per_token: float = 0.000002) -> float:
    return tokens_used * price_per_token
