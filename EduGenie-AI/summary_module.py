from gemini_service import generate_response


def summarize_text(text: str) -> str:
    return generate_response(
        "Summarize the following text in concise bullet points. "
        f"Text: {text}"
    )
