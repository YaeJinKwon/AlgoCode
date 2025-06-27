import sys

input = sys.stdin.readline

n = int(input())
m = int(input())


graph = [[1e9]*(n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
            
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1e9:
            graph[i][j] = 0

for i in graph:
    print(*i)


