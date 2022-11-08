from random import randint

enemy_list = []

class Player():
 # This is the info needed for the player and assings random stats
    def __init__(self):
        self.name = str(input("Please enter a name: \n"))
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(80,100)       
        self.defence = randint(80,100)  
    
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





