import pandas as pd

## reads the csv file from the project file
df_csv = pd.read_csv('pokemon_data.csv') 

## reads the xlsx file from the project file
df_xlsx = pd.read_excel('pokemon_data.xlsx')

## reads the txt file as a csv file because the text file has columns broken
## up by tabs. the delimiter seperates the file after each tab
df_txt = pd.read_csv('pokemon_data.txt',delimiter = '\t')

## prints contents of the dataframe
print(df_csv)

## prints the top however many given rows of the data frame
print(df_csv.head(13))

## prints the top however many given rows of the data frame
print(df_csv.tail(3))

## prints the headings for each column
print(df_csv.columns)

## prints specified column data
print(df_csv[['Name','Type 1','HP']][144:148])

## Prints specified row(s) (SPECIFIC LOCATION (ROW, COLUMN))
print(df_csv.iloc[526:528,1])

## Iterate through rows, that contain specified info

for index, row in df_csv.iterrows():
    print(index,row['Name'])
    print('\n')

print(df_csv.loc[((df_csv['Type 1'] == 'Ground') | (df_csv['Type 1'] == 'Rock')) & ((df_csv['Type 2'] == 'Ground') | (df_csv['Type 2'] == 'Rock'))])


## Sorting the data
print(df_csv.sort_values(['Type 1','Speed'], ascending = [True,False]))

## Creating new columns / data for the dataframe

df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Defense'] + df_csv['Sp. Atk'] + df_csv['Sp. Def'] + df_csv['Speed']

## Deleting new columns / data for the dataframe

df_csv = df_csv.drop(columns = ['HP'])

## Making a new data frame that is Csv without a specific column

df_AA = df_csv.drop(columns = ['HP'])

## Creating the new file
df_AA.to_csv('modified_data.csv')
df_AA.to_excel('modified_data.xlsx')
df_AA.to_csv('modified_data.txt', sep = '\t')

for index, row in df_csv.iterrows():
    print(index,row)
    print('\n')
