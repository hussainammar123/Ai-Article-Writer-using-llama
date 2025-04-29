from flask import Flask, request, jsonify, render_template
import ollama
from ollama import Client
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# ✅ Connect to Ollama
client = Client()

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    description = data.get('description', '')

    if not description:
        return jsonify({'error': 'Description is required.'}), 400

    try:
        # ✅ Generate article using local LLaMA model
       
        response = client.chat(
            model='llama2:7b-chat',
   # or 'llama2' or whatever model you have pulled
            messages=[
                {'role': 'user', 'content': f"Write a detailed article on: {description}"}
            ],
             options={
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 4352  # ✅ limit article to ~500 tokens
    }
            
        )

        generated_text = response['message']['content'].strip()

        return jsonify({'generated_article': generated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
