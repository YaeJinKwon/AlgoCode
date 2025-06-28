import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def find(a):
    if parent[a] !=a:
        parent[a] = find(parent[a])
    return parent[a]

def made(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(T):
    N, M = map(int,input().split())
    parent = [0]*(N+1)
    for i in range(1, N+1):
        parent[i] = i
    c = 0
    for i in range(M):
        a ,b = map(int,input().split())
        if(find(a) != find(b)):
            c+=1
            made(a,b)
    print(c)