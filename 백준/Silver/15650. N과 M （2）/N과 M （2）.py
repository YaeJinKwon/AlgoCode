import sys
input = sys.stdin.readline

N, M = map(int,input().split())


arr = [0] * M
v = [False] * (N+1)
def soo(c, s):
    if (c == M):
        print(*arr)
        return
    for i in range(s,N+1):
        arr[c] = i
        soo(c+1, i+1)

soo(0,1)

    