import sys

input = sys.stdin.readline

n = int(input())
data = []
data.append(0)
for _ in range(n):
    data.append(int(input()))

if(n==1):
    print(data[1])
elif(n==2):
    print(data[1]+data[2])
elif(n==3):
    dp = [0] *(n+1)
    dp[0] = 0
    dp[1] = data[1]
    dp[2] = data[1]+data[2]
    dp[3] = max(data[2]+dp[0], dp[1])+data[3]
    print(max(dp))
else:
    dp = [0] *(n+1)
    dp[0] = 0
    dp[1] = data[1]
    dp[2] = data[1]+data[2]
    dp[3] = max(data[2]+dp[0], dp[1])+data[3]
    for i in range(4,n+1):
        dp[i] = max(data[i-1]+dp[i-3],dp[i-2] ,dp[i-4]+data[i-1])+data[i]



    print(max(dp))
