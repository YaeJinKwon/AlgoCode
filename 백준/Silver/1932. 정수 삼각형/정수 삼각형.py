import sys

input = sys.stdin.readline

t = int(input())
data = []
for _ in range (t):
    data.append(list(map(int,input().split())))

dp = [[0] * i for i in range(1,t+1)]


dp[0][0] = data[0][0]
for i in range(1, t):
    for k in range(0,i+1):
        if(k == 0):
            dp[i][k] = data[i][k]+dp[i-1][0]
            continue
        if(k == i):
            dp[i][k] = data[i][k]+dp[i-1][-1]
            continue
        dp[i][k] = max(dp[i-1][k], dp[i-1][k-1]) + data[i][k]


print(max(dp[t-1]))
