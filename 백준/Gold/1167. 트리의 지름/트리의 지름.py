import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]

for i in range(V):
    data = list(map(int,input().split()))
    for i in range(1, len(data)-1,2):
        if(data[i+1]==-1):
            break
        graph[data[0]].append((data[i],data[i+1]))


maxnode = 0
maxdist = 0

def dfs(i, cost):
    global maxnode, maxdist
    visit[i] = 1
    if cost >= maxdist:
        maxdist = cost
        maxnode = i
    for x in graph[i]:
        a, d = x
        if visit[a] == 0:
            dfs(a,cost+d)



visit = [0] * (V+1)
dfs(1,0)
visit = [0] * (V+1)
dfs(maxnode,0)
print(maxdist)