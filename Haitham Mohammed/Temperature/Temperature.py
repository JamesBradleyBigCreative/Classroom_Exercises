usr = input("Do you want to convert c to f or f to c (c/f)  ")

def Celcius():
    celcius = int(input("Enter temperature in Degrees Celcius: "))
    celcius = celcius * 0.55555555555
    celcius = celcius + 32
    print(f"{celcius} degrees farenheit")




def Fareheit():
    farenheit = int(input("Enter temperature in Degrees Fareheit: "))
    farenheit = farenheit - 32
    farenheit = farenheit * 0.55555555555
    print(f"{farenheit} degrees celcius")





if usr == "c":
   Celcius()
elif usr == "f":
    Fareheit()





