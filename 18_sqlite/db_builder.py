#Spooky Ghosts: Jun Hong Wang, James Yu, Thomas Zhang
#softdev pd7
#k18 -- sqlite in python
#2022-10-26
#time spent: 1.5 hrs

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#auto delete pre-existing tables to make way for new table creation
#c.execute("DROP TABLE if exists students")
c.execute("DROP TABLE if exists courses")
c.execute("DROP TABLE if exists students")

#if keep running this, the table will keep expanding
#c.execute("CREATE TABLE if not exists students (name TEXT, age INTEGER, id INTEGER)")

#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

#creates tables we will populate
command = f"CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

command = f"CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)

#appears that commands starting with "." don't work
#c.execute(".headers on")

#now using with to simplify open process
#for students.csv
#semicolons not needed in c.execute()
with open("students.csv", newline='') as f:
    d = csv.DictReader(f)
    for row in d:
        #debug print statement to see what's in each row
        print(row)
        #row is in name, age, id
        n = row['name']
        a = row['age']
        i = row['id']
        #fstring with information from vars into structure of command
        con = f"INSERT INTO students VALUES (\"{n}\", \"{a}\", \"{i}\")"
        c.execute(con)

#for courses.csv
with open("courses.csv", newline='') as f2:
    d2 = csv.DictReader(f2)
    for row in d2:
        #debug print statement to see what's in each row
        print(row)
        #row is in code, mark, id
        code = row['code']
        mark = row['mark']
        i = row['id']
        #fstring with information from vars into structure of command
        con = f"INSERT INTO courses VALUES (\"{code}\", \"{mark}\", \"{i}\");"
        c.execute(con)

#==========================================================
#if this part is commented out, the commands from code above aren't loaded, so the tables aren't populated
db.commit() #save changes
db.close()  #close database


