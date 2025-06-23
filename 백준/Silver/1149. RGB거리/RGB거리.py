import sys

input = sys.stdin.readline

t = int(input())
data = []
for _ in range (t):
    data.append(list(map(int,input().split())))

dp = [[0] * 3 for _ in range(t)]

dp[0][0] = data[0][0]
dp[0][1] = data[0][1]
dp[0][2] = data[0][2]

for i in range(1, t):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + data[i][2]

print(min(dp[t-1]))
