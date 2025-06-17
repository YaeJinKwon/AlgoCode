t = int(input())

for _ in range(t):
    money = int(input())
    
    ans = []
    c = [25, 10, 5, 1]
    for i in c:
        ans.append(money // i)
        money = money % i
    print(ans[0], ans[1], ans[2], ans[3])
    
    
