from gemini_service import generate_response


def answer_question(question: str) -> str:
    return generate_response(
        "Answer this educational question clearly and accurately. "
        f"Question: {question}"
    )
