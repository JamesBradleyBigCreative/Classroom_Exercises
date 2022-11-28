
from random import  randint

goblin_list = []
hobgoblin_list = []
enemy_list = []
is_win = False
is_lose = False
class Goblin:
    def __init__(self):
        self.Name = "Goblin"
        self.Level = 1
        self.Attack = randint(40,60)
        self.Health = randint(60,200)
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
    
    def weapon(self):
      rand = randint(1,5)
      if rand <= 5:
            self.weapon = "LA CHANCLA"
            print("You have equipped LA CHANCLA")
      else:
            self.weapon = "DA CROCS"
            print("You have eqipped DA CROCS ")
    
    

class Warlock :
    def __init__(self):
        self.Class = "Warlock"
        self.Level = 1
        self.Attack = randint(75,100)
        self.Health = randint(50,100)
        self.Defence = randint(70,100)
 
    def weapon(self):
       rand = randint(1,5)
       if rand <= 5:
            self.weapon = "LOS FUTBOL"
            print("You have equipped LOS FUTBOL")
       else:
            self.weapon = "DA  BANANANA"
            print("You have eqipped DA BANANANA ")

class Hunter :
    def __init__(self ):
        self.Class = "Hunter"
        self.Level = 1
        self.Attack = randint(80,100)
        self.Health = randint(60,100)
        self.Defence = randint(60,100)

    def weapon(self):
            rand = randint(1,5)
            if rand <= 5:
                self.weapon = "LOS SANDALIAS"
                print("You have equipped LOS SANDALIAS")
            else:
                self.weapon = "DA ZUCC"
                print("You have eqipped DA ZUCC ")

player_1 = Hunter()
player_2 = Titan()
player_3 = Warlock() 



class_input = str(input("Choose a player class\n Hunter\n Titan\n Warlock\n : "))
def story(Hobgoblin, is_win, is_lose):  
        inp_3 = input("You see a large treasure chest and no one is around!, \
               do you want to open it yes or no(y/n): ") 
        if inp_3 == "y" or inp_3 == "Y":
                print("You have been trapped and you died !")
                is_lose = True
        else:
                print("Smart choice, you avoided a coin trap. You survived!") 
        while is_win == False and is_lose == False:    
            
            inp_4 = input("A hobgoblin attacks you. Do you want to attack it or run away: ")
            Current_Hobgoblin = Hobgoblin()
            if inp_4 == "Attack" or inp_4 == "attack":
                if class_input == "Hunter" or class_input == "hunter":    
                    Current_Hobgoblin.Health = Current_Hobgoblin.Health - player_1.Attack
                    player_1.Level = 2
            
                print(f"You dealt {player_1.Attack} damage to the hobgoblin, \
                    its health is now{Current_Hobgoblin.Health} and you are now level {player_1.Level}")
                player_1.Level += 1 
                if class_input == "Titan" or class_input == "Titan":    
                    Current_Hobgoblin.Health = Current_Hobgoblin.Health - player_2.Attack
                    player_2.Level = 2
                    print(f"You dealt 10 damage to the hobgoblin,\
                        its health is now{Current_Hobgoblin.Health} and you are now level {player_2.Level}")    
                
                if class_input == "Warlock" or class_input == "Warlock":    
                    Current_Hobgoblin.Health = Hobgoblin.Health - player_3.Attack
                    player_3.Level = 2
                    print(f"You dealt 10 damage to the hobgoblin, \
                        its health is now{Current_Hobgoblin.Health} and you are now level {player_3.Level}")    
            elif inp_4 == "run" or inp_4 == "run away":
                
                print("You have run away and gained a\
                     debt of 2000 coins as a punishment for your humiliating feat. You Lose")
                is_lose = True
  

























