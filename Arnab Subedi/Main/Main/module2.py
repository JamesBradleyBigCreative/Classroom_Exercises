from random import randint
class character:
    #ask the user to name the character and has stored values about their characters
    def __init__(self):
        self.attacks = randint(2,120)
        self.health = randint(60,120)
        self.name = input("Enter your name: ")
        self.level = 1
        self.defence = randint(3,120)
    def information(self):
        print(f"{self.name} is level {self.level} and has {self.health} health and does {self.attacks} damage")
#stores an instance of character in the variables player_1, player_2 and player_3


class Goblin:
    def __init__(self):
        self.attacks = randint(2,120)
        self.health = randint(60,120)
        self.name = "Goblin"
        self.level = randint(1,34)
        self.defence = randint(3,120)


#Passes goblin class into hobgoblin class as a inheritance
class hobgoblin(Goblin):
    #Takes goblin from parent class and takes the attributes and uses it as its own
    #Then edits for its 
    def __init__(self):
        Goblin.__init__(self)
        self.name = "hobgoblin"
        self.health = (self.health * 1.5)


enemy_list =[]

def generate_enemy():
    #ask user for the number of enemies to generate, then populates the list
    #with the required ammount of enemies
    number_of_enemy = int(input(
        "Enter the ammount of enemies: "))

    for i in range(number_of_enemy):
        enemy_list.append(Goblin())
    for j in range(len(enemy_list)):
    #checks length of list should match user input number
        print(vars(enemy_list[j]))
    #prints each item in the list as variable
              
