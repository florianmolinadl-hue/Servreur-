from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# 📁 dossier pour stocker les audios
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

messages = []


# 💬 envoyer message texte
@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    msg = data.get("msg", "")
    messages.append(msg)
    return "ok"


# 📥 récupérer messages
@app.route("/get", methods=["GET"])
def get():
    return jsonify(messages)


# 🎤 upload audio
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return "no file", 400

    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    # on envoie le nom du fichier au chat
    messages.append("AUDIO:" + filename)

    return "ok"


# 🎧 récupérer audio
@app.route("/audio/<filename>")
def get_audio(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# 🚀 lancement
if __name__ == "__main__":
    app
