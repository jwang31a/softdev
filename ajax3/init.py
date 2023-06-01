from flask import Flask, request, jsonify, render_template
                   
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.form["username"]
    password = request.form["password"]
    output = username + " " + password
    print(output)
    if username and password:
        print("this part ran")
        return jsonify(output=output)
    return jsonify({"error" : "ayo"})
    
if __name__ == "__main__":
    app.debug = True
    app.run()