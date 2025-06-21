import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

arr = deque()
for i in range(1, n+1):
    arr.append(i)


ans = []
count = 0 
while arr:
    count +=1
    if count == k:
        ans.append(arr.popleft())
        count = 0
    else : arr.append(arr.popleft())

print('<', end="")
print(*ans, sep=', ', end ='>')


