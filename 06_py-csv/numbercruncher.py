"""
Matthew Yee, Jun Hong Wang
SoftDev pd7
k06 -- StI/O: divine your destiny!
2022-10-02
Time Spent:

DISCO:

QCC:

HOW THIS SCRIPT WORKS:
initial idea:
this should be very similar to what we did in 05, but instead of splitting @ and $, we split newlines and ,
split file based on newline, store in string
split each string based on comma, separate the string of occupation and percent
    if there are quotations at the beginning, only separate the comma at the end
then for the weighted random part:
    either use weighted random from random
    or make our own weighted random implementation
"""

import random

#opens file and stores in file var, then turns file into string
file = open("occupations.csv")
src = file.read()

def un_csv():
    #splits based on newline, returns array of strings
    foo = src.split("\n")
    #iterates through list of strings, but we ignore the first element in list, since it's not actually part of the data set
    for n in range(len(foo) + 1)
    return foo