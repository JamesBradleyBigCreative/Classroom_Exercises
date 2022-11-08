##-----------------------------------------------------------------------------
##Prescence Check: Checking if data has been entered into a field/ is not blank
##-----------------------------------------------------------------------------

#x = input("Enter your name: ")

#while len(x) == 0:
    #print("\nNO DATA ENTERED")
    #x = input("\nEnter your name: ")

#print(f"\nHello {x}")

##----------------------------------------------------------------------------------------------
##Length Check: Checking if data that has been entered into a field is the length that is wanted
##----------------------------------------------------------------------------------------------

#temp = input("Enter A 7 Letter Word: ")

#while len(temp) != 7:

    #print("\nDATA IS NOT 7 CHARACTERS LONG")

    #print(f"{temp} IS {len(temp)} CHARACTERS LONG")

    #temp = input("\nEnter A 7 Letter Word: ")

#print(f"\nWell Done {temp} is 7 letters")

##------------------------------------------------
##Type Check: Checking the data type of a variable
##------------------------------------------------

#var = True

#print(var)
#print(type(var))

#print("Is Bool",isinstance(var,bool))
#print("Is Int",isinstance(var,int))

##-------------------------------------------------------
##Format Check: Checks if the data is in the right format
##-------------------------------------------------------

#Imports regular expressions
#import re

#email = input("Enter your email: ")

# Pattern is the accepted format 
#[A-Za-z0-9] is the acceptable inputs for each section A-Z letters, a-z letters, and 0-9 digits

#pattern = "^[A-Za-z0-9]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+$"

#re.match() function of re in Python will search the regular expression pattern and return the first occurrence
#re.search() function will search the regular expression pattern and return the first occurrence. Unlike Python re.match(), it will check all lines of the input string.

#emailMatch = re.search(pattern,email)

#print(dir(re.Match))

#if emailMatch:
    #print("Valid")
    #print(emailMatch)
    #print(emailMatch.groups())
#else:
    #print("Invalid")
    #print(emailMatch)

##---------------------------------------------------------------------
##Range Check: Checks if the data value falls between a specified range
##---------------------------------------------------------------------

#score = int(input("Enter Your Score: "))

#if score >= 80 and score <= 100:
    #print("You Get An A")

#elif score >= 60 and score < 80:
    #print("You Get An B")

#elif score >= 45 and score < 60:
    #print("You Get An C")

#elif score < 45 and score >= 0:
    #print("You Get An F")

#elif score < 0 or score > 100:
    #print("IMPOSSIBLE")

##--------------------------------------------------------------------------------------------------
##Check Digit: Checks if the data entered is a number if its a string (doesnt work with floats)
##--------------------------------------------------------------------------------------------------

#a = ["qw","weew","3434"]
#b = "567765567"

#for i in a:
    #print(i.isdigit())
    
#print(b.isdigit())