
white = [[0]*100 for _ in range(100)]

n = int(input())

for _ in range(n):
    i, j = map(int, input().split())
    for x in range(10):
        for y in range(10):
            white[i+x][j+y] = 1

count = 0
for x in range(100):
    for y in range(100):
        if white[x][y] == 1:
            count += 1

print(count)