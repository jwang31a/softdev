"""
Matthew Yee, Jun Hong Wang
SoftDev pd7
k05
2022-09-28
Time Spent:

DISCO:
QCC:
OPS SUMMARY:
"""

import random

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
        #checks against @@@ in case someone has @ in their name
        if src[n:n + 3] == "@@@":
            substring = src[prev_ind:n]
            helper(substring)
            prev_ind = n + 3

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
            
    #returns true or false
        
def random_devo():
    rand_key = random.choice(list(krewes.keys()))
    l = len(krewes[rand_key])
    return krewes[rand_key][random.randrange(0,l,1)]

#print(random_devo())