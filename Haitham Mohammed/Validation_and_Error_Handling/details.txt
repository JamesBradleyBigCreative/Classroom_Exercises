
import re

name = str(input("Enter your name: "))
def NameCheck (name):
    while len(name) == 0:
        print("You have not entered a name!")
        name = str(input("Enter your name: "))
    
    if isinstance(name,str) == True:
        print("Valid name")
    else:
        print("Invalid name")
        name = str(input("Enter your name: "))
       
NameCheck(name)

DOB = str(input("Enter your Date Of Birth: "))
def DOB_check(DOB):
    while len(DOB) == 0:
        print("You have not entered your Date of Birth")
        DOB = str(input("Enter your Date Of Birth: "))
    pattern_2 = re.compile("^[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]$")
    if pattern_2.match(DOB):
        print("Valid Date of Birth")
    else:
        print("Invalid Date of Birth")
        DOB = str(input("Enter your Date Of Birth: "))
DOB_check(DOB)
number = str(input("Enter your phone number: "))
def number_check(number):
    while len(number) == 0:
        print("You have not entered your phone number")
        number = str(input("Enter your phone number: "))
    pattern_3 = re.compile ("^[0-9]$")
    
    if pattern_3.match(number):
        print("Valid phone number")
    else:
        print("Invalid phone number")
        number = str(input("Enter your phone number: "))
number_check(number)
address = str(input("Enter your address: "))
def address_check(address):
    while len(address) == 0:
        print("You have not entered your address")
        number = str(input("Enter your address: "))
    pattern_4 = re.compile ("^[A-Za-z0-9]$")
    
    if pattern_4.match(address):
        print("Valid address")
    else:
        print("Invalid address")
        address = str(input("Enter your address: "))
address_check(address)
postcode = str(input("Enter your postcode: "))
def postcode_check(postcode):
    while len(postcode) == 0:
        print("You have not entered your postcode")
        postcode = str(input("Enter your postcode: "))
    pattern_5 = re.compile ("^[A-Za-z0-9] [A-Za-z0-9]$")
    
    if pattern_5.match(postcode):
        print("Valid postcode")
    else:
        print("Invalid postcode")
        number = str(input("Enter your postcode: "))
postcode_check(postcode)

print(name,DOB,number,address,postcode)



f = open("demofile.txt", "a")

