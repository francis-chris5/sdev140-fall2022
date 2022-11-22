# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:36:34 2022

Fall 2022 Projects

@author: c.s.francis
"""



class Animal():
    def __init__(self, name, age, weight, sound):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__sound = sound


    def getName(self):
        return self.__name
    
    def setName(self, newName):
        self.__name = newName
        
    def getAge(self):
        return self.__age
    
    def setAge(self, newAge):
        self.__age = newAge
        
    def getWeight(self):
        return self.__weight
    
    def setWeight(self, newWeight):
        self.__weight = newWeight
        
    def getSound(self):
        return self.__sound
    
    def setSound(self, newSound):
        self.__sound = newSound
        
    def makeSound(self):
        return self.getSound() + " " + self.getSound() + " " + self.getSound()

    def __str__(self):
        return "This is " + self.getName() + " who is a " + str(self.getAge()) + " year old, and goes " + self.makeSound()
    
    def __eq__(self, obj):
        if isinstance(obj, Animal) and self.getAge() == obj.getAge():
            return True
        else:
            return False
            

if __name__ == "__main__":
    pass
    
