from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import os

app = Flask(__name__)
CORS(app)

# Gemini Client
client = genai.Client(
    api_key=os.getenv("AIzaSyDlWfPiXWZPzhX1IfBPBizI9c_WVYYJtCs")
)

# Home Route
@app.route("/")
def home():
    return "Free Telugu AI Assistant Running Successfully!"

# Chat Route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        # Check message exists
        if not data or "message" not in data:
            return jsonify({
                "reply": "Please send a message"
            }), 400

        user_message = data["message"]

        # Gemini Response
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
You are a helpful AI assistant.

Rules:
- Reply clearly
- Use Telugu or English
- Keep answers simple and friendly

User: {user_message}
"""
        )

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server Error: {str(e)}"
        }), 500


# Run Flask App
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )