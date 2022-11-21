<<<<<<< HEAD
from characters import *

def generate_goblin_list():
    num_of_enemies = 0
    num_of_enemies = int(input(
        "Enter how many goblins you would like to battle: "))
     
    for i in range(num_of_enemies):
        goblin_list.append(Goblin())

def generate_hobgoblin_list():
    num_of_enemies = 0
    num_of_enemies = int(input(
        "Enter how many hobgoblins you would like to battle: "))
     
    for i in range(num_of_enemies):
        hobgoblin_list.append(Hobgoblin())

class_input = str(input("Choose a player class\n Hunter\n Titan\n Warlock\n : "))
if class_input == "Hunter" or class_input == "hunter":    
    player_1 = Hunter()
    print("You have chosen the Hunter Class ")
    player_1.weapon()
    print(vars(player_1))
    generate_goblin_list()
    for j in range(len(goblin_list)):
        # checks len of list (matching the inputed value)
        print(vars(goblin_list[j]))
    generate_hobgoblin_list()
    story(Hobgoblin)

elif class_input == "Titan" or class_input == "titan":
    player_1 = Titan()
    print("You have chosen the Titan Class ")
    player_1.weapon()
    print(vars(player_1))
    generate_goblin_list()
    for j in range(len(goblin_list)):
        # checks len of list (matching the inputed value)
        print(vars(goblin_list[j]))
    generate_hobgoblin_list()
    for j in range(len(hobgoblin_list)):
        # checks len of list (matching the inputed value)
        print(vars(hobgoblin_list[j]))
    story(Hobgoblin)
elif class_input == "Warlock" or class_input == "warlock":
    player_1 = Warlock()
    print("You have chosen the Warlock Class ")
    player_1.weapon()
    print(vars(player_1))
    generate_goblin_list()
    for j in range(len(goblin_list)):
        # checks len of list (matching the inputed value)
        print(vars(goblin_list[j]))
    generate_hobgoblin_list()
    for j in range(len(hobgoblin_list)):
        # checks len of list (matching the inputed value)
        print(vars(hobgoblin_list[j]))
    story(Hobgoblin)
 
else:
    print("You obviously did not get sent to school, learn how to spell and try again! ")
    class_input = input("Choose a player class\n Hunter\n Titan\n Warlock\n:")












=======
from characters import *

class_input = str(input("Choose a player class\n Hunter\n Titan\n Warlock\n : "))
if class_input == "Hunter" or class_input == "hunter":    
    player_1 = Hunter()
    player_1.weapon()
    print(vars(player_1))

elif class_input == "Titan" or class_input == "titan":
    player_1 = Titan()
    player_1.weapon()
    print(vars(player_1))
elif class_input == "Warlock" or class_input == "warlock":
    player_1 = Warlock()
    player_1.weapon()
    print(vars(player_1))
else:
    print("You obviously did not get sent to school, try again ")
    class_input = input("Choose a player class\n Hunter\n Titan\n Warlock\n:")



def generate_enemy_list():
    num_of_enemies = 0
    num_of_enemies = int(input(
        "Enter how many enemies you would like to battle: "))
     
    for i in range(num_of_enemies):
        enemy_list.append(Goblin())

generate_enemy_list()


for j in range(len(enemy_list)):
    # checks len of list (matching the inputed value)
    print(vars(enemy_list[j]))

>>>>>>> 98e7e1f627f822d717cb5a658057910330f30225
