def GetValue(newItem):
    print(MyDict)
    Keys = MyDict.keys()
    Keys = list(Keys)

    for i in range(len(MyDict)):
        if newItem == Keys[i]:
            print(f"The price of your item is {MyDict[newItem]}")
            return MyDict[newItem]
        elif i == len(MyDict)-1:
            print("You may have misspelled your item")

def BackgroundGetValue(newItem):
    Keys = MyDict.keys()
    Keys = list(Keys)

    for i in range(len(MyDict)):
        if newItem == Keys[i]:
            return MyDict[newItem]

def Purchase():
    print(IiS)
    newItem = input("Enter the item you want to buy: ")
    Keys = IiS.keys()
    Keys = list(Keys)

    for i in range(len(IiS)):
        if newItem == Keys[i]:
            print(f"Current Stock is {IiS[newItem]}")
            print(f"You have purchased {newItem}")
            IiS[newItem] = (IiS[newItem] - 1)
            print(f"New Stock is {IiS[newItem]}")
            break
        elif i == len(IiS)-1:
            print("You may have misspelled your item")

def Basket():
    print(f"{IiS}\n")
    print(f"{MyDict.values()}\n")
    newItem = input("Enter the item you want add to basket: \n")
    Keys = IiS.keys()
    Keys = list(Keys)

    for i in range(len(IiS)):
        if newItem == Keys[i]:
            print(f"You have added {newItem} to the basket \n")
            IiS[newItem] = (IiS[newItem] - 1)
            basketlist.append(newItem)
            return IiS , basketlist
        elif i == len(IiS)-1:
            print("You may have misspelled your item")



MyDict = {
    "Milk":2.0,
    "Bread":1.0,
    "Cheese":0.5,
    "T-Shirt":40.0,
    "Jeans":40.0,
    "Tv":100.0,
    "Blazer":20.0,
    "Tie":10.0,
    "Hat":5.0,
    "Trainers":70.0,
    }

IiS = {
    "Milk":20,
    "Bread":20,
    "Cheese":20,
    "T-Shirt":30,
    "Jeans":30,
    "Tv":5,
    "Blazer":10,
    "Tie":40,
    "Hat":20,
    "Trainers":15,
    }

basketlist = []
TotalPrice = 0
EWallet = 100


H = int(input("How many items to purchase: "))
for j in range (H):
    Basket()

print(basketlist)

for i in range (len(basketlist)):
    Temp = BackgroundGetValue(basketlist[i])
    TotalPrice = TotalPrice + Temp

print(TotalPrice)

if (TotalPrice > EWallet):
    print("You cant afford to purchase your items")
