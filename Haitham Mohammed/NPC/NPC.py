loop = True
print("''''''''''''''''''''''''''''''''''''''''\n       DA NPC Shop      \n ''''''''''''''''''''''''''''''''''''''''")
Items =  {"bike": 100, 
          "motorbike": 700, 
          "car": 1500, 
          "supercar" : 80000, 
          "jet": 500000, 
          "boeing-747": 15000000}

buy = []
wallet = int(input("enter money: "))
print(f"You have ${wallet}")
for key, value in Items.items():
    print(key, '->', value)
NPC = str(input("Hello my name is Amanda \nWhat would you like to purchase(type q to quit): "))
NPC= NPC.lower()
def shop(loop,NPC):

    while loop == True:
        global wallet 
        if NPC.lower() == "bike":
           
            wallet -= Items[NPC]
            print(f"You have bought a {NPC}, you now have ${wallet}")
            buy.append(NPC)
            loop = False

        elif NPC.lower() == "motorbike" :
            wallet = wallet - Items[NPC]
            print(f"You have bought a {NPC}, you now have ${wallet}")
            buy.append(NPC)
            loop = False
            
        elif NPC.lower() == "car":
            wallet = wallet - Items[NPC]
            print(f"You have bought a {NPC}, you now have ${wallet}")
            buy.append(NPC)
            loop = False

        elif NPC.lower() == "supercar":
            wallet = wallet - Items[NPC]
            print(f"You have bought a {NPC}, you now have ${wallet}")
            buy.append(NPC)
            loop = False

        elif NPC.lower() == "jet":
            wallet = wallet - Items[NPC]
            print(f"You have bought a {NPC}, you now have ${wallet}")
            buy.append(NPC)
            loop = False

        elif NPC.lower() == "boeing-747":
            wallet = wallet - Items[NPC]
            print(f"You have bought a {NPC}, you now have ${wallet}")
            buy.append(NPC)
            loop = False

        else:
            quit()

      

shop(loop,NPC)        
Again = False
while Again == False:
 
    Another = input("Do you want to buy another item (y/n)")
    Another = Another.lower()
    if Another == "y":
        NPC = str(input("What would you like to purchase(type q to quit): "))
        buy.append(NPC)
        print(buy)
        shop(loop,NPC) 

    elif Another == "n":
        break