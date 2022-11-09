stock = { 
   "Amazon": "115",
    "Sony": "65",
    "Netflix": "226",
    "Tesco": "219",
    "Tesla": "286",
    "Meta": "137",
    "Microsoft": "236",
    "Uber": "28",
    "Aston martin": "129"

   
   
   
    }

for item, key in stock.items():
  print(item, key)



#task2

inp = input("Enter a stock to buy ")
if inp == "Amazon":
    print(115)
   
elif inp == "Sony":
        print(65)
elif inp == "Netflix":
    print(226)
   
elif inp == "Tesco":
        print(219)
elif inp == "Tesla":
    print(286)
   
elif inp == "Meta":
        print(137)
elif inp == "Microsoft":
        print(236)
elif inp == "Uber":
        print(28)
elif inp == "Aston martin":
        print(129)
else:
    print("Invalid spelling")


#task3

in_stock = {
    
     "Amazon": "303",
    "Sony": "814",
    "Netflix": "925",
    "Tesco": "623",
    "Tesla": "521",
    "Meta": "492",
    "Microsoft": "350",
    "Uber": "844",
    "Aston martin": "639"


    }

Confirm = input("are you sure you would like to get this stock?")

buy = int(input("how much would you like to buy of this stock?"))

if inp == "Amazon":
    print(303 - buy)

elif inp == "Sony":
    print(814-buy)

elif inp == "Netflix":
    print(925-buy)

elif inp == "Tesco":
    print(623-buy)

elif inp == "Tesla":
    print(521-buy)

elif inp == "Meta":
    print(492-buy)

elif inp == "Microsoft":
    print(350-buy)

elif inp == "Uber":
    print(844-buy)

elif inp == "Aston martin":
    print(639-buy)
else:
    print("invalid")


# ALL NUMERICAL VALUES MUST BE CHANGED TO INTEGERS OR FLOATS
# DO NOT HARD CODE VALUES IN STATEMENTS, MUST SPECIFY DICTIONARY OR LIST ELEMENTS