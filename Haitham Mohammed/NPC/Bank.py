from NPC import *
from Main import *
class Bank:
    def __init__(self,loan,withdrawl,deposit,scam):
        self.loan = loan
        self.withdrawl = withdrawl
        self.deposit = deposit
        self.scam = scam
    
    def loan(self):
        while credits == True:
            
            loan = input("Are you interested in taking a loan (y/n)")
            loan.upper()
            if loan == "Y":
                wallet += 1000
                self.loan = True
                print(f"You now have ${wallet}")
            else:
                credits == False



    