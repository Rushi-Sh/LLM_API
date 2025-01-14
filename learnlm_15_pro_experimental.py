import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("learnlm-1.5-pro-experimental")

def learnlm_15_pro_experimental(message):
    response = model.generate_content(message)
    return response.text
