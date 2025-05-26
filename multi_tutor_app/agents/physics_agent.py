from gemini_utils import call_gemini

def handle_physics_question(question: str) -> str:
    prompt = f"You're a physics tutor. Explain or solve: {question}"
    return call_gemini(prompt)
