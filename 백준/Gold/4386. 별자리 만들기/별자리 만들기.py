import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
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
for i in range(V):
    a, b = map(float, input().split())
    arr.append((a, b))

line = []

for i in range(V):
    for j in range(i+1,V):
        d = (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2 
        line.append((math.sqrt(d), i, j))

line.sort()

cost  = 0
for i in line:
    c , a , b = i
    if find(a) != find(b):
        made(a,b)
        cost += c

print(cost)


    
