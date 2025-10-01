from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)

# Load Grok API key from environment
GROK_API_KEY = os.getenv("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY not set!")

@app.route("/")
def index():
    return render_template("index.html")  # Serve HTML from templates folder

@app.route("/grok", methods=["POST"])
def grok_chat():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"reply": "Please provide a prompt!"}), 400

    url = "https://api.groq.com/openai/v1/chat/completions"  # Replace with your Grok endpoint
    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"model": "openai/gpt-oss-120b", "messages": [{"role": "user", "content": prompt}],"max_tokens": 1000}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        choices=result.get("choices")
        if choices and len(choices) > 0:
            reply_text = choices[0]["message"]["content"]
        else:
            reply_text = "No response from Grok."
        return jsonify({"reply": reply_text})
    except requests.exceptions.RequestException as e:
        return jsonify({"reply": f"Error contacting Grok API: {str(e)}"}), 500

if __name__ == "__main__":
    # Serve externally if needed: 0.0.0.0
    app.run(host="127.0.0.1", port=5000, debug=True)