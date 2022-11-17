# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:14:36 2022

Fall 2022 Projects

@author: c.s.francis
"""


myList = [1, 17, 23, "hello world", True, True, False, 0, 0, 1, "blue"]

myTuple = (3, 4, 5) ## cannot be changed, otherwise just like a list

mySet = {"stuff", 23, 39, True}

myDictionary = {"name": "chris", "age": 44, "town":"clarksville"}


## list comprehension
filteredList = [x for x in myList if str(x).isnumeric() and x < 20]
print(filteredList)


if __name__ == "__main__":
    print(myList)
    print(myList[3])
    for item in myList:
        print(item)
    for index in range(len(myList)):
        print(myList[index])
        
    print()
    print()
    print()
    
    print(mySet)
    ## print(mySet[2]) ## set are all or none
    for item in mySet:
        print(item)
        
    if "stuff" in mySet:
        print("whoop there it is...")
    else:
        print("not that i seee....")
    
    if 27 in mySet:
        print("whoop there it is...")
    else:
        print("not that i seee....")
        
    print()
    print()
    print()
    
    print(myDictionary)
    print(myDictionary["age"])
    for item in myDictionary:
        print(item)
        
    ## if "name" in myDictionary.keys():
    if "chris" in myDictionary.values():
        print("found it")
    else:
        print("not here")
    
    
    
