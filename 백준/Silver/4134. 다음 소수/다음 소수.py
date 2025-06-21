import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    while(True):
        count = 0
        if(n < 2):
            n+=1
            continue
        if n == 2:
            print(n)
            break
        if(n%2 == 0) :
            n+=1
            continue

        for i in range(2,int(math.isqrt(n))+1):
            if(n%i == 0):
                count+=1
            if(count >= 1):
                break
        if (count == 0):
            print(n)
            break
        n +=1