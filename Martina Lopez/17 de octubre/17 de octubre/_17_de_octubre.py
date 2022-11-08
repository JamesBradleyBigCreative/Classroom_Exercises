# Built in dunctions (school w3)

# ALL() FUNCTION:
# Returns true if all element in date structure are.
# True otherwise will return false.
myList = [0, 1, 0,1]
x = all (myList)
print (x)

# ANY() FUNCTION:
# Chcek if any elements in the structure are true.
# If so will return true.
y = any (myList)
print (y)

# DIR() FUNCTION:
# Return properties of specified object
class person:
    name = "Mar"
    age = 17
print(dir(person))

# CASTING:
# Comverts one date type into a specified type 
num = int(5.00)
num2 = float(5)
num3_str = str(5.66)
print(num3_str, ". Type", type(num3_str))

# isistance() Function
# Returns true or false depending on if the
# variable matches the specified date type
x = 5
print(isinstance(x, int))

#LEN() FUNCTION
# Returns length/count of date structure (index = 1)
print(len(myList))

# MIN() & MAX()
# Returns minimum or maximum of specified values 
print("min: ", min(4,10), "\n", max(5,11))

# POW() FUNCTION 
print(pow(10, 2))