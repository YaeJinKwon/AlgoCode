import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int,input().split())
data = []
for i in range(N):
    data.append(list(map(int, input().rstrip())))

v = [[0]*M for _ in range(N)]

di = [-1, 0 ,1 ,0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    dq = deque()
    dq.append((i, j, 1))
    v[i][j] = 1
    while(dq):
        i, j, c = dq.popleft()
        if(i == N-1 and j == M-1):
            return c
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if(0<=ni and ni<N and 0<= nj and nj < M and v[ni][nj] == 0 and data[ni][nj]==1):
                dq.append((ni,nj, c+1))
                
                v[ni][nj] = 1
    return c

ans = bfs(0,0)
print(ans)
