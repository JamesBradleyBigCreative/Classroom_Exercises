#presence check

name = input("please enter your name: ")

while len(name) == 0:
    print("you have not entered your name!")
    name = input("please enter your name: ")

print(f"Thank you for entering your name {name}! ")

#length check

h = input("please enter a 4 letter word: ")

while len(h) != 4:
    print(f"Invalid, word is not 4 letters , it is {str(len(h))}")
    h = input("please enter a 4 letter word: ")

print("\n")
print(f"thank you {h} is 4 letters!")

#type check

data = input("enter your data: ")

print(data)
print(type(data))

print(f"is string, {isinstance(data,str)}")
print(f"is float, {isinstance(data,float)}")
print(f"is int, {isinstance(data,int)}")

#Format check
import re
sortcode = input("enter your sortcode: ")
cont = False
rex = re.compile("^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$")
while cont == False:
    if rex.match(sortcode):
        print("[[[[[SORT CODE ACCEPTED!]]]]]")
        cont = True
    else:
        print("[[[[MAKE SURE THE SORT CODE IS IN THE FORMAT 00-00-00 WHERE 0 is 0-9! ]]]]")
        sortcode = input("Enter your Sort code: ")

#range check

score = int(input("Enter your score:"))

if score <= 39:
    print(f"You did not pass as your score {score} is lower than 39!")
elif score >= 40 and score <=100:
    print(f"You have passed with {score} points!")

#check digit
a = "2022"
b = "twentytwo"
c = "20twentytwo"

print(a.isdigit())
print(b.isdigit())
print(c.isdigit())


