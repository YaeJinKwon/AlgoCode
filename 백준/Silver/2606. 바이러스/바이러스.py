import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())

data = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)


v = [0]*(N+1)

def bfs(R):
    v[R] = 1
    dq = deque()
    dq.append(R)
    c = 0
    while(dq):
        x = dq.popleft()
        for i in data[x]:
            if v[i] == 1:
                continue
            dq.append(i)
            v[i] = 1
            c+=1
    return c

ans = bfs(1)
print(ans)