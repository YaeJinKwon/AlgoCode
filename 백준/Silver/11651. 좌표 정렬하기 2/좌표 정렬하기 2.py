import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x : (x[0],x[1]) if x[0]==x[1] else (x[1],x[0]) )

for i, j in arr:
    print(i, j)
