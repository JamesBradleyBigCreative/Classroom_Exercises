import re

name = input("Enter your name: ")


f = open("TXT.txt","w")
f.write("_________________")
f.close()

def NameChecks(name):
    Flag = True
    while Flag == True:

        while len(name) == 0:
            print("\nERROR NO INPUT")
            name = input("\nEnter your name: ")

        if isinstance(name,str) == True:

            pattern = "^[A-Za-z-]+$"
            nameMatch = re.search(pattern,name)

            if nameMatch:
                print("\nName Input Succesful")
                f = open("TXT.txt","a")
                f.write(f"\n{name}")
                Flag = False
            else:
                print("\nERROR NAME FORMAT INCORRECT")
                name = input("\nEnter your name: ")

NameChecks(name)

#-------------------------------------------------------------------------

DoB = input("\nEnter your Date of Birth: ")

def DoBChecks(DoB):
    Flag = True
    while Flag == True:

        while len(DoB) == 0:
            print("\nERROR NO INPUT")
            DoB = input("\nEnter your Date of Birth: ")

        if isinstance(DoB,str) == True:

            pattern = "^[0-9]+\/[0-9]+\/[0-9]+$"
            DoBMatch = re.search(pattern,DoB)

            if DoBMatch:
                temp = DoB.split("/")
                if int(temp[2]) > 2022 or int(temp[0]) > 31 or int(temp[1]) > 12:

                    print("\n INVALID DATE OF BIRTH")
                    DoB = input("\nEnter your Date of Birth: ")
                else:
                    print("\nDate of Birth Input Succesful")
                    f = open("TXT.txt","a")
                    f.write(f"\n{DoB}")
                    Flag = False
            else:
                print("\nERROR DATE OF BIRTH FORMAT INCORRECT")
                DoB = input("\nEnter your Date of Birth: ")

DoBChecks(DoB)

#-------------------------------------------------------------------------

PhoneNum = input("\nEnter your Phone Number: ")

def PhoneChecks(PhoneNum):
    Flag = True
    while Flag == True:

        while len(PhoneNum) == 0:
            print("\nERROR NO INPUT")
            PhoneNum = input("\nEnter your Phone Number: ")

        if PhoneNum.isdigit() == True:

            pattern = "^[0-9]+$"
            PhoneMatch = re.search(pattern,PhoneNum)

            if PhoneMatch:

                if len(PhoneNum) != 11:

                    print("\n INVALID PHONE NUMBER")
                    PhoneNum = input("\nEnter your Phone Number: ")

                else:
                    print("\nPhone Number Input Succesful")
                    f = open("TXT.txt","a")
                    f.write(f"\n{PhoneNum}")
                    Flag = False

            else:
                print("\nERROR PHONE NUMBER FORMAT INCORRECT")
                PhoneNum = input("\nEnter your Phone Number: ")

PhoneChecks(PhoneNum)

#-------------------------------------------------------------------------

Postcode = input("\nEnter Your Postcode: ")

def PostCodeChecks(Postcode):
    Flag = True
    while Flag == True:

        while len(Postcode) == 0:
            print("\nERROR NO INPUT")
            Postcode = input("\nEnter your Post Code: ")

        if isinstance(Postcode,str) == True:

            pattern = "^[NESW][0-9A-Z]+\s[0-9][A-Z][A-Z]+$"
            PostMatch = re.search(pattern,Postcode)

            if PostMatch:
                temp = Postcode.split(" ")

                if (len(temp[0]) <= 4 and len(temp[1]) >= 2) and (len(temp[1]) == 3):

                    print("\nPost Code Input Succesful")
                    f = open("TXT.txt","a")
                    f.write(f"\n{Postcode}")
                    Flag = False

                else:
                    print("\n INVALID POST CODE")
                    Postcode = input("\nEnter your Post Code: ")

            else:
                print("\nERROR POST CODE FORMAT INCORRECT")
                Postcode = input("\nEnter your Post Code: ")

        else:
            print("ERROR")
            Postcode = input("\nEnter your Post Code: ")

PostCodeChecks(Postcode)

#-------------------------------------------------------------------------

Address = input("\nEnter your Address(House Number And Street Name): ")

def AddressChecks(Address):
    Flag = True
    while Flag == True:

        while len(Address) == 0:
            print("\nERROR NO INPUT")
            Address = input("\nEnter your Address: ")

        if isinstance(Address,str) == True:

            pattern = "^[0-9][0-9]+\s[A-Za-z]+\s[A-Za-z]+$"
            AddressMatch = re.search(pattern,Address)

            if AddressMatch:
                print("\nAddress Input Succesful")
                f = open("TXT.txt","a")
                f.write(f"\n{Address}")
                Flag = False

            else:
                print("\nERROR ADDRESS FORMAT INCORRECT")
                Address = input("\nEnter your Address: ")

        else:
            print("ERROR")
            Address = input("\nEnter your Address: ")

AddressChecks(Address)

#-------------------------------------------------------------------------

