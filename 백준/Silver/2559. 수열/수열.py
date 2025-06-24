import sys

input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))
total = []
total.append(0)
tmp = 0
for i in arr:
    total.append(i+tmp)
    tmp += i
ans = -1e9
for i in range(k, n+1):
    ans = max(total[i]-total[i-k],ans)

print(ans)