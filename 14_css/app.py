from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask objectls


@app.route("/")

def mimic():
    return render_template ('index.html')

  
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()