import random as ran
import tkinter 
def Program():
    global x
    global y
    global list1
    list1 = []
    list2 = []
    exit = False
    LoopNum = 0
    while exit == False:
        while LoopNum == 1:
            print("You can type 'done' at any point to finish inputing items or type 'Quit' to stop the program altogether!")
            LoopNum += 1
        Item = str(input("Enter item: "))
        list1.append(Item)
        if Item == "done":
            list1.remove("done")
        elif Item == "Done":
            list1.remove("Done")
        elif Item == "Quit" or Item == "quit":
            quit()
        LoopNum += 1
        if Item == "Done" or Item == "done":
            for x in list1:
                print(x)
            exit = True
            list2.append(ran.choice(list1))
            print(f"{list2} has been chosen")
            list2.clear()
Program()

def Repeat():
    global inp

    Loop = True 
    while Loop == True:
        global repeat
        global Removal
        repeat = str(input("Do you wish to re-roll removing (R) or not removing (NR) a name? (with/without) \nYou can also choose to 'add' more items to your current list: "))
        if repeat == "R" or repeat == "r":
            y = (ran.choice(list1))
            print(f"{y} was your result")
        elif repeat == "NR" or repeat == "nr":
            Removal = input("Enter the item you wish to remove: ")
            list1.remove(Removal)
            for x in list1:
                print(x)
            y = (ran.choice(list1))
            print(f"{y} was your result")
        elif repeat == "add" or repeat == "Add":
           Program()
        elif repeat == "quit" or repeat == "Quit":
            quit()
Repeat()
