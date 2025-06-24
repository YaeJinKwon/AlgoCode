import sys

input = sys.stdin.readline

n, k = map(int,input().split())

money = []

for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)

ans  = 0
for i in money:
    if i > k:
        continue
    ans += k//i
    k = k%i
print(ans)