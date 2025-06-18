a, b, c, d, e, f = map(int,input().split())


for i in range(-999, 1000):
    for k in range(-999, 1000):
        if ((a*i + b*k == c) and(d*i + e*k == f)):
            print(i, k)
            break
