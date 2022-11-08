#name = str(input("please enter a name:"))
#while len(name) == 0:
    #print("Error you did not enter a name")
    

#print("Thank you " + name + " for entering your name")

#variable at the beginning stores the name variable
#when name is mentioned in the code involving + the user input is added

#word = input("Please enter a 4 letter word :")

#while len(word) != 4:
    #print("\n")
    #print("That is " + str(len(word)) + " letters, please try again")

#print("\n")
#print("well done " +word+ " is a 4 letter word")


#data = "hello"
#print(data)
#print(type(data))

#print("Is String:", isinstance(data,str))
#print("Is Float:" , isinstance(data,float))
#print("Is Int:" , isinstance(data,int))
#print("Is Boolean:" , isinstance(data,bool))

#import re
#email = input("Enter an email address: ")
#pattern = "^[A-Za-z0-9.]+\@[A-Za-z0-9.]+\.[A-Za-z0-9.]+$"
#emailMatch = re.match(pattern, email)

#if emailMatch:
    #print("This is a valid email format")
#else:
    #print("This is an invalid email format")

#The code checks the 


#score = int(input("Please enter your score: "))

#if score <= 39:
    #print("You failed the exam")
#elif score >= 40 & score <= 100:
    #print("You have passed the exam")

#a = "2022"
#b = "twentytwentytwo"
#c = "20twenty2"


#print(a.isdigit())
#print(b.isdigit())
#print(c.isdigit())




# importing the module




import re 

name = input("Enter your name:")
def NameCheck (name):
    while len(name) == 0:
        print("Invalid name")
        name = input("Enter your name:")
    else:
        print("valid name")

NameCheck(name)

def DOBCheck (DOB):
    DOB = input("enter your date of birth")
    pattern = "^[0-9]"

   


DOB =  input("enter your date of birth:")

phone_number = input("enter your phone number:")
address = input("enter your address:")
postcode = input("enter your postcode:")
print(name,DOB,phone_number,address,postcode)


