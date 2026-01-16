from flask import Flask, jsonify
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    path = os.path.join(os.path.dirname(__file__), "data.json")

    with open(path, "r") as f:
        data = json.load(f)

    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
