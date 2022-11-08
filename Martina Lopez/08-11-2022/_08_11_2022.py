from characters import *

enemy_list = []

player_1 = Player()
player_2 = Player()
player_3 = Player()

print(vars(player_1))
print(vars(player_2))
print(vars(player_3))

# print(player_1.name)
# print(player_1.level)
# print(player_1.health)
# print(player_1.attack)
# print(player_1.defence)
# Es lo mismo que hacer = print(vars(player_1))

def generate_enemy_list():
    number_of_enemies = 0
    number_of_enemies = int(input(
        "How many enemies would you like to create?: "))
    for i in range(number_of_enemies):
        enemy_list.append(Goblin())
    for j in range(len(enemy_list)):
# Checks the length of the list (which should match the number of enemies
# chosen) then prints the attributes of each object stored in the list.
                              print(vars(enemy_list[j]))                 
generate_enemy_list()



