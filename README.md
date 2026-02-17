# 🚀 MaddyBot — AI Chat Assistant

**MaddyBot** is a modern, production-ready AI chatbot built with **Flask** that delivers fast, context-aware conversations through a clean, mobile-first interface. It integrates Groq’s high-performance LLM API to provide intelligent responses with minimal latency.

Designed with usability and performance in mind, MaddyBot offers a seamless chat experience across desktop and mobile devices while maintaining a scalable backend architecture.

---

## 🌐 Live Demo
👉 https://maddybot.maadhuavati.in  
_Deployed on a custom domain with secure HTTPS._

---

# ✨ Key Highlights

- ⚡ Real-time AI conversations powered by Groq  
- 📱 Fully responsive, mobile-first UI  
- 💬 Persistent chat history using localStorage  
- 🧠 Context-aware responses  
- 🎨 Markdown rendering with syntax-highlighted code blocks  
- 📋 One-click code copy functionality  
- ⏳ Typing indicators for natural interaction  
- 🛡️ Robust error handling  
- 🌍 Production deployment on a custom subdomain  

---

# 🧠 Tech Stack

### Backend
- Python  
- Flask  
- Groq API (OpenAI-compatible)

### Frontend
- HTML5  
- CSS3  
- Vanilla JavaScript  

### Deployment
- Vercel (Serverless Functions)  
- Custom Domain with HTTPS  

---

# 📂 Core Features

## ✅ Intelligent Chat Interface
A WhatsApp-style conversational layout designed for clarity and ease of use.

## ✅ Context Retention
Maintains recent conversation history to generate more relevant responses.

## ✅ Developer-Friendly Formatting
- Automatic markdown parsing  
- Syntax-highlighted code blocks  
- Copy button for rapid usage  

## ✅ Mobile Optimization
Handles viewport resizing, keyboard behavior, and scrolling for a smooth mobile experience.

---

# 🛠️ Run Locally

## Prerequisites
- Python 3.x  
- pip  

---

## 1. Clone the Repository
```bash
git clone https://github.com/Maadhu938/maddybot.git
cd maddybot
```

---

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variable

### Windows (CMD)
```bash
set GROK_API_KEY=your_key_here
```

### macOS / Linux
```bash
export GROK_API_KEY=your_key_here
```

---

## 4. Start the Server
```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🚀 Deployment Guide (Vercel)

## Recommended Project Structure
```
project-root
│
├── api/
│     └── app.py
├── static/
├── templates/
├── vercel.json
└── .vercelignore
```

---

## vercel.json
```json
{
  "version": 2,
  "builds": [
    { "src": "api/app.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "handle": "filesystem" },
    { "src": "/(.*)", "dest": "/api/app.py" }
  ]
}
```

**Important:**  
`"handle": "filesystem"` ensures static assets load correctly before requests reach Flask.

---

## Environment Variables

Add your API key inside:

**Vercel Dashboard → Project Settings → Environment Variables**

```
GROK_API_KEY=your_key_here
```

Redeploy after adding it.

---

# 📈 Future Improvements

- 🔥 Streaming AI responses for real-time typing  
- 👤 User authentication & personalized memory  
- 🌎 Multi-language support  
- 📊 Usage analytics dashboard  
- ⚡ Dedicated backend hosting for improved scalability  
- 🧠 Long-term conversational memory  

---

# 💡 What This Project Demonstrates

This project showcases the ability to:

✅ Design and deploy production-grade web applications  
✅ Integrate large language model APIs  
✅ Build responsive, user-focused interfaces  
✅ Configure serverless deployments  
✅ Manage environment variables securely  
✅ Debug real-world deployment challenges  

---

# 📄 License
Open-source and available for educational and personal use.

---

## ⭐ If you found this project interesting, consider starring the repository!
