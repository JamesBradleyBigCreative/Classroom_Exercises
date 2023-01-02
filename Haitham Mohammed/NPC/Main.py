from NPC import *
from Bank import *
import Bank as b
import NPC as n
def shop(loop,NPC):

    while loop == True:
        global wallet 
        global credits
        global loan
        global Items

      
        
        if wallet <= 0:
            print("You are offcially broke")
            credits = True
            loan()
            break
        
        elif NPC.lower() == "bike":
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
            print("You idiot we don't have that here!")
            break

      

shop(loop,NPC)  