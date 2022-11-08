P1 = {
    "Number": 174,
    "Name": "Carol Taylor",
    "Missing teeth": 0,
    "Fillings": 11,
    "Private patient": "Y",
    "Risk score": 0,
    "Emergency appointment": None
    }
P2 = {
    "Number": 203,
    "Name": "Janet Williams",
    "Missing teeth": 1,
    "Fillings": 2,
    "Private patient": "Y",
    "Risk score": 0,
    "Emergency appointment": None
}
P3 = {
    "Number": 365,
    "Name": "Annette Loyd",
    "Missing teeth": 3,
    "Fillings": 7,
    "Private patient": "N",
    "Risk score": 0,
    "Emergency appointment": None
    }



patients = [P1, P2, P3]

teeth= int(input("Enter amount of missing teeth: "))
fill= int(input("Enter amount of fillings: "))
calc1 = teeth * 5
calc2 = fill * 2



if  calc1 + calc2 :
    patients[0][6] = True
else:
    patients[0][6] = False

teeth1 = int(input("Enter amount of missing teeth:"))
fill1 = int(input("Enter amount of fillings:"))
calc3 = teeth1 * 5
calc4 = fill1 * 2
if calc3 + calc4  > 15:
        patients[1][6] = True
else:
        patients[1][6] = False

print(patients[0][6])
print(patients[1][6])
print(patients)
