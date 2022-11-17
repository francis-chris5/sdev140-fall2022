# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:30:25 2022

Fall 2022 Projects

@author: c.s.francis
"""

import datetime

def writeSequentialFile():
    with open("employesSequential.txt", "a") as toFile:
        more = input("is there another employee to enter data for? (yes/no) ")
        while more.lower() == "yes":
            name = input("TELL ME WHO IT IS THEN!!! ")
            rateOfPay = input("HOW MUCH DO THEY MAKE!!!! ")
            toFile.write(name + "\n")
            toFile.write(rateOfPay + "\n")
            more = input("is there another employee to enter data for? (yes/no) ")
            

def readSequentialFile():
    employeeData = []
    with open("employesSequential.txt", "r") as fromFile:
        for line in fromFile.readlines():
            employeeData.append(line[:-1])
    return employeeData

def getHours(name):
    hw = float(input(f"GIMME {name}'s HOURS!!!! "))
    return hw


def calculatePay(hoursworked, rateofpay):
    if hoursworked < 40:
        grosspay = hoursworked * rateofpay
    else:
        grosspay = (hoursworked-40) * rateofpay * 1.5 + 40 * rateofpay
    
    taxdeduction = grosspay * 0.15
    
    netpay = grosspay - taxdeduction
    
    return grosspay, taxdeduction, netpay

#nextuser = "yes"

def writePayStub():
    timestamp = datetime.date.today()
    employeeData = readSequentialFile()
    payStubPrinter = open("weeklypay.txt", "a")
    payStubPrinter.write("\n\n\n\n--------------------------------------------\n")
    payStubPrinter.write(str(timestamp) + "\n")
    payStubPrinter.write("Name\t\t\t\t | Gross Pay \t | Taxes \t | Net Pay\n")
    payStubPrinter.write("--------------------------------------------\n")
    
    for index in range(0, len(employeeData), 2):
        grosspay, taxdeduction, netpay = calculatePay(getHours(employeeData[index]), float(employeeData[index+1]))
        payStubPrinter.write(employeeData[index] + " \t\t\t\t | " + format(grosspay, ".2f") + " \t\t | " + format(taxdeduction, ".2f") + " \t | " + format(netpay, ".2f") + "\n\n\n")
    payStubPrinter.close()




if __name__ == "__main__":
    choice = int(input("""WHAT DO YOU WANT DO?
         --input 1 to add data to the database
         --input 2 to run weekly payroll
         --input 3 to exit
"""))
    if choice == 1:
        writeSequentialFile()
    elif choice == 2:
        writePayStub()
    else:
        pass
    










###########################  WHITE SPACE FOR SCROLLING  ############
