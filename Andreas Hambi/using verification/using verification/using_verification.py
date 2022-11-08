import re

def name():
    global person
    person = input("enter your name: ")
    

    a = False

    while len(person) == 0:
        print("You have not entered a name, please try again: ")
        person = input("enter your name: ")

    while a == False:
        pattern = re.compile("^[A-Za-z]+$")    
        if pattern.match(person):
            print("This is a valid name")
            a = True
        else:
            print("This is an invalid name")
            person = input("enter your name: ")
    
    #print(type(person))
name()

def dob():
    global dateOfBirth
    dateOfBirth = input("Please enter your date of bbirth in the format DD/MM/YYYY:    ")
    b = False

    while len(dateOfBirth) == 0:
        print("You have not entered a date of birth, please try again: ")
        dateOfBirth = input("Please enter your date of bbirth in the format DD/MM/YYYY")

    while b == False:
        pattern_2 = re.compile("^[0-9]+\/[0-9]+\/[0-9]+$")
        if pattern_2.match(dateOfBirth):
            print("This is a valid date of birth")
            b = True               

        else:
            print("invalid date of birth please try again")
            dateOfBirth = input("Please enter your date of bbirth in the format DD/MM/YYYY:    ")
    
    f.write(dateOfBirth)
dob()

def phoneNumber():
    global number
    number = input("Enter your 11 digit phone number starting with 07     ")
    c = False

    while len(number) == 0:
        print("You have not entered a phone number, please try again: ")
        number = input("Enter your 11 digit phone number starting with 07     ")

    while c == False:
        pattern_3 = re.compile("^[07]+[0-9]+$")
        if pattern_3.match(number) and len(number) == 11:
            print("This is a valid phone number")
            c = True
            
        else:
            print("Invalid phone number, please try again:  ")
            number = input("Enter your 11 digit phone number starting with 07     ")

    f.write(number)
phoneNumber()

def address():
    global house
    house = input("Enter you address:  ")
    d = False

    while len(house) == 0:
        print("You have not entered an address, please try again: ")
        house = input("Enter you address:  ")

    while d == False:
        pattern_4 = re.compile("^[0-9]+[A-Za-z ]+$")
        if pattern_4.match(house):
            print("This is a valid address")
            d = True
            
        else:
            print("Invalid address, please try again:  ")
            house = input("Enter you address:  ")
    
    f.write(house)

address()

f= open(f"{person}.txt","w")
f.write(f"NAME: {person}")
f.write(dateOfBirth)
f.write(number)
f.write(house)