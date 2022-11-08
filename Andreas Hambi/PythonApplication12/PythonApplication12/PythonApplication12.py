board = [ [ "O", "X", "O" ],[ "X", "X ", "O" ],[ "O", "O", "X"] ]

def visualize(): 
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = "")
        print()

visualize()