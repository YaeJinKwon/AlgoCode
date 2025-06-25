import sys
import heapq

input = sys.stdin.readline


n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

ans = []
for j in range(n):
    heapq.heappush(ans,(-arr[n-1][j], n-1, j))

for _ in range(n-1):
    a, b, c = heapq.heappop(ans)
    heapq.heappush(ans,(-arr[b-1][c], b-1 , c))

print(-heapq.heappop(ans)[0])
