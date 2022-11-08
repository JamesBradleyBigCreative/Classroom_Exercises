print("f = farenheight \nc = celcius ")
user_in = input("do you want to convert f-c or c-f: ")

def farenheight():
    f = float(input("enter your celcius to convert to farenheight: "))
    c = (f-32)*5/9
    print(f" Your conversion gives {c} celcius")


def celcius():
    c = float(input("enter your farenheight to convert to celcius: "))
    f = c * 9/5 + 32
    print(f" Your conversion gives {f} celcius")

if user_in == "f-c" :
    farenheight()
elif user_in == "c-f":
    celcius()
else: 
    exit()
    