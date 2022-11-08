#LIBRARIES

from ast import And, Or
import random
import time

# CHARACTER INFO
name = None
age = None
vehicle = None
specialPower = None
villains = ['Cell','Raditz','Vegeta','Frieza']


# METHODS/FUNCTION DEFINITIONS
def GenerateRandomInteger(_min, _max):
    rand = random.randint(_min,_max)
    return rand

def Chapter_1():
    print("CHAPTER 1: \n")
    print(name, " went on a dangerous mission to save the galaxy. \n")
    print(name, " is ", age, " years old and gets around in a.", vehicle, "\n")
    print(name, " will save the day with the power of ", specialPower, ". \n")

def Chapter_2():
    print("CHAPTER 2: \n")
    ChosenVillNum = GenerateRandomInteger(0,len(villains)-1)
    ChosenVill = villains[ChosenVillNum]
    print("On",Pluralname,"journey they encounter the villain", ChosenVill, ". \n")

    if (ChosenVill == 'Raditz' or ChosenVill == 'Vegeta'):
        print(f"{Pluralname} is facing a Saiyan. \n")
        x = input("Press K to use Kaiyoken to match their power. \n")
        if (x == "K" or x == "k"):
            print(f"{name} has used Kaiyoken to power up to unfathomable levels. \n")
            print(f"By using {specialPower} {name} has defeated {ChosenVill}.\n")
            flag = True
            return flag
        else:
            print(f"{name} failed to power up in time, {ChosenVill} has defeated them in battle.\n")
            flag = False
            return flag
    elif(ChosenVill == 'Frieza'):
        print(f"{ChosenVill} was too strong {Pluralname} friend has died. \n")
        y = input("Press S to transform. \n")
        if (y == "s" or y == "S"):
            print(f"The trauma of that even caused {name} to transform into the legendary super {name}. \n")
            print(f"{ChosenVill} was defeated when {name} threw their {vehicle} into {ChosenVill}. \n")
            flag = True
            return flag
        else:
            print(f"{name} failed to power up in time, {ChosenVill} has defeated them in battle.\n")
            flag = False
            return flag
    elif(ChosenVill == 'Cell'):
        print(f"By absorbing two androids and {Pluralname} {vehicle.lower()}, {ChosenVill} has transformed into Perfect {ChosenVill}. \n")
        print(f"{name} sacrificed themselves in battle.\n")
        sonname = input("Enter your sons name: \n") + "han"
        print(f"However their son {sonname} takes on the fight.\n")
        p = input("Press S to transform. \n")
        if (p == "s" or p == "S"):
            print(f"{sonname}han managed to transform into Super {sonname} 2. \n")
            print(f"{ChosenVill} was defeated when {sonname} used his {specialPower}. \n")
            flag = True
            return flag
        else:
            print(f"{sonname} failed to power up in time, {ChosenVill} has defeated them in battle. \n")
            flag = False
            return flag

def Chapter_3(flagfunc):
    print("CHAPTER 3:\n")
    if flagfunc == True:
        print(f"{name} saved the galaxy \n")
    else:
        print(f"{name} failed to save the galaxy \n")

    
# MAIN
name = str(input('Enter name: '))
age = int(input('Enter age: '))
vehicle = str(input('Enter vehicle: '))
specialPower = str(input('Enter special power: '))
Pluralname = name + "s"

input('PRESS ENTER TO CONTINUE...')

Chapter_1()
flag = Chapter_2()
Chapter_3(flag)
