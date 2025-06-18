x = []
y = []

for _ in range(3):
    i, j = map(int,input().split())
    x.append(i)
    y.append(j)

ansx = 0
ansy = 0

for i in x:
    if(x.count(i) == 1):
        ansx = i
        break

for i in y:
    if(y.count(i) == 1):
        ansy = i
        break

print(ansx, ansy)