import pandas as pd
import os

df_csv = pd.read_csv('pokemon_data.csv')
df_csv.style.hide(subset=None, axis=0, level=None, names=False)

def start_up():
    print("   Welcome to the Pokedex   ")
    print("____________________________")
    print("What would like to search by")
    print("""
    _____________________
    |  Pokedex No.  '0' |
    ---------------------
    _____________________
    |  Pokemon Name 'N' |
    ---------------------
    _____________________
    |  Pokemon Type 'T' |
    ---------------------
    """)
    
    to_cont = False
    to_cont = user_menu()

    if to_cont == True:
        os.system('cls')
        print("\nHeading back to the Menu...\n")
        start_up()


def user_menu():

    attempts = 0
    while attempts < 3:
        Choice = input("")

        if Choice == '0':
            to_cont = search_by_num()
            return to_cont

        elif Choice == 'N' or Choice == 'n':
            to_cont = search_by_name()
            return to_cont

        elif Choice == 'T' or Choice == 't':
            to_cont = search_by_type()
            return to_cont

        else:
            print("Wrong Input")
            attempts += 1
    
    if attempts == 3:
        print("\nTOO MANY ATTEMPTS")
        quit()


def search_by_num():
    attempts1 = 0
    while attempts1 < 3:
        try:
            Input = int(input("\nEnter Pokedex Number: "))
            if Input > 721 or Input > 721:
                raise OverflowError
            break

        except ValueError:
            print("\nNUMBER NOT ENTERED")
            attempts1 += 1

        except OverflowError:
            print("\nVALUE NOT WITHIN POKEDEX PARAMETERS")

    if attempts1 == 3:
        print("\nTOO MANY ATTEMPTS")
        quit()

    print("")
    print(df_csv.loc[(df_csv['#'] == Input)])

    attempts2 = 0
    while attempts2 < 3:

        to_cont = input(
            "\nDo you wish to continue using the pokedex 'Y' or 'N': ")

        if to_cont == 'Y' or to_cont == 'y':
            return True

        elif to_cont == 'N' or to_cont == 'n':
            return False

        else:
            print("Wrong Input")
            attempts2 += 1

    if attempts2 == 3:
        print("\nTOO MANY ATTEMPTS")
        quit()


def search_by_name():
    attempts1 = 0
    while attempts1 < 3:
        Input = (input("\nEnter Pokemon Name: "))

        if Input in df_csv['Name'].to_string(index = False):
            print("")
            print(df_csv.loc[(df_csv['Name'] == Input)])
            break

        else:
            print("Wrong Input")
            attempts1 += 1

    if attempts1 == 3:
        print("\nTOO MANY ATTEMPTS")
        quit()

    attempts2 = 0
    while attempts2 < 3:

        to_cont = input(
            "\nDo you wish to continue using the pokedex 'Y' or 'N': ")

        if to_cont == 'Y' or to_cont == 'y':
            return True

        elif to_cont == 'N' or to_cont == 'n':
            return False

        else:
            print("Wrong Input")
            attempts2 += 1

    if attempts2 == 3:
        print("\nTOO MANY ATTEMPTS")
        quit()


def search_by_type():
    Input = type_check()

    print("")

    x = df_csv.loc[
        ((df_csv['Type 1'] == Input) | (df_csv['Type 2'] == Input))]
    print(x.to_string(index = False))

    attempts = 0
    while attempts < 3:
        to_cont = input(
            "\nDo you wish to continue using the pokedex 'Y' or 'N': ")

        if to_cont == 'Y' or to_cont == 'y':
            return True

        elif to_cont == 'N' or to_cont == 'n':
            return False

        else:
            print("Wrong Input")
            attempts += 1

    if attempts == 3:
        print("\nTOO MANY ATTEMPTS")
        quit()

def type_check():
    with open("PokeTypes.txt","r") as f:
        lines = [line.rstrip() for line in f]

        attempts = 0
        Flag = False
        while attempts < 3:
            Input = (input("\nEnter Pokemon Type: "))

            if Input in lines:
                return Input
                break

            else:
                print("Wrong Input")
                attempts += 1

        if attempts == 3:
            print("\nTOO MANY ATTEMPTS")
            quit()

start_up()