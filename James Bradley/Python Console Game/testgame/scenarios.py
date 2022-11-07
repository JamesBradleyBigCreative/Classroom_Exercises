# IMPORTS
#----------------------------------------------------------------------------#
# Imports the characters module we created
from characters import *


# VARIABLES
#----------------------------------------------------------------------------#
selection = "NILL"


# FUNCTIONS
#----------------------------------------------------------------------------#
def game_start():
    # Chooses which enemy you will face
    selected_enemy = randint(0, len(enemy_list))

    # Function to begin the game scenario
    print(player.name + "... this is where your story begins... \n")
    print("You wake up in a dark, damp room...  it appears to be a cell of "
          + "some kind...")
    print("From the corner of the room you hear a high pitched jabbering...")
    print("Without warning, a " + enemy_list[selected_enemy].name
          + " jumps out and attacks!")
    battle_start(enemy_list[selected_enemy])

def battle_start(enemy):
    # Function to initiate a battle sequence
    while player.health >= 0 & enemy.health >= 0:

        # Prints the current stats of the combatants at the start of each round
        print_stats(player)
        print_stats(enemy)

        # Asks the user to choose what they want to do
        selection = input("How do you wish to proceed?  (ATTACK or RUN AWAY):"
                  + "\n").upper()

        if selection == "ATTACK":
            print("You prepare to attack the " + enemy.name)
        elif selection == "RUN AWAY":
            print("You attempt to run away...")
        else:
            print()
