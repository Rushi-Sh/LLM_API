import requests
import os
import json


api_key = os.environ.get("GROQ_API_KEY")


url = "https://api.groq.com/openai/v1/models"


headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


response = requests.get(url, headers=headers)


response_data = response.json()


output_file = "groq_models.json"
with open(output_file, "w") as file:
    json.dump(response_data, file, indent=4)

print(f"Response saved to {output_file}")
