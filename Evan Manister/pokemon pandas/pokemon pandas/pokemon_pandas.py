import pandas as pd

#df_csv = pd.read_csv('pokemon_data.csv')

pd.options.display.max_rows = 9999
pd.options,display.max_columns = 9999

# Reads .CSV file and stores data in dataframe
df = pd.read_csv('pokemon_data.csv')

# Creating new columns / data for the dataframe
#df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Defense'] + df_csv['Sp .Atk'] + df_csv['Sp. Def]

#df_amended = df_csv.drop(columns = ['Speed'])

#for index, row in df_csv.iterrows():
#    print(index, row)
#    print('\n')

#df_ammended.to_csv('modified_data.csv')
#df_ammended.to_excel('modified_data.xlsx)
#df_ammended.to_csv('modified_data.txt', sep = '\t')

#Task 1 
#This creats all the different types of pokemon
total_types = df['Type 1'].value_counts()

#Task 2 
#Sorts out each attack, by the different generation of what the pokemon is
attack_by_generation = df['Attack'].groupby(df['Generation']).mean()

#Task 3 
#This gives you the average stats for each trait; so attack, defence etc
average_stats = df[['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'HP']].groupby(df['Generation']).mean()

#Task 4 
#Gives you the top 10 values for the 'attack' trait
top_10 = df.sort_values(['Attack'], ascending = False).head(10)

#Task 5 
#Gives you the bottom 10 values for the 'attack' trait
bottom_10 = df.sort_values(['Attack'], ascending = False).tail(10)

#SAVING NEW DATABASE
total_types.to_csv('total_types_database.csv')
attack_by_generation.to_csv('attack_by_generation_database.csv')
average_stats.to_csv('average_stats_database.csv')
top_10.to_csv('top_10_database.csv')
bottom_10.to_csv('bottom_10_database.csv')    