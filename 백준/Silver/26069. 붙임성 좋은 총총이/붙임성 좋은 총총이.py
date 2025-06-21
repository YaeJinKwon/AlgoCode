import sys
input = sys.stdin.readline

n = int(input())

s = set()
ans = 0
for _ in range (n):
    data = input().rstrip().split()
    if data[0] == "ChongChong" or data[1] == "ChongChong":
        s.add(data[0])
        s.add(data[1])
    if data[0] in s or data[1] in s:
        s.add(data[0])
        s.add(data[1])

print(len(s))
