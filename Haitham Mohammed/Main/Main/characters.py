
from random import  randint
enemy_list = []

class Goblin:
    def __init__(self):
        self.Name = "Goblin"
        self.Level = 1
        self.Attack = randint(40,60)
        self.Health = randint(10,60)
        self.Defence = randint(30,50)
 
class Hobgoblin(Goblin):
    def __init__(self):
        Goblin.__init__(self)
        self.Name = "Hobgoblin"
        self.Health = (self.Health * 1.25)
        self.Attack = (self.Attack * 1.25)
        self.Defence = (self.Defence * 1.25)


class Titan :

    def __init__(self):
        self.Class = "Titan"
        self.Level = 1
        self.Attack = randint(80,200)
        self.Health = randint(65,100)
        self.Defence = randint(80,100)
        self.Coins = 0

    def weapon():
      rand = randint(1,5)
      if rand <= 5:
            self.weapon = "LA CHANCLA"
            print("You have equipped LA CHANCLA")
      else:
            self.weapon = "DA CROCS"
            print("You have eqipped DA CROCS ")
      

    def coins(self):
        inp_3 = input("You see a large treasure chest and no one is around!, do you want to open it (y/n): ")
        if inp_3 == "y":
            self.coins -= 50
            self.health -= 25
            print(f"You have been trapped and lost 50 coins you now have {self.coins} coins and your health is {self.health}")
   
        else:
            self.coins += 75 
            self.health += 45
            print("You have been granted 75 coins!")
            print(f"Smart choice, you avoided a coin trap. You have been awarded {self.coins} coins. Your health is now {self.health}")
    

class Warlock :
    def __init__(self):
        self.Class = "Warlock"
        self.Level = 1
        self.Attack = randint(75,100)
        self.Health = randint(50,100)
        self.Defence = randint(70,100)
        self.Coins = 0
    def weapon(self):
       rand = randint(1,5)
       if rand <= 5:
            self.weapon = "LOS TACONES"
            print("You have equipped LOS TACONES")
       else:
            self.weapon = "DA  "
            print("You have eqipped DA CROCS ")

    def coins():
        inp_3 = input("You see a large treasure chest and no one is around!, do you want to open it (y/n): ")
        if inp_3 == "y":
            self.coins -= 50
            self.health -= 25
            print(f"You have been trapped and lost 50 coins you now have {Warlock.coins} coins and your health is {Warlock.Health}")
   
        else:
            self.coins += 75 
            self.health += 45
            print("You have been granted 75 coins!")
            print(f"Smart choice, you avoided a coin trap. You have been awarded {Warlock.coins} coins. Your health is now {Warlock.Health}")
 

class Hunter :
    def __init__(self):
        self.Class = "Hunter"
        self.Level = 1
        self.Attack = randint(80,100)
        self.Health = randint(60,100)
        self.Defence = randint(60,100)
        self.Coins = 0   


    def weapon(self):
        rand = randint(1,5)
        if rand <= 5:
            self.weapon = "LOS SANDALIAS"
            print("You have equipped LOS SANDALIAS")
        else:
            self.weapon = "DA CROCS"
            print("You have eqipped DA CROCS ")
   

    def coins(self):
        inp_3 = input("You see a large treasure chest and no one is around!, do you want to open it (y/n): ")
        if inp_3 == "y":
            self.coins -= 50
            self.health -= 25
            print(f"You have been trapped and lost 50 coins you now have {Hunter.coins} coins and your health is {Hunter.health}")
   
        else:
            self.coins += 75 
            self.health += 45
            print("You have been granted 75 coins!")
            print(f"Smart choice, you avoided a coin trap. You have been awarded {Hunter.coins} coins. Your health is now {Hunter.health}")
























