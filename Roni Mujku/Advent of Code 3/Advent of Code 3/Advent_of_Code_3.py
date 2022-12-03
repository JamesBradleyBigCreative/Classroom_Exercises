import string

mydict = {}

def read_input(filename : str):
    rucksacks = []
    with open(filename, 'r') as file:
        for line in file:
            rucksacks.append(line.strip())
    return rucksacks


def dictmaker():
    alphabet=list(string.ascii_lowercase)+list(string.ascii_uppercase)
    nums = []
    for i in range (52):
        nums.append(i+1)


    for key in alphabet:
        for value in nums:
            mydict[key] = value
            nums.remove(value)
            break


def Part1Attempt(Input):
    total = 0
    for line in Input:
        string1 = slice(0,len(line)//2)
        string2 = slice(len(line)//2,len(line))
        for i in range(len(line[string1])-1):
            if line[string1][i] == line[string2][i]:
                x = mydict[line[string1][i]]
                total += x
    return total

def Part1(Input):
    total = 0
    shared = []
    for item in Input:
        firsthalf = item[:len(item)//2]
        secondhalf = item[len(item)//2:]
        print(firsthalf)
        print(secondhalf)
        for i in range(len(firsthalf)):
            if firsthalf[i] in secondhalf:
                shared.append(firsthalf[i])
                x = mydict[firsthalf[i]]
                total += x
                print(firsthalf[i])
                print(x)
                print(total)
                break
    return total

def Part2(Input):
    total = 0
    i = 0
    while i < len(Input):
        i2 = i + 1
        i3 = i + 2
        print(Input[i],Input[i2],Input[i3])
        for char in Input[i]:
            if char in Input[i2] and char in Input[i3]:
                x = mydict[char]
                total += x
                print(char)
                print(x)
                print(total)
                break
        i += 3
    return total

Input = "input.txt"
d = read_input(Input)
#print(d)

dictmaker()

x = Part2(d)

print(x)