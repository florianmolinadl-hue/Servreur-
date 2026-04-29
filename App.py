from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
cle = "qazwsxedcrfvtgbyhnujmikolp"
mapping = dict(zip(alphabet, cle))

def coder(msg):
    return "".join(mapping.get(c, c) for c in msg.lower())

@app.route("/send", methods=["POST"])
def send():
    msg = request.json["msg"]
    messages.append(coder(msg))
    return "ok"
    SERVER = "https://chat-abc123.onrender.com"
