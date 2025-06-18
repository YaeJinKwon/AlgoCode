n = int(input())

ans = 1000000
for i in range(1, n):
    s = i
    for k in str(i):
        s += int(k)
    if s == n:
        ans = min(ans,i)
if(ans == 1000000):
    print(0)
else : print(ans)