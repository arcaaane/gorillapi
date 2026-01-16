from flask import Flask, jsonify
import json, os

app = Flask(__name__)

from flask import Flask, jsonify
import json, os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(path, "r") as f:
        local_data = json.load(f)
    try:
        r = requests.get("https://gtag-api-one.vercel.app/api/gorilla-tag", timeout=5)
        external_json = r.json()
        build_id = external_json.get("buildId")
        build_date = external_json.get("date")

    except Exception as e:
        build_id = None
        build_date = None

    response = {
        "gorillatag-build-id": build_id,
        "gorillatag-build-date": build_date,
        **local_data
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
