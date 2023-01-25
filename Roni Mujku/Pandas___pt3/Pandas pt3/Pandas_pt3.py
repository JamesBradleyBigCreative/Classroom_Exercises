import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 999

# Returns an dataframe of the total number of pokemon in each type
def Task1_Pt1():
    df_csv = pd.read_csv("pokemon_data.csv")
    # Counts the number of values in each type in the data base
    #total_types = pd.DataFrame(columns=['Type','Total'])
    total_types = df_csv['Type 1'].value_counts().rename_axis('Type').reset_index(name='Total')
    print(total_types)
    return total_types

# Returns a dataframe of the total attack from each generation
def Task1_Pt2():
    df_csv = pd.read_csv("pokemon_data.csv")
    # Counts the total attack grouped by generation
    freq = df_csv['Attack'].groupby(df_csv['Generation']).value_counts()
    return freq

# Returns a dataframe of each of the average stats of each generation
def Task2():
    df_csv = pd.read_csv("pokemon_data.csv")
    # Creates a new database of the means of each stat grouped by each generation
    avg_strength = df_csv[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']].groupby(df_csv['Generation']).mean()
    return avg_strength

## Returns a dataframe of the 20 pokemon with the highest Attack
def Top_20_Strongest():
    df_csv = pd.read_csv("pokemon_data.csv")
    # Sorts the database by given stats in descending order
    # and creates a new data frame of the top 20 pokemon
    top_20 = df_csv.sort_values(['Attack','HP','Defense'], ascending = False).head(20)

    return top_20


total_types = Task1_Pt1()
#attack_by_generation = Task1_Pt2()
#average_stats = Task2()
#top_20 = Top_20_Strongest()

total_types.to_csv('total_types_database.csv')
#attack_by_generation.to_csv('attack_by_generation_database.csv')
#average_stats.to_csv('average_stats_database.csv')
#top_20.to_csv('top_20_database.csv')

total_types = pd.read_csv('total_types_database.csv')
print(total_types)
total_types.plot(kind='scatter',x='Type',y='Total',color='red')
plt.show()