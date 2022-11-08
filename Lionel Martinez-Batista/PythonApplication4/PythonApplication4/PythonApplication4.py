from ast import Pass
from pickle import NONE
from types import NoneType
from unittest import skip


purse = 10.0

Products = {'coke': 1.50,
            'rice': 1.50,
            'sugar': 1.50,
            'pizza': 1.50,
            'garlic': 1.50,
            'lemons': 1.50,
            }
print('All for 1.50')
for x in Products:
   print(x)

def Buy_more():
    x = str(input('Do you wish to continue with your purchase? Y/N \n '))
    print('You currently have', purse)
    if x == 'N' or x == 'n':
        print('Have a nice day')
        quit()
    elif x == 'Y' or x =='y':
        global purchase
        purchase = str(input("Enter your choice: "))
    else:
       print('Error')
       quit()
        

purchase = str(input("Enter your choice: "))

while purse > 1.49:
           
    
    if purchase == 'coke':
        print("coke")
        purse -= 1.50
        print('You currently have: \n',purse)
        Buy_more()
        
    elif purchase == 'rice':
        print("rice")
        purse -= 1.50
        print('You currently have: \n',purse)
        Buy_more()
        
    elif purchase == 'sugar':
        print("sugar")
        purse -= 1.50
        print('You currently have: \n',purse)
        Buy_more()
        
    elif purchase == 'pizza':
        print("pizza")
        purse -= 1.50
        print('You currently have: \n',purse)
        Buy_more()
        
    elif purchase == 'garlic':
        print("garlic")
        purse -= 1.50
        print('You currently have: \n',purse)
        Buy_more()
        
    elif purchase == 'lemons':
        print("lemons")
        purse -= 1.50
        print('You currently have: \n',purse)
        Buy_more()
        
    else:
        print('Item not available')
        Buy_more()