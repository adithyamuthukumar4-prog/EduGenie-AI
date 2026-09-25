import os

from dotenv import load_dotenv

load_dotenv()


def generate_response(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Gemini is not configured. Add GEMINI_API_KEY to the .env file."

    from google import genai

    client = genai.Client(api_key=api_key)
    model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text or "Gemini returned an empty response."
