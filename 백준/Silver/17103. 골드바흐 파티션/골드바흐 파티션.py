import sys, itertools
input = sys.stdin.readline


prime = [1] * 1000001
prime[0] = prime[1] = False
for i in range(2, int(1000001 ** 0.5)+1):
    if prime[i]:
        for j in range(i*i, 1000001, i):
                prime[j] = False

t = int(input())

for _ in range(t):
    c= 0
    n = int(input())
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
             c +=1
    print(c)




