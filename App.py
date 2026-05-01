from flask import Flask, request, jsonify
import os

app = Flask(__name__)

FILE = "messages.txt"

if not os.path.exists(FILE):
    open(FILE, "w").close()


def load():
    with open(FILE, "r", encoding="utf-8") as f:
        return [l.strip() for l in f.readlines()]


def save(msg):
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


@app.route("/send", methods=["POST"])
def send():
    msg = request.json.get("msg")
    if msg:
        save(msg)
    return "ok"


@app.route("/get")
def get():
    return jsonify(load())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
