import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 999
# Returns an integer of the total number of pokemon
def Task1_Pt1():
    df_csv = pd.read_csv("pokemon_data.csv")
    total_types = df_csv['Type 1'].value_counts()
    return total_types

# Returns a list of the number of pokemon from each type
def Task1_Pt2():
    #types = ["Normal","Fire","Water","Grass","Electric","Ice","Fighting",
    #         "Poison","Ground","Flying","Psychic","Bug","Rock","Ghost",
    #         "Dark","Dragon","Steel","Fairy"]
    #totals = []
    #for item in types:
    #    df_csv = pd.read_csv("pokemon_data.csv")
    #    df_csv = df_csv.loc[(df_csv['Type 1'] == item)]
    #    total_num_of_poke = len(df_csv.index)
    #    totals.append(total_num_of_poke)
    df_csv = pd.read_csv("pokemon_data.csv")
    freq = df_csv['Type 1'].groupby(df_csv['Generation']).value_counts()
    return freq

# Returns a list of each of the average stats of each generation
def Task2():
    #stats = ['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']
    #totals = []
    #for item in stats:
    #    df_csv = pd.read_csv("pokemon_data.csv")
    #    #x = df_csv.loc[(df_csv['Generation'] == i)]
    #    #df_csv = x[item]
    #    #y = df_csv.mean()
    #    #to_append = [i, float(df_csv.mean())]
    #    strength = df_csv[item].groupby(df_csv['Generation']).mean()
    #    #totals.append(strength)
    df_csv = pd.read_csv("pokemon_data.csv")
    avg_strength = df_csv[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']].groupby(df_csv['Generation']).mean()
    return avg_strength

# Returns a list of the 20 pokemon with the highest Attack
def Top_20_Strongest():
    #top_20 = []
    #top_20_names = []
    #df_csv = pd.read_csv("pokemon_data.csv")
    #df_csv = df_csv.sort_values(['Attack'], ascending = False)
    #df_csv = df_csv.head(20)
    #y = df_csv['Attack'].tolist()
    #for index,value in df_csv.iterrows():
    #    to_add = [
    #        value['Name'],value['Type 1'],value['Type 2'],value['Generation']]
    #    top_20.append(to_add)
    #    temp = value['Name'].split()
    #    top_20_names.append(temp[0])
    df_csv = pd.read_csv("pokemon_data.csv")
    top_20 = df_csv.sort_values(['Attack','HP','Defense'], ascending = False).head(20)

    ## Creating a bar graph of the top 20 pokemon
    #xaxis = np.array(top_20_names)
    #yaxis = np.array(y)

    #f = plt.figure()
    ##plt.hist(xaxis, rwidth=0.7)

    #manager = plt.get_current_fig_manager()
    #manager.window.state('zoomed')

    ##plt.ylabel('Attack')
    ##plt.xlabel('Names')
    ##plt.figure(figsize=(20, 3))  # width:20, height:3
    #plt.bar(xaxis, yaxis, width=0.2)
    #plt.xticks(xaxis, rotation='vertical')
    #plt.show()

    return top_20

total_types = Task1_Pt1()
attack_by_generation = Task1_Pt2()
average_stats = Task2()
top_20 = Top_20_Strongest()

total_types.to_csv('total_types_database.csv')
attack_by_generation.to_csv('attack_by_generation_database.csv')
average_stats.to_csv('average_stats_database.csv')
top_20.to_csv('top_20_database.csv')