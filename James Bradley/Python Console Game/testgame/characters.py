# IMPORTS
#----------------------------------------------------------------------------#
# Imports the "randint" function from the "random" library
from random import randint


# CLASSES
#----------------------------------------------------------------------------#
# Creates a default template for in game characters
class Default:
    def __init__(self):
        self.health = 0
        self.attack = 0
        self.defence = 0


# Assigns stats to the player object, asks user for a name and inherits stats
# from default
class Player(Default):
    def generate(self):
        self.name = input("Please enter a name for your character: \n")
        self.health = randint(80, 100)
        self.attack = randint(80, 100)
        self.defence = randint(80, 100)


# Assigns stats to the Goblin object, assigns name and inherits stats from
# default
class Goblin(Default):
    def generate(self):
        self.name = "Goblin"
        self.health = randint(80, 100)
        self.attack = randint(80, 100)
        self.defence = randint(80, 100)


# FUNCTIONS
#----------------------------------------------------------------------------#
# Prints the generated stats for the chosen character/enemy
def print_stats(character):
    print()
    print("Name: " + character.name)
    print("Health: " + str(character.health))
    print("Attack: " + str(character.attack))
    print("Defence: " + str(character.defence))
    #print(vars(character))
    print()
