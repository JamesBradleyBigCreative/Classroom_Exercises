from characters import * 


enemy_list = []

class Player():
    def __init__(self):
        self.name = input("please enter a name: \n")
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(60,120)
        self.defence = randint(80,100)
        #creating multiple names of characters with diffrent heath stats

class Goblin():
        #ask the suer to name their character, and assign random stats  

    def  __init__(self):
        self.name = "Goblin"
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(60,120)
        self.defence = randint(80,100)

class Hobgoblin(Goblin):
    #ask the suer to name their character and assign random stats
    #this Hobgoblins stats are all increased comparted to the other character
    def __init__(self):
        Goblin.__init__(self)
        self.name = "Hobgoblin"
        self.health = self.health * 1.25
        self.attack = self.attack * 1.50
        self.defence = self.defence * 1.50



player_1 = Player()
enemy_1 = Hobgoblin()


def generate_enemy_list():
    number_of_enemys = 0
    number_of_enemys = int(input("How many enemies do you want to create: \n"))
    for i in range(number_of_enemys):
        enemy_list.append(Goblin())

# here is where the option of making more enemys is
print(vars(player_1))
print(vars(enemy_1))

generate_enemy_list()
#remember to call the goblins after
for j in range(len(enemy_list)):
    print(vars(enemy_list[j]))