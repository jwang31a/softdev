"""
Matthew Yee, Jun Hong Wang
SoftDev pd7
k05 -- text file to dictionary
2022-09-28
Time Spent: 1.8 hrs
DISCO:
We learned how to add elements to an array using array and .append
Learned how to add keys to a dictionary
open("filename") creates a file object that can be stored, and file.read() will convert that into a string
QCC:
Why doesn't numpy exist?
When we tried to use a function from numpy, it wouldn't work because numpy was missing, even though we imported it. 
OPS SUMMARY:
1) open file, read file to turn into string
2) translate string into dictionary:
    iterate through the string, until hit @ or end of string
    use substring, then cut it up between $
    turn the information inside the substring into an array containing the period, name, and dname
    check if key exists, if not, make a new key and add that array to the array for that dict
    if it does, add array to value
3) use random_devo() to randomly select devo + duckie + period
"""

import random
import array

#opens krewes.txt and makes a file
file = open("krewes.txt")
#converts into string
src = file.read()
#empty initial krewes dict
krewes = {}

#converts string into dictionary
def translate():
    #keeps track of first non @ char
    prev_ind = 0
    #for loop for indices
    for n in range(len(src)):
        substring = ""
        info = []
        #checks against @@@ in case someone has @ in their name
        if src[n:n + 3] == "@@@" or n == len(src) - 1:
            substring = src[prev_ind:n]
            #calls helper function to return all the information related to a person
            info = helper(substring)
            #searches for existing keys matching one from current person
            if search(list(krewes), info[0]):
                krewes[info[0]].append([info[0], info[1], info[2]])
            #creating a new key if key doesn't exist
            else:
                krewes[info[0]] = [ [ info[0], info[1], info[2] ] ]
            prev_ind = n + 3
    return krewes

#copy paste pretty much from translate, but instead of filtering for @, we filter for $
def helper(substring):
    #keeps track of first non $ char
    prev_ind = 0
    #keeps track of key, name, dname
    key = 0
    name = ""
    dname = ""
    #for loop for indices
    for n in range(len(src)):
        #checks for period
        if prev_ind == 0 and substring[n:n + 3] == "$$$":
            key = substring[prev_ind : n]
            prev_ind = n + 3
        #checks for name
        elif substring[n:n + 3] == "$$$":
            name = substring[prev_ind : n]
            prev_ind = n + 3
        #duckie name
        else:
            dname = substring[prev_ind : n]
    #temp return
    return [key, name, dname]

#linear search
#l is the list we're searching through, key is what we're looking for
def search(l, key):
    for n in l:
        if key == n:
            return True
    return False
    #returns true or false

#our function for randomly choosing devo and duckie
def random_devo():
    rand_key = random.choice(list(krewes.keys()))
    l = len(krewes[rand_key])
    #test to make sure it got devos and duckies from different periods
    #print(rand_key + "\n")
    return krewes[rand_key][random.randrange(0,l,1)]

#main function for running code
def main():
    translate()
    print(random_devo())
