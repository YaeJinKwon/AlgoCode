import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

v = [[0]*M for _ in range(N)]
di = [-1 ,0, 1, 0]
dj = [0, -1, 0, 1]


def bfs(m):
    dq = deque()
    c = 0
    for x in m:
        i, j = x
        dq.append((i, j, 0))
        v[i][j] = 1
    while(dq):
        i,j,c = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(0<=ni and ni<N and 0<= nj and nj < M and v[ni][nj] == 0 and graph[ni][nj] == 0):
                dq.append((ni,nj,c+1))
                graph[ni][nj] = 1
    return c

m = []
for i in range(N):
    for j in range(M):
        if(graph[i][j] == 1):
           m.append((i,j))

ans = bfs(m)

for i in range(N):
    for j in range(M):
        if(graph[i][j] == 0):
            ans = -1
            break
print(ans)
