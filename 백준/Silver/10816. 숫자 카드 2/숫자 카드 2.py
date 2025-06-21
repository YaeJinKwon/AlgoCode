import sys

input = sys.stdin.readline

n= int(input())

d = dict()
a = list(map(int,input().split()))
for i in a:
    if i not in d:
        d[i] =1
    else:
        d[i] += 1

m = int(input())
b = list(map(int,input().split()))
ans = []
for i in b:
    if i in d:
        ans.append(d[i])
    else:
        ans.append(0)

print(*ans)