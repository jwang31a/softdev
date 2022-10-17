"""
TEAM NAME
SoftDev
K12 -- Making a form using templates and the difference between post and get
2022-10-17
time spent: 1 hour
"""

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

@app.route("/") 
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST']) #you need methods = in order for a post request to work
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    if request.method == 'GET': # make sure post doesn't break the webpage
        print("***DIAG: request.args['username']  ***")
        print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    #print("REQUEST TYPE")
    #print(str(type(request))) request is NOT a string or dictionary (<class 'werkzeug.local.LocalProxy'>)
    if request.method == 'POST': # you can cat a string to a template and it will put it below everything
        return render_template('response.html')+"Username: "+ request.form['username']+"<br> Request: " \
                 + request.method +"<br> HEY!"
    else:
        return render_template('response.html')+"Username: "+ request.args['username']+"<br> Request: " \
                + request.method +"<br> HEY!" #request.method returns the request type
        


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()