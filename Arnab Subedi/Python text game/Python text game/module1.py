#Defining classes for characters which stores character details

class naruto:
    health = 500
    name = "Naruto"
    rank = "Ninja"
    abilities = "shadow clone jutsu"
    ultimate = "rasengan"
    def stats():
        print(f"{naruto.name} is {naruto.rank} and has the ability {naruto.abilities} and his ultimate is {naruto.ultimate} and has {naruto.health} health \n")
        print("\n")

class sasuke:
    health = 350
    name = "sasuke"
    rank = "Akatsuki"
    abilities = "rinnegan"
    ultimate = "asura path"
    def stats():
        print(f"{sasuke.name} is {sasuke.rank} and has the ability {sasuke.abilities} and his ultimate is {sasuke.ultimate} and has {sasuke.health} health \n")
        print("\n")
        

class kakashi:
    health = 300
    name = "kakashi"
    rank = "hokage"
    abilities = "copy"
    ultimate = "rasengan"

    def stats():
        print(f"{kakashi.name} is {kakashi.rank} and has the ability {kakashi.abilities} and his ultimate is {kakashi.ultimate} and has {kakashi.health} health \n")
        print("\n")

#class for level 1 of the game which has a boss and the character has to kill the boss
class level1:
    def __init__(self,name,ability,health,ultimate):
        self.name = name
        self.ability = ability
        self.health = health
        self.ultimate = ultimate
    def villain(self):
        print(f" There once was a villian far from the world.. \n")
        print(f" He hid in the sand of the moon and watched the earth grow... \n")
        print(f" His name was madara uchiha... \n ")
        print(f" One october he fell from the moon and infront of {self.name} \n")
        battle = input("do you want to fight madara uchiha y/n: ").lower
        print("\n")
        if battle == "y":
             print(f"{self.name} used his ability but it failed \n")
        elif battle == "n":
            print("you lost! \n")
            exit()
        self.health -= 120
        print(f"{self.name} lost 120 hp leaving him with {self.health} \n")
        battle_a = input("your ultimate is charged up do you want to use it y/n: ")
        print("\n")
        if battle_a == "y":
           print(f"{self.name} used his ultimate {self.ultimate} and killed madara uchiha with {self.health} hp \n")
           print("you completed level 1")
        elif battle_a == "n":
            print("you lost! \n")
            exit()

#class for level 2 
class level2:
    def __init__(self,name,ability,health,ultimate):
        self.name = name
        self.ability = ability
        self.health = health
        self.ultimate = ultimate
    def villain(self):
        damage = 0
        print(f"{self.name} heads towards the sand village ----- \n")
        direction = input(f"do you want {self.name} to go n,s,e,w : ")
        ob = ""
        if direction == "n":
            print(f"{self.name} goes north! \n")
            print("\n")
            print(f"{self.name} finds a hidden object in a stone carving! \n")
            print("\n")
            print(f" this object give {self.name} a power boost! ")
            print("\n")
            ob = "pb"
        elif direction == "s":
            print(f"{self.name} goes south! ")
            print("\n")
            print(f"{self.name} finds a hidden object in a leaf ! \n")
            print("\n")
            print(f" this object give {self.name} a health boost ! ")
            print("\n")
            ob = "hb"
        elif direction == "e":
            print(f"{self.name} goes east! ")
            print("\n")
            print(f"{self.name} finds a hidden object in a ocean ! \n")
            print("\n")
            print(f" this object give {self.name} a 10 second damage protection ! ")
            print("\n")
            ob = "10 sec"
        elif direction == "w":
            print(f"{self.name} goes west! ")
            print("\n")
            print(f"{self.name} finds a hidden object in a cave ! \n")
            print("\n")
            print(f" this object give {self.name} a chakra boost to make normal abilites more powerful! \n ")
            print("\n")
            ob = "chakra boost"
        boss_health = 1200
        print(f"{self.name} while patroling sees a flashing light from the ocean! \n")
        do = input(f"do you want to run or do you want to fight! r/f :")
        print("\n")
        if do == "r":
            print(f"{self.name} decides to run from the main boss: ")
            print("\n")
            print(" You lost !")
            exit()
        elif do == "f":
            print(f"{self.name} decides to fight the main boss! \n ")
            print("\n")
            print(f"The boss has {boss_health} Hp! ")
            print("\n")
            p = input(f"do you want to use your object {ob} y/n: ")
            if p == "y":
                if ob == "pb":
                    print(f"{self.name} recieves a power boost! \n")
                    damage += 1200
                    print(f"{self.name} will damage the boss {damage} ! \n")
                    print(f"{self.name} One shots the boss with his ultimate {self.ultimate} and leaves the boss with {boss_health-damage}! \n")
                    print(f"You won this level ! \n")
                elif ob == "hb":
                    print(f"{self.name} recieves a health boost! \n")
                    self.health += 300
                    print(f"{self.name} has {self.health} hp ! \n")
                    print(f"{self.name} has more health and uses {self.ability} 3 times and kills the main boss ! \n")
                    print(f"You won this level ! \n")
                elif ob == "10 sec":
                    print(f"{self.name} recieves a 10 seconds damage protection")
                    i = 0
                    for i in range(10):
                        i+=1
                        print(i)
                    print(f"this gave {self.name} enough time to beat the boss by using his ultimate {self.ultimate}! \n")
                    print(f"you won this level! ")
                elif ob == "chakra boost":
                    print(f"{self.name} got a chakra boost and causes more damage with first ability")
                    damage += 1000
                    print(f"{self.name} causes {damage} with his ability leaving the boss with {boss_health-damage}, with one more hit from his ability {self.ability} he beats the boss! ")
                    print(f"you won this level !")
                    
                    
                 








