# Presence check = To check that data has been entered into a field and that the field has not been left blank

number_plate = input("Enter your registration number")

while len(number_plate) == 0:
    print("You have not entered a registration number. Please try again:")
    number_plate = input("Enter your registration number")

print("Thank you for entering the registration number" + number_plate + "      thank you, Goodbye!")


# Length check = checks that the data is not too long or too short (limitation = doesnt check data type, could put correct length of anything and still have no errors)

name = input("Enter a 4 letter name:   ")

while len(name) != 4:
    print("\n")
    print("That is " + str(len(name)) + "letters, Please try again:")
    name = input("Enter a 4 letter name:   ")

print("\n")
print("Great job!, " + name + ", it is a 4 letter name")


# Type check = checks the data type of an input

#first way = prints the data type
data = "hello"

print(data)
print(type(data))

#second way = checks true if the input matches the corrwct data type

print("Is string:", isinstance(data , str))
print("Is integer:", isinstance(data , int))
print("Is float:", isinstance(data , float))
print("Is boolean", isinstance(data, bool))

# format check = checks that the data is in the right format

import re

email = input("Please enter your email address: ")
pattern = "^[ A-Za-z0-9.]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+$"            # this allows users to have capital characters from A-Z as well as lowercase characters from a-z and numbers 0-9 
email_match = re.match(pattern,email)                               # must have an @ symbol and a . inbetween in oreder for it to be a valid email address

if email_match: 
    print("This is a valid email address")

else:
    print("This is an invalid email address")

# Range check = checks that the data entered is within the correct range

score = int(input("Please enter your score out of 30: "))

if score > 30:
    print("invalid score, enter again")

elif score >= 0 & score <=30:
    print("your score is  " + str(score) + "/30")

# check digit = checks that the data entered in a string are numbers

a = "20072"

b = "twentytwothousand"

c = "20twenty2"

print(a.isdigit())
print(b.isdigit())
print(c.isdigit())                                                 #cant be a mix of letters and numbers, must strictly be numbers
