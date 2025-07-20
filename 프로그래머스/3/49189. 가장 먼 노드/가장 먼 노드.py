import heapq


def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append((e[1],1))
        graph[e[1]].append((e[0],1))
        
    dist = [1e9]*(n+1)
    dist[0] = 0
    dist[1] = 0
    dq = []
    heapq.heappush(dq,(1,0))
    while dq:
        now, dis = heapq.heappop(dq)
        if dis > dist[now]:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(dq, (i[0], cost))
    answer = 0
    m = max(dist)
    for d in dist:
        if d == m:
            answer +=1

    return answer