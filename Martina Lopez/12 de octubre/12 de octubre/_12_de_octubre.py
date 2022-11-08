import class_module as game
import random as rand
import sys as system

isPlaying = True

def Menu():
    global isPlaying 
    choice = input("If you WANT to play enter 'Y', if you DON'T WANT to play enter 'N' : ")
    if choice == "Y" or choice == "y":
        isPlaying = True
    elif choice == "N" or choice ==  "n":
        isPlaying = False
    else:
       isPlaying = True 
Menu()


while isPlaying == True:
    number = rand.randint(1, 7)

    if game.player.Health > 1 and game.player.Health < 20:
        print("explore")    
        input("press enter ")
        if number == 1:
            print(game.scene.scene_1)
            game.player.Coins += 1 
            print("coins: ", game.player.Coins)
            print("\n")
        elif number == 2:
            print(game.scene.scene_2)
            game.player.Health -= 1
            print("Health: ", game.player.Health)
            print("\n")
        elif number == 3:
            print(game.scene.scene_4)
            game.player.Health += 1 
            print("Health: ", game.player.Health)
            print("\n")
        elif number == 4:
            print(game.scene.scene_3)
            if game.player.Coins > 0:
               game.player.Coins -= rand.randint(1, (game.player.Coins)) 
            elif game.player.Coins < 0:
                game.player.Coins == False 
            print("Coins: ", game.player.Coins)
            print("\n")
        elif number == 5:
            print(game.scene.scene_5)
            game.player.Coins += rand.randint(1, 20)
            print("coins: ", game.player.Coins)
            print("\n")
