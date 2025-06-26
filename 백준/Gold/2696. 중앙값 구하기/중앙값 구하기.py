import sys
import heapq
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range((n//10)+1):
        arr.extend(list(map(int,input().split())))
    ans =[]
    left = []
    right = []
    mid = arr[0]
    ans.append(mid)
    for i in range(1, n):
        if mid > arr[i]:
            heapq.heappush(left, -arr[i])
        else:
            heapq.heappush(right, arr[i])


        if i % 2 == 0:
            if len(left) > len(right) :
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            elif len(right )> len(left):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            ans.append(mid)
        
    
    print(len(ans))

    for i in range(0, len(ans),10):
        print(*ans[i:i+10])


        