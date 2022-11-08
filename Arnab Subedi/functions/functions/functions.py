from email.errors import InvalidBase64CharactersDefect


list1 = [0,1,1,0]
list2 = [3,20,11,22]

#all function
x = all(list1)
print(x)

#Any function
x = any(list1)
print(x)

# dir function
class Person:
    name = "cam"
    age = 29
print(dir(Person))

#Casting
num = int(5.9)
num2 = float(5)
num3 = str(5.666)

print(f"{num3} type: {type(num3)}")

#isinstance

num = 7
print(isinstance(num,int))

#len

hello ="hello world"
print(len(hello))

#min and max

print(f"minimum: {min(list2)} Maximum: {max(list2)}")

#pow

print(pow(2,10))