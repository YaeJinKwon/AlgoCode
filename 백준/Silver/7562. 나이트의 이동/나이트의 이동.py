import sys
from collections import deque
input = sys.stdin.readline

di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1,  1,  2, 2, 1 ,-1, -2]

def bfs(now):
    dq = deque()
    i, j = now
    dq.append((i,j))
    v[i][j] = 1
    while(dq):
        i, j = dq.popleft()
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if(0<= ni and ni < l and 0<= nj and nj<l and v[ni][nj] == 0):
                dq.append((ni, nj))
                v[ni][nj] = v[i][j] +1




T = int(input())

for _ in range(T):
    l = int(input())
    now = list(map(int,input().split()))
    go = list(map(int,input().split()))
    v = [[0]*l for _ in range(l)]
    bfs(now)
    print(v[go[0]][go[1]]-1)