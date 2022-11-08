
from tkinter import *

win = Tk()
win.geometry("400x300")


def England():
    label1 = Label(win, Text = "the capital city of england is London")
    label1.pack
def China():
    label2 = Label(win, Text = "the capital city of china is beijing")
    label2.pack
def America():
    label3 = Label(win, Text = "the capital city of America is Washington")
    label3.pack
def Netherlands():
    label4 = Label(win, Text = "the capital city of netherlands is amsterdam")
    label4.pack
 
but1 = Button(win, text = "england", command = England, activeforground = "blue", activebackground = "white",pady = 10, padx = 15)
but2 = Button(win, text = "england", command = China, activeforground = "blue", activebackground = "white",pady = 10, padx = 15)
but3 = Button(win, text = "england", command = America, activeforground = "blue", activebackground = "white",pady = 10, padx = 15)
but4 = Button(win, text = "england", command = Netherlands, activeforground = "blue", activebackground = "white",pady = 10, padx = 15)
win.mainloop

    
