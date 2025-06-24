import sys

input = sys.stdin.readline

s = input().rstrip()

q = int(input())


for _ in range(q):
    a, l, r = map(str ,input().split())
    l = int(l)
    r = int(r)
    sub = s[l:r+1]
    if a in sub:
        print(sub.count(a))
    else:
        print(0)