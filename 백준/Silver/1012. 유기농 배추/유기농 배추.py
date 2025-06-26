import sys
from collections import deque
input = sys.stdin.readline


di = [-1, 0 ,1 ,0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    v[i][j] = 1
    while(dq):
        i, j = dq.popleft()
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if(0<=ni and ni<N and 0<= nj and nj < M and v[ni][nj] == 0 and data[ni][nj]==1):
                dq.append((ni,nj))
                v[ni][nj] = 1

T = int(input())
for _ in range(T):

    M, N, K = map(int,input().split())

    data = [[0]*M  for _ in range(N)]
    v = [[0]*M for _ in range(N)]

    for _ in range(K):
        i, j = map(int, input().split())
        data[j][i] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1 and v[i][j] ==0:
                bfs(i,j)
                count+=1

    print(count)

            

