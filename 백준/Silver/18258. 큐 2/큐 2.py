import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque()
for _ in range(n):
    data = list(map(str, input().rstrip().split()))
    if data[0] == 'push':
        arr.append(data[1])
    elif data[0] == 'pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(arr))
    elif data[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)