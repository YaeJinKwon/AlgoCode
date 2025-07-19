def findO(board):
    v = [[0] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O" and v[i][j] == 0:
                v[i][j] = 1
                countR = 0
                countC = 0
                countZ = 0
                countY = 0
                for k in range(3):
                    if board[i][k] == "O":
                        countR+=1
                    if board[k][j] == "O":
                        countC+=1
                    if board[k][k] == "O":
                        countZ+=1
                    if board[k][2-k] =="O":
                        countY +=1
                if countR == 3 or countC == 3 or countZ == 3 or countY == 3:
                    return True
                
    return False
        
def findX(board):
    v = [[0] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X" and v[i][j] == 0:
                v[i][j] = 1
                countR = 0
                countC = 0
                countZ = 0
                countY = 0
                for k in range(3):
                    if board[i][k] == "X":
                        countR+=1
                    if board[k][j] == "X":
                        countC+=1
                    if board[k][k] == "X":
                        countZ+=1
                    if board[k][2-k] =="X":
                        countY +=1
                if countR == 3 or countC == 3 or countZ == 3 or countY == 3:
                    return True
                
    return False

def solution(board):
    countX = 0
    countO = 0
    for line in board:
        for i in line:
            if i == 'O':
                countO +=1
            elif i == 'X':
                countX +=1
    if(countX > countO):
        return 0
    elif(countO-countX>1):
        return 0
    else:
        a = findO(board)
        b = findX(board)
        if (countO == countX):
            if a:
                return 0
        if (countO == countX+1):
            if b:
                return 0
        if (a and b):
            return 0
    return 1