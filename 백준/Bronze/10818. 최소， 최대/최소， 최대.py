import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

print(min(array), end= " ")
print(max(array), end= " ")
