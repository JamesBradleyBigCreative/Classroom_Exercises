f = open("A.H.txt", "w")
f.write("This is being written from visual studio!")
f.close
f = open("A.H.txt", "r")
print (f.read())