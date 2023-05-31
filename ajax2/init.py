from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/ajax", methods = ["POST"])
def ajax():
    print(request.form)
    # username = request.form['username']
    # print(username)
    return jsonify(username = username)

if __name__ == "__main__":
    app.debug = True
    app.run()