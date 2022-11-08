import module1 as game
import sys as system
import random as rand

health = 100
volatility = 10
is_playing = True

def menu():
    global is_playing
    choice =  input("do you want to play. Type Y for yes    Type N for no")
    if choice == "Y" or choice == "y":
        is_playing = True
    elif choice == "N" or choice == "n":
        is_playing = False
    else:
        is_playing = True

def new_func():
    is_playing = True
menu()

PLAYER = game.player(game.batman.coins, game.batman.health, game.batman.coins)

while is_playing == True:
    number = rand.randint(1,5)

    
    if health > 1:
         
        print("exploring...")
        print("\n")
        option = input("Press Enter:")
        if option == "q" or option == "Q":
            menu()    
        
        if number == 1:
            print(game.scene.scene_1)
            game.batman.coins += 1
            print("coins: ", game.batman.coins)
            print("\n")
        
        elif number == 2:
            print(game.scene.scene_2)
            game.batman.health -= 10
            print("health: ", game.batman.health)
            print("\n")
        
        elif number == 3:
            print(game.scene.scene_3)
            game.batman.health += 10
            print("health: ", game.batman.health)
            print("\n")
        
        elif number == 4:
            print(game.scene.scene_4)
            game.batman.coins -=1
            print("coins: ", game.batman.coins)
            print("\n")
    else:
        is_playing = False
