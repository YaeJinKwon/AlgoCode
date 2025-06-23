import sys, math

input = sys.stdin.readline

n = int(input())

S =[]

for _ in range(n):
    a = list(map(int,input().split()))
    S.append(a)

minTotal = 1e9
def sol(i, arr, s):
    global minTotal
    if i == n//2:
        arr1 = []
        for i in range(n):
            if i in arr:continue
            arr1.append(i)

        c1 = 0
        for i in arr:
            for j in arr:
                c1 += S[i][j]
        
        c2 = 0
        for i in arr1:
            for j in arr1:
                c2 += S[i][j]
        minTotal = min(minTotal, abs(c1 - c2) )
        return
    for k in range(s, n):
        arr.append(k)
        sol(i+1, arr, k+1)
        arr.pop()

sol(0, [], 0)
print(minTotal)