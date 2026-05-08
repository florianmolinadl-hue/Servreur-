from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

FILE = "messages.json"

# 📦 Charger les messages
def load_messages():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# 💾 Sauvegarder
def save_messages(msgs):
    with open(FILE, "w") as f:
        json.dump(msgs, f)

# 📩 Envoyer un message
@app.route("/send", methods=["POST"])
def send():
    data = request.json
    msg = data.get("msg")

    if not msg:
        return jsonify({"error": "no msg"}), 400

    messages = load_messages()
    messages.append(msg)
    save_messages(messages)

    return jsonify({"status": "ok"})

# 📥 Récupérer messages
@app.route("/get", methods=["GET"])
def get():
    return jsonify(load_messages())

# 🚀 Run local / Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
