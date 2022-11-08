class SignUp:
    def __init__(self, mail, name, username, password):
        self.mail = mail
        self.name = name
        self.username = username
        self.password = password
    def verification(self):
       x = False
       while x == False:
        if self.mail and self.name and self.username and self.password != "":
            x = True
            return False
        else:
            x = False
            print("[[[[ONE OR MORE VALUES ARE EMPTY PLEASE ENTER AGAIN TO CONTINUE!]]]]")
            print("\n")
            return True
            

class LogIn:
    def __init__(self,username,password,username1,password1):
        self.username = username
        self.password = password
        self.username1 = username1
        self.password1 = password1
    def authentication(self):
       count = 0
       authentication = False
       while authentication == False:
           if self.username == self.username1 and self.password == self.password1:
               print("[[[[[WELCOME!]]]]]")
               print("\n")
               authentication = True
           else: 
               print("[[[[INCORRECT USERNAME OR PASSWORD]]]]")
               print("\n")
               if count != 3:
                   self.username = input("Enter a Username: ")
                   self.password = input("Enter a password: ")
                   print("\n")
               else:
                   print("[[[[[TOO MANY ATTEMPTS YOU HAVE BEEN LOCKED OUT]]]]]")
                   print("\n")
                   exit()

               count +=1
       
class Graph:
    def graph():
        import numpy as np
        import matplotlib.transforms as mtransforms
        import matplotlib.pyplot as plt
        from matplotlib.cbook import get_sample_data


        def convertdate(x):
            return np.datetime64(x, 'D')


        fname = get_sample_data('Stocks.csv', asfileobj=False)
        stock_data = np.genfromtxt(fname, encoding='utf-8', delimiter=',',
                                   names=True, dtype=None, converters={0: convertdate},
                                   skip_header=1)


        fig, ax = plt.subplots(1, 1, figsize=(6, 8), layout='constrained')

        # These are the colors that will be used in the plot
        ax.set_prop_cycle(color=[
            '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a',
            '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94',
            '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d',
            '#17becf', '#9edae5'])

        stocks_name = ['IBM', 'Apple', 'Microsoft', 'Xerox', 'Amazon', 'Dell',
                       'Alphabet', 'Adobe', 'S&P 500', 'NASDAQ']
        stocks_ticker = ['IBM', 'AAPL', 'MSFT', 'XRX', 'AMZN', 'DELL', 'GOOGL',
                         'ADBE', 'GSPC', 'IXIC']

        # Manually adjust the label positions vertically (units are points = 1/72 inch)
        y_offsets = {k: 0 for k in stocks_ticker}
        y_offsets['IBM'] = 5
        y_offsets['AAPL'] = -5
        y_offsets['AMZN'] = -6

        for nn, column in enumerate(stocks_ticker):
            # Plot each line separately with its own color.
            # don't include any data with NaN.
            good = np.nonzero(np.isfinite(stock_data[column]))
            line, = ax.plot(stock_data['Date'][good], stock_data[column][good], lw=2.5)

            # Add a text label to the right end of every line. Most of the code below
            # is adding specific offsets y position because some labels overlapped.
            y_pos = stock_data[column][-1]

            # Use an offset transform, in points, for any text that needs to be nudged
            # up or down.
            offset = y_offsets[column] / 72
            trans = mtransforms.ScaledTranslation(0, offset, fig.dpi_scale_trans)
            trans = ax.transData + trans

            # Again, make sure that all labels are large enough to be easily read
            # by the viewer.
            ax.text(np.datetime64('2022-10-01'), y_pos, stocks_name[nn],
                    color=line.get_color(), transform=trans)

        ax.set_xlim(np.datetime64('1989-06-01'), np.datetime64('2023-01-01'))

        fig.suptitle("Technology company stocks prices dollars (1990-2022)",
                     ha="center")

        # Remove the plot frame lines. They are unnecessary here.
        ax.spines[:].set_visible(False)

        # Ensure that the axis ticks only show up on the bottom and left of the plot.
        # Ticks on the right and top of the plot are generally unnecessary.
        ax.xaxis.tick_bottom()
        ax.yaxis.tick_left()
        ax.set_yscale('log')

        # Provide tick lines across the plot to help your viewers trace along
        # the axis ticks. Make sure that the lines are light and small so they
        # don't obscure the primary data lines.
        ax.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)

        # Remove the tick marks; they are unnecessary with the tick lines we just
        # plotted. Make sure your axis ticks are large enough to be easily read.
        # You don't want your viewers squinting to read your plot.
        ax.tick_params(axis='both', which='both', labelsize='large',
                       bottom=False, top=False, labelbottom=True,
                       left=False, right=False, labelleft=True)

        # Finally, save the figure as a PNG.
        # You can also save it as a PDF, JPEG, etc.
        # Just change the file extension in this call.
        # fig.savefig('stock-prices.png', bbox_inches='tight')
        plt.show()

        
    #precense check
