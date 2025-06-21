import sys

input = sys.stdin.readline

s= input().rstrip()

ans = set()

for i in range(len(s)):
    for k in range(i,len(s)):
        ans.add(s[i:k+1]) 

print(len(ans))
