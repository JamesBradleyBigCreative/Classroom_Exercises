# Built in functions

# all()
# Returns true if all elements in the structure are true
# If not all are true it will return false
myList = [1,0,1,0]

x = all(myList)

print(x)

# any()
# Checks if any elements in structure are true
# If so, true will be returned

Y = any(myList)
print(Y)

# any()
# return properties of specified object

class Person:
    name = "cam"
    age = 29

print(dir(Person))

# CASTING
# Converting a data type into another
num = int(5.00)
num2 = float(5)
num3 = str(5.799)
print(num)
print(num2)
print(num3)
print(num3, ". Type", type(num3))

# isinstance()
# returns true or false depending on if the variable matched the specified data type
x = 5
print(isinstance(x, float))

# len()
# Returns you the length of the data structure you use it with 

print(len(myList))

# min() & max()
# Returns minimum or maximum of specified values

print("min: " ,min(4,10), "max: ",max(5,11))

# pow()
# Returns the power of the specified values

print(pow(2,10))