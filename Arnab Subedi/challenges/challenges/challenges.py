#task1

from asyncio.windows_events import NULL


stock = {
    "amazon" :115.81,
    "apple" :152.9,
    "Nasdaq Composite" :10933.73,
    "russell200index" :1676.01,
    "Tesla Inc" :286.80,
    "Meta" :137.79,
    "mcdonalds" :242.71,
    "Kfc" :110.06,
    "sainsburys" :190.84,
    "morissons" :286.70,
    
    }
for key,value in stock.items():
    print(key,value)
print("\n")
#task2
def userin ():
    global buy2
    buy2 = input("Enter the stock you want to buy? ")
    for item in stock:
        if buy2 == item:
            print(f"the prices of the stock are {stock[item]}")
            break
        else:
            print("invalid")
            
userin()
print("\n")
in_stock = {
    "amazon" :12,
    "apple":44,
    "Nasdaq Composite":22,
    "russell200index":123,
    "Tesla Inc":343,
    "Meta":3213,
    "mcdonalds":3213,
    "Kfc":3123,
    "sainsburys":23,
    "morissons":2212,
    
    }
print("the share stocks are :")
for key,value in in_stock.items():
    print(key,value)

print("\n")
bought_2 = buy2
share = int(input("how many shares do you want to buy?"))
calculate = None

print("\n")
#task3
def share2 ():
    for key,value in in_stock.items():
        if bought_2 == key:
                print(f"The share stock was {value} ")
                value -= share
                print(f"the share stock now is {value}")
                break
        else:
                print("invalid")
                break
share2()

print("\n")

#task 4
def basket():
    global total
    global count
    total = 0
    count = 0
    while count != 1:
        global basket
        basket = input("enter a stock into your basket?\n ")
        for key,value in in_stock.items():
            if basket == key:
                global amount
                amount = int(input("how much shares do you want to buy? \n"))
                value -= amount
                print(f"the stock left over is {value}")
                for key1,value1 in stock.items():
                    if basket ==key1:
                        total += amount * value1
                    else:
                        NULL
                print(f"your basket total is {total}\n")
                        
                global continue1     
                continue1 = input("do you want to add another item : yes/no ?\n")
                if continue1 == "yes":
                    count=0
                else:
                    count = 1
            else:
                break
basket()



                 

       