import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = set()
b = set()
for _ in range(n):
    d.add(input().rstrip())

for _ in range(m):
    b.add(input().rstrip())

a = list(d & b)
a.sort()
print(len(a))
for i in a:
    print(i)