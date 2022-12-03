input_file1 = 'input.txt'

def Part1(input_file):
    test = 0
    f = open(input_file,'r')

    for line in f:
        if 'A' in line and 'X' in line:
            test += 4
        elif 'A' in line and 'Y' in line:
            test += 8
        elif 'A' in line and 'Z' in line:
            test += 3

        elif 'B' in line and 'X' in line:
            test += 1
        elif 'B' in line and 'Y' in line:
            test += 5
        elif 'B' in line and 'Z' in line:
            test += 9

        elif 'C' in line and 'X' in line:
            test += 7
        elif 'C' in line and 'Y' in line:
            test += 2
        elif 'C' in line and 'Z' in line:
            test += 6

    print(test)

def Part2(input_file):
    test = 0
    f = open(input_file,'r')

    for line in f:
        if 'A' in line and 'X' in line:
            test += 3
        elif 'A' in line and 'Y' in line:
            test += 4
        elif 'A' in line and 'Z' in line:
            test += 8

        elif 'B' in line and 'X' in line:
            test += 1
        elif 'B' in line and 'Y' in line:
            test += 5
        elif 'B' in line and 'Z' in line:
            test += 9

        elif 'C' in line and 'X' in line:
            test += 2
        elif 'C' in line and 'Y' in line:
            test += 6
        elif 'C' in line and 'Z' in line:
            test += 7

    print(test)

Part2(input_file1)