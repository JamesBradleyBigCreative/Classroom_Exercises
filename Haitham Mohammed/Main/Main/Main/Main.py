
from characters import *

def generate_goblin_list():
    num_of_enemies = 0
    num_of_enemies = int(input(
        "Enter how many goblins you would like to battle: "))
     
    for i in range(num_of_enemies):
        goblin_list.append(Goblin())
    for j in range(len(goblin_list)):
        # checks len of list (matching the inputed value)
        print(vars(goblin_list[j]))

def generate_hobgoblin_list():
    num_of_enemies = 0
    num_of_enemies = int(input(
        "Enter how many hobgoblnis you would like to battle: "))
     
    for i in range(num_of_enemies):
        hobgoblin_list.append(Hobgoblin())
    for j in range(len(hobgoblin_list)):
        # checks len of list (matching the inputed value)
        print(vars(hobgoblin_list[j]))


if class_input == "Hunter" or class_input == "hunter":    
    player_1 = Hunter()
    print("You have chosen the Hunter Class ")
    player_1.weapon()
    print(vars(player_1))
    generate_goblin_list()
    generate_hobgoblin_list()
    story(Hobgoblin, is_win, is_lose)
   

elif class_input == "Titan" or class_input == "titan":
    player_2 = Titan()
    print("You have chosen the Titan Class ")
    player_2.weapon()
    print(vars(player_2))
    generate_goblin_list()
    generate_hobgoblin_list()
    story(Hobgoblin, is_win, is_lose)

elif class_input == "Warlock" or class_input == "warlock":
    player_3 = Warlock()
    print("You have chosen the Warlock Class ")
    player_3.weapon()
    print(vars(player_3))
    generate_goblin_list()
    generate_hobgoblin_list()
    story(Hobgoblin, is_win, is_lose)
 
else:
    print("You obviously did not get sent to school, learn how to spell and try again! ")
    class_input = input("Choose a player class\n Hunter\n Titan\n Warlock\n:")







