import sys
import heapq

input = sys.stdin.readline


n = int(input())

arr = []
for _ in range(n):
    nums = list(map(int,input().split()))
    for i in nums:
        if len(arr)<n:
            heapq.heappush(arr,i)
        else:
            if arr[0] < i:
                heapq.heappop(arr)
                heapq.heappush(arr,i)
print(arr[0])