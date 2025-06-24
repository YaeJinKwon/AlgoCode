import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

def check1(i,j,n):
    for k in range(i, i+n):
        for l in range(j, j+n):
            if arr[k][l] == 1:
                return False
    return True


def dfs1 (i, j, n):
    global ans1
    if(check1(i ,j,n)):
        ans1 +=1
        return
    if(n==1):
        return
    dfs1(i ,j, n//2)
    dfs1(i,j+n//2,n//2)
    dfs1(i+ n//2, j,n//2)
    dfs1(i+n//2,j+ n//2,n//2)


def check2(i,j,n):
    for k in range(i, i+n):
        for l in range(j, j+n):
            if arr[k][l] == 0:
                return False
    return True


def dfs2 (i, j, n):
    global ans2
    if(check2(i ,j,n)):
        ans2 +=1
        return
    if(n==1):
        return
    dfs2(i ,j, n//2)
    dfs2(i,j+n//2,n//2)
    dfs2(i+ n//2, j,n//2)
    dfs2(i+n//2,j+ n//2,n//2)

ans1 = 0
ans2 = 0

dfs1(0,0,n)
dfs2(0,0,n)

print(ans1)
print(ans2)