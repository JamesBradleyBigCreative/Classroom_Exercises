import re 

def Name():
    name = input("Enter your full name: ")
    while len(name) == 0:
       print("You forgot to type your name. ")
       name = input ("try one more time." "\n" "write your name: ")
    pattern = "^[A-Za-z]+$"
    nameMatch = re.match(pattern, name)
    if nameMatch:
        print("Thank you, this is a valid name. Please, continue")
    else:
        print(input("This is an invalid name." "\n" "Try one more time: "))
Name()

print("\n")

def Age():
    age = input ("Enter your age: ")
    while len(age) == 0:
        print("You forgot to type your age.")
        age = input("Try one more time." "\n" "Write tour age please: ")
    pattern = "^[0-9]+$"
    ageMatch = re.match(pattern, age)
    if ageMatch:
        print("Valid age. Please, continue")
    else:
        print(input("This is an invalid Age." "\n" "Try one more time: "))
Age() 

print("\n")

def Birth():
    birth = input("DD/MM/YY: ")
    while len(birth) == 0:
        print("You forgot to type your birth.")
        birth = input("Try one more time." "\n" "Write tour birth please: ")
    pattern = "^[0-9]+\/[0-9]+\/[0-9]+$"
    birthMatch = re.match(pattern, birth)
    if birthMatch:
        print("Thank you, this is a valid birth. Please, continue")
    else:
        print(input("This is an invalid birth." "\n" "Try one more time: "))
Birth()

print("\n")

def Tell_Num():
    num = input("Enter your tell number: ")
    while len(num) != 11:
        print("This is " + str(len(num)) + " digits. Please, make sure that your tell number has 11 digitsnumbers ")
        num = input (" please, write your tell number again:  ")
    pattern = "^[0-9]+$"
    numMatch = re.match(pattern, num)
    if numMatch:
        print("Valid tell number. Please, continue")
    else:
        print(input("This is an invalid tell number." "\n" "Try one more time: "))

Tell_Num()

print("\n")

def Address():
    house = input("Enter your Address: ")   
    while len(house) == 0:
       print("You forgot to type your address. ")
       house = input ("try one more time." "\n" "write your address: ")
    pattern = "^[A-Za-z]+$"
    addressMatch = re.match(pattern, house)
    if addressMatch:
        print("Thank you, this is a valid address. Please, continue")
    else:
        print(input("This is an invalid address." "\n" "Try one more time: "))
Address()

