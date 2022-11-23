from random import randint
from random import choices


class Player():
    
    def __init__(self): # Constructer, Self allows you to access the
        #  attributes of that instance of the class
        self.name = input("Enter Your Character Name: ")
        self.level = 1
        self.exp = 0
        self.exp_boundry = 100
        self.health = randint(60,120)
        self.attack = randint(30,60)
        self.defense = randint(20,70)
        self.coins = 50
        self.equipment_inventory = {}
        self.item_inventory = []

    def level_up(self,exp_gained):
        print(f"\nYOU GAINED {exp_gained} EXPERIENCE POINTS")
        self.exp += exp_gained
        if self.exp >= self.exp_boundry:
            self.level += 1
            print(f"\nYOU LEVELED UP TO LEVEL {self.level}!!!!")
            self.exp_boundry *= 1.2
            self.health *= 1.2
            self.attack *= 1.2
            self.defense *= 1.2
            self.exp = 0


class Goblin():
    
    def __init__(self):
        self.name = "Goblin"
        self.level = 5
        self.health = randint(40,60)
        self.attack = randint(20,30)
        self.defense = randint(10,40)
        self.coins = 30
        self.inventory = {}
        self.exp = randint(10,25)


class HobGoblin(Goblin): # Inheritance: by putting a class as a parameter of
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
        self.coins = int((self.coins*2))
        self.exp = randint(20,35)


class Slime(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Slime"
        self.health = randint(5,15)
        self.attack = randint(5,15)
        self.defense = randint(5,15)
        self.coins = 10
        self.exp = randint(5,15)


class WildDog(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Wild Dog"
        self.health = randint(40,60)
        self.attack = randint(10,35)
        self.defense = randint(10,35)
        self.coins = 30
        self.exp = randint(25,40)


class Bandit(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Bandit"
        self.health = randint(40,60)
        self.attack = randint(40,60)
        self.defense = randint(40,60)
        self.coins = 100
        self.exp = randint(30,50)


class DemonKnight(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Demon Knight"
        self.health = randint(90,120)
        self.attack = randint(90,120)
        self.defense = randint(90,120)
        self.coins = 200
        self.exp = randint(50,70)


Potion = randint(30,55)