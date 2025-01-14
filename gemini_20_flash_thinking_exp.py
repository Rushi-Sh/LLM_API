import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")

def gemini_20_flash_thinking_exp(message):
    response = model.generate_content(message)
    return response.text
