import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int,input().split()))
sortArr = sorted(list(set(arr)))

di = {}
for i in range(len(sortArr)):
    di[sortArr[i]] = i


for i in range(n):
    arr[i] = di.get(arr[i])

print(*arr)