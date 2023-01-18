import pandas as pd
df = pd.read_csv('pokemon_data.csv')
loop = True
name_list = []
i = 0
for index, row in df.iterrows():
        name_list.append(df.iloc[i, 1])
        i+=1
def Overall(loop):
   
 
    while loop == True:
 
        usr = str(input("Welcome to the POKEDEX what Pokemon would you like to look up?: "))
        usr =usr.capitalize()

        if usr in name_list:
            print(df.loc[df['Name'] == usr])
        else:
            print("Error please type a valid Pokemon name")

        leave = input("Would you like to exit? (y/n)")
        leave.lower()

        if leave == "y":
            print("Goodbye!")
            loop = False
Overall(loop)
temp = True
def TypeSearch(temp):
    while temp == True:
 
            Type = str(input("Welcome to the POKEDEX Type search what Pokemon Type would you like to look up?: "))
            Type =Type.capitalize()

        
            x = df.loc[((df['Type 1'] == Type) | (df['Type 2'] == Type))]
            print(x.to_string(index = False))
        

            leave = input("Would you like to exit? (y/n)")
            leave.lower()

            if leave == "y":
                print("Goodbye!")
                temp = False
TypeSearch(temp)