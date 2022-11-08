listOfNames = []

i = 0
while i < 3:
    listOfNames.insert(i,"Cameron"+ "_" + str(i + 1))
    i += 1

for name in listOfNames:
     print(name)
