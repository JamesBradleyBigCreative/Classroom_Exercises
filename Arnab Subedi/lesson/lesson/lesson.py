food = {
    "coke":1.50,
    "rice":1.50,
    "sugar":1.50,
    "pizza":1.50,
    "garlic":1.50,
    "lemons":1.50,
}


for i in food:
    print(i)

def calculate(total,price):
    total -= price
    return total

def main():
    purse = 0
    purse = input("how much money do you have: ")
    continue2 = None
    continue2 = input("do you want to continue yes/no : ")
    while continue2 == "yes":
        continue2 = input("do you want to continue yes/no : ")
        purchase = str(input("Enter your choice: "))
        if purchase == "coke":
            purse = calculate(purse,1.5)
            print(f"your wallet is : {purse}")
        elif purchase == "rice":
            purse = calculate(purse,1.5)
            print(f"your wallet is : {purse}")
        elif purchase == "sugar":
            purse = calculate(purse,1.5)
            print(f"your wallet is : {purse}")
        elif purchase == "pizza":
            purse  = calculate(purse,1.5)
            print(f"your wallet is : {purse}")
        elif purchase == "garlic":
            purse = calculate(purse,1.5)
            print(f"your wallet is : {purse}")
        elif purchase == "lemons":
            purse = calculate(purse,1.5)
            print(f"your wallet is : {purse}")
        else:
            break
main()