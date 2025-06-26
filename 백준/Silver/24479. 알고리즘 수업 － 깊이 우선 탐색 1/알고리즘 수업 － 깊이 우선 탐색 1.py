import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int,input().split())

data = []

for _ in range(M):
    u, v = map(int, input().split())
    data.append((u, v))

data.sort(key=lambda x : (x[0], x[1]))

graph = [[] for _ in range(N+1)]

for u, v in data:
    graph[u].append(v)
    graph[v].append(u)


check = [0]*(N+1)

c = 0
def dfs(R):
    global c
    c+=1
    check[R] = c 
    for i in graph[R]:
        if(check[i] > 0):
            continue
        dfs(i)

dfs(R)

for i in range(1, N+1):
    print(check[i])