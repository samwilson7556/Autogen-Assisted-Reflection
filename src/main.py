# main.py
from flask import Flask, request, jsonify
from src.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def home():
    return "Autogen Assisted Reflection API is up and running!"

if __name__ == "__main__":
    app.run(debug=True)
