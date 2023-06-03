from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("sample.db", check_same_thread=False)

@app.route("/")
def home():
    table = """
        <table>

        </table>
    """
    return render_template("index.html", table = table)

@app.route("/ajax", methods=["POST"])
def ajaxStuff():
    db = sqlite3.connect("sample.db", check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT * FROM sample;")
    #c.execute("SELECT fruit, amount FROM sample WHERE fruit = ?;")
    data = c.fetchall()
    db.close()
    current = request.form.get("things")
    print(current)
    return jsonify(data)

if __name__ == "__main__":
    app.debug = True
    app.run()