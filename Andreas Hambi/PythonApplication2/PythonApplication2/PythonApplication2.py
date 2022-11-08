#myArray = ["D", "F", "R", "A"]

#myArray.sort()

#print(myArray)


 #LIBRARIES
#import random
#import time

# CHARACTER INFO
#name = None
#age = None
#vehicle = None
#specialPower = None

# METHODS/FUNCTION DEFINITIONS
#def Chapter_1():
 #   print(name, " went on a dangerous mission to save the galaxy. \n")
  #  print(name, " is ", age, " years old and gets around in a.", vehicle, "\n")
  #  print(name, " will save the day with the power of ", specialPower, ". \n")

#def Chapter_2():
#    print("chapter 2 coming soon...")



# MAIN
#name = str(input('Enter name: '))
#age = int(input('Enter age: '))
#vehicle = str(input('Enter vehicle: '))
#specialPower = str(input('Enter special power: '))

#input('PRESS ENTER TO CONTINUE...')

#Chapter_1()
#Chapter_2()



import random
import time


#character info
name = None
age = None 
vehicle = None
super_power = None


#def Chapter_1():
 #   print(name, " went on a dangerous mission to save the galaxy. \n")
  #  print(name, " is ", age, " years old and gets around in a.", vehicle, "\n")
  #  print(name, " will save the day with the power of ", specialPower, ". \n")




#scenario
def chapter_1():
 print(name, ' went to buy some milk "and" never to be returned again \n')
 print(name, "is", age, " years old and has 2 kids that he left behind. he left them without a single penny and drove off with a. ", vehicle, "\n")
 print(name, "he really disapeared and never came back showing us tha he had", super_power, ". \n")


def chapter_2():
    print("chapter 2 coming soon")


def GenerateRandomInteger(minimum, maximum):
    rand = random.randint(minimum, maximum)
    return rand
#main
name = str(input("Enter a Name: "))
age = int(input('Enter Age'))
vehicle = str(input('Enter your Vehicle'))
super_power = str(input('Enter your super power'))


_randomNumber = GenerateRandomInteger(0,10)

if _randomNumber>7:
    print("Aviol gets back to his kid's")
elif _randomNumber<5:
    print("Aviol doesent get back to his kid's")
elif _randomNumber==7:
    print('Aviol says hello')
def Chapter_2():
    print("chapter 2 comining soon...")











