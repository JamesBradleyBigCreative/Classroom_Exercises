from characters import *

enemy_list = []

def generate_enemy_list():
    # Asks user for amount of enemies to generate.
    number_of_enemies = 0
    number_of_enemies = int(input(
        "how many enemies would you like to create? : "))

    for i in range(number_of_enemies):
        enemy_list.append(Goblin())

    for j in range(len(enemy_list)):
        print(vars(enemy_list[j]))

player_1 = Player()
enemy_1 = Hobgoblin()
#player_2 = Player()
#player_3 = Player()



print(vars(player_1))
#print(vars(enemy_1))



generate_enemy_list()

#checks the length of the list(which should match the number of enemies 
# chosen) then prints the attributes of each object storede in the list.


#print(vars(player_2))
#print(vars(player_3))

