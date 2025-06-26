import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
data = []

for _ in range(N):
    data.append(list(map(int,input().rstrip())))



di = [-1, 0 ,1 ,0]
dj = [0, 1, 0, -1]

danji = []

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    v[i][j] = 1
    c = 0
    while(dq):
        i, j = dq.popleft()
        c +=1
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if(0<=ni and ni<N and 0<= nj and nj < N and v[ni][nj] == 0 and data[ni][nj]==1):
                dq.append((ni,nj))
                v[ni][nj] = 1
    danji.append(c)


v = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and v[i][j] == 0:
            bfs(i,j)

print(len(danji))
danji.sort()
for i in danji:
    print(i)
    