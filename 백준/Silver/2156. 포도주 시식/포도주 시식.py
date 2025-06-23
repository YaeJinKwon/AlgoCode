import sys

input = sys.stdin.readline

n = int(input())
data = []
data.append(0)
for _ in range(n):
    data.append(int(input()))


if n == 1:
    print(data[1])
    exit()

dp = [0] * (n + 1)
dp[1] = data[1]
if n >= 2:
    dp[2] = data[1] + data[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-1], dp[i-2]+ data[i] ,dp[i-3]+data[i-1]+data[i])



print(dp[n])