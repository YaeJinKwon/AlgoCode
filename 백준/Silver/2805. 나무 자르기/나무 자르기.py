import sys

input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int,input().split()))


start = 0
end = max(arr)

ans = 0
while(start <= end):
    count = 0
    mid = (start+end)//2
    for i in arr:
        if i > mid:
            count += i - mid
    if count >= M:
        ans = mid
        start = mid +1
    else:
        end = mid-1

print(ans)
