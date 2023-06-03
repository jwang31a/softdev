from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("sample.db", check_same_thread=False)

@app.route("/", methods=["GET", "POST"])
def home():
    #this route has two functions: one is to render the page, the other is to respond to the ajax request
    if request.method == "POST":
        current = request.form.get("things")
        db = sqlite3.connect("sample.db", check_same_thread=False)
        c = db.cursor()
        c.execute("SELECT fruit, amount FROM sample WHERE fruit = ?;", (current,))
        data = c.fetchall()
        print(data)
        db.close()
        return jsonify({"fruit": data[0][0], "amount": data[0][1]}) 
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()