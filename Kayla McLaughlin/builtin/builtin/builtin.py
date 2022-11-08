


MyList = [0,1,0,1]
# all() function = Returns true if all elements in data structure are true otherwise will return false. 0 = false.
x = all(MyList)
#print(x)

# any() function = checks if any element in the structure is true. if so will return true. (if at least one is true, will print true) 
y = any(MyList) 
print(y)

# dir() = returns properties of specified object
class person:
    name = "kayla"
    age = 17

print(dir(person))

#casting - converting one data type to another. eg int('float') = integer. 

num = int(5.00)
num2 = float(5)
num3 = str(5.676)
print (num2)

#type - returns the data type.

print (num3, ". Type", type(num3))

# isinstance() - returns true or false depending on if the variable matches the specified data type. e.g is x a float? = false 

x = 5
print(isinstance(x,float))

#len() - prints the length of the mentioned data structure.
print(len(MyList))

# min() or max() returns minimum (smallest) or maximum (largest) of specified values
print(min(4,10))

# pow() - returns - to the power of - 
print(pow(5,10))