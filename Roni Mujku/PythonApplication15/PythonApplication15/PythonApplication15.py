def FtoC(Input):
    C = (Input-32) * (5/9)
    return C

def CtoF(Input):
    F = (Input*(9/5)) + 32
    return F

Start = input("Press F to convert to fahrenheit or Press C to convert to celcius: ")
if Start == 'F' or Start == 'f':
    x = float(input("Enter Your Temp in celcius: "))
    print(CtoF(x))
elif Start == 'C' or Start == 'c':
    x = float(input("Enter Your Temp in fahrenheit: "))
    print(FtoC(x))
