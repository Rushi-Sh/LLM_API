import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-exp-1206")

def gemini_exp_1206(message):
    response = model.generate_content(message)
    return response.text
