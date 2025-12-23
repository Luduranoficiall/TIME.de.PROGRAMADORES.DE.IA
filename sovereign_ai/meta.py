from llm import llm

def plan(intent: str) -> list[str]:
    res = llm(
        "Define best pipeline (Architect, Backend, Reviewer, Security) "
        f"for intent:\n{intent}\nReturn comma-separated."
    )
    return [x.strip() for x in res.split(",")]

def score(output: str) -> int:
    return int(llm(
        "Score technical quality 0-10. Respond ONLY number.\n"
        f"{output}"
    ))

def refine(output: str) -> str:
    return llm(
        "Improve to enterprise-grade. No explanation.\n"
        f"{output}"
    )
