# selected_letter = int(input("Enter a Letter: "))

# chr()

# print(chr(selected_letter))

# Changes a DECIMAL value to an ASCII character

# print(ord(selected_letter))

# Changes an ASCII chraracter to a DECIMAL value

#for i in range(65, 95):
 #print(chr(i), end = "")


#print()

# SQUARE

#size = 5
#count = 0

#for i in range(size):
#    for j in range(size):
#        print(chr(65 + count), end = " ")
#        count += 1
#    print()

# RIGHT ANGLED TRIANGLE:

#size = 5

#for i in range (size):
#    for j in range(i+1):
        # range is i + 1
#        print(chr(j + 65), end = " ")
#    print()


#OPPOSITE ANGLED TRAINGLE
#from ctypes import c_double


#size = 5 

#for i in range(size):
#    for j in range(1, size - i):
#        print(" ", end= " ")
            #print at the start and end with spaces
#    for k in range(i + 1):
#        print(chr(65 + k), end = " ")
#    print()


# HOLLOW ANGLED TRIANGLE 

#size = 10

#for i in range(1, size+1):
    
#    count = 0

#    for j in range(i):
#        if j == 0 or j == i -1:
#            print(chr(65 + count), end = "")
#            count +=1
#        else:
#            if i != size:
#                #If i is smaller than size
#                print(" ", end = "")
#                #Print with a space
#            else: 
#                print(chr(65 + count), end = "")
#                count +=1
#    print()
    

# TRIANGLE

#size = 7

#for i in range(size):
#    for j in range (size - i - 1):
#        # make the size 1 smaller than i
#        print(" .", end = "")
#        # The full-stop fills in the amount of gaps until the letters start
#    for k in range((i * 2) +1):
#        print(chr(65 + k), end = "")
#    print()

# HOLLOW TRIANGLE

#size = 9

#for i in range(size):
#    for j in range(size - i - 1):
#        print(" ", end = " ")
            #for j, the range is size - 1 - i,
            #then print with spaces at the start and end

#    count = 0 

#    for k in range((i * 2) + 1):
#        if k == 0 or k == 2 * i:
#            # if k is equal to 0, or if k is equal to 2 x i
#            print(chr(65 + count), end = " ")
#            count +=1
#        else:
#            if i == size -1:
#                print(chr(65 + count), end = " ")
                    #if i is equal to the size of -1
                    # then print, with letters + count, then end with spaces at the end of each line
#                count += 1
#            else:
#                print(" ", end = " ")
            
#    print()


# UPSIDE DOWN TRIANGLE 

#size = 9

#for i in range(size):
#    for j in range(i):
#        print(" ", end = " ")
   
#    for k in range(2*(size - i) - 1):
#        print(chr(65 + k), end = "")
#    print()


# PARALLELOGRAM

size = 5
count = 0
for i in range(size+1):
    for j in range(size+1):
        print(chr(65 + count), end = " ")
        count += 1
    print()