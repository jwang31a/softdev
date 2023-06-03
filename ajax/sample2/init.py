from flask import Flask, request, render_template, jsonify, redirect
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("sample.db", check_same_thread=False)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    current = request.form["fruit"]
    print(current)
    db = sqlite3.connect("sample.db", check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT fruit, amount FROM sample WHERE fruit = ?;", (current,))
    raw = c.fetchall()
    db.close()
    if raw:
        data = raw[0][0] + " " + str(raw[0][1])
        return jsonify(data=data)
    return jsonify({"error": "you stupid"})

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")