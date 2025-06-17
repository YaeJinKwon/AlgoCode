a = input().split()
ans = []
for i in a:
    new = i[2]+i[1]+i[0]
    ans.append(int(new))

print(max(ans))
