def convertFahr(c):
   f = (c * (9/5)) + 32    
   return f

def convertCel(f):
   c = (f - 32) * (5/9)
   return c

print("Operation: for C to F enter 1, for F to C enter 2, for exit enter 3")
select = int(input("Select operation: "))
Flag = True
while Flag == True:
   if select == 1:
       cel = float(input('Enter temperature in Celsius: '))

       print('%0.1f degrees Celsius is equivalent to %0.1f degrees Fahrenheit' %(cel, convertFahr(cel)))
       select = int(input("Select operation: "))
   elif select == 2:
       fahr = float(input('Enter temperature in Fahrenheit: '))

       print('%0.1f degrees Fahrenheit is equivalent to %0.1f degrees Celsius' %(fahr, convertCel(fahr)))
       select = int(input("Select operation: "))
   elif select == 3:
       print("Exiting......")
       Flag = False
   else:
       print("Invalid selection")
       select = int(input("Select operation: "))
