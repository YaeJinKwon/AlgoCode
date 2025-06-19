import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())
arr = set(arr)
arr = list(arr)
arr.sort(key=lambda x : (len(x), x) )

for i in arr:
    print(i)
