shape = int(input("###########PICK A SHAPE###########""\n"
              "##################################""\n"
              "###########-1 Parallelogram""\n"
              "###########-2 Trapezium""\n"
              "###########-3 Diamond"))

size = 0
def Paralelogram(size):
   
    count = 0
    for i in range(size):
        print((" ") * i, end ="")
        for j in range(size):
            print(chr(65+count), end= ' ')
        count+= 1

        print()

Paralelogram(size)


def Trapezium(size):

    count = 0
    for i in range(size):
        print((" ")*i, end ="")
        for j in range(2*(size-i)+i):
            print(chr(65+count), end= ' ')
        count+= 1

        print()
Trapezium(size)


def Diamond(size):

    for i in range(size):
        for j in range(size- i - 1):
            print(" ", end = " ")
        for k in range((i*2)+1):
            print(chr(65+ k), end = " ")
        print()


    for i in range(size):
        for j in range(i+1):
            print(" ", end = " ")
    
        for k in range(2*(size-i-1)-1):
            print(chr(65+ k),end = " ")
        print()
Diamond(size)














if shape == 1:
    size = int(input("You have chosen parallelogram, what size would you like it to be? "))
    Paralelogram(size)
elif shape == 2:
    size = int(input("You have chosen trapezium, what size would you like it to be? "))
    Trapezium(size)
elif shape == 3:
    size = int(input("You have chosen diamond, what size would you like it to be"))
    Diamond(size)
else:
    print("Invalid input!")










