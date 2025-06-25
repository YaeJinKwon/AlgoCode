import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

arr = [0]
for i in data:
    if arr[-1] < i:
        arr.append(i)
    elif arr[-1] > i:
        start = 0
        end = len(arr)
        while(start<=end):
            mid = (start + end)//2
            if arr[mid] < i:
                start = mid +1
            else:
                end = mid-1
        arr[start] = i

print(len(arr)-1)