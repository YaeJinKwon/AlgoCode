import sys

input = sys.stdin.readline

t = int(input())
dp = [0]* (t+1)

for i in range (2, t+1):
    dp[i] = dp[i-1] + 1
    if (i%3==0):
        dp[i] = min(dp[i//3]+1, dp[i])
    if(i%2==0):
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[t])
