##chr() ## This converts decimals to characters
##ord() ## This converts characters to decimals

#selective_letter = int(input("Enter a letter? "))
#print(chr(selective_letter))
#selective_letter = input("Enter a letter? ")
#print(ord(selective_letter))


#for i in range(65,91):
#    print(chr(i),end = '') ## This prints out alphabet in ascii
#print()


#size = 5
#count = 0
#for i in range(size):
#    for j in range(5):
#        print(chr(65+i),end = ' ')## Print a Cube of letters
#        count+= 1
#    print()


#size = 5

#for i in range(size):
#    for j in range(i+1):
#        print(chr(j+65), end = ' ') ## prints right angle triangel
#    print()

#size = 5   
#for i in range(size):
#    for j in range(1,size-i):
#        print(" ", end =" ")
#    for k in range(i+1):
#        print(chr(65+k), end = ' ')##Prints other way around

#    print()

#size = 10

#for i in range(1,size +1):
#    count = 0
#    for j in range(i):
#        if j == 0 or j == i -1:
#            print(chr(65+count), end = " ") ## Print a hollowless right angle triangle
#            count+= 1
#        else:
#            if i != size:
#                print(" ",end = " ")
#            else:
#                print(chr(65+ count), end = " ")
#                count += 1
#    print()

#triangle full

#size = 7 
#for i in range(size):
#    for j in range(size-i-1):
#        print(" ", end  = " ")
#    for k in range((i*2)+1):
#        print(chr(65+k), end = " ")
#    print()

#hollow triangle

#size = 9

#for i in range(size):
#    for j in range(size-i-1):
#        print(" ",end = " ")
#    count = 0
#    for k in range((i * 2) +1): 
#        if k == 0 or k == 2 * i :
#            print(chr(65+count),end = " ")
#            count += 1
#        else:
#            if i == size -1:
#                print(chr(65+count),end = " ")
#                count+= 1
#            else:
#                print(" ",end = " ")
#    print()

#upside down triangle

size = 9

for i in range(size):
    for j in range(i):
        print(" ",end = " ")
    for k in range(2*(size - i) - 1):
        print(chr(65+k),end = " ")
    print()