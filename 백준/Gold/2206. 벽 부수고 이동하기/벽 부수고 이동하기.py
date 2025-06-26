import sys
from collections import deque
input = sys.stdin.readline

N, M= map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

wall = []
wall.append((0,0))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            wall.append((i,j))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

v = [[[1e9]*2 for _ in range(M)] for _ in range(N)]


def bfs():
    dq = deque()
    dq.append((0,0,0))
    v[0][0][0] = 1
    while(dq):
        i, j, wall = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (0<=ni and ni <N and 0<= nj and nj < M ):
                if(graph[ni][nj] == 0 and v[ni][nj][wall] == 1e9):
                    dq.append((ni,nj,wall))
                    v[ni][nj][wall] = v[i][j][wall]+1

                elif(graph[ni][nj] == 1 and v[ni][nj][wall] == 1e9 and wall == 0):
                    dq.append((ni,nj,wall+1))
                    v[ni][nj][wall+1] = v[i][j][wall]+1

bfs()
ans1 = v[N-1][M-1][0]
ans2 = v[N-1][M-1][1]
ans = min(ans1,ans2)
if ans == 1e9:
    ans = -1
print(ans)