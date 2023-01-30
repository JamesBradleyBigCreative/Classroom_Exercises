import pandas as pd
from os import path
looping = True
# Checks if Dataframe exists
def File_check():
    a = True
    while a == True:
        if path.exists("data.csv") == True:
            return True
        else:
            return False
    
File_check()
exists = File_check()
print(exists)

def dataframe(exists, looping):
   if exists == False:
      data = {
        "Name": [],
        "Age": [],
        "D.O.B": [],
        "Country of origin": []
      }
      df = pd.DataFrame(data)
      df.to_csv("data.csv")
     
      while looping == True:

        name = input("Enter your name: ")
        name.capitalize

        data["Name"].append(name)

        age = int(input("Enter your age: "))
        data["Age"].append(age)

        DOB = input("Enter your Date of Birth: ")
        data["D.O.B"].append(DOB)

        country = input("Enter your country of origin: ")
        country.capitalize()
        data["Country of origin"].append(country)
        finish = input("Would you like to finish the database: ")
        finish.capitalize()
        if finish == "Y" or finish == "Yes":
            df.to_csv("data.csv")
            print(data)
            looping = False
        else:
            dataframe(exists, looping)
   elif exists == True:


            
dataframe(exists, looping)




