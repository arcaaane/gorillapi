from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "A content packed API for all things Gorilla Tag!"})

@app.route("/hello")
def main():
    return jsonify({"message": f"Hello {name}!"})

def handler(environ, start_response):
    return app(environ, start_response)
