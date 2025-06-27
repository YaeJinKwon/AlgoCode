import sys
import heapq

input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

dq = []
dis = [1e9]*(V+1)
heapq.heappush(dq, (0, K))
dis[K] = 0

while(dq):
    dist, now = heapq.heappop(dq)
    if dis[now] < dist:
        continue
    for i in graph[now]:
        cost = dist+i[1]
        if cost < dis[i[0]]:
            dis[i[0]] = cost
            heapq.heappush(dq, (cost, i[0]))

for i in range(1,V+1):
    if dis[i] == 1e9:
        print("INF")
    else:
        print(dis[i])


