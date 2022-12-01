#Code for while loop
x=0    
while (x<4):
    print (x)
    x= x+1
    
print("\n")
print("\n")

#For Loop Simple Example	
x=0 
for x in range (2,7):
    print (x)

print("\n")
print("\n")


#Use of for loop in string	
Months = ["Jan","Feb","Mar","April","May","June"]
for m in (Months):
    print (m)

print("\n")
print("\n")


#Use break-statement in for loop	
for x in range (10,20):      #Once loop reaches 15 (condition) the loop breaks
       if (x == 15): break
       print (x)

print("\n")
print("\n")


#Use of Continue statement in for loop	
for x in range (10,20): 
#Prints numbers that do not appear in the 5 times tables as there is no remainder when those numbers are divided by 5 
       if (x % 5 == 0): continue
       print (x)

print("\n")
print("\n")


#Code for “enumerate function” with “for loop”	
Months = ["Jan","Feb","Mar","April","May","June"] # enumerate numbers each index and displays the number and the index in the terminal
for i, m in enumerate (Months):
    print (i,m)


print("\n")
print("\n")


#for loop to repeat the same statement over and again
for i in '123':
    print ("guru99",i,)

print("\n")
print("\n")


#Break statement inside a for-loop
my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')

print('Loop is Terminated')


#SET MyList TO <'Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'>
#SEND <My_list> TO DISPLAY

#IF <myList[i] = Guru>
#THEN <SEND <Found the name Guru> TO DISPLAY> 
#END IF

#SEND <Loop is Terminated> TO DISPLAY


print("\n")
print("\n")


#Example: Break statement inside while-loop
my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 
i = 0

while True:
    print(my_list[i])
    if (my_list[i] == 'Guru'):
        print('Found the name Guru')
        break
        print('After break statement')
    i += 1

print('After while-loop exit')

#SET MyList TO <'Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'>
#SET i TO <0>


#WHILE <True> OUTPUT <myList> 

#IF <MyList[i] = Guru> 
#THEN <SEND <Found the name Guru> TO DISPLAY> 
#i += 1

#END WHILE


#OUTPUT 'After while-loop exit' 