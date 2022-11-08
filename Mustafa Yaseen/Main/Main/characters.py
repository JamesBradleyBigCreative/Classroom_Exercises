from random import randint 
enemy_list = [] 
class Player():
    def __init__(self):
        self.name = str(input("Enter a name: \n"))
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(80,140)
        self.defense = randint(60,100)
        #ask the user for their name and the stats are randomly generated


class Goblin():
    def __init__(self):
        self.name = "Goblin"
        self.level = 1
        self.health = randint(40,60)
        self.attack = randint(30,50)
        self.defense = randint(30,50)

class Hobgoblin(Goblin):
    def __init__(self):
        Goblin.__init__(self)
        self.name = "Hobgoblin"
        self.health = (self.health * 1.5)
        self.attack = (self.attack * 1.5)
        self.defense = (self.defense * 1.5)
#hobgoblin takes the attributes from the parent class then a person is able to
#edit it for their own use

