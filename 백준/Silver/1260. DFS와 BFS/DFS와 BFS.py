import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()



cDfs = []

def dfs(V):
    global c
    v[V] = 1
    cDfs.append(V)
    for i in graph[V]:
        if v[i] == 0:
            dfs(i)

cBfs = []
def bfs(V):
    v[V] = 1
    cBfs.append(V)
    dq = deque()
    dq.append(V)
    while(dq):
        x = dq.popleft()
        for i in graph[x]:
            if v[i] == 0:
                v[i] = 1
                dq.append(i)
                cBfs.append(i)

v = [0] * (N+1)
dfs(V)
v = [0]* (N+1)
bfs(V)

print(*cDfs)
print(*cBfs)
                