#stock = {
 #   "Amazon" : "115.66",
  #  "Meta" : "138.09",
   # "Tesco" : "219.30",
    #"Tesla" : "286.90",
   # "Apple" : "152.98",
    #"pen" : "203.45",
    #"Rubber" :"278.65",
    #"Dog" : "156.57",
    #"Cat" : "123.78",
    #"Ice Cream" : "346.89",
  # }

#userinput = str(input('enter a item'))

#for x, y in stock.items():
   # if x == userinput:
       # print(x)
      #  break

stock = {
    "Amazon" : "115.66",
    "Meta" : "138.09",
    "Tesco" : "219.30",
    "Tesla" : "286.90",
    "Apple" : "152.98",
    "pen" : "203.45",
    "Rubber" :"278.65",
    "Dog" : "156.57",
    "Cat" : "123.78",
    "Ice Cream" : "346.89",
    } 
for item,value in stock.items():
    print(item,value)


# task 2
#def userin ():
  #  buy2 = input("Enter the stock you want yo buy? ")
  #  for item in stock:
 #       if buy2 == item:
 #           print(stock[item])
            break
 #       else:
#            print("invalid")
#userin()


#task 3
stock_level = {
    "Amazon" : 30,
    "Meta" : 50,
    "Tesco" : 70,
    "Tesla" : 20,
    "Apple" : 40,
    "pen" : 110,
    "Rubber" :30,
    "Dog" : 50,
    "Cat" : 70,
    "Ice Cream" : 90,
    }
               

print("Here are all the items in stock")

for item,value in stock_level.items():
    print(item,value)

buy  = int(input("How many of this stock do you want to buy?"))

if buy2 == "Amazon":
    print(30 - buy)
elif buy2 == "Meta":
    print(50 - buy)
elif buy2 == "Meta":
    print(50 - buy)




else:
    print("Error: try again!!")





        
