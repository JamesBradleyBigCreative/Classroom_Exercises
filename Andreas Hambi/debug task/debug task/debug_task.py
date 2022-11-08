# REMIND YOURSELF OF THE FORMULA FOR CELSIUS FAHRENHEIT CONVERSION BEFORE YOU ATTEMPT THIS 
#Python program to convert Celsius to Fahrenheit and vice-versa

# find temperature in Fahrenheit

def convertFahr(c):  # user-defined function
   c = (c * (9/5)) + 32    
   return c


# find temperature in Celsius
def convertCel(f):  # user-defined function
   f = (f   - 32) * (5/9)
   return f


# select operation
print("Operation: for C to F enter 1, for F to C enter 2, for exit enter 3")
select = int(input("Select operation: "))

while select != 3:
   if select == 1:
       # take inputs
       cel = float(input('Enter temperature in Celsius: '))

       # calling function and display result
       print('%0.1f degrees Celsius is equivalent to %0.1f degrees Fahrenheit' %(cel, convertFahr(cel)))
       select = input("Select operation: ")
   elif select == 2:
       # take inputs
       fahr = float(input('Enter temperature in Fahrenheit: '))

       # calling function and display result
       print('%0.1f degrees Fahrenheit is equivalent to %0.1f degrees Celsius' %(fahr, convertCel(fahr)))
       select = input("Select operations: ")
