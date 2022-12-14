# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

#we can move the methods = ['GET', 'POST'] into the app.route() as another parameter
@app.route("/", methods=['GET', 'POST']) 
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    #prints __main__
    print(app)
    print("***DIAG: request obj ***")
    #request is module, how print?
    print(request)
    print("***DIAG: request.args ***")
    #what is args? arguments provided to module?
    print(request.args)
    #is request.args an array? based on [] usage in print statement
    print("***DIAG: request.args['username']  ***")
    #prints the type then submitted username
    #for some reason this breaks the entire page, maybe because the username isn't submitted yet?
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    #not sure
    print(request.headers)
    print("request.forms")
    print(request.forms)
    #all are print statements, so should show up in the terminal
    #loads another page?
    return render_template( 'login.html' )

#confusing route link, still has old route even if both are changed?
#but works if both are the same, if not, uses old working one
@app.route("/asdf", methods=['GET', 'POST']) 
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    #if post request, then we can't print out submitted username
    #print(request.args['username'])
    #the username the user submits can actually be used, and we can serve different pages based on response
    print("***DIAG: request.headers ***")
    print(request.headers)
    print("request.forms")
    #request.form is the counterpart to request.arg but for post instead of get, also a dictionary
    print(request.form['username'])
    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
