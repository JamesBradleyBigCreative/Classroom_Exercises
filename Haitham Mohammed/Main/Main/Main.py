from characters import *
p1 = Player()
e1 = Hobgoblin()
e2 = Goblin()
print(vars(p1))
print(vars(e1))
print(vars(e2))

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