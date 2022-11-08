
board = [[" ", "X", "O"], ["O", " ", "X"], ["X", "X", "O"]]

def visualize():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = "")
        print("\n")

visualize()