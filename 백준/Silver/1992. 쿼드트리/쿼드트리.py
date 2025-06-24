import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().rstrip())))

def check(i, j, size):
    color = arr[i][j]
    for k in range(i, i+size):
        for l in range(j, j+size):
            if arr[k][l] != color:
                return False
    return True
ans = []
def dfs(i,j,size):
    if(check(i,j,size)):
        ans.append(str(arr[i][j]))
        return
    ans.append('(')
    dfs(i,j, size//2)
    dfs(i, j+size//2,  size//2)
    dfs(i+size//2, j,  size//2)
    dfs(i+size//2, j+size//2,  size//2)
    ans.append(')')

dfs(0,0,n)
print("".join(ans))