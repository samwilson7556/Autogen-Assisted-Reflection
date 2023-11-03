# src/app.py

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Load LLM inference configurations
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Initialize agents
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture_episode():
    episode = request.form['episode']
    user_proxy.initiate_chat(assistant, message=f"Capture episode: {episode}")
    # Further processing and analysis can be done here
    return render_template('insights.html')  # Redirect to insights page

if __name__ == "__main__":
    app.run(debug=True)
