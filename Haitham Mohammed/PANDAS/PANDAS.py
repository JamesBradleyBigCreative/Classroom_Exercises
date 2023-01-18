import pandas as pd
#Imports files and reads them according to their data type
df_csv=pd.read_csv('pokemon_data.csv')
#Displays database string-by-string
#print(df_csv.to_string())

#df_xlsx=pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.to_string())

#df_txt =pd.read_csv('pokemon_data.txt', delimiter = '\t')
##Delimeter is used to change tabs found seprated coloumns in a text file and will cover that into a new coloumn
#print(df_txt.to_string())

## prints first 3 items
#print(df_csv.head(100))

##prints last 3 items
#print(df_csv.tail(3))

##prints all columnn titles
#print(df_csv.columns)

##prints all of the items under their name column and specifies specific range from index 0
#print(df_csv[['Name', 'Type 1', 'HP']][0:3])

## gives information for the specified row of the database.
#print(df_csv.iloc[1])

##Using commas it will display the specific item from its row and coloumn
#print(df_csv.iloc[1,2])

#prints full dataframe for index and rows, you can specify what column you want to display
#for index, row in df_csv.iterrows():
#print(index,row['Name'])


# Displays all rows that contain a specific value , you can specify multiple requirements and/or sepreately search for multiple requirements
#print(df_csv.loc[(df_csv['Type 1'] == 'Grass') & (df_csv['Type 2'] == 'Poison')])

#Soring the data alphabetically and numerically
#print(df_csv.sort_values(['Type 1','Speed'] , ascending = [True,False]))

#creating a Totals column
df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Sp. Atk'] + df_csv['Sp. Def']+ df_csv['Speed'] +  df_csv['Defense']

#removes a column from dataframe
df_amended = df_csv = df_csv.drop(columns = ['Total'])
print(df_csv)
# creates and converts dataframe into different files
df_amended.to_csv('modified_data.csv')
df_amended.to_excel('modified_data.xlsx')
df_amended.to_csv('modified_data.txt', sep = '\t')