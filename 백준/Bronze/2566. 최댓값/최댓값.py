maxNum = 0
ni = 0
nj = 0
for i in range(9):
    array = (list(map(int, input().split())))
    maxNum = max(maxNum, max(array))
    if maxNum == max(array):
        ni = i + 1
        nj = array.index(maxNum) + 1

print(maxNum)
print(ni, nj)
