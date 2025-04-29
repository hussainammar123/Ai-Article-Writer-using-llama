#AI ARTICLE WRITER
📝 AI Article Writer (Using Ollama + Flask)
A lightweight, fast, and locally hosted AI Article Generator Web App that uses LLaMA models via Ollama and a Flask backend to generate high-quality articles from simple user prompts — with no cloud dependency.

🚀 Features
✨ AI-generated articles based on user prompts using LLaMA models

🧠 Powered by Ollama and models like llama2, llama3, or mistral

🌐 Clean and responsive web interface (HTML, CSS, JS)

⚡ Fast local execution — no need for OpenAI API

📋 One-click Copy to Clipboard for generated articles

🕒 Loading animation while article is being generated

🔐 100% local — great for privacy-focused users

📦 Technologies Used
Python 3.x

Flask – lightweight Python web framework

Ollama – for running large language models locally

HTML5, CSS3, JavaScript – for frontend

LLaMA models – via ollama client (e.g., llama3, llama2:7b-chat)

📸 Screenshots
(Add your own UI screenshots here for a visual boost!)

🛠 Installation & Setup
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/ai-article-writer.git
cd ai-article-writer
2. Install Python dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Install and Run Ollama
Make sure Ollama is installed.

bash
Copy
Edit
ollama pull llama2:7b-chat
ollama serve
4. Start the Flask server

python app.py
Open your browser and go to: http://127.0.0.1:5000

✍️ Usage
Enter a topic or description in the input box.

Click "Generate Article".

Wait for the AI to create the article.

Click "Copy Article" to save it to your clipboard.

💡 Customization
#You can change the model by editing app.py:

response = client.chat(
    model='llama2:7b-chat',
    ...
)
#To use other models like llama3, mistral, or custom fine-tuned models, pull them using:

ollama pull llama3
📁 Project Structure
/static
    └── articles_background.png
/templates
    └── index.html
app.py
README.md
✅ Future Enhancements
Streamed output (real-time typing effect)

Export article to PDF or DOCX

Save article history

Add article title generation

Add user authentication

🧠 Credits
Ollama – for enabling local LLMs

Meta AI (LLaMA) – for powerful open-source models

Flask – simple and powerful Python web framework

.
