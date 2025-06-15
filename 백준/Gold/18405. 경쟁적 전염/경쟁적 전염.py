import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 정보 수집 및 정렬
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))  # (virus 번호, i, j)
virus.sort()

def bfs():
    dq = deque()
    for vir, i, j in virus:
        dq.append((i, j, 0, vir))  # (i, j, time, virus 번호)

    while dq:
        i, j, time, vir = dq.popleft()
        if time == s:
            return
        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 0:
                graph[ni][nj] = vir
                dq.append((ni, nj, time + 1, vir))

bfs()
print(graph[x - 1][y - 1])
