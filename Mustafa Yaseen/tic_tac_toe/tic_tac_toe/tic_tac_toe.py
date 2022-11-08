


board = [["O","X","O"],["O","O","X"],["X","X","O"]]

def visualise():
    for i in range(3):
        for j in range(3):
            if j !=0:                   
                print("|",end = "")
            print(board[i][j],end = "")

    print()
    if i != 2:
        print("------")
              
visualise()


