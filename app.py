from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

messages = []
voices = []

@app.route("/")
def home():
    return "Serveur OK 🚀"

@app.route("/send", methods=["POST"])
def send():
    msg = request.json["msg"]
    messages.append(msg)
    return "ok"

@app.route("/get")
def get():
    return jsonify(messages)

@app.route("/voice", methods=["POST"])
def voice():
    f = request.files["file"]
    name = f"voice_{len(voices)}.wav"
    f.save(name)
    voices.append(name)
    return "ok"

@app.route("/voices")
def get_voices():
    return jsonify(voices)

@app.route("/<file>")
def files(file):
    return send_file(file)

if __name__ == "__main__":
    app.run()
