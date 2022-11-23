
from random import randint

enemy_list = []
team_list = {}

class Player():
 # This is the info needed for the player and assings random stats
    def __init__(self):
        self.name = str(input("Please enter a name: \n"))
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(80,100)       
        self.defence = randint(80,100)  

class TeamMate1():
    # This team mate will help more and will give extra support
     def __init__(self):
        self.name = "TeamMate1"
        self.level = 1
        self.health = randint(60,80)
        self.attack = randint(40,60)
        self.defence = randint(60,80)     
        
class DefenceTeam():
    # This character is for defence and to help 
    def __init__(self):
        self.name = "DefenceTeam"
        self.level = 1
        self.health = randint(80,100)
        self.defence = randint (80,100)

class AttackTeam():
    # This is to help the team attack against the enemy
    def __init__(self):
        self.name = "AttackTeam"
        self.level = 1 
        self.health  = randint(80,100)
        self.attack = randint(80,100)


# The "self." + "randint(,) - gives each character a stat randomly

# Print player 1's entered name

#print(player_1.name)
#print(player_1.level)
#print(player_1.health)

class Goblin():
 # This is the info needed for the player, assigns random stats for the enemy
    def __init__(self):
        self.name = "Goblin"
        self.level = 1
        self.health = randint(40,60)
        self.attack = randint(30,50)       
        self.defence = randint(30,50) 


class Hobgoblin(Goblin):
 # This makes Hobgoblin have the same attributes as Goblin
 # Edits them for it's own use
    def __init__(self):
        Goblin.__init__(self)
        self.name = "Hobgoblin"
        self.health = self.health * 1.25
