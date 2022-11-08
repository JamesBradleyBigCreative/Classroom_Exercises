cost ={
    "pen" : 0.05,
    "chair" : 5,
    "tomatoes" : 0.05,
    "keyboard" : 7,
    "ring" : 0.2,
    "Andreas coffee" : 0.4,
    "higlighter" : 0.05,
    "pencil case" : 5,
    "mouse" : 2.5,
    "trainers" : 7
}


sell ={
    "pen" : 1,
    "chair" : 25,
    "tomatoes" : 0.5,
    "keyboard" : 117,
    "ring" : 8,
    "Andreas coffee" : 2,
    "highlighter" : 1,
    "pencil case" : 4,
    "mouse" : 50,
    "trainers" : 70
}

for item,value in cost.items():
    print(item,value)

print("\n")

for item,value in sell.items():
    print(item,value)

print("\n")

item_select = input("select an item:")
print("\n")
cost = float(input("enter cost price:"))
print("\n")
sell = float(input("enter sell price:"))
print("\n")

def loss():
    if cost > sell:
        print("Loss is:")
        print(cost - sell)

def profit():
    if sell > cost:
        print("Profit is:")
        print(sell - cost )


def positive():
    if cost >= 0:
        print("cost is a positive number!")

    else:
        print("cost is negative number!")


    if sell >= 0:
        print("sell is a positive number!")

    else:
        print("sell is a negative number!")

positive()
profit()
loss()