import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

graph = [[]for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


node = [0] * (N+1)
dq = deque()
dq.append(1)

while dq:
    x = dq.popleft()
    for i in graph[x]:
        if(node[i] == 0):
            node[i] = x
            dq.append(i)

for i in range(2, N+1):
    print(node[i])

