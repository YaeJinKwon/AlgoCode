import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

m = max(array)

for i in range(n):
    array[i] = array[i] / m * 100

print(sum(array)/n)