import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[1e9]*(n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a-1][b-1] = c


for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


ans = 1e9
for i in range(n):
    ans = min(ans, graph[i][i])

if ans == 1e9:
    print(-1)
else:
    print(ans)
    

