n = int(input())

x = []
y = []

for _ in range(n):
    i, j = map(int, input().split())
    x.append(i)
    y.append(j)

print((max(x)- min(x)) * (max(y)- min(y)))