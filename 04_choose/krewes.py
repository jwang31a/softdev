"""
AJJ Eating Blue Pho: Joseph Wu, Jun Hong Wang, Anjini Katari
04_choose
SoftDev period 7
2022-09-22

DISCO:
* When importing a package, make sure to use the package name before the function.
* For example, rng.randint(0,2)
* list(dictionary) returns an array of the keys
* can have multiple types in a dictionary, can also put dictionary inside a dictionary
QCC:
OPS SUMMARY:
Initial questions about design:
* choose a list first, then a devo from that list
* but how to randomly choose a list?

Original Idea:
1) Testing with random and random package
2) Figured out how to use key to get value in dictionary
3) Figured out how to randomly choose a key
4) Randomly choose developer out of chosen list

Revised Idea:
* Use different random functions to generalize the function instead of hard coding it
1) Get a list of the periods (keys)
2) Using that list of the periods, randomly choose one and get the value associated with that key
3) Get a random developer using that list
4) Return developer
"""
import random as rng

test = {2:['Ivan', 'Talia', 'Julia'], 7:['Joseph', 'Jun Hong', 'Anjini'], 8:['Gordon', 'Joshua', 'Yuki']}

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }

#dictionary we used to test the capabilities of dictionaries (holding different types)
dd = {0:'yes', 1: 9, 2: 1.918471, 3: krewes}

# our initial method
def choosedev(dictionary):
    period = rng.randint(0,2)
    devs = []
    if period == 0:
        devs = krewes[2]
    elif period == 1:
        devs = krewes[7]
    else:
        devs = krewes[8]
    return devs[rng.randint(0, len(devs) - 1)]

#testing random
def randomtesting():
    return rng.randint(0,2)

#method we run to choose a random developer, always leave one commented out
def testing():
    #print(choosedev(krewes))
    print(choosedev2(krewes))
    
#more general method for choosing devo if there are more classes
def choosedev2(dictionary):
    classes = list(krewes)
    period = krewes[rng.choice(classes)]
    devo = period[rng.randint(0, len(period) - 1)]
    return devo