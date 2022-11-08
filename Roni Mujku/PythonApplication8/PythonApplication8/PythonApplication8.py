i = 4
listOfNames = []

while i > 3:
    listOfNames.insert(1,"Cameron"+ "_" + str(i))
    i += 1

for name in listOfNames:
    print(listOfNames)
