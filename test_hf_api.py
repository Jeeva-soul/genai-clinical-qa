import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
headers = {
    "Authorization": f"Bearer " + os.getenv("HUGGINGFACEHUB_API_TOKEN")
}

data = {
    "inputs": "What is diabetes?",
    "parameters": {"max_new_tokens": 100}
}

response = requests.post(API_URL, headers=headers, json=data)

try:
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(f"❌ Error parsing response: {e}")
    print(f"Raw text: {response.text}")
