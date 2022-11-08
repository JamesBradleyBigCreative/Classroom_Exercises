# Main Code

import Welcome as wel
import random as rand


Names = {
    "nathan" : 2203,
    "jordan" : 8586,
    "collin" : 8902,
    "vinny"  : 5242
}


# Entering the pin and username for the atm

def main():
    NewUser = input("Do You Want to add another User ('Y' or 'N'): ")
    NoOfTries = 0

    if NewUser == 'Y' or NewUser == 'y':
        name = input("Enter your name: ")
        AddNewUser(name)

    Flag = False
    
    user = input("\nEnter your name: ")

    if user in Names:
        while Flag == False:

            pin = int(input("\nEnter your pin: "))

            value = Names[user]

            if pin == value:
                wel.WelcomeScreen(user)
                Flag = True

            elif(NoOfTries > 2):
                print("\nError: Too Many Attempts")
                print("\nYou Are Now Locked out of the ATM")
                Flag = True

            else:
                print("\nError Wrong Pin")
                print(f"\nTries Remaining: {2-NoOfTries}")
                NoOfTries += 1

    else:
        print("\nWrong Name Entered")

# Allows the user to create a new account

def AddNewUser(name):

    NewUser = wel.users(name,0,rand.randrange(100000,999999),[])
    wel.accounts.append(NewUser)
    wel.accountnames.append(NewUser.name)
    Pin = rand.randrange(1000,9999)
    print(f"Your New Pin is {Pin}")
    Names.update({name : Pin})


main()

