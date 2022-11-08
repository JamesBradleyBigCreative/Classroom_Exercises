from characters import *

enemy_list = []
player_1 = player()
#player_2 = player()
#player_3 = player()

## prints all the stats that player_1 inputs. 
### (prints the variables that player_1 inputs)
print(vars(player_1))    
#print(vars(player_2))
#print(vars(player_3))


goblin_1 = goblin()
#goblin_2 = goblin()
#goblin_3 = goblin()


print(vars(goblin_1))
#print(vars(goblin_2))
#print(vars(goblin_3))


hobgoblin_1 = hobgoblin()
#hobgoblin_2 = hobgoblin()
#hobgoblin_3 = hobgoblin()

print(vars(hobgoblin_1))
#print(vars(hobgoblin_2))
#print(vars(hobgoblin_3))

generate_enemy_list()
