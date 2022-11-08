Cost = {
    "Costs: "
    "Apple" : 0.05,
    "Banana" : 0.08,
    "Tomatoes" : 0.60,
    "Watermelon" : 1.15,
    "Lemon" : 0.10
 }

Sell = {
    "Sell: "
    "Apple" : 0.25,
    "Banana" : 0.50,
    "Tomatoes" : 0.30,
    "Watermelon" : 1.05,
    "Lemon" : 0.45
 }

for item,value in Cost.items():
  print(item,value)

print("\n")

for item,value in Sell.items():
  print(item,value)

print("\n")

item_selection=(input("Enter the item that you want to buy: "))
print("\n")
Cost=float(input("The cost price is: "))
print("\n")
Sell=float(input("The sell price is: "))
print("\n")

def Loss():
    if Cost > Sell:
        print("Your loss is: ")
        print(Cost - Sell)

def Profit():
    if Sell > Cost:
        print("Your profit is: ")
        print(Sell - Cost)

def positive():
    if Cost >= 0:
        print("Your cost is a positive number!")
    else:
        print("your cost is a negative number")


    if Sell >= 0:
        print("Your sell is a positive number")
    else:
        print("Your sell is a negative number!")

positive()
Profit()
Loss()

