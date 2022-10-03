"""
The Hacking Hornets: Matthew Yee, Jun Hong Wang
SoftDev pd7
k06 -- StI/O: divine your destiny!
2022-10-02
Time Spent: 1.3 hrs
DISCO:
* lists and arrays are different in Python, to use arrays, we have to import the module
* use random.uniform(lower bound, upper bound) instead of randrange if we want to get floats/non-ints
* split(char) splits a string wherever it sees that character
QCC:
* is there a way to do weighted random without having to implement it ourselves?
HOW THIS SCRIPT WORKS:
initial idea:
this should be very similar to what we did in 05, but instead of splitting @ and $, we split newlines and ,
split file based on newline, store in string
split each string based on comma, separate the string of occupation and percent
    if there are quotations at the beginning, only separate the comma at the end
then for the weighted random part:
    either use weighted random from random
    or make our own weighted random implementation
    
1) Open file, file.readlines() to split each line into own string and put into list
2) Call un_csv() to separate the commas
    loop through each string in list, see if it has a " in it
    if it does, we call un_comma(substring) to split based on comma between the full occupation and percentage
    if it doesn't, we can just split(",") to get rid of the comma
    we convert the string with the number to a float
    add the information to dictionary, with occupation as the key, and percentage as the value
3) We randomly choose the occupation by calling rand_occ, which:
    keeps track of s, the percentages of occupations we subtract
    then goes into a for loop through the dictionary, generating a random number between 0 and 99.9 - s
    if that random number is less than the percentage of occupation, then return that occupation
    else, we add that percentage to s, and we keep going on in the for loop
    this keeps the original probability of landing on each occupation
"""

import random

#opens file and stores in file var, then turns file into string
file = open("occupations.csv")
#rename to src if uncommented foo in un_csv()
foo = file.readlines()
#empty dictionary to be populated by un_csv()
d = {}

def un_csv():
    #splits based on newline, returns list of strings
    """
    commented out foo bc readlines() does it for us
    if want to make src.split() work, change range of for loop to -2
    """
    #foo is list of strings
    #foo = src.split("\n")
    #iterates through list of strings, but we ignore the first and last elements in list, since it's not actually part of the data set
    for n in range(1, len(foo) - 1):
        #list to store occupation and percent
        l = []
        #if the first char is ", then there is a comma somewhere inside the job class, so we can't just split
        if foo[n][0] == "\"":
            l = un_comma(foo[n])
        #else, we can just split and store the information in dictionary
        else:
            l = foo[n].split(",")
            #split converts into 2 strings, so we have to convert into int
            l[1] = float(l[1])
        d[l[0]] = l[1]
    return d

#very similar to what we did in 05, iterating through a string to find chars/strings we don't want
def un_comma(substring):
    #vars to store information
    occ = ""
    per = 0
    for n in range(1, len(substring)):
        if substring[n] == "\"":
            occ = substring[1:n]
            break
    per = float(substring[n+2:len(substring)])
    return [occ, per]

def rand_occ():
    #per = d.values()
    s = 0
    #loops through dictionary
    for n in d:
        #stores a random number from 0 to 99.9 - s
        #used random.uniform instead of randrange bc randrange takes integers
        r = random.uniform(0, 99.9 - s)
        #if the randomly generated number is less than the value, then we return the occupation
        if r < d[n]:
            return n
        #else, increment s by the value, so that we generate numbers from 0 to a lower bound
        else:
            s += d[n]

#main function to run code easily
def main():
    un_csv()
    print(rand_occ())
