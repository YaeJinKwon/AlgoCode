import sys
import heapq

input = sys.stdin.readline

N , M = map(int, input().split())

graph = [[] for _ in range(N+1)]
ind = [0] * (N+1)
for _ in range (M):
    a, b = map(int,input().split())
    graph[a].append(b)
    ind[b] += 1

dp = []

for i in range(1,len(ind)):
    if ind[i] == 0:
        heapq.heappush(dp , i)

ans = []
while(dp):
    a = heapq.heappop(dp)
    ans.append(a)
    for x in graph[a]:
        ind[x] -= 1
        if ind[x] == 0:
            heapq.heappush(dp, x)
print(*ans)