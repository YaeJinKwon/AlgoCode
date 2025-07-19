from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(maps, start, end):
    v = [[0]*len(maps[0]) for _ in range(len(maps))]
    dq = deque()
    dq.append((start[0][0], start[0][1], 0))
    while(dq):
        i, j, c= dq.popleft()
        if i == end[0][0] and j == end[0][1]:
            return c
        for k in range(4):
            ni = i+ di[k]
            nj = j +dj[k]
            if(0<=ni<len(maps) and 0<=nj<len(maps[0]) and maps[ni][nj] != 'X' and v[ni][nj] == 0):
                v[ni][nj] = 1
                dq.append((ni, nj, c+1))
    return -1

def solution(maps):
    start = []
    leb = []
    exit = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start.append((i,j))
            elif maps[i][j] == 'L':
                leb.append((i,j))
            elif maps[i][j] == 'E':
                exit.append((i,j)) 
    answer = 0
    count1 = bfs(maps, start, leb)
    count2 = bfs(maps, leb, exit)
    if( count1 == -1 or count2 == -1):
        return -1
    else: 
        answer = count1+ count2
    return answer