from random import randint


class Player():
    # Asks the user to name their character, and assigns random stats
    def __init__(self):

        self.name = input("Enter your name: ")
        self.level = 1
        self.health = randint(40,80)
        self.attack = randint(80,100)
        self.defence = randint(80,100)
        while len(self.name) == 0:
            print("invalid input")
            self.name = input("Please Enter your name:")

class Goblin():
    def __init__(self):
        self.name = "Goblin"
        self.level = randint(1,3)
        self.health = randint(10,45)
        self.attack = randint(20,55)
        self.defence = randint(20,55)

class Hobgoblin(Goblin): 
    #inheritance - takes (inherits) attributes from another class. 
    #e.g: hobgoblin takes attributes from goblin but edits them for itself.
    def __init__(self):
       Goblin.__init__(self)
       self.name = "Hobgoblin"
       self.health = self.health * 1.25




