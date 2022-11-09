def Collector():
    Dict = {}
    for item in mylist:
        temp = item.split(",")
        Dict.update({temp[0]:temp[3]})
    return Dict


mylist = []
item = input("Enter item name: ")
cost = int(input("\nEnter cost price: "))
sell = int(input("\nEnter selling price: "))
def loss():
    if cost > sell:
        Varloss = cost - sell
        mylist.append(f"{item},{cost},{sell},{Varloss}")
        print(f"\nProfit is : ${Varloss}")

def profit():
    if sell > cost:
        VarProfit = sell - cost
        mylist.append(f"{item},{cost},{sell},{VarProfit}")
        print(f"\nProfit is : ${VarProfit}")

         
def positive():
    if cost >= 0:
        print("\nCost is a positive number")
    else:
        print("\nCost is a negative number")
    if sell >= 0:
        print("\nSell is a positive number")
    else:    
        print("\nSell is a negative number")

positive()
loss()
profit()
print (Collector())
