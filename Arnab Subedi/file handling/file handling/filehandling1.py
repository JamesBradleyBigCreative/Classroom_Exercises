import os
i =3
for m in range(1000000):
    i+=1
    os.remove(f"file{i}.txt")
