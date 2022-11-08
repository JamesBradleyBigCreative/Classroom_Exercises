def Start():
    purse = 100.0
    global item_List
    item_List = ["coke","rice","sugar","pizza","garlic","lemons"]
    Flag = True
    while Flag == True:
        
        Choice = input("Do You Want to Puchase something:Y/N ")

        if Choice == "Y":
            purchase = str(input("Enter your choice: "))

            if purse < 0.0:
                print("Out of Money")
                Flag = False
                return item_List
            elif purchase == item_List[0]:
                print("coke")
                purse -= 1.50
                print("Purse: ",purse)
            elif purchase == item_List[1]:
                print("rice")
                purse -= 1.50
                print("Purse: ",purse)
            elif purchase == item_List[2]:
                print("sugar")
                purse -= 1.50
                print("Purse: ",purse)
            elif purchase == item_List[3]:
                print("pizza")
                purse -= 1.50
                print("Purse: ",purse)
            elif purchase == item_List[4]:
                print("garlic")
                purse -= 1.50
                print("Purse: ",purse)
            elif purchase == item_List[5]:
                print("lemons")
                purse -= 1.50
                print("Purse: ",purse)
        elif Choice == "N":
            print("No Purchase Made")
            Flag = False
            return item_List



print("coke")
print("rice")
print("sugar")
print("pizza")
print("garlic")
print("lemons")

Start()

