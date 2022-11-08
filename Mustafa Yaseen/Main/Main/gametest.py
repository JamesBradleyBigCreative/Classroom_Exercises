from characters import *

player_1 = Player()
enemy_1 = Hobgoblin()
enemy_2 = Goblin()
def generate_enemy_list():
    number_of_enemies = 0
    number_of_enemies = int(input(
        "how many enemies would you like to create: "))
    for i in range(number_of_enemies):
        enemy_list.append(Goblin())

generate_enemy_list()
print(vars(player_1))
print(vars(enemy_1))
print(vars(enemy_2))

for j in range(len(enemy_list)):
    #Check the length of the list (matching) however many enemies are chosen
    #Then prints the attributes of each object stored in the list
    print(vars(enemy_list[j]))