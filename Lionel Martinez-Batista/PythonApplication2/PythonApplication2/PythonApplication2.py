def Num():
    int(input('Enter your first number: '))

def Num2():
    int(input('Enter your second number'))

def operation():
    str(input('Enter operator'))


if operation == '+':
    print (Num + Num2)
elif operation == '-':
    print (Num - Num2)
elif operation == '/':
    print (Num / Num2)
elif operation == '*':
    print (Num * Num2)

operation()