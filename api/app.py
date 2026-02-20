import os
from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates")
)

app.secret_key = os.urandom(24)

# Load Groq API key
GROK_API_KEY = os.getenv("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY not set!")


SYSTEM_PROMPT = """You are Maddy, a friendly and helpful AI assistant. You are:
- Warm, approachable, and conversational
- Knowledgeable but explain things clearly
- Quick to use examples and analogies
- Helpful with code, writing, analysis, and general questions
- You use markdown formatting for better readability
- You add relevant emojis occasionally to be friendly 😊
Keep responses concise but thorough. If you don't know something, say so honestly.
"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/grok", methods=["POST"])
def grok_chat():

    data = request.get_json(silent=True) or {}

    prompt = data.get("prompt")
    conversation_history = data.get("history", [])

    if not prompt or not isinstance(prompt, str):
        return jsonify({"reply": "Please provide a valid prompt."}), 400

    # ✅ Build SAFE messages list
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Only keep last 10 messages for speed + safety
    for msg in conversation_history[-10:]:

        if not isinstance(msg, dict):
            continue

        role = msg.get("role")
        content = msg.get("content")

        # Strict validation
        if role in ["user", "assistant", "system"] and isinstance(content, str) and content.strip():
            messages.append({
                "role": role,
                "content": content.strip()
            })

    # Add latest user prompt
    messages.append({
        "role": "user",
        "content": prompt.strip()
    })

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "moonshotai/kimi-k2-instruct-0905",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2048
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=45
        )

        response.raise_for_status()

        result = response.json()

        reply_text = result["choices"][0]["message"]["content"]

        return jsonify({
            "reply": reply_text,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

    except requests.exceptions.RequestException as e:

        # 🔥 This prints REAL Groq error in Vercel logs
        print("GROQ ERROR:", response.text if 'response' in locals() else str(e))

        return jsonify({
            "reply": " Sorry — I'm having trouble thinking right now. Please try again."
        }), 500


@app.route("/clear", methods=["POST"])
def clear_chat():
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)