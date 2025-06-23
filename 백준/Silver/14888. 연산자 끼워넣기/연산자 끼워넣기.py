import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
A = list(map(int,input().split()))
a = []

for i in range(len(A)):
    for _ in range(A[i]):
        a.append(i)

ansMin = 1e9
ansMax = -1e9
v = [0] * (n-1)

def solve(k, ans):
    global ansMax
    global ansMin
    if k == n-1:
        ansMax = max(ans, ansMax)
        ansMin = min(ans, ansMin)
        return
    for i in range(n-1):
        if v[i] == 1:
            continue
        v[i] = 1
        if a[i] == 0:
            newans = ans + arr[k+1]
        elif a[i] == 1:
            newans = ans - arr[k+1]
        elif a[i] == 2:
            newans = ans * arr[k+1]
        elif a[i] == 3:
            if ans < 0:
                newans = -(-ans // arr[k + 1])
            else:
                newans = ans // arr[k + 1]
        solve(k+1,newans)
        v[i] = 0

        
solve(0, arr[0])
print(ansMax)
print(ansMin)
    
