listOfNames = []

i = 0# change i to 0
while i < 4:#added colon
    listOfNames.insert(i,"Cameron" + "_"+str(i+1))

    i += 1

for name in listOfNames:
    print(name) #fix on indentation
