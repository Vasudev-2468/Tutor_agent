# from agents.math_agent import handle_math_question
# from agents.physics_agent import handle_physics_question

# def classify_and_delegate(question: str) -> str:
#     lower_q = question.lower().strip()

#     # Expanded keyword lists for each subject
#     math_keywords = [
#         "integrate", "solve", "equation", "algebra", "calculate", "derivative",
#         "differentiation", "integration", "probability", "permutation", "combination",
#         "trigonometry", "logarithm", "matrix", "vectors", "geometry", "limits", "mean", "mode", "median"
#     ]

#     physics_keywords = [
#         "velocity", "acceleration", "force", "newton", "kinematics", "gravity",
#         "thermodynamics", "friction", "energy", "work", "momentum", "optics",
#         "magnetism", "wave", "quantum", "current", "voltage", "resistance", "pressure"
#     ]

#     # Check for math-related words
#     if any(word in lower_q for word in math_keywords):
#         return handle_math_question(question)

#     # Check for physics-related words
#     elif any(word in lower_q for word in physics_keywords):
#         return handle_physics_question(question)

#     # Default fallback
#     return "Sorry, I can't classify the subject of your question."



# Using the Generative ai to experiment the results

import os
from dotenv import load_dotenv
import google.generativeai as genai

from agents.math_agent import handle_math_question
from agents.physics_agent import handle_physics_question

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def classify_and_delegate(question: str) -> str:
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

        prompt = f"""
        Classify the following question into one of these subjects: Math or Physics.
        Respond with only one word: 'Math' or 'Physics'.

        Question: "{question}"
        """

        response = model.generate_content(prompt)
        subject = response.text.strip().lower()

        # Debug (optional)
        print(f"[Classifier] Gemini classified subject as: {subject}")

        if "math" in subject:
            return handle_math_question(question)
        elif "physics" in subject:
            return handle_physics_question(question)
        else:
            return "Sorry, I couldn't classify your question confidently."

    except Exception as e:
        return f"Error during classification or delegation: {str(e)}"
