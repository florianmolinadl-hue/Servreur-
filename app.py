from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

# 🏠 test serveur
@app.route("/")
def home():
    return "Serveur OK 🚀"

# 📤 envoyer message
@app.route("/send", methods=["POST"])
def send():
    data = request.json

    if not data or "msg" not in data:
        return "error", 400

    messages.append(data["msg"])
    return "ok"

# 📥 récupérer messages
@app.route("/get")
def get():
    return jsonify(messages)


# 🚀 LANCEMENT (important pour Render)
if __name__ == "__main__":
    app.run()
