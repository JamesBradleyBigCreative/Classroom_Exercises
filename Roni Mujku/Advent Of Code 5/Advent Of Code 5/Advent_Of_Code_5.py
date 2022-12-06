def Part1():
    with open("input.txt",'r') as f:
        for line in f:
            #line.strip()
            line = line.split()
            #print(line)
            x = int(line[3]) - 1
            y = int(line[5]) - 1
            for i in range(int(line[1])):
                temp = list_of_stack[x].pop()
                #print(list_of_stack[y])
                list_of_stack[y].append(temp)
                #print(list_of_stack)
    print(stack1.pop(),stack2.pop(),stack3.pop(),stack4.pop(),stack5.pop())
    print(stack6.pop(),stack7.pop(),stack8.pop(),stack9.pop())


def Part2():
    with open("input.txt",'r') as f:
        for line in f:
            #line.strip()
            line = line.split()
            print(line)

            x = int(line[3]) - 1
            y = int(line[5]) - 1
            z = int(line[1])
            A = (len(list_of_stack[x])) - z
            to_move = list_of_stack[x][A:]
            print(to_move)
            del list_of_stack[x][A:]
            print(list_of_stack[x])
            for i in range (len(to_move)):
                list_of_stack[y].append(to_move[i])
            print(list_of_stack[y])


    print(stack1.pop(),stack2.pop(),stack3.pop(),stack4.pop(),stack5.pop())
    print(stack6.pop(),stack7.pop(),stack8.pop(),stack9.pop())

stack1 = ['T','R','G','W','Q','M','F','P']
stack2 = ['R','F','H']
stack3 = ['D','S','H','G','V','R','Z','P']
stack4 = ['G','W','F','B','P','H','Q']
stack5 = ['H','J','M','S','P']
stack6 = ['L','P','R','S','H','T','Z','M']
stack7 = ['L','M','N','H','T','P']
stack8 = ['R','Q','D','F']
stack9 = ['H','P','L','N','C','S','D']
stack1.reverse()
stack2.reverse()
stack3.reverse()
stack4.reverse()
stack5.reverse()
stack6.reverse()
stack7.reverse()
stack8.reverse()
stack9.reverse()
list_of_stack = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]

print(list_of_stack)

Part2()