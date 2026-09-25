from gemini_service import generate_response


def get_learning_recommendations(subject: str) -> str:
    return generate_response(
        "Create a practical, ordered learning path for this subject. "
        f"Subject: {subject}"
    )
