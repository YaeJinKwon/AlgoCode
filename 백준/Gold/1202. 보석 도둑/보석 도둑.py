import sys
import heapq
input = sys.stdin.readline

N, K = map(int,input().split())

jewel =[]
for _ in range(N):
    m, v = map(int,input().split())
    jewel.append((m,v))


bag = []
for _ in range(K):
    bag.append(int(input()))

jewel.sort()
bag.sort()
ans = 0
temp = []
j = 0
for i in range(K):
    b = bag[i]
    while(j<N and jewel[j][0] <= b ):
        m,v = jewel[j]
        heapq.heappush(temp, -v)
        j+=1
    if temp:
        ans +=  -heapq.heappop(temp)

print(ans)
        
