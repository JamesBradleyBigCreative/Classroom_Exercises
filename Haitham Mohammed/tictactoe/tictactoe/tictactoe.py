board = [["o","x","o"],["x","x","x"],["o","o","o"]]

def visulise():
    for i in range(3):
        for j in range(3):
            if j != 0:
                print("|", end = "")
            print(board[i][j], end= "")
        print()
        if i != 2:
            print("-----")
visulise()