from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.txt")

@app.route("/api/data", methods=["POST"])
def save_data():
    payload = request.get_json(silent=True) or {}
    text = payload.get("text")
    if not isinstance(text, str):
        return jsonify({"error": "Invalid payload"}), 400
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)