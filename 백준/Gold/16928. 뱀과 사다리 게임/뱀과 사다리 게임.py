import sys
from collections import deque
input = sys.stdin.readline

N, M= map(int,input().split())
sada = dict()
for _ in range(N):
    x, y = map(int,input().split())
    sada[x] = y

bem = dict()
for _ in range(M):
    x, y = map(int,input().split())
    bem[x] = y

graph = [0]*101

def bfs():
    dq = deque()
    dq.append(1)
    graph[1] = 1
    while(dq):
        x = dq.popleft()
        if (x == 100):
            break
        if x in bem:
            t = bem[x]
            graph[t] = graph[x]
            x = t
        elif x in sada:
            t = sada[x]
            graph[t] = graph[x]
            x = t
        for i in range(1,7):
            nx = x + i
            if(nx<=100 and graph[nx] == 0):
                dq.append(nx)
                graph[nx] = graph[x] + 1
bfs()    
print(graph[100]-1)
