import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int,input().split())

data = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

for i in data:
    i.sort()

v = [0]*(N+1)

def bfs(R):
    v[R] = 1
    c = 2
    dq = deque()
    dq.append(R)
    while(dq):
        x = dq.popleft()
        for i in data[x]:
            if v[i] >= 1:
                continue
            dq.append(i)
            v[i] = c
            c+=1

bfs(R)
for i in range(1, N+1):
    print(v[i])