import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

def gemini_15_pro(message):
    response = model.generate_content(message)
    return response.text
