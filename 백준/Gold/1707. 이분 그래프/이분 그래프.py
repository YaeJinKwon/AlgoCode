import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v= map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    v = [0] * (V+1)

    def dfs(i, c):
        if c%2 == 0:
            v[i] = 1
        else:
            v[i] = 2
        for x in graph[i]:
            if v[x] == 0:
                if not dfs(x, c+1):
                    return False
            else:
                if v[x] == v[i]:
                    return False
        return True

    check = 0
    for i in range(1, V+1):
        if v[i] == 0:
            if not dfs(i,0):
                check = 1
                break
    if(check == 1):
        print('NO')    
    else:            
        print('YES')
