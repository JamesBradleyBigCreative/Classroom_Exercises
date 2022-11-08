from tkinter import *
from tkinter import messagebox
import random

capitals = {
    "England" : "London",
    "Japan": "Tokyo",
    "Nigeria": "Abuja",
    "Kenya": "Nairobi",
    }

def Problem_One():
    messagebox.showinfo("England",capitals["England"])

def Problem_Two():
    messagebox.showinfo("Japan",capitals["Japan"])

def Problem_Three():
    messagebox.showinfo("Nigeria",capitals["Nigeria"])

def Problem_Four():
    messagebox.showinfo("Kenya",capitals["Kenya"])


top = Tk()

top.geometry("600x600")


England = Button(top,command = Problem_One, text = "England", fg = "red")  
England.pack( side = LEFT)  
Japan = Button(top,command = Problem_Two, text = "Japan", fg = "black")  
Japan.pack( side = RIGHT )  
Nigeria = Button(top,command = Problem_Three, text = "Nigeria", fg = "blue")  
Nigeria.pack( side = TOP )  
Kenya = Button(top,command = Problem_Four, text = "Kenya", fg = "green")  
Kenya.pack( side = BOTTOM)  

top.mainloop()

