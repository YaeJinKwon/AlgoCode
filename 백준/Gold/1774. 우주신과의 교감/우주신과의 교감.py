import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
parent = [0]*(N+1)

for i in range(1, N+1):
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

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

line = []

for i in range(N):
    for j in range(i+1,N):
        d = (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2 
        line.append((math.sqrt(d), i+1, j+1))

line.sort()



for i in range(M):
    a, b = map(int,input().split())
    made(a, b)
cost  = 0
for i in line:
    c , a , b = i
    if find(a) != find(b):
        made(a,b)
        cost += c

print(format(round(cost,3),'0.2F'))
