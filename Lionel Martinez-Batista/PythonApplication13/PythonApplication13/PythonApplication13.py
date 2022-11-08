measurementUnit = str(input('Please choose Fahrenheit (F) or Celsius (C): '))
Temp = int(input('Input the temperature you wish to translate: '))

if measurementUnit == 'F' or 'f' or 'Fahrenheit' or 'fahrenheit':
    print((Temp - 32) * 5/9)
    print('Is the equivalent to', Temp, 'in Celsius')
elif measurementUnit == 'C' or 'c' or 'celsuis' or 'Celsius':
    print(Temp * (9/5) + 32)
    print('Is the equivelent to', Temp, 'In Fahrenheit')
else:
    print('Invalid input')