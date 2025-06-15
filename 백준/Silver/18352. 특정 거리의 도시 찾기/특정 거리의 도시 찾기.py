from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

data = [[]for _ in range (n+1)]

for i in range (m):
    a, b = map(int, input().split())
    data[a].append(b)

visited = [False]*(n+1)

answer = []
def bfs(start, level):
    dq = deque()
    dq.append((start,level))
    visited[start] = True
    while dq:
        now, lev= dq.popleft()
        if(lev == k):
            answer.append(now)
        if(lev > k):
            break
        for i in data[now]:
            if not visited[i]:
                visited[i] = True
                dq.append((i, lev+1))
        lev += 1
        
bfs(x,0)
answer.sort()
if len(answer) == 0:
    print(-1)
for i in answer:
    print(i)
    