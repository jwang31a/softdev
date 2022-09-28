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

krewes = {}

def read():
    

def randomDevo():
    randKey = random.choice(list(krewes.keys()))
    l = len(krewes[randKey])
    return krewes[randKey][random.randrange(0,l,1)]

print(randomDevo())