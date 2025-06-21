import sys
input = sys.stdin.readline

n = int(input())

s = set()
ans = 0
for _ in range (n):
    data = input().rstrip()
    if data == "ENTER":
        s = set()
        continue
    if data not in s:
        s.add(data)
        ans +=1
print(ans)
