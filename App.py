
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

messages = []

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 💬 ENVOI MESSAGE
@app.route("/send", methods=["POST"])
def send():

    data = request.json

    msg = data["msg"]

    messages.append(msg)

    return {"ok": True}


# 💬 RÉCUPÉRATION
@app.route("/get")
def get():

    return messages


# 📎 UPLOAD FICHIER
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    filename = file.filename

    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(path)

    user = request.form.get("user")

    messages.append(
        f"{user}:📎 {filename}"
    )

    return {"ok": True}


# 📥 DOWNLOAD
@app.route("/files/<filename>")
def files(filename):

    return send_from_directory(
        UPLOAD_FOLDER,
        filename
    )


# 🚀 START
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
