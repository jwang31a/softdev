# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    #print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
* We can see what's returned in the webpage itself, as plain text.
* There's no value for name, so the name doesn't show. 

QCC:
0. Looks like a constructor from object oriented programming, like Java from last year.
1. Could refer to location (like in local files?), based on what route means, as well as the meaning of / in the terminal.
2. Print to webpage?
3. 
4. Since it's return, it probably won't say anything until we print it. However, since it launches a webpage, it might be visible somewhere there, like in the console. 
5. app.run() looks like it's making the object app do something, like in an object-oriented programming language
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
