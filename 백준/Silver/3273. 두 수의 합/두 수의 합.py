import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())




count = 0
sum = 0

arr.sort()

left = 0
right = n-1
while(left<right):
    sum = arr[left]+arr[right]
    if(sum == x):
        count+=1
        left+=1
        right-=1
    elif(sum < x):
        left+=1
    elif(sum>x):
        right-=1


print(count)