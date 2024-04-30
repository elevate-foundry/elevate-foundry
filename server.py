from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests
import datetime
import os

app = Flask(__name__)

# Retrieve OpenAI API key from GitHub secret
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    raise ValueError("OpenAI API key not found in environment variables.")

# Now you can use openai_api_key as needed in your application

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    message = request.json["message"]
    context = ""  # Initialize context variable

    def continue_conversation(prompt, context):
        endpoint = "https://api.openai.com/v1/chat/completions"
        payload = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 10000
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.post(endpoint, json=payload, headers=headers)
        if response.status_code == 200:
            completion = response.json()["choices"][0]["message"]["content"]
            return completion
        else:
            print("Error:", response.text)
            return None

    bot_response = continue_conversation(message, context)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
