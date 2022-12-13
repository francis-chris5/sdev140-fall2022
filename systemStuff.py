# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:34:02 2022

Fall 2022 Projects

@author: c.s.francis
"""

from os import makedirs, listdir
from os.path import isdir, isfile, join

import sys

## add a directory to look for python modules to import with
#sys.path.insert(0, "C:/Users/franc/Documents")
#import most


## dig through the folders and files on a computer
def checkDirectory(path):
    folderCounter = 0
    fileCounter = 0
    for item in listdir(path):
        if isdir(join(path, item)):
            print(item + " -- it's a directory" )
            folderCounter += 1
        elif isfile(join(path, item)):
            print(item + " ++ this one's a file")
            fileCounter += 1
    print("folders: " + str(folderCounter) + ", files: " + str(fileCounter))
          
          
            
        
        
        




if __name__ == "__main__":
    workingDirectory = "C:/Users/franc/Documents/delete"
    checkDirectory(workingDirectory)
    if not isdir(join(workingDirectory, "newestStuff")):
        makedirs("newestStuff")
    with open("newestStuff/morestuff.txt", "w") as toFile:
        toFile.write("Here are some words for the file\n")
        
    checkDirectory(workingDirectory)
    checkDirectory(workingDirectory + "/newestStuff")
    
        
    
    
    
    
    
