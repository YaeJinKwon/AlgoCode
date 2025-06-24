import sys

input = sys.stdin.readline

s = input().rstrip().split('-')
num = []
for i in range(len(s)):
    a = list(map(int, s[i].split('+')))
    for j in a:
        if i == 0:
            num.append(j)
        else:
            num.append(-j)
print(sum(num))
