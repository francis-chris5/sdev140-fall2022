# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:17:23 2022

Fall 2022 Projects

@author: c.s.francis
"""

importantStuff = 42

# return method
def double(x):
    d = x * 2
    return d


# void method
def triple(x):
    t = x * 3
    print(t)
    
    
def incrementUpToQuadruple(x):
    d = 2 * x
    t = 3 * x
    q = 4 * x
    return x, d, t, q


def usesImportant():
    print(importantStuff)
##end usesImportant()


def changesImportant():
    global importantStuff
    importantStuff += 3
    








# print(double(1))
# triple(2)
# print(incrementUpToQuadruple(3))

if __name__ == "__main__":
    print(double(4))
    print(double(18))
    print(double(1))
    
    print(double(54) - 6)
    
    
    triple(3)
    
    triple(double(5))
    # double(triple(5)) ## does not work this way
    
    myTuple = incrementUpToQuadruple(4)
    
    print(myTuple)
    print(myTuple[2])
    print(myTuple[1])

    
    
    
    
    
    
    
    
    

    