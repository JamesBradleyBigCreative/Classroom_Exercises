import pandas as pd

#Pandas reading dataframes and files from outside of the program. CSV FILE< EXCEL FILE< TXT< FILE
df_csv = pd.read_csv('pokemon_data.csv')
df_xlsx = pd.read_excel('pokemon_data.xlsx')
df_txt = pd.read_csv('pokemon_data.txt', delimiter = '\t') #Text files are seperated by tabs so it needs a delimiter to seperate the collums of tabs.

#printing

#print(df_csv)
#print(df_csv.to_string())
#print(df_csv.head(3)) # first 3 items
#print(df_csv.tail(3)) # last 3 items
#print(df_csv.columns) # prints the columns names and values
#print(df_csv['Name'][0:3]) # prints the column Name from values 0-3
#print(df_csv[['Name','Type 1', 'HP']][0:3])
#print(df_csv.iloc[2,1]) # print specific rows and specific location (row,column)

#for index, row in df_csv.iterrows():
#    print(index,row['Name']) # iterates through dataframes and prints the rows. Can specifiy collumn.

#print(df_csv.loc[(df_csv['Type 1'] == 'Fire') & (df_csv['Type 2'] == 'Steel')]) # Find specific information for specific values of rows. using the & you can add multiple conditions, with | you can print multiple values for two or more conditions either.
#print(df_csv.describe())

#SORTING / Describing

#print(df_csv.loc[(df_csv['Type 1'] == 'Fire') & (df_csv['Type 2'] == 'Steel')]) # Find specific information for specific values of rows. using the & you can add multiple conditions, with | you can print multiple values for two or more conditions either.
#print(df_csv.describe())
#print(df_csv.sort_values(['Type 1','HP' ], ascending = [True,False])) # Sorts data in alphabetical order or numerical ascending or descending order, the variable ascending determines if it is ascending or decending.

#Making changes to data / creating a new column

#print(df_csv.head(5))
#df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Defense'] + df_csv['Sp. Atk']+ df_csv['Sp. Def'] +df_csv['Speed'] # this is creating a new column names total and adding all other values of numbers into the total.
#print(df_csv.loc[(df_csv['Total'] >= 700)])
#df_csv = df_csv.drop(columns=['Total'])

#df_csv['Total'] = df_csv.iloc[:,4:10].sum(axis=1) ## reduces the amount of code to sum of more columns


#cols = list(df_csv.columns)
#df_csv = df_csv[cols[0:4] + [cols[-1]]+cols[4:12]]## this code changes position of a column
#for index, row in df_csv.iterrows():

#    print(index,row)

#df_csv = df_csv.drop( ['Total']) ## this removes a column from the dataframe

#SAVING DATA ON SPECIFIED FILES

#df_ammended = df_csv.drop(columns = ['Speed'])## this removes the colum specified
#df_ammended.to_csv('modified_data.csv')## this creates a new csv file. using the modified file
#df_ammended.to_excel('modified_data.xlsx')  ##this creates a new xlsx file. using the modified file
#df_ammended.to_csv('modified_data.txt',sep = "\t")  ##this creates a new txt file. using the modified file

#Filtering DATA



