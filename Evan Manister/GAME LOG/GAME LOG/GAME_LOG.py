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



def generate_enemy_list():
    # Asks user for the number of enemies to generate, then populates the list  
    # with the required number. 
    number_of_enemies = 0 
    number_of_enemies = int(input(
        "how many enemies would you like to create: \n"))

    
    for i in range(number_of_enemies):
        enemy_list.append(Goblin())




generate_enemy_list()
print(vars(player_1))
print(vars(team_mate))
print(vars(defence_team))
print(vars(attack_team))
print(vars(enemy_1))
print(vars(super_wizard))

player_1 = Player()  
enemy_1 = Hobgoblin()
team_mate = TeamMate1()
defence_team = DefenceTeam()
attack_team = AttackTeam()


for j in range(len(enemy_list)):
    # Checks the length of the list (which should match the number of
    # enemies chosen) then prints the attributes of each object stored in the list
    print(vars(enemy_list[j]))

from random import randint

enemy_list = []

