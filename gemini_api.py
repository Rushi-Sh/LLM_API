import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def learnlm_15_pro_experimental(message):
    model = genai.GenerativeModel("learnlm-1.5-pro-experimental")
    response = model.generate_content(message)
    return response.text

def gemini_exp_1206(message):
    model = genai.GenerativeModel("gemini-exp-1206")
    response = model.generate_content(message)
    return response.text

def gemini_20_flash_thinking_exp(message):
    model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")
    response = model.generate_content(message)
    return response.text

def gemini_20_flash_exp(message):
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(message)
    return response.text

def gemini_15_pro(message):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(message)
    return response.text

def gemini_15_flash(message):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(message)
    return response.text

def gemini_15_flash_8b(message):
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    response = model.generate_content(message)
    return response.text

