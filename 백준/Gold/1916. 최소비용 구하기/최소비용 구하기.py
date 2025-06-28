import sys
import heapq 
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))

start, end = map(int,input().split())

dp = []
dis = [1e9]*(N+1)
dis[start] = 0

heapq.heappush(dp,(0, start))
while(dp):
    dist, now = heapq.heappop(dp)
    if dist > dis[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < dis[i[0]]:
            dis[i[0]] = cost
            heapq.heappush(dp, (cost, i[0]))

print(dis[end])