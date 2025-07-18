import sys

input = sys.stdin.readline

t = int(input())
arr = []

for _ in range(t):
    arr.append(int(input()))
if t == 1:
    print(arr[0])
elif t == 2:
    print(arr[0]+arr[1])
else:
    dp = [0]*(t+1)
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[1]+arr[2], arr[0]+arr[2])
    for i in range(3, t):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    print(dp[t-1])