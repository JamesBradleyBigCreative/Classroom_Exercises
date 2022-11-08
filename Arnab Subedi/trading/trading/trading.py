import module1 as mod
print(' [[[[[[[WELCOME TO OUR SPECIALISED TRADING PLATFORM]]]]]]]')
print("\n")

sign = input("Do you want to sign up y/n :")
if sign == "y":
    print("[[[[CONTINUING TO SIGN UP]]]]")
    print("\n")
else:
   print("[[[[[See you next time!]]]]]")
   print("\n")
   exit()

def hello():
  global username1
  global password1
  mail1 = input("Enter your mail: ")
  name1 = input("Enter your full name: ")
  username1 = input("Enter your username: ")
  password1 = input("Enter your password: ")
  print("\n")
  mod.SignUp(mail1,name1,username1,password1)
  sign = False
  while sign == False:
      if mod.SignUp.verification(mod.SignUp(mail1,name1,username1,password1)) == True:
            mail1 = input("Enter your mail: ")
            name1 = input("Enter your full name: ")
            username1 = input("Enter your username: ")
            password1 = input("Enter your password: ")
            print("\n")
            mod.SignUp(mail1,name1,username1,password1)
      elif mod.SignUp.verification(mod.SignUp(mail1,name1,username1,password1)) == False:
          sign = True
          print("[[[[[SIGN UP COMPLETED SUCCESFULLY!]]]]]")
        
hello()



 
def login():
    username2 = input("Enter your username: ")
    password2 = input("enter your password: ")
    print("\n")
    mod.LogIn.authentication(mod.LogIn(username2,password2,username1,password1))
login()


def MoneyIn():
    Continue = False
    choice = input("If you want to add money press Y or N if you don't want to add money: ")
    global money
    money = 0
    if choice == "y":
        adc = int(input("Enter the ammount of money You want to enter: "))
        money += adc
        card_num = input("Enter your card number: ")
        card_exp = input("Enter your card expiration: ")
        card_cvc = input("Enter your Cvc: ")
        print("\n")
        mod.Card_Details.moneyin(mod.Card_Details(card_cvc,card_num,card_exp,money))
    else:
        ""
def withdrawal():
    accountnumber1 = input("Enter your account number: ")
    sortcode1 = input("enter you sort code: ")
    print("\n")
    mod.bankdetails.withdrawl(mod.bankdetails(accountnumber1,sortcode1,v))


def trading():
    a = input("Do you want to display stock graph Y/N :")
    if a == "y" or a =="Y":
        mod.Graph.graph()
    else:
        ""
    stocks = ["NASDAQ","SP500","ALPHABET","ADOBE","MICROSOFT","IBM","APPLE","AMAZON","DELL","XEROX"]
    print("[[[[The current stocks avaiable at our trading platform ara: ]]]]")
    for i in stocks:
        print(i)
    what = str(input("What Stock do you want to invest your money on: "))
    stock = ""
    c = False
    while c == False:
       if what in stocks:
           stock += what
           c = True
       elif what not in stocks:
           stock = ""
           print("[[[[[invalid stock selection please retry!]]]]] ")
           what = str(input("What Stock do you want to invest your money on: "))
    print("\n")
    print("The years to invest available are: \n")
    years = [1992,1996,2000,2004,2008,2016,2020]
    for i in years:
        print(i)
    year = int(input("what year do you want to invest in the stock! "))
    b = False
    year1 = 0
    while b == False:
        if year in years:
            year1 += year
            b = True
        else:
            year1 = 0
            print("[[[[[Invalid year please retry!]]]]] ")
            year = input("what year do you want to invest in the stock! ")
    print("[[[[[----TRANSITIONING TO PAYMENT------]]]]]")
    MoneyIn()
    global v
    if stock == "APPLE":
        v = mod.stocks.APPLE(mod.stocks(stock,year1,money))
    elif stock == "NASDAQ":
       v = mod.stocks.NASDAQ(mod.stocks(stock,year1,money))
    elif stock == "SP500":
        v =mod.stocks.SP500(mod.stocks(stock,year1,money))
    elif stock == "ALPHABET":
       v = mod.stocks.ALPHABET(mod.stocks(stock,year1,money))
    elif stock == "ADOBE":
       v = mod.stocks.ADOBE(mod.stocks(stock,year1,money))
    elif stock == "MICROSOFT":
       v = mod.stocks.MICROSOFT(mod.stocks(stock,year1,money))
    elif stock == "IBM":
       v = mod.stocks.IBM(mod.stocks(stock,year1,money))
    elif stock == "AMAZON":
       v = mod.stocks.AMAZON(mod.stocks(stock,year1,money))
    elif stock == "DELL":
       v = mod.stocks.DELL(mod.stocks(stock,year1,money))
    elif stock == "XEROX":
       v = mod.stocks.XEROX(mod.stocks(stock,year1,money))
    else:
        print("[[[[INVALID STOCK]]]]")
    c = input("Do you want to withdraw?: ")
    print("\n")
    money += v
    if c == "Y" or c== "y":
        withdrawal()
    else:
        n = input("Do you want to trade again?: ")
        print("\n")
        if n == "Y" or n == "y":
            trading()
        else:
            print("[[[[[EXITING PROGRAM]]]]]")
            print("\n")
            exit()
trading()


