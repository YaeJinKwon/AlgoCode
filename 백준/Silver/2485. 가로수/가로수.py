import sys
import math
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

M = []
for i in range(n-1):
    M.append(arr[i+1] - arr[i])

n = math.gcd(*M)

c =0
for i in M:
    c += i//n -1

print(c)