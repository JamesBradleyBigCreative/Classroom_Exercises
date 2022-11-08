f = open("Kayla.txt" , "r")
print(f.read())

def PrintsReciept(name, accnum, bal):
    reciept = open("reciept.txt", "w")

    f.write(name, "this is your reciept \n", "new balance: ", bal)

    print(f.read)