class bankdetails:
    def __init__(self,accountnumber, sortcode, amount):
        self.accountnumber = accountnumber
        self.amount = amount
        self.sortcode = sortcode

    def withdrawl(self):
        import re
        withdrawl = False
        while withdrawl == False:
            if len(self.accountnumber) == 8:
                print("[[[[Account Number Accepted!]]]]")
                withdrawl = True
            else:
                print("[[[[Account Number is meant to be 8 Digits!]]]]")
                self.accountnumber = input("Enter your account number: ")
                
        cont = False
        rex = re.compile("^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$")
        while cont == False:
            if rex.match(self.sortcode):
                print("[[[[[SORT CODE ACCEPTED!]]]]]")
                cont = True
            else:
                print("[[[[MAKE SURE THE SORT CODE IS IN THE FORMAT 00-00-00 WHERE 0 is 0-9! ]]]]")
                self.sortcode = input("Enter your Sort code: ")
        print(f"[[[[[[WITHDRAWAL SUCCESFULL OF AMMOUNT {self.amount}! ]]]]]]")


class Card_Details:
    def __init__(self, card_CVC, card_number, card_expiration, money):
        self.card_CVC = card_CVC
        self.card_number = card_number
        self.card_expiration = card_expiration
        self.money = money
    def moneyin(self):
        import re
        mon = False
        while mon == False:
            if len(self.card_CVC) ==3:
                print("[[[[[CVC ACCEPTED!]]]]]")
                print("\n")
                mon = True
            else:
                print("[[[[[CVC IS MEANT TO BE 3 DIGITS!]]]]]")
                print("\n")
                self.card_CVC = input("Enter your CVC: ")
        a = False
        while a == False:
            if len(self.card_number) == 16:
                print("[[[[[CARD NUMBER ACCEPTED!]]]]]")
                print("\n")
                a = True
            else:
                print("[[[[[CARD NUMBER IS MEANT TO BE 16 DIGITS!]]]]]")
                print("\n")
                self.card_number = input("Enter your card number: ")
        b = False
        r = re.compile("^[0-9][0-9]/[0-9][0-9]$")
        while b == False:
            if r.match(self.card_expiration):
                print("[[[[[DATE OF EXPIRY ACCEPTED!]]]]]")
                print("\n")
                b = True
            else:
                print("[[[[[PLEASE MAKE SURE THE EXPIRY FORMAT IS 00/00!]]]]]")
                print("\n")
                self.card_expiration = input("Enter your expiry date")
        print(f"[[[[[MONEY IN SUCCESSFULLY OF AMOUNT {self.money}]]]]]")
        print("\n")

class stocks:
    def __init__(self,stock,year,money):
        self.stock = stock
        self.year = year
        self.money = money
    def APPLE(self):
        global profit
        dates = {
            1992:0.5,
            1996:0.2,
            2000:1,
            2004:0.4,
            2008:6.2,
            2012:18.45,
            2016:25.61,
            2020:76.45,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit







            


        
    def NASDAQ(self):
        global profit
        dates = {
            1992:633,
            1996:1050,
            2000:4880,
            2004:2150,
            2008:2580,
            2012:3200,
            2016:5340,
            2020:9060,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit
    def SP500(self):
        global profit
        dates = {
            1992:408,
            1996:668,
            2000:1518,
            2004:1150,
            2008:1500,
            2012:1420,
            2016:1900,
            2020:2700,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit
    def ALPHABET(self):
        global profit
        dates = {
            1992:3,
            1996:25,
            2000:43,
            2004:63,
            2008:283,
            2012:322,
            2016:802,
            2020:1500,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit
    def ADOBE(self):
        global profit
        dates = {
            1992:3.7,
            1996:7.8,
            2000:15.3,
            2004:19.5,
            2008:36,
            2012:35,
            2016:91,
            2020:328,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit
    def MICROSOFT(self):
        global profit
        dates = {
            1992:1.6,
            1996:3.8,
            2000:28,
            2004:17,
            2008:21,
            2012:22,
            2016:50,
            2020:175,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit
    def IBM(self):
        global profit
        dates = {
            1992:11.2,
            1996:17,
            2000:67,
            2004:60,
            2008:72,
            2012:125,
            2016:106,
            2020:95,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit
    def AMAZON(self):
        global profit
        dates = {
            1992:0.2,
            1996:2.1,
            2000:3.8,
            2004:2.7,
            2008:4.6,
            2012:9.5,
            2016:33,
            2020:180,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit

    def DELL(self):
        global profit
        dates = {
            1992:0.01,
            1996:0.3,
            2000:2,
            2004:3.2,
            2008:5.2,
            2012:6,
            2016:9,
            2020:50,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit
    def XEROX(self):
        global profit
        dates = {
            1992:14,
            1996:33,
            2000:34,
            2004:24,
            2008:24,
            2012:15,
            2016:20.5,
            2020:34,
            }
        profit  = 0
        initial  = 0
        mon = self.money
        i = self.year
        if i == 2020:
            print("[[[[[You have made no profit!]]]]]")
        else:
            ""
        while i != 2020:
            inv = dates[i]
            initial += float(mon) / inv
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
            i = i+4
            if i == 2020:
                break
            inv = dates[i]
            print(f"Your Balance has gone to {initial*inv}")
            print("\n")
        profit += initial * dates[2020]
        print(f"Your total profit from investment is {profit}!")
        return profit