import re

def user_name():
    name = input("Enter your Name: ")
    pattern = "^[A-Za-z]+$"
    nameMatch = re.match(pattern,name)
    if nameMatch:
        print("valid input")
    else:
        print("invalid input")
        name =  input("Enter your Name: ")

    while len(name) == 0:
        print("invalid input.")
        name = input(" Please Enter Your Name: ")


user_name()


def DOB():
    dob = input("Enter your date of birth (dd/mm/yy): ")
    pattern = "^[0-9]+\/[0-9]+\/[0-9]+$"
    dobMatch = re.match(pattern, dob)
    if dobMatch:
        print("valid date of birth.")
    else:
        print("invalid Birth date.")
DOB()

def tel_Num():
    num1 = input(" Enter your phone number. (It must be 11 Digits and bein with 07!) : ")
    while len(num1) != 11:
        print("\n")
        print("That is " + str(len(num1)) + " digits , please try again! ")
        num1 = int(input(" Enter your phone number. \n (Remember that it must be 11 Digits and bein with 07!) : "))
    print("Valid number")

tel_Num()









# phone number + address



 





