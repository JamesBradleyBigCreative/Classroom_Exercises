def Part1():
    total = 0
    with open("input.txt",'r') as f:
        for line in f:
            x = line.strip()
            x = x.split(',')
            y = x[0].split('-')
            z = x[1].split('-')
            uB1,uB2,lB1,lB2 = int(y[1]),int(z[1]),int(y[0]),int(z[0])
            print(x,y,z)
            if uB1 >= uB2 and lB1 <= lB2:
                print(uB1)
                total += 1
                print(f"\nFirst if passed| Total: {total}\n")
            elif uB2 >= uB1 and lB2 <= lB1:
                total += 1
                print(f"\nSecond if passed| Total: {total}\n")
            else:
                print("NOTHING")
    return total

def Part2():
    total = 0
    with open("input.txt",'r') as f:
        for line in f:
            x = line.strip()
            x = x.split(',')
            y = x[0].split('-')
            z = x[1].split('-')
            uB1,uB2,lB1,lB2 = int(y[1]),int(z[1]),int(y[0]),int(z[0])
            print(x,y,z)
            if uB1 >= uB2 and lB1 <= lB2:
                total += 1
                print(f"\nFirst if passed| Total: {total}\n")

            elif uB2 >= uB1 and lB2 <= lB1:
                total += 1
                print(f"\nSecond if passed| Total: {total}\n")

            elif uB1 >= lB2 and uB1 <= uB2:
                total += 1
                print(f"\nThird if passed| Total: {total}\n")

            elif uB2 >= lB1 and uB2 <= uB1:
                total += 1
                print(f"\nFourth if passed| Total: {total}\n")

            else:
                print("NOTHING")
    return total

#print(Part1())
        
print(Part2())        

