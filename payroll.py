# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:30:25 2022

Fall 2022 Projects

@author: c.s.francis
"""

employeename = input("TELL ME WHO YOU ARE!!! ")
hoursworked = float(input("GIMME YOUR HOURS!!!! "))
rateofpay = float(input("HOW MUCH DO YOU MAKE!!!! "))


## single line selection structure
grosspay = (hoursworked * rateofpay, (hoursworked-40) * rateofpay * 1.5 + 40 * rateofpay ) [hoursworked > 40]

taxdeduction = grosspay * 0.15

netpay = grosspay - taxdeduction


print("Name\t | Gross Pay \t | Taxes \t\t | Net Pay")
print("")
print(f"{employeename} \t | {grosspay} \t\t | {taxdeduction} \t | {netpay}")

















###########################  WHITE SPACE FOR SCROLLING  ############
