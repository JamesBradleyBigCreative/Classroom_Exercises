#LIBRARIES
from msilib.schema import Font
import random
import time
import tkinter as tk
from tkinter import font
from turtle import width




# CHARACTER INFO
name = None
rank = None
weapon = {
    1:"ak47",
    2:"scar",
    3:"longrangerifle",
    4:"sniper",
    5:"pistol"}
enemy = "russian"
kills = 0# METHODS/FUNCTION DEFINITIONS

def Chapter_1():
    print(name, " Ran through the forest to find a weapon . \n")
    print(name, " is ", rank, " and is part of the modern military forces" "\n")
    print(name, " has found a weapon in the forest ", weapon, ". \n")
    

def Chapter_2():
    higher = True
    print(name,"encountered a ",enemy, "\n")
    if rank == "luitenant":
        print("rank is higher than rusaian" "\n")
        higher = True
    elif rank == "soldier":
        print("rank is lower than russian" "\n")
        higher = False
    elif rank == "general":
        print("rank is higher than russian" "\n")
        higher = True
    elif rank == "commander":
        print("rank is lower than russain" "\n")
        higher = False
    else:
        higher = None
    if higher == True:
        print(name,"shot down the russian" "\n")
        kills = 1
    else:
        print("you died" "\n")
        exit()
    if kills == 1:
        print("you have won againts the enemy" "\n")
        win = tk.Tk()
        win.title("you won")
        win.geometry('600x400+50+50')
        win.configure(bg="black")
        photo = tk.PhotoImage()
        label = tk.Label(win,text = "you won",bg="white",fg = "black",font="times").pack(pady=150)
        
        
        
        
        


        win.mainloop()
    else:
        print("you have lost""/n")

# MAIN
name = str(input('Enter name: '))
rank = str(input("what rank are you? : luitenant,soldier,general,commander : "))
weapon = weapon[random.randint(1,5)]


input('PRESS ENTER TO CONTINUE...')

Chapter_1()
Chapter_2()
