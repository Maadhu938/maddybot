---

MaddyBot

A modern AI-powered chatbot built with Flask, featuring a clean, mobile-friendly web interface and code highlighting.


---

🚀 Project Overview

MaddyBot is a web-based chatbot that leverages Flask to handle backend logic and serve dynamic, context-aware responses using the Groq API. It provides a WhatsApp-style interface with code formatting, copy buttons, and full mobile support.

Tech Stack:

- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- API: Groq (OpenAI-compatible)

---

📂 Features

- Interactive, mobile-friendly chat UI
- Remembers conversation context
- Markdown and code highlighting (with copy button)
- Responsive design for all devices
- Typing indicator and timestamps
- Persistent chat history (localStorage)
- Error handling and loading states

---

🛠️ How to Run Locally

**Prerequisites:**
- Python 3.x
- Flask

**Installation:**

1. Clone the repository:

   ```sh
git clone https://github.com/Maadhu938/maddybot.git
cd maddybot
   ```

2. Install dependencies:

   ```sh
pip install -r requirements.txt
   ```

3. Set your Groq API key as an environment variable:

   - On Windows (CMD):
     ```sh
     set GROK_API_KEY=your_key_here
     ```
   - On Linux/macOS:
     ```sh
     export GROK_API_KEY=your_key_here
     ```

4. Run the Flask app:

   ```sh
python app.py
   ```

5. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

📱 Mobile & Desktop Support

- Fully responsive: works on all phones, tablets, and desktops
- Handles mobile keyboard and scrolling issues
- Uses dynamic viewport height for best experience

---

💻 Code Formatting

- Code blocks are syntax highlighted (dark theme)
- Copy button for easy code copying

---

🚀 Deploying & Pushing to GitHub

1. Initialize git (if not already):
   ```sh
git init
git remote add origin https://github.com/YOUR_USERNAME/maddybot.git
   ```
2. Add and commit your changes:
   ```sh
git add .
git commit -m "Initial commit"
   ```
3. Push to GitHub:
   ```sh
git push -u origin main
   ```

---

🌐 Deploying to Vercel

You can deploy this Flask app to Vercel using their Python runtime:

1. **Project Structure**
   - Your Flask app should be in `api/app.py`.
   - Static files in `/static`, templates in `/templates` (at project root).
   - The root should contain `vercel.json` and `.vercelignore`.

2. **vercel.json**
   ```json
   {
     "version": 2,
     "builds": [
       { "src": "api/app.py", "use": "@vercel/python" }
     ],
     "routes": [
       { "src": "/static/(.*)", "dest": "/static/$1" },
       { "src": "/(.*)", "dest": "/api/app.py" }
     ]
   }
   ```

3. **.vercelignore**
   ```
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   venv/
   .env
   .DS_Store
   .git/
   .gitignore
   README.md
   ```

4. **Set your environment variable**
   - In the Vercel dashboard, add `GROK_API_KEY` under Project Settings > Environment Variables.

5. **Deploy**
   - Push your code to GitHub and import the repo in Vercel, or use `vercel` CLI to deploy directly.

6. **Access your app**
   - Vercel will provide a public URL after deployment.

---

📈 Future Enhancements

- Integrate advanced AI models for more natural conversations
- Add support for multiple languages
- Implement user authentication for personalized interactions
- Deploy the application to a cloud platform for public access

---

📄 License

This project is open-source and free to use for learning and personal purposes.

---
