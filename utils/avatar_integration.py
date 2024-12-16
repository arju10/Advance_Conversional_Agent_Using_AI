import requests
import os

DID_API_KEY = os.getenv("DID_API_KEY")

def render_avatar_response(text_response):
    url = "https://api.d-id.com/talks"
    headers = {"Authorization": f"Bearer {DID_API_KEY}"}
    payload = {
        "script": {"type": "text", "input": text_response},
        "source_url": "https://studio.d-id.com/share?id=6a68d93566e60f7eae72cba83c9dd0a7&utm_source=copy"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("result_url", "")
