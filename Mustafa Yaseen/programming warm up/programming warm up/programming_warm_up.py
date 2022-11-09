#Q1:    Initialise the variables with the appropriate data types
name_String = "Mustafa"
age_Integer =  16
height_Float = 160

print("Q1_Output:\n         ", name_String, age_Integer, height_Float)
 
#Q2:    Fill in the missing elements for the data structures for the following data structures
#a)
list_LicensePlates = ["uiwadha","bwsdnhkjans"]

#b)
dict_Details = {"Name":"Mustafa", "age":16, "Phone number ":"07487 654 321", "Road ":"123 bark street"}

print("Q2a_Output:\n         ", list_LicensePlates)
print("Q2b_Output:\n         ", dict_Details)



#Q3:    Rewrite the following program so that ALL variables are localised



def UserInput():
    value = int(input("Enter numerical value: "))


    return value

def Calculation():
    num1 = UserInput()
    num2 = UserInput()
    return num1 + num2

print("Q3_Output:\n         ", Calculation())


#Q4:    a) increment the value of val_1 with the value of val_2
#       b) multiply the value of val_3 with val_4
#       c) find a way to print the value for the remainder of 9 divided by 2
val_1 = 5
val_2 = 3



print( val_1)
    val_1+= val_2
    

val_3 = 7

val_4 = 4


print(val_3)

val_3 *= val_4

remainder = 9 % 2 

print("Q4_Output:\n         ", remainder)
#________________________________________________________________

#Q5:    
myArray = [2,4,8,1,6,3,9,5]


#       a) Given the array of integers create a FOR loop that only prints values less than 7

#       b) Given the same list create a FOR loop the only prints values greater than or equal to 7

for x in myArray:
    if x<7:
        print(x)


for x in myArray:
    if x>7:
        print(x)


