import sys

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range((n//10)+1):
        arr.extend(list(map(int,input().split())))
    ans =[]
    h = []
    for i in range(0,n):
        h.append(arr[i])
        if i%2 == 0:
            h.sort()
            ans.append(h[len(h)//2])
    print(len(ans))
    c = 0
    for i in range(len(ans)):
        if (c>9):
            c= 0
            print()
        c+=1
        print(ans[i], end = " ")