import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

def check(i, j, size):
    color = arr[i][j]
    for k in range(i, i+size):
        for l in range(j, j+size):
            if arr[k][l] != color:
                return False
    return True

ans = [0]*3
def dfs(i,j,size):
    if(check(i,j,size)):
        if arr[i][j] == -1:
            ans[0]+=1
        elif arr[i][j] == 0:
            ans[1]+=1
        elif arr[i][j] == 1:
            ans[2]+=1
        return
    for k in range(3):
        for l in range(3):
            dfs(i+k*(size//3), j+l*(size//3), size//3)

dfs(0,0,n)
print(ans[0])
print(ans[1])
print(ans[2])