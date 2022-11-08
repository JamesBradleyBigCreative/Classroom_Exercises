import re 

# PRESENCE CHECK - checks that data that has been entered and is not a blank field.
#name = input(" Please Enter Your Name: ")

#while len(name) == 0:
 #   print("invalid input.")
  #  name = input(" Please Enter Your Name: ")


# LENGTH CHECK - checks that the data isn't to long or short.
#pin = input("Enter your 4 digit pin: ")

#while len(pin) != 4:
    #print("\n")
    #print("That is " + str(len(pin)) + " characters , please try again! ")
    #pin = input("Enter your 4 digit pin: ")

#print("\n")
#print("Congratulations. Access Granted.")

# TYPE CHECK - checks what kind of data is stored in that variable

#data = "helloooo"

#print(data)
#print(type(data))

# Type check pt. 2
#print("is string: ", isinstance(data, str ))
#print("is integer: ", isinstance(data, int ))
#print("is float: ", isinstance(data, float ))

# FORMAT CHECK - checks that the data is in the right format.

#email = input("Enter Email Address: ")
#pattern = "^[A-Za-z0-9.]+\@[A-Za-z0-9]+\.[A-Za-z0-9]+$"
#emailMatch = re.match(pattern, email)

#if emailMatch:
 #   print("this is a valid email.")
#else:
  #  print("invalid email.")

# RANGE CHECK - checks the data falls between a specified range.
score = int(input("Please enter your score: "))

# or 
 

if score <= 39:
    print("You did not Pass")
elif score >= 40 & score <= 100:
    print("you have passed")

#CHECK DIGIT - checks that the data entered is a number#

a = "22"
b = "twentytwo"
c= "20two"

print(a.isdigit())
print(b.isdigit())
print(c.isdigit())