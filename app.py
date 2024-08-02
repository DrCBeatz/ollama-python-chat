# app.py

from flask import Flask, render_template, request, Response
import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://ollama:11434')
MODEL = os.getenv('MODEL_NAME', 'llama3.1:8b')

def ask_question(query):
    response = requests.post(
        f"{OLLAMA_API_URL}/api/chat",
        json={"model": MODEL, "messages": [{'role': 'user', 'content': query}]},
        stream=True
    )
    def generate():
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                chunk_str = chunk.decode('utf-8')
                logging.debug(f"Chunk: {chunk_str}")
                yield chunk_str
    return Response(generate(), content_type='text/plain')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    logging.debug(f"User input: {user_input}")
    return ask_question(user_input)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
