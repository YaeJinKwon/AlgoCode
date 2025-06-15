import sys
from collections import deque
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

def wall(count, start):
    global answer
    if count == 3:
        count_virus = diff()
        answer = max(zero - count_virus - 3, answer)
        return
    for idx in range(start, n * m):
        i = idx // m
        j = idx % m
        if graph[i][j] == 0:
            graph[i][j] = 1
            wall(count + 1, idx + 1)
            graph[i][j] = 0


def diff():
    count = 0
    visitVir = [[False]*m for _ in range(n)]
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
    return count
                    


wall(0,0)
print(answer)