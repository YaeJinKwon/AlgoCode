import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = []

def soon (c):
    if c == m:
        print(*arr)
        return
    for i in range(1,n+1):
        arr.append(i)
        soon(c+1)
        arr.pop()

soon(0)