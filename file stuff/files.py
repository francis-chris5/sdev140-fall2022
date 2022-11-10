# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:34:32 2022

Fall 2022 Projects

@author: c.s.francis
"""


def simpleFileWriting():
    ## create a file handler
    toFile = open("test1.txt", "w")
    ## write text to the file
    toFile.write("hello world\n")
    toFile.write("more words\n")
    ## close
    toFile.close()



def betterWayToWriteFiles():
    with  open("test1.txt", "w") as toFile:
        toFile.write("improved file writing\n")
        toFile.write("another set of words\n")


def addToAFile():
    with  open("test1.txt", "a") as toFile:
        toFile.write("more stuff appended on\n")
        toFile.write("a whole bunch of stuff here\n")


def readFromAFile():
    temp = ""
    with open("test1.txt", "r") as fromFile:
        for line in fromFile.read():
            temp += line
        print(temp)
        
        
def pythonScript():
    with open("runThis.py", "w") as writeScript:
        writeScript.write("print(\"Hello World\")")
        

def webpage():
    with open("lookAtThis.html", "w") as createPage:
        createPage.write("<html> \n <head><title>Written By Script</title></head>\n")
        createPage.write("<body> <h1> Hello world </h1> <p>This page was created by a python script</p></body></html>")
        

    

if __name__ == "__main__":
    #simpleFileWriting()
    #betterWayToWriteFiles()
    #addToAFile()
    readFromAFile()
    pythonScript()
    webpage()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #############  for scrolling  #####################
    
