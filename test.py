import requests

url = "https://ai-chatbot-1-cgan.onrender.com/chat"

data = {
    "message": "Hello"
}

response = requests.post(url, json=data)

print(response.json())