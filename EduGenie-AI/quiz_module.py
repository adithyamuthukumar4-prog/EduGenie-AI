from gemini_service import generate_response


def generate_quiz(text: str) -> str:
    return generate_response(
        "Create a short quiz from this material. Include questions and answers. "
        f"Material: {text}"
    )
