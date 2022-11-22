"""
Jun Hong Wang and Ravindra Mangar
softdev pd7
k20: restful journey skyward (getting information from api)
2022-11-21
time spent: 0.6 hrs
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)
file = open("key_nasa.txt")
key = file.read()
file.close()

@app.route("/")
def image():
    url = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}")
    u = url.json()
    print(u)
    return render_template("main.html", imageurl=u["url"])

if __name__ == "__main__": 
    app.debug = True
    app.run()    
