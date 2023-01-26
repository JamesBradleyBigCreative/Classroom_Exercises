import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 999

# Returns an dataframe of the total number of pokemon in each type
def Task1_Pt1():
    df_csv = pd.read_csv("pokemon_data.csv")
    # Counts the number of values in each type in the data base
    #total_types = pd.DataFrame(columns=['Type','Total'])
    total_types = df_csv['Type 1'].value_counts().rename_axis('Type').reset_index(name='Total')
    return total_types

def total_type2():
    df_csv = pd.read_csv("pokemon_data.csv")
    total_types = df_csv['Type 2'].value_counts().rename_axis('Type').reset_index(name='Total')
    return total_types

# Returns a dataframe of the total attack from each generation
def Task1_Pt2():
    df_csv = pd.read_csv("pokemon_data.csv")
    # Counts the total attack grouped by generation
    freq = df_csv['Attack'].groupby(df_csv['Generation']).sum()
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

def scatter_of_pokemon_per_type():
    total_types = pd.read_csv('total_types_database.csv')
    total_types = total_types.drop(["Unnamed: 0"], axis=1)

    total_types2 = pd.read_csv('total_types2_database.csv')
    total_types2 = total_types2.drop(["Unnamed: 0"], axis=1)

    ax1 = total_types.plot(kind='scatter',x='Type',y='Total',color='Blue', label = 'Type 1',rot=90)
    total_types2.plot(kind='scatter',x='Type',y='Total',color='Red',label = 'Type 2',rot=90, ax = ax1)
    plt.show()

def bar_of_attack_by_gen():
    gen_attacks = pd.read_csv('attack_by_generation_database.csv')
    gen_attacks.plot(kind = 'bar',x = 'Generation', y = 'Attack', color = 'Gold', rot=0)
    plt.show()

def pies_of_stats_by_gen():
    avg_stats = pd.read_csv('average_stats_database.csv')

    values = avg_stats.iloc[0:6].values.tolist()[0] # average numbers
    labels = [x for x in avg_stats.columns] # stats
    title = int(avg_stats.iloc[0].values.tolist()[0]) # generation
    values.pop(0)
    labels.pop(0)

    #fig, ax = plt.subplots(figsize=(10, 7), facecolor='#e8f4f0')
    #ax.pie(values, labels=labels, colors=colors,autopct = '%1.2f%%', startangle=30, textprops={'color':font_color})
    #title = plt.title(title, fontsize=16, color=font_color)
    #title.set_position([.5, 1.02])
    #plt.rcParams['font.size'] = 16.0
    #plt.show()

    font_color = '#525252'
    colors = ['#f7ecb0', '#ffb3e6', '#99ff99', '#66b3ff', '#c7b3fb','#ff6666', '#f9c3b7']
    fig, axes = plt.subplots(2,3, figsize=(10, 10), facecolor='#e8f4f0')
    new_avg_stats = avg_stats.drop("Generation", axis='columns')

    for i , (column, row) in enumerate(new_avg_stats.iterrows()):
        ax = axes[i // 3, i % 3]
        ax.pie(row, 
                   labels=row.index, 
                   startangle=30, 
                   colors=colors,
                   radius = 1.4,
                   autopct = '%0.1f%%',
                   textprops={'color':font_color,'fontsize': 9})
        ax.set_title(column + 1, fontsize=11, color=font_color, pad = 20)

    fig.subplots_adjust(wspace=1) # Space between charts

    title = fig.suptitle('Average of Stats in Each Generation', y=.95, fontsize=20, color=font_color)
    # To prevent the title from being cropped
    plt.subplots_adjust(top=0.85, bottom=0.15)

    plt.show()

#total_types = Task1_Pt1()
#attack_by_generation = Task1_Pt2()
#average_stats = Task2()
#top_20 = Top_20_Strongest()
#total_types2 = total_type2()

#total_types.to_csv('total_types_database.csv')
#total_types2.to_csv('total_types2_database.csv')
#attack_by_generation.to_csv('attack_by_generation_database.csv')
#average_stats.to_csv('average_stats_database.csv')
#top_20.to_csv('top_20_database.csv')

#print(average_stats)
scatter_of_pokemon_per_type()
bar_of_attack_by_gen()
pies_of_stats_by_gen()