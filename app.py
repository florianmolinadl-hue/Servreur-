from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return "Serveur OK 🚀"

@app.route("/send", methods=["POST"])
def send():
    try:
        msg = request.json["msg"]
        messages.append(msg)
        return "ok"
    except:
        return "error", 400

@app.route("/get")
def get():
    return jsonify(messages)

# IMPORTANT RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
