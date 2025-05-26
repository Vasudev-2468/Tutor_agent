import google.generativeai as genai

genai.configure(api_key="AIzaSyDEpPNn7OVd8Ib7McC-chWFBMh-YXk38GQ")

def call_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("models/gemma-3n-e4b-it")  # <-- Correct model path
    response = model.generate_content(prompt)
    return response.text
