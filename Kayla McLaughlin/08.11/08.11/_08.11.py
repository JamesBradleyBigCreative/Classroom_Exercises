from gamefunctions import *
from characters import *
import random

isPlaying = False
enemy_list = []


print("Welcome to My text adventure game, " , player_1.name, "!" )
play = input("Enter P to play or Q to quit! : ")
   
if play == "P" or play == "p":
   print("Great! Let's Play!")
   isPlaying = True
elif play == "Q" or play == "q":  
    quit_game()



       


def generate_enemy_list():
    number_of_enemies = 0
    number_of_enemies = randint(1,5)
    print("OH NO! ", number_of_enemies ,"Goblins have appeared and are ready to fight!")
    
    for i in range(number_of_enemies):
        enemy_list.append(Goblin())

    for j in range(len(enemy_list)):
        print(vars(enemy_list[j]))
        



print(vars(player_1))


while isPlaying == True and player_1.health > 1 :
    print("exploring...")
    userinput = input("[press enter to continue exploring.]")
    random_number = random.randint(1,6)
    if random_number == 1 or random_number == 3:
        print(scene.scene1)
        print("There is a goblin lurking here.\n", (vars(enemy_1)))
        attack = input("would you like to attack? Y / N : ")
        if attack == "Y" or attack == "y" :
           fight_scene()
        elif attack == "n" or attack == "N":
            print("you ran away! but you tripped:( .. your health is now", player_1.health - 17)
        elif attack != "y" or attack != "Y" or attack != "n" or "N":
            print("Invalid answer!")
            attack = input("would you like to attack? Y / N : ")



    if random_number == 2 :
            print(scene.scene2)
            print("you found an apple tree! Eat an apple to get your health up!")
            print("your health is now ", player_1.health + 5 )
    if player_1.health < 1:
        print("game over.")
        quit()

