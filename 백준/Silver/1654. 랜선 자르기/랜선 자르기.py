import sys

input = sys.stdin.readline

K, N = map(int,input().split())
arr = []

for _ in range(K):
    arr.append(int(input()))

start = 0
end =  max(arr)
ans = []
while(start <= end):
    if(start + end == 1):
        ans.append(1)
        break
    mid = (start + end)//2
    count = 0
    for i in arr:
        count += i // mid
    if count == N:
        ans.append(mid)
        start= mid+1
    elif count < N:
        end = mid-1
    else:
        ans.append(mid)
        start= mid+1

print(max(ans))
        