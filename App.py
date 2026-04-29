from flask import Flask, request, jsonify
import os

app = Flask(__name__)

messages = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
cle = "qazwsxedcrfvtgbyhnujmikolp"
mapping = dict(zip(alphabet, cle))

def coder(msg):
    return "".join(mapping.get(c, c) for c in msg.lower())

@app.route("/")
def home():
    return "Serveur OK 🚀"

@app.route("/send", methods=["POST"])
def send():
    msg = request.json["msg"]
    messages.append(coder(msg))
    return "ok"

@app.route("/get", methods=["GET"])
def get():
    return jsonify(messages)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
