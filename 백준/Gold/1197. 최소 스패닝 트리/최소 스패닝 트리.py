import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int,input().split())
parent = [0]*(V+1)

for i in range(1, V+1):
    parent[i] = i

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def made(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[a] = b

    else:
        parent[b] = a
arr = []
for i in range(E):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))

arr.sort()
cost = 0
for i in arr:
    c, a, b = i
    if (find(a) != find(b)):
        made(a,b)
        cost += c
print(cost)
    
