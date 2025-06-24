import sys

input = sys.stdin.readline

n = int(input())

time = list(map(int,input().split()))

time.sort()
ans = 0
total =0

for i in range(n):

    ans = ans+time[i]
    total += ans

print(total)