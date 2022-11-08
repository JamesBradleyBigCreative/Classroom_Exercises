import module1 as mod
import random as rand
import sys as system
import module2 as mod2


avatar = mod.Player("Avatar",100,0,20,20,{})

def Main():
    global isplaying
    isplaying = True
    while avatar.health > 0 and isplaying == True:
        print("Do you wish to play")
        x = input("'S' to Start| 'Q' to Quit\n")
        if x == "Q" or x == "q":
            print("Quitting.........")
            isplaying = False
        elif x == "S" or x == "s":
            Explore = mod2.Explore(isplaying)
        else:
            print("Error Wrong Input")

    if avatar.health == 0 or avatar.health < 0:
        print("YOU DIED")
        quit()
    elif isplaying == False:
        print("Quitting.........")
        quit()

Main()