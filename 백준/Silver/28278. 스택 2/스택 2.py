import sys, math
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    x = list(map(int,input().split()))
    if x[0] == 1:
        arr.append(x[1])
    elif x[0] == 2:
        if len(arr)>0:
            print(arr.pop())
        else:
            print(-1)
    elif x[0] == 3:
        print(len(arr))
    elif x[0] == 4:
        if len(arr)>0:
            print(0)
        else:
            print(1)
    elif x[0] == 5:
        if len(arr)>0:
            print(arr[-1])
        else:
            print(-1)