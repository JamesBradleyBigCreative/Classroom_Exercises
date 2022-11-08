
#task1
stock = {
    "amazon" :"115.81",
    "apple" :"152.9",
    "Nasdaq Composite" :"10,933.73",
    "russell200index" :"1,676.01",
    "Tesla Inc" :"286.80",
    "Meta" :"137.79",
    "mcdonalds" :"242.71",
    "Kfc" :"110.06",
    "sainsburys" :"190.84",
    "morissons" :"	286.70",
    
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