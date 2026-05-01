from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# 📦 DB
def get_db():
    conn = sqlite3.connect("chat.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        msg TEXT,
        time TEXT
    )
    """)

    # comptes par défaut
    try:
        c.execute("INSERT INTO users (username,password) VALUES (?,?)", ("julie","2506"))
        c.execute("INSERT INTO users (username,password) VALUES (?,?)", ("florian","88900988"))
    except:
        pass

    conn.commit()
    conn.close()

init_db()


# 🔐 LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = data.get("username")
    pwd = data.get("password")

    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (user,pwd))
    result = c.fetchone()

    conn.close()

    if result:
        return jsonify({"status":"ok"})
    return jsonify({"status":"error"})


# 📤 SEND
@app.route("/send", methods=["POST"])
def send():
    data = request.json
    user = data.get("user")
    msg = data.get("msg")

    time = datetime.now().strftime("%H:%M")

    conn = get_db()
    c = conn.cursor()

    c.execute("INSERT INTO messages (user,msg,time) VALUES (?,?,?)",
              (user,msg,time))

    conn.commit()
    conn.close()

    return jsonify({"status":"ok"})


# 📥 GET
@app.route("/get", methods=["GET"])
def get():
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT user,msg,time FROM messages ORDER BY id ASC")
    rows = c.fetchall()

    conn.close()

    messages = [
        f"{row['user']}|{row['msg']}|{row['time']}"
        for row in rows
    ]

    return jsonify(messages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
