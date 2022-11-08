from CHARACTERS import *



player_1 = Player()  
enemy_1 = Hobgoblin()

def generate_enemy_list():
    # Asks user for the number of enemies to generate, then populates the list  
    # with the required number. 
    number_of_enemies = 0 
    number_of_enemies = int(input(
        "how many enemies would you like to create: \n"))

    
    for i in range(number_of_enemies):
        enemy_list.append(Goblin())



generate_enemy_list()
print(vars(player_1))
print(vars(enemy_1))

for j in range(len(enemy_list)):
    # Checks the length of the list (which should match the number of
    # enemies chosen) then prints the attributes of each object stored in the list
    print(vars(enemy_list[j]))


