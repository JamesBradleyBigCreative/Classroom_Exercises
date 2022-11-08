board = [["  ", "  ", "  "],["  ", "  ", "  "],["  ","  ","  "]]

def vizualise():
    for i in range(3):
        for j in range(3):
            if j != 0:
                print(" | ",end = " " )
            print(board[i][j], end = " ")

        print()


vizualise()
