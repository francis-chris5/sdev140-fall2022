# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:39:37 2022

Fall 2022 Projects

@author: c.s.francis
"""

total = 0
choice = input("Is there another item? (Yes, No)")
recieptPrinter = open("receipt.txt", "w")


while choice.lower() == "yes":
    price = float(input("how much is it? "))
    tax = price * 0.07
    total += price + tax
    recieptPrinter.write("price: " + format(price, ".2f") + "\ttax: " + format(tax, ".2f") + "\n")
    
    choice = input("Is there another item? (Yes, No)")
    

print("the total is $" + format(total, ".2f"))
recieptPrinter.write("\n\n\nthe total is $" + format(total, ".2f"))
recieptPrinter.close()



if __name__ == "__main__":
    #print("Ready to run...")
    pass
    
