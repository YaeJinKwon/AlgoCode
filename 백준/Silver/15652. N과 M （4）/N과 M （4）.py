import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = []

def soon (c, s):
    if c == m:
        print(*arr)
        return
    for i in range(s,n+1):
        arr.append(i)
        soon(c+1, i)
        arr.pop()

soon(0, 1)