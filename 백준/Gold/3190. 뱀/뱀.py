from collections import deque

n = int(input())
k = int(input())

graph = [[0]*n for _ in range(n)]

for i in range(k):
    r, l = map(int, input().split())
    graph[r-1][l-1] = 2


l = int(input())

lotate = deque()
for i in range(l):
    x, c = map(str, input().split())
    lotate.append((int(x), c))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

lot = 1
snake = deque()

time = 0
lt, lc = lotate.popleft()
x= 0
y= 0
snake.append((0,0))
while(True):
    time += 1 
    x = x + dx[lot]
    y = y + dy[lot]
    if (x<0 or x >=n or y<0 or y>=n or graph[x][y] == 1):
        break
    if graph[x][y] == 2:
        graph[x][y] = 1
        snake.append((x,y))
    else:
        graph[x][y] = 1
        snake.append((x,y))
        tx, ty = snake.popleft()
        graph[tx][ty] = 0
    if lt == time:
        if lc == 'L':
            lot -= 1
            if lot == -1:
                lot =3
        elif lc == 'D':
            lot += 1
            if lot == 4:
                lot = 0
        if(len(lotate)>0):
            lt, lc = lotate.popleft()


    
print(time)

