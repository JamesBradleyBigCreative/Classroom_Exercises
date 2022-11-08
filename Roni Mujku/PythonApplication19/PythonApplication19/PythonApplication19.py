board = [["X","O","O"],["X","O","O"],["X","O","O"]]

def visualize():
    for i in range(3):
        for j in range(3):
            if j != 0:
                print(" | ", end = "")
            print(board[i][j], end = "")
        print("")
        if i != 2:
            print("---------")

visualize()

