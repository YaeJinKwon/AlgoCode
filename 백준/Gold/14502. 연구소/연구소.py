import sys
from collections import deque
import copy
input = sys.stdin.readline

# input
n, m = map(int, input().split())

graph = []


for i in range(n):
    graph.append(list(map(int, input().split())))



# find virus
virus = []
zero = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i,j))
        elif graph[i][j] == 0:
            zero += 1



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


answer = 0

def wall(c):
    
    if(c == 3):
        diff()
        return
    for i in range (n):
        for j in range(m):
            if(graph[i][j] == 0):
                graph[i][j] = 1
                wall(c+1)
                graph[i][j] = 0

Vir = [[False]*m for _ in range(n)]

def diff():

    count = 0
    visitVir = copy.deepcopy(Vir)

    for vir in virus:
        dq = deque([(vir[0],vir[1])])
        visitVir[vir[0]][vir[1]] = True
        while dq:
            x, y = dq.popleft()
            for i in range (4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(0<=nx and nx<n and 0<=ny and ny<m and not visitVir[nx][ny] and graph[nx][ny] == 0):
                    visitVir[nx][ny] = True
                    count += 1
                    dq.append((nx,ny))
    global answer
    answer = max(zero - count -3, answer)
                    


wall(0)
print(answer)