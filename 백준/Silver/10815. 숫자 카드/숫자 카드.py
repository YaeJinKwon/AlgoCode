n = int(input())
arr = list(map(int,input().split()))
arr = set(arr)




m = int(input())
check = list(map(int, input().split()))
ans = []

for i in check:
    if(i in arr):
        ans.append(1)
    else:
        ans.append(0)

print(*ans)
