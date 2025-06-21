import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))

arr = deque()

for i in range(n):
    if A[i] == 0:
        arr.append(B[i])

for i in C:
    arr.appendleft(i)
    print(arr.pop(), end=" ")
