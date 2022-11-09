from tkinter import *   
  
  
top = Tk()  
  
top.geometry("200x100")  
  
def fun():  
  tkinter.messagebox.showinfo("Hello","Red Button clicked")

b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)    
  
  
b1.pack(side = LEFT)

top.mainloop()  