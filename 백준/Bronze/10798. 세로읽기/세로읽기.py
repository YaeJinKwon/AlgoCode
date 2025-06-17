array = []
maxL = 0
for i in range(5):
    array.append(list(map(str, input())))
    maxL = max(maxL, len(array[i]))
ans = []
for i in range(maxL):
    for k in range(5):
        if(len(array[k]) <= i ):
            continue
        ans.append(array[k][i])

print("".join(ans))