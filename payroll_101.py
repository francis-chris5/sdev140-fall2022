# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:30:25 2022

Fall 2022 Projects

@author: c.s.francis
"""


def getInputs():
    en = input("TELL ME WHO YOU ARE!!! ")
    hw = float(input("GIMME YOUR HOURS!!!! "))
    rop = float(input("HOW MUCH DO YOU MAKE!!!! "))
    return en, hw, rop 

exitprogram = False

print("Name\t | Gross Pay \t | Taxes \t\t | Net Pay")
print("--------------------------------------------")

while not exitprogram:
    # employeename = input("TELL ME WHO YOU ARE!!! ")
    # hoursworked = float(input("GIMME YOUR HOURS!!!! "))
    # rateofpay = float(input("HOW MUCH DO YOU MAKE!!!! "))
    employeename, hoursworked, rateofpay = getInputs()
    
    
    ## single line selection structure
    #grosspay = (hoursworked * rateofpay, (hoursworked-40) * rateofpay * 1.5 + 40 * rateofpay ) [hoursworked > 40]
    if hoursworked < 40:
        grosspay = hoursworked * rateofpay
    else:
        grosspay = (hoursworked-40) * rateofpay * 1.5 + 40 * rateofpay
    
    taxdeduction = grosspay * 0.15
    
    netpay = grosspay - taxdeduction
    
    
    print("Name\t | Gross Pay \t | Taxes \t\t | Net Pay")
    print("--------------------------------------------")
    print(f"{employeename} \t | {grosspay} \t\t | {taxdeduction} \t | {netpay}")
    print()
    print()

    nextuser = input("Is there somebody else? Enter \"Yes\" or \"No\": ")
    if nextuser.lower() == "no":
        exitprogam = True
    













###########################  WHITE SPACE FOR SCROLLING  ############
