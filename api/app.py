import os
from flask import Flask, request, jsonify, render_template, session
import requests
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates")
)
app.secret_key = os.urandom(24)  # For session management

# Load Grok API key from environment
GROK_API_KEY = os.getenv("GROK_API_KEY")
if not GROK_API_KEY:
    raise ValueError("GROK_API_KEY not set!")

# System prompt to give Maddy a personality
SYSTEM_PROMPT = """You are Maddy, a friendly and helpful AI assistant. You are:
- Warm, approachable, and conversational
- Knowledgeable but explain things clearly
- Quick to use examples and analogies
- Helpful with code, writing, analysis, and general questions
- You use markdown formatting for better readability
- You add relevant emojis occasionally to be friendly 😊
Keep responses concise but thorough. If you don't know something, say so honestly."""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/grok", methods=["POST"])
def grok_chat():
    data = request.get_json()
    prompt = data.get("prompt")
    conversation_history = data.get("history", [])
    
    if not prompt:
        return jsonify({"reply": "Please provide a prompt!"}), 400

    # Build messages with system prompt and conversation history
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Add recent conversation history (limit to last 10 exchanges for context)
    for msg in conversation_history[-20:]:
        messages.append(msg)
    
    # Add current user message
    messages.append({"role": "user", "content": prompt})

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": messages,
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        result = response.json()
        choices = result.get("choices")
        if choices and len(choices) > 0:
            reply_text = choices[0]["message"]["content"]
        else:
            reply_text = "No response from the API."
        return jsonify({
            "reply": reply_text,
            "timestamp": datetime.now().strftime("%I:%M %p")
        })
    except requests.exceptions.Timeout:
        return jsonify({"reply": "Request timed out. Please try again."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

@app.route("/clear", methods=["POST"])
def clear_chat():
    """Endpoint to clear chat history"""
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=True)

