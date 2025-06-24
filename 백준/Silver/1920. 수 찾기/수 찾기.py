import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))

a.sort()

for i in find:
    start = 0
    end = n-1
    target = i
    while(start <= end):
        mid = (start+end)//2
        if a[mid] == target:
            print(1)
            break
        elif a[mid] > target:
            end = mid-1
        elif a[mid] < target:
            start = mid+1
    else:
        print(0)