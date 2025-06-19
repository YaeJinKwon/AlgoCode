import sys
input = sys.stdin.readline
n = int(input())
arr = []
for k in range(n):
    i, j = input().rstrip().split()
    arr.append((int(i),j,k))

arr.sort(key=lambda x : (x[0], x[2]) )

for i, j, k in arr:
    print(i, j)