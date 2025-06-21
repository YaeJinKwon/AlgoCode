import sys
import math
input = sys.stdin.readline

m, n = map(int, input().split())

for i in range(m, n+1):
    if i<2:
        continue
    if i == 2:
        print(i)
        continue
    c =0
    for k in range(2,int(math.isqrt(i)+1)):
        if (i%k==0) :
            c = 1
            break
    if(c== 0):
        print(i)