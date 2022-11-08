from random import randint


class Player():
    
    def __init__(self): # Constructer, Self allows you to access the
        #  attributes of that instance of the class
        self.name = input("Enter A NPC Name: ")
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(30,60)
        self.defense = randint(20,70)


class Goblin():
    
    def __init__(self):
        self.name = "Goblin"
        self.level = 5
        self.health = randint(40,60)
        self.attack = randint(20,30)
        self.defense = randint(10,40)


class Hobgoblin(Goblin): # Inheritance: by putting a class as a parameter of
   # another class, the Second class inherits all the attributes of the first
   # class which can be reassigned
    
    def __init__(self):
        super().__init__() # Note: The child's __init__() function overrides
       # the inheritance of the parent's __init__() function.
       # To keep the inheritance of the parent's __init__() function,
       # add a call to the parent's __init__() function:
       # Eg: Goblin.__init__(self) or super().__init__()
        self.name = "Hobgoblin"
        self.health = (self.health*1.25)


