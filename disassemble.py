# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 18:07:27 2022

Fall 2022 Projects

@author: c.s.francis
"""

import dis

def doubleAndLoop(x):
    double = x * 2
    for i in range(double, 0, -1):
        print("the number is going down, it's currently " +str(i))
    print("and that's all")



def divide(x, y):
    z = x / y
    return z



if __name__ == "__main__":
    # dis.dis(doubleAndLoop(5))
    dis.dis(print(divide(17, 5)))
    
   
    
