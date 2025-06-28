import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def made(a ,b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b



n, m = map(int,input().split())

parent = [0]*(n)
for i in range(n):
    parent[i] = i

for i in range(1,m+1):
    a, b = map(int,input().split())
    if(find(a) == find(b)):
        print(i)
        break
    else: made(a,b)
else:
    print(0)
