from random import randint

class Player():
 # Ask the suer to name their character, and assigns random stats. 
    def __init__(self):
        self.name = input("Please enter a name:  ")
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(80,100)
        self.defence = randint(80,100)
class Goblin():
    def __init__(self):
        self.name = "Goblin"
        self.level = randint(1,10)
        self.health = randint(40,60)
        self.attack = randint(30,50)
        self.defence = randint(30,50)

class Hobgoblin(Goblin):
# Inheritance - takes (inheritance) attributes from another class. Takes the 
# attributes from it's parent class (Globin) then edits them for its own use
    def __init__(self):
        Goblin.__init__(self)
        self.name = "Hobgoblin"
        self.health = self.health * 1.25
