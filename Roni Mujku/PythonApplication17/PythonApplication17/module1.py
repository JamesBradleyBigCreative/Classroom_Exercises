#Module 1

import os
from time import sleep

# The User Class
class users:
    def __init__(self,name,balance,accNum,History):
        self.name = name
        self.balance = balance
        self.History = History
        self.accNum = accNum

# Declaring the base accounts already stored in the ATM
nathan = users("nathan",100.0,523433,[])
jordan = users("jordan",100.0,234323,[])
collin = users("collin",100.0,876345,[])
vinny = users("vinny",100.0,123536,[])

# 2 Lists of the class instances themselves and the names stored in those classes as its own list
accounts = [nathan,jordan,collin,vinny]
accountnames = []
for i in accounts:
    accountnames.append(i.name)


#WelcomeScreen() The main function of the code where every external function is called in and the main loop

def WelcomeScreen(user):
    isQuit = False
    while isQuit == False:
        #sleep(4)


        print("""
        ___________________________                           ____________________
        | Mini Statement Press 'M'|                           | Balance Press 'B'|
        ---------------------------                           --------------------
    
        ______________________                                _______________
        | Withdrawl Press 'W'|                                | Transfer 'T'|
        ----------------------                                ---------------

        ____________________                                  _________________
        | Deposit Press 'D'|                                  | Quit Press 'Q'|
        --------------------                                  -----------------
        """)
        UserChoice = input("\nWhat Operation Do You Want To Perform: ")

        if UserChoice == 'M' or UserChoice == 'm':
            FileorTerm = input("\nDo You Want Your Reciept Printed (Press 'P') or On The Terminal (Press 'T')")
            if FileorTerm == 'P' or FileorTerm == 'p':

                for item in range(len(accountnames)):

                    if user == accounts[item].name:
                        MiniStatementPrint(accounts[item].History)

            if FileorTerm == 'T' or FileorTerm == 't':

                for item in range(len(accountnames)):

                    if user == accounts[item].name:
                        MiniStatement(accounts[item].History)

        elif UserChoice == 'W' or UserChoice == 'w':
            withdraw(user)
            os.system('cls')

        elif UserChoice == 'D' or UserChoice == 'd':
            deposit(user)
            os.system('cls')

        elif UserChoice == 'B' or UserChoice == 'b':
            for item in range(len(accountnames)):

               if user == accounts[item].name:
                   Balance(accounts[item])

        elif UserChoice == 'T' or UserChoice == 't':
            for item in range(len(accountnames)):

                if user == accounts[item].name:
                    Transfer(accounts[item])

        elif UserChoice == 'Q' or UserChoice == 'q':
            for item in range(len(accountnames)):

               if user == accounts[item].name:
                   PrintReciept(accounts[item].name, accounts[item].accNum, accounts[item].balance)

            print("\nQuitting from the terminal.....")
            isQuit = True

        else:
            print("Wrong Input")
            

# Prints a Ministatement for the user displaying the previous deposits and withdrawls done in the program

def MiniStatement(list1):

    print(f"""
             Mini Statement         
    (UP TO 8 ACCOUNT ENTERIES SINCE LAST STATEMENT)

    14 OCTOBER CHQ 10.98 DR

    15 OCTOBER CHQ 14.34 DR
    """)

    for i in range (len(list1)):
        print("   ", list1[i])
        print("   ")

# Prints a Ministatement for the user displaying the previous deposits and withdrawls done in the program by using file handiling and creates an actual text file

def MiniStatementPrint(list1):

    f = open("Reciept.txt", "w")

    f.write(f"""
             Mini Statement         
    (UP TO 8 ACCOUNT ENTERIES SINCE LAST STATEMENT)

    14 OCTOBER CHQ 10.98 DR

    15 OCTOBER CHQ 14.34 DR
    """)

    f.close()

    for i in range (len(list1)):
        f = open("Reciept.txt", "a")

        f.write("\n    " + list1[i])
        f.write("\n   ")

        f.close()

    f = open("Reciept.txt", "r")
      
    print(f.read())

# Deposit adds funds as a float to the currents users balance var from the users class

def deposit(name):
    prompt = float(input("\nEnter how much you would like to deposit:  "))
    
    for item in range(len(accountnames)):
        if name == accounts[item].name:

            accounts[item].balance += prompt

            accounts[item].History.append(f"17 OCTOBER DEP {prompt} DR")

            print("\nYour new balance is:" ,accounts[item].balance)

# Withdraw takes funds as a float to the currents users balance var from the users class if the input is larger than the users current balance than an error message will print

   
def withdraw(name):
    prompt = float(input("\nEnter how much you would like to withdraw:  "))

    for item in range(len(accountnames)):

        if name == accounts[item].name:

            if prompt > accounts[item].balance:
                print("ERROR ATTEMPTED TO WITHDRAW MORE THAN CURRENT BALANCE")

            else:
                accounts[item].balance -= prompt

                accounts[item].History.append(f"17 OCTOBER WIT {prompt} DR")

                print("\nYour new balance is:" ,accounts[item].balance)


#A reciept that is printed when the Quit option is chosen on the welcome screen

def PrintReciept(name, accnum, bal):
    reciept = open("receipt.txt", "w")

    reciept.write("""
    RECIEPT
    -------
    """)

    reciept = open("receipt.txt","a")

    reciept.write(f"""
    NAME: {name}
    ACCOUNT NUMBER: {accnum} 
    CURRENT BALANCE: ${str(bal)} 
    """)

    reciept = open("receipt.txt", "r")

    print(reciept.read())

    reciept.close()

# Displays the users balance variable from the users class (Is called in the WelcomeScreen function when 'b' is inputed)

def Balance(user):
    print(f"\nCurrent Balance is {user.balance}")

# Transfer an inputed fund from the current users balance to another chosen users balance

def Transfer(user):
    print(accountnames)

    x = input("\nWho Would You Like to Transfer Funds To: ")
    flag = False

    for item in range(len(accountnames)):

       if x == accounts[item].name:
           FundsToSend = float(input("\nHow Much Would You Like To Transfer: "))

           user.balance -= FundsToSend

           accounts[item].balance += FundsToSend
           print(f"You Have Sent ${FundsToSend}")
           flag = True

    if flag == False:
        print("\nERROR USER DOES NOT EXIST")

