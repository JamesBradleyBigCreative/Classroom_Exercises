choice = input("what would you like to convert. Type C or F")



def celcius():
    f = float(input("enter temperature in farenheit"))
    c = (f - 32) * 5/9
    print(c)


def farenheit():
    c = float(input("enter temperature in celcius"))
    f = c * 9/5 + 32
    print(f)



if choice == "F":
    celcius()

elif choice == "C":
    farenheit()

else:
    print("Error: Please try again")