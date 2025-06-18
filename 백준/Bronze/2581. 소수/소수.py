m = int(input())
n = int(input())

total = 0
minN = 10000
for i in range(m, n+1):
    if i < 2:
        continue
    if i > 3 and i % 2 == 0:
        continue
    temp = 0
    for k in range(2,i+1):
        if i % k == 0:
            temp +=1
    if temp == 1:
        total += i
        minN = min(minN, i)

if(total == 0):
    print(-1)
else:
    print(total)
    print(minN)