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
node[1] = 1
dq = deque()
for i in graph[1]:
    dq.append((1,i))

while dq:
    parent, x = dq.popleft()
    node[x] = parent
    for i in graph[x]:
        if(node[i] == 0):
            dq.append((x, i))

for i in range(2, N+1):
    print(node[i])

