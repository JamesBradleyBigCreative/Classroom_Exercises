from random import randint


class Player():
    # Asks the user to name their character, and assigns random stats
    def __init__(self):
        self.name = input("Enter your name: ")
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(80,100)
        self.defence = randint(80,100)

class Goblin():
    def __init__(self):
        self.name = "Goblin"
        self.level = 1
        self.health = randint(40,65)
        self.attack = randint(30,50)
        self.defence = randint(30,50)

class Hobgoblin(Goblin): 
    #inheritance - takes (inherits) attributes from another class. 
    #e.g: hobgoblin takes attributes from goblin but edits them for itself.
    def __init__(self):
       Goblin.__init__(self)
       self.name = "Hobgoblin"
       self.health = self.health * 1.25

