import random as ran
loop = True
List1 = []



def Name():
    exit = False
    LoopNum = 0
    global Item
    num = None

    while exit == False:
        while LoopNum == 1:
            print("You can type 'done' at any point to finish inputing items or 'quit' to exit the program altogether!")
            LoopNum += 1
        Item = str(input("Enter item: "))
        List1.append(Item)
        if Item == "done":
            List1.remove("done")
        elif Item == "Done":
            List1.remove("Done")
        elif Item == "Quit" or Item == "quit":
            quit()
        LoopNum += 1
        if Item == "Done" or Item == "done":
            #y = (ran.choice(List1))
            num = List1[ran.randint(0, (len(List1)-1))]
            for x in List1:
                print(x)            
            print(f"{num} was your result")
            exit = True
    Again(num)
        
def Again(y):
    while loop == True:
        global repeat
        global Removal
        repeat = str(input("Do you wish to re-roll with or without removing a name? (with/without) \nYou can also choose to 'add' more items to your current list"))
        if repeat == "With" or repeat == "with":
            y = (ran.choice(List1))
            print(f"{y} was your result")
        elif repeat == "Without" or repeat == "without":
            Removal = input("Enter the item you wish to remove: ")
            List1.remove(Removal)
            print(List1)
            print(f"{y} was your result")
        elif repeat == "add" or repeat == "Add":
            Name()            
        elif repeat == "quit" or repeat == "Quit":
            quit()
    

Name()   
