#this stuff is all a demo to test my ajax skills

import sqlite3, json

db = sqlite3.connect("data.db", check_same_thread = False)
c = db.cursor()
c.executescript(
    """
    DROP TABLE IF EXISTS Login;
    DROP TABLE IF EXISTS Words;
    """
)

c.executescript(
    """
    CREATE TABLE IF NOT EXISTS Login(username text, password text);
    CREATE TABLE IF NOT EXISTS WORDS(sentence text);
    """
)

db.commit()
db.close()

#u = username, p = password
def addUser(u, p):
    db = sqlite3.connect("data.db", check_same_thread = False)
    c = db.cursor()
    c.execute("SELECT ? from Login", (u,))
    data = c.fetchall()
    if data != []:
        return False
    c.execute("INSERT INTO Login values (?, ?)", (u, p))
    db.commit()
    db.close()
    return True

def addWords():
    return 0

def checkUser(u):
    db = sqlite3.connect("data.db", check_same_thread = False)
    c = db.cursor()
    c.execute("SELECT username, password from Login FROM Login WHERE username = ?", (u,))
    username = c.fetchall()
    db.close()
    return 0