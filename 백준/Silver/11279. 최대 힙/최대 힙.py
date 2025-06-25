import sys
import heapq

input = sys.stdin.readline


n = int(input())

arr = []
for _ in range(n):
    a = int(input())
    if a > 0:
        heapq.heappush(arr, -a)
    else:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)

