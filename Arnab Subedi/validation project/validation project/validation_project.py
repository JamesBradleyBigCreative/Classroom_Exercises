
def validation():
    name = input("please enter your Full name: ")
    dob = input("please enter your date of birth: ")
    phone = input("please enter your phone number: ")
    address = input("enter your address: ")
    postcode = input("enter your postcode: ")
    a = False
    while a == False:
        if len(name) == 0:
            print("Name cannot be empty:")
            name = input("please enter your Full name: ")
        else:
            print("NAME ACCEPTED!")
            a = True

    b = False
    while b == False:
        import re
        rex = re.compile("^[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]$")
        if rex.match(dob):
            print("DATE OF BIRTH ACCEPTED!")
            b = True
        else:
            print("Dob not in the correct format it must be 00/00/0000")
            dob = input("please enter your date of birth: ")
    c = False
    while c == False:
        pat = re.compile("^[07]+[0-9]+$")
        if len(phone) == 11 and pat.match(phone):
            print("Phone number accepted! ")
            c = True
        elif len(phone) == 10 and pat.match(phone):
            print("Phone number accepted! ")
            c = True
        else:
            print("Phone number should be 11 digits or 10 ditits without the 0! and should start with 07 ")
            phone = input("please enter your phone number: ")
    d = False
    while d == False:
        form = re.compile("^[0-9]+[ ]+[A-Za-z]+[ ]+[A-Za-z]+$")
        if len(address) != 0 and form.match(address):
            print("ADDRESS ACCPETED!")
            d = True
        else:
            print("Address cannot be empty!")
            address = input("enter your address: ")
    e = False
    while e == False:
        if len(postcode) >=6 and len(postcode) <=8:
            print("Postcode accepted!")
            e = True
        else:
            print("Postcode has to be in between 6-8 characters!")
            postcode = input("enter your postcode")
    f = open(f"{name}.txt","w")
    f.write(f"NAME: {name}\n")
    f.write(f"DATE OF BIRTH : {dob}\n")
    f.write(f"PHONE: {phone}\n")
    f.write(f"ADDRESS: {address}\n")
    f.write(f"POSTCODE: {postcode}\n")
            
validation()



        

