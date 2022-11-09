from random import randint
from random import choices


class Player():
    
    def __init__(self): # Constructer, Self allows you to access the
        #  attributes of that instance of the class
        self.name = input("Enter Your Character Name: ")
        self.level = 1
        self.health = randint(60,120)
        self.attack = randint(30,60)
        self.defense = randint(20,70)
        self.coins = 50
        self.inventory = {}


class Goblin():
    
    def __init__(self):
        self.name = "Goblin"
        self.level = 5
        self.health = randint(40,60)
        self.attack = randint(20,30)
        self.defense = randint(10,40)
        self.coins = 30
        self.inventory = {}


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

class Slime(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Slime"
        self.health = randint(5,15)
        self.attack = randint(5,15)
        self.defense = randint(5,15)
        self.coins = 10

class WildDog(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Wild Dog"
        self.health = randint(40,60)
        self.attack = randint(10,35)
        self.defense = randint(10,35)
        self.coins = 30

class Bandit(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Bandit"
        self.health = randint(40,60)
        self.attack = randint(40,60)
        self.defense = randint(40,60)
        self.coins = 100

class DemonKnight(Goblin):

    def __init__(self):
        super().__init__()
        self.name = "Demon Knight"
        self.health = randint(90,120)
        self.attack = randint(90,120)
        self.defense = randint(90,120)
        self.coins = 200


def GenerateEnemyList(number_of_enemies,enemy_list):
    generated_list = []

    try:
        # Asking user for number of enemies to generate
        number_of_enemies = int(number_of_enemies)
    except:
        print("Error Invalid Input")
        return None
    # Error Handling if the user doesnt input an integer

    if number_of_enemies <= 10 and number_of_enemies > 0:
        for i in range(number_of_enemies): # Populates the enemy list with how
           #many enemies are specified
            x = choices(list(enemy_list), weights = 
                    (30,25,20,15,10,5),k = 1)
            x = x[0]

            if x.name == "Slime":
                generated_list.append(Slime())

            elif x.name == "Goblin":
                generated_list.append(Goblin())

            elif x.name == "Hobgoblin":
                generated_list.append(HobGoblin())

            elif x.name == "Wild Dog":
                generated_list.append(WildDog())

            elif x.name == "Bandit":
                generated_list.append(Bandit())

            elif x.name == "Demon Knight":
                generated_list.append(DemonKnight())
    else:
        print("Error Invalid Number of Enemies")
        return None

    return generated_list
