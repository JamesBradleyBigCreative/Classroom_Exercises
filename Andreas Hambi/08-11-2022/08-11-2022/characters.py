from random import randint

class player():
## self allows player_1 and player_2 to access the player class or blueprint    
    def __init__(self):                                 
        self.name = input("Please enter a name:  ")
        self.level = 1
        self.health = randint(75, 120)
        self.attack = randint(10, 25)
        self.defence = randint(75, 120)
        self.role = input("Please enter your character's role or origin:  ")


class goblin():
    def __init__(self):                                 
        self.name = "Lolo"
        self.level = 1
        self.health = randint(45,60)
        self.attack = randint(9,12)
        self.defence = randint(30,45)

class hobgoblin(goblin):
    ## hobgoblin takes attributes from parent class(goblin) then edits them for
    ## its own use
    def __init__(self):             
            goblin.__init__(self)
            self.name = "Lolar"
            self.level = randint(1,4)
            self.health = self.health * 1.25
            self.attack = self.attack * 1.25
            self.defence = self.defence * 1.25

def generate_enemy_list():
## asks user for the number of enemies they would like to generate, 
## then populates the list with required number
    number_of_enemies = 0
    number_of_enemies = int(input("how many enemies would you like to create:"
                                 ))
    for i in range(number_of_enemies):
        enemy_list.append(goblin())

    for j in range(len(enemy_list)):
## checks the length of the list (should match number of enemies chosen 
## and print the attributes of each object stored in the list)
        print(vars(enemy_list[j]))

