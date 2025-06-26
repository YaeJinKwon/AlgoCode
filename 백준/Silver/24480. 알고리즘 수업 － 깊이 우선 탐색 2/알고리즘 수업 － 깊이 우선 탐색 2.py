import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int,input().split())

data = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

for i in data:
    i.sort(reverse = True)

check = [0]*(N+1)

c = 0
def dfs(R):
    global c
    c+=1
    check[R] = c 
    for i in data[R]:
        if(check[i] > 0):
            continue
        dfs(i)

dfs(R)

for i in range(1, N+1):
    print(check[i])