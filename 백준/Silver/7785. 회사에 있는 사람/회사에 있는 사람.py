import sys

input = sys.stdin.readline
n = int(input())

check = set()

for _ in range(n):
    name, ch = input().rstrip().split()
    if(ch == 'enter'):
         check.add(name)
    if(ch == 'leave'):
         check.remove(name)

check = list(check)
check.sort(reverse=True)

for i in check:
    print(i)
