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


def calculatePay(hoursworked, rateofpay):
    if hoursworked < 40:
        grosspay = hoursworked * rateofpay
    else:
        grosspay = (hoursworked-40) * rateofpay * 1.5 + 40 * rateofpay
    
    taxdeduction = grosspay * 0.15
    
    netpay = grosspay - taxdeduction
    
    return grosspay, taxdeduction, netpay

nextuser = "yes"


payStubPrinter = open("weeklypay.txt", "w")
payStubPrinter.write("Name\t\t\t\t | Gross Pay \t | Taxes \t | Net Pay\n")
payStubPrinter.write("--------------------------------------------\n")

while nextuser.lower() == "yes":

    employeename, hoursworked, rateofpay = getInputs()
    
    
    grosspay, taxdeduction, netpay = calculatePay(hoursworked, rateofpay)
    
    
    payStubPrinter.write(employeename + " \t\t\t\t | " + format(grosspay, ".2f") + " \t\t | " + format(taxdeduction, ".2f") + " \t | " + format(netpay, ".2f") + "\n\n\n")


    nextuser = input("Is there somebody else? Enter \"Yes\" or \"No\": ")

    
payStubPrinter.close()













###########################  WHITE SPACE FOR SCROLLING  ############
