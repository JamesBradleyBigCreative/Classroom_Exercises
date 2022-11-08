from random import randint
from Characters import *

enemy_list = []

def GenerateEnemyList():
    number_of_enemies = 0
    print("Amount of enemies cant exceed 50 and be 0 or below")

    try:
        # Asking user for number of enemies to generate
        number_of_enemies = int(input(
            "Enter the amount of enemies you want to fight: "))
    except:
        print("Error Invalid Input")
        return None
    # Error Handling if the user doesnt input an integer

    if number_of_enemies <= 50 and number_of_enemies > 0:
        for i in range(number_of_enemies): # Populates the enemy list with how
           #many goblins are specified
            enemy_list.append(Goblin())
    else:
        print("Error Invalid Number of Enemies")
        return None

#player_1 = Player()
#enemy_1 = Hobgoblin()
#player_2 = Player()
#player_3 = Player()

# Vars() prints every class variable that is in a class as a dictionary

#print(vars(player_1))
#print(vars(enemy_1))

#print(vars(player_2))
#print(vars(player_3))

GenerateEnemyList()
for j in range(len(enemy_list)):
    # Checks the length of the list and then prints the attributes of each
    # object in the list
    print(vars(enemy_list[j]))