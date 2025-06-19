import sys
input = sys.stdin.readline
n = int(input())

ans = [0]*10001

for _ in range(n):
    i = int(input())
    ans[i] += 1 

for i in range(10001):
    if(ans[i] == 0):
        continue
    else:
        for _ in range(ans[i]):
            print(i)