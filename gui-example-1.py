# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 18:57:10 2022

Fall 2022 Projects

@author: c.s.francis
"""


import tkinter as tk


def SayHi(event):
    lblOutput["text"] = "Hello World!!!"


window = tk.Tk()
window.geometry("777x444")


btnClicker = tk.Button(window, text="Click Me")
btnClicker.bind("<Button-1>", lambda e: SayHi(e))

lblOutput = tk.Label(window, text="")


btnClicker.pack()
lblOutput.pack()






if __name__ == "__main__":
    window.mainloop()
    



























####################################