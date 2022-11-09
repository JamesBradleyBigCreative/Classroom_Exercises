array = [1,0,0,1,0]
# len: calculates length of structure
print(len(array))
# remove: removes specified detail of structure
array.remove(1)
print(array)
# all: checks if all items in structure are true
x = all(array)
print(x)
# pop: removes indexes based on specified elemenrs and the last element is popped it is not specified.
array.pop()
print(array)
# any: similar to all but checks if any elements in the structure are true , if so it will return true.
b = any(array)
print(x)
# bin: finds binary equivalent of inpuited number
print(bin(33))
# dir(): returns properties of specified object(class and functions)
print(dir(array))
# casting : int(), str(), float() , bool()
num = int(5.0)
num2 = float(4)
num3 = str(3333333333.333444443)
#type , returns data type 
print(type(444))

#isInstance checks whether data type is the one specified
print(isinstance(3,bool))

# min and max : returns minimum or maximum of specified values
print(min(4,10))
print(max(4,10))

# pow: value of the indicies of the specified values
print(pow(2, 10000000000000000000000000000000000000000000000000000000000000000000000000000000))
