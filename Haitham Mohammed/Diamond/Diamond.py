##Changes a decimal value to an ASCII character
#chr()

#Changes ACII character to a decimal value
#ord()


##creates square by itterating through the first 25 letters of the alphabet in 5 rows

#size = 5
#count = 0
#for i in range(size):
#    for j in range(size):
#       print(chr(65+count), end= ' ')
#       count+= 1

#    print()

# #creates right angled triangle by adding a laetter consequecutively 
#size = 5

#for i in range(size):
#    for j in range(i+1):
#        print(chr(65+ j), end = ' ' )
#    print()

## flipped right angle triangle
#size = 5
#for i in range(size):
#    for j in range(1, size - i):
#        print(" ", end= " ")
#    for k in range(i + 1):
#        print(chr(65+k), end= " ")
#    print()
## Hollow triangle
#size =10
#for i in range(1,size+11):
#    count = 0



#    for j in range(i):
#        if j == 0 or j == i-1:
#            print(chr(65+count), end = ' ')
#            count+= 1
#        else:
#            if i != size:
#                print(" ", end = " ")
#            else:
#                print(chr(65 + count), end = " ")
#                count+=1
#    print()
## Triangle

#size  = 7

#for i in range(size):
#    for j in range(size- i - 1):
#        print(".", end = " ")
#    for k in range((i*2)+1):
#        print(chr(65+ k), end = " ")
#    print()

##Hollow triangle

#size = 9

#for i in range(size):
#    for j in range(size -1 -i):
#        print(" ", end = "")
#    count = 0
#    for k in range((i*2)+1):
#        if k ==0 or k ==2* i:
#            print(chr(65+ count), end = "")
#            count += 1

#        else:
#            if i == size-1:
#                print(chr(65+ count), end = "")
#                count += 1
#            else: 
#                print(" ", end = "")


#    print()

##upside down triangle
#size = 9

#for i in range(size):
#    for j in range(i):
#        print(" ", end = " ")
    
#    for k in range(2*(size-i)-1):
#        print(chr(65+ k),end = " ")
#    print()



size = int(input("What size would you like to have on you Diamond?:  "))
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
