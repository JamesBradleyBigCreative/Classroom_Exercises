# IMPORTS
#----------------------------------------------------------------------------#
# Imports the characters module we just created
from characters import *
from scenarios import *


# GLOBAL VARIABLES
#----------------------------------------------------------------------------#
enemy_list = []


# FUNCTIONS
#----------------------------------------------------------------------------#

def create_player():
# Creates a new character based on the "Player" class we created, generates
# it's stats, then displayes them to the user
    player = Player()
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


def create_enemies():
# Asks the user how many enemies they wish to generate, then populates a list
# with the chosen number
    number_of_enemies = 0
    number_of_enemies = int(input(
        "How many enemies would you like to create: "))

    for i in range(number_of_enemies):
        enemy_list.append(Goblin())
        enemy_list[i].generate()
        #print_stats(enemy_list[i])


# MAIN CODE
#----------------------------------------------------------------------------#

create_player()
create_enemies()
level1()