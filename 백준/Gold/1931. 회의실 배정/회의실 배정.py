import sys

input = sys.stdin.readline

n = int(input())

time = []
for _ in range(n):
    x ,y = map(int,input().split())
    time.append((x,y))

time.sort(key= lambda x :(x[1],x[0]))


ans = 1
x , y = time[0]
for i in range(1,n):
    nx, ny = time[i]
    if y <= nx:
        ans+=1
        y = ny

print(ans)