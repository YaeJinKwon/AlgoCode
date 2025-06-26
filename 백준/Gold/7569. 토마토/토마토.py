import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int,input().split())

graph = []
for _ in range(H):
    graph2 = []
    for _ in range(N):
        graph2.append(list(map(int,input().split())))
    graph.append(graph2)

di = [-1 ,0, 1, 0]
dj = [0, -1, 0, 1]
dx = [1,-1]


def bfs(m):
    dq = deque()
    for x in m:
        h, i, j = x
        dq.append((h, i, j))
    while(dq):
        h,i,j = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(0<=ni and ni<N and 0<= nj and nj < M  and graph[h][ni][nj] == 0):
                dq.append((h,ni,nj))
                graph[h][ni][nj] += graph[h][i][j]+1
        for k in range(2):
            nh = h + dx[k]
            if(0<=nh and nh<H and graph[nh][i][j] == 0):
                dq.append((nh,i,j))
                graph[nh][i][j] += graph[h][i][j]+1


m = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if(graph[h][i][j] == 1):
                m.append((h,i,j))

ans = 0
bfs(m)
for h in range(H):
    for i in range(N):
        for j in range(M):
            if(graph[h][i][j] == 0):
                print(-1)
                exit()
            ans = max(ans, graph[h][i][j])
print(ans-1)