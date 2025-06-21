import sys

input = sys.stdin.readline

s= input().rstrip()

ans = set()

for i in range(len(s)):
    for k in range(1,len(s)+1):
        ans.add(s[i:k]) 

print(len(ans)-1)
