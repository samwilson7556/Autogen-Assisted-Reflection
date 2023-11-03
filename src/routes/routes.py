# File: src/routes/routes.py

from flask import Flask, request, jsonify
from src.services.service import capture_episode

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    episode_text = request.json.get('episode_text', '')
    if not episode_text:
        return jsonify({'error': 'episode_text is required'}), 400
    
    insights = capture_episode(episode_text)
    return jsonify({'insights': insights}), 200

if __name__ == '__main__':
    app.run(debug=True)
