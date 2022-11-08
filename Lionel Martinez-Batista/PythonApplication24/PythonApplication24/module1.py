from random import randint

enemy_list = []
class Player():
    def __init__(self):
        # Asks the user the names of the character and randomly assigns stats
        self.name = input("Enter a Character name: ")
        self.attack = randint(30, 60)
        self.defence = randint(20, 70)
        self.level = 1
        self.health = randint(60, 120)

class Goblin():
    def __init__(self):
        self.name = "Goblin"
        self.attack = randint(30, 60)
        self.defence = randint(20, 50)
        self.level = 1
        self.health = randint(40, 60)

class HobGoblin(Goblin):
    # Hobgoblin takes the attributes from the parent class (Goblin)
    # Then edits them for its own use
    def __init__(self):
        Goblin.__init__(self)
        self.name = "HobGoblin"
        self.health = (self.health * 1.25)
        self.attack = (self.attack * 1.3)
        self.defence = (self.defence * 1.5)

def generate_enemy_list():
    number_of_enemies = 0
    number_of_enemies = int(input(
        "How many enemies would you like to create: \n"))
    for i in range(number_of_enemies):
        enemy_list.append(Goblin())

