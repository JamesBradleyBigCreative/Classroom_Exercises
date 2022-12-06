def Part1():
    with open("input.txt","r") as f:
        chars = []
        for letter in f:
            chars = [*letter]
        
        #print(chars)
        i = 4

        while i < len(chars):
            temp_list = [chars[i-1],chars[i-2],chars[i-3],chars[i-4]]
            print(temp_list)
            if len(temp_list) != len(set(temp_list)):

                i += 1
            else:
                print(i)
                break

def Part2():
    with open("input.txt","r") as f:
        chars = []
        for letter in f:
            chars = [*letter]
        
        #print(chars)
        i = 14
        x = 0

        while i < len(chars):

            temp_list = []
            j = 14 + x

            while j > x:
                temp_list.append(chars[j-1])
                j -= 1

            print(temp_list)
            if len(temp_list) != len(set(temp_list)):

                i += 1
                x += 1
            else:
                print(i)
                break


#Part1()
Part2()