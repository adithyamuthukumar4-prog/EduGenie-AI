from gemini_service import generate_response


def explain_topic(topic: str) -> str:
    return generate_response(
        "Explain this topic for a student using simple language and a short example. "
        f"Topic: {topic}"
    )
