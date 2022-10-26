import csv

#opens a file, creates file object
f = open("students.csv")
#creates dictionary
r = csv.DictReader(f)
#prints each row
for row in f:
    #print(row)
    #to remove newline at end
    row = row.strip("\n")
    #then individual elements in list
    l = row.split(",")
    print(l)