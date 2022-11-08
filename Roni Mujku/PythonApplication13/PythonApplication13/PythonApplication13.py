class Sales:
    def __init__(self):
        self.__Mylist = []
        self.__MyDict = {}

    def Collecter(self):
        self.__MyDict = {}
        for item in self.__Mylist:
            temp = item.split(",")
            self.__MyDict[temp[0]] = temp[3]
        return self.__MyDict

    def ProfLoss(self):
        print("----------------------------------------------------------------")
        flag = True
        while flag == True:
            item = input("\nEnter the name of your item: ")
            Cost_Price = float(input("\nEnter the cost of making your item: "))
            Selling_Price = float(input("Enter the selling price of your item: "))

            if (Selling_Price < 0 or Cost_Price < 0):
                print("\nError inputed price below 0 ")
                return None

            else:
                if (Cost_Price > Selling_Price):
                    loss = Selling_Price - Cost_Price
                    self.__Mylist.append(f"{item},{Cost_Price},{Selling_Price},{loss}")
                    print(f"\nYou are selling your item at a loss of ${loss} ") 

                elif (Selling_Price > Cost_Price):
                    profit = Selling_Price - Cost_Price
                    self.__Mylist.append(f"{item},{Cost_Price},{Selling_Price},{profit}")
                    print(f"\nYou are selling your item at a profit of ${profit} ")

            Continue = input("\nPress Any Key to continue: Press N to stop: ")
        
            if Continue == 'N':
                print("\nExiting..... \n")
                flag = False

    def GetDict(self):
        print(self.__MyDict)

    def AddDict(self,ItemName,ItemProfit):
        self.__MyDict.update({ItemName:ItemProfit})

    def GetList(self):
        print(self.__Mylist)

    def Addlist(self,ItemName,ItemProfit):
        self.__MyDict.update({ItemName:ItemProfit})

Tesco = Sales()

Tesco.ProfLoss()

print(Tesco.Collecter())