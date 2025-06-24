import sys

input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
total = [0]*(n+1)
total[1] = arr[0]
for i in range(2, n+1):
    total[i] += total[i-1] +arr[i-1]

for _ in range(m):
    i, j = map(int,input().split())
    print(total[j] - total[i-1])