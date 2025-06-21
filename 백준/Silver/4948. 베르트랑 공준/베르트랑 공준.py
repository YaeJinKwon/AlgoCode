import sys
import math
input = sys.stdin.readline


while(True):
    n = int(input())
    if(n == 0):
        break
    ans = 0
    for i in range(n+1, (2*n)+1):
        c = 0
        if(i<2):
            continue
        if(i==2):
            ans+=1
            continue
        if(i%2==0):
            continue
        for k in range(2, math.isqrt(i)+1):
            if i%k == 0: 
                c=1
                break
        if (c == 0) : ans +=1
    print(ans)

