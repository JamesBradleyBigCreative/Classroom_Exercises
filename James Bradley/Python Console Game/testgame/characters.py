# IMPORTS
#----------------------------------------------------------------------------#
# Imports the "randint" function from the "random" library
from random import randint


# CLASSES
#----------------------------------------------------------------------------#

class Player():
    # Asks use to name their character, and assigns random stats
    def generate(self):
        self.name = input("Please enter a name for your character: \n")
        self.health = randint(80, 100)
        self.attack = randint(80, 100)
        self.defence = randint(80, 100)
        self.luck = randint(50, 100)
        self.score = 0


class Goblin():
    # Assigns name, and random stats
    def generate(self):
        self.name = "Goblin"
        self.health = randint(80, 100)
        self.attack = randint(80, 100)
        self.defence = randint(80, 100)

    # Function to increase the players score when this enemy dies
    def on_death():
        player.score += 1000


# VARIABLES
#----------------------------------------------------------------------------#
enemy_list = []
player = Player()


# FUNCTIONS
#----------------------------------------------------------------------------#

def create_player():
# Creates a new character based on the "Player" class we created, generates
# it's stats, then displayes them to the user
    player.generate()
    print_stats(player)

    # Asks user to confirm they are happy with the rolled stats, and allows
    # them to re-roll if needed
    confirmation = "NO"
    while confirmation == "NO":
        confirmation = input(
            "Are you happy with these stats? (YES / NO): ").upper()

        if confirmation == "NO":
            player.generate()
            print_stats(player)
        else:
            confirmation == "YES"
    print()


def generate_enemy_list():
# Asks the user how many enemies they wish to generate, then populates a list
# with the chosen number
    number_of_enemies = 0
    number_of_enemies = int(input(
        "How many enemies would you like to create: "))

    for i in range(number_of_enemies):
        enemy_list.append(Goblin())
        enemy_list[i].generate()

    # Prints the stats for each newly created enemy (to prove that the
    # generation has been successful)
    #for j in range(len(enemy_list)):
    #    print_stats(enemy_list[j])

    print()

def print_stats(character):
    # Prints the generated stats for the chosen character/enemy
    print()
    print("Name: " + character.name)
    print("Health: " + str(character.health))
    print("Attack: " + str(character.attack))
    print("Defence: " + str(character.defence))
    #print(vars(character))
    print()
