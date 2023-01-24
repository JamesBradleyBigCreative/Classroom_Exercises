
shape = int(input("---------------------ENTER NUMBER------------------------""\n"
                  "#########################################################""\n"
                  "##### 1 : Parallelogram #################################""\n"
                  "##### 2 : Trapezium #####################################""\n"
                  "##### 3 : Diamond #######################################""\n"
                  "\n"
                  ))

if shape == 1:
    size = int(input(("Parellelogram Selected Please select the size: ")))
elif shape == 2:
    size = int(input(("Trapezium Selected Please select the size: ")))
elif shape == 3:
    size = int(input(("Diamond Selected Please select the size: ")))
else:
    print("Invalid Input")

size = 9
count = 0

def parellogram(size):
    count = 0
    for i in range(size):
        print((" ")*i,end = " ")
        for j in range(size):
            print(chr(65+count),end = " ")
            count += 1
        print()


def trapezium(size):
    count = 0
    for i in range(size):
        print((" ")*i,end = " ")
        for j in range(2*(size-i)+i):
            print(chr(65+count),end = " ")
        count += 1
        print()


def diamond(size):
        for i in range(size):
            for j in range(size-i-1):
                print(" ", end  = " ")
            for k in range((i*2)+1):
                print(chr(65+k), end = " ")
            print()
        
        for i in range(size):
            for j in range(i+1):
                print(" ",end = " ")
            for k in range(2*(size - i-1) - 1):
                print(chr(65+k),end = " ")
            print()


def heart(size):
    print("HERE IS YOUR HEART")
    import os
    os.startfile(r"C:\Users\Learner\source\repos\print_diamond1\print_diamond1\heart.png")


heart(size)

