import sys
import heapq
input = sys.stdin.readline
T = int(input())

def dijk(start):
    dq = []
    dis = [1e9]*(n+1)

    heapq.heappush(dq, (0, start))
    dis[start] = 0

    while(dq):
        dist, now = heapq.heappop(dq)
        if dist > dis[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if dis[i[0]] > cost:
                dis[i[0]] = cost
                heapq.heappush(dq, (cost, i[0]))
    return dis


for _ in range(T):
    n, m, t = map(int,input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    
    ans = []
    distanceS = dijk(s)
    distanceG = dijk(g)
    distanceH = dijk(h)
    for _ in range(t):
        x = int(input())
        if distanceS[x] == distanceS[g]+distanceG[h]+distanceH[x]:
            ans.append(x)
        elif distanceS[x] == distanceS[h]+distanceH[g]+distanceG[x]:
            ans.append(x)
    ans.sort()
    print(*ans)
