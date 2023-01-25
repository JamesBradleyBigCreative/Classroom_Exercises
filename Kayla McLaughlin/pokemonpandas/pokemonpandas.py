import pandas as pd


pd.options.display.max_rows = 9999
pd.options.display.max_columns = 9999

potato = pd.read_csv('pokemon_data.csv') 

#print(df_csv)

total_types = potato['Type 1'].value_counts()

attack_by_generation = potato['Attack'].groupby(potato['Generation']).mean()

average_stats = potato[['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'HP']].groupby(potato['Generation']).mean()

top_10 = potato.sort_values(['Attack'], ascending = False).head(10)

bottom_10 = potato.sort_values(['Attack'], ascending = False).tail(10)


total_types.to_csv('total_types_database.csv') # saves the new database to a csv file
attack_by_generation.to_csv('average_stats_database.csv')
average_stats.to_csv('average_stats_database.csv')
top_10.to_csv('top_10_database.csv')
bottom_10.to_csv('bottom_10_database.csv')