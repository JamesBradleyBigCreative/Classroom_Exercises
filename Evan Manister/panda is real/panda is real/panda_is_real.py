import modified_data.txt as pd 

#adding delimiter means that the tag is a new line which won't output everything as a straight line

#Reads .CSV file and stores data in dataframe
df_csv = pd.read_csv('pokemon_data.csv')

#Reads .XLSX file and stores data in dataframe   
#df_xlsx = pd.read_excel('pokemon_data.xlsx')

#Reads .TXT file, sets Delimiter as TAB and stores data in dataframe
#df_txt = pd.read_csv('pokemon_data.txt', delimiter = '\t')

#Prints the contents of the data frame
#print(df_csv)  # Whole file
#print(df_csv.head(3)) # First three items
#print(df_csv.tail(3)) # Last three items

# Prints the headings for each column
#print(df_csv.columns)

#Prints specified column data
#print(df_csv[['Name', 'Type 1', 'HP']][0:3])

#Print specified row(s) (Specific Location (ROW, COLUMN))
#print(df_csv.iloc[2,1])

# Iterating through rows 
#for index, row in df_csv.iterrows():
    #print(index, row['HP'])
    #print('\n')    

#Interacting through rows, that contain specified information 
#print(df_csv.loc[(df_csv['Type 1']== 'Fire') | (df_csv['Type 1']== 'Steel')])

# Sorting the data 
#print(df_csv.sort_values(['Type 1', 'HP'], ascending = [True, False]))

# Creating new columns / data for the dataframe 
#df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Defense'] + df_csv['Sp. Atk'] + df_csv['Sp. Def'] + df_csv['Speed']


#df_amended = df_csv.drop(columns = ['Sp. Atk'])


#for index, row in df_csv.iterrows():
#    print(index, row)
#    print('\n')

#df_amended.to_csv('modified_data.csv')
#df_amended.to_excel('modified_data.xlsx')
#df_amended.to_csv('modified_data. txt', sep = '\t')