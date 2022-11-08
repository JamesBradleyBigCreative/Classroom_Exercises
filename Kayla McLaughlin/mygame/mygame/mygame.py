import sys as system
import random

# Data structures
# import



class Player:
    def __init__(self,health,coins,power ):
     self.health = health
     self.coins = coins
     self.power = power

player1= Player(68, 3 ,"Iron Fist")
player2= Player(3, 4 ,"Invisibility")
isPlaying = False
listof_players = [player1, player2]

class Scene:
    scene1 = "You have discovered a Cave!" #find 1 gold coins.
    scene2 = "You found an Apple Tree!" # can buy apples (for health). ("ur health is...") 
    scene3 = "You have discovered a Cave!"
    scene4 = "oh no! While walking down the hill, you tripped and lost 3 gold coins in the grass. (and some health too...) "



play = input("Press P to play! q to quit: ")

if play == "p" or play=="P":
    print("GREAT!!")
elif play == "q" or "Q":
    system.exit()

def QUIT():
    play = input("are you sure you want to quit? y / n: ")

    if play == "n" or play=="N":
        print("GREAT!!")
    elif play == "y" or "Y":
        system.exit()


 


PLAYER = None
p_input = input("choose your player! player 1 or player 2:  ")

if p_input == "1" :
    print(player1.health, player1.coins, player1.power)
    PLAYER = player1
    isPlaying = True
elif p_input == "2":
    print(player2.health, player2.coins, player2.power )
    PLAYER = player2
    isPlaying = True



while isPlaying == True:
    if PLAYER.health<1:
        QUIT()

    randomNumber = random.randint(1,10)
    if randomNumber == 1 :
        print( Scene.scene1 )
        PLAYER.coins += 2
        print( "You have found 2 GOLD COINS! coins = ", PLAYER.coins )

    if randomNumber == 2:
        print(Scene.scene2)
        PLAYER.health += 10
        print ("health has improved! Health = ", PLAYER.health)

    if randomNumber == 3:
        print(Scene.scene3)
        PLAYER.coins += 10
        print("jackpot! You found 10 GOLD COINS! Coins = ", PLAYER.coins)

    if randomNumber == 4:
        print(Scene.scene4)
        PLAYER.coins -= 3
        PLAYER.health -= 2
        print("coins = ", PLAYER.coins , "health = ", PLAYER.health)
        
    if randomNumber == 7:
        print("you were attacked by spiders!")
        PLAYER.health -= 4
        print ("Your health has decreased. Health = ", PLAYER.health) 
        

    print("exploring...")
    userInput = input("press enter to continue! ")


    if userInput == "q":
        QUIT(isPlaying)
        

   
        
        






