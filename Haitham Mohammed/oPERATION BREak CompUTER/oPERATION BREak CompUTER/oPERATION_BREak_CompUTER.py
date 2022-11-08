for i in range(200000):
 a = open(f"hello{i}.txt","x")
 a.write("{2000000*20000000}")
 a.close()