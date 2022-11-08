
from random import randint

enemy_list = []
skl = ["Andreas", "Arnab", "Aviol", "Evan", "Haitham","James", "Kayla",  "Lionel", "Leslie", "Martina", "Mustafa", "Roni"]
class Player:
    def __init__(self):
        self.Name = str(input("Enter a name: \n"))
        # asks usr to name character
        self.Level = 1
        self.Attack = randint(80,100)
        self.Health = randint(60,120)
        self.Defence = randint(80,100)


class Goblin:
    def __init__(self):
        self.Name = "Goblin"
        self.Level = 1
        self.Attack = randint(40,60)
        self.Health = randint(10,60)
        self.Defence = randint(30,50)
# Hobgoblin takes attributes from its parent's class then edits them for its 
# wn use 
class Hobgoblin(Goblin):
    def __init__(self):
        Goblin.__init__(self)
        self.Name = "Hobgoblin"
        self.Health = (self.Health * 1.25)
        self.Attack = (self.Attack * 1.25)
        self.Defence = (self.Defence * 1.25)
