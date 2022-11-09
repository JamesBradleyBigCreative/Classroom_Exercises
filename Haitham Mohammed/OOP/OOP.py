import module1 as mod

inp_1 = input("Pick a number between 1 and 10: ")
def weapon(self):
        
        if inp_1 >= 5:
            self.weapon = "Flip-flops"
            self.xp += 15
        else:    
            self.xp += 25
            self.weapon = "Pan"


weapon()
inp_2 = input("Pick a number between 1 and 6: ")
def health(self):
        if inp_2 > 3:
            self.xp += 20
            self.health += 50
            print("Health is 50")
        elif inp_2 < 3:
            self.xp += 25
            self.health += 100
            print("Health is 100")
health()
inp_3 = input("You see a large treasure chest and no one is around!, do you want to open it (y/n): ")
        
def coins(self):
        
        if inp_3 == "y":
            self.coins = self.coins - 50
            print("You have been trapped and lost 50 coins")
            self.xp -= 10
        else:
            self.xp
            self.coins = self.coins + 50
            print("Smart choice, you avoided a coin trap. You have been awarded 50 coins")
coins()






inp_4 = None
def xp(self):
    inp_4 = self.xp
    while self.xp >= 100:
            exit()
xp(mod.mov.description(mod.mov()))


print(mod.mov.description(mod.mov(inp_1,inp_2,inp_3)))





