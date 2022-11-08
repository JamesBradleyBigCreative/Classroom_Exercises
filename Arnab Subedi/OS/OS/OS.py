board = [
    ["1","1","1"],
    ["1","1","1"],
    ["1","1","1"],
    ]
def visualise():
    for i in range(3):
        for o in range(3):
            if o != 0:
                print("|",end = "")
            print(board[o][i],end ="")
        print("")
        if i != 2:
            print("-----------")
            
        
visualise()