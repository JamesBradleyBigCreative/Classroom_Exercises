import pandas as pd

df = pd.read_csv('pokemon_data.csv')

user = input("Enter Pokemon?: ")

print(df.loc[(df['Name'] == user)])