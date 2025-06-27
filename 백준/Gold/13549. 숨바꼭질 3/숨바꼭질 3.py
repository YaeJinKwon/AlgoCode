import sys
import heapq

input = sys.stdin.readline

N, K = map(int,input().split())

dq = []
dis = [1e9] * 100002
heapq.heappush(dq, (0, N))

dis[N] = 0

while(dq):
    dist, now = heapq.heappop(dq)
    if dis[now] < dist:
        continue
    if(0<=now*2  and now*2 <len(dis)):
        cost = dist
        if(dis[now*2] > cost):
            dis[now*2] = cost
            heapq.heappush(dq,(cost, now*2))  
    for i in (now-1, now+1):
        if(0<=i and i<len(dis)):
            cost = dist + 1
            if(dis[i] > cost):
                dis[i] = cost
                heapq.heappush(dq,(cost, i))

print(dis[K])
