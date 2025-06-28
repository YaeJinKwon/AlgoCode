import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))





count = 0
sum = 0

arr.sort()

left = 0
right = n-1
ans = []
while(left<right):
    sum = arr[left]+arr[right]
    ans.append((abs(sum), arr[left],arr[right]))
    if(sum == 0):
        print(arr[left], arr[right])
        break
    elif(sum < 0):
        left+=1
    elif(sum > 0):
        right-=1

ans.sort()
print(ans[0][1],ans[0][2])

