from module1 import *

player_one = Player()
enemy_one = Goblin()
enemy_two = HobGoblin()

print(vars(player_one))
generate_enemy_list()
print(vars(enemy_one))
print(vars(enemy_two))
for j in range(len(enemy_list)):
    # Checks the length of the list
    # (which should match the number of enemies chosen)
    print(vars(enemy_list[j]))