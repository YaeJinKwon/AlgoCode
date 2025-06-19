n = int(input())

ans = []
for i in range(n//5 + 1):
    tempN = n - 5*i
    cnt = i
    cnt += tempN//3
    tempN = tempN%3
    if(tempN==0):
        ans.append(cnt)

if len(ans) == 0:
    print(-1)
else : print(min(ans))
