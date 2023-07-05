
import pandas as pd
import os.path
file_exists = os.path.exists("Person_Data.csv")
if not file_exists:

    Data = {
        "Name": [],
        "Age": [],
        "D.O.B.": [],
        "Country of origin": []
        
    }
    x = pd.DataFrame(Data)
    x.to_csv("Person_Data_csv", index = False)
    quit()

x = pd.read_csv("Person_Data")


Data ={
    "Name": input("Enter name: "),
    "Age": input("Enter Age: "),
    "D.O.B": input("Enter date of birth: "),
    "Country of origin": input("Enter Country of origin: ")
}

x.append(Data, ignore_index = True)
print(Data)
x.to_csv("Person_Data.csv", index = False)


