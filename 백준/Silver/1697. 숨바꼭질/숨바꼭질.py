import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int,input().split())


data = [0]*(max(M,N)+2)

v = [0] *(max(M,N)+2)

dx = [1, -1]

def bfs(N):
    dq = deque()
    dq.append(N)
    v[N] = 1
    while(dq):
        x = dq.popleft()
        if(0<= x and 2*x<=M+1 and v[2*x] ==0):
                dq.append(2*x)
                v[2*x] = v[x]+1
        for i in range(2):
            nx = x + dx[i]
            if(0<= nx and nx<=(max(M,N)+1) and v[nx] ==0):
                dq.append(nx)
                v[nx] = v[x]+1
    return v[M]

ans = bfs(N)
print(ans-1)