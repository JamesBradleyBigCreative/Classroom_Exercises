
#LIBRARIES
import random
import time

# CHARACTER INFO

name = None
age = None
element = None
weapon = None

# METHODS/FUNCTION DEFINITIONS          
def Chapter_1():
    print(name, "went to an arena \n")
    print(name, " is ", age, " and will fight with the", element, "element \n")
    print(name, " will possibly win the fight with using a ", weapon, "and the element of " ,element, "\n" )

    
    
def Chapter_2():
 print("chapter 2 coming soon...")

def GenerateRandomInteger(_min, _max):
    rand = random.randint(_min,_max)
    return rand

# MAIN
name = str(input('Enter name: '))
age = int(input('Enter age: '))
element = str(input('Enter element: '))
weapon = str(input('Enter weapon: '))

input('PRESS ENTER TO CONTINUE...')


Chapter_1()
Chapter_2()