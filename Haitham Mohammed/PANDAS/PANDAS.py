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
#df_csv['Total'] = df_csv['HP'] + df_csv['Attack'] + df_csv['Sp. Atk'] + df_csv['Sp. Def']+ df_csv['Speed'] +  df_csv['Defense']

##removes a column from dataframe
#df_amended = df_csv = df_csv.drop(columns = ['Total'])
#print(df_csv)
## creates and converts dataframe into different files
#df_amended.to_csv('modified_data.csv')
#df_amended.to_excel('modified_data.xlsx')
#df_amended.to_csv('modified_data.txt', sep = '\t')

#Creates DataFrame
mydataset = {
  'People': ["Bob", "Jeff", "Jon"],
  'Age': [99, 69, 21]
}

#df = pd.DataFrame(mydataset)
#print(df)
#Create series within python
age = [99, 69, 21]
#df= pd.Series(age)
#print(df)

#Return specific value of series
#print(age[0])
#Creates labels e.g changes index to whatever you want
df = pd.Series(age, index = ["Bob", "Jeff", "Jon"])
#return label's value

#print(df["Jon"])

#Create a series from a dict

salary = {"month1": 4200, "month2": 3800, "month3": 3900}
df = pd.Series(salary)
#print(df)

#Convert specific indecies of a dict to a series
df =pd.Series(salary, index = ["month1","month3"])
#print(df)

#Create Dataframe
data = {
  "salary": [4200, 3800, 3900],
  "hours": [5000, 4000, 4005]
  

}

df = pd.DataFrame(data)

print(df)

#returns specified row
#print(df.loc[[0,1]])

#name indices of rows
df = pd.DataFrame(data, index = ["me","myself","i"])
#print(df)

#locate named indicies
print(df.loc["me"])

#Load a csv file into a dataframe(compressed)
df = pd.read_csv("pokemon_data.csv")
#print(df)
#print out dataframe fully
#print(df.to_string())

#returns maximum amount of rows
print(pd.options.display.max_rows)

#increase maximum amount of rows
pd.options.display.max_rows = 9999
dz = pd.read_csv("pokemon_data.csv")

#load json data into dataframe

dj = pd.read_json("data.json")
#print(df.to_string)

#create dataframe from dicts


data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":"NaN",
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":"NaN"
  }
}

df = pd.DataFrame(data)

#print(df) 
# displays information about the dataframe
#print(df.info)

#remove rows with empty cells (loading a new csv file)
df = pd.read_csv("data.csv")
new_df = df.dropna()
print(new_df.to_string())
