import sys
import heapq

input = sys.stdin.readline

N, E = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

def dijk(start, end):
    dq = []
    dist = [1e9] * (N+1)

    heapq.heappush(dq, (0, start))
    dist[start] = 0

    while dq:
        dis, now = heapq.heappop(dq)
        if dis > dist[now] :
            continue
        for i in graph[now]:
            cost = dist[now] + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(dq, (cost, i[0]))

    return dist[end]

ans = dijk(1, v1)
ans += dijk(v1, v2)
ans += dijk(v2, N)

ans2 = dijk(1, v2)
ans2 += dijk(v2, v1)
ans2 += dijk(v1, N)


if ans >= 1e9:
    print(-1)
else:  
    print(min(ans,ans2))