
import random as rand
import module1 as mod

P = input("To play type P to exit type E: ").lower()
#Simple menu
if P == "p":
   ""
elif P == "e":
  exit()



def char_sel():
    #defining global variables to store character details
    global inf
    global ch
    global selected
    global name_1
    global ultimate_1
    global rank_1
    global abilities_1
    global health_1
    ch = ""
    #boolean
    selected = False
    #printing through list

    characters = ["kakashi","naruto","sasuke"]
    print("\n")
    for i in characters:
        print(f"{i} \n")
    #while loop for selection of character
    while selected == False:
        ch = input("please enter a character:  ")
        print("\n")
        inf = input("do you want to learn your characters stats y/n : ")
        print("\n")
        if inf == "y":
            if ch == "kakashi":
               print(mod.kakashi.stats())
               selected = True
            elif ch == "naruto":
                print(mod.naruto.stats())
                selected = True
            elif ch == "sasuke":
                print(mod.sasuke.stats())
                selected = True
            else:
                print("invalid character \n")
        elif inf == "n":
            selected = True
        #storing character details from module one in variables
    if ch == "kakashi":
       name_1 = mod.kakashi.name
       ultimate_1 = mod.kakashi.ultimate
       abilities_1 = mod.kakashi.abilities
       health_1 = mod.kakashi.health       
    elif ch == "naruto":
      name_1 = mod.naruto.name
      ultimate_1 = mod.naruto.ultimate
      abilities_1 = mod.naruto.abilities
      health_1 = mod.naruto.health
    elif ch == "sasuke":
      name_1 = mod.sasuke.name
      ultimate_1 = mod.sasuke.ultimate
      abilities_1 = mod.sasuke.abilities
      health_1 = mod.sasuke.health



     
               
       



char_sel()
#random desision of levels
l = rand.randint(1,2)
lost = True
continue_1 = ""
continute_2 = ""

if l == 1:
    continue_1 = input("do you want to continue to level 1 y/n : ")
    print("\n")
elif l ==2 :
    continue_2 = input("do you want to continute to level 2 y/n: ")
if continue_1 == "y":
    while lost != False:
        if l == 1:
            mod.level1.villain(mod.level1(name_1,abilities_1,health_1,ultimate_1))
            lost = False
elif continue_1 == "n":
    exit()
elif continue_2 == "y":
    while lost != False:
        if l == 2:
           mod.level2.villain(mod.level2(name_1,abilities_1,health_1,ultimate_1))
           lost = False
elif continue_2 == "n":
    exit()

else:
    exit()
ex = input("do you want to exit>> y/n :")
if ex == "y":
    exit()
else: 
    if l == 1:
        print("STARTING LEVEL 2 -----------------------")
        print("\n")
        print("\n")
        mod.level2.villain(mod.level2(name_1,abilities_1,health_1,ultimate_1))
    elif l == 2:
        print("STARTING LEVEL 1 -----------------------")
        print("\n")
        print("\n")
        mod.level1.villain(mod.level1(name_1,abilities_1,health_1,ultimate_1))
    else:
        exit()


print("\n")
print(" CONGRATULATIONS YOU COMPLETED THE GAME!!!!")
print("\n")
            

    

        

