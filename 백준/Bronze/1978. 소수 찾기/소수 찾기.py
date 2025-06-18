
n = int(input())

array = list(map(int, input().split()))
ans = 0
for i in array:
    if i < 2:
        continue
    temp = 0
    for k in range(1,i+1):
        if i % k == 0:
            temp +=1
    if temp == 2:
        ans +=1


print(ans)