from flask import Flask, jsonify
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    path = os.path.join(os.path.dirname(__file__), "data.json")

    with open(path, "r") as f:
        data = json.load(f)

    return jsonify(data)

def handler(environ, start_response):
    return app(environ, start_response)
