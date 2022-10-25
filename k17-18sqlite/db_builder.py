#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

command = f"CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#courses and students.csv
f = open("students.csv")
d = csv.DictReader(f)
for row in d:
    #to remove newline at end
    print(row)
    #row is in name, age, id
    n = row['name']
    a = row['age']
    i = row['id']
    con = f"INSERT INTO students VALUES ({n}, {a}, {i});"
    c.execute(con)
    #print(n, a, i)



"""
#==========================================================

db.commit() #save changes
db.close()  #close database
"""

