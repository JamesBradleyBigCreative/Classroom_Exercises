import pandas as pd
import matplotlib.pyplot as plt
#Task 1 

#Reading file
df = pd.read_csv("pokemon_data.csv")

#Setting max rows and cols
pd.options.display.max_rows = 9999999999999999999
pd.options.display.max_columns = 9999999999999999999
print(df)
types = []
summs = []

#Populating list with all type 1
for i in df["Type 1"]:
    if i not in types:
        types.append(i)

df.plot(kind = "area", x="Sp. Atk", y= "Attack")
plt.show()
#usr = input("Enter a pokemon type: ")
#usr = usr.lower()
#usr = usr.capitalize()

#populating list with amount of time each type appears
for i in types:
    summs.append((df["Type 1"] == i).sum())


#creating dataframe from lists and displaying it
d = {'Types': types, 'Totals': summs}
a = pd.DataFrame(d)
a.to_csv("How_manyTypes.csv")

##Task 2

strnth = df['Attack'].groupby(df['Generation']).mean()
#print(strnth)

##Task 3 find average for all attributes
all_average = df[['Attack', 'Defense', 'HP', 'Sp. Atk', 'Sp. Def', 'Speed']].groupby(df['Generation']).mean()
#print(all_average)


#Task 4
df['Total'] = df['Attack'] + df['Defense'] + df['HP'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] 
top_20 = df.sort_values(['Total'], ascending = False).head(20)
#Task 5
bottom_20 = df.sort_values(['Total'], ascending = True).head(20)

#convert to files

strnth.to_csv("Strength.csv")
all_average.to_csv("Strength.csv")
top_20.to_csv("Top.csv")
strnth.to_csv("Bottom.csv")
a.to_csv("How_manyTypes.csv")

