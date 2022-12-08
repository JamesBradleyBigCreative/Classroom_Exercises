byeBye = False
myList = []

#open txt file
f = open("christmas.txt", "r")

#appends list with correct info from txt file 
for i in f.readlines():
    myList.append(i)

#attempt int input, if wrong try again, return input once integer
def correct_input():
    i = 0
    while True:
        try:
           i = int(input("What day of christmas are you on?: "))
        except:
           print("ERROR: Please Enter a valid day between [1] and [12]: \n")
        else:
           return i

#Checks that the users input is in between the correct values 
def value_check(j):
    while True:
        if j > 12 or j < 1:
            print("ERROR: Incorrect Number")
            correct_input()
        else:
            break

    return j

#while loop to allow the user to run the program again or to exit
def try_again():

    result = False

    while True:
        hello = input("Would you like to try again?:  Y / N")
        hello = hello.upper()
        if hello == "Y":
            return result
        elif hello == "N":
            print("Thank you for playing come back again")
            result = True
            return result
        else:

            print("ERROR: Invalid Option")


#main body - cal functions + countdown of days
while byeBye == False:

    days = value_check(correct_input())

    while days != 0:
        print(days, myList[days-1])
        days -= 1
    
    byeBye = try_again()

