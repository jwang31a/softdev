from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods = ["POST"])
def ajax():
    username = request.form["username"]
    password = request.form["password"]
    output = username + " " + password
    print(output)
    return jsonify({"output" : "user info " + output})

if __name__ == "__main__":
    app.debug = True
    app.run()