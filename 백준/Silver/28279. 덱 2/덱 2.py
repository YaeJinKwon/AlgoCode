import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque()
for _ in range(n):
    a = list(map(int,input().split()))

    if a[0] == 1:
        arr.appendleft(a[1])
    elif a[0] == 2:
        arr.append(a[1])
    elif a[0] == 3:
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif a[0] == 4:
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif a[0] == 5:
        print(len(arr))
    elif a[0] == 6:
        if arr:
            print(0)
        else: print(1)
    elif a[0] == 7:
        if arr:
            print(arr[0])
        else: print(-1)
    elif a[0] == 8:
        if arr:
            print(arr[-1])
        else: print(-1)
