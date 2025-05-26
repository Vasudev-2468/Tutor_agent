from gemini_utils import call_gemini

def handle_math_question(question: str) -> str:
    prompt = f"You're a math tutor. Solve or explain: {question}"
    return call_gemini(prompt)
