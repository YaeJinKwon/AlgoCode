import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def make(a ,b):
    x = find(a) 
    y = find(b)
    if x<y:
        parent[y] = x
        
    else:
        parent[x] = y




n, m = map(int,input().split())

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i


for _ in range(m):
    c, a, b = map(int,input().split())
    if c == 0:
        make(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print("NO")



