from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

# 🔑 Add your API key here
client = genai.Client(api_key=os.getenv("AIzaSyBn1PbYfedPwXURZH6x13T0lks9um6-Pqo"))

@app.route("/")
def home():
    return "Free Telugu AI Assistant Running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"You are a helpful assistant. Reply in Telugu or English clearly.\nUser: {user_message}"
    )

    return jsonify({"reply": response.text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)