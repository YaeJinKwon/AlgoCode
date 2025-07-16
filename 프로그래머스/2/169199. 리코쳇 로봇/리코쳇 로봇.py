from collections import deque


def solution(board):
    
    dq = deque()
    dist = [[1e9]*len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if  board[i][j] == 'R':
                dq.append((i,j , 0))
                dist[i][j] = 0
                
                break
    di = [-1,0,1,0]
    dj = [0,1,0,-1]

    answer = -1

    while(dq):
        i,j,c = dq.popleft()
        if board[i][j] == 'G':
            answer = c
            break
        for x in range(4):
            ni = i
            nj = j
            while(0<=ni + di[x]<len(board) and 0<=nj + dj[x]<len(board[0]) and board[ni + di[x]][nj + dj[x]] != 'D'):
                ni += di[x]
                nj += dj[x]
            if dist[ni][nj] > c+1:
                dist[ni][nj] = c+1
                dq.append((ni,nj,c+1))

    return answer