import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon_data.csv")
total1 = -1

pd.options.display.max_rows = 9999


for i in df.index:
    total1 += 1
    
df.plot()
plt.show()
    
print(f"The total Number of Pokemon is {total1} ")


types1 = []
totals = []

for i in df["Type 1"]:
    if i not in types1:
        types1.append(i)

    else:
        ""


for i in types1:
    totals.append((df["Type 1"] == f"{i}").sum())

print("\n")    
d = {'Types':types1,'Totals':totals}

total_types = pd.DataFrame(d)
total_types.to_csv("total_types.csv")
print(total_types)
print()

gen = []
columns1 = ["HP","Attack","Defense","Sp .Atk","Sp .Def"]
averageAtk = []
averageHP = []
averageDef = []
averageSpDf = []
averageSpAt = []

for col in df.columns:
    columns1.append(col)



for i in df["Generation"]:
    if i not in gen:
        gen.append(i)
    else:
        ""



for i in gen:
    averageAtk.append(df.query(f"Generation=={i}")["Attack"].mean())
    averageHP.append(df.query(f"Generation=={i}")["HP"].mean())
    averageDef.append(df.query(f"Generation=={i}")["Defense"].mean())
    averageSpDf.append(df.query(f"Generation=={i}")["Sp. Atk"].mean())
    averageSpAt.append(df.query(f"Generation=={i}")["Sp. Def"].mean())

    
f = {"Generation":gen,"AttackMean":averageAtk,"HpMean":averageHP,"DefMean":averageDef,"SpDfMean":averageSpDf,"SpAt":averageSpAt}


print()
total_average = pd.DataFrame(f)
total_average.to_csv("total_average.csv")
print(total_average)

print()
freq = df['Type 1'].groupby(df['Generation']).value_counts()
freq.to_csv('Freq.csv')
print(freq)


top = df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk']+ df['Sp. Def'] +df['Speed']
top.to_csv("Top.csv")

print(df.sort_values(['Total'], ascending = False).head(20))
print()
print(df.sort_values(['Total'], ascending = False).tail(20))
