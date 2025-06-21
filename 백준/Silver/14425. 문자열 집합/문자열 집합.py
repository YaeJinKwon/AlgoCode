import sys

input = sys.stdin.readline
n, m = map(int, input().split())


S = set()
for i in range(n):
    S.add(input().rstrip())

count = 0
for i in range(m):
    c = input().rstrip()
    if(c in S):
        count +=1

print(count)
