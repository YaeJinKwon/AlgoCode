import sys
input = sys.stdin.readline


n = int(input())
col = [0] * n
v1 = [0]*n
v2 = [0]*2*n
v3 = [0]*2*n
ans = 0
def nqueen(i):
    global ans
    if i == n:
        ans += 1
        return
    for k in range(n):
        col[i] = k
        if v1[k] == 0 and v2[i-k] == 0 and v3[i+k] == 0:
            v1[k] = 1
            v2[i-k] = 1
            v3[i+k] =1
            nqueen(i+1)
            v1[k] = 0
            v2[i-k] = 0
            v3[i+k] =0


nqueen(0)
print(ans)