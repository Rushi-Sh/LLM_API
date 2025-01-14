import os
from groq import Groq


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def whisper_large_v3_turbo(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="whisper-large-v3-turbo",
    )
    return chat_completion.choices[0].message.content


def llama_3_3_70b_versatile(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content


def gemma2_9b_it(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gemma2-9b-it",
    )
    return chat_completion.choices[0].message.content


def llama_3_2_90b_vision_preview(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-3.2-90b-vision-preview",
    )
    return chat_completion.choices[0].message.content


def llama3_70b_8192(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content


def llama_3_2_1b_preview(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-3.2-1b-preview",
    )
    return chat_completion.choices[0].message.content


def llama_guard_3_8b(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-guard-3-8b",
    )
    return chat_completion.choices[0].message.content


def llama_3_2_11b_vision_preview(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )
    return chat_completion.choices[0].message.content


def llama_3_3_70b_specdec(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-3.3-70b-specdec",
    )
    return chat_completion.choices[0].message.content